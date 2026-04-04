---
title: Selfish mining mitigations (Publish or Perish)
source_url: https://github.com/monero-project/research-lab/issues/144
author: tevador
assignees: []
labels: []
created_at: '2025-08-27T18:21:26+00:00'
updated_at: '2025-09-24T19:31:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero is currently being attacked by a malicious pool that has around 33% of the network hashrate (`α = 0.33`). There is no evidence that the malicious pool has reached the majority of the network hashrate. Nevertheless, any pool with `α > 0.25` can cause disruption with selfish mining, which is a malicious mining strategy which allows the pool to gain more that its fair share of the block rewards [1].

This is a proposal to mitigate selfish mining. It assumes that Monero keeps RandomX as its consensus mechanism and that `α < 0.5`. It does not (and cannot) address 51% attacks.

It's actually 2 proposals. The first proposal is a soft fork, which does not alter any consensus rules and only needs to be adopted by the honest majority of miners. The second, more comprehensive proposal, requires a hard fork.

After reviewing the available literature about selfish mining, I first want to disqualify all mitigation strategies that rely on more frequent hashrate sampling. This is the Fruitchain and related proposals [2,3]. The main idea is to submit proof of work "fruits" or "shares" with a much lower difficulty than what is required to mine a block and then aggregate those shares within a block. These ideas are unsuitable for Monero because RandomX is too slow to verify. A block consisting of 100 work shares would require 1.5 seconds just to verify the PoW.

Secondly, a large number of mitigations focus on tie-breaking rules [1,4], which apply when the attacker's private chain has the same length as the honest chain. These proposals are not sufficient against a resourceful attacker with `α > 0.25`, who can often outmine the honest majority and win due to the longest chain rule. We need a mitigation strategy that can work even if the attacker's chain is longer.

### 1. Soft-forking proposal

The most efficient selfish mining mitigation that can be rolled out as a soft fork is Publish or Perish (PoP) [5]. It works when the attacker's chain is less than `k` blocks longer than the honest chain (otherwise it falls back to the longest chain rule to allow network partitions to be eventually resolved). A chain weight rule is applied that takes into account the block's relative time of arrival and its embedded uncle block.

PoP introduces the concept of late blocks. A block is late if it arrives more than `D` seconds after any other block of the same height. This only requires relative time measurement and does not need the clocks of the network nodes to be synchronized. Late blocks do not contribute to the weight of its chain.

In case of two competing chains of equal weight, the PoP paper calls for a random selection to be made, but I would suggest to use a deterministic tie breaking rule (e.g. with hashing).

For a practical implementation in Monero, we would create a new tx_extra tag for uncle blocks and each miner could include an uncle block of height exactly N-1 (where N is the height of the current block) in the coinbase transaction. The uncle block is represented by its PoW header, which allows the PoW to be checked. Since the PoW header does not include the height, we would validate the height by checking that the `prev_id` field is the same as the one in block N-1 of the canonical chain. The approximate size of an uncle block is 80 bytes, which is quite negligible. Uncle blocks do not affect block rewards or the cumulative difficulty.

We would use `k = 3`, which means the attacker would need to mine 3 blocks more than the honest majority to cause a reorg. We would use a propagation delay of `D = 5` seconds.

While not perfect, this strategy significantly reduces the excess profits from selfish mining. With `α = 0.48`, the attacker gets ~64% of the block rewards compared to ~88% with no mitigations (numbers from [5]).

### 2. Hard-forking proposal

The hard-forking proposal extends PoP with Reward Splitting (RS) [6]. It bears some similarities with the proposal by @venture-life [7].

This proposal fully removes the economic incentives for selfish mining unless the attacker can mine at least 20 blocks faster than the honest majority.

I will first list the consensus changes:

1. Include the block height in the PoW blob.
2. Reduce the target block time to 60 seconds and raise the output lock time to 20 blocks. The block reward and the penalty free block size will be halved.
3. Increase coinbase maturity to 1440 blocks (1 day).
4. The coinbase transaction of the block at height N pays out the block reward of the block at height N-20.
5. A new coinbase transaction field `miner_address` that includes the miner's Monero address (or more addresses and the percentages how to split the reward). This will be used in block N+20 to pay the miner(s).
6. A new coinbase transaction field `uncle_blocks` that includes uncle blocks. Uncle blocks include the PoW header, the coinbase transaction and its inclusion proof. Only uncle blocks with a height of at least N-20 can be included in block N.
7. Apply the PoP fork selection rule with `k = 3` and `D = 5`. Only uncle blocks with a height of N-1 are counted towards the chain weight.
8. The difficulty adjustment algorithm uses the past 1440 blocks, starting from block N-30. Uncle blocks are included in the difficulty calculation. The lowest and the highest 120 block times are trimmed out before calculating the average block time.
9. The block reward for block at height N is split equally between the miner who mined the block N and all miners who mined an uncle block of height N that was included in blocks N+1 to N+20.

Rationale:

1. Including the block height in the PoW header makes uncle blocks easier to verify and can also help to detect malicious activity of public pools (e.g. mining a parallel chain).
2. Monero used to have a 60 second block time, but it was increased to 120 seconds in 2016 to reduce the natual orphan rate. Due to reward splitting, orphan blocks are not an issue in this proposal. The faster blocks make it harder for a minority hashrate attacker to reorg longer time periods of the honest chain at the cost of doubling the PoW to verify the chain, which is acceptable. Adjusting the output lock time to 20 blocks matches the current 10-block lock time (the same 20 minutes on average, but reduced variance).
3. Longer coinbase maturity prevents malicious miners from quickly selling mined coins after an attack and promotes long-term mining.
4. Delaying the payment of block rewards is required for reward splitting in order to collect uncle blocks. 20 blocks seems like a good compromise as it matches the output lock time.
5. Miner addresses are needed because miners no longer construct their own outputs. Note that the full (main) address and a transparent tx private key are needed in order to verify that the coinbase payout is constructed correctly (similar to p2pool).
6. Uncle blocks are needed for consensus as they affect both the block reward and the difficulty calculation.
7. Keeping the PoP chain selection rules makes the hard forking proposal strictly stronger than the soft forking one.
8. It's essentially the same algorithm, only adjusted for 2x faster blocks and include uncles for proper network hashrate estimation.
9. Reward splitting means that orphaning blocks no longer increases malicious miner's rewards (up to the limit of 20 blocks). There is no reward for including uncle blocks because malicious miners will never include them and honest miners have enough incentive through the cumulative difficulty increase that they bring due to being counted in the difficulty adjustment algorithm (a heavier chain is more difficult to reorg, which secures past block rewards waiting to be unlocked). 

The exact effect of this proposal (in terms of rewards for a specific attacker strategy) is unclear (pending Monte Carlo simulations), but it should be much closer to a fair distribution.

### References

[1] Majority is not Enough: Bitcoin Mining is Vulnerable https://arxiv.org/abs/1311.0243

[2] FruitChains: A Fair Blockchain https://eprint.iacr.org/2016/916

[3] Optimal Reward Allocation via Proportional Splitting https://arxiv.org/abs/2503.10185

[4] One Weird Trick to Stop Selfish Miners: Fresh Bitcoins, A Solution for the Honest Miner. https://eprint.iacr.org/2014/007

[5] Publish or Perish https://www.researchgate.net/publication/312184074_Publish_or_Perish_A_Backward-Compatible_Defense_Against_Selfish_Mining_in_Bitcoin

[6] Lay Down the Common Metrics: Evaluating Proof-of-Work Consensus Protocols' Security https://ieeexplore.ieee.org/document/8835227

[7] https://github.com/monero-project/research-lab/issues/141



# Discussion History
## dimagid | 2025-08-27T21:14:33+00:00
@tevador, thanks for the proposal. How does it mitigate a selfish mining attack that prioritizes discrediting RandomX and destabilizing the network over profit? Specifically, how do the consensus rules (like k=3 and the 1-day coinbase maturity) make such an ideological attack prohibitively expensive and less effective at causing visible disruption, even with external funding?

## tevador | 2025-08-28T07:11:24+00:00
> how do [the proposed changes] make such an ideological attack prohibitively expensive [...]?

I never claimed that this proposal makes attacks prohibitively expensive.

> How does it mitigate a selfish mining attack that prioritizes discrediting RandomX and destabilizing the network over profit?

