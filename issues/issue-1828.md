---
title: Wallet sync - upgrade to 64 bit arithmetics and streamlining blockchain scan
source_url: https://github.com/monero-project/monero/issues/1828
author: fireice-uk
assignees: []
labels:
- proposal
created_at: '2017-03-02T16:28:02+00:00'
updated_at: '2018-01-13T11:51:10+00:00'
type: issue
status: closed
closed_at: '2018-01-13T11:51:10+00:00'
---

# Original Description
### Summary
By replacing the large integer arithmetic functions in the crypto library with the amd64-64-24k implementation, I managed to raise single threaded scanning performance, using extracted blockchain data, on my cpu from 3200 I/s (indices per second) to 5500 I/s. Furthermore I identified poor cpu utilisation when scanning with the wallet. Full blockchain scan on the same cpu took 30 minutes, against expected 20 minutes based on the single threaded "bare metal" scanner.

By upgrading to the faster scanning algorithm and addressing the causes of cpu under-utilisation, we can shorten the full blockchain scan to under 10 minutes. This will eliminate the need for shortcuts such as scanning only some blocks or some transactions.

### Arbitrary precision arithmetic vs cryptography
Cryptographic functions and algorithms in Monero will remain unchanged. While an essential component of every asymmetric algorithm, arbitrary precision maths is simple to write and verify. Most complex operations will be familiar to anybody who completed primary school maths  - add, multiply, square. As such it is fairly easy to verify correctness of the implementation.

### Bandwidth utilisation
Following the feedback, I decided to spilt the bandwidth streamlining into another proposal. Scanning at current speed requires around 2MB/s of network bandwidth, and after eliminating CPU bottlenecks I would expect it to require in the ballpark of 8MB/s bandwidth, so full speed sync will be only possible on loopback and LAN.

### CPU utilisation
As per my benchmark, current wallet is not even scanning at the theoretical single core speed. There is huge room for improvement if we switch to more efficient data structures.

# Discussion History
## danrmiller | 2017-03-02T16:32:28+00:00
Can you link the code for the faster implementation?

## fireice-uk | 2017-03-02T16:40:23+00:00
The implementation written by Dr. Bernstein et al. - https://bench.cr.yp.to/supercop/supercop-20170228.tar.xz 

For the sake of modifying the existing algorithms as little as possible (it was a large point in the feedback to the previous draft), i only replaced the fe_* functions in crypto-ops.c

## vtnerd | 2017-03-02T17:58:18+00:00
@luigi1111 - who had a concern of network forks (i.e. not all nodes would be verifying signatures with the same code since this is ASM for x86-64 only). Using this for wallet code would not have such issues, but we'd have to figure out how to have both in existence.

The faster scanning algorithm - does it use the existing RPC mechanism but with less data? I dislike these types of general purpose deserialization routines because they copy data to a separate buffer even if the caller is going to ignore it (i.e. range proofs copied from raw network buffer to another series of heap allocated objects). Protobuf has the exact same annoyance. So its often not that the TCP overhead of the extra data, but the CPU savings by the recipient. Have you been able to determine how much of each in this situation? There are lots of improvements to be made on the serialization/deserialization code (multiple copies to temporary buffers and other oddities). If you hacked together a new RPC call that skipped these routines altogether, the results are going to be a bit distorted to what can be achieved with the existing RPC calls, but a good indicator of how much improvement can be made in that underlying framework. 

EDIT: These types of general purpose deserialization routines refers to the ones monero is currently using, not your unspecified technique.

## ghost | 2017-03-02T20:40:24+00:00
I would really appreciate @RandomRun input

## fireice-uk | 2017-03-02T21:13:54+00:00
#### Fork risk
While the code is strictly needed only in the wallet implementation, there needs to be some thought whether it won't be useful to have two algorithms checking each other. If sig32(x)  != sig64(x) for any x then we have _much_ bigger problems than just a fork, IMO it would be a useful canary in that case.

#### Technique for the benchmark
The current code is running with a dump of the relevant TX data to a static file. I was only interested in CPU performance at this stage.

#### Live RPC performance
Scanning is a batch, not an interactive process. Is there any reason why we can't have a single buffered fetcher and a worker for every CPU core? Other than taking timing and atop measurements during sync. and confirming that the current code somehow manages not to max out anything, I haven't taken a detailed look at what's actually happening there.


