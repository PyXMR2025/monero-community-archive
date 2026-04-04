---
title: Implement Detective Mining (Pool Software Change, No Protocol Change Required)
source_url: https://github.com/monero-project/research-lab/issues/140
author: fluffypony
assignees: []
labels: []
created_at: '2025-08-19T08:04:00+00:00'
updated_at: '2025-08-29T16:25:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We should encourage pools to adopt the "detective mining" strategy from Lee and Kim, which leverages information pools already leak in their job messages to collapse a selfish miner's private lead. Crucially, this is deployable at the pool or Stratum-proxy level with no consensus or protocol changes.

Paper: https://eprint.iacr.org/2019/486

Thanks to @AJ\_\_1337 on X for highlighting the paper.

## One-paragraph explainer

Selfish pools must distribute jobs that tell their workers which parent to mine on (eg. Qubic uses pool.qubic.li). Those jobs reveal the pool's private tip via the previous block hash. A detective miner subscribes to those jobs, detects when the leaked prevhash does not match the public tip, and immediately mines a "counter" child block on top of the selfish pool's hidden parent. Publishing that child forces the selfish pool to reveal its private block or lose it, repeatedly cutting off the attacker's lead and eroding their advantage. The original paper models and simulates this dynamic and shows the attacker's extra revenue disappears as detective adoption grows.

Practically, if ~50% of the Monero hashrate (the largest pools) implement this, then the selfish miner’s break-even jumps to roughly 42 percent if tie-breaking favours the honest chain, ~37 percent under neutral tie-breaking, and ~32 percent if tie-breaking favours the attacker (see Figure 11 in the paper). Comparatively, the baseline without detective miners is the classical Eyal–Sirer threshold that can be near 25 percent when tie-breaking favours the attacker, rising toward one third otherwise. If we are between 50% and 100% hashrate adoption across pools then it wipes out the ability to selfish-mine entirely across the tested splits (see Figures 14 and 15).

Why this is pool-side: Stratum job messages include a prevhash or equivalent parent reference that pools must share with miners. In Stratum v1 job payloads this field is explicit, and in Stratum v2 there is a dedicated SetNewPrevHash message. That is the hook detective mining exploits.

## Actionable plan for pools and stratum proxies

**Scope.** All work is at the pool or proxy layer. No protocol or consensus changes are needed.

### 1) Instrumentation and detection

* [ ] Add a lightweight "sensor" client that subscribes to competing pools' job streams. Capture the current prevhash and job IDs.
* [ ] Continuously compare the observed prevhash with your node's public tip. If it diverges for more than T seconds, flag a likely private branch.

### 2) Counter-template construction

* [ ] When a leak is detected, construct a valid block template whose parent equals the leaked prevhash. Keep the template minimal if needed. For Bitcoin-style stacks this means a legal header, coinbase, and a conservative transaction set.

### 3) Hash allocation and switching

* [ ] Immediately redirect a configurable fraction of your pool's hashrate to the counter-template, even if that means the entire pool's hashrate uses this new template. Revert to public-tip templates when the competitor's jobs return to the public parent.

### 4) Submission and networking

* [ ] On a find, broadcast your child block immediately. The selfish pool must then publish its private parent to avoid losing it, collapsing its lead. 

## Why this helps

* **Mechanism.** Detective mining repeatedly cuts the attacker's private lead by forcing reveals whenever the attacker tries to extend a hidden branch.
* **Practicality.** It exploits fields pools already expose in job messages, and it works today with Stratum, which means it works with Monero.
* **Economics.** The paper's simulations show the attacker's excess revenue shrinks quickly as the detective share grows, and multiple selfish pools cannibalise one another even more once detective miners are active.

## Pool Software Anti-Decoy Counter-Measures

Pool software should include some sneakiness to prevent their sensor probes from being detected. Here's a checklist:

### Detection and corroboration

* Require quorum: do not act unless the same off-tip prevhash is observed by multiple independent sensors on different IP ranges and regions.
* Verify persistence: the off-tip parent must persist across multiple `mining.notify` messages or SV2 `SetNewPrevHash` updates for T seconds before diverting any hash.
* Share-acceptance check: each sensor submits a few shares on the leaked job and proceeds only if the pool accepts them, proving the job is live and not a read-only decoy.
* P2P sanity check: confirm the leaked parent is not yet known to your full node or the public tip.

### Sensor hygiene

* Make sensors hard to fingerprint: rotate IPs and providers, vary user agents, and keep normal share cadence and difficulties so targeted fake jobs are harder to aim at. Stratum sessions are per-connection with per-connection state (extranonce1), so blend in.
* Use multiple ingress points: subscribe to several pool endpoints when available and compare job streams in real time.

### Activation policy

* Two-stage diversion: on a valid signal, divert a tiny fraction H of hash first, auto-ramp only if corroboration continues during a grace window. Roll back automatically if any check fails. The detective-mining literature supports that even modest detective share reduces attacker advantage.
* Rate-limit triggers: bound how often you will divert within a rolling window and cap the maximum detective-hash allocation to limit worst-case decoy cost.
* Cross-sensor consistency: abort if the pool delivers inconsistent prevhashes across your own sensors in close time proximity, which is a strong indicator you are being singled out. Stratum allows different jobs per connection, so inconsistency is meaningful.

### Telemetry and audits

* Log every incident: prevhash, job IDs, times seen, which sensors corroborated, share-acceptance results, diversion start/stop, and outcomes.
* Track false positives and orphan rate during trials, then tighten thresholds based on empirical results.


# Discussion History
## kayabaNerve | 2025-08-19T13:40:00+00:00
Can't a malicious pool (as we're discussing here) lie about having a private chain to cause other pools to divert hashpower? The counter seems to be 'the malicious pool is itself distributing work on an alt-chain', but I wouldn't be surprised if a pool could identify the connections another pool is listening via.

## fluffypony | 2025-08-19T14:07:23+00:00
> Can't a malicious pool (as we're discussing here) lie about having a private chain to cause other pools to divert hashpower? The counter seems to be 'the malicious pool is itself distributing work on an alt-chain', but I wouldn't be surprised if a pool could identify the connections another pool is listening via.

Yes but that's easy to mitigate - a pool could easily operate their sensors on different IP addresses with different addresses, and only shift hashrate if a quorum of sensors see the same prev_id. The pool software should also require the leaked parent to persist across time and messages, not a single `notify` or `SetNewPrevHash`, and then abort if the pool flips parents or sends mutually inconsistent jobs across your own connections, which is a strong sign you’ve been singled out. Also there's no need for the whole hashrate to flip to that block - even if single-digit percentages mine it, it forces the malicious pool to disclose.

## fluffypony | 2025-08-19T14:14:35+00:00
Added an anti-decoy counter-measure checklist to the issue.

## SChernykh | 2025-08-19T14:23:05+00:00
> The selfish pool must then publish its private parent to avoid losing it, collapsing its lead.

No they won't publish it. If a block at height N+1 is private and someone mines a child block at height N+2, it will not become the longest chain because of the missing N+1. It will just dangle in node's memory, or will be rejected.

## fluffypony | 2025-08-19T14:32:03+00:00
> No they won't publish it. If a block at height N+1 is private and someone mines a child block at height N+2, it will not become the longest chain because of the missing N+1. It will just dangle in node's memory, or will be rejected.

You’re right that an N+2 child without its N+1 parent will not be accepted. That isn’t the claim. Detective mining doesn’t magic N+2 onto the main chain; it changes the attacker’s pay-off so they either reveal N+1 now or eat the loss.

Two outcomes once the detective child is broadcast:

1. Attacker reveals. To realise any revenue from their private branch, the selfish pool must publish N+1 so the network can validate the detective’s N+2. Publishing early collapses their private lead back toward parity and neuters the selfish-mining advantage. This is exactly the dynamic modelled in the detective-mining paper (see Fig. 2(c)–(d); the authors explicitly assume the rational response is to release the private blocks when a child appears)

2. Attacker withholds. Then they forfeit N+1’s reward and keep hashing on a branch that other pools can keep targeting with further detective children. Meanwhile, the public chain advances. Economically this is worse than revealing, which is why the paper’s state machine and simulations show the attacker’s extra revenue shrinking as detective share grows

Network mechanics are straightforward: nodes that see a block whose parent is unknown don’t attach it; they request or await the missing parent and hold the child as an orphan until the parent arrives. That’s normal Bitcoin/Monero behaviour and precisely why the attacker must release the parent to get paid.

So the sentence should read more precisely: “Publishing the detective child forces a choice. If the selfish pool wants any revenue from its private fork, it must reveal the parent now, which collapses its lead; otherwise it burns its private blocks.” That is the incentive lever detective mining exploits, and it requires only pool-side changes, not protocol changes.

## SChernykh | 2025-08-19T14:41:07+00:00
If an attacker withholds, and mines their own version of N+2, then what will happen? Detectives will mine on top of attacker's N+2, or their own N+2?

## preoncyber | 2025-08-19T14:45:33+00:00
This is with known dark pools. How do we counter unknown pools? 

## stringhandler | 2025-08-19T15:05:50+00:00
> No they won't publish it. If a block at height N+1 is private and someone mines a child block at height N+2, it will not become the longest chain because of the missing N+1. It will just dangle in node's memory, or will be rejected.

Not sure if it's better here or as a new proposal, but to allow mining without the having `N+1`, you could change the block hashing structure to be longer, and have `x` blocks hashes. So for example if you wanted to prevent a selfish mine of 5 blocks, you could have the `block_hash_blob` that is fed into randomx be `<block n-5><block n-4>...<block n-1><block_hashing_blob>`.

The reason this needs to be in the `block_hashing_blob` is so that selfish pools must publish it to their miners. In this case I believe the miners for qubic are mercenary, so they are in the public and anyone can mine to their pool, seeing the chain.

If you change the way a block is hashed together, you could potentially even form a merkle tree, ideally with enough data to calculate the difficulty of each block.

So prev_block_hash becomes a node in a merkle tree,  `prev_block_mr = Hash(prev_prev_block_mr, other_blob_hash)`  and is recursive.

Then stratum blobs are a short merkle tree of `prev_block_mrs` with enough data to know the strength of the chain, even if they don't have the full blocks. The non-selfish pools can mine on the chain, even though they don't have it. 


## fluffypony | 2025-08-19T15:22:08+00:00
> If an attacker withholds, and mines their own version of N+2, then what will happen? Detectives will mine on top of attacker's N+2, or their own N+2?

Detectives always target the attacker’s latest leaked tip. If the attacker withholds and privately finds their own N+2, your sensors will see the pool’s jobs switch to prevhash = that N+2, and you switch to mining N+3 on top of it.

The reason is:

* You cannot profitably extend your own N+2, because you do not have the attacker’s hidden N+1. Any N+3 you mine on your own N+2 will remain unprovable until the attacker reveals N+1.
* By targeting the attacker’s current private tip every time it advances, you keep creating a child that becomes valid the moment they reveal. To realise any reward on their private branch, they must publish the missing parent(s), which collapses their lead.
* If they still refuse to reveal, they are burning their own N+1 (and possibly N+2) rewards while you have only diverted a bounded fraction of hash for a bounded time.

So here's the sequence:

1. Public at N. Attacker withholds N+1a.
2. Detective mines and broadcasts N+2d on top of N+1a. It waits as an orphan until N+1a appears.
3. Attacker withholds further and finds N+2a. Their jobs now reference N+2a.
4. Detectives pivot to mine N+3d on top of N+2a.
5. To get paid, the attacker must reveal N+1a (and N+2a if they have it). Once revealed, your N+2d/N+3d immediately contend, cutting their advantage. If they do not reveal, they forfeit those rewards.