Selfish mining is typically employed for profit. I'd argue that any pool who mines Monero at least partially cares about profits, including the current malicious pool.

But the mitigation stategies described here also help against an irrational attacker who does not care about mining profits. Overall, they would cause less disruption to the network:

1. Malicious reorgs would be much less frequent due to the new fork choice policy. The attacker has to mine 3 more blocks than the honest chain in order to reorg. (This applies to both proposals.)
2. Even if the attacker does reorg, honest pools would typically not lose revenue due to reward splitting. (This only applies to the second proposal.)
3. The attacker would be much less likely to cause a reorg that invalidates transactions, which would have to be 20 blocks deep instead of the current 10 blocks. (This only applies to the second proposal.)

## shortwavesurfer2009 | 2025-08-28T10:41:45+00:00
This would require adjusting the fee back to 0.3 Monero per block, correct?

I think it would also require adjusting the ring signature decoy selection algorithm because currently I believe that's set to deal with 10 blocks as the lock time.

## tevador | 2025-08-28T12:52:14+00:00
> This would require adjusting the fee back to 0.3 Monero per block, correct?

Yes, the block reward would be halved to 0.3 and the penalty free block size would also be halved. I forgot to mention this explicitly.

## tevador | 2025-08-28T12:55:52+00:00
> I think it would also require adjusting the ring signature decoy selection algorithm because currently I believe that's set to deal with 10 blocks as the lock time.

Yes, the wallet side code would need to be adjusted to match the new lock time consensus rule. Note that the decoy selection algorithm itself is not a consensus rule. In any case, decoy selection will go away with FCMP.

## monerobull | 2025-08-29T08:18:26+00:00

> Couldn't an adversary with enough hash add thousands or as many miner addresses in field as they want and distribute the hash-power so each miner_address can still get paid 0.000000000001 XMR and all those ID get added into the chain?

I guess this depends on if this data can be pruned after some time? 

## tevador | 2025-08-29T10:45:43+00:00
> Is that on-chain then?

Yes, everything needed for consensus must be on-chain.

> If so couldn't this be spammed? Or bloat the chain significantly?

