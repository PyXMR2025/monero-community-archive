---
title: Monero Research Lab Meeting - Wed 15 June 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/714
author: Rucknium
assignees: []
labels: []
created_at: '2022-06-13T13:06:24+00:00'
updated_at: '2022-06-21T01:00:11+00:00'
type: issue
status: closed
closed_at: '2022-06-21T01:00:11+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#712  

# Discussion History
## UkoeHB | 2022-06-15T18:00:57+00:00
```
[06-15-2022 16:59:53] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/714
[06-15-2022 16:59:54] <UkoeHB> 1. greetings
[06-15-2022 16:59:54] <UkoeHB> hello
[06-15-2022 17:00:19] <kayabanerve[m]> Morning
[06-15-2022 17:00:21] <rbrunner> Hi
[06-15-2022 17:00:26] <jberman[m]> howdy
[06-15-2022 17:00:30] <xmr-ack[m]> hi
[06-15-2022 17:01:09] <Rucknium[m]> Hi
[06-15-2022 17:01:32] <ooo123ooo1234567> hello
[06-15-2022 17:01:58] <jeffro256[m]> hello
[06-15-2022 17:02:38] <UkoeHB> 2. updates, what is everyone working on?
[06-15-2022 17:04:51] <UkoeHB> me: still working on seraphis enote scanning workflow (almost ready to start unit testing) + spent a couple days working on monerokon slides
[06-15-2022 17:05:12] <Rucknium[m]> Did K-S tests on output from mj-xmr 's Python implementation of the wallet2 decoy selection algorithm. I found an apparent off-by-one error, which mj then fixed. New output is passing statistical tests so far, although there may be issues with inappropriate use of integers in the wallet2 code.
[06-15-2022 17:05:14] <jberman[m]> approved 7760 pending merge conflicts, putting slides together for monerokon, getting back over to 8076
[06-15-2022 17:05:50] <jberman[m]> > although there may be issues with inappropriate use of integers in the wallet2 code
[06-15-2022 17:05:51] <jberman[m]> sounds familiar
[06-15-2022 17:07:42] <jeffro256[m]> I'm working through reviewing #7760, changing to EC SSL certs , and added a PR #8385 which makes presistent SSL an opt-in feature, even if in restricted mode. To that effect, I'm working on a p2p crawler which tries to track monerod nodes on persistent SSL certs 
[06-15-2022 17:09:04] <jeffro256[m]> > putting slides together for monerokon
[06-15-2022 17:09:11] <jeffro256[m]> What are you presenting about?
[06-15-2022 17:10:23] <jberman[m]> hoping to run down the proposed Seraphis/Jamtis features from a higher level user perspective, highlighting pros/cons
[06-15-2022 17:12:22] <kayabanerve[m]> Still working on my own things, yet recently further discussed FROST with a few parties, including as a slide for MK.
[06-15-2022 17:12:28] <UkoeHB> yeah there is a huge amount of material to cover so we will see how it goes
[06-15-2022 17:13:03] <ooo123ooo1234567> jberman[m]: does it include something on top of jamtis gist ?
[06-15-2022 17:13:04] <kayabanerve[m]> jberman[m]: Do we get to end Reddit discussions about the ovk?
[06-15-2022 17:14:06] <rbrunner> ovk?
[06-15-2022 17:14:16] <UkoeHB> 3. we can move to discussion
[06-15-2022 17:16:25] <Rucknium[m]> jberman:  As you (I think) discovered, MyMonero / lws transactions are fingerprintable on-chain due to how they choose fees (  https://github.com/mymonero/mymonero-core-cpp/pull/36 ). How could we go about getting a list of "suspects" on the mainnet chain?
[06-15-2022 17:17:44] <jberman[m]> ooo123ooo1234567: no, it's not new information
[06-15-2022 17:18:10] <kayabanerve[m]> rbrunner: Outgoing view key
[06-15-2022 17:18:18] <jberman[m]> there's a slide on that, ya
[06-15-2022 17:18:21] <rbrunner> Ah, ok, thanks
[06-15-2022 17:18:31] <rbrunner> Ending discussion on Reddit? Dream on :)
[06-15-2022 17:18:57] <kayabanerve[m]> I did want to ask the current bch code for jamtis. I do believe that should finalize to bech32n
[06-15-2022 17:19:08] <kayabanerve[m]> Right now, it's written as base32 with *some* bch
[06-15-2022 17:19:09] <kayabanerve[m]> s/bech32n/bech32m/
[06-15-2022 17:20:01] <ooo123ooo1234567> kayabanerve[m]: it's minor detail
[06-15-2022 17:20:04] <UkoeHB> kayabanerve[m]: there is no such code
[06-15-2022 17:20:09] <UkoeHB> unless tevador has something
[06-15-2022 17:20:15] <jberman[m]> Rucknium[m]: simplest/quickest way would be to run their fee algorithm at various times to get a range of what fees their txs would be. hardest way would be to definitively calculate the plausible fees it could have chosen for each tx. they can likely be pinpointed with effort
[06-15-2022 17:20:23] <kayabanerve[m]> Though I'll caveat I believe the Bitcoin bip defining bech32m also defines a version, which I'm not proposing carrying 
[06-15-2022 17:20:39] <kayabanerve[m]> ooo123ooo1234567: Agreed, yet there was an example cited and it was unknown what it did
[06-15-2022 17:21:02] <ooo123ooo1234567> <Rucknium[m]> "Did K-S tests on output from mj..." <- Is there any public goal that is supposed to be achieved with this scientific approach of code translation from one lang to another ?
[06-15-2022 17:21:05] <kayabanerve[m]> UkoeHB: I believe they do, yet it's private at this time, but I just wanted to start noting that specific detail
[06-15-2022 17:21:30] <Rucknium[m]> jberman: Hardest way as in most computationally expensive? Or also hard on developer time?
[06-15-2022 17:22:00] <jberman[m]> I don't think it would be computationally impractical, just hard on developer time
[06-15-2022 17:22:27] <ooo123ooo1234567> * with this (pseudo-)scientific approach
[06-15-2022 17:23:01] <Rucknium[m]> ooo123ooo1234567: Yes. Two main purposes. We need a mathematical definition of the probability density function that the wallet2 decoy selection algorithm uses. Also we can use this code to check how well other implementations in "third party" wallets are mimicking the wallet2 behavior.
[06-15-2022 17:24:29] <jeffro256[m]> > > <@rucknium:monero.social> jberman:  As you (I think) discovered, MyMonero / lws transactions are fingerprintable on-chain due to how they choose fees (  https://github.com/mymonero/mymonero-core-cpp/pull/36 ). How could we go about getting a list of "suspects" on the mainnet chain?
[06-15-2022 17:24:29] <jeffro256[m]> > 
[06-15-2022 17:24:29] <jeffro256[m]> > simplest/quickest way would be to run their fee algorithm at various times to get a range of what fees their txs would be. hardest way would be to definitively calculate the plausible fees it could have chosen for each tx. they can likely be pinpointed with effort
[06-15-2022 17:24:29] <jeffro256[m]> A cool project would be to color each transaction based on the fee algorithm, then try to trace senders though tx tree based on that coloring and see how badly that affects linkability 
[06-15-2022 17:26:54] <Rucknium[m]> I know devs are focused on hard fork issues and multisig right now, but it would be great if someone could take on the project of identifying the MyMonero / lws fingerprintable txs. I could maybe make an attempt with some pointers.
[06-15-2022 17:27:42] <rbrunner> Any news on PR 8149? Still waiting for the results of the external review I guess?
[06-15-2022 17:28:03] <UkoeHB> rbrunner: the audit is still in-progress I think
[06-15-2022 17:28:05] <jeffro256[m]> The review is to be done by inference AG right ?
[06-15-2022 17:28:33] <ooo123ooo1234567> <jeffro256[m]> "I'm working through reviewing #7..." <- Nothing mentioned here can be qualified as research, there are even open source crawlers for p2p network. Also SSL is mostly useless. And code reading is a bare minimum of development process, it isn't research.
[06-15-2022 17:29:15] <UkoeHB> jeffro256[m]: yes they are doing the audit
[06-15-2022 17:29:23] <rbrunner> It's almost cool how we will sail through the planned hardfork release date tomorrow without batting an eye ... at least so far.
[06-15-2022 17:29:43] <kayabanerve[m]> rbrunner: I did submit my own review with a few notes.
[06-15-2022 17:30:06] <rbrunner> Nice
[06-15-2022 17:31:05] <jeffro256[m]> > It's almost cool how we will sail through the planned hardfork release date tomorrow without batting an eye ... at least so far.
[06-15-2022 17:31:06] <jeffro256[m]> deadlines shmeadlines 
[06-15-2022 17:31:28] <ooo123ooo1234567> Rucknium[m]: mymonero / lws fingerprintable txs isn't a priority
[06-15-2022 17:32:08] <Rucknium[m]> ooo123ooo1234567: Yes, it's a priority.
[06-15-2022 17:32:10] <rbrunner> Whoever fancies to work on that will it make their own personal priority for a certain time ...
[06-15-2022 17:32:34] <cryptogrampy[m]> is the fingerprint simply that one can say the tx came from LWS?  does self-hosting an LWS server produce the same fingerprint?
[06-15-2022 17:32:41] <rbrunner> That's open source for you.
[06-15-2022 17:32:49] <ooo123ooo1234567> UkoeHB: early next week == monday or tuesday, right ?
[06-15-2022 17:32:59] <cryptogrampy[m]> the same fingerprint as MyMonero*
[06-15-2022 17:33:15] <ooo123ooo1234567> Rucknium[m]: reference implementation wallet2 is a ppriority, third party services aren't priority; why ?
[06-15-2022 17:33:30] <ooo123ooo1234567> s/ppriority/priority/
[06-15-2022 17:34:47] <Rucknium[m]> ooo123ooo1234567: First, on-chain action by some users can harm other users. That's one reason why users can no longer set their own ring size.
[06-15-2022 17:35:08] <kayabanerve[m]> <rbrunner> "It's almost cool how we will..." <- I have two conflicts here.
[06-15-2022 17:35:08] <kayabanerve[m]> 1) we moved multisig to the CLI labeling it "experimental". Without 8149, it should be "unsafe"
[06-15-2022 17:35:08] <kayabanerve[m]> 2) I have a minor PR I was hoping to get included and thought I had the necessary approvals for yet remains sitting there :C
[06-15-2022 17:35:35] <jeffro256[m]> > is the fingerprint simply that one can say the tx came from LWS?  does self-hosting an LWS server produce the same fingerprint?
[06-15-2022 17:35:35] <jeffro256[m]> jberman would know best, but it seems that the fingerprint is just a binary yes/no whether or not a wallet uses the MyMonero fee algorithm
[06-15-2022 17:35:53] <jeffro256[m]> To oversimplify 
[06-15-2022 17:36:31] <ooo123ooo1234567> Rucknium[m]: There are reasons to write/use ad-hoc implementation instead of wallet2, but it's certainly not due to alternative DSA. There is no point to chase every ad-hoc implementation, fix reference one
[06-15-2022 17:36:32] <Rucknium[m]> Second, MyMonero / lws has a subtle difference in the decoy selection algorithm compared to wallet2, so identifying those txs help with understanding what is happening with decoy selection on-chain.
[06-15-2022 17:36:33] <kayabanerve[m]> > <@jeffro256:monero.social> > is the fingerprint simply that one can say the tx came from LWS?  does self-hosting an LWS server produce the same fingerprint?
[06-15-2022 17:36:33] <kayabanerve[m]> > 
[06-15-2022 17:36:33] <kayabanerve[m]> > jberman would know best, but it seems that the fingerprint is just a binary yes/no whether or not a wallet uses the MyMonero fee algorithm
[06-15-2022 17:36:33] <kayabanerve[m]> Which voids their ring sigs and removes entire trees as valid decoys
[06-15-2022 17:36:39] <rbrunner> kayabanerve[m]: I wasn't accusing anybody, just being amused a bit about the Monero dev community as a whole :)
[06-15-2022 17:37:25] <jberman[m]> >  is the fingerprint simply that one can say the tx came from LWS?
[06-15-2022 17:37:25] <jberman[m]> this is the LWS one which is currently fixed in the develop branch, soon to be fixed in other branches
[06-15-2022 17:37:43] <kayabanerve[m]> rbrunner: I was throwing a tiny bit of shade and wanted to reraise the CLI option discussion :p
[06-15-2022 17:37:53] <jeffro256[m]> kayabanerve : Isn't 1) just a matter of word choice. Usually users equate "experimental" with "unsafe" .
[06-15-2022 17:37:55] <cryptogrampy[m]> Is there any way to prevent someone from making an implementation that is more fingerprintable in the first place?
[06-15-2022 17:37:56] <jberman[m]> the mymonero fingerprint is tied to the mymonero client still until those other PR's are shipped. so even if you self-host, if you're using the mymonero client your txs are fingerprintable as coming from the mymonero client 
[06-15-2022 17:38:00] <ooo123ooo1234567> Rucknium[m]: It's waste of time and certainly not a priority
[06-15-2022 17:38:12] <jeffro256[m]> > "Which voids their ring sigs and removes entire trees as valid decoys"
[06-15-2022 17:38:20] <kayabanerve[m]> jeffro256[m]: 8149 is experimental yet I believe it to be safe, even if I get why we won't endorse it as such
[06-15-2022 17:38:23] <jeffro256[m]> Yes there's a lot of knockon effects for sure 
[06-15-2022 17:38:32] <kayabanerve[m]> The current is dead code definitively broken
[06-15-2022 17:38:43] <kayabanerve[m]> It's not experimental once the experiment fails 
[06-15-2022 17:38:47] <Rucknium[m]> ooo123ooo1234567: Again, you don't understand the issues involved, so you don't see why it's a priority. Stick to what you know, I guess.
[06-15-2022 17:39:01] <kayabanerve[m]> I'm mainly worried users will see experimental and believe 8149 was merged when it wasn't
[06-15-2022 17:39:14] <Rucknium[m]> Or at least don't try to make definitive statements about what you don't know
[06-15-2022 17:39:50] <ooo123ooo1234567> Rucknium[m]: how to test understanding ? any counterexample ?
[06-15-2022 17:40:14] <Rucknium[m]> ooo123ooo1234567: Did you read those papers I suggested to you?
[06-15-2022 17:40:20] <jeffro256[m]> > I'm mainly worried users will see experimental and believe 8149 was merged when it wasn't
[06-15-2022 17:40:20] <jeffro256[m]> I guess that's a good point, it's not really experimental, it's just wrong 
[06-15-2022 17:40:40] <jeffro256[m]> * Not 8149 I mean, current code 
[06-15-2022 17:40:41] <jberman[m]> cryptogrampy[m]: UkoeHB has ideas in seraphis to make it easier to write wallet code where fees are less discernible, basically by rounding to an even higher place + reducing significant digits in the fee
[06-15-2022 17:40:43] <UkoeHB> hence why I said current code should be completely disabled lol
[06-15-2022 17:41:06] <ooo123ooo1234567> UkoeHB: it doesn't matter who you said
[06-15-2022 17:41:08] <ooo123ooo1234567> s/who/what/
[06-15-2022 17:41:41] <UkoeHB> jberman[m]: more than an idea https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis/tx_discretized_fee.cpp
[06-15-2022 17:42:08] <jberman[m]> true true :)
[06-15-2022 17:42:27] <kayabanerve[m]> UkoeHB: Agreed. Could you put up a PR tonight after this? Should we ping mooo?
[06-15-2022 17:43:11] <kayabanerve[m]> Because at the least, it's experimental -> unsafe for the CLI. Next would be a compile time def, which I'm not wholly against and think is probably optimal due to existing users. Finally would be yeah, ripping it.
[06-15-2022 17:44:47] <UkoeHB> kayabanerve[m]: tbh I don't think disabling would fly, the HF might just be delayed I guess
[06-15-2022 17:45:27] <kayabanerve[m]> Right. That's why there's the middle ground and a minimum :p
[06-15-2022 17:50:35] <ooo123ooo1234567> <Rucknium[m]> "ooo123ooo1234567: Yes. Two..." <- Once isolated ref implementation of DSA is available, what is the next goal ? Is there any public place which lists long term goal (with intermediate steps) that needs this work ?
[06-15-2022 17:52:52] <ooo123ooo1234567> <kayabanerve[m]> "Because at the least, it's..." <- instead of playing in this game of words, it would be good to have better understanding what is secure or not and why, much more helpful
[06-15-2022 17:53:48] <UkoeHB> ok we are getting to the end of the hour, any last minute comments/questions?
[06-15-2022 17:54:11] <kayabanerve[m]> ooo123ooo1234567: ... the current code is definitively insecure. Experimental suggests it may be fine, and it's an unknown. It's not an unknown. There's no experiment
[06-15-2022 17:54:45] <ooo123ooo1234567> <Rucknium[m]> "Or at least don't try to make..." <- the goal of that work is unknown, is it possible to make it public or not ?
[06-15-2022 17:54:45] <kayabanerve[m]> Therefore, experimental should at least be changed to unsafe as experimental was chosen with the expectation of 8149 being merged which is experimental, pending further review
[06-15-2022 17:55:13] <ooo123ooo1234567> kayabanerve[m]: you're continuing to play with words again, unknown things can be cleared out with some amount of work
[06-15-2022 17:56:02] <kayabanerve[m]> There's no word game here. That was facts on the current code and interpretation. That message didn't make a single comment on 8149
[06-15-2022 17:56:44] <kayabanerve[m]> My following comment said 8149 is considered experimental pending review, sure, yet didn't discuss why/how, making your comments still irrelevant
[06-15-2022 17:59:36] <UkoeHB> ok that's the end of the meeting, thanks for attending everyone
```