## fluffypony | 2025-08-19T15:25:13+00:00
> This is with known dark pools. How do we counter unknown pools?

You cannot preempt a pool you cannot see. Detective mining only triggers when a pool leaks its private tip in Stratum jobs. But any pool that recruits external hash leaks by design, so the counter is to maximise sensor coverage. A perfectly closed, in-house farm can hide, but getting to ~34 percent that way is operationally very hard - AND we'd see the global / unknown hashrate increasing and have nothing to attribute it, which is a totally different threat to the one we've seen recently.

If another threat emerges that is trying to get 34% through bribery / merge-mining, it's easy to get "on the inside" with them and get the pool address, even if it's not publicly disclosed.

## tevador | 2025-08-19T16:56:26+00:00
> If the attacker withholds and privately finds their own N+2, your sensors will see the pool’s jobs switch to prevhash = that N+2, and you switch to mining N+3 on top of it.

The sensors won't recognize N+2, they will just see some unknown prev_id in the block template. Only the miner who found the winning nonce will recognize N+2.

This is an important distinction because the "detective miners" need to make sure that the secret chain actually starts from the known chain tip, otherwise they might accidentally help a 51% attacker build a parallel chain. This is a problem because the Monero block template doesn't include the block height.

Even if you can somehow ensure you are advancing the chain, the detective N+2 block would probably need to be empty to avoid accidental double spends because the set of transactions included in N+1 is unknown.

> nodes that see a block whose parent is unknown don’t attach it; they request or await the missing parent and hold the child as an orphan until the parent arrives

A quick look at the source code suggests that monerod will currently reject blocks with an unknown parent. However, this could be changed.

https://github.com/monero-project/monero/blob/389e3ba1df4a6df4c8f9d116aa239d4c00f5bc78/src/cryptonote_core/blockchain.cpp#L2122-L2126



## BawdyAnarchist | 2025-08-19T17:12:24+00:00
At a minimum it looks like a really good way to detect a potential selfish mining reorg in progress.

I wonder about the incentives of an attacker like Qubic, who might not be mining with profit in mind. (In their case, likely considering mining as a marketing expense for their token). But more generally, let's say that an attacker's goal is network disruption. They could simply withold the parent indefinitely, regardless of profit, and cause chain delays. If they do this enough times over 720 blocks, it might even cause difficulty adjustment swings.



## fluffypony | 2025-08-19T17:32:16+00:00
> > If the attacker withholds and privately finds their own N+2, your sensors will see the pool’s jobs switch to prevhash = that N+2, and you switch to mining N+3 on top of it.
> 
> The sensors won't recognize N+2, they will just see some unknown prev_id in the block template. Only the miner who found the winning nonce will recognize N+2.
> 
> This is an important distinction because the "detective miners" need to make sure that the secret chain actually starts from the known chain tip, otherwise they might accidentally help a 51% attacker build a parallel chain. This is a problem because the Monero block template doesn't include the block height.
> 
> Even if you can somehow ensure you are advancing the chain, the detective N+2 block would probably need to be empty to avoid accidental double spends because the set of transactions included in N+1 is unknown.
> 
> > nodes that see a block whose parent is unknown don’t attach it; they request or await the missing parent and hold the child as an orphan until the parent arrives
> 
> A quick look at the source code suggests that monerod will currently reject blocks with an unknown parent. However, this could be changed.
> 
> https://github.com/monero-project/monero/blob/389e3ba1df4a6df4c8f9d116aa239d4c00f5bc78/src/cryptonote_core/blockchain.cpp#L2122-L2126

Great points. Three clarifications and two concrete safeguards.

1) Sensors do not need to "recognize N+2" by hash, they only need to see that a pool's job prevhash switches from the public tip to an unknown hash. That flip is the signal a private child exists. In Stratum v2 this flip is explicit via `SetNewPrevHash`.

2) We can avoid helping deep reorgs by enforcing "adjacency" - ie. act only when you have continuity that the leak is the immediate child of the public tip, not some far-back ancestor. I think the way to do this is through two simple rules:

    * You observed the same pool issuing jobs on the public tip, then within a short window it switched to an unknown prevhash. Treat that unknown as N+1 of the current tip for that pool.
    * Prefer job streams that include a height field and require `height == public_height + 1` before acting. afaik most XMR pools include height in the job payload already?

If a pool does not expose height, fall back to the continuity rule above and require multiple corroborating sensors before diverting any hash. For extra safety, start with a tiny detective fraction and auto-backoff if the signal diverges.

3) Unknown-parent children and Monero today: you're right that current monerod tends to reject unknown-parent blocks rather than caching them. That weakens the pure "pre-propagate the child" angle, but it does not break the incentive: the attacker still has to reveal their parent to realise revenue, and when they do you immediately submit your child. A separate improvement would be to accept and hold unknown-parent children as orphans for later attachment.

NOTE: we don't need to have such a thing running globally on the network, we could make that code change and pools could run it and peer with each other, ensuring that they get pre-propagated child blocks even if the network as a whole doesn't all have them.

**Two other operational safeguards we can add:**

* Something like an "adjacency gate" - only divert when we have continuity evidence from the same pool: jobs on the public tip followed immediately by jobs with an unknown prevhash, plus share-acceptance on that job, and quorum across multiple sensors. If the unknown prevhash appears without that sequence, we do not divert.

* Empty detective blocks by default - build the detective child with only the coinbase to avoid any accidental double spends, since the N+1 transaction set is unknown. Thanks to tail emission, the base reward is fixed at 0.6 XMR, so empty blocks are clean and predictable.

In terms of the net effect, even if the attacker keeps privately extending on top of our published child, they cannot capture that middle reward and must still reveal to get paid. With adjacency checks, quorum, and empty detective blocks, we avoid aiding a deep parallel chain while keeping the attacker's expected gain down and their time to reveal short.

If useful, we can also ask that xmrig etc. add a pool-side requirement to include `height` in job messages.

## fluffypony | 2025-08-19T17:45:54+00:00
> At a minimum it looks like a really good way to detect a potential selfish mining reorg in progress.
> 
> I wonder about the incentives of an attacker like Qubic, who might not be mining with profit in mind. (In their case, likely considering mining as a marketing expense for their token). But more generally, let's say that an attacker's goal is network disruption. They could simply withold the parent indefinitely, regardless of profit, and cause chain delays. If they do this enough times over 720 blocks, it might even cause difficulty adjustment swings.

Totally agree on the first line: detective mining is an excellent early warning.

On a disruption-motivated attacker who withholds indefinitely:

1. Detective mining is still useful because it caps the size of any eventual reorg. If the attacker ever reveals, our pre-mined children on their leaked tips attach immediately, so their reveal collapses to at most a 1-block lead instead of a multi-block jump. That reduces the blast radius of each attempt, even if the attacker is not profit-seeking. ALSO it gives operators live telemetry to coordinate responses in real time (raise confs, re-peer, temporarily reallocate hash away from suspected pools).

2. Detective mining *can't* force a reveal; if an attacker is willing to burn money to slow blocks, they can withhold forever. The effect is a temporary slowdown (as you highlighted) until difficulty readjusts, but to my mind this is no different from an attacker bringing hashrate on and off just to mess with the difficulty.

I think the bottom line here is that if the attacker is willing to light money on fire, they can slow blocks proportional to their private hash until difficulty catches up. Detective mining will not stop that, but it prevents those withheld blocks from being converted into profitable or deep reorgs, and it gives the ecosystem early, actionable signals to blunt the operational impact.

## tevador | 2025-08-19T18:47:23+00:00
> This is an important distinction because the "detective miners" need to make sure that the secret chain actually starts from the known chain tip, otherwise they might accidentally help a 51% attacker build a parallel chain. This is a problem because the Monero block template doesn't include the block height.

I have to correct myself here. The block template indirectly commits to the height in the miner transaction, so accidentally creating a valid block at the wrong height is not possible. At most, the malicious pool could deceive the detective miners into wasting their hashrate.

## AwfulCrawler | 2025-08-19T21:03:44+00:00
I'm not sure if this approach would really help in the current situation.

If we take the recent multiblock reorgs - say 8 blocks for example.  I'm not sure I get how the detective mining will help that much.  My question is how would the outcome of that particular event have changed if detective mining had been in effect.

Assume that: 
1) The selfish miner ignores any detective mined blocks
2) No reduction in hashrate on the public chain due to detective mining hashrate being redirected
3) Detective mining hashrate is equal to the selfish miner

Assumption 2 is unrealisticly optimistic but we can then assume that the competition between the private and public chains turn out identically as in the actual reorg which took place.

I believe assumption 3 is probably too optimistic for the detective miner hashrate but it's just there to have something to work with.

Outcome:

- The selfish miner and public chain get built on as before up until the moment the selfish miner tries to publish its own 8 blocks at once
- At most 7(?) detective mined blocks are produced in the lead up to publishing the 8 block reorg.  These blocks do not build on top of each other
- Since the detective blocks do not build on top of each other, the earlier ones e.g. built on the first private block are almost certainly going to be rejected because they form an alternative chain extension of length 1 only.
- Only the later detective blocks have a realistic chance of being accepted
- End result is still an 8 block reorg, but the detective miners might now be the tip.  
- The selfish miner loses 0.6 xmr from what they would have got.

This is a positive outcome, but in reality the detective mining will reduce the hashrate on the public chain, slowing it down and therefore the loss of the tip of the reorg (not a certainty) is partially, or fully compensated for.

Am I missing something about how alternative chains are measured against each other?

## fluffypony | 2025-08-20T03:56:43+00:00
@AwfulCrawler detective mining helps **before** the reveal by cutting off private runs, and at reveal it **interleaves** detective blocks into the attacker's sequence, so long multi-block reorgs become much less likely and often much shallower.

What you might be missing:

1. Chain selection is by cumulative difficulty, *not* pure block count. At reveal time, each height N+k can land either the attacker's private block or the detective's pre-mined child; whichever lands first and then gets extended contributes that height's weight to the winning branch. That interleaving breaks the attacker's consecutive run.

2. Detective blocks are per-height tripwires, not a new chain. In other words, they do not stack on each other by design. They "booby trap" each private parent: when the attacker reveals N+1, the detective child for N+2 can attach immediately and deny the attacker that height. If detectives caught multiple private tips along the way, this can repeat at N+3, N+4, etc., fragmenting the reveal.

3. The big effect is probabilistic run-length collapse. So every time the attacker extends privately, detectives are racing to find a child on that same hidden tip. That adds a new transition that keeps returning the system to parity, which is why the paper's model shows long private runs become rare and the attacker's edge shrinks quickly as detective share grows. In other words, the "8-block" scenario becomes far less likely *to form in the first place*.

4. Today, monerod typically rejects unknown-parent children, so even absent any change to this, detectives would resubmit their N+2, N+3, etc. immediately when N+1 appears. You then get a race at each height. Even a few detective wins break the attacker's consecutive sequence and reduce the realised reorg depth. A daemon option to cache unknown-parent children would strengthen this further.

5. Re: "attacker loses only 0.6 XMR", if detectives win *ANY* heights, the attacker loses **that** subsidy and any fees for those heights. Empty detective blocks are a safety choice to avoid accidental double spends when N+1's tx set is unknown; they still deny the attacker that height's revenue. In future FMCP might allow some conservative tx inclusion, but I don't know that's even necessary.

About the three assumptions:

* Assumption 1, attacker ignoring detective blocks is fine to assume - detectives still deny heights at reveal.
* Assumption 2, no public-chain slowdown is conservative for the defender. In practice a pool diverts a small fraction first and ramp only with corroboration, keeping public production healthy.
* Assumption 3, detective hash equal to attacker is generous, but the paper shows you DO NOT need hashrate parity; even modest detective share materially cuts the attacker's edge and the odds of long runs.