It could be spammed the same way miners can now spam outputs in their coinbase transaction. The only difference is that a spammy block N would force the miner of block N+20 to create a lot of outputs. That could be mitigated by counting the size of the coinbase outputs in the size of block N and not N+20. Additionally, there could be some limit on the number of coinbase outputs per block. A typical block should only have one address in the `miner_address` field, which is 65 bytes (unless it's mined by p2pool).

(The text above is a reply to a comment that was later deleted.)

> I guess this depends on if this data can be pruned after some time?

Yes, both `miner_address` and `uncle_blocks` are prunable (i.e. nodes can prune them after verification).

## venture-life | 2025-08-29T21:27:28+00:00
Thanks @tevador for this proposal. It's very intriguing.
One change not listed yet is probably the relaying of competing in-time blocks (so that uncles are reliably included). 

I haven't fully grasped all the parts yet, but once I have them lined up, I will try to simulate the changes and hopefully will lead to the same benchmark numbers from the PoP paper. I'm currently dissecting the implications of 2 branches longer than 2 blocks each. The tips of both won't have any uncles referenced if I understand correctly? Ie, Reward splitting only applies to the first block of each branch from the mutual parent.

Another thing I'm unsure about, is whether the "Perish" part can be recouped if the attacker has a lead of 1 and embeds the the public block once it arrives in his next block template.

> [W]eighted FRP addresses the selfish mining problem at the price of sacrificing partition recovery time. In our scheme, previously separated groups of miners would consider blocks mined by the other groups during the partitioned period late and only recognize the weight of their own blocks. Consequently, every group works on its own chain until the first rule in weighted FRP applies.

This quote is from the PoP paper, end of page 13. This seems very similar to the current first-seen rule. It depends on the connectivity of an attacker (gamma). I don't think this paragraph is actually correct in the paper, it should fall back to rule 3 in this case. In our case, deterministic selection. Which seems promising when competing blocks are relayed. 


## venture-life | 2025-08-29T22:03:22+00:00
I think I understand now what they mean by 
> [...] Consequently, every group works on its own chain until the first rule in weighted FRP applies.

In their simulation, they have segregated the honest miners `(1 − α)/2` since there will likely be edge nodes who deems blocks late or in-time differently from the rest. I'm not sure if even in the absence of an malicious entity this might happen considering the higher block frequency (1min). Personally, I like the deterministic selection of a branch in this case.

Edit: Also, is it possible to have two different kind of uncles, eg, in-time uncles affecting the weight and reward-splitting, and late uncles affecting reward splitting only? 

## tevador | 2025-08-30T09:16:22+00:00
> One change not listed yet is probably the relaying of competing in-time blocks (so that uncles are reliably included).

I only listed consensus changes. But yes, all valid uncles would be relayed.

> I'm currently dissecting the implications of 2 branches longer than 2 blocks each. The tips of both won't have any uncles referenced if I understand correctly?

Depends on if the selfish miner selected "publish" or "perish". If the selfish miner's chain is entirely private, it will have a weight of zero (all blocks are late). If the selfish miner is publishing each block in time, the public chain will have uncles included that will again make it have a higher weight.

> Reward splitting only applies to the first block of each branch from the mutual parent.

Reward splitting is orthogonal to PoP. Uncles relevant for RS can be included late (up to 20 blocks later). Uncles relevant for PoP are more narrowly defined.

> Another thing I'm unsure about, is whether the "Perish" part can be recouped if the attacker has a lead of 1 and embeds the the public block once it arrives in his next block template.

If the attacker has a private block N+1, once the public N+1 arrives, he can either immediately publish his N+1, in which case it can be included as an uncle by the public chain block N+2, or he can withhold N+1, in which case it won't be counted in the weight of his chain. Both options have the same net effect.

See the PoP Fig. 3 (left side). The only case when the selfish miner wins unconditionally under PoP is when he mines 2 blocks while the honest chain mines 1 block (the SSH case). All other cases depend on tie breaking and will only have a 50% chance of success.

This means that under PoP, there would mostly be 1-block reorgs and 2-block reorgs would only have 50% chance of success. 3-block reorgs or longer would be much less likely because they would require the selfish chain to be 3 blocks longer to skip the PoP weight rule entirely (e.g. the public chain has 3 blocks, the attacker has 6 blocks etc.).

> there will likely be edge nodes who deems blocks late or in-time differently from the rest. I'm not sure if even in the absence of an malicious entity this might happen

I think this shouldn't happen if `D` is set to 2x the maximum block propagation time. Then all honest blocks will always be in time.

E.g.:

At time `t`, honest node `A` mines block `BA1`.
At time `t+D/2`, honest node `B` mines block `BB1` (just as `BA1` arrives). Note that `BB1` cannot be mined any later than this because node `B` will start mining block `BB2` immediately after receiving `BA1`.
At time `t+D`, node `A` receives block `BB1`.

With deterministic selection, at time `t+D`, all honest nodes will be mining on top of the same block while including the other block as an uncle.

If `B` is a malicious node, it can release block `BB1` later than at `t+D/2`, which will cause some nodes to deem the block to be late, but I don't think this can benefit the attacker.

> Also, is it possible to have two different kind of uncles, eg, in-time uncles affecting the weight and reward-splitting, and late uncles affecting reward splitting only?

This is already included in the proposal. Under the PoP fork choice rule, late blocks have a weight of 0 regardless of any included uncles. Reward splitting doesn't care about late blocks. It comes into effect 20 blocks later when one of the forks had alread won (assuming 20+ block reorgs don't happen).

## venture-life | 2025-08-30T11:31:33+00:00
Thanks for the input. 
IIUC, It's actually quite nice, any block withheld (and matched upon the public finds one), cannot be mined upon efficiently _before match_ since the public chain would incorporate the matched block as an uncle.

> If the attacker has a private block N+1, once the public N+1 arrives, he can either immediately publish his N+1, in which case it can be included as an uncle by the public chain block N+2

I hope my follow-ups are constructive. Just to confirm, currently a malicious miner has a better connectivity to some honest miners than they have to the rest. So, for example, if I receive 2 blocks at the same height and both within `D`, would I know include the second as uncle and mine on the first, or would I rather treat them equally and resort to rule 3, deterministic selection? 