## vtnerd | 2017-03-02T22:51:32+00:00
> **Fork risk**
>
> While the code is strictly needed only in the wallet implementation, there needs to be some thought whether it won't be useful to have two algorithms checking each other. If sig32(x) != sig64(x) for any x then we have much bigger problems than just a fork, IMO it would be a useful canary in that case

Some odd wording ("won't be useful"), but yes it could be useful in that sense.


> **Technique for the benchmark**
>
>The current code is running with a dump of the relevant TX data to a static file. I was only interested in CPU performance at this stage.

Ok, so this tells us that we could theoretically eliminate ~10mins (on your system) from the scan time by reducing the wait time for the cryptographic calls.


> **Live RPC performance**
>
> Scanning is a batch, not an interactive process. Is there any reason why we can't have a single buffered fetcher and a worker for every CPU core? 

The only reason is integration effort within the existing code. Pre-fetching elements will definitely reduce latencies, but the only immediate option (AFAIK) is firing up a temporary thread. In this particular case, if a "long sync" can be determined, a `common/thread_group.h` / `common/task_region.h` would allow for 1+ fetching threads to be re-used and then "joined" at every response completion. Doing much else is probably pointless in the short term, since HTTP-RPC is being replaced with a ZMQ implementation.

Long term some system-wide asynchronous request system would be nice. Background fetching could be used more since it didn't have to overcome thread creation cycles. The asynchronous part isn't strictly necessary, but has better thread usage efficiency. Of course overall throughput will drop (synchronous performance is hard to beat),  but many of these operations are not concerned about maximizing bulk data transfers.

## fireice-uk | 2017-03-03T00:39:53+00:00
I was actually more ambitious here, I was thinking of starting n+1 threads "a single buffered fetcher and a worker for every CPU core" and a simple 1-producer-n-consumers design pattern. It won't be implementation dependant (all the HTTP -> ZMQ changes will go in the producer), and it should solve whatever bottlenecks are there.

## fireice-uk | 2017-03-03T00:57:35+00:00
Regarding the 7.5 minute figure - that comes from the theoretical benchmark and an assumption that we will use 1.5 cores of a dual core cpu (with other half being taken up by fetching and unserialising data) 

## vtnerd | 2017-03-03T04:41:34+00:00
I think I have a rough idea of what you are proposing, which is why I pointed to the thread_group / task_regions code. It will be dead simple to start up N threads, and then spawn parallel fetch and compute tasks on those threads. I would expect the dead simple implementation to have some slight CPU underutilization, but I am not sure that its worth chasing that last few percentage immediately. I would not expect a producer queuing design to have a significant amount of additional work though - couple of locks, notifiers, and a queue.

My other ramblings about ZMQ were a bit forward looking to `monero-wallet-rpc`, which shares code lots of code with `monero-wallet-cli`. `monero-wallet-rpc` is both a client and server, and the server portion is currently single threaded. Luckily, few (if any) users are running multiple clients to `monero-wallet-rpc`. But if @hyc goes all crazy and allows multiple accounts per wallet, then this may change some usage patterns. The server is likely to remain single threaded for a while though.

## vtnerd | 2017-03-03T05:01:13+00:00
Also, I should specify that the current code is (possibly) creating a series of threads for each transaction. So dead-simple is possibly a stretch - some refactoring across the relevant functions would be necessary too.

## vtnerd | 2017-03-03T05:04:06+00:00
> Regarding the 7.5 minute figure - that comes from the theoretical benchmark and an assumption that we will use 1.5 cores of a dual core cpu (with other half being taken up by fetching and unserialising data)

Was the benchmark doing the same "work" as the current wallet functions, or only inspecting output addresses?

