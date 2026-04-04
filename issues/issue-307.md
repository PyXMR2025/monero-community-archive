---
title: Research meeting 25 February 2019 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/307
author: SarangNoether
assignees: []
labels: []
created_at: '2019-02-22T19:16:06+00:00'
updated_at: '2019-03-11T17:12:37+00:00'
type: issue
status: closed
closed_at: '2019-02-25T21:47:43+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 25 February 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Output selection
a. Selection algorithm
b. Requirements (if any) for coinbase

3. Other work
a. Sarang
b. Surae
c. Others?

4. Questions

5. Action items

# Discussion History
## SarangNoether | 2019-02-22T19:20:01+00:00
Output selection
---

**Introduction**
For every output spent in a transaction, the wallet chooses a ring of 10 additional decoy outputs from the chain to use in a ring signature. Originally, the wallet chose these decoys uniformly from the chain. In later versions, it chose them from a modified triangular distribution. Since it is suspected that users generally spend newer outputs more often than older outputs, the wallet should select decoys from a distribution that matches the expected spend pattern.

**Current approach**
Empirical studies on both Bitcoin and certain older Monero transactions suggest that a particular statistical distribution (call it exp-gamma) closely matches provable spend patterns. Currently, the wallet selects a block at random using exp-gamma, and then forms a small window of blocks around it; the size of the window depends on how many neighboring blocks are empty. It then selects an output uniformly from the window. This ensures that in general, newer outputs are more likely to be selected than older outputs.

**Drawbacks**
Depending on transaction volume, it is often the case that there is large variability in the number of outputs contained in blocks. At the extreme, up to 25% of blocks at any given time may be empty, containing only a coinbase output. This variability means that the selection algorithm will choose outputs from smaller (in terms of outputs) blocks with higher probability than is expected. This is apparent when a transaction occurs whose input rings might contain many coinbase outputs.

An adversary analyzing the chain may develop a heuristic stating that a coinbase output appearing in a ring is a decoy, under the (currently unproven) assumption that coinbase outputs have a different spend pattern than non-coinbase outputs. A more clever adversary might develop more advanced statistical heuristics that account for the size of the block where an output was generated.

**Goals**
We want to modify the wallet's output selection algorithm to more correctly account for variability in block sizes, while still staying true to the expected spend distributions known from empirical data. This will help to mitigate the types of analysis that could be useful to an adversary.

Outputs generated in neighboring blocks, regardless of the size of the blocks, should be selected with approximately the same probability once we account for the exp-gamma distribution. Further, outputs generated in the same block should all be selected with precisely the same probability, since these outputs have the same age.

**Selection algorithms**
Here are four options for output selection, including the current one. Each has a short name so we can refer to it easily.

1. Partial window. This is the current approach, where the size of the window around the chosen block depends on whether or not adjacent blocks are empty or non-empty.

2. Full window. This is a slight modification to partial window, where the size of the window around the chosen block is fixed according to a given parameter.

3. Output lineup. In this approach, an exp-gamma selection is made on the entire list of outputs, ignoring the structure of blocks altogether. Once an output is selected, another uniform selection is made among all outputs in the block.

4. Biased lineup. In this approach, an exp-gamma selection is made on a block. A uniform selection is then made among all outputs from the tip of the chain to twice the age of the selected block.

**Chain density**
Each of the output selection outputs is tested against several different chain densities (the distribution of the number of outputs per block).

1. Real. This uses actual Monero chain data for all post-RingCT blocks generated before 15 February 2019.

2. Geometric. This uses a geometric distribution to determine the number of outputs in each block.

3. Famine. This assumes that blocks newer than the exp-gamma mean (approximately 1.8 days) are all empty, and that older blocks are packed using a geometric distribution.

4. Feast. This assumes that blocks newer than the exp-gamma mean are all packed using a geometric distribution, and that older blocks are empty.

The last two models are extreme cases, intended to simulate different types of worst-case behaviors. The first two models are intended to simulate more typical chain conditions and transaction behavior.

**Simulation method**
Each combination of selection algorithm and chain density is simulated using a chain consisting of 500000 blocks. After generating the chain, 10000 selections are made from the same point in time at the tip of the chain; that is, we assume that the chain does not grow as we make the selections.

We initially examine only two simple metrics.

1. Mean fraction. What fraction of selection block ages are less than the exp-gamma expected mean (approximately 1.8 days)?

2. Coinbase ratio. What fraction of selections are coinbase outputs? For comparison, the fraction of coinbase outputs appearing in the entire chain (which is independent of the selection algorithm and depends only on the chain density) is also provided.