## tevador | 2025-08-30T11:41:12+00:00
> So, for example, if I receive 2 blocks at the same height and both within D, would I know include the second as uncle and mine on the first, or would I rather treat them equally and resort to rule 3, deterministic selection?

If both blocks `BA1` and `BB1` are in time, you will apply the deterministic selection rule, which will tell you e.g. to mine on top of `BB1`. In that case, you will include `BA1` as an uncle block.

## venture-life | 2025-08-30T12:20:38+00:00
That's really cool. I know you mentioned this earlier already but it's nice to have gone through all the parts working in conjunction. Like, assuming the selfish miner would have won the coin flip, he still couldn't have been mining _efficiently_ before broadcasting, since others would mine (granted on the same tip) with the weight of an uncle :)

## jeffro256 | 2025-08-31T00:17:06+00:00
I would be in favor of raising the difficulty window to 2-3 days instead of 1. I remember a while back when some large miner was causing the difficulty to thrash up and down because they would mine only 1/2 of the day. They would turn off when the difficulty rose, then turn back on after the difficulty crashed.

## nahuhh | 2025-08-31T21:01:05+00:00
> I would be in favor of raising the difficulty window to 2-3 days instead of 1. I remember a while back when some large miner was causing the difficulty to thrash up and down because they would mine only 1/2 of the day. They would turn off when the difficulty rose, then turn back on after the difficulty crashed.


I too remember that. Blocks would be every 1 min while the 1.5gh botnet was mining, then every 4 mins when it stopped.

A longer difficulty allows longer periods of attack though - and longer period of slow blocks when they stop.

note that w/o using uncles/orphans in the difficulty calculation, the difficulty window doesnt do anything to hamper selfish mining.

re longer diff adjustment windows: on the contrary, i think a shorter difficulty window would lead to shorter attacks.

i would be in favor of calculating difficulty dynamically so that large deviations to the block production dont delay the diff increase/decrease unnecessarily.

something like
```
diff_period = 720 // includes uncles 

// example values
blocks_expected = 20
blocks_seen = 40 // includes uncles

if (blocks_expected < 20 || blocks_expected > (blocks_seen * 0.8)) {
    new_diff_period = diff_period;
} else {
    new_diff_period = diff_period / ((blocks_seen / blocks_expected) * 4);
}
```

in this example @ 2x block production rate, the "burst" `new_diff_period` would be 90 blocks

## tevador | 2025-09-01T06:54:23+00:00
@jeffro256 @nahuhh 

> I would be in favor of raising the difficulty window to 2-3 days instead of 1.

> i would be in favor of calculating difficulty dynamically so that large deviations to the block production dont delay the diff increase/decrease unnecessarily.

I think that's a separate issue out of scope of this proposal.

## 0xalank | 2025-09-04T19:13:37+00:00
>  I first want to disqualify all mitigation strategies that rely on more frequent hashrate sampling
> A block consisting of 100 work shares would require 1.5 seconds just to verify the PoW.

I would challenge the immediate dismissal of hashrate sampling for future work. Since RandomX validation can be done async upon receiving the sample as opposed to during block validation time. So if it were to in reality be 1.5 seconds to validate 100 samples, this can be done over the 2 minute block time with significantly impacting the uncle rate.

Even if it were not to be done async, sub second validation for ~100 RandomX hashes would be expected.

## tevador | 2025-09-04T20:27:28+00:00
@0xalank

It's probably somewhat feasible for online verification (P2Pool does it), but the impact on chain verification would not be small - e.g. 100 hours of CPU time per year of blocks instead of the current 1 hour of CPU time.

I would consider these strategies if they offered significantly better protection from selfish mining, but they don't. The referenced paper [6] tests two such strategies (Fruitchains and Subchains) and they perform worse than reward splitting with just uncle blocks. I see no reason to pay the high PoW cost for an inferior defense strategy.


## 0xalank | 2025-09-04T21:36:57+00:00
@tevador 

In Zhang & Preneel Fruitchains and Subchains perform poorly because fruits and "weak blocks" receive no immediate reward, making withholding risk-free.