## fireice-uk | 2017-03-03T13:06:54+00:00
As I said in the OP, it scans all the indices and gives us how many of them belong to the given private viewkey (let's say x), unless I'm wildly mistaken here, all the other jobs after that are proportional to x rather than total transactions on the blockchain. 

## fireice-uk | 2017-03-03T13:21:26+00:00
Ah, if you are thinking of checking Is then that's O(xlog n) where n is the total number of transactions.

## vtnerd | 2017-03-04T00:43:14+00:00
Ok, so these benchmark numbers seem to be under "ideal" conditions. For instance, the current implementation checks for reorgs. There might more necessary checks that I am not aware of. I recommended thread_group / task_region simply because it should be easier to speedup the existing implementation which is creating/destroying many threads. And I doubt anyone will argue against you doing additional optimization work since your description _should_ be possible without massive alterations.

As for the crypto, my recommendation would be to put the x86-64 ASM in `src/wallet`, then provide alternate functions whose names clearly indicate they are for wallet import only (for the reasons discussed above). When Cmake detects a non x86-64 target, forward to the code in `src/crypto`. Then `tests/unit_tests` between the two. There will be some duplication in logic, but it seems safest for the reasons above. And most importantly I am not speaking for the monero project - @luigi1111 @hyc @iamsmooth @kenshi84 @moneromooo-monero @anonimal (who else?) may have some feedback.

I would also like to point out [neon2 scalar multiplication ASM](https://bench.cr.yp.to/impl-scalarmult/curve25519.html), written by DJB and Peter Schwabe. This should speed up the ECDH portion of the address scanning on relevant arm processors. The neon2 ASM is also **not** in NaCL, and unlike the x86-64 ASM, there is no indication that it will be included. Furthermore, libsodium does **not** appear to be using the x86-64 ASM nor neon2 ASM.

## fireice-uk | 2017-03-05T14:00:42+00:00
If creating special version of the crypto code just for the scan is the way you want to do it, I'm more than happy to do it this way.

There doesn't seem to be any vocal opposition, so I will try to draft FFS on Monday.

## ghost | 2017-03-06T13:27:14+00:00
I'm just going to log a warning now. I predict that this is going to result in drama down the line. It is a major change you're proposing and you haven't once stepped foot into the dev channel on IRC or Slack to discuss this. 

I predict you will raise funding, then work on it, then it won't go right for some reason or another, and you'll complain all over Reddit when the funds aren't released. 

I hope you prove me wrong, but I want the ability to look back and say 'I told you so'. 

## fireice-uk | 2017-03-06T13:50:28+00:00
This way of doing it has apparently been okay'ed by the big man himself ( [1](https://www.reddit.com/r/Monero/comments/5wc2th/a_proposal_to_speed_up_wallet_sync_around_5x/de9upt5/) ). And I'm sure all the core developers had a chance to read it. What else can I do if they chose not to respond?

As with regards to funds not being released, I'm prepared to work with them and give them the benefit of doubt. I like Monero and I want this to work. 

## fluffypony | 2017-03-06T13:55:48+00:00
Ultimately, funds are released when milestones are hit, but deciding if a milestone is hit is up to the community at large (including fellow developers and less-technical observers). The easiest way to avoid issues is just to make the milestones as objective as possible. Sometimes the subjective stuff is hard ("produce well-documented code", for instance) and should not form part of a separate milestone, but of the over-arching goals.

## fireice-uk | 2017-03-06T13:58:24+00:00
That was my thinking exactly, I'm doing a draft for FFS right now, so I will post it in an hour or two.

## fireice-uk | 2017-03-06T14:41:58+00:00
https://forum.getmonero.org/6/ideas/87580/cutting-wallet-sync-time

## kenshi84 | 2017-03-06T14:55:56+00:00
@vtnerd I wish I could make some comments here, but this kind of code optimization stuff is just beyond my ability :P
I'm curious to see how this proposal develops :)

## danrmiller | 2017-03-06T16:56:39+00:00
Is the main concern that using non-constant time functions might get used somewhere else in the code where it could leak timing? Is there agreement that its safe here? What can be done to reduce the risk?

The other concern I saw was potential platform-specific implementation differences, which I think you responded could be viewed as a beneficial "cross-check".


## fireice-uk | 2017-03-06T17:03:29+00:00
That was in the feedback to my very first draft - as this only gives a very minor performance improvement in comparison to 64 bit integers, I simply dropped it.

My opinion on the matter is that there are only two specific situations that I can see timing information to be of any use - hardware wallets and wallets running on vps.

## moneromooo-monero | 2017-03-06T20:16:31+00:00
>  And I'm sure all the core developers had a chance to read it. What else can I do if they chose not to respond?

The rough goals in the first post are fine, assuming I read correctly as being (1)  use 64 bit ops where possible, and (2) better use of hardware parallelism. The devil is in the details, and some optimizations may not be worth any particular drawbacks. This will be seen in the actual patches, so I have not much to say right now.


## fireice-uk | 2017-03-06T21:34:43+00:00
Of course, I assume there will be plenty of feedback once you can look at the actual code. Right now the aim is to get this project off the ground and funded.

## vtnerd | 2017-03-07T15:37:00+00:00
> Is the main concern that using non-constant time functions might get used somewhere else in the code where it could leak timing? Is there agreement that its safe here? What can be done to reduce the risk?

The functions were written by cryptographers for usage in cryptographic situations. The implementations should be constant time. The primary concern is that the implementation will only work on 64-bit x86 based chips (newer Intel and AMD). With different implementations, the possibility exists that a subtle difference could cause some machines to reject a tx as having an invalid signature, with other machines accepting the same tx (network fork).

---------------

> The rough goals in the first post are fine, assuming I read correctly as being (1) use 64 bit ops where possible, and (2) better use of hardware parallelism. The devil is in the details, and some optimizations may not be worth any particular drawbacks. This will be seen in the actual patches, so I have not much to say right now.

Agreed. IMO, funding a performance patch is going to be more problematic than a feature patch. The ASM is highly likely to be improve performance though, it is already open source and has been benchmarked. Which makes this somewhat awkward to to fund too since the code is available. Individuals will just have to take this into consideration when making their decision.

------------
> My opinion on the matter is that there are only two specific situations that I can see timing information to be of any use - hardware wallets and wallets running on vps.

Did you mean nodes running on vps? I do not recommend running a wallet on vps. And actually I wouldn't run my node on a vps either. The latency work _should_ be helpful for people doing vps node -> desktop wallet.

## vtnerd | 2017-03-07T15:50:47+00:00

>>  Is the main concern that using non-constant time functions might get used somewhere else in the code where it could leak timing? Is there agreement that its safe here? What can be done to reduce the risk?
>
> The functions were written by cryptographers for usage in cryptographic situations. The implementations should be constant time. The primary concern is that the implementation will only work on 64-bit x86 based chips (newer Intel and AMD). With different implementations, the possibility exists that a subtle difference could cause some machines to reject a tx as having an invalid signature, with other machines accepting the same tx (network fork).

I forgot to mention that AFAIK, this x86-64 implementation is not currently used in any cryptographic library. The NaCL pages state the code will be used in the next version, but whether there are changes between the benchmark code and the final version is not yet known.

## hyc | 2017-03-07T17:24:28+00:00
Lee Clagett wrote:
>     Is the main concern that using non-constant time functions might get used
>     somewhere else in the code where it could leak timing? Is there agreement
>     that its safe here? What can be done to reduce the risk?
>
> The functions were written by cryptographers for usage in cryptographic
> situations. The implementations should be constant time. The primary concern
> is that the implementation will only work on 64-bit x86 based chips (newer
> Intel and AMD). With different implementations, the possibility exists that a
> subtle difference could cause some machines to reject a tx as having an
> invalid signature, with other machines accepting the same tx (network fork).
>
> ------------------------------------------------------------------------------
>
>     The rough goals in the first post are fine, assuming I read correctly as
>     being (1) use 64 bit ops where possible, and (2) better use of hardware
>     parallelism. The devil is in the details, and some optimizations may not
>     be worth any particular drawbacks. This will be seen in the actual
>     patches, so I have not much to say right now.
>
> Agreed. IMO, funding a performance patch is going to be more problematic than
> a feature patch. The ASM is highly likely to be improve performance though, it
> is already open source and has been benchmarked. Which makes this somewhat
> awkward to to fund too since the code is available. Individuals will just have
> to take this into consideration when making their decision.

Ditto. Promising XX% speedup is unrealistic, and people will have a legitimate 
right to complain if a specific number is in the FFS proposal but users don't 
see it in their own use. On the other hand, the current proposal doesn't 
mention *any* speedup at all. So all of this work could be done and wind up 
yielding 0% improvement and it will be considered to have been completed 
successfully. Pointless in that case. People need to know what they're buying 
here - why is this work worth doing, what range of improvement can be expected 
in real world use?

-- 
   -- Howard Chu
   CTO, Symas Corp.           http://www.symas.com
   Director, Highland Sun     http://highlandsun.com/hyc/
   Chief Architect, OpenLDAP  http://www.openldap.org/project/


## hyc | 2017-03-07T17:27:09+00:00
Lee Clagett wrote:
>     Is the main concern that using non-constant time functions might get used
>     somewhere else in the code where it could leak timing? Is there agreement
>     that its safe here? What can be done to reduce the risk?
>
> The functions were written by cryptographers for usage in cryptographic
> situations. The implementations should be constant time. The primary concern
> is that the implementation will only work on 64-bit x86 based chips (newer
> Intel and AMD). With different implementations, the possibility exists that a
> subtle difference could cause some machines to reject a tx as having an
> invalid signature, with other machines accepting the same tx (network fork).

There's an old proverb - "a man with two watches never knows what time it is."

-- 
   -- Howard Chu
   CTO, Symas Corp.           http://www.symas.com
   Director, Highland Sun     http://highlandsun.com/hyc/
   Chief Architect, OpenLDAP  http://www.openldap.org/project/


## moneromooo-monero | 2017-03-07T19:13:47+00:00
I think the best is to have testable performance thresholds. This way, it is objectively testable, and the bound can be set to a level that the author knows can be achieved. Too high will attract suckers but risk failing, too low will just fail to interest.

Good point on potential difference between 32 and 64 bit code. If there's going to be a 64 bit asm implementation from NaCl, and if we're going to switch anyway (IIRC that's what fluffypony had in mind as the best target), then it would make sense to wait and use that instead, to get all the validation and testing, and keep any changes to just CPU and I/O utilization improvements.
I'd forgot about the crypto lib changes, so that should be hashed out first, before optimizing something which might become moot when this is done.

## fireice-uk | 2017-03-07T22:02:37+00:00
> I think the best is to have testable performance thresholds. This way, it is objectively testable, and the bound can be set to a level that the author knows can be achieved. Too high will attract suckers but risk failing, too low will just fail to interest.

That wouldn't be a problem - with the obvious caveat that we are not writing a miner here, slower but clear code is better than faster and obfuscated. Let's formally define it and see if you are happy.

For a quad-core system with 8 available threads, which is hosting a wallet only, and connects to a daemon over 1Gbit LAN. Let's say that x is equal to the current full sync time (scanning every tx).

For Milestone 1:
- Scan time will be 0.75x or less, as long as the daemon is able to serve the wallet at sufficient speed.

For Milestone 2:
- Scan time will be 0.5x or less, as long as the daemon is able to serve the wallet at sufficient speed.

This is a fairly modest target (I prefer to under-promise and over-deliver than the other way round), and it still guarantees that we will double the performance.

> If there's going to be a 64 bit asm implementation from NaCl

The amd64-64-24k lib implements all the critical operations in asm. After a quick glance at them, there is very little room for further optimisation. There might be some in the ge_* family of functions, however I wouldn't feel qualified to mess with those.

## fireice-uk | 2017-03-08T01:39:21+00:00
@vtnerd 
>Did you mean nodes running on vps? I do not recommend running a wallet on vps. And actually I wouldn't run my node on a vps either. The latency work should be helpful for people doing vps node -> desktop wallet.

I actually did mean wallets. Most people go "oooh side-channel attack" while forgetting that you usually need to be so close to the physical hardware that rootkiting and stealing the key is like taking a candy from a baby.

## danrmiller | 2017-03-08T05:20:01+00:00
Lee Clagett wrote:
> The primary concern is that the implementation will only work on 64-bit x86 based chips (newer Intel and AMD). With different implementations, the possibility exists that a subtle difference could cause some machines to reject a tx as having an invalid signature, with other machines accepting the same tx (network fork).

That's a serious concern for a concern for a consensus system like this. I think TweetNaCl is being looked at partly because it's hopefully less painful to audit and validate. So moneromooo-monero's suggestion to wait and use that makes sense.

## fireice-uk | 2017-03-08T11:16:54+00:00
@danrmiller I think we already addressed that concern. Unless you are saying that the wallet code can cause a fork somehow?

## vtnerd | 2017-03-08T15:21:53+00:00
>> Did you mean nodes running on vps? I do not recommend running a wallet on vps. And actually I wouldn't run my node on a vps either. The latency work should be helpful for people doing vps node -> desktop wallet.
>
> I actually did mean wallets. Most people go "oooh side-channel attack" while forgetting that you usually need to be so close to the physical hardware that rootkiting and stealing the key is like taking a candy from a baby.

I was not thinking of any side-channel attacks. If someone is putting their spend keys on the VPS then the owner of that hardware has access to it. A single employee of that VPS provider that knew a sizeable amount of XMR was for the taking could do some damage. There is no "reversing" the transaction, and even traceability is going to be difficult.

## fireice-uk | 2017-03-08T16:34:52+00:00
@vtnerd Exactly. Just to clarify, timing attack (that we are droning on about here) is one of the possible side-channel attacks. 

## fireice-uk | 2017-03-10T14:59:17+00:00
@fluffypony I think everyone had a chance to comment. Can we move the project to the funding stage?

## fireice-uk | 2017-03-17T12:33:17+00:00
@fluffypony Ok. I get the message. So much for "community" funding system.

## ghost | 2017-03-20T04:40:37+00:00
@fireice-uk Fluffy's a busy dude. And this change to the central Monero software seems like it's a major one, which means it's going to move extra slow. Overall, I'd just suggest patience. Many people, including myself, are excited by this proposal and hope it materializes in a manner that satisfies everybody. Right now the bull's eye seems centered on the current point release.

## fireice-uk | 2017-03-21T22:47:26+00:00
@xmr-eric Don't worry, I will wait.

## anonimal | 2017-03-22T02:40:25+00:00
No code samples (implementation complete, using supercop) for this at least a small portion of this proposal?

## fireice-uk | 2017-03-22T03:53:42+00:00
All the code is here - https://bench.cr.yp.to/supercop/supercop-20170228.tar.xz Didn't write anything new yet, just refactored it to work with Monero's ge_*

## anonimal | 2017-03-22T04:21:49+00:00
>Didn't write anything new yet

I know, that's what I'm asking for. Linking to supercop doesn't show me any of your implementation. Is this only a refactoring proposal?

## fireice-uk | 2017-03-22T11:04:58+00:00
Correct, there are no new features, only performance improvements. There are two parts:

- Refactoring the bignum arithmetic to use amd64-64-24k from the supercop lib. It is to be exported as a special version of crypto-ops.c used only in wallet scans.
- Refactoring wallet scan design to make it more parallel.
- Overall I am happy to guarantee that taken together both changes will double the performance (half the scan time), but the actual gain will be closer to quadrupling the performance.

There is no implementation currently, just a bare-metal benchmark to quantify the exact performance gain. I will start working if/when the powers that be decide to move the project to the funding stage. 

## damoon223 | 2017-03-24T15:33:14+00:00
hi
please add your email  otherwise contact me please 


## fireice-uk | 2017-03-24T15:37:42+00:00
@damoon223 
It is in my PGP key

## fluffypony | 2017-03-25T13:36:53+00:00
@fireice-uk sorry, been busy with the 0.10.3 release, and as you know we've had all those nigglies we've had to deal with. Also I get notifications for every Github comment, so I may miss specific mentions - you should've just pinged me on IRC like everyone else does:)

Can you update the thread to today's prices, and then I'll move it to Funding Required?

## fireice-uk | 2017-03-25T14:30:07+00:00
@fluffypony All done.

## fireice-uk | 2017-03-27T04:37:51+00:00
@fluffypony  
```
<fluffypony> ok cool - I'll move the proposal to funding after the 0.10.3.1 tag
```

## dEBRUYNE-1 | 2018-01-08T12:37:16+00:00
+proposal

## fireice-uk | 2018-01-13T11:51:10+00:00
@dEBRUYNE-1 I resigned that project more than 6 months ago. I will close it so that it doesn't clutter up your repo.

# Action History
- Created by: fireice-uk | 2017-03-02T16:28:02+00:00
- Closed at: 2018-01-13T11:51:10+00:00