Basically, under detective mining, an 8-block reveal attempt rarely assembles as 8 clean attacker blocks. Pre-mined detective children at multiple heights fragment the reveal and reduce the realised reorg, while the ongoing race during withholding makes long private runs statistically hard to build. That is *exactly* the mechanism quantified in the detective-mining paper, and would have totally rekt this "attack".

## AwfulCrawler | 2025-08-20T05:04:40+00:00
You're right I am not 100% on how the cumulative difficulty is used to select block candidates and this might be what made me confused.

I was going off the assumption that if e.g. the first detective block outscores the 2nd attacker block, then it wouldn't matter that much since there are 6 more attacker blocks to go adding cumulative difficulty to the attacker's proposed chain, whereas there is only the one detective block (with no blocks on top) to compete with that.

If, however, the 1st detective block outscoring the 2nd attacker block could cut it off, this becomes a much better situation.

I need to take a closer look at the paper and get a better idea of how the alternative chains compete before taking any more space up here, but your response gives me something to go off of, thanks.

## zawy12 | 2025-08-20T08:08:05+00:00
In combination with this, when there's a tip race honest miners should choose to work on the tip with the best timestamp. The "detective tip" will have a good timestamp because it's revealed immediately, but the attacker's tip doesn't because he assigned the timestamp and solved the block before he knew when he would have to release it.  This reduces the attacker's "gamma" below 0.5 (below neutral tie-breaking).

Releasing a bunch of blocks at once means he's using a "stubborn" selfish mining tactic (there are 3 types).

If you know there's an attack, there's another mitigation technique: copy the attack. This cancels each other's gains. If they're both 33%, the remaining "agnostic" 33% who's releasing blocks immediately come out the same as the attackers. I don't know if this is better than detective mining or not.

## SChernykh | 2025-08-20T08:15:12+00:00
@fluffypony 
>  at reveal it interleaves detective blocks into the attacker's sequence

This is simply not true. The attacker mines only on top of **their** blocks, so all the detective blocks will be orphaned. Except the very latest one, at the tip.

## fluffypony | 2025-08-20T08:41:53+00:00
> This is simply not true. The attacker mines only on top of **their** blocks, so all the detective blocks will be orphaned. Except the very latest one, at the tip.

Sorry I could have worded that better - you're right that the attacker never mines on detective blocks. "Interleaving" does not mean the attacker builds on our blocks. It means that at reveal time each contested height has 2 competing children - the attacker’s child and the detective’s child - and the network adopts whichever child for that height propagates first and then gets extended. Some heights resolve to A, others to D, so the final accepted sequence often alternates.

Just to make it as clear as possible:

- Before reveal, detectives mine a child on each leaked private parent. They target the attacker's current private tip, not their own chain.
- At reveal of N+1a, there are now two valid candidates for N+2: the attacker's N+2a and the detective's N+2d. Nodes will accept whichever they see first and then extend. Same at N+3, N+4, and so on if detectives have pre-mined those children of the attacker's leaked tips.
- The attacker "only mining on their blocks" does not orphan detective children by fiat. Orphaning is decided by arrival and extension at each height under cumulative difficulty. If comparable hash races those heights, some fall to A and some to D - that is the interleaving we mean.
- If detective hash is similar to the attacker's, the chance the attacker wins all k heights in a run is roughly 0.5^k. Long clean reveals become vanishingly likely. Even a few detective wins break the consecutive run and shrink realised reorg depth.

Put differently: detectives do not help the attacker. They pre-position rival children on the attacker's hidden parents so that, at reveal, some contested heights resolve to the defender rather than the attacker. That fragments the reveal and makes deep, clean reorgs much harder to land. The more hashrate is given to detective mining by pools, the faster these blocks happen, and the worse it is for the attacker.

## zawy12 | 2025-08-20T08:47:03+00:00
Another technique is for honest nodes to ignore reorgs for $\sqrt{N}$ block times where N is the size of the reorg.  This requires the reorg tip to prove it was on the >50% hashrate side of the network partition by ~1 standard deviation, or that it had that amount of luck.  It delays repairs in an "honest" network partition and hurts a miner if the majority of the hashrate doesn't follow the rule. Of course a node that was off line doesn't follow the rule when it comes online because he already *knows* there was a "network partition" by being offline.  Similarly, if nodes know there was a partition by there being a long delay between blocks, they ignore the rule according to some additional rule.  Selfish mining works because nodes are switching tips without any good "proof" that the new tip has the Proof of Work lead (i.e. that it had the majority hashrate).

## SChernykh | 2025-08-20T08:53:43+00:00
> some contested heights resolve to the defender rather than the attacker

I still don't quite agree. What I've seen in reality, is that the attacker gets a comfortable lead over other pools (2 blocks), and keeps mining as long as they have this lead. As soon as the lead reduces to 1 block, they publish their chain. This is how they reached 8-block reorg - due to pure luck when they got a 4-block lead in the beginning.

So when they release block N+8a, network will see block N+8a, N+7a, ..., N+1a and will switch to it because network is only at N+7. It's impossible to have the interleave "N+8a, N+7d, N+6a, N+5d, ..." becase N+8a points to N+7a, not N+7d as its parent.

## zawy12 | 2025-08-20T09:02:56+00:00
> At reveal of N+1a, there are now two valid candidates for N+2: the attacker's N+2a and the detective's N+2d. Nodes will accept whichever they see first and then extend. 

If nodes chose the tip with the most accurate timestamp, the attacker loses. (on average)

For the case of 33% attacker and 33% detective, the attacker's gamma reduces from 0.25 for detective alone to 0. He has 33% chance of winning instead of 50%.

## stringhandler | 2025-08-20T09:06:21+00:00
Is there any scope for this:

**Allow missing (or dummy) monero blocks temporarily, if the difficulty and number of transactions can be verified.** 

Basically, if the randomx via  nonce is verifiable, then nodes can add a dummy block, which consists of only the hash, nonce and prev_hash, and continue. 

So if you know enough of the prev_header, non-selfish mining pools could build on top of this dummy block (or chain of dummy blocks), knowing they will be accepted, even if the selfish pool never publishes the block.

UTXOs can't be used for 10 blocks anyway, so the data isn't needed. Then, if the data is still missing, the block should mark it as missing in the n+10'th block. At this point, any data in the block is lost, but the chain can continue.

I think if you could change the stratum hashing blob enough, you could force the selfish pool to reveal enough of this data to build a chain with a dummy block. 

## fluffypony | 2025-08-20T09:43:09+00:00
@zawy12 Thanks for the ideas. Some quick thoughts on it:

1) Tie-breaking by timestamp during a tip race

* Pools can choose a local policy to prefer the block whose timestamp is closest to now when two tips are neck-and-neck. That can reduce the attacker’s gamma in practice because honest blocks generally propagate immediately, while withheld blocks often have weirder timestamps.
* Caveat: timestamps are miner-chosen within bounds. In Monero a block must be ≥ median of the last 60 and ≤ now + 2 hours, so an attacker can game toward the limit. Use timestamp only as a soft tie-breaker at pools, not as a consensus rule.

2) Releasing many blocks at once = stubborn strategy

Correct - that matches the stubborn mining family generalised beyond the original Eyal-Sirer SM1 strategy. The literature shows stubborn variants can be profitable in some regions, which is why cutting private runs is valuable.

3) "Copy the attack" to cancel gains

Two attackers do tend to cannibalise each other - see the Miner’s Dilemma - but this still degrades network health and honest revenue, and normalises withholding as a tactic. Detective mining is preferable because it uses leaked prevhash to collapse private leads without honest miners withholding their own blocks.

4) Ignore reorgs for sqrt(N) block times

That is effectively a reorg-delay/finality rule. It would be a consensus-level behaviour change with liveness risks during genuine partitions and creates timing games with timestamps. Monero’s chain selection is cumulative difficulty, not timestamps or wait rules, so adopting this would be a much bigger change than pool-side detective mining.

Detective mining still helps in your scenarios:

* It adds a per-height tripwire: at each leaked parent there is a pre-mined competing child ready to race when the parent appears, which statistically breaks long clean runs that stubborn strategies rely on. That is exactly why selfish-miner edge shrinks as detective share grows in the models.
* All of this is deployable at pools or Stratum proxies - no protocol changes needed.

At the end of the day, timestamp-weighted tie-breaks can be a small, a pool-local nudge; "copy the attack" hurts everyone; reorg-delay rules are heavy and risky. Detective mining directly targets the attacker’s private lead with pool-only changes and plays well with faster propagation and conservative pool tie-breaking.

## fluffypony | 2025-08-20T09:48:30+00:00
> I still don't quite agree. What I've seen in reality, is that the attacker gets a comfortable lead over other pools (2 blocks), and keeps mining as long as they have this lead. As soon as the lead reduces to 1 block, they publish their chain. This is how they reached 8-block reorg - due to pure luck when they got a 4-block lead in the beginning.
> 
> So when they release block N+8a, network will see block N+8a, N+7a, ..., N+1a and will switch to it because network is only at N+7. It's impossible to have the interleave "N+8a, N+7d, N+6a, N+5d, ..." becase N+8a points to N+7a, not N+7d as its parent.

I think we are talking past each other on what "interleave" means.

- Interleaving does not require the attacker to build on detective blocks. It is about what each node accepts at each height when the attacker reveals.
- Reveal is not atomic. Even if the attacker dumps N+1a...N+8a rapidly, every node still processes a sequence: sees N+1a, then later sees some N+2 child, then later N+3, etc. There is always a gap between those arrivals across the network.
- Detectives use that gap. The moment N+1a appears, we resubmit N+2d. Some peers will see N+2d before N+2a and adopt it. On those peers, N+3a is then invalid until they later see N+2a and consider a reorg. Meanwhile honest hash on those peers can extend N+2d. Repeat at later heights if we have N+3d, N+4d, ...
- The attacker cannot force all peers to receive N+2a before N+2d. Gossip and validation are sequential and latency is heterogeneous. With comparable detective hash, the chance the attacker wins every contested height falls exponentially with run length. That is what I mean by "interleaving" outcomes at reveal.
- Your example "N+8a points to N+7a, not N+7d" is correct as a block header fact, but beside the point. Interleaving is not about what the attacker mined. It is about which child of each height lands first and then gets extended by enough hash to become the accepted history on that part of the network (ie. CUMULATIVE PoW difficulty, which the attacker cannot sustain at their <51% hashrate).

Detective blocks are intentionally independent per height. They are tripwires that deny the attacker specific heights at reveal. Even a few wins break a long clean sequence and reduce realised reorg depth.

The attacker does not orphan detective blocks "by definition". At reveal there is a real race at each height between A's child and D's child. Some heights resolve to A, some to D, which fragments what would otherwise be a clean 8-block reveal.

## fluffypony | 2025-08-20T09:55:12+00:00
> Is there any scope for this:
> 
> **Allow missing (or dummy) monero blocks temporarily, if the difficulty and number of transactions can be verified.**

Interesting idea, but on Monero this would be a protocol change with some safety issues:

- PoW commits to more than prev_hash and nonce. The Monero block hash is computed over a "block hashing blob" that includes the block header, the Merkle root of the block's transactions, and the transaction count. You cannot verify or later reconcile PoW without the tx root and count. 
- You cannot validate the coinbase without the full block. Monero checks the miner transaction against the emission schedule and the dynamic block weight penalty, which depends on the recent median block weight and the actual block weight and fees. That requires the full tx set. 
- "UTXOs can't be used for 10 blocks anyway" is something that will likely go away with FMCP and some of the other protocol changes coming down the pipe.
- Accepting headers without data is a DoS and inflation risk. Invalid coinbases, oversized blocks, or bad txs could be locked in without anyone being able to verify or unwind deterministically. It would also partition the network between nodes that accept placeholders and those that do not.
- Changing Stratum does not help here. Stratum is a pool protocol. It cannot force consensus nodes to accept incomplete blocks, and an attacker can run a custom pool anyway. 
- Current monerod behavior aligns with this: blocks whose parent is unknown or whose data is missing are rejected or treated as orphaned, not inserted as placeholders.

Admittedly I think the last point should change, and is relatively easy to do so.

## stringhandler | 2025-08-20T10:06:04+00:00
> Changing Stratum does not help here. Stratum is a pool protocol. It cannot force consensus nodes to accept incomplete blocks, and an attacker can run a custom pool anyway.

What I meant here is to change the input (block_hashing_blob) into RandomX in such a way that all the parameters needed to construct a dummy block must be published by the malicious pool via Stratum, hence revealing enough to construct a valid chain

## fluffypony | 2025-08-20T10:17:00+00:00
> What I meant here is to change the input (block_hashing_blob) into RandomX in such a way that all the parameters needed to construct a dummy block must be published by the malicious pool via Stratum, hence revealing enough to construct a valid chain

I get what you're aiming for, but I don't think this can be done at the Stratum layer without changing consensus.

- RandomX's input is fixed by consensus to the "block hashing blob" which already includes more than just prev_hash and nonce. It is the serialised block header plus the Merkle root of the block's transactions and the transaction count. Pools can't redefine that via Stratum; if they did, the result wouldn't validate. 
- Even if a pool publishes the Merkle root and tx count in jobs (they effectively do, because miners hash the blob), nodes still must see the actual transactions to verify the coinbase amount, block weight penalty, and fee accounting. You can't safely "continue on dummy headers" in Monero - full validation requires the tx set (otherwise it's a massive DoS risk, at the very least). 
- Header-only acceptance would be a protocol change with serious risks: nodes could be led to extend an invalid chain (bad coinbase, oversized block, bad tx set) they cannot verify yet. That's why monerod rejects unknown-parent or incomplete blocks today rather than inserting placeholders. 
- A malicious pool could also fabricate Merkle roots in job blobs to steer honest hash, then never reveal matching transactions. Stratum can't police that - only full block validation can.

## stringhandler | 2025-08-20T10:21:06+00:00
Yeah I meant change consensus and Stratum

## SChernykh | 2025-08-20T13:56:41+00:00
> Detective blocks are intentionally independent per height. They are tripwires that deny the attacker specific heights at reveal. Even a few wins break a long clean sequence and reduce realised reorg depth.

> The attacker does not orphan detective blocks "by definition". At reveal there is a real race at each height between A's child and D's child. Some heights resolve to A, some to D, which fragments what would otherwise be a clean 8-block reveal.

Still, in the end, when all blocks propagate, and N+8a is the longest chain, it will be 8 blocks from the attacker that will end up in the blockchain. All the other blocks will be orphaned. The only detective block that can survive it, will be N+8d.

## fluffypony | 2025-08-20T15:12:36+00:00
> Still, in the end, when all blocks propagate, and N+8a is the longest chain, it will be 8 blocks from the attacker that will end up in the blockchain. All the other blocks will be orphaned. The only detective block that can survive it, will be N+8d.

That conclusion only holds if the attacker's 8-block chain is *already the heaviest path everywhere at reveal*. That is the assumption, not the consequence.

With detective mining, at each contested height there are two children of the same parent: A's and D's. If any D child lands first on a chunk of the network and gets even a single honest extension before A's counterpart arrives, then on those nodes A's block for that height will not be on the eventual main chain. So more than just the latest detective block can survive.

So imagine this playing out:

* N is public. Attacker withholds N+1a.
* Detectives have N+2d ready. When N+1a appears, some peers see and extend N+2d to N+3h before they ever see N+2a.
* When N+2a finally arrives, that path is lighter on those peers, so they keep N+2d → N+3h. Any later A blocks that depend on N+2a cannot be accepted there unless they outweigh the competing path.

Only in the special case where the attacker wins the race at every height after reveal do you end up with N+1a...N+8a and all D blocks orphaned. Detective mining exists precisely to make that all-A outcome unlikely as run length grows.

## j-berman | 2025-08-20T16:10:23+00:00
In this scenario, the attacker will sometimes still win the race to block N+2a against the honest hash, and trigger a reorg on the main chain.

Considering this proposed defense is assuming >50% of the hash rate defending, and that reorgs are still inevitable given above, why not just have the defending >50% hash rate instead defend by ignoring the attacker entirely, and just don't build on any of their blocks?

It would be potentially more disruptive to the network, but it would cut the attacker's revenue to 0 under the same hash rate assumptions (defenders have >50% hash rate and are colluding to implement some strategy to protect the network).

If assuming defenders have a higher hash rate than the attacker, but less than 50%, and the numbers still work out to cutting the attacker's revenue some amount (a little hard to tell from the paper how that is slated to shake out), then the strategy still seems to have merit to me.

____

There is one other concern with this proposal I figure is worth voicing: if the attacker has a method to communicate with its miners privately (e.g. they are in complete control of their own hash rate, or retain significant control over the hash rate), it seems the strategy would fail. Worst case seems that honest hash is temporarily diverted, and the strategy could be pulled back easily as this would be detectable. So it may still be worth attempting against the particular threat of a public pool.

## fluffypony | 2025-08-20T18:27:40+00:00
> In this scenario, the attacker will sometimes still win the race to block N+2a against the honest hash, and trigger a reorg on the main chain.
> 
> Considering this proposed defense is assuming >50% of the hash rate defending, and that reorgs are still inevitable given above, why not just have the defending >50% hash rate instead defend by ignoring the attacker entirely, and just don't build on any of their blocks?
> 
> It would be potentially more disruptive to the network, but it would cut the attacker's revenue to 0 under the same hash rate assumptions (defenders have >50% hash rate and are colluding to implement some strategy to protect the network).
> 
> If assuming defenders have a higher hash rate than the attacker, but less than 50%, and the numbers still work out to cutting the attacker's revenue some amount (a little hard to tell from the paper how that is slated to shake out), then the strategy still seems to have merit to me.

Appreciate the input. Detective mining does not assume a >50 percent defensive cartel, and it avoids the risks in "just ignore the attacker's blocks."

You can't "ignore attacker blocks" even with majority hash:

* You cannot reliably know which valid block came from the attacker. Blocks have no provenance field. A pool's Stratum leak is not visible to consensus nodes. You will inevitably censor honest blocks or be trivially evaded.
* Telling a majority to locally reject otherwise valid blocks is a de facto consensus fork. One side mines a policy chain, the other mines the protocol chain. That is far riskier than pool-side detective mining.
* It normalises permanent censorship. Even if well intended, you are building a rule to reject valid blocks by origin.

Instead, with detective mining we have two key advantages:

* Works with any positive defensive share. You do not need majority coordination (or any coordination across pools), and I largely think it's better if pools do this independently instead of trying to cooperate (better for decentralisation I mean). As detective share rises, long private runs become rare and deep reveals tend to fragment, reducing realised reorg depth and attacker EV.
* Pure pool or proxy change. No protocol edits, no coordination across all honest hash, no permanent policy that can split the chain.

Also the "attacker wins N+2 sometimes" scenario is fine, imho. Reorgs are not eliminated. They become shorter and less profitable. At reveal, each height is a race between A's child and D's child. The chance the attacker wins every contested height falls exponentially with run length. That is the lever.

> There is one other concern with this proposal I figure is worth voicing: if the attacker has a method to communicate with its miners privately (e.g. they are in complete control of their own hash rate, or retain significant control over the hash rate), it seems the strategy would fail. Worst case seems that honest hash is temporarily diverted, and the strategy could be pulled back easily as this would be detectable. So it may still be worth attempting against the particular threat of a public pool.

It's true that detective mining cannot see a perfectly closed farm, but *adding* 34% hashrate in secret is a challenge. If they try recruit miners in any way that is publicly known, someone will infiltrate the cabal, and they just need to work with a pool that has detective mining in order to thwart the attack.

Also, importantly, the "ignore attacker" idea still fails here for the same reason as above: you cannot identify their blocks on chain.

## SChernykh | 2025-08-20T18:53:33+00:00
> When N+1a appears, some peers see and extend N+2d to N+3h before they ever see N+2a.

I watched their reorg in real time. It took just a few seconds to broadcast all 8 blocks, also because they were mining empty blocks. Chances to go from N+2d to N+3h are slim to none. This won't work.

## j-berman | 2025-08-20T19:14:04+00:00
@fluffypony  I disagree with some of the framing in your arguments there, but nonetheless, I agree the strategy seems plausible on first pass for the scenario where <50% of the hash rate is attempting it. I'm not convinced it's superior if >50% hash rate is willing to ignore the attacker's blocks; however, it would be valid to say that since detective mining does not require >50% to work, then there is less of a centralizing factor not present in the scheme to some extent.
 
 > You cannot reliably know which valid block came from the attacker

If you can reliably detect the attacker's block hashes in this detection scheme (because they are publicly sharing their block hashes), that implies you can reliably detect the attacker's blocks.

> Telling a majority to locally reject otherwise valid blocks is a de facto consensus fork. One side mines a policy chain, the other mines the protocol chain. That is far riskier than pool-side detective mining.

Detective mining implies the defenders ignore the non-attacker chain (i.e. locally reject otherwise valid blocks), and when the attacker releases their hidden block, reorg the chain to the chain the defenders *have* been mining on. By the same logic it would also be a de facto consensus fork. I think this point is moot.

> It normalises permanent censorship. Even if well intended, you are building a rule to reject valid blocks by origin.

Detective mining is arguably worse on this front. First, it would seem to require honest hash mine empty blocks for the reasons stated above, i.e. actually censor transactions. Second, it's building a rule to accept an attacker's *originally hidden* blocks by origin, and reject other honest blocks.

> You do not need majority coordination

You don't need majority coordination for >50% either. The >50% hash rate miners can mine on the non-attacker chain, independently with their own block templates across pools.

> Pure pool or proxy change. No protocol edits, no coordination across all honest hash, no permanent policy that can split the chain.

The chain "splits" in both schemes and neither require protocol edits nor explicit coordination across all honest hash. The defensive mining works by triggering a reorg on top of the attacker's block. I also think this is a moot point.

From a network stability standpoint, I think the main benefit of the defensive mining approach is fewer reorgs.

______


> I watched their reorg in real time. It took just a few seconds to broadcast all 8 blocks, also because they were mining empty blocks. Chances to go from N+2d to N+3h are slim to none. This won't work.

This strategy only works if their first block hash was broadcasted to their network well before they mined the other 7 blocks. So the defenders divert toward mining on top of that first block hash as soon as it's broadcasted. So long as defenders divert toward mining on top of that broadcasted block hash, it does seem plausible to me that it *should* end up cutting the attacker's revenue some amount.

## fluffypony | 2025-08-20T19:39:42+00:00
> I watched their reorg in real time. It took just a few seconds to broadcast all 8 blocks, also because they were mining empty blocks. Chances to go from N+2d to N+3h are slim to none. This won't work.

Did they MINE those blocks in a few seconds? Obviously not. We're NOT relying on extending N+2d *after reveal*.