I would imagine if you want the softest deployable defense first, PoP (with k=3, D≈5s) reduces selfish-mining advantage without major protocol changes; but for removing the economic incentive under α<~0.35 and adding robust hashrate sampling, PRS with workshares outperforms uncle-only RS.

Another consideration is uncle-only RS may not provide sufficient samples (~720 uncles over 24 hours as of today), which is too sparse to accurately estimate hashrate share on short timescales, whereas workshares via PRS can provide more samples per block interval and thus a much tighter coupling between the sampling and the honest majority.

## tevador | 2025-09-05T08:46:32+00:00
> PRS with workshares outperforms uncle-only RS

AFAIK there is no qualitative difference between PRS with workshares and RS with uncles. The performance depends on the hashrate sampling frequency, which can be the same for both.

My hard forking proposal already includes 2x faster block time. This could probably be increased further if we find the PoW cost acceptable and the performance benefit is worth it. It will need to be simulated.

## josetornante | 2025-09-06T12:30:46+00:00
This seems similar to the system implemented by Virel, [MiniDAG](https://virel.org/docs/technical-features/minidag/) (already a feature in the mainnet), but with a delayed block reward for side blocks (Virel does not reward side blocks, they are only accounted in the cumulative difficulty). We have currently a block time of 15 seconds and a limit for inclusion of side blocks of 3 blocks (45 seconds). Orphans are much less common with this MiniDAG.

## tevador | 2025-09-08T19:25:30+00:00
> Virel does not reward side blocks, they are only accounted in the cumulative difficulty

The main reason why selfish mining works is that a reorg steals the block reward of the orphaned blocks. Uncle blocks need to have an equal block reward to disincentivize selfish mining.

In other words, Virel is as vulnerable to selfish mining as Monero.

## ArticMine | 2025-09-12T03:50:01+00:00
One question I have is how will this impact scaling penalty and related fees. In particular the relative incentives between the miner who mines block N and the miner who receives the reward at block N-20.

## tevador | 2025-09-12T16:48:59+00:00
There is no impact. The reward for block N-20 is calculated based on the fees and the size of block N-20. The miner of block N just creates the coinbase output for the previously calculated amount going to the miner of block N-20 (assuming no uncle blocks of N-20 are included in the chain).


## ArticMine | 2025-09-15T01:53:38+00:00
I am concerned that this can be manipulated by malicious miner who, for example:

1) Mines a block with no rewards 2x the short term median, MS, where the penalty, P, equals the base block reward, R

2) Collects all the fees off chain; for example via a website. 

In this scenario the reward splitting would  be splitting 0 XMR  with the orphan blocks. 

One way I see to address this would be to carve out transaction fees, the penalty and 10% of the base  block reward (in this case 0.03XMR) . This would be paid to the block at N-20 at the time the block is mined. This would eliminate those parts of the block reward that can be controlled by the miner of block N-20 (fees and the penalty), while allowing 10% of the base block reward to cover the situation where the miner chooses to subsidize the penalty. The latter actually occurred in early 2017. This also would allow for block signing. up to 10% of the base  block reward plus transaction fees less the penalty. 

The balance 90% of the base block reward (0.27 XMR) would be paid out by block N as proposed. This would involve two sets of coinbase transactions a regular one as now (fees, penalty plus 0.03XMR) paid at  the time block N-20 is mined and the delayed (0.27 XMR) paid when block 20 is mined.

On another note.  Halving both the base block reward, R and the penalty free zone, ZM works. We also would have to double the scaling rate. for the fee levels. This would allow the transactions to scale as before and would keep the fee paid by a given transaction the same (twice the fee rate but half the penalty).





## Gingeropolous | 2025-09-15T17:33:37+00:00
@tevador , in #145, you indicate that Publish or Perish cannot stop a 51% attack. From my understanding of PoP, this is only true if k != infinity.  (i wanted to post here to not clutter the lucky tx)

If k = infinity, then PoP does indeed prevent 51% attacks, because the remaining 49% of the network can still create and submit a block before the 51% does. (it becomes a race for that D parameter). 

(We should also probably define 51% attack. Are we just talking about deep re-orgs? Or are we including empty block production. PoP with k=infinity can prevent deep re-orgs. It can also lessen the effects of empty block production). 

