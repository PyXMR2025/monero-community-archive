---
title: 'Countering Selfish-Mine: Promote Orphans to uncles (equal pay) and decide
  deterministally (in stratum) who becomes father :)'
source_url: https://github.com/monero-project/research-lab/issues/141
author: venture-life
assignees: []
labels: []
created_at: '2025-08-20T10:41:12+00:00'
updated_at: '2025-09-17T17:25:41+00:00'
type: issue
status: closed
closed_at: '2025-09-17T17:25:41+00:00'
---

# Original Description
### preliminary
There is this no-free-lunch theorem and I do think if PoW blocks are accurately sampling from the underlying hashrate distribution, it should not be possible to skew that. Blocks just need to be accurately recognized to account for asynchronicity (of block-first-seen), malicious or not. The one thing that makes selfish-mine extract more than their fair share is exploiting that information asymmetry by partitioning clueless, honest miners into different branches.
 
There is also an important distinction of what is decided by PoW and what is "hard-coded" by honest participants. For example, If I modify my monerod to reward myself 60 XMR on finding a block, my hashrate does not get recognized and my block would simply be ignored by the honest participants who didn't relax that rule in their monerod.

### What is the selfish-mine exploit exactly?
Quote from Selfish-Mining re-examined: "Selfish mining is an instance of game-theoretic attacks that take advantage
of information asymmetry in distributed systems". This is exactly what PoW tries to overcome. Unfortunately, the current PoW selfish miners use the information asymmetry of block first_seen which _can_ be replaced by randomized but deterministic selection.

One thing to highlight about the Selfish-Mine exploit is that an attack is seen by the network in real-time prior to the inevitable re-org. This is due to the fact that the side-chain has two parts, a hidden tail and the published branch which **is continuously being ignored by the miners trapped in the losing branch** because of matching cumulative difficulty and the first_seen rule and the reactivity nature of selfish-mine. The trapped miners are modeled by `(1-γ)` where `γ` "denotes the ratio of honest miners that choose to mine on the pool’s block" (citation from the infamous paper, Majority is not enough - Bitcoin is vulnerable, referred to as 'the paper' from here).

### Prevention
It seems therefore strictly better to free the trapped miners (collapse the two public branches into one) as soon as possible by choosing deterministically which branch to mine on (implemented within stratum, no protocol change). 

_This fixes `γ` to 0.5 and the pareto front (Fig. 3 of the paper) shows that you need a pool share `α > 0.25` to be profitable. On first glance, it doesn't seem promising on it's own since `γ` relies on additional effort of employing sensors and skew the `first_seen` metric to your favor. With a high enough `γ` you can currently profit with even less than 25% hashrate share. If your share is > 25% you don't need to rely on luck or sensors anymore and you profit even more if you had previously a `γ` below 0.5._

Actually, the cursive part is not quite right, you can read it as intuition only. Deterministic mining would set gamma effectively to 0 but introduce a new random variable with expected outcome of 0.5. It might be seen as a replacement for gamma, but it is more powerful, since gamma may be retained over a certain period whereas the randomized choosing of a branch eliminates the partition.

I think the upside of collapsing the branch as quickly as possible is bigger here. I propose a further adjustment in which it does not  matter from a reward perspective which branch is ultimately adopted. What matters is that the partitioning of the honest hashrate by `γ` bands together and we free our friends quickly. The further adjustment is quite drastic but effective:

- we have an additional field "donation" (not sure if that can be a stealth address or not). To account for p2pool, this should allow lists of addresses with percentage
- block rewards are paid out by the subsequent block (N+1) based on that donation field
- rewards would be given to all competing blocks (uncles) uniformly. This needs to parent (N-1) + uncles from N-2. The branch point to be considered should be one block earlier since we want to account for the asynchronous nature of PoW that the exploit leverages


outside of protocol, in stratum:

- mine on the candidate that is the index of the sorted array of all candidate block hashes. (index is determined as first bits of the hashed array modulo len(candidates) ). In effect, all honest miners mine on the same block.


I hope this makes sense. 

# Discussion History
## venture-life | 2025-08-20T11:45:02+00:00
the reward would need to be fleshed out more. I'm currently unsure whether that ought to be:
in the normal case: 0.5 to parent 0.5 to grandfather (ie, the same miner, paid in blocks N+1 and N+2)
in the re-org case: 0.5 to parent, 0.25 to grandfather, 0.25 to grandfather's competing block (uncle)