The mechanic is this: while the attacker is growing the private run, they must keep pushing new prevhashes to their workers. Detectives target each of those leaked tips in real time. By the time the attacker reveals N+1a...N+8a, we have pre-mined rival children D2, D3, ... for several of those heights and submit them immediately when their parents appear.

The only way the final chain ends up as N+1a...N+8a is if the attacker won the race at every height during the private run. With comparable detective hash, the chance of a clean 8-for-8 sweep is roughly (α/(α+δ))^8. If α ≈ δ, that is about 0.4 percent. In expectation, some heights flip to D, so more than just the tip can survive.

So the claim "only N+8d could ever survive" assumes away the per-height races that happen before reveal. The defence's main effect is to clip private runs as they form, not to out-race an 8-block burst *after* reveal.

Here's a table showing an imaginary attack from block 1000 @ 223344 cumulative diffi

| t (mm\:ss) | Attacker actions                                                    | Detective pool actions                                                                                  | Honest miners / pools                                                                                                     | Dominant public tip after this step (height, cum diff)                                                           |
| ---------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 00:00      | Finds 1001a privately. Updates jobs to prevhash = 1001a. Withholds. | Sensors see off-tip prevhash. Build counter template for 1002d. Divert small hash slice.                | Mine on public tip 1000.                                                                                                  | (1000, 223344)                                                                                                   |
| 02:00      | Still mining on 1001a.                                              | Finds 1002d on top of 1001a. Broadcasts, queues for instant resubmission once 1001a appears.            | Still on 1000.                                                                                                            | (1000, 223344)                                                                                                   |
| 04:00      | Finds 1002a privately. Updates jobs to prevhash = 1002a. Withholds. | Switch sensors to target 1003d on 1002a.                                                                | Still on 1000.                                                                                                            | (1000, 223344)                                                                                                   |
| 06:00      | Extends privately toward 1003a. Withholds.                          | Finds 1003d on 1002a. Broadcasts, queue until parent appears.                                           | Still on 1000.                                                                                                            | (1000, 223344)                                                                                                   |
| 08:00      | Reveals 1001a and 1002a in quick succession.                        | Immediately resubmits queued 1002d and 1003d as parents appear.                                         | Peers accept 1001a. At height 1002, some see 1002d before 1002a and adopt it.                                             | Often becomes 1001a accepted: (1001, 223345). Height 1002 contested.                                             |
| 08:02      | Continues broadcasting.                                             | Keep resubmitting per leaked tip as it appears.                                                         | On a large slice of peers, 1002d is accepted before 1002a. Honest hash on those peers begins working on 1003h atop 1002d. | Common outcome now 1000 → 1001a → 1002d: (1002, 223346)                                                          |
| 10:00      | Broadcasts 1003a.                                                   | N/A.                                                                                                    | Honest miners find 1003h on top of 1002d on part of the network.                                                          | A frequent resolution: 1000 → 1001a → 1002d → 1003h: (1003, 223347)                                              |
| 12:00      | If more withheld blocks exist, tries to push them.                  | If attacker had leaked 1003a earlier, detectives had 1004d queued and now resubmit it as 1003a appears. | Honest miners keep extending the heaviest path they observed first.                                                       | Heaviest path often remains A at 1001, D at 1002, H at 1003. Example tip (1004, 223348) after next honest block. |


## fluffypony | 2025-08-20T19:53:48+00:00
@j-berman hmmmm...I just want to make sure I understand what you're suggesting. Are you saying pools should use detectives and then go "we refuse to build on block hashes N, N+1 etc" because they know they're attacker's block hashes? That way the 8-block chain drops, but no pools EXCEPT the attackers build on it?

If I am understanding you correctly, then my issue is that using detectives to hard-reject specific block hashes is brittle and unsafe. imho we should use detectives to steer where you mine, not what you accept.

Here's why I suspect that to be the case:

* Identification is not authoritative. Detectives see leaked prevhashes on some Stratum connections. An attacker can equivocate per connection, rotate endpoints, or keep hash fully private. You will sometimes mislabel and refuse an honest block, or split from peers who did not see the same leak.

* It creates a policy fork. If a leaked block later sits on the objectively heaviest chain, pools that refuse it are intentionally mining a minority fork. Unless you truly control a stable >50 percent and everyone enforces the same list, you degrade liveness and risk a durable split.

* It is after-the-fact. A blocklist does not stop the private run from forming. Detective mining's value is pre-reveal: it clips the run by pre-positioning children at each leaked tip and lowering the odds of a clean multi-block reveal.

* It normalises censorship by origin. You are enshrining a rule to reject valid blocks based on who you think mined them, which can be spoofed and sets a bad precedent.

If we want to focus on things that are safe, require no protocol changes, and can't be abused to the detriment of the network:

* Keep consensus behaviour unchanged: follow cumulative difficulty.
* Use detectives only to decide where to point hash when a leak is corroborated.
* Add soft tie-breaks at pools during races (first-seen, timestamp-nearest-now) rather than hard rejections.
* Queue and resubmit empty detective children the instant their parents appear; this denies the attacker consecutive heights without any origin filter.
* Bound risk with quorum, persistence, share-acceptance checks, and small-then-ramp diversion.

Ultimately, if you have a real, coordinated, durable majority you can overpower almost any tactic, but blocklists by hash are a blunt tool that invite forks and mistakes - and it is a MASSIVE centralisation vector that I really hope we all want to avoid. Detective mining achieves defence without changing validation, without a cartel, and with far lower blast radius.


## j-berman | 2025-08-20T20:28:40+00:00
Seems we will likely go in circles at this point, you didn't really address my points. I maintain the strategy is sub-optimal if >50% hash is on board for it.

## zawy12 | 2025-08-20T22:32:51+00:00
### Detectives with equal hashrate => honest non-detectives break even?

If an attacker has 33% and the detectives have 33%, the non-detectives will break even. Figure 11 in the paper shows attacker, detectives, and non-detectives each have 33% revenue when they each have 33% hashrate. Look at the "neutral tie-breaking" chart (&gamma; = 0.5) where the lines for honest revenue Rh and selfish revenue R_s50 cross at 33% hashrate and they each get 33% revenue.  R_s50 is when detective hashrate equals non-detectives, so all 3 groups have 33% hashrate and 33% revenue. Unfortunately, I don't immediately see in the paper what happens in general if detective hashrate always equals attacker's hashrate, but my estimation via complex reasoning is that everyone would break even at all values of equal hashrate.  

Since the detectives release a block first, they have a slight advantage over selfish miners by lowering &gamma; a little below 0.5.  If pools use the timestamp check, they have another advantage.  

### Copy cats with equal hashrate => honest miners break even?

Let's say attacker hashrate = copy cat hashrate = 40% hashrate.  A perfect copy cat seems to mean both attackers lose 50% of their blocks to races. The 20% honest miners are sitting there watching and helping them attack each other. They might also lose 50% of their blocks. If that's the case, the difficulty would soon drop to half due to everyone having 50% orphans, then they're all breaking even as if there was no attack. And if they all stick around and start being honest, they'll regain their losses as it will take the difficulty as long to rise as it fell. So the copy cat method may not costs honest miners anything when copy cat hashrate is equal to attackers hashrate. 

**What's the difference between detectives and copy cats if everyone breaks even in both?** 
There aren't as many orphans in the detective method so difficulty doesn't drop as low.

I had further comments in response to @fluffypony but I didn't want to pollute this thread with off-topic discussion, so I put it [here](https://github.com/zawy12/difficulty-algorithms/issues/87#issuecomment-3208266376) on my own github.

## SChernykh | 2025-08-20T22:47:02+00:00
> The only way the final chain ends up as N+1a...N+8a is if the attacker won the race at every height during the private run. 

No. The only way the final chain DOESN'T end up at N+1a...N+8a is if there is a competing block N+8d and miners mine N+9h. But even in this case, the attacker gets 7 blocks instead of 8.

Because, I repeat again: attacker announces that their chain tip is N+8a, and it has higher cumulative difficulty than everything else at the moment (this is in the logic of their selfish mining - they only commit to building a long chain if they get a 2-block lead by luck in the beginning).

So all honest nodes naturally will **request** blocks N+7a, N+6a, ..., N+1a from attacker's nodes (following the chain of prev_id hashes), just to switch to that chain because this is the consensus rule - the highest cumulative difficulty chain wins.

## fluffypony | 2025-08-21T04:46:31+00:00
> Seems we will likely go in circles at this point, you didn't really address my points. I maintain the strategy is sub-optimal if >50% hash is on board for it.

I agree that >50% is optimal, I said as much in the first post - and, to that end, to get the top 3-4 pools to implement this is definitely achievable.

## fluffypony | 2025-08-21T04:56:31+00:00
> No. The only way the final chain DOESN'T end up at N+1a...N+8a is if there is a competing block N+8d and miners mine N+9h. But even in this case, the attacker gets 7 blocks instead of 8.
> 
> Because, I repeat again: attacker announces that their chain tip is N+8a, and it has higher cumulative difficulty than everything else at the moment (this is in the logic of their selfish mining - they only commit to building a long chain if they get a 2-block lead by luck in the beginning).
> 
> So all honest nodes naturally will **request** blocks N+7a, N+6a, ..., N+1a from attacker's nodes (following the chain of prev_id hashes), just to switch to that chain because this is the consensus rule - the highest cumulative difficulty chain wins.

You are 100% right about the burst-reveal corner case. If the attacker dumps 8 blocks fast and that pure A-chain is already heaviest everywhere, nodes will switch to 1001a...1008a. In that case most detective children get orphaned, possibly except the tip.

The key effect of detective mining is *earlier*, during formation of the private run, not after reveal:

* While the attacker is growing the run, every leaked tip has a detective child racing it. That adds a transition that keeps cutting the private lead. Long clean runs like 8 become far less likely in the first place.

* At reveal, detective children only survive if they beat the attacker's child for that height to a meaningful slice of hash and get extended. With today's behaviour and a very fast multi-block reveal, that often means only the last contested height can flip.

So I will restate my claim more precisely as: if the attacker both manages to build a long private run and then blasts it fast enough that their child wins the race at each contested height on most peers, the final chain can be all A. Detective mining makes the first part rare, and sometimes flips one or more of the last contested heights on reveal, but it does not guarantee interleaving in every burst.

Detective mining is about reducing the frequency and realised depth of long reorgs, not guaranteeing that an already-formed 8-block burst will always be split up on reveal.

## AwfulCrawler | 2025-08-21T06:28:58+00:00
After some further clarifying and reading through the paper, I have some additional comments to make regarding the contents of the
paper, the assumptions it makes and the applicability of the results.

- The paper does not have cumulative difficulty as a consideration, but just counts blockchain length as the deciding factor when faced with two competing chain tips

- There is a probability, gamma, of following the selfish miner's fork for chains of equal length, which is varied in the simulations.  gamma=0.5 probably corresponds the most closely to the cumulative difficulty criterion

- They vary the percentage of honest miners who switch to detective mining.  They use three values.
Here I believe there is a typo in the paper.  They say they use the hashrate delta for detective mining with values
0, 0.5/(1-alpha), and 1/(1-alpha), where alpha is the (proportion of) hashrate of the selfish miner and (1-alpha) the hashrate
for the rest of the miners.  However then they introduce theta as the "percent ratio of detective miners except selfish miners",
which I believe means delta/(1-alpha)*100.  They say that they investigate theta=0%, 50% and 100%.
So I think they meant delta = 0, 0.5(1-alpha) and (1-alpha).  Also  delta = x/(1-alpha) > 1 for certain values of alpha,
and the model needs all hashrates represented as percentage of total hash.  So that's further confirmation that they probably
mean TIMES (1-alpha) rather than DIVIDED BY (1-alpha) when defining delta.