All [simulation Python code](https://github.com/SarangNoether/research-lab/tree/outputs/source-code/outputs) is available.

**Results**
The following table shows the results of the two metrics for each combination of selection algorithm and chain density.

```
density selection   mean    coinbase (chain fraction)
-----------------------------------------------------
real    partial     0.5509  0.1463 (0.0595)
        full        0.5461  0.0913
        lineup      0.5100  0.0804
        bias        0.5456  0.0746
geom    partial     0.5460  0.3166 (0.2493)
        full        0.5421  0.2767 (0.2500)
        lineup      0.5276  0.2564 (0.2496)
        bias        0.5521  0.2491 (0.2504)
famine  partial     0.5379  0.6872 (0.2502)
        full        0.5372  0.6601 (0.2500)
        lineup      0.3405  0.5114 (0.2499)
        bias        0.5289  0.6221 (0.2512)
feast   partial     0.5424  0.6279 (0.9924)
        full        0.5480  0.6052 (0.9920)
        lineup      0.7378  0.4454 (0.9919)
        bias        0.5420  0.4817 (0.9921)
```

## b-g-goodell | 2019-02-22T20:44:29+00:00
Dude, this bias method is surprisingly good! What are your thoughts, @SarangNoether? 

## SarangNoether | 2019-02-22T20:55:59+00:00
Under normal chain density conditions, switching to any of the methods does a better job at maintaining a proper ratio while respecting the expected age mean. The issue is deciding what we want to happen under extreme conditions. Under the famine density model, lineup does better than bias at the ratio, but chooses older outputs to do so. Under the feast density model, bias has a higher ratio (which is actually closer to the chain ratio) but respects the mean.

So, we ought to decide what should happen under extreme conditions. Do we want to allow for flexibility in selected output ages to keep a lower coinbase ratio? Or are we willing to assume more coinbase selections if this is what is happening on the chain?

## SamsungGalaxyPlayer | 2019-02-22T20:58:12+00:00
Adding a potentially bad idea to the discussion:

### Requiring that all rings spending coinbase outputs can only include other coinbase outputs as decoys.

Thus, wallet software will avoid coinbase outputs as decoys entirely. Very few users solo mine. The vast majority of the time, coinbase outputs in rings are assumed to be decoys with high accuracy.

When requiring all-coinbase rings if a single coinbase output is used, we certainly don't eliminate the coinbase issue. However, we still improve it significantly. It adds a needed layer of separation. There are some discussions on how to potentially require more layers of separation, but this goes down a significant rabbit hole.

I personally believe that 99%+ of users will improve their privacy by never touching coinbase outputs at all. They will be much better off using transactions even 1 layer of separation away from coinbase.

## b-g-goodell | 2019-02-22T21:08:49+00:00
We can discuss the relative benefits and costs to such a requirement; may as well include it on the agenda. This way we can get arguments for/against into the logs for later referral.

## b-g-goodell | 2019-02-22T21:14:56+00:00
> Under normal chain density conditions, switching to any of the methods does a better job at maintaining a proper ratio while respecting the expected age mean. The issue is deciding what we want to happen under extreme conditions. Under the famine density model, lineup does better than bias at the ratio, but chooses older outputs to do so. Under the feast density model, bias has a higher ratio (which is actually closer to the chain ratio) but respects the mean.
> 
> So, we ought to decide what should happen under extreme conditions. Do we want to allow for flexibility in selected output ages to keep a lower coinbase ratio? Or are we willing to assume more coinbase selections if this is what is happening on the chain?

In the famine scenario, the "ground truth" spend-time distribution driving the monero economy is getting heavier tailed and more right-skewed as transactions are being spent with longer and longer spend-times. In the feast scenario, the "ground truth" distribution is getting more left-skewed and probably less heavy tailed (although it will always remain heavy-tailed, the heaviness will drop). So I see picking older outputs during famine as a feature, not a bug, of the lineup method...

## RandomRun | 2019-02-24T00:50:53+00:00
@SamsungGalaxyPlayer, as @SarangNoether suggested, the reason that coinbase outputs are selected more often than other outputs only have to do with the way the current output selection method works in that it selects uniformly at random an output from a selected block. 

So outputs from small blocks will tend to get selected more often than the ones from bigger blocks (given that over time all blocks will tend to get selected the same number of times regardless of how many outputs they contain). If that issue is resolved and all outputs are equally likely to be selected, then there will be no reason to avoid coinbase outputs since they won't be over represented.

Notice that not all coinbase outputs are currerntly over represented, only those from small blocks will be, and so a coinbase output from a block with say 10 outputs will be less likely to be a decoy than a non-coinbase output from a block with only 5 outputs in the same ring. Assuming no other information about them. 

With the current method, if you were to segregate coinbase outputs from the rest of them, then the next thing an attacker could look to is regular outputs that appear in blocks containing the minimal number of regular outputs (only two). You would observe that those outputs are also over represented, although less so than the coinbase ones, and thus they would have a higher probability of being decoys, compared to outputs originating from bigger blocks.

Looking at it this way, it may be a more interesting metric to look at outputs that come from blocks with i outputs, let's call them type i. All type 1 outputs will be coinbase, but not conversely. Since coinbase outputs are chosen ~25% of the time as a whole (in contrast to their frequency among all other outputs of about ~7%), type 1 outputs must show an even more extreme deviation in their ring presence from their actual frequency on the blockchain. So looking for type 1 outputs in rings would give an even better heuristics to find likely decoys. 

Ideally, I think we should be looking at a table with all these values for comparison:

|  density  |  selection  |  mean  |  coinbase  |  type 1  |  type 2  |  type 3  |  ...........
-------------|---------------|----------|--------------|-----------|-----------|-----------|-----------------

I would be curious to see how the suggested methods perform against these metrics in simulations, and what the numbers are for the actual chain.

## SarangNoether | 2019-02-25T21:47:38+00:00
    [2019-02-25 11:56:41] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/307
    [2019-02-25 11:56:58] <sarang> We'll start momentarily; see agenda in topic
    [2019-02-25 11:59:15] <suraeNoether> good mooooorning mrl
    [2019-02-25 11:59:20] <sarang> Hullo all
    [2019-02-25 11:59:25] <sarang> Let's get started!
    [2019-02-25 11:59:34] <ArticMine> hi
    [2019-02-25 11:59:38] <sarang> 1. Greetings
    [2019-02-25 12:00:13] <sarang> A very talkative bunch we are today
    [2019-02-25 12:00:21] <suraeNoether>  howdy  :D
    [2019-02-25 12:00:23] <vtnerd> hello
    [2019-02-25 12:00:23] <moneromooo> Mooooo.
    [2019-02-25 12:00:46] <sarang> A particular topic I added to the agenda is 2. Output selection
    [2019-02-25 12:01:14] <sarang> I have a short writeup and some sim results on the agenda issue: https://github.com/monero-project/meta/issues/307#issuecomment-466514757
    [2019-02-25 12:01:37] <sarang> The problem is that our current algo overselects outputs from small blocks
    [2019-02-25 12:01:40] <suraeNoether> Sarang and I last week in person nailed down some distributional stuff for output selection and coded up a few different ways of assessing the results.
    [2019-02-25 12:02:08] <sarang> You'll see 4 different algos tested, each for 4 different chain output density scenarios
    [2019-02-25 12:02:26] <suraeNoether> each of these scenarios represents a different plausible situation our economy could undergo
    [2019-02-25 12:02:35] → MalMen_ joined (~malmen@176.79.85.91)
    [2019-02-25 12:02:40] <suraeNoether> a feast scenario is one in which we get popular, a famine scenario is one in which monero usage drops
    [2019-02-25 12:02:53] <sarang> Under normal chain conditions, each of the 3 alternatives (the fourth is the current method) does a better job than what we have now
    [2019-02-25 12:02:56] <sgp_> o/
    [2019-02-25 12:02:59] <sarang> Under extreme conditions, there are tradeoffs
    [2019-02-25 12:03:06] <sarang> Here is what I want to know from this group:
    [2019-02-25 12:03:24] <sarang> if the chain density hits a low point, what should selection do?
    [2019-02-25 12:04:09] <sarang> If it stays true to chain condition, we'll overselect (for example) coinbase... but if we skew to older outputs, we maintain a better weighted ratio
    [2019-02-25 12:04:38] <suraeNoether> so, here is my thinking
    [2019-02-25 12:04:57] <suraeNoether> if chain density is dropping, then spend-times are getting longer and longer
    [2019-02-25 12:05:02] ⇐ MalMen quit (~malmen@dsl-85-91.bl27.telepac.pt): Ping timeout: 245 seconds
    [2019-02-25 12:05:05] <sarang> yep
    [2019-02-25 12:05:05] * MalMen_ → MalMen
    [2019-02-25 12:05:08] <suraeNoether> that's economicalliy a depression
    [2019-02-25 12:05:25] <suraeNoether> so the average age of ring members should also increase to reflect the "true" spend-time distribution
    [2019-02-25 12:05:30] → OsrsNeedsF2P joined (~OsrsNeeds@2607:fea8:95e0:963::5)
    [2019-02-25 12:05:51] <suraeNoether> on the other hand, during a feast scenario, the opposite is happening
    [2019-02-25 12:06:54] <sarang> Based on that, the output-lineup algo does a better job
    [2019-02-25 12:06:57] <suraeNoether> in that regard, it seems like the lineup method performs better htan others
    [2019-02-25 12:06:58] <suraeNoether> yep
    [2019-02-25 12:07:08] <sarang> under those extreme densities, it skews the ages
    [2019-02-25 12:07:15] <suraeNoether> btw i look at geometric as a flavor of the famine scenario
    [2019-02-25 12:07:22] <suraeNoether> oh wait, feast i mean
    [2019-02-25 12:07:45] <sarang> Geometric was intended as a 0-order approximation of real conditions; it's not very good but it's something to use for comparison
    [2019-02-25 12:08:18] <suraeNoether> in addition to comparing these different sampling methods, a method of directly estimating our true spend-time distribution occurred to me last night, and i'm writing it up now
    [2019-02-25 12:08:20] <sarang> Does anyone else have any thoughts on these?
    [2019-02-25 12:08:50] <sarang> RandomRun made a good suggestion for a more general set of quantities to test, that I'll write up and add to the table
    [2019-02-25 12:08:56] <moneromooo> Did you try the gamma * num-outs-per-block combo ?
    [2019-02-25 12:08:57] <sarang> (see their comment on the issue)
    [2019-02-25 12:09:21] <sarang> suraeNoether worked up a version of that but was not happy with its outcome
    [2019-02-25 12:09:41] <suraeNoether> moneromooo: the lineup and bias methods are designed to estimate that method moneromooo since computing it directly runs into certain numerical problems
    [2019-02-25 12:09:52] <ArticMine> If I understand correctly chain density is a measure of velocity
    [2019-02-25 12:09:54] → p0nziph0ne joined (p0nziph0ne@gateway/vpn/privateinternetaccess/p0nziph0ne)
    [2019-02-25 12:10:05] <sarang> chain density = distribution of number of outputs per block
    [2019-02-25 12:11:07] <sarang> I don't know how much this applies to velocity if amounts and destinations cannot be known
    [2019-02-25 12:11:20] <ArticMine> Which given a fixed money supply is a measure of velocity.
    [2019-02-25 12:11:40] <sarang> ok
    [2019-02-25 12:11:50] <suraeNoether> ArticMine: yes, although the specific interpretation of velocity is tricky in this context
    [2019-02-25 12:11:53] <sarang> Does this lead you to conclusions about how the selection should behave?
    [2019-02-25 12:12:13] <ArticMine> It relates it to market conditions
    [2019-02-25 12:12:44] <suraeNoether> yes
    [2019-02-25 12:12:52] <ArticMine> and also block weight
    [2019-02-25 12:13:00] <suraeNoether> a long spend-time distribution is a recession. a short spend-time distribution is a boom.
    [2019-02-25 12:14:23] <sarang> Unless the results from RandomRun's suggestion indicate otherwise, I'll recommend moving to the output-lineup algorithm at an upcoming release
    [2019-02-25 12:17:07] <suraeNoether> I'm also going to mess around with sampling methods, but I'm not expecting to get something that appears to perform better than the lineup method before the next fork
    [2019-02-25 12:17:13] <sarang> OK, moving on for now... related to this, from time to time there have been suggestions of whether to treat coinbase outputs differently for the purposes of decoy selection
    [2019-02-25 12:17:14] <ArticMine> My question is outliers in the spends
    [2019-02-25 12:17:22] <sarang> ArticMine: in what way
    [2019-02-25 12:18:08] <ArticMine> Namely spend that are very different from the norm at a given point in time
    [2019-02-25 12:18:34] <suraeNoether> articmine: this is the classic(tm) problem with spend-time distributions
    [2019-02-25 12:18:35] <sarang> Selecting from the best known distribution is intended to account for this as much as is reasonable
    [2019-02-25 12:19:02] <sarang> Of course, multiple rings spending outliers from the same point in time are problematic for different reasons
    [2019-02-25 12:19:29] <sarang> Any, back to the previous statement I made about coinbase outputs...
    [2019-02-25 12:19:46] <sarang> It is probable that they are spent with a different distribution that is (as of now) not tested
    [2019-02-25 12:19:57] <sarang> I don't support treating them differently
    [2019-02-25 12:20:12] <sarang> But I thought that I would mention it in the context of output selection anyway
    [2019-02-25 12:20:52] <sarang> Using a properly weighted selection algorithm will reduce their occurrence in rings as a consequence, which seems reasonable to me
    [2019-02-25 12:21:13] <ArticMine> but not their elimination
    [2019-02-25 12:21:23] <sarang> No, of course not
    [2019-02-25 12:21:27] <ArticMine> good
    [2019-02-25 12:21:48] <sarang> With the proposed algo change, their selection will be reduced toward the fraction of their occurrence on the chain
    [2019-02-25 12:22:08] <sarang> and will do the same for all outputs based on how dense their blocks are, of course
    [2019-02-25 12:22:32] <sarang> Anyway, please comment after the meeting or on the GitHub agenda issue with any other thoughts on output selection
    [2019-02-25 12:22:35] <suraeNoether> i don't support treating coinbase differently because then the next question is whether we should treat rings with ring members that come from coinbase transactions differently. and so on; the natural conclusion is to ensure transaction trees are sort of homogeneous in their depth and stuff, and that partitions the entire space way too much. it's an over-optimization with dubious benefits, imo
    [2019-02-25 12:22:37] <sgp_> It's my opinion that coinbase outputs will never be spent in the incredible vast majority of transactions of normal users. A heuristic to eliminate the coinbase has high accuracy for anyone not suspected of mining
    [2019-02-25 12:23:01] <suraeNoether> sgp_: high sensitivity but awful specificity
    [2019-02-25 12:23:06] <sarang> ^
    [2019-02-25 12:23:09] <sgp_> Under normal Monero network conditions, over 75% of the hashrate is allocated to public pools. These are all transparent
    [2019-02-25 12:23:55] <ArticMine> Who then promptly spend the coinbase
    [2019-02-25 12:24:10] <sgp_> yes, and it's clear which transactions spend the coinbase too
    [2019-02-25 12:24:18] <sgp_> so these outputs are effectively dead
    [2019-02-25 12:24:28] <sarang> Like I said, there is probably a different spend pattern that would be interesting to examine, both in Bitcoin and in our older discernible spends
    [2019-02-25 12:24:44] <sarang> and of course the pool issue that sgp_ mentions
    [2019-02-25 12:25:08] <sarang> Requiring a mix of coinbase-only in rings moves the problem up one level in the txn graph
    [2019-02-25 12:25:29] <suraeNoether> sgp_: protecting coinbase transactions when miners can merely churn for almost no fees is not super rational. there will always be some effectively dead outputs. i'm much more concened about the privacy problems induced b y multiple-input trnasactions that are all spending inputs from similar time periods.
    [2019-02-25 12:25:30] <sgp_> yes, that one level doesn't eliminate the problem, but it makes it much better than it is today
    [2019-02-25 12:25:46] <suraeNoether> sgp_: i don't think that's been quantified, though
    [2019-02-25 12:25:56] <ArticMine> Yes but overall there is merit to including coinbase because of outliers
    [2019-02-25 12:26:06] <ArticMine> among coinbase
    [2019-02-25 12:26:08] <sgp_> suraeNoether: I argue against protecting coinbase outputs. I want to call them all essentially transparent
    [2019-02-25 12:26:17] <suraeNoether> sgp_: ah, i'm okay with that
    [2019-02-25 12:26:27] <suraeNoether> sgp_: hmm wait
    [2019-02-25 12:26:30] <sgp_> Since in most cases, the vast majority are already
    [2019-02-25 12:26:31] <suraeNoether> sgp_: let me think about that
    [2019-02-25 12:27:09] <ArticMine> I am not so sure. In most but not all cases
    [2019-02-25 12:27:14] <sgp_> Public pools don't care since they make the info transparent anyway. We don't need to "protect" them
    [2019-02-25 12:27:15] <suraeNoether> sgp_: i disagree that they are essentially transparent
    [2019-02-25 12:27:32] <sgp_> suraeNoether: why, because it's a pool-reported heuristic?
    [2019-02-25 12:27:50] <suraeNoether> no no; i mean i disagree that coinbase transactions are essentially transparent despite the public information posted by pools
    [2019-02-25 12:28:03] <suraeNoether> i can still manage to spend coinbase transactions with a high degree of plausible deniability
    [2019-02-25 12:28:05] <sarang> If their payout txns are reported...
    [2019-02-25 12:28:24] <sgp_> Perhaps it's more accurate for me to say: we know exactly what transactions these coinbase outputs are spent in
    [2019-02-25 12:28:32] <sgp_> Which pronounces them dead in other transactions
    [2019-02-25 12:28:37] <sgp_> known decoys
    [2019-02-25 12:28:51] <suraeNoether> yes; i thought you were tr ying to apply the blanket term to *all* coinbase transactions. #notallcoinbases
    [2019-02-25 12:29:11] <sgp_> no, only public pool transactions spending coinbase outputs
    [2019-02-25 12:29:34] <suraeNoether> o kay, so is *anyone* in favor of treating coinbase transactions differently?
    [2019-02-25 12:29:48] <sarang> To sum up: sgp_ had previously advocated for a default/rule that a ring with a coinbase must contain only coinbase
    [2019-02-25 12:29:56] <ArticMine> It comes down to the outliers issue. Not all coinbase outputs are dead. With a ring size of 11 we can afford to spend 1 ring on this
    [2019-02-25 12:30:33] <ArticMine> If the ring size were say 3 I would support sgp_s position
    [2019-02-25 12:30:36] <moneromooo> If you want to avoid pool coinbase outs as fake outs, use a blackball list with them.
    [2019-02-25 12:30:41] <sgp_> ArticMine: in my opinion, the cost of wasting 1 ouptput per tx is worse than the harm' to solo miners if we avoid coinbase outputs entirely
    [2019-02-25 12:31:09] <sgp_> moneromooo: we want to avoid interactivity. That's really cumbersome to expect of users, and it allows for pool fuckery if they report bad info to wallet clients
    [2019-02-25 12:31:34] <sarang> I assume moneromooo meant a blackball list with sources chosen by the user
    [2019-02-25 12:31:41] <moneromooo> People don't have to do anything. They only do anything if they want to avoid those outputs.
    [2019-02-25 12:31:42] <sarang> not some global version that can be DoS
    [2019-02-25 12:31:44] <ArticMine> But you agree tat the issue is way less wit ring 11 tan say ring 3
    [2019-02-25 12:32:03] <sgp_> ArticMine: yes, a larger ringsize mitigates these issues
    [2019-02-25 12:32:29] <sarang> I think that the idea of coinbase-only rings deserves more careful analysis to numerically examine the benefits and chain costs
    [2019-02-25 12:32:30] <sgp_> But I still advocate for this at any feasible ringsize
    [2019-02-25 12:32:34] <moneromooo> If it was automated and everyone was magically using that system, non pool miners would be spenidng at effective mixin 0.
    [2019-02-25 12:32:47] <sgp_> moneromooo: yes
    [2019-02-25 12:33:20] <sgp_> problem is unless we avoid the coinbase outputs, wallets will select this "0-mixin" outputs in their rings
    [2019-02-25 12:33:28] <sarang> I recommend we table this in the absence of any numerical evidence
    [2019-02-25 12:33:36] <sarang> but that we obtain this evidence if it exists
    [2019-02-25 12:33:52] <ArticMine> I agree
    [2019-02-25 12:34:11] <sarang> And we can discuss after the meeting (but I wish to respect our 1-hour goal and others' time)
    [2019-02-25 12:34:16] <sarang> On to 3. Other work
    [2019-02-25 12:34:18] <sgp_> I understand your point of view sarang, but the main concept isn't very difficult. You see x% of public pools which also mine and make transparent x% of new coinbase outputs
    [2019-02-25 12:34:33] <sgp_> but we can move on sure
    [2019-02-25 12:35:03] <sarang> I have been working on output selection, finalizing data on block size algos, gave a talk in Nashville to a meetup
    [2019-02-25 12:35:21] <sarang> One meta-item: the Loki Foundation wishes to fund me and/or suraeNoether in part for the next funding round
    [2019-02-25 12:35:29] <sarang> but it comes with a contract
    [2019-02-25 12:35:38] <endogenic> sarang's talk: https://www.youtube.com/watch?v=H8ijX02J7Y0
    [2019-02-25 12:35:48] <endogenic> surae's talk: https://www.youtube.com/watch?v=9srtIk9M2yg
    [2019-02-25 12:35:53] <sarang> I'm hesitant because I'm sure the contract terms could be abused if they were out for PR or other ends
    [2019-02-25 12:36:17] <sarang> I am going to request that the contract terms be made public, since I am not a lawyer
    [2019-02-25 12:36:20] <suraeNoether> i think that's true of any contract
    [2019-02-25 12:36:25] <moneromooo> I don't remember them as PR whores fwiw.
    [2019-02-25 12:36:29] <sarang> cool
    [2019-02-25 12:36:34] <moneromooo> I didn't exactly look for it though.
    [2019-02-25 12:36:39] <suraeNoether> however, i think we could propose amendments re: anticipated problems
    [2019-02-25 12:36:40] <sarang> I'm trying to maintain healthy skepticism while appreciating their offer
    [2019-02-25 12:37:00] <sarang> Yeah. If we can publish the contract and there are no serious objections, it reduces the community funding burden while not changing our research goals
    [2019-02-25 12:37:13] <ArticMine> Making te contract public is a reasonable approach
    [2019-02-25 12:37:17] <sarang> the total would be 15K USD, split between 1 or 2 people
    [2019-02-25 12:37:26] <endogenic> i'd suggest consulting with a lawyer about assignment of IP, non disclosure, requirements to execute things for them, etc
    [2019-02-25 12:37:44] <sarang> Yeah, they specifically don't take ownership of any research product
    [2019-02-25 12:37:49] <ArticMine> Assignment of IP?
    [2019-02-25 12:37:52] <endogenic> as mentioned when a contract is couched in consulting language they can say they had expectations of certain things
    [2019-02-25 12:37:54] <moneromooo> One fairly easy way to prevent most of that is to say "sarang can stop this contract at any time, and the pro rata is due".
    [2019-02-25 12:37:54] <sarang> but do state that if they share confidential info with researchers, it can't be discussed
    [2019-02-25 12:37:57] ⇐ adhux0x0f0x3f quit (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f): Remote host closed the connection
    [2019-02-25 12:38:15] <sarang> So if they knew about some kind of bug, they could disclose under the contract's NDA clause
    [2019-02-25 12:38:19] <moneromooo> That is a massive no.
    [2019-02-25 12:38:40] <moneromooo> It allows them to control what you can do open source.
    [2019-02-25 12:38:47] <sarang> that's my fear
    [2019-02-25 12:38:59] <sarang> If they'll alter or remove that, it takes away most of my concern
    [2019-02-25 12:39:14] <sarang> I'll discuss with them and get the contract posted publicly
    [2019-02-25 12:39:19] <moneromooo> If they know of a bug, htey can use H1.
    [2019-02-25 12:39:22] <sarang> exactly
    [2019-02-25 12:39:30] <sarang> I wonder if it's for a bug in _their_ software
    [2019-02-25 12:39:38] <sarang> but anyway
    [2019-02-25 12:39:56] <sarang> This week, I'll be finishing up additional output selection tests, doing some lit review backlog, bulletproofs MPC, etc.
    [2019-02-25 12:39:59] <sarang> How about suraeNoether ?
    [2019-02-25 12:40:37] <suraeNoether> Sarang and I have a deadline of March 1 for this paper we are writing; it was previously Feb 18 but it has moved. I'm finishin g up three proofs of security for that paper, and I  believe we will be making the details public soon.
    [2019-02-25 12:40:53] <suraeNoether> sarang: have we talked with our co-authors about when we can talk about this?
    [2019-02-25 12:40:57] <sarang> Ah yes, I forgot to mention that
    [2019-02-25 12:41:07] <sarang> Once it's submitted I'm sure they'll post to IACR
    [2019-02-25 12:41:34] <suraeNoether> this paper we think is rather competitive, it's proposing something novel with immediate applicability, so it should be a shoe-in for publication.
    [2019-02-25 12:41:50] <koracain> loki... wait jeff's project? oh lol that's a safe bet
    [2019-02-25 12:41:50] <sarang> Yep! Relates to the DLSAG construction but with much more on applications
    [2019-02-25 12:41:53] <suraeNoether> in addition to that, i'm simulating blockchain stuff for the matching paper to try to get that out the door
    [2019-02-25 12:42:14] <suraeNoether> i actually have a quiet week of writing for once, which is nice
    [2019-02-25 12:42:24] <suraeNoether> konferenco stuff will have some more announcmeents later this week
    [2019-02-25 12:42:36] <suraeNoether> if anyone wishes to submit an abstract to come speak, please drop one on us at https://konferenco.xyz
    [2019-02-25 12:42:58] <suraeNoether> we are working to accommodate speaker travel costs, too
    [2019-02-25 12:43:42] <suraeNoether> oh, and before I forget: the scholarship applications at MAGIC are now live, so anyone in the US, EU, or ZA who want a small scholarship to mitigate the costs of their books or whatever, swing on by https://magicgrants.org
    [2019-02-25 12:44:07] <suraeNoether> and i think that's it!
    [2019-02-25 12:44:17] ⇐ p0nziph0ne quit (p0nziph0ne@gateway/vpn/privateinternetaccess/p0nziph0ne): Remote host closed the connection
    [2019-02-25 12:44:29] <endogenic> thanks as always guys
    [2019-02-25 12:44:45] <sarang> koracain: you personally believe accepting Loki funding is a good bet? Or sarcasm?
    [2019-02-25 12:44:49] <endogenic> you're both rockstars..
    [2019-02-25 12:44:57] <sarang> Also: any other work for anyone to report?
    [2019-02-25 12:44:58] <koracain> i know one of their devs
    [2019-02-25 12:45:07] <sarang> cool
    [2019-02-25 12:45:08] → p0nziph0ne joined (p0nziph0ne@gateway/vpn/privateinternetaccess/p0nziph0ne)
    [2019-02-25 12:45:18] <suraeNoether> oh yeah, the most interesting part of these research meetings, to me, is the folks who aren't sarang and i
    [2019-02-25 12:45:19] <sarang> Their foundation is a legally-established foundation in Australia
    [2019-02-25 12:45:37] <moneromooo> From experience, knowing a dev at one company does not mean you know what the boss will do when possible.
    [2019-02-25 12:45:44] <suraeNoether> i'm interested in how wallet dev is coming from endogenic, i'm interested in what hyc has been working on with moneroR, i want to hear from isthmus but he's usually in meetings around now
    [2019-02-25 12:45:44] <koracain> he's legit i havn't looked very hard at the project but yah lol he'd probably blow them up if they broke monero
    [2019-02-25 12:46:19] <sarang> FWIW foundation funding wouldn't change our research goals or agenda in any way
    [2019-02-25 12:46:28] <sarang> They require monthly reports, but we already do that
    [2019-02-25 12:46:53] <sarang> I'm optimistic that they just want to support Monero research since it would also benefit their project
    [2019-02-25 12:46:59] <endogenic> also when Samsung Noether
    [2019-02-25 12:47:04] <sarang> heh
    [2019-02-25 12:47:15] <sarang> that falls under 5. Questions
    [2019-02-25 12:47:30] <endogenic> :P
    [2019-02-25 12:47:39] <koracain> look hard at it but jeff is in the i2p channels on here via a relay bot
    [2019-02-25 12:47:40] <sarang> My question for moneromooo et al: when do non-consensus decisions like output selection need to be in place for an upcoming release?
    [2019-02-25 12:48:40] <moneromooo> If it's the output lining thing, I can have it done pretty quick given it's very similar to what we already have.
    [2019-02-25 12:49:11] <sarang> What is the expected timeline for a point release after the network upgrade?
    [2019-02-25 12:49:14] <sarang> A month? Two?
    [2019-02-25 12:49:33] <moneromooo> I don't think anything was even really talked about yet.
    [2019-02-25 12:49:38] <sarang> ok, wasn't sure
    [2019-02-25 12:49:39] <moneromooo> But that sounds plausible.
    [2019-02-25 12:50:05] <sarang> Well, at least the algorithm is coded up in Python already (link in agenda writeup)
    [2019-02-25 12:50:15] <sarang> so anyone can play around or test them
    [2019-02-25 12:50:39] <sarang> Real chain data is included (thanks to moneromooo for pulling that)
    [2019-02-25 12:50:57] <sarang> Other questions before we wrap up and return to informal discussion?
    [2019-02-25 12:52:05] <sarang> Righto!
    [2019-02-25 12:52:09] <sarang> 6. Action items
    [2019-02-25 12:52:30] <sarang> I will complete additional output selection testing and consider the possibilities for coinbase more thoroughly
    [2019-02-25 12:52:54] <sarang> as well as get the Loki contract squared away and the other items I listed above
    [2019-02-25 12:52:58] <sarang> suraeNoether?
    [2019-02-25 12:53:36] <sarang> Ah, and an urgent call for translations was just made: https://www.reddit.com/r/Monero/comments/auo078/urgentcall_for_translators_we_have_two_days_to/
    [2019-02-25 12:55:31] <sarang> Quiet times... well, thanks to everyone for joining. We'll formally adjourn now, but feel free to continue any discussions about previous topics. I'll post logs on the GitHub issue later today

## binaryFate | 2019-03-11T15:54:44+00:00
> 3. Output lineup. In this approach, an exp-gamma selection is made on the entire list of outputs, ignoring the structure of blocks altogether. Once an output is selected, another uniform selection is made among all outputs in the block.

Because of the second part "Once an output is selected, another uniform selection..." I do not understand how you are not again skewing towards outputs that are few in their block. An output in a single-output block right next to outputs in a 100-outputs block has 100x more chance to be selected than them.

Probably I am missing something obvious, because this seems contrary to your stated goals?

> 4. Biased lineup. In this approach, an exp-gamma selection is made on a block. A uniform selection is then made among all outputs from the tip of the chain to twice the age of the selected block.

I am worried this will result in a practical decoy distribution significantly different from the exp-gamma, far from the actual spend distribution. Given the metrics used here, the only thing we can check is that roughly 50% of the selected decoy fall before/after 1.8 days. But maybe the distribution makes no sense besides still having a proper median. 
In other words, I am worried you focus here on the local issue of outputs having a different likelihood depending on the size of the blocks, but on a global scale you may mess up the overall distribution being used.

## SarangNoether | 2019-03-11T16:00:13+00:00
The uniform selection is made only among outputs in the same block as the selected output. If the exp-gamma selection chooses an output that is alone in its block, the uniform selection has no effect.

The use of a modified output-based selection algorithm certainly implies some skew from the "ideal" exp-gamma distribution, for sure. This is why we must weigh the benefits (e.g. proper weighting by output density) against any risks (e.g. moving away from an expected spend distribution).

## binaryFate | 2019-03-11T16:09:23+00:00
> The uniform selection is made only among outputs in the same block as the selected output. If the exp-gamma selection chooses an output that is alone in its block, the uniform selection has no effect.

I see, thanks.

> The use of a modified output-based selection algorithm certainly implies some skew from the "ideal" exp-gamma distribution, for sure. This is why we must weigh the benefits (e.g. proper weighting by output density) against any risks (e.g. moving away from an expected spend distribution).

The proposals being discussed mostly make a difference at a "granular" level, looking at likelihood of blocks and outputs adjacent to one another; having likely a negligible effect on the overall distribution. Proposal 4. seems to be in a different league though so it would be interesting to check.

## SarangNoether | 2019-03-11T16:51:53+00:00
I personally support option 3 (output lineup).

## binaryFate | 2019-03-11T17:02:54+00:00
Can you confirm that option 3. here is picking based on output time (and not their index)? And that the second step, uniform distribution over the others of the block, is to deal with all outputs in a block having the same time?

## SarangNoether | 2019-03-11T17:12:37+00:00
It derives an average output time from the entire chain (but could do so from a more limited scope) and uses that for the exp-gamma selection. And yes, the uniform selection accounts for all outputs in a block having the same age.

# Action History
- Created by: SarangNoether | 2019-02-22T19:16:06+00:00
- Closed at: 2019-02-25T21:47:43+00:00