And if we do want to back away from k=infinity, we could have k = 1000 or something else massive, so in the case that an authority can't swoop in to correct the agents in the autonomous system, it would eventually self correct. But most users with stalled daemons would probably find a way to reconnect to the proper chain. 

## tevador | 2025-09-15T18:28:52+00:00
@ArticMine That's a valid concern. However, giving 10% of the reward directly to the block miner might incentivize selfish mining. I'm not sure if there is a better solution.

@Gingeropolous The table in #145 assumes PoP with k=3. You are right that PoP with k=∞ can stop 51% attacks, but I wouldn't recommend using it because it can spontaneously chain split, which is arguably worse than a deep reorg. PoP with k=1000 has the same problem, but the chain split will eventually resolve. However, depending on the hashrate distribution between the split chains, it could take up to several days, so it's not much better than k=∞.

## ArticMine | 2025-09-17T03:22:52+00:00
It comes down to what the actual selfish mining advantage is. Then making it unprofitable. 

For example at close to 50% selfish mining in theory comes in at 2x since it produces 100% of the blocks rather than 50%. At ~35% its get more interesting. The selfish chain should fall behind, still there may an isolated burst. 

The other factor is the fee in reward. It is currently 2% -3%. With full penalty free zone it would be 5% - 6%.  if fees double the fees then 2x the above. Once we start scaling then fee in reward will drop. 

There is room to drop the 10% of the base block reward paid up front  (block n-20) down to even 1% and still make block signing work, although I would prefer at least 2% - 5%. Furthermore this percentage can be deducted from the block miners reward on the back end (block N), effectively making the base block reward part prepayment upfront revenue neutral. What must not be deducted at the back end (block N) is fees and penalties for the reasons I mentioned. above. 

Is there a scenario, that I am missing, where the selfish miner gets less than say 10% of the block reward here? 

## tevador | 2025-09-17T16:52:34+00:00
> There is room to drop the 10% of the base block reward paid up front (block n-20) down to even 1% and still make block signing work, although I would prefer at least 2% - 5%.

This proposal doesn't include block signing and I wouldn't recommend it.

Is there a reason to pay any portion of the base reward upfront? I think it would be OK to give `fees - penalty` to the miner at block N-20 and split the `base_reward` at block N. I don't see any scenario when a non-malicous miner would willingly make a block so large that the penalty exceeds the fees. That would be irrational.

## ArticMine | 2025-09-17T20:49:13+00:00
> This proposal doesn't include block signing and I wouldn't recommend it.

Linking the up front partial payment of the base reward to block signing does male a lot of sense to me. I expect that block signing will require between 1% and 10% of the block reward. This can be addressed in a future block signing proposal. It should only be added here once the block signing requirements are determined. I will note that if block signing is not implemented then there is no reason to add a block signing alone partial base block reward pre payment here, 

 >  I don't see any scenario when a non-malicous miner would willingly make a block so large that the penalty exceeds the fees. That would be irrational.

In theory this is correct. The historical reality, however did provide a valid reason for altruistic miners to act irrationally by mining blocks where the penalty exceeds the fees. This occurred in 2017 with the RingCT hard fork, where a typical transaction went from ~400 bytes to ~13500 bytes yet the penalty free zone ZM was only increased from 40000 bytes to 60000 bytes. The result was that transaction were simple getting stuck because of very high fees. The interim solution was modify the mining code to allow for  one unprofitable transaction. This kept the network going until a subsequent hard for later in the year increased ZM to 300000 bytes. In retrospect ZM should have been increased to 1500000 bytes at the time. This was only really fixed when bullet proofs came in in 2018, 2in 2out transaction dropped to ~2700 bytes and ZM stayed at 300000 bytes. 

I see a small amount around of the base block reward  1%  to 2% to be paid up front to the block miner to allow for altruistic miner who wish to support Monero as reasonable, especially  given the history of this. This can also be used for block signing above and can be deducted from the payment to the block miner 20 block later in the case of selfish mining. 



## tevador | 2025-09-18T05:21:28+00:00
> I see a small amount around of the base block reward 1% to 2% to be paid up front to the block miner to allow for altruistic miner who wish to support Monero as reasonable, especially given the history of this.