- They then ASSUME that a selfish miner will publish their hidden chain as soon as they see a detective block, and all of their
modeling is based on this assumption.  They do not model at all any situation where the selfish miner ignores the detective blocks.  In their model the selfish miner ALWAYS publishes their chain when they see the first detective block.  They never investigate the case where detective blocks are ignored.

- They only justify this assumption by saying: 
>If the detective miners find a new valid block on the private chain, they publish it, and then the selfish mining pool can not keep its chain secret anymore [note: yes they can].  If a block after the private chain is published, the selfish mining pool should admit that it is not in the lead anymore [note: no reason for this is given].  In this situation, for getting revenue, the smartest way is to open up all selfish mining pool's private chain and pray for honest miners to choose its chain.

Nothing in their statement gives a reason WHY.  I.e. this is merely an assumption and not a reasoned deduction.

- This assumption allows silly choices for theta, like 100%, since even though in that case the honest miners are not even mining
the main chain anymore, they will eventually mine a detective block and the selfish miner will then get triggered to publish
their block.  But what if they don't publish?  The paper never addresses this except for saying publish the blocks "and pray"
is the best strategy.  You do not need to pray when you know the cumulative difficulty of your private chain vs the public honest
chain.  You KNOW that your private chain is the best or not.  No religion required.

- This assumption does not even seem to make sense for the parameter values for theta that they use:
it IS more profitable to ignore the detective blocks.  At 100% detective hash rate (i.e. NONE!!! dedicated to the honest chain),
the selfish miner can make a consecutive chain of arbitrary length.  They can even go until there is no
competing detective block at the tip and essentially publish when he likes, taking 100% of the blocks.
Alternatively, with 50% detective hash rate (of the honest hash),
the selfish miner only needs 34% of the total hash rate to, again, grow his chain faster than the main chain FOR CERTAIN,
because the main chain will have < 34% of the total hash rate dedicated to it.
The selfish miner can then, again, wait for there to be no competing detective block for the very tip
of the chain and publish whenever they like, grabbing 100% of the blocks.

- The paper does NOT investigate at all the effect of publishing N blocks through the network quickly.  There is
no modeling of this.

- Given the above considerations, at the very least a simulation of the case where the selfish miner ignores the detective blocks probably should have been done (but for lower values of detective hash percentage).

- Even disregarding the above, the results of the paper focus on the percentage revenue (number of blocks) obtained by selfish
mining and how it is affected by the detective mining strategy.  A selfish miner is not necessarily motivated only to maximize
the number of blocks they mine.  They can also be motivated to create the longest reorg regardless of profitability, or some
sort of mixed motivation, weighted towards maximum block rewards or maximum reorg length.

- Large reorgs, although rewarding a selfish miner with many xmr, are not necessarily profitable, since the reorg can
degrade trust in the blockchain and drive down the price of the coin.  Since it seems that the current attacker is performing
large reorgs when they can, it is not safe at all to assume they are motivated purely to obtain the maximum amount of xmr possible, or the maximum fiat value from mining possible either.

- The example I first gave further up the thread was largely correct.  It is only the tip of the reorg that is in danger of being
lost by the selfish miner.  Allocating hashrate from the honest chain to produce detective blocks WILL make reorgs bigger, especially if the attacker is motivated to create long reorgs.  Diverting 50% or 100%, as in the paper, is SUICIDALLY DANGEROUS and not worth considering.

- My opinion in the end is that  the paper does not constitute evidence that detective mining will do anything helpful.
They use parameter ranges which render their own assumptions nonsensical and even if their conclusions are true they do not apply to an adversary who is motivated by maximum length block reorgs to a non-zero degree.

Do not implement this.  It will exacerbate the problem immensely if not fatally.

## SChernykh | 2025-08-21T07:01:19+00:00
What is apparent, is that a simulation or a test on testnet is needed to model a situation where an attacker has 30-40% of hashrate and just ignores detective blocks until they get an uncontested chain tip.

## fluffypony | 2025-08-21T07:12:30+00:00
> What is apparent, is that a simulation or a test on testnet is needed to model a situation where an attacker has 30-40% of hashrate and just ignores detective blocks until they get an uncontested chain tip.

That's a great idea!

## fluffypony | 2025-08-21T07:21:40+00:00
@AwfulCrawler I think I may have created some confusion with the % adoption thing - I didn't mean to imply that pools should divert that much of the net hashrate, but rather that pools that account for >51% of the hashrate should implement detective mining. I also think we've improved a bit on the paper within these discussions, so the paper doesn't necessarily stand alone. With those clarifications, let me respond to the points you've made:

> Length vs cumulative difficulty

Agree the paper counts length. In practice we would implement against cumulative difficulty. Nothing in the tactic depends on length specifically. When we say "tripwire at height N+2", read that as "competing child for the same parent". Chain selection remains heaviest‑chain.

> δ and θ notation

Also agree the symbols in the paper are confusing. Operationally, we care about the detective share of total hash, not just among non‑attackers. We are not proposing δ anywhere near 100 percent. A realistic pool policy is to start at 5 to 10 percent of your pool hash on a valid signal, cap at 20 percent, and auto‑revert if corroboration breaks.

> "They assume the attacker publishes as soon as a detective block appears"

That is the profit‑maximising best response in their model. If an attacker ignores detective blocks, two things are true:

* They cannot realise the revenue from their private blocks while withholding. If their goal is profit, they are strictly worse off the longer they wait.
* If their goal is disruption, detective mining still helps by capping how often long, clean runs form and by giving operators early, high‑confidence telemetry. It does not force a reveal, and I apologise if I've mistakenly claimed that it does.

> "At 50 percent or 100 percent detective share you make reorgs bigger"

I think we can all agree that diverting that much is a bad idea. I'm certainly not proposing it. The deployment plan should be small‑then‑ramp with a hard cap and automatic backoff. You keep the public chain healthy and you only spend bounded hash while a corroborated leak persists.

> "Attacker ignores detective blocks and grows an arbitrary run"

If detectives pulled nearly all honest hash off the public tip, yes. I don't think that should happen. With small bounded diversion, public production continues. The attacker's expected private run length still drops because each leaked tip is contested in real time. You are trading a small amount of honest hash for a large reduction in the probability of long clean runs. That is the lever.

> "Burst publish of N blocks is not modelled"

Yes that is true. Two thoughts:

* The main effect of detective mining is pre‑reveal. It reduces the frequency with which long private runs exist to be blasted.
* Post‑reveal, today's monerod rejects unknown‑parent children, so earlier detective children may be orphaned in a very fast burst. A modest daemon improvement to cache children‑before‑parent would strengthen the post‑reveal effect. Either way, the pre‑reveal clipping still stands.

> "Only the reorg tip is at risk, so attacker usually keeps most blocks"

In a very fast burst reveal with current relay, often yes. That is why we are explicit that detective mining reduces expected reorg depth and attacker EV, but cannot guarantee that an already‑formed 8‑block run gets split at many heights on reveal. The practical gain comes from making such runs rarer and typically shorter.

> "Why not just ignore the attacker's blocks if you have majority hash"

Detectives let us infer leaked parents on some Stratum connections. That does not give an on‑chain provenance flag you can safely match in validation. Hard‑rejecting by hash creates a policy fork and invites mistakes or evasion. Detective mining leaves consensus untouched. It only steers where we point hash when a leak is corroborated.

> "Attackers may value disruption over profit"

Agreed. Detective mining still helps by shortening many runs, reducing the average realised reorg depth, and giving operators early warnings to raise confs and tighten peering. It does not stop a fully private, deep‑pocketed attacker from slowing blocks proportional to their private hash. Nothing pool‑only can.

## What I'm actually proposing we deploy in a testnet test

**Triggering**

* Quorum of K sensors on different IP ranges see the same off‑tip parent from the same pool
* Persistence T seconds and share‑acceptance on that job
* Adjacency continuity: the pool was on the public tip, then flipped to the unknown parent within a short window

**Mining policy**

