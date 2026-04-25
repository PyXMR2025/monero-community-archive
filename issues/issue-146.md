---
title: Share or Perish (selfish mining mitigation)
source_url: https://github.com/monero-project/research-lab/issues/146
author: tevador
assignees: []
labels: []
created_at: '2025-09-25T06:22:27+00:00'
updated_at: '2026-04-25T12:27:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Share or Perish

The previously proposed Publish or Perish [1] (PoP) has some shortcomings. With the default parameter `k=3`, it cannot prevent deeper reorgs, like those that happened recently. Increasing `k` comes with a risk of nontrivial chain splits. Even with `k=3`, partition recovery with PoP might take over 20 blocks in some cases [2].

This is a new proposal "Share or Perish" (SoP), partly based on PoP and combined with the idea of workshares [3], which I previously dismissed due to their high cost, but this proposal presents parameters with acceptable costs. Similarly to PoP, SoP is a soft-forking proposal that only introduces a new fork choice rule but doesn't affect rewards or other consensus rules. SoP should be much more resilient to long reorgs and has better partition recovery time than PoP.

### Parameters

SoP defines three security parameters `w` (workshare ratio), `d` (network propagation delay, same as PoP) and `k` (partition recovery, same as PoP).  

| Parameter | Description | Recommended value |
|-----------|-------------|-------------------|
| `w`       | workshare ratio | 16 |
| `d`       | network propagation delay | 5 |
| `k`       | partition recovery | 3 |

(Table 1)

### Work objects

Let's recall Monero's PoW header format:

| Field | Type | Size (B) |
|-------|------|------|
| version_major | varint | 1 |
| version_minor | varint | 1 |
| timestamp | varint | 5 |
| prev_id | hash | 32 |
| nonce | int | 4 |
| tx_tree_hash | hash | 32 |
| num_transactions | varint | 1-2 |
| **Total**|| 76-77 |

(Table 2)

Miners take this PoW header (also called the hashing blob) and search for a nonce value that meets the current block difficulty.

Normally, only the block header itself is used as a proof-of-work. SoP introduces an additional work object called "workshare", which is defined as a distinct PoW header that meets at least `1/w` of the current block difficulty and has the same `prev_id` value as the containing block.

#### Extra block data

Valid workshares are included in blocks. On average, a block will contain `w-1` workshares. A workshare can be serialized with only 4 fields from Table 2: `timestamp`, `nonce`, `tx_tree_hash` and `num_transactions`. The remaining values are implicit.

There are two ways how workshares can be included in a block:

1) They are placed in tx_extra of the miner transaction. This is the simplest backwards-compatible solution with guaranteed data availability. However, this introduces extra non-prunable data into the blockchain (about 170 MB per year with the recommended parameters).
2) Each block contains a commitment to the set of workshares, but the data itself is sent in a separate P2P message. This would be more complex to implement, but allows for workshares to be pruned when they are not needed anymore for verification.

#### Uniqueness of workshares

SoP additionally requires miners to set the `version_minor` block header field to be equal to the number of workshares included in the block. Workshares included in the block must have sequential values of `version_minor` starting from `0` and ending with `block.version_minor-1`.

This rule serializes the mining of workshares and its purpose is to make it harder for malicious miners to withhold their own workshares, while including the workshares published by other miners.

### Chain weight

Let `diff(x)` be a function that returns the difficulty of the block at height `x`. SoP uses a modified weight for the last `10*w` blocks of the blockchain. Let `t` be the chain tip height. The weight of a block at height `h` is equal to the sum of the weights of its work objects according to the following table:

| Block height   | Block header | Workshare |
|----------------|--------------|-------------|
| `h > t - 10*w` | <code>l<sub>b</sub>\*diff(h)/w</code>| <code>l<sub>b</sub>\*l<sub>w</sub>\*diff(h)/w</code> |
| `h <= t - 10*w`| `diff(h)`    | `0`        |

(Table 3)

The lateness factors <code>l<sub>b</sub></code> (for blocks) and <code>l<sub>w</sub></code> (for workshares), which can have a value of `0` or `1`, are described in the next section.