## plowsof | 2022-06-15T18:02:57+00:00
Logs 
```
16:59:53 <UkoeHB> meeting time https://github.com/monero-project/meta/issues/714

16:59:54 <UkoeHB> 1. greetings

16:59:54 <UkoeHB> hello

17:00:19 <kayabanerve[m]> Morning

17:00:21 <rbrunner> Hi

17:00:26 <jberman[m]> howdy

17:00:30 <xmr-ack[m]> hi

17:01:09 <Rucknium[m]> Hi

17:01:32 <ooo123ooo1234567> hello

17:01:58 <jeffro256[m]> hello

17:02:38 <UkoeHB> 2. updates, what is everyone working on?

17:04:51 <UkoeHB> me: still working on seraphis enote scanning workflow (almost ready to start unit testing) +
spent a couple days working on monerokon slides

17:05:12 <Rucknium[m]> Did K-S tests on output from mj-xmr 's Python implementation of the wallet2 decoy
selection algorithm. I found an apparent off-by-one error, which mj then fixed. New output is passing
statistical tests so far, although there may be issues with inappropriate use of integers in the wallet2 code.

17:05:14 <jberman[m]> approved 7760 pending merge conflicts, putting slides together for monerokon, getting
back over to 8076

17:05:50 <jberman[m]> > although there may be issues with inappropriate use of integers in the wallet2 code

17:05:51 <jberman[m]> sounds familiar

17:07:42 <jeffro256[m]> I'm working through reviewing #7760, changing to EC SSL certs , and added a PR #8385
which makes presistent SSL an opt-in feature, even if in restricted mode. To that effect, I'm working on a p2p
crawler which tries to track monerod nodes on persistent SSL certs

17:09:04 <jeffro256[m]> > putting slides together for monerokon

17:09:11 <jeffro256[m]> What are you presenting about?

17:10:23 <jberman[m]> hoping to run down the proposed Seraphis/Jamtis features from a higher level user
perspective, highlighting pros/cons

17:12:22 <kayabanerve[m]> Still working on my own things, yet recently further discussed FROST with a few
parties, including as a slide for MK.

17:12:28 <UkoeHB> yeah there is a huge amount of material to cover so we will see how it goes

17:13:03 <ooo123ooo1234567> jberman[m]: does it include something on top of jamtis gist ?

17:13:04 <kayabanerve[m]> jberman[m]: Do we get to end Reddit discussions about the ovk?

17:14:06 <rbrunner> ovk?

17:14:16 <UkoeHB> 3. we can move to discussion

17:16:25 <Rucknium[m]> jberman:  As you (I think) discovered, MyMonero / lws transactions are fingerprintable
on-chain due to how they choose fees (  https://github.com/mymonero/mymonero-core-cpp/pull/36 ). How could we
go about getting a list of "suspects" on the mainnet chain?

17:17:44 <jberman[m]> ooo123ooo1234567: no, it's not new information

17:18:10 <kayabanerve[m]> rbrunner: Outgoing view key

17:18:18 <jberman[m]> there's a slide on that, ya

17:18:21 <rbrunner> Ah, ok, thanks

17:18:31 <rbrunner> Ending discussion on Reddit? Dream on :)

17:18:57 <kayabanerve[m]> I did want to ask the current bch code for jamtis. I do believe that should finalize
to bech32n

17:19:08 <kayabanerve[m]> Right now, it's written as base32 with *some* bch

17:19:09 <kayabanerve[m]> s/bech32n/bech32m/

17:20:01 <ooo123ooo1234567> kayabanerve[m]: it's minor detail

17:20:04 <UkoeHB> kayabanerve[m]: there is no such code

17:20:09 <UkoeHB> unless tevador has something

17:20:15 <jberman[m]> Rucknium[m]: simplest/quickest way would be to run their fee algorithm at various times
to get a range of what fees their txs would be. hardest way would be to definitively calculate the plausible
fees it could have chosen for each tx. they can likely be pinpointed with effort

17:20:23 <kayabanerve[m]> Though I'll caveat I believe the Bitcoin bip defining bech32m also defines a
version, which I'm not proposing carrying

17:20:39 <kayabanerve[m]> ooo123ooo1234567: Agreed, yet there was an example cited and it was unknown what it
did

17:21:02 <ooo123ooo1234567> <Rucknium[m]> "Did K-S tests on output from mj..." <- Is there any public goal
that is supposed to be achieved with this scientific approach of code translation from one lang to another ?

17:21:05 <kayabanerve[m]> UkoeHB: I believe they do, yet it's private at this time, but I just wanted to start
noting that specific detail

17:21:30 <Rucknium[m]> jberman: Hardest way as in most computationally expensive? Or also hard on developer
time?

17:22:00 <jberman[m]> I don't think it would be computationally impractical, just hard on developer time

17:22:27 <ooo123ooo1234567> * with this (pseudo-)scientific approach

17:23:01 <Rucknium[m]> ooo123ooo1234567: Yes. Two main purposes. We need a mathematical definition of the
probability density function that the wallet2 decoy selection algorithm uses. Also we can use this code to
check how well other implementations in "third party" wallets are mimicking the wallet2 behavior.

17:24:29 <jeffro256[m]> > > <@rucknium:monero.social> jberman:  As you (I think) discovered, MyMonero / lws
transactions are fingerprintable on-chain due to how they choose fees (  https://github.com/mymonero/mymonero-
core-cpp/pull/36 ). How could we go about getting a list of "suspects" on the mainnet chain?

17:24:29 <jeffro256[m]> >

17:24:29 <jeffro256[m]> > simplest/quickest way would be to run their fee algorithm at various times to get a
range of what fees their txs would be. hardest way would be to definitively calculate the plausible fees it
could have chosen for each tx. they can likely be pinpointed with effort

17:24:29 <jeffro256[m]> A cool project would be to color each transaction based on the fee algorithm, then try
to trace senders though tx tree based on that coloring and see how badly that affects linkability

17:26:54 <Rucknium[m]> I know devs are focused on hard fork issues and multisig right now, but it would be
great if someone could take on the project of identifying the MyMonero / lws fingerprintable txs. I could
maybe make an attempt with some pointers.

17:27:42 <rbrunner> Any news on PR 8149? Still waiting for the results of the external review I guess?

17:28:03 <UkoeHB> rbrunner: the audit is still in-progress I think

17:28:05 <jeffro256[m]> The review is to be done by inference AG right ?

17:28:33 <ooo123ooo1234567> <jeffro256[m]> "I'm working through reviewing #7..." <- Nothing mentioned here can
be qualified as research, there are even open source crawlers for p2p network. Also SSL is mostly useless. And
code reading is a bare minimum of development process, it isn't research.

17:29:15 <UkoeHB> jeffro256[m]: yes they are doing the audit

17:29:23 <rbrunner> It's almost cool how we will sail through the planned hardfork release date tomorrow
without batting an eye ... at least so far.

17:29:43 <kayabanerve[m]> rbrunner: I did submit my own review with a few notes.

17:30:06 <rbrunner> Nice

17:31:05 <jeffro256[m]> > It's almost cool how we will sail through the planned hardfork release date tomorrow
without batting an eye ... at least so far.

17:31:06 <jeffro256[m]> deadlines shmeadlines

17:31:28 <ooo123ooo1234567> Rucknium[m]: mymonero / lws fingerprintable txs isn't a priority

17:32:08 <Rucknium[m]> ooo123ooo1234567: Yes, it's a priority.

17:32:10 <rbrunner> Whoever fancies to work on that will it make their own personal priority for a certain
time ...

17:32:34 <cryptogrampy[m]> is the fingerprint simply that one can say the tx came from LWS?  does self-hosting
an LWS server produce the same fingerprint?

17:32:41 <rbrunner> That's open source for you.

17:32:49 <ooo123ooo1234567> UkoeHB: early next week == monday or tuesday, right ?

17:32:59 <cryptogrampy[m]> the same fingerprint as MyMonero*

17:33:15 <ooo123ooo1234567> Rucknium[m]: reference implementation wallet2 is a ppriority, third party services
aren't priority; why ?

17:33:30 <ooo123ooo1234567> s/ppriority/priority/

17:34:47 <Rucknium[m]> ooo123ooo1234567: First, on-chain action by some users can harm other users. That's one
reason why users can no longer set their own ring size.

17:35:08 <kayabanerve[m]> <rbrunner> "It's almost cool how we will..." <- I have two conflicts here.

17:35:08 <kayabanerve[m]> 1) we moved multisig to the CLI labeling it "experimental". Without 8149, it should
be "unsafe"

17:35:08 <kayabanerve[m]> 2) I have a minor PR I was hoping to get included and thought I had the necessary
approvals for yet remains sitting there :C

17:35:35 <jeffro256[m]> > is the fingerprint simply that one can say the tx came from LWS?  does self-hosting
an LWS server produce the same fingerprint?

17:35:35 <jeffro256[m]> jberman would know best, but it seems that the fingerprint is just a binary yes/no
whether or not a wallet uses the MyMonero fee algorithm

17:35:53 <jeffro256[m]> To oversimplify

17:36:31 <ooo123ooo1234567> Rucknium[m]: There are reasons to write/use ad-hoc implementation instead of
wallet2, but it's certainly not due to alternative DSA. There is no point to chase every ad-hoc
implementation, fix reference one

17:36:32 <Rucknium[m]> Second, MyMonero / lws has a subtle difference in the decoy selection algorithm
compared to wallet2, so identifying those txs help with understanding what is happening with decoy selection
on-chain.

17:36:33 <kayabanerve[m]> > <@jeffro256:monero.social> > is the fingerprint simply that one can say the tx
came from LWS?  does self-hosting an LWS server produce the same fingerprint?

17:36:33 <kayabanerve[m]> >

17:36:33 <kayabanerve[m]> > jberman would know best, but it seems that the fingerprint is just a binary yes/no
whether or not a wallet uses the MyMonero fee algorithm

17:36:33 <kayabanerve[m]> Which voids their ring sigs and removes entire trees as valid decoys

17:36:39 <rbrunner> kayabanerve[m]: I wasn't accusing anybody, just being amused a bit about the Monero dev
community as a whole :)

17:37:25 <jberman[m]> >  is the fingerprint simply that one can say the tx came from LWS?

17:37:25 <jberman[m]> this is the LWS one which is currently fixed in the develop branch, soon to be fixed in
other branches

17:37:43 <kayabanerve[m]> rbrunner: I was throwing a tiny bit of shade and wanted to reraise the CLI option
discussion :p

17:37:53 <jeffro256[m]> kayabanerve : Isn't 1) just a matter of word choice. Usually users equate
"experimental" with "unsafe" .

17:37:55 <cryptogrampy[m]> Is there any way to prevent someone from making an implementation that is more
fingerprintable in the first place?

17:37:56 <jberman[m]> the mymonero fingerprint is tied to the mymonero client still until those other PR's are
shipped. so even if you self-host, if you're using the mymonero client your txs are fingerprintable as coming
from the mymonero client

17:38:00 <ooo123ooo1234567> Rucknium[m]: It's waste of time and certainly not a priority

17:38:12 <jeffro256[m]> > "Which voids their ring sigs and removes entire trees as valid decoys"

17:38:20 <kayabanerve[m]> jeffro256[m]: 8149 is experimental yet I believe it to be safe, even if I get why we
won't endorse it as such

17:38:23 <jeffro256[m]> Yes there's a lot of knockon effects for sure

17:38:32 <kayabanerve[m]> The current is dead code definitively broken

17:38:43 <kayabanerve[m]> It's not experimental once the experiment fails

17:38:47 <Rucknium[m]> ooo123ooo1234567: Again, you don't understand the issues involved, so you don't see why
it's a priority. Stick to what you know, I guess.

17:39:01 <kayabanerve[m]> I'm mainly worried users will see experimental and believe 8149 was merged when it
wasn't

17:39:14 <Rucknium[m]> Or at least don't try to make definitive statements about what you don't know

17:39:50 <ooo123ooo1234567> Rucknium[m]: how to test understanding ? any counterexample ?

17:40:14 <Rucknium[m]> ooo123ooo1234567: Did you read those papers I suggested to you?

17:40:20 <jeffro256[m]> > I'm mainly worried users will see experimental and believe 8149 was merged when it
wasn't

17:40:20 <jeffro256[m]> I guess that's a good point, it's not really experimental, it's just wrong

17:40:40 <jeffro256[m]> * Not 8149 I mean, current code

17:40:41 <jberman[m]> cryptogrampy[m]: UkoeHB has ideas in seraphis to make it easier to write wallet code
where fees are less discernible, basically by rounding to an even higher place + reducing significant digits
in the fee

17:40:43 <UkoeHB> hence why I said current code should be completely disabled lol

17:41:06 <ooo123ooo1234567> UkoeHB: it doesn't matter who you said

17:41:08 <ooo123ooo1234567> s/who/what/

17:41:41 <UkoeHB> jberman[m]: more than an idea
https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis/tx_discretized_fee.cpp

17:42:08 <jberman[m]> true true :)

17:42:27 <kayabanerve[m]> UkoeHB: Agreed. Could you put up a PR tonight after this? Should we ping mooo?

17:43:11 <kayabanerve[m]> Because at the least, it's experimental -> unsafe for the CLI. Next would be a
compile time def, which I'm not wholly against and think is probably optimal due to existing users. Finally
would be yeah, ripping it.

17:44:47 <UkoeHB> kayabanerve[m]: tbh I don't think disabling would fly, the HF might just be delayed I guess

17:45:27 <kayabanerve[m]> Right. That's why there's the middle ground and a minimum :p

17:50:35 <ooo123ooo1234567> <Rucknium[m]> "ooo123ooo1234567: Yes. Two..." <- Once isolated ref implementation
of DSA is available, what is the next goal ? Is there any public place which lists long term goal (with
intermediate steps) that needs this work ?

17:52:52 <ooo123ooo1234567> <kayabanerve[m]> "Because at the least, it's..." <- instead of playing in this
game of words, it would be good to have better understanding what is secure or not and why, much more helpful

17:53:48 <UkoeHB> ok we are getting to the end of the hour, any last minute comments/questions?

17:54:11 <kayabanerve[m]> ooo123ooo1234567: ... the current code is definitively insecure. Experimental
suggests it may be fine, and it's an unknown. It's not an unknown. There's no experiment

17:54:45 <ooo123ooo1234567> <Rucknium[m]> "Or at least don't try to make..." <- the goal of that work is
unknown, is it possible to make it public or not ?

17:54:45 <kayabanerve[m]> Therefore, experimental should at least be changed to unsafe as experimental was
chosen with the expectation of 8149 being merged which is experimental, pending further review

17:55:13 <ooo123ooo1234567> kayabanerve[m]: you're continuing to play with words again, unknown things can be
cleared out with some amount of work

17:56:02 <kayabanerve[m]> There's no word game here. That was facts on the current code and interpretation.
That message didn't make a single comment on 8149

17:56:44 <kayabanerve[m]> My following comment said 8149 is considered experimental pending review, sure, yet
didn't discuss why/how, making your comments still irrelevant

17:59:36 <UkoeHB> ok that's the end of the meeting, thanks for attending everyone


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2022-06-15T18:04:16+00:00
@UkoeHB you are too quick! thanks for chairing the meeting!

# Action History
- Created by: Rucknium | 2022-06-13T13:06:24+00:00
- Closed at: 2022-06-21T01:00:11+00:00