in combination with stratum's deterministic block candidate selection, longer branches _should_ not happen given that the majority adopts that selection rule. In any case, the reward is diminished due to at least one valid uncle.

with an orphan / uncle and re-org: avg payout would be 0.5. 
either 0.5 + 0.25 (if branch was chosen)
or 0.25 (if branch was not chosen)
avg: 0.5, (ie, the reward matches the probability of any branch chosen, Miners choose not only uniformly between competing blocks but also deterministically, something that the "Optimal Selfish Mining Strategies in Bitcoin" failed to address (when modelling uniform tie-breaking, they assume both branches will be mined upon with 50% hashrate).

the point is, it collapses the 2 branches into one as quickly as possible. The detective mining proposal also aims to collapse the secret chain and force a re-org (them publishing), but as I understand it, it would be done only after the pool has already gained a lead. I'm also unsure about how "mmediately mines a "counter" child block on top of the selfish pool's hidden parent." works in practice given that there is PoW effort involved.

## venture-life | 2025-08-22T16:28:03+00:00
just to recap.
The attack works by finding a block which he doesn't broadcast. When other's find a new block, he immediately broadcasts his conflicting block and hopes to partition the network hashrate by the first_seen rule. He might still fail, the ramp-up is successful once he gains a lead of 2+ blocks.

If there is concern about the scheme / sketch above because of mass-broadcasting several blocks at once, the general idea might still be applicable, but modified to e.g. having the donor be N+60/61 instead of N+1/2. We could even gather attestations from the 60 blocks in between, and promote the orphan only if a certain threshold of block have attested to it.

Also, to clarify, competing blocks must only be allowed at the tip, not retroactively.

## tevador | 2025-08-22T18:53:43+00:00
> block rewards are paid out by the subsequent block

This doesn't work well with Monero due to the quadratic burn rule. Essentially, a malicious miner of the N+Mth block can make the block reward to be zero if the mined block is sufficiently large.

Even for a non-malicious miner, the incentive to include transactions is simply not there if it has no effect on that miner's own rewards.

> rewards would be given to all competing blocks (uncles) uniformly

Literature suggests [1] that uncle rewards make selfish mining more profitable (was studied with Ethereum, but might also apply in this case).

[1] The Impact of Uncle Rewards on Selfish Mining in Ethereum, https://arxiv.org/abs/1805.08832

> mine on the candidate that is the index of the sorted array of all candidate block hashes

This only affects the case when the selfish miner's chain has the same length as the honest chain. For the pool currently attacking Monero, they have been releasing chains that are at least 1 block longer that the honest chain. Deterministic tie breaking can't help in this case.

## venture-life | 2025-08-22T19:43:42+00:00
Thanks for your reply and assessment. I appreciate it.

To your points, yes, it's a very rudimentary idea that doesn't account for penalties / quadratic burns yet.
But I was actually suggesting that it's not really up to the donor (N+Mth block) to include these donation transaction but that this would be implemented in place of the current coinbase rewards which if deviated, would simply completely reject the entire block. 
Like, right now, I imagine someone could modify monerod to construct a block that upon finding rewards him 60 XMR instead of 0.6. It would be rejected by every other node. So, the donor's wouldn't have a choice, it would be "hard-coded". 

He can only fill his donation address (or for p2pool, a list with percentages), which future block miners are obligated to pay.

Regarding uncles in ethereum, the difference with my (likely stupid) idea, is that of "equal-pay", ie, the uncle would take from the "real" parent, so that both get the same. 

Regarding the last point, this is true, but it's important I think how they generate / ramp-up this lead. It only works by shifting hashpower away from the main branch. Part of the honest miners are already on the other branch before the re-org happens.

We don't need to discuss about it further. I value your expertise and if you see the idea futile, it is what it is. 

## venture-life | 2025-08-22T20:45:14+00:00
> This doesn't work well with Monero due to the quadratic burn rule. Essentially, a malicious miner of the N+Mth block can make the block reward to be zero if the mined block is sufficiently large.

> Even for a non-malicious miner, the incentive to include transactions is simply not there if it has no effect on that miner's own rewards.

sorry, there was a confusion on my side. I understand your point now better. Yes, this is not at all addressed. 

## tevador | 2025-09-11T05:19:17+00:00
Perhaps this can be closed in favor of #144?

## venture-life | 2025-09-17T17:25:41+00:00
Thanks for the reminder, yes can be closed

# Action History
- Created by: venture-life | 2025-08-20T10:41:12+00:00
- Closed at: 2025-09-17T17:25:41+00:00
