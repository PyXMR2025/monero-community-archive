---
title: '[Vulnerability Disclosure] Post-Mortem of 10-Block-Old Decoy Selection Bug
  2023'
source_url: https://github.com/monero-project/monero/issues/8872
author: jeffro256
assignees: []
labels: []
created_at: '2023-05-23T15:11:50+00:00'
updated_at: '2023-06-06T01:07:39+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:07:38+00:00'
---

# Original Description
# Post-Mortem of 10-Block-Old Decoy Selection Bug 2023

## Quick Facts

* Severity: HIGH
* Affected versions: GUI/CLI wallet versions v0.13.0.0 to v0.18.2.1
* Impact: Loss of sender anonymity for transactions spending funds exactly 10 blocks old
* Fix: Update wallet to v0.18.2.2
* Workaround: No real decent workarounds currently

## Introduction

When the Monero wallet needs to construct a transaction with a certain input, it also picks decoys inputs from the chain based on a certain distribution called a "gamma distribution". The gamma distribution makes picking recent decoys more likely than picking older decoys, mimicking how real users spend their funds. However, in the gamma picker code, there was a off-by-one bug that didn't allow the gamma picker to pick decoys which are exactly 10 blocks old. The wallet can, however, still spend owned outputs that are exactly 10 blocks old. This means that an external observer can guess the true spend of an input ring with very high likelihood if one of the ring members is exactly 10 blocks old.

This bug has been patched in v0.18.2.2 and it is recommended that all users update their wallets as soon as possible. Since many third-party wallet applications rely on the core "wallet2" code, if you do not use the Monero Core CLI/GUI wallets, ask the development team of your wallet if they have upgraded to the new wallet2 code. Upgrading your wallet to v0.18.2.2 will not only improve your sender anonymity, but will increase the anonymity pool for all other users, including those the older vulnerable wallet code.

## Technical Explanation

### More In-Depth Background