* Divert h = 5 to 10 percent of the pool's hash to the detective template on the leaked parent
* Cap at H = 20 percent maximum, hard limit
* Empty detective blocks by default to avoid accidental double spends
* Auto‑revert if any check fails or the leak ceases (ie. the quorum doesn't stop operating just because this is happening)

**Networking**

* Pre‑queue detective children and resubmit the instant their parents appear
* Optional improvement to nodes: cache unknown‑parent children for rapid attachment when the parent arrives

**Telemetry**

* Log every trigger and outcome, publish stats on reorg depth distribution before and after

## Concrete expectations to judge the testnet test by

* Fewer long private runs observed by sensors over time
* Lower 95th percentile realised reorg depth during attack windows
* No material increase in average time between public blocks, because diversion is small and bounded
* Attacker revenue share decreases in windows where leaks are frequent and detectors are active

If these do not hold with the test, then it's failed and we pursue some other option. The upside is real and the downside is bounded when you do not yank half the network off the public tip.

@SChernykh does that sound like a good outcome for the test?

The MAJOR advantage is that we can actually build and run this ASAP. Protocol level changes are going to be lengthy - maybe several years away - and much of the community is going to push back on anything PoS-related, which may lead to a chain fork. If this works we can avoid that, and *at least* kick the can down the road.

## SChernykh | 2025-08-21T08:27:07+00:00
Yes, the expectations look good. Also, there's no need to implement the trigger detection for the test, as we will be running both sides.

## zawy12 | 2025-08-21T11:46:19+00:00
I believe Monero's difficulty algorithm has a lag that should prevent manipulation, but if it doesn't or isn't sufficient, using cumulative difficulty instead of block count could give the attacker an advantage: he might be able to change timestamps to get a slightly higher chain work at the same height.  This would improve his gamma from 0.5 to 1.  A copy cat attack on manipulation of the timestamps could thwart that advantage, or reduce his gamma to 0.  

[edit: the lag appears to ignore the most recent 15 blocks, so I don't think it could be manipulated to improve or worsen gamma in a <15 block reorg ]

[My "timestamp-enforcement" mitigation](https://github.com/zawy12/difficulty-algorithms/issues/87) could be tried on testnet without changing code if someone has a large fraction of hashrate to simulate the attacker and the timestamp enforcers.  If there's the possibility it's going to be used, it's important for someone to be measuring the difference between timestamps and block arrival times on main net right now to see how accurate honest miners' clocks and timestamps currently are so that we know how loose the settings need to be so that when it's attempted the honest miners using and not using the mitigation aren't orphaning each other which would help the attacker.

It would also be good to know how frequent honest disruptions are that last more than 1 block time.  But the only easy check is to see how often timestamps (that aren't obviously bad with large "negative" solvetimes before or after) are more than 6 blocktimes apart. With no disruptions and constant hashrate it's supposed to be exponentially distributed: 1-CDF(6) = 0.25% of the blocks.

**However,** the vibe coding script indicates it needs 80% adoption to cut 1-block reorgs in half if the attacker has 40%.  If the enforcers of timestamps only equal the attackers' hashrate, it doesn't appear to change his gains. It appears to help him if they are less (by the enforcers getting themselves orphaned with the attacker getting help from honest miners).  

So I'm less enthusiastic now that I see it needs to be a code update. 

Similarly, if miners require a reorg to prove it had higher hashrate, it needs to be a formal consensus rule. An example rule for "proof of higher PoW" would be:

> If reorg depth N is > 2, do not switch tips unless PoW of reorg is > 1 Stdev above current tip.

A reasonably accurate current local time can be used to make the above PoW measurements more precise. This would help relax the requirement if there's an honest partition. What I mean is that the cumulative difficulty would have an additional term added to it that is D * t/T where D is the difficulty that miner is currently trying to solve, t is local time minus the local time when the tip was first seen and T is block time.  Notice this isn't timestamp-based weighting, but the best estimate of the number of hashes performed since the tip arrived.  This adjustment helps use the Stdev calculation which will have a decimal point that needs more precision than sum of difficulties.  The paper napkin estimate of the Stdev is SQRT of the attackers PoW_attacker (sum of difficulties + D * t/T).  So his chain is accepted when PoW_a - SQRT(PoW_a) > PoW_honest.  The D * t/T solves [a particularly devilish problem with measuring PoW and hashrate](https://delvingbitcoin.org/t/correcting-the-error-in-getnetworkhashrateps/1745/4). If you've been working on a tip for T seconds and a tip 1 block ahead arrives (1 block reorg) it's not actually evidence of higher hashrate. You _expected_ to find a block on your own tip at that moment, so it's not evidence of more work.  But I'm not brave enough to suggest everyone autistically apply the math that correctly so I specified applying it only N > 2. also, SQRT is an underestimate of the Stdev. It's actually larger for small N. 

CORRECTION: SQRT(PoW) isn't right because it's a large number when I should be thinking in terms of blocks. Maybe it should be SQRT(PoW / mean(PoW/block))   This means the math changes such that PoW_a above is pretty much SQRT(N + t/T) 

CORRECTION:  If t/T >1 it could cause a disaster in an honest 50%-50% partition.  Change my math to t/T up to a max of 1.

Of course there is the complaint that it will take an honest partition longer to resolve.  However, that's just good intentions gone awry. How many times has an honest partition caused a 5 block reorg in the history of the chain? How many times was it an attack? For this reason having sufficient evidence of the alternate tip having higher work is mathematically correct. It enforces proof of work.  To be precise, I mean proof of higher mean hashrate since the split. 

To be clear, if a node knows there's an honest partition such as having his node offline, the proof isn't applied. He also doesn't apply it if he believes his clock might have significant error.

Requiring formal consensus changes makes the copy cat method look better. It's incentive-based.

## dimagid | 2025-08-21T17:23:16+00:00
Have we experienced a reorganization of 10 blocks or more since this attack began? The ongoing and sustained intention of the attack is to destroy Monero. What do we do if a selfish mining reorganization of 10 blocks or more occurs—do we just turn off the lights and go to sleep? Do you believe the lock-in period for XMR should be increased from 10 to 15 or 20 blocks under certain conditions? Additionally, while the proposal is aimed at the pool level, is there any way to implement it at the solo mining level as well? How can solo miners avoid validating chains produced through selfish mining? Thank you for your responses.

## PPPDUD | 2025-08-21T20:46:53+00:00
@fluffypony Has anybody actually agreed to implement this?

## AwfulCrawler | 2025-08-21T22:27:34+00:00
@fluffypony I was mainly addressing the paper and what's in the paper but I flatly disagree that the presence of a detective block forces them to publish to maximise profit.  Basically: ignoring the detective blocks eventually orphans everything except the tip.  There's no interleaving or chance to build on top of the detective blocks when the attacker broadcasts their hidden chain.  In the parameter ranges the paper talked about, ignoring IS more profitable.  For lower parameter ranges this is entirely unknown until a simulation or some other calculations are done..

A couple of extra points:

- The selfish miner could simply incorporate the block into their chain (hiding the rest).  The honest miners will not be able to do anything with the detective block.  The selfish miners lose nothing by doing this, they simply start mining on top of the detective block.  No profitability loss at all.  The detectives have now extended the alternative chain by 1.  If the honest chain ever gets close enough to the partially visible alternative chain with a mix of selfish and detective blocks, the selfish miner reveals the full alternative chain and the network switches to the hybrid selfish/detective chain.  The selfish miner wastes no hashrate and loses nothing.  
 
Edit: Actually this should be tested and should have been tested in their model.  They do lose out by delaying their payoff but the end payout will be unaffected.  Any motivation to create reorgs and all you will be doing is helping the attacker.  It's possible that the detective miners could increase the profitability of the selfish miner with this strategy as well.  A script simulating the strategy like they did in the paper could confirm this.

- On a technical note, the detective blocks may include transactions that have already been included in the hidden chain, which could cause problems when implementing in the wild and not as a statistical model as in the paper.

Edit2: I'm going to work on a script to (a) recreate the paper's results/graphs for a single selfish miner.  (b) simulate alternative selfish miner actions.  I'm rusty so it could take a while / end up not getting done.  Anyone wants to beat me to it go ahead.

## fluffypony | 2025-08-22T04:47:42+00:00
> [@fluffypony](https://github.com/fluffypony) Has anybody actually agreed to implement this?

Read the thread - we're going to test this on testnet and see if it works

## fluffypony | 2025-08-22T05:02:31+00:00
@AwfulCrawler Thanks for digging in! A few clarifications that separate what the paper models from what we should actually deploy.

> Ignoring detective blocks orphans everything except the tip

* If the attacker **ignores** D and later bursts N blocks, then yes, with today's Monero relay most D children will be orphaned in a fast reveal. I hopefully haven't claimed otherwise😅 The primary effect of detective mining is **before** reveal: it reduces how often long private runs form by contesting each leaked tip in real time. That is orthogonal to a burst reveal.
* If the attacker **incorporates** D into their private chain (mines on top of D), they have **already surrendered that block's reward** to the defender. The "end payout unaffected" claim is false in that branch. They traded a shorter lead for a lead that includes a block they do not own.

> Presence of a D block does not force publication

* Yes 100%. The paper assumes a profit-maximising attacker who reveals when a D child exists on their hidden parent. That is a modelling choice, not a consensus law. An attacker who withholds longer still cannot realise any revenue until reveal, and if they mine on top of D they lose at least that height's reward. So, for a profit-seeking attacker, ignoring D is not strictly free.

> Detectives might help the attacker by extending the alternative chain

* Only if you divert a large fraction of honest hash. I hope I've been clear that I'm **not** proposing that. A sensible rollout is 5–10 percent of a pool's hash on a corroborated leak, hard-capped at 20 percent, auto-reverting if the signal breaks. That keeps the public tip healthy while still creating per-height tripwires that clip private runs. With that cap, any marginal increase in the attacker's run probability is small and is offset by the attacker either losing D's height or facing extra race risk at reveal.

> Interleaving and burst publish

* With today's monerod rejecting children-before-parent, a very rapid multi-block reveal often means only the **last** contested height has a shot to flip, we agree on that. The lever we rely on is **run-length suppression** during formation, not guaranteed slicing of a completed 8-block burst.
* A small daemon improvement to cache unknown-parent children would strengthen the post-reveal effect, but detective mining does not depend on it.

> Transactions in D may collide with hidden blocks

* We avoid that by defaulting D to **empty blocks**. That denies the attacker the subsidy at that height without risking accidental double spends.
* An interesting idea that I just thought of: pools could include a conservative set of transactions received WELL after the sensors detected a new block; this might mean that, if the attacker ignores the block, **THEY end up with a double-spend at reveal and thus have an invalid block!**

> Simulate the attacker that ignores D

* Good idea. Two things worth simulating:

  * **Run-length distribution** under small δ (say 5–20 percent of total) with the attacker ignoring D vs no detectives. Metric: tail of the private run-length CDF and realised reorg depth under burst reveal.
  * **Attacker EV** when they sometimes mine on top of D. Metric: expected subsidy lost to D vs any increase in reveal success probability from a slightly longer run.

## aj13337 | 2025-08-22T08:19:33+00:00
> * An interesting idea that I just thought of: pools could include a conservative set of transactions received WELL after the sensors detected a new block; this might mean that, if the attacker ignores the block, **THEY end up with a double-spend at reveal and thus have an invalid block!**

The selfish miner can include a decoy transaction in his private block, keep it secret, and broadcast it on a large delay so that the detective mistakenly includes it, causing their block to be invalid. I think you have to mine an empty block to avoid this.

There are a few conceivable ways to allow the detectives to mine non-empty blocks but everything I can think of would require a consensus change.

## AwfulCrawler | 2025-08-22T09:10:03+00:00
I've had a first go at recreating the results of the paper.  I believe they have implemented their model as described incorrectly and that I have identified how they have implemented it incorrectly.

I am not 100% sure about this as of course I myself may have incorrectly implemented their model.  However it is not very many lines of code, so it is easy for someone else to have a look at or, ideally, indepently implement the paper model for themselves and see if they recreate the graphs. I believe they will not and this is a serious concern.

Link to the git with R scripts and graphs: https://github.com/AwfulCrawler/detective_mining/ 
Work in progress and code has just been churned out pretty quickly and over-annotated but that's how it goes.


## fluffypony | 2025-08-22T09:26:21+00:00
> The selfish miner can include a decoy transaction in his private block, keep it secret, and broadcast it on a large delay so that the detective mistakenly includes it, causing their block to be invalid. I think you have to mine an empty block to avoid this.
> 
> There are a few conceivable ways to allow the detectives to mine non-empty blocks but everything I can think of would require a consensus change.

Good catch!

## venture-life | 2025-08-22T12:17:52+00:00
I am **very** naive in my understanding, but isn't this downstream of the assumption that there is a free lunch to be had in PoW? 
Over-cutting the secret chain and forcing them to publish (and trigger a re-org) surely might limit the length, but it does acknowledge their lead and they reap the gains from the then-published branch, imho.
It's also not clear to me whether a further partitioning of the honest miner's hashrate into detective mining, when they already are partitioned into different branches, leads to a net positive outcome.

I have suggested essentially under-cutting the attacker's branch in issue #141 

## zawy12 | 2025-08-22T13:34:47+00:00
I don't understand the counterarguments to the objections. If public miners can't mine on N+2d due to not having N+1a until the attacker chooses, and if attacker can mine on top of N+2d privately, I don't know why the key assumption in the paper is true. The key assumption is:

>the selfish mining pool can not keep its chain secret any more ... the smartest way is to open up all selfish mining [blocks as soon as detectives find a block before the attacker] ... the selfish mining pool must inevitably release its block B [if detectives find C first].  

Look at the limits which are easy to analyze. If detectives are 0%, selfish miner wins a little. If detectives are 60% and attacker is 40%, most of the time the detectives are mining the public chain because it's longer. But when the attacker gets lucky, detectives switch. If they find a block first, they can't switch back or they'll be 2 blocks behind the private chain. They have to mine on top of their own private block. Attacker just mines on top of the detectives blocks. When the attacker decides to release, the attacker and detectives get all the rewards that their hashrates deserve.  The attack has been eliminated at the cost of deeper reorgs. The reorgs are as deep as the attacker wants. Except there's no reorg because the public chain didn't extend. 

As detectives increase, public orphans and the attacker's excess gains are reduced, but the ability to keep the chain silent increases.  The attacker's excess gains go down with more detectives because the two of them have fewer public miners to orphan.  I don't understand the comments that say larger detective hashrate is more dangerous.

If the key assumption in the paper is wrong, the public, detectives, and attacker do not all "break even" in rewards per hashrate that I described (edit: when detective hashrate = attackers). That's the claim of the paper if you look at figure 11 for attacker = detective hashrates at 33% and 50% when gamma = 0.5. They both break even for their hashrate which means the public also breaks even. With the assumption not being true, the detectives have to be 100% of the public miners for everyone to break even. 

## zawy12 | 2025-08-22T16:19:25+00:00
Below are @fluffypony's counterarguments. 

> If the attacker incorporates D into their private chain (mines on top of D), they have already surrendered that block's reward to the defender. The "end payout unaffected" claim is false in that branch. They traded a shorter lead for a lead that includes a block they do not own.

> An attacker who withholds longer still cannot realise any revenue until reveal, and if they mine on top of D they lose at least that height's reward. So, for a profit-seeking attacker, ignoring D is not strictly free.

I don't see how small detectives put any pressure on the attacker. They give him the choice of reducing himself to a simple selfish mine (no deep reorgs) and get a normal profit and they split the rewards according to their hashrate, or, if attacker + detective > public, the attacker can orphan all of the public chain at any point he chooses, splitting profits with detectives.  Ideally, the attacker wants attacker + detectives = 51% so they can jointly maximize the number of public orphans with the minimum hashrate.  I don't think anything special happens in the case of attacker + detective < 50% (small detectives) that breaks the trend indicated by the 4 cases I've pointed out.   

 This appears to be his "excess" rewards per hashrate in increasing order:  (if the key assumption is wrong)

1) detectives + attackers = 100%  (0% excess gains per hashrate due to no orphans anywhere)
2) 0% detectives  (selfish mining gains)
3) detectives + attackers < 51%  (deeper reorgs that splits _higher_ profit margins per hashrate than mining alone because he's closer to 51% than he otherwise would have been)
4) detectives + attackers = 51% (split 100% of 49% public orphans according to hashrate)

Case 3) is the hardest to analyze. The other 3, by my reasoning are immediately true if attackers always mines on top of detectives.  The claim is being made that detectives stay small so that we're in condition 3 and that somehow that motivates the attacker to release earlier than if there were no detectives. But I can't see any push to reveal and it breaks the trend shown by the other cases. Fewer detectives => better outcome doesn't seem like it should be true.

For the case of  detectives + attacker from 51% to 100%, their rewards per hashrate increasingly reduce to normal as they have less and less public orphan losses to share. But attacker gets all the tx fees.

BTW the paper examines a "copy cat" attack in Figure 14 for N=2. They indicate the 2 copy cats lose (presumably to honest miners) as long as their sum is less than 51%. But I don't know if they're taking into account difficulty being lowered, so my claim that copy cats (same hashrate) eventually breaks even with honest miners may still be true. 

Like timestamp enforcement, detective mining appears to reduce the attacker's gains only to the extent it removes his ability to choose when to release.

## zawy12 | 2025-08-23T09:41:21+00:00
@awfulcrawler:
> The selfish miner could simply incorporate the block into their chain (hiding the rest). The honest miners will not be able to do anything with the detective block. The selfish miners lose nothing by doing this ...  the selfish miner reveals the full alternative chain and the network switches to the hybrid selfish/detective chain. The selfish miner wastes no hashrate and loses nothing.

@fluffypony:

> If the attacker incorporates D into their private chain (mines on top of D), they have already surrendered that block's reward to the defender. The "end payout unaffected" claim is false in that branch. They traded a shorter lead for a lead that includes a block they do not own.

Awfulcrawler seems to be correct except the attacker doesn't break even. He gets a higher profit margin thanks to the detectives.  If the attacker always privately mines on top of detectives, it's exactly equal to a larger selfish mine. The closer a selfish mine gets to 51%, the more "rewards per hashrate contributed" the attacker and detectives get. Above 51%, the attacker has complete control.  

Other options: 

1) "Enforcing timestamps" appears to work great at eliminating selfish mining profits, but requiring clocks to be +/- 10 seconds accurate seems to be a big hurdle.  Vibe coding results say it forces a lot of deep reorgs.  

2) [ edit: this won't  do anything to stop 4 or more multi-block reorgs if a simple and strict rule of "do not switch tips until alternate chain is 3 blocks ahead" is applied, but it makes the attacker take massive losses ] Enforcing "statistical evidence of higher PoW before switching tips" would work but it's a big consensus ask.  This is my favorite because it's like an improved PoW. Notice that the longer a partition stays active as a result of this rule, a resolution is more likely to occur in terms of the percent difference between the hashrates. Using a cube root instead of square root rule would force a faster convergence. For example "do not switch tips unless  N - cieling(SQRT(N)) >  M where N and M are the number of blocks since the common ancestor that the alternate tip and the current tip have, respectively."

3) Pools are currently motivated to "copy cat". If you can see the attacker's blocks, honest pools would go immediately to a private mine. If they win or lose the battle, the reorg isn't as deep because there won't be many public blocks.  So it causes delays instead of deep reorgs.  As soon as one of the attackers gets a statistical lead, they publish. It takes away the attacker's "thunder" of deep reorgs. People don't like the feeling of pools centralizing, but nothing in Nakamoto consensus needs or enforces decentralization. It only allows decentralization. The security is based on the profit motive of not having their CAPEX investment devalued by attacking the coin, not that they are diverse.