For block heights `t - 10*w` and older, workshares have no impact on the block weight, so they can be ignored and don't need to be verified. This means that the impact of SoP on new nodes downloading the blockchain is negligible.

#### Lateness factors

Similar to PoP, SoP also reduces the weight of "late" blocks to zero. This is accomplished with a block lateness factor <code>l<sub>b</sub></code>.

There is a separate factor <code>l<sub>w</sub></code> which causes the weights of withheld workshares to be zero even if the containing block is not late.

Let <code>h<sub>0</sub></code> be the block height when the node came online.

Let there be an alt-chain that forks off the main chain at height <code>h<sub>f</sub></code> and contains <code>n<sub>f</sub></code> work objects that are not contained in the main chain.

Let `block_seen` be the unix timestamp when the evaluated block of height `h` was first seen by the node. Let `share_seen` be the unix timestamp when the evaluated workshare was first seen by the node.

Let `main_seen` be the unix timestamp when the main chain block of height `h` was first seen by the node. If the main chain block of height `h` doesn't exist (i.e. the alt-chain is ahead), we set `main_seen = block_seen`.

The lateness factors are then defined as follows:

| Condition | <code>l<sub>b</sub></code> |
|------------------------|----------------------------------------|
| if <code>h<sub>0</sub> < h<sub>f</sub> && n<sub>f</sub> < k*w && block_seen - main_seen > d</code>                | `0` |
| else               | `1` |

(Table 4)

| Condition | <code>l<sub>w</sub></code> |
|------------------------|----------------------------------------|
| if <code>h<sub>0</sub> < h<sub>f</sub> && n<sub>f</sub> < k*w && main_seen - share_seen <= d</code>                | `0` |
| else               | `1` |

(Table 5)

The lateness factors can be distinct from `1` only if the node was online before the fork height and the two chains differ by fewer than `k*w` work objects.

By Table 4, a block is considered to be late if it's seen more than `d` seconds after the main chain block of the same height.

By Table 5, a share is considered to be late if it's not seen more than `d` seconds before the main chain block of the same height.

Note that the lateness factors are subjective; different nodes can calculate different values of <code>l<sub>b</sub></code> and <code>l<sub>w</sub></code> for the same block, which can lead to different chain weights.

#### Tie breaking

If a node sees two chains of the exact same weight, it makes a random selection.

### Security

We will evaluate the security of SoP with the recommended parameters of `w = 16`, `d = 5` and `k = 3` against an attacker with `α = 0.33`, i.e. a minority hashrate attacker.

#### Short forks

A selfish miner can decide to withhold blocks or both blocks and workshares.

If only blocks are withheld (i.e. the attacker still publishes mined workshares for the public chain tip), SoP behaves similarly to PoP for block races of length 1. Once the attacker starts mining on top of a secret block, his workshares can no longer be relayed and will have <code>l<sub>w</sub> = 0</code>, so the attacker's chain is always at a disadvantage.

For withholding shares, the attacker has a dilemma. A workshare must be published at least 6 seconds before its containing block to be counted (Table 5). On the contrary, the attacker's withheld block must be published at most 5 seconds after the corresponding honest block (Table 4). Therefore any witholding strategy will always have either <code>l<sub>w</sub> = 0</code> or <code>l<sub>b</sub> = 0</code>.

Additionally, when withhoding shares, the attacker typically won't be able to include honest workshares in his first private block due to duplicate `version_minor` values.

#### Long forks

If the attacker can mine at least 48 work objects faster than the honest majority, he can avoid the lateness penalties.

The probabilty of this happening is < 0.06% with `α = 0.33`. The attacker can expect to achieve this on average once per 10 days of selfish mining (these numbers are based on the formulas from [4]) and the result will be, on average, a 3-block reorg. This can be compared with Nakamoto consensus, when the `α = 0.33` attacker can effect a 3-block reorg on average once per hour.