IMO, the base block reward is not needed for altruistic use cases. Altruistic miners can simply include their own transaction that pays a higher fee to compensate for the penalty caused by another transaction. In practice, there are almost always some transaction in the mempool that pay a higher fee than needed for penalty purposes, so it's likely that the fees alone would be enough to include at least one unprofitable transaction.

## ArticMine | 2025-09-18T20:07:34+00:00
> IMO, the base block reward is not needed for altruistic use cases. Altruistic miners can simply include their own transaction that pays a higher fee to compensate for the penalty caused by another transaction. In practice, there are almost always some transaction in the mempool that pay a higher fee than needed for penalty purposes, so it's likely that the fees alone would be enough to include at least one unprofitable transaction.

Creating an additional transaction and paying the fee for it could easily cost the altruistic miner 10x , 40x or even more times the cost of the proposed altruism. This because the uneconomic transaction could be over by say 10% of the fee and the additional transaction of similar weight could trigger the next fee level because of the quadratic penalty. As for high fee transactions they would be already in the block. Any rational miner would include them first. IMO this additional transaction model would have failed in early 2017. 

The reality here is that the first 50%, followed by the next 30% of the base block reward are the most critical  to deter selfish mining. After that, IMO, I doubt it will have any significant impact on the selfish miner. This leaves 20% of the base block reward that can be used to claw back any payments made upfront, by adjusting the split between what is paid to the orphan blocks vs what is paid to the selfish miner after the 20 blocks. 

This is a very good proposal, which I would love to support,  but we have to very careful not to create unintended negative incentives by attempting to extract the last piconero from the selfish miner. 

## tevador | 2025-09-19T09:13:52+00:00
> Creating an additional transaction and paying the fee for it could easily cost the altruistic miner 10x , 40x or even more times the cost of the proposed altruism. This because the uneconomic transaction could be over by say 10% of the fee and the additional transaction of similar weight could trigger the next fee level because of the quadratic penalty. As for high fee transactions they would be already in the block. Any rational miner would include them first. IMO this additional transaction model would have failed in early 2017.

Let's take a real world example.

Block [3503287](https://xmrchain.net/block/3503287) has a total size of 301 060 bytes. The total fees are 18343 micronero and the penalty is 7 micronero.

An atruistic miner could still include over 50 000 bytes of zero-fee transactions and the total block reward would still be more than the base reward of 0.6 XMR (max block size would be 352 452 bytes).

If you think that block has unrealistically high fees (it's actually close to average), let's assume that all transactions in the block pay the minimum fee (0.02 micronero per byte). The total fees would be about 6019 micronero. An atruistic miner could still include almost 29 000 bytes of zero-fee transactions without reducing the block reward below 0.6 XMR (max block size would be 330 047 bytes).

We can go even further and assume the block was full of zero-fee transactions. Let's say the altruistic miner wants to add one additional 13 KB transaction (corresponds to about 18/2, way above average tx size) and pay the penalty with his own 1/2 transaction with a size of 1531 bytes. How much would the tx fee of his transaction need to be? About 1621 micronero. The 13 KB transaction would normally need about 260 micronero of tx fees, so the miner is paying about 6x the cost of atruism in the worst case scenario of 314 KB of zero-fee transactions in a block.

I think it's safe to say that altruism is more than possible without dipping into the base block reward.

## ArticMine | 2025-09-23T02:24:14+00:00
Thank you. This is very helpful. 

I do agree that the Fee in Reward for the short term median will easily cover any altruistic mining. Block 3503287 is a great example. 

 I fully support this selfish mining mitigation proposal and urge its adoption. 

## venture-life | 2025-09-24T19:31:44+00:00
I got some preliminary results of Publish or Perish simulated here: https://github.com/venture-life/mining-simulator/blob/main/out/simulation-results.md

Subject to errors/mistakes. The simulation only models the soft-fork proposal so far, no vesting/reward splitting. Also, I forgot to change to 1-min block frequency as well. So the simulation-results are done with 2-min block frequency.

To note (maybe obvious), but when two branches are racing, the weight difference is usually +-2 only, since the subsequent "cousins" from the initial uncle-branch are not included.

# Action History
- Created by: tevador | 2025-08-27T18:21:26+00:00