(Large portions are text below are copied directly from @j-berman's ["Post-Mortem of Decoy Selection Bugs"](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html) in 2021)

The decoy selection algorithm is designed to select outputs from across the blockchain based on observed spending patterns, as recommended in [Moser et al](https://arxiv.org/pdf/1704.04299/). The paper's analysis uses spending patterns from earlier versions of Monero - where in some cases, the real outputs used in transactions could be deduced with certainty - in order to arrive at a distribution of Monero user spending patterns. The paper highlights that users were more likely to spend outputs received relatively quickly than they were to spend outputs held for a long time. The paper then recommends factoring in the observed spending patterns when selecting outputs from across the blockchain to use as decoys, rather than apply an equal probability to the entire set of outputs from across the blockchain. This way, newer outputs would be more likely to be selected as decoys than older outputs, thus better obfuscating which output is real in users' transactions.

When the paper's recommendation [was first implemented in Monero v0.13.0.0](https://github.com/monero-project/monero/pull/3528), the wallet correctly applied the observed spending pattern from the tip of the blockchain when selecting decoys. However, when the algorithm [was upgraded in v0.14.1.0](https://github.com/monero-project/monero/pull/5389), the algorithm applied the observed spending pattern from 10 blocks prior to the chain tip. This was done because outputs younger than 10 blocks old are locked and cannot be spent, therefore it seemed logical to apply the distribution starting 10 blocks prior to the chain tip so as to only consider spendable outputs.

### The Off-By-One Bug

Before picking decoys for a new transaction, the wallet grabs the cumulative distribution of outputs across the blocks for the entire chain using the RPC command /get_output_distrubution.bin. To prevent the gamma picker from picking decoys from blocks that are younger than ten blocks, [an "end" pointer is calculated](https://github.com/monero-project/monero/blob/35e0a968bde4644a86f6f455b1a50ca25398fa15/src/wallet/wallet2.cpp#L970) which bounds the chain information that the gamma picker considers. You can see that the calculation does not consider the last 10 blocks (the block unlock time) of chain information. However, since a newly created transactions will not enter the current highest block, but the next future block, the newest information considered at the time of transaction construction is actually 11 blocks older than the next future block (which ostensibily a new transaction will reside in).

However, wallets will still construct transactions with owned ring members that are exactly 10 blocks old. If all wallets adhere to this flawed logic, then the only time an 10-block old ring member will show up in a transaction is if it is the true spend. This heuristic would be devastating for sender anonymity with 10-block old true spends.

The bug was patched in PR [#8794](https://github.com/monero-project/monero/pull/8794).

### Emperical Analysis
![Screenshot from 2023-05-29 23-17-24](https://github.com/monero-project/monero/assets/10839482/9107463d-08b5-4f81-bb0d-a647c312c986)

The graph you see above shows how much 10-block-old ring members vs 11-block-old ring members appeared in transactions over time. The blue line represents the percent of transaction ring members on-chain that are exactly 10 blocks old over time, with yellow representing the same for 11-block-old ring members. The dashed green line shows the ratio between these two values over time. There are a few interesting patterns, but the most relevant to this analysis is the spike in 10-block old ring member usage after the v0.18.2.2 release, the first wallet release with the bug fixed, as well as the increase in ratio between these two ages. Since there is currently no way for the core dev team to track wallet version usage, there isn't any readily available data on the proportions of users using old wallets versus new wallets, information which would help establish correlation in the 10-block old ring member data. However, such a noticeable spike in the number of 10-block old ring member usage coinciding precisely when the patched release was launched suggests that this patch did statistically alter decoy selection for young ring members.

Also, thankfully, the data tells a more complex story than our worst-case heuristic scenario. There were still a lot of 10-block old ring member usage before the bug was patched, likely due to custom wallet software. This makes the deanonymization heuristic less potent than originally anticipated.

## Conclusion

Not to beat a dead horse, echoing @j-berman in his [original decoy selection bug post-motem](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html): "anyone with a background in statistics and probability theory is encouraged to join in discussions geared toward improving the algorithm." In hindsight, this bug could have been discovered if the statistical distributions had been analyzed carefully. Instead, the bug was [stumbled upon by accident](https://github.com/monero-project/monero/pull/8794#issuecomment-1478585470) while [attempting to fix an infinite while loop](https://github.com/monero-project/monero/pull/8794#issue-1633821949) during decoy selection. This brings me to a second point which I think is important but may be controversial: the wallet2 decoy selection code needs to be completely rewritten. The `wallet2::get_outs` function is [over 600 lines long](https://github.com/monero-project/monero/blob/94e67bf96bbc010241f29ada6abc89f49a81759c/src/wallet/wallet2.cpp#L8165), with few comments and inadequate testing. Seeing as how the important decoy selection is to the privacy model of Monero, the code which actually implements this functionality in most wallets is of substandard quality. There are a lot of great ongoing discussions relating to decoy selection like [non-coinbase-only selection for non-coinbase](https://github.com/monero-project/research-lab/issues/109), [coinbase consolidation transactions](https://github.com/monero-project/research-lab/issues/108), [ring binning](https://github.com/monero-project/research-lab/issues/84), [etc](https://github.com/monero-project/research-lab/issues/86). And while Monero has always been forward focused, it has also been more grounded and battle-tested as compared to other more experimental privacy-preserving coins. This only happens through the hard work and dedication of community members peering over the code and hardening it. Feel free to join the #monero-research-lab and #monero-dev channels on IRC/Matrix to participate and communicate more with existing community members. You can also join relevant [Monero Workgroups](https://www.getmonero.org/community/workgroups/). 

# Discussion History
## janowitz | 2023-05-24T07:17:00+00:00
I wonder why this disclosure has been delayed until now after a fix in form of 0.18.2.2 has been out for almost two months now and users / wallets / service providers could have been urged to update their daemon to mitigate the implying risk and prevent more transactions like this being created. Especially frequently transacting users have been affected most.

Nevertheless, it would be great if someone could run some kind of magic to find out how many transactions have been affected in total and percentage of total transactions. 0.14.1.0 has been released in July 2019, so the bug has been there for almost four years.

## j-berman | 2023-05-24T14:18:24+00:00
> I wonder why this disclosure has been delayed until now after a fix in form of 0.18.2.2 has been out for almost two months now

First, I agree this announcement shouldn't have been delayed. It should have gone out close to when the issue was discovered before the release, and definitely along with the release. This was a mistake that I bear some responsibility for that I would like to not see repeated in the future.

When I announced a similar bug in the algorithm 1.5 years back, I had some inaccuracies in my initial announcement. I corrected them quickly, but the damage of those inaccuracies was already done as they spread through the media. I continue to feel that damage to this day. Speaking for myself, I was hesitant to make a similar mistake this time around because of that experience.

The above isn't an excuse, it's just explaining what led to my personal hesitation. I could have and should have been more proactive ensuring there was clearer messaging for this issue earlier on, both so users can protect themselves, and for wallets in the ecosystem to roll out an update. I take responsibility for this mistake.

Ultimately processes for these sorts of announcements can and should be improved. In this case what would have clearly helped at the least was me making it clearer both in IRC and to members of the core team what the ramifications of this issue were straight away. Maybe it also makes sense to bring back dev meetings where people discuss PR's in flight; that might have increased the chances more people would become aware of this PR's ramifications. But, what would have been best was simply taking initiative and not hesitating to deliver the message.

Credit goes to @jeffro256 for taking initiative on this.

> it would be great if someone could run some kind of magic to find out how many transactions have been affected in total and percentage of total transactions. 0.14.1.0 has been released in July 2019, so the bug has been there for almost four years.

@jeffro256 has done this. You can see in the chart the percentage of transactions affected has a ceiling of around ~0.6% of all transactions (the dark blue line in the chart).

One additional point worth mentioning: I'm not aware of any wallets in the wild that avoided this issue, but it is theoretically possible anyone could have implemented a decoy selection algorithm that avoided it. If some unknown custom wallet software out in the wild did not have this issue (e.g. some high volume merchant), and accounted for a large number of the observed transactions with an output 10 blocks old, then the severity of this bug would be reduced. Off hand, I would say this is probably unlikely, but technically there is no way of knowing if this is the case or not.

## janowitz | 2023-05-24T16:28:04+00:00
Fair enough, I don't want to blame anyone and thanks for this honest reply, @j-berman! I can just talk from the outside, since I didn't make it to a dev / mrl meeting for the last couple of months, so I appreciate your work and this discovery even more.

However, like you said we should think about processes how certain issues should be handled. Sure, if funds are at risk you cannot disclose anything until a fix has been done, users urged (maybe for some other reason) to update and only when most of the network is up to date. Issues like this one potentially affecting users' privacy should be published much faster after a review from some other skilled people, without spreading potential misinformation which shouldn't be the case latest when the patch has been reviewed, otherwise we lose credibility.

> @jeffro256 has done this. You can see in the chart the percentage of transactions affected has a ceiling of around ~0.6% of all transactions (the dark blue line in the chart).

I've noticed it, however I have some issues with the chart. It mentions inputs, not transactions which can have and mostly(?) have several inputs. If one of those is affected, all of them are (think of a p2pool miner consolidating dozens of inputs but also an incoming tx one or change). On the other hand the chart goes back to early 2017, while 0.14.1.0 came out mid 2019. The peak in the ratio of 10/11 has been mid 2018, were those not affected and only became an issue with some decoy selection tweak?

@jeffro256 I would be very grateful if you could run your script to count the total amount of tx from when [0.14.1.0 has been released](https://github.com/monero-project/monero/releases/tag/v0.14.1.0) since from the release notes I don't see what could have caused the current issue. Also are there any rings containing two 10-block decoys? If so, wouldn't this be some kind of evidence of a custom implementation?

## j-berman | 2023-05-27T00:49:10+00:00
After more digging, this off-by-1 bug affects versions released starting from [v0.13.0.2](https://github.com/monero-project/monero/releases/tag/v0.13.0.2) [[source](https://github.com/monero-project/monero/pull/3528/files#diff-04cf14f64d2023c7f9cd7bd8e51dcb32ed400443c6a67535cb0105cfa2b62c3cR6330)].
_____

@janowitz valid response, I agree with pretty much all of your points.

> The peak in the ratio of 10/11 has been mid 2018, were those not affected and only became an issue with some decoy selection tweak?

I don't see how that peak could be affected by this bug since that was before the bug was introduced (in October 2018).

Versions prior to v0.13.0 appear to be safe because they rely on [the same logic](https://github.com/monero-project/monero/commit/1593553e03aef8d44621aaf79a33ba25f69a2bd7#diff-94841b820d7dfb0ef2f631d635c246ea152fba2cf868b62a0dc084f04e9e2f6cR2649) that matches [consensus](https://github.com/monero-project/monero/blob/f307621678c24ee7ca158fde38080d787d678733/src/cryptonote_core/blockchain.cpp#L3531-L3536) to determine which set of outputs were usable.

That peak seems like it would be a distinct investigation in its own right.

## plowsof | 2023-05-29T12:00:09+00:00
commenting here for visibility:  from @j-berman 's [comment](https://github.com/monero-project/monero-site/pull/2170#discussion_r1207538965)
>If this recommendation ends up causing people to spike pay in 11 blocks versus 10, then that in and of itself could theoretically leave another way to stick out. Like you noted in your prior sentence, since newer wallets can now select 10 block decoys, old wallets are now protected if they spend an output 10 blocks old. I think it's arguably safer not to recommend older wallet users wait 11 blocks and just recommend people update wallets asap.  

can we then delete this sentence from the disclosure:
> If you must absolutely stay behind with an older wallet version, do not ever spend funds as soon as they are unlocked; make sure to wait one extra block before sending.

## jeffro256 | 2023-05-30T04:00:08+00:00
> Also are there any rings containing two 10-block decoys? If so, wouldn't this be some kind of evidence of a custom implementation?

Yes this metric would likely be even more telling than counting raw ring members. And since inputs within transactions are more or less guaranteed to be created by the same implementation, batching the results by transaction instead of by ring member will give a more "median" look at the data where transactions where large batch transactions do not sway the results as much proportionally. Sorry I have been slow to run new results, I'll look into this soon.

## jeffro256 | 2023-05-30T04:00:57+00:00
@plowsof: updated 

## selsta | 2023-06-06T01:07:38+00:00
Since this will be added to the blog I will close this issue here.

# Action History
- Created by: jeffro256 | 2023-05-23T15:11:50+00:00
- Closed at: 2023-06-06T01:07:38+00:00