For deeper reorgs of 10+ blocks, the situation is more complicated, but Monte Carlo simulations show that the attacker can achieve on average about 1 such reorg per 3 years of stubborn mining (see [5] for details about stubborn mining strategies). With Nakamoto consensus, the attacker can expect to achieve several 10-block reorgs per day.

Note that by Table 3, blocks with 160+ confirmations will use the standard block difficulty as their weight. The SoP chain weight will converge to this value with a sufficient number of blocks.

#### Partition recovery

Since the subjective block weights are limited to forks of fewer than 48 work objects (Tables 4 and 5), network partitions will on average resolve after 3 blocks, when the objective chain weights kick in. The same applies to offline nodes joining the network (which can be considered a special case of a network partition).

### References

[1] [Selfish mining mitigations (Publish or Perish)](https://github.com/monero-project/research-lab/issues/144) (github issue)

[2] [Publish or Perish: A Backward-Compatible Defense Against Selfish Mining in Bitcoin](https://www.researchgate.net/publication/312184074_Publish_or_Perish_A_Backward-Compatible_Defense_Against_Selfish_Mining_in_Bitcoin) (PDF paper)

[3] [FruitChains: A Fair Blockchain](https://eprint.iacr.org/2016/916) (PDF paper)

[4] [Success probability of a double-spend attack with minority hashpower share](https://github.com/monero-project/research-lab/issues/102#issuecomment-2402750881) (github comment)

[5] [Stubborn Mining: Generalizing Selfish Mining and Combining with an Eclipse Attack](https://eprint.iacr.org/2015/796) (PDF paper)

# Discussion History
## tevador | 2025-09-25T22:23:34+00:00
Preliminary Monte Carlo simulations discovered an issue. The actual average time between 10+ block reorgs is not 5-6 years, but only about 65 days. This difference is due to the fact that the attacker can use the honest workshares in the first block of the private chain, but the honest chain can't use the attacker's withheld shares. In rare cases, the first block takes a long time to mine, allowing the attacker to build a chain weight advantage that can be exploited to perform a 10+ block reorgs with additional luck (mainly due to several workshare-poor blocks found by the honest chain in a quick succession).

If the attacker doesn't include honest workshares in his first private block, achieving a 10+ reorg is nearly impossible. However, I can't think of any way to prevent the attacker from including honest workshares. Note that increasing `w` doesn't help much against this strategy.



## tevador | 2025-09-26T06:55:42+00:00
> However, I can't think of any way to prevent the attacker from including honest workshares.

A possible mitigation, although not a perfect one:

1. Require blocks to have `version_minor` equal to the number of included workshares.
2. Require all included workshares to have unique `version_minor` values.

This works in the synchronous case. In reality, the honest miners would produce some stale workshares with equal `version_minor` due to propagation delays. The attacker would not be able to use the majority of his secret workshares, as they would typically match `version_minor` of an honest workshare.

## tevador | 2025-09-28T19:25:09+00:00
I updated my Monte Carlo simulation and tested more efficient attacker strategies aimed at network disruption rather than profits. Stubborn mining (see ref [5]) seems to perform the best in terms of the number of 10+ block reorgs.

The following table lists the average time between 10+ block reorgs an `α = 0.33` attacker can cause using T<sub>5</sub> stubborn mining (i.e. mining the private fork when up to 5 work objects behind the honest chain).

| `w` | unique workshares | uncle blocks | 10+ reorg avg. time |
|-----|-------------------|--------------|----------------|
| `8` |       No          |     Yes      |   ~3 days      |
| `8` |       No          |     No       |   ~4 days      |
| `16`|       No          |     Yes      |   ~10 days     |
| `16`|       No          |     No       |   ~11 days     |
| `8` |       Yes         |     Yes      |   ~14 days     |
| `8` |       Yes         |     No       |   ~19 days     |
| `16`|       Yes         |     Yes      |   ~2 years     |
| `16`|       Yes         |     No       |   ~3 years     |

"Unique workshares" refers to the `version_minor` rule described above. "Uncle blocks" specify if uncle blocks are counted in chain weight.

Based on these results, I made the following changes:

* Increased `w` from `8` to `16`
* Added a workshare uniqueness rule
* Removed uncle blocks

## venture-life | 2025-09-28T19:49:07+00:00
Regarding profitability, does it make sense to restrict the mining transaction of a work-object/block to `R=1/(version_number+1)` and include / merge with the mining-transaction of the highest-version workshare that was included?

Include / merge the highest-version workshare's mining transaction would need to be scaled as well by `R= version_minor / (version_minor+1)`

## tevador | 2025-09-28T20:19:03+00:00
> mining-transaction of the highest-version workshare

Workshares only include the data listed in Table 2. No transactions are relayed or validated. Including miner transactions would significantly increase the amount of extra data and most importantly, would require keeping workshares forever rather than pruning them after 160 blocks.

## tevador | 2025-09-29T10:48:10+00:00
Note: A workshare can be serialized with only 4 fields from Table 2: `timestamp`, `nonce`, `tx_tree_hash` and `num_transactions`. The remaining values are implicit. So the size of a workshare is 42-43 bytes. With `w=16`, that would take about 170 MB of blockchain space in tx_extra per year.

## lmb | 2025-09-30T07:47:20+00:00
Nit: would it make sense to define timestamps as monotonic clocks in second units? That would avoid clock skew issues due to NTP or similar.

## tevador | 2025-09-30T16:08:44+00:00
> Nit: would it make sense to define timestamps as monotonic clocks in second units? That would avoid clock skew issues due to NTP or similar.

That's unrelated to this proposal. I suggest to open a separate issue for this. SoP has no requirements for the timestamp field beyond the standard block validity rules.

## venture-life | 2025-10-14T21:24:31+00:00
@tevador in your simulation, do you have figures of what the average block share of an attacker with 33% hashrate share was, after the 10+block re-org was achieved?

I also have a question regarding SoP, but I'm not sure if these have practical relevance.

With 16 workshares, the mean time for a workshares will be 7.5s, 48% will be found within `D=5s`. I assume miners consume work-shares in their hashing blob immediately after arrival or self-found. However, with a block rate of `1/120s`, we have a 4% chance of finding a block within the next 5s. Should miners delay the propagation in this case (where a block is found too early for the last workshare to be counted), or on-receive, might they even rationally demote the block to a workshare? (*only relevant for the first 5s of hashing I think, and therefore not really practical)


## venture-life | 2025-10-15T13:13:07+00:00
Thought about it some more. It doesn't benefit to include a block as workshare (since it would be late by definition), but for the scenario described, a miner could keep mining on the `prev_id` so that the last workshare would get counted. 

According to table 5, a workshare is expired if not seen `D` seconds before it's containing block's arrival. This could be tightened to have it expired if not seen `D` seconds before it's containing block height's earliest arrival.

## tevador | 2025-10-15T17:45:04+00:00
> Thought about it some more. It doesn't benefit to include a block as workshare (since it would be late by definition), but for the scenario described, a miner could keep mining on the prev_id so that the last workshare would get counted.

Yes, including a block as a workshare makes zero sense. Mining on top of the previous block *might* be beneficial in edge cases, but only for a few seconds.

Note that a block with a "late" share will still benefit from it after ~3 blocks when the lateness penalty disappears (provided that the block is still part of the heaviest chain by that time).

> According to table 5, a workshare is expired if not seen D seconds before it's containing block's arrival. This could be tightened to have it expired if not seen D seconds before it's containing block height's earliest arrival.

Yes, it might work to remove the incentives for mining on top of the previous block. I'll think about it.

## Rucknium | 2025-11-25T21:41:13+00:00
@tevador Could you share your simulation code?

## tevador | 2025-12-06T17:15:25+00:00
@Rucknium 

Here: https://github.com/tevador/scratchpad/blob/master/share-or-perish/blockhain-sim.py

Should be able to reproduce the table from https://github.com/monero-project/research-lab/issues/146#issuecomment-3344168035

# Action History
- Created by: tevador | 2025-09-25T06:22:27+00:00