## shlee-lab | 2025-08-24T09:33:55+00:00
Hello everyone,

I’m Suhyeon Lee, the author of Detective Mining.

I was surprised (and glad) to see such active discussion about my research.
(By the way, the original version was a rough technical paper—sorry about the writing quality. It was later published in a simpler format here: https://www.sciencedirect.com/science/article/pii/S2405959522000443).

There are so many comments that I may have missed some issues. (For example, one of you pointed out that the implementation in the paper is incorrect. It will take some time to look back into the old code and verify what went wrong, but I’ll eventually review it.)

In the meantime, let me briefly review the core concept of Detective Mining, and then discuss the pros and cons you mentioned.

Core concept:

- Selfish mining is a strategy where an attacker mines privately when they have a lead, causing others to waste computation.

- Detective Mining mines on top of the selfish miner’s private lead, and is possible only if the selfish miner operates as an open mining pool.

- The strategy of Detective Mining is to resolve the selfish miner’s private fork as quickly as possible, thereby eliminating the private lead.

Pros:

- Detective miners can achieve higher profits than both selfish and honest miners, since they always mine on the longest lead.

Cons:

- Detective Mining assumes that the attacker is economically rational. If the selfish miner is not profit-oriented, it may pursue other types of attacks. For example, as some of you mentioned, the attacker might withhold block contents, preventing us from ever knowing some blocks.

- Detective Mining does not necessarily reduce the selfish miner’s revenue below that of honest mining. It helps resolve private forks, but it isn’t a “help” to the selfish miner. Otherwise, the selfish miner could enjoy deeper forks more often.

Up to this point, these are theoretical comments. After reading your discussion, I realized there are also practical issues with Detective Mining:

- Even if there are detective miners, is there an official channel to send new block information from Detective Mining to the selfish miner (e.g., Qubic mining pool)?

- Even if such a channel exists, what if the selfish miner ignores it and continues mining on the private chain?

Answer to issue 2 which can neutralize detective mining:

Selfish mining exploits private forks but still adheres to the longest-chain (or heaviest-chain) rule. If the selfish miner ignores this rule, all other honest miners must reject Qubic’s chain, creating an eternal fork. Unless Qubic consistently controls more than 51% of mining power, it cannot win against the honest miners’ chain. The key question then becomes: how many honest miners would follow through with this decision in Monero?

## zawy12 | 2025-08-24T10:09:57+00:00
@shlee-lab this is the problem two of us have with the usefulness of detective mining.  When detectives mine on top of an attacker's private block, the honest non-detectives can't mine on top of the detectives' block because they don't have the attacker's prior block transactions to validate.  But the attacker can mine on top of the detectives' block.  If the attacker always mines on top of detective blocks that were mined on top of his private blocks, and applies the simple selfish mining algorithm, it appears his rewards per hashrate increase because the detective blocks plus his gets their combined hashrate closer to or above 51%.  It appears the detective blocks are only helping him because he can freely choose when to make the combined "private" chain public.  

As their combined hashrate exceeds 51% the attacker's "excess gains" above normal mining start to fall until at 100% of honest miners being detectives, the attacker doesn't have any "excess gains" above normal mining, but he controls how long transactions on the "private" chain will not be viewable (with combined hashrate is above 51%) and he gets 100% of fees. The public chain will be "silent" as long as his wants.  As was discussed, the detective blocks can't include transactions due to the possibility of being invalidated from having duplicates of prior transactions in the attacker's blocks (that he can't see).  If detectives make their blocks public, the attacker doesn't face the same "vice versa" risk. 

## dimagid | 2025-08-24T13:27:09+00:00
The other key question is: how many honest miners are actually mining on the pool that engages in selfish mining, using their hash rate to enable deep reorganizations and potentially—if it hasn’t happened already—carry out double-spending attacks?

Another important point: do we even need the hash rate of a malicious pool that aims to harm Monero?

I believe that using Detective Mining is like turning the other cheek: we try to see if the selfish miner stops being selfish because we mine on their private chain, or because they eventually realize that honest mining is more beneficial. But if that doesn’t happen, then of course we, as honest miners, must move forward and continue protecting our network and currency by adhering to honest practices.

## shlee-lab | 2025-08-24T21:54:49+00:00
@zawy12 Detective mining doesn’t increase the attacker’s excess gains. It may incidentally increase the fees a selfish pool collects, but the point of detective mining is to resolve private forks and suppress deep reorgs, which are what drive the attacker’s extra profit. I agree the “silent chain” risk you mention is real and needs guardrails.

## shlee-lab | 2025-08-24T21:58:33+00:00
@dimagid Selfish mining exploits any PoW chain that follows the longest/heaviest-chain rule. So the real question behind your question is: are we willing to deviate from that rule? Simply ignoring the attacker’s valid blocks and “sticking to honest mining” creates a policy fork and makes the rule ambiguous.

As a (admittedly heavy) consensus idea which needs a change in a protocol, here’s a relative-timing approach: allow a block to include a list of block hashes it has observed consecutive higher heights (for example n>2 to prevent exploits on this rule by a big mining pool). If any of those referenced blocks later appear, they are forcibly orphaned with no reward, signaling they were mined earlier and intentionally withheld. We don’t need exact clock times—the inclusion list is the evidence. This could help solo miners infer withholding and keep following the honest chain.

@fluffypony what do you think? If the selfish mining pool will not follow the long chain rule, then finally we need to change the protocol a bit. 

## fluffypony | 2025-08-25T18:39:28+00:00
@shlee-lab could that be done on a pool level without a protocol change? If, for instance, we have >50% of pools implementing Detective Mining v2 or whatever this is called, then we can have them do almost anything (in terms of block selection) without needing any protocol changes.

## zawy12 | 2025-08-25T23:36:11+00:00
> Detective mining doesn’t increase the attacker’s excess gains.  ...  the point of detective mining is to resolve private forks and suppress deep reorgs

How does it do this if the attacker can mine on top of detective blocks and the situation is as I described.  In other words, which of these statements are you saying isn't true?

1) public chain can't mine on top of a detective block until attacker reveals the private parent block
2) attacker can mine privately on top of a detective's block
3) rewards per hashrate increase as a selfish mine hashrate gets closer to 51%

## AwfulCrawler | 2025-08-26T07:11:25+00:00
I have fleshed out a bit my attempt to recreate the results / figures of the paper.  I don't think fig 11 and fig 12 are consistent with each other.

https://github.com/AwfulCrawler/detective_mining/

## shlee-lab | 2025-08-29T16:20:55+00:00
@fluffypony This will need a protocol change. This way is considered cause it seems like community members here don't prefer the idea mining on the top of the selfish miner's fork.

## shlee-lab | 2025-08-29T16:25:03+00:00
@zawy12 All the three are true. What I mean is that the detective mining disturbs the selfish miner's fork continuance. It obviously reduces the revenue of the selfish mining comparing to the selfish mining without detective mining. Otherwise, the honest chain will suffer from longer and more frequent reorgs.

# Action History
- Created by: fluffypony | 2025-08-19T08:04:00+00:00
