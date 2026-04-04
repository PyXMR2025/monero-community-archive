---
title: Simple Market-Based Monero Fee Proposal
source_url: https://github.com/monero-project/research-lab/issues/152
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2025-10-28T00:50:44+00:00'
updated_at: '2025-12-02T15:37:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a simple Monero market-based fee proposal. The main motivations for this proposal are:

* To substantially simplify the fees and block size calculations. In many ways, simpler is better!
* To remove the need to "predict the future" by assigning a "fair" XMR/USD value. Some other proposals incorporate an implied value based on activity, which I believe is not a safe assumption (activity doesn't determine price). This proposal works for all XMR/USD values.
* To add more predictable scaling parameters.
* To improve privacy.

## Transaction Weight and Size

I will leave it to others to define a transaction's weight. I use weight in my calculations.

_See_ https://github.com/seraphis-migration/monero/issues/44

At the time of writing, consensus seems to be roughly around the following general statement:

> Make the tx weight calculation roughly byte size, where you can still calculate the weight of a tx in an offline context using n inputs, n outputs, and extra len.

This page doesn't further discuss transaction weight. It instead discusses with _what to do after we have a weight_.

This also doesn't conflict with PoWER; it only applies to the direct transaction fee.

## Other Proposals/References

* https://github.com/seraphis-migration/monero/issues/44
* https://github.com/ArticMine/Monero-Documents/tree/master
* https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf
* https://github.com/monero-project/research-lab/issues/133

## Summary

* Eliminate minimum fee (technically, it lowers it to the smallest XMR unit 1 piconero, or 0.000000000001 XMR).
* Create a small penalty free zone (e.g. 400 kB weight), called the "base space." If blocks stay under this size, miners of those block earn the full tail emission reward of 0.6 XMR.
* Allow miners to grow blocks from that zone to X (e.g. 2x the penalty zone size, in this example 800 kB weight).
* For each 1% of this additional "flex space" that is consumed, miners lose out on 1% of the tail emission. This is a linear penalty. Continuing the example of 400 kB of flex space above the 400 kB base space, a block of 404 kB would yield an issuance reward of 0.594 XMR.
* At point X (e.g. 800 kB), the block reward has decreased to 0. So a 800 kB block in the example would yield an issuance reward of 0 XMR.
* Allow miners to increase the maximum size of the "flex space" by y% per block (e.g. 10% per year).
* Implement a consensus rule to require all transaction fees to be a denomination of a power of e.g. 2 starting from the smallest Monero unit.


## Flex Space Growth 

<img width="886" height="484" alt="Image" src="https://github.com/user-attachments/assets/ab91d3ae-c8df-4e0f-8b40-b1249712cc8e" />

We can configure an appropriate flex space growth per block. I believe that a growth value of approximately 10% per year is a good target.

I do not believe that the base space should grow each year, though that could grow as well. An advantage to keeping it the same is that if Monero block space demand decreases over time, the low-cost "spam" potential does not increase.

We cannot predict the future, so we do not now exactly what growth rate is most appropriate. It should be a balance that allows for Monero network growth while still encouraging block efficiency.

I picked an initial flex space equal to the base space. A different value can be chosen if desired, but again, simplicity seemed like a reasonable option here.

## Miner Reward

<img width="1000" height="484" alt="Image" src="https://github.com/user-attachments/assets/7899febf-b455-4224-b1d2-edfb280102c0" />

Miner block reward decreases linearly for each percent of flex space consumed. The example above uses a flex space of 1000 kB.

This provides an incentive for miners to avoid using the flex space unless market conditions are favorable (if fees are high enough).

## Market Competition for Fees

This proposal treats market competition for block space as an advantage. This allows for Monero miners to charge as little as 1 piconero if there is no/low demand. It also allows for uncapped fees if demand for space is high.

The relationship between block space supply, transaction demand, and the XMR/USD price are allowed to dynamically play out in a free mining market.

This proposal still requires fees to be denominated. This improves privacy by requiring wallets to "fit in" at least somewhat. Fees that do not fit into a piconero/weight power of 2 are rejected by consensus rules.

In an efficient market, wallets should use a relatively small number of denominations at a given time, depending on the senders' willingness to pay for priority confirmations. However, allowing a huge range of values (1 to near-infinity) will prevent the Monero network from its users all converging on a single max fee level. The goal here is to achieve a balance that encourages transaction uniformity without requiring a specific, singular fee level (e.g. $0.10, as established by an oracle).

Using a power of 2 retains an incentive to communicate with a miner. A sender could collude with a miner by sending them their transaction at the next highest fee level, and receive a partial rebate if they overpay. Currently, Monero has much larger incentives with larger multipliers. Still, the power of 2 can be reduced to a smaller growth denomination in fees, for example 10% growth between denominations, if miner collusion is not adequately discouraged with this power of 2 proposal.


power | picos | XMR | USD@330
-- | -- | -- | --
0 | 1 | 1E-12 | $              0.00
1 | 2 | 2E-12 | $              0.00
2 | 4 | 4E-12 | $              0.00
3 | 8 | 8E-12 | $              0.00
4 | 16 | 1.6E-11 | $              0.00
5 | 32 | 3.2E-11 | $              0.00
6 | 64 | 6.4E-11 | $              0.00
7 | 128 | 1.28E-10 | $              0.00
8 | 256 | 2.56E-10 | $              0.00
9 | 512 | 5.12E-10 | $              0.00
10 | 1024 | 1.024E-09 | $              0.00
11 | 2048 | 2.048E-09 | $              0.00
12 | 4096 | 4.096E-09 | $              0.00
13 | 8192 | 8.192E-09 | $              0.00
14 | 16384 | 1.6384E-08 | $              0.00
15 | 32768 | 3.2768E-08 | $              0.00
16 | 65536 | 6.5536E-08 | $              0.00
17 | 131072 | 1.3107E-07 | $              0.00
18 | 262144 | 2.6214E-07 | $              0.00
19 | 524288 | 5.2429E-07 | $              0.00
20 | 1048576 | 1.0486E-06 | $              0.00
21 | 2097152 | 2.0972E-06 | $              0.00
22 | 4194304 | 4.1943E-06 | $              0.00
23 | 8388608 | 8.3886E-06 | $              0.00
24 | 16777216 | 1.6777E-05 | $              0.01
25 | 33554432 | 3.3554E-05 | $              0.01
26 | 67108864 | 6.7109E-05 | $              0.02
27 | 134217728 | 0.00013422 | $              0.04
28 | 268435456 | 0.00026844 | $              0.09
29 | 536870912 | 0.00053687 | $              0.18
30 | 1073741824 | 0.00107374 | $              0.35
31 | 2147483648 | 0.00214748 | $              0.71
32 | 4294967296 | 0.00429497 | $              1.42
33 | 8589934592 | 0.00858993 | $              2.83
34 | 17179869184 | 0.01717987 | $              5.67
35 | 34359738368 | 0.03435974 | $           11.34
36 | 68719476736 | 0.06871948 | $           22.68
37 | 1.37439E+11 | 0.13743895 | $           45.35
38 | 2.74878E+11 | 0.27487791 | $           90.71
39 | 5.49756E+11 | 0.54975581 | $        181.42
40 | 1.09951E+12 | 1.09951163 | $        362.84

## Initial Space Sizes

I am using the following rough values to estimate the Monero conditions with FCMP++:

* Transaction weight: 10 kB
* Free space: 400 kB
* Initial penalty space: 400 kB

| Year | Free Space Txs | Penalty Space Txs | Max Txs | Min Fee/Penalty Tx |
| --- | --- | --- | --- | --- |
| 0 | 40 | 40 | 80 | 0.015 XMR |
| 1 | 40 | 48 | 88 | 0.013 XMR |
| 2 | 40 | 57 | 97 | 0.011 XMR |
| 10 | 40 | 167 | 207 | 0.004 XMR |
| 20 | 40 | 498 | 538 | 0.001 XMR |


| This Many Tx/Blocks | Yield this Many Tx/Day | or this Many Tx/Year | Block Size |
| --- | --- | --- | --- |
| 40 | 28,800 | 10,512,000 | 400 kB |
| 80 | 57,600 | 21,024,000 | 800 kB |
| 88 | 63,360 | 23,126,400 | 880 kB |
| 97 | 69,840 | 25,491,600 | 970 kB |
| 207 | 149,040 | 54,399,600 | 2070 kB |
| 538 | 387,360 | 141,386,400 | 5380 kB |
| 1000 | 720,000 | 262,800,000 | 10000 kB |
| 2500 | 1,800,000 | 675,000,000 | 25000 kB |

Monero transactions per day in 2025: 15,000 to 45,000

Bitcoin transactions per day in 2025: 255,000 to 645,000.

Starting with a larger flex space may be preferable to some, but please keep in mind that:
1. 10 kB is likely an overestimate for FCMP average transaction weight
2. This basic calculation assumes that Monero transactions are about 25x larger (more costly) than Bitcoin transactions.
3. Money finds a way. If fees become expensive, this will encourage innovation for and increase demand for L2s and bridging.
4. The larger you permit the growth, the more challenging it becomes to run a node.

## Potential Enhancements

A more complicated model could look back at how full the last X blocks' flex spaces were, for example 3 months. If they are over 90% full (or a similar value), then an additional growth rate could be permitted. If they are less than e.g. 10% full, then the flex space could decrease. Personally, I think this complexity will cause more problems than it helps. However, allowing the flex space to _decrease slightly_ if it is not used for a long period of time could serve as a useful tool to discourage spam in an environment where XMR has low value.

---

If you want me to provide estimates for other variables, please let me know!

# Discussion History
## SamsungGalaxyPlayer | 2025-10-29T14:01:06+00:00
Here is an example that is more aggressive. I upped the initial flex space from 400 kB -> 600 kB (for initial block sizes of up to 1000 kB), and I upped the flex space growth to 25% a year. XMR/USD is still $330.

year | penalty max kb | tx/block | penalty min xmr/tx | penalty min usd/tx | max growth/yr gb
-- | -- | -- | -- | -- | --
0 | 1,000 | 100 | 0.010 | $                             3.30 | 263
1 | 1,250 | 125 | 0.007 | $                             2.33 | 329
2 | 1,563 | 156 | 0.005 | $                             1.70 | 411
3 | 1,953 | 195 | 0.004 | $                             1.27 | 513
4 | 2,441 | 244 | 0.003 | $                             0.97 | 642
5 | 3,052 | 305 | 0.002 | $                             0.75 | 802
6 | 3,815 | 381 | 0.002 | $                             0.58 | 1,003
7 | 4,768 | 477 | 0.001 | $                             0.45 | 1,253
8 | 5,960 | 596 | 0.001 | $                             0.36 | 1,566
9 | 7,451 | 745 | 0.001 | $                             0.28 | 1,958
10 | 9,313 | 931 | 0.001 | $                             0.22 | 2,448
11 | 11,642 | 1,164 | 0.001 | $                             0.18 | 3,059
12 | 14,552 | 1,455 | 0.000 | $                             0.14 | 3,824
13 | 18,190 | 1,819 | 0.000 | $                             0.11 | 4,780
14 | 22,737 | 2,274 | 0.000 | $                             0.09 | 5,975
15 | 28,422 | 2,842 | 0.000 | $                             0.07 | 7,469
16 | 35,527 | 3,553 | 0.000 | $                             0.06 | 9,337
17 | 44,409 | 4,441 | 0.000 | $                             0.04 | 11,671
18 | 55,511 | 5,551 | 0.000 | $                             0.04 | 14,588
19 | 69,389 | 6,939 | 0.000 | $                             0.03 | 18,235
20 | 86,736 | 8,674 | 0.000 | $                             0.02 | 22,794


Here is an even more aggressive example with the same flex space value but a growth rate of 50% a year:

year | penalty max kb | tx/block | penalty min xmr/tx | penalty min usd/tx | max growth/yr gb
-- | -- | -- | -- | -- | --
0 | 1,000 | 100 | 0.010 | $                             3.30 | 263
1 | 1,500 | 150 | 0.005 | $                             1.80 | 394
2 | 2,250 | 225 | 0.003 | $                             1.07 | 591
3 | 3,375 | 338 | 0.002 | $                             0.67 | 887
4 | 5,063 | 506 | 0.001 | $                             0.42 | 1,330
5 | 7,594 | 759 | 0.001 | $                             0.28 | 1,996
6 | 11,391 | 1,139 | 0.001 | $                             0.18 | 2,993
7 | 17,086 | 1,709 | 0.000 | $                             0.12 | 4,490
8 | 25,629 | 2,563 | 0.000 | $                             0.08 | 6,735
9 | 38,443 | 3,844 | 0.000 | $                             0.05 | 10,103
10 | 57,665 | 5,767 | 0.000 | $                             0.03 | 15,154
11 | 86,498 | 8,650 | 0.000 | $                             0.02 | 22,732
12 | 129,746 | 12,975 | 0.000 | $                             0.02 | 34,097
13 | 194,620 | 19,462 | 0.000 | $                             0.01 | 51,146
14 | 291,929 | 29,193 | 0.000 | $                             0.01 | 76,719
15 | 437,894 | 43,789 | 0.000 | $                             0.00 | 115,079
16 | 656,841 | 65,684 | 0.000 | $                             0.00 | 172,618
17 | 985,261 | 98,526 | 0.000 | $                             0.00 | 258,927
18 | 1,477,892 | 147,789 | 0.000 | $                             0.00 | 388,390
19 | 2,216,838 | 221,684 | 0.000 | $                             0.00 | 582,585
20 | 3,325,257 | 332,526 | 0.000 | $                             0.00 | 873,877

Please bear in mind the the max annual growth rates are **underestimates** because I re-target growth once a year in these calculations, when each block would be able to grow more than the prior one in practice.


## ArticMine | 2025-11-05T08:18:38+00:00
I have reviewed this and will be following up with more detailed comments. I will say that I have many very serious concerns, starting from a drastic violation of the Monero social covenant going back to the Cryptonote whitepaper. I remain strongly opposed to this proposal. 

## jeffro256 | 2025-11-05T18:00:33+00:00
I want to push back on one major misconception that I see in this proposal: you *must* attempt to predict the future of miner's decisions in a fee market if you want accurate guesses about when your transaction could be included in a block. As soon as a rational miner has to make choices about whether or not to include certain transactions in a block, either due to consensus limits, or trade-offs between block subsidy in the flex zone, you have created a complex fee market where peers with agency are competing to get into a block, all having only partial information of the situation. It doesn't matter how simple your scaling proposal could be. Peers will make moves in this market in the future which rationally should affect how you make yours. We could switch to a fixed block size of 1 MB like Bitcoin, which is simple, but they also still have fee markets. I agree that USD or other currencies shouldn't necessarily be part of the equation, but they aren't currently in the reference code, so I don't see why it was brought up.

Now about the flex zone. I would be in strong disagreement of allowing automatic exponential growth to the flex zone without the adoption there to force it up, or other forces to pull it back down. An allowed growth of 10% each year would result in at 1271x growth in the flex zone by 2100. Maybe bandwidth / compute power grows by that much in that amount of time, maybe it doesn't. I would much rather require the flex space to grow by adopters forced to burn XMR to raise that limit.

As for the powers-of-2 fee quantizing, I think that that is a bit too aggressive. It wouldn't matter much now when fees are less than 1 US cent's worth, but if/when fees are something non-trivial for real transactors, raising it by 2x could be really painful. It probably needs more research, but I would be willing to bet that slightly more granular fees allowances wouldn't hurt anonymity that much. Also since it's worth noting, the fee quantization needs to be baked into *consensus* rules, not relay rules like the rest of the fee rules. This is because if fee quantization is merely a *relay* rule, then each miner is incentivized to allow transactions with fees who aren't quantized, but which are slightly higher than a quantized fee. The transaction authors are incentivized to do this because they can get included in a block faster without paying 2x fees. So if we bake powers-of-2 fee quantization into consensus rules, then we have effectively bake in an illiquid fee market until the next hard fork.

## SamsungGalaxyPlayer | 2025-11-05T18:10:58+00:00
If people are concerned with short-term bursts of spam, an additional requirement could be added that the latest block is not more than Z% larger than the average of the last ~100 blocks, for example 10% larger.

Personally I think that this complexity provides little benefit, and it comes with the disadvantage of adding an undue delay to "legit" transaction surges.

If you're worried about the harm from spam in a short-term surge, then you probably should be for a more restrictive block size.

---

Regarding @ArticMine's comment, this simply is not a "drastic violation." If this simple method is chosen with an initial flex size of 16 MB and a growth rate of 50% per year, it's easy to see how aggressive growth plans can still be accommodated for.

---

@jeffro256 competition for block space happens in any restrictive case, right? Today in Monero, senders need to select a fee based on the current market and block conditions. I can create a transaction this second with an empty mempool, and it can fill up 10 seconds later with transactions with a higher fee multiplier.

I brought up the USD pricing primarily as a comment on setting minimum fees. Monero currently uses minimum fees. If the price of XMR is $1 million, then the minimum fee is arguably too high. Similarly, if this minimum fee is relied upon as being an economically significant deterrent against spam, then a too low XMR price in USD terms negatively tests that assumption.

This proposal basically says "we don't care what the price is, all we care about is the potential harm to nodes." And then we let the free market pick the minimum fee. For the flex space to be used, the fee must also exceed the tail emission penalty for that transaction.

Regarding the power of 2, that could be changed to a smaller value like a 10% step increase. However, I would like to note that Monero currently has fee multipliers that significantly exceed powers of two.

## SamsungGalaxyPlayer | 2025-12-02T14:49:46+00:00
Using @tevador's numbers from https://github.com/monero-project/research-lab/issues/155:

* Total available space: 10800 KB (10.8 MB)
* Free space: 5400 KB (I set this to half of the initial total space since it was unspecified, but a different % can be chosen)
* Initial flex space: 5400 KB
* Growth rate per year: 40%


year | max block size kb | tx/block | penalty min xmr/tx | penalty min usd/tx | max growth/yr gb
-- | -- | -- | -- | -- | --
0 | 10,800 | 1,080 | 0.0011 | $                             0.37 | 2,838
1 | 15,120 | 1,512 | 0.0006 | $                             0.20 | 3,974
2 | 21,168 | 2,117 | 0.0004 | $                             0.13 | 5,563
3 | 29,635 | 2,964 | 0.0002 | $                             0.08 | 7,788
4 | 41,489 | 4,149 | 0.0002 | $                             0.05 | 10,903
5 | 58,085 | 5,808 | 0.0001 | $                             0.04 | 15,265
6 | 81,319 | 8,132 | 0.0001 | $                             0.03 | 21,371
7 | 113,847 | 11,385 | 0.0001 | $                             0.02 | 29,919
8 | 159,385 | 15,939 | 0.0000 | $                             0.01 | 41,886
9 | 223,139 | 22,314 | 0.0000 | $                             0.01 | 58,641
10 | 312,395 | 31,240 | 0.0000 | $                             0.01 | 82,097
11 | 437,353 | 43,735 | 0.0000 | $                             0.00 | 114,936
12 | 612,294 | 61,229 | 0.0000 | $                             0.00 | 160,911
13 | 857,212 | 85,721 | 0.0000 | $                             0.00 | 225,275
14 | 1,200,097 | 120,010 | 0.0000 | $                             0.00 | 315,385
15 | 1,680,135 | 168,014 | 0.0000 | $                             0.00 | 441,540
16 | 2,352,190 | 235,219 | 0.0000 | $                             0.00 | 618,155
17 | 3,293,065 | 329,307 | 0.0000 | $                             0.00 | 865,418
18 | 4,610,292 | 461,029 | 0.0000 | $                             0.00 | 1,211,585
19 | 6,454,408 | 645,441 | 0.0000 | $                             0.00 | 1,696,218
20 | 9,036,172 | 903,617 | 0.0000 | $                             0.00 | 2,374,706
21 | 12,650,640 | 1,265,064 | 0.0000 | $                             0.00 | 3,324,588




## SamsungGalaxyPlayer | 2025-12-02T15:33:59+00:00
## Possible Flex Space Growth Guardrails

### Background

It's challenging to add a check to confirm _if the flex space growth is actually needed_. In a scenario where XMR is hugely valuable, it might be too expensive to use the flex space. Allowing the flex space to continue to grow will reduce the penalty per tx that the fee needs to overcome, which mitigates a potential "downward spiral" where the price continues to climb but the flex space isn't ever used, and thus doesn't grow (this is why in the original proposal, the flex space grows regardless).

We could add a check that the flex space only grows if 100% of the free space is consumed, but we should assume it will be filled with near-zero costs transactions (e.g. spam).

### Idea 1

Enforced after 100 blocks from the mechanism's implementation, require that a transaction's fee exceeds 1/4 of the median fee (per weight) for the last 100 blocks. This requirement is not enforced if any of the flex space is used. Only increase the flex space (at a per-block rate equivalent to 40% per year) if 100% of the free space of the previous block is used.

In a low competition environment, this won't do much. Probably nothing at all. The flex space will continue to grow if spam is included for free. If no one bothers to spam, then the flex space won't grow. I guess no one bothers to spam Monero today despite being able to, so maybe this is a safer assumption than I think (at least for this).

In a medium competition environment, this could reduce the risk of spam filling in the rest of the free space. If the median fee is significant enough, it will at least somewhat discourage spam.

In a high competition environment, the flex space will be used and thus this requirement is irrelevant. The flex space will continue to grow.

Somewhat counterintuitively, this would cause the flex space to increase if demand is high or low (assuming someone spams, but not if someone doesn't), but not medium.

The advantage of this method is that it still allows the free market to set the minimum fee. It's dynamic to current market conditions.

In any case, this does nothing to prevent miners from filling blocks with spam. They only pay if the flex space is used (thus causing the block reward to decrease).

I will also note that the current minimum fee mechanism in Monero does not prevent near-zero fees either. They can be bypassed by miners according to ArticMine. Spammers could work with a miner today (or be a miner themselves) to pack blocks for near free, and at no cost to the miner (and potentially a small profit to the miner).

We then require that the free space capacity be fully used to grow the flex space.

Instead of exactly 100%, we could set it to 100% minus the weight of a 1-in/2-out transaction to not penalize rounding.

### Idea 2

This builds on idea 1, but we add more conditions:

1. If the free space isn't full, then we _decrease_ the flex space by the same growth rate, to a minimum value equal to the free space (so it doesn't go to 0).
2. If the free space is full, then we _increase_ the flex space by _half_ of the growth rate (e.g. 20% annualized for a 40% max growth rate).
3. If the free space is full and at least half of the flex space is full, then we increase the flex space by the _full_ growth rate.

# Action History
- Created by: SamsungGalaxyPlayer | 2025-10-28T00:50:44+00:00
