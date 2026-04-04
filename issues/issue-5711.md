---
title: High-precision fees leak information [discussion]
source_url: https://github.com/monero-project/monero/issues/5711
author: Mitchellpkt
assignees: []
labels: []
created_at: '2019-07-01T03:57:25+00:00'
updated_at: '2021-09-18T15:36:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero's reference wallet offers the user four priority levels, then calculates the dynamic fee based on transaction weight and blockchain conditions. Users of the core software thus provide a large anonymity pool for each other. Unfortunately, a minority of transactions are generated using custom software whose non-standard fee selection algorithms causes them to stand out from the crowd. 

Currently, there are four separate anonymity pools
-  Correct (reference) dynamic fee algorithm (calc'd from {1,2,3,4})
-  Fixed absolute fee (e.g. 0.002 XMR)
-  Fixed fee per weight (e.g. 0.01 XMR / kB)
-  Outliers to above 3 sets 

![https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/fees_high_precision.png](https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/fees_high_precision.png)

The community should consider/discuss ways to limit information leakage. One class of possible solutions focuses on lowering fee resolution, for example a consensus rule that requires fees to be an integer power of two:

![https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/fees_binned.png](https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/fees_binned.png)

We could choose a more coarse or more granular filter, or even limit decimal expression to a single figure. Lots of different ways to approach this... High level, the idea should be to limit fingerprinting ability while maintaining a dynamic fee market with multiple priority levels.

What are your thoughts?

(More information available at [k2019.noncesense.org](http://k2019.noncesense.org) and during [Visualizing Monero (6:45)](https://youtu.be/XIrqyxU3k5Q?t=405) talk)

# Discussion History
## SamsungGalaxyPlayer | 2019-07-01T14:16:16+00:00
A coarse filter seems appropriate to me. I have no particular opinion on the specific implementation.

## iamsmooth | 2019-07-01T21:42:31+00:00
Well the 'fee sniping' aspect is pretty harmful to block because it encourages wallets, large transactors, or just the cost-sensitive to make direct deals with miners which both encourages centralization and probably hurts privacy in other off-chain ways (dealing directly with miners likely means the miners will gain more information about the transactions and/or users; there are likely ways to avoid this, but you can't really count on individual parties, wallet devs, etc. using them). The incentive to circumvent is pretty high here.

Probably the better solution is for the reference software to use a more economically sensible method of bidding than the very course 'levels' (which is economically irrational from an individuals perspective and invites 'sniping' in the middle).

The other random fee levels which appear to defy sensible explanation could potentially have good technical solutions, like at least rejecting relay of transactions implausibly-far from the current fee market (similar to the idea on ring members). If there isn't a good economic rationale for them, and there doesn't appear to be, incentive to bypass seems low.



## iamsmooth | 2019-07-01T21:55:09+00:00
Upon further consideration, bypassing the public fee market leaves even on-chain traces. Transactions which are mined sooner than their public fees would justify either show evidence of off-chain payment, or it might be the miner's own transaction making the fee irrelevant, both of which create distinct identifiable subsets. The latter issue can't really be addressed, but former issue implies reducing incentives to bypass.

## SamsungGalaxyPlayer | 2019-07-03T13:58:33+00:00
I'm struggling to see exactly how reduced incentives could really help here. Monero's fees are already so small that it's unlikely most people have a strong reason to talk directly with miners. Nevertheless, this off-chain communication is unavoidable, and until we come to a scenario when this is a wide issue, I'm worried we will let these risks outweigh the risks of exposed actual, evidenced, on-chain transactions. I would nevertheless like to hear more about how you envision reducing these bypass incentives.

## iamsmooth | 2019-07-04T10:55:09+00:00
@SamsungGalaxyPlayer You reduce the bypass incentives by not putting unnecessarily extreme restrictions on the allowable fees. IIRC the current granularity between priority levels is something like 4x (not 100% sure as I didn't follow the last round of changes that closely). In the talk it was briefly recommended to use 2x, which is slightly better, but not all that much.

It is not surprising, therefore, that we see people ignoring or bypassing the 'standard' fee levels in favor of only making a slight increment over the lower level (this is evident in the data presented in the talk). Rather than paying 4x as much, you get the same benefit by paying, say 1% or 5% more. This is happening, even though, as you say, the fees seem quite small to us both in absolute terms. Nevertheless the world is diverse and people have different perspectives on what is worth optimizing. Clearly, from the data, there are people who think it is worthwhile.

The alternative is to make the increments between the fee levels much smaller so there is less incentive to bypass the 'standard' levels, and then make the standard wallet also use smaller increments for priority (bear in mind that the standard wallet already has a feature to automatically elevate fees, but it elevates them by an unreasonable amount). Once the standard wallet is doing it, there is nothing non-standard or privacy-breaking about other people doing it.

This is a situation where the best solution is to adopt an "if you can't beat them, join them mentality" and not try to place unenforceable restrictions on the fee market which have other negative unintended consequences.

Again, this differs entirely from the largely nonsensical (yet sometimes seen) fees described in the talk which are completely outside the range of competitive fees that such a standard wallet would ever use, and I am fully in support of discouraging with technical measures (at least relay blocking, if not in-block consensus rules)

> until we come to a scenario when this is a wide issue

Sorry, I don't agree with this approach at all. 

First of all, it (as with my objection to the ongoing anti-ASIC war) implies a hands-on approach of continued forking which inevitably centralizes the protocol. Five years in, it is long past time to at least try to deploy a protocol that isn't flawed-by-design and can be left alone without known long-term failure modes. I know we are not there yet, we should at least be moving in that direction and not the opposite direction.

Second, in some ways by the time this starts happening (and is clearly identified, as some of the agreements are likely to be secret or at least not explicitly publicized), some of the damage is already done. It favors the larger miners (making deals with smaller ones is too much trouble) and once people start making these deals with miners, it changes the ecosystem where not only the miners but those making the deals with them become invested in the status quo in a very direct commercial manner, and will oppose changing it.

I recognize the problem that is trying to be solved here but I disagree that quantized fees (at least if done coarsely) is a good solution.

There may be some other approaches that involve burning some fees (which makes even more sense given Monero's infinite tail reward since this does not necessarily imply aggressively deflating the currency), since burning fees can't be bypassed (the block reward penalty relies on this too), but I don't have a specific proposal to make on it at this point.

## iamsmooth | 2019-07-05T01:25:55+00:00
Oh, I forgot to mention that another concept I had in mind when it comes to reducing bypass incentives is to modify the dynamic blocksize system so that it avoids short term scarcity. An example of this is vitalik's proposal here https://github.com/zcash/zcash/issues/3473 (I'm not endorsing this specific proposal, just offering it an example). In this model, the blocksize dynamically adjusts so that blocks are usually about half full, meaning there is little short term scarcity and little reason to want to outbid. You can just pay the standard fee and get into a block relatively soon under almost all conditions. Although I don't think it was intended as a privacy improvement, it has that as a side effect (as a disadvantage, this scheme seems to offer no protection against runaway blockchain growth).

There are a few other alternative fee market proposals (if I come across links I will drop them here or anyone else is welcome to) from academics recently which might be useful here, in that they attempt to mitigate short term fee fluctuations. So again while not intended there may be a privacy side benefit.

## SamsungGalaxyPlayer | 2019-07-05T15:51:02+00:00
@iamsmooth thanks for the explanation. I still think that this proposal makes sense, but I also think smaller fee increments make sense too to reduce the risk of side-channel fees to miners.

## crazyguy42781 | 2021-09-18T15:36:18+00:00
I understand the normal fees that are already set, but what about setting a flat fee per transaction, doesn't matter the size.  It would be harder to trace back cause all fees would be the same whether sending a small amount or large amount. 

# Action History
- Created by: Mitchellpkt | 2019-07-01T03:57:25+00:00
