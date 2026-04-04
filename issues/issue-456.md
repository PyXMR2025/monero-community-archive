---
title: 'Research meeting: 22 April 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/456
author: SarangNoether
assignees: []
labels: []
created_at: '2020-04-22T14:36:16+00:00'
updated_at: '2020-04-22T18:16:22+00:00'
type: issue
status: closed
closed_at: '2020-04-22T18:16:21+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 22 April 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-04-22T16:22:28+00:00
# Impacts of exchange rate volatility for Monero ecosystem contributors

Just completed a study quantifying the impact of exchange rate volatility for Monero-denominated delayed payouts. ([Twitter thread](https://twitter.com/Mitchellpkt0/status/1252720219644063745), [code](https://github.com/Mitchellpkt/volatility_analysis/blob/master/volatility_analysis.ipynb))

## Motivation

At the time of writing, most contributors need to pay their regular rent/tuition/food/etc bills in fiat currency. Exchange rate volatility resulting in loss of monero's buying power effectively reduces contributor compensation. To protect against this, proposals often include a volatility buffer. Rather than relying on gut intuition or short term market trends, this notebook analyzes exchange rate volatility over the last few years to suggest a statistically-appropriate buffer.

**This method utilizes sliding window statistics over the monero/fiat exchange rate time series.** The window width is determined by the time between quote issuance and payout. The length of the time series should be long enough to avoid recency bias, and short enough to remain representative (conditions in 2020 vary significantly from 2015). Here, we use 4 months for the window width (1 month to fundraise + 3 months to complete work), and initially select 2 years 
for the timeseries length.

## 2-year results

We observe an unfortunate asymmetry over the past two years, for example: contributors to projects with a 4-month timeline were more than twice as likely to experience a 50% decrease in compensation value (red line) than a 50% increase in compensation value (green line).
![image](https://user-images.githubusercontent.com/21246742/80006898-bfff0e80-8482-11ea-9114-5f2d67b6e989.png)

The red cross highlights that USD/XMR decreased over 65% of sliding 4-month windows (i.e. only 35% of contributors would receive payouts worth the quote price). The orange cross shows that an 80% likelihood of receiving a sufficient payout would be achieved with a +35% buffer.
![image](https://user-images.githubusercontent.com/21246742/80006936-cdb49400-8482-11ea-994b-d95efab6a291.png)

## An observation on methods

The last point highlights how this framework is formalized as a model:

[INPUTS:] **X% confidence** that a **Y-month payout** will cover the quote (based on the **last Z months of data**) can be achieved with an [OUTPUT:] **V% volatility buffer**.

Rephrasing the (orange cross) example above: 80% confidence that a 4-month payout will cover the quote (based on the last 24 months of data) can be achieved with a 35% volatility buffer.

## 4-year results

Now, let's consider what happens if we double the timeframe (so that the data include a bull market as well as cryptowinter). The previous plots spanned the last 2 years (blue dots); now let's extend this to 4 years (blue & green dots).
![image](https://user-images.githubusercontent.com/21246742/80007032-f2a90700-8482-11ea-96b2-4b9ed2715a54.png)

Now that our we include both the bull run leading up to the all time high *and* the subsequent decay, the extended data set contains new outcomes on both sides of the red breakeven line (+ a few outliers omitted on this plot that are shown in the next).
![image](https://user-images.githubusercontent.com/21246742/80007065-fc326f00-8482-11ea-8c6d-0b99321a7363.png)

Over the 4 year history, we see that about 60% of the windows receive a payout covering the quoted value (red cross). Since the data set now includes an 8x bubble in its entirety, the volatility insurance rate for 80% confidence rises to a 170% buffer (orange cross).
![image](https://user-images.githubusercontent.com/21246742/80007083-05234080-8483-11ea-8d23-86c9ceb2e1c3.png)

## Comments

I'm hoping that having a volatility risk management framework like this will increase funding accessibility for people/businesses that want to contribute but cannot afford speculate on income.

NOTE: Past performance is no guarantee of future results. **This framework does not predict prices; it merely estimates uncertainty.**



## Mitchellpkt | 2020-04-22T17:13:06+00:00
Discovered a few months ago that Monero's plaintext unlock time leaks information and presents a transaction linkability risk (documented below). An encrypted unlock time would solve privacy issuess, however the design and performance characteristics must be carefully considered. 

Insight has put together a proposal for Isthmus & TheCharlatan to research solutions over the summer. Looking for feedback on the plan here: [https://github.com/insight-decentralized-consensus-lab/monero_encrypted_unlock_time](https://github.com/insight-decentralized-consensus-lab/monero_encrypted_unlock_time)

## SarangNoether | 2020-04-22T18:16:21+00:00
    [2020-04-22 12:59:57] <sarang> First, GREETINGS
    [2020-04-22 12:59:58] <sarang> hi
    [2020-04-22 13:00:09] — sarang will wait a couple of minutes for people to arrive
    [2020-04-22 13:00:26] <sgp_> Hello
    [2020-04-22 13:00:49] <moneromooo> .time localtime
    [2020-04-22 13:00:49] <monerobux> Could not find timezone localtime.
    [2020-04-22 13:00:50] <sgp_> .time cdt
    [2020-04-22 13:00:50] <monerobux> Could not find timezone cdt.
    [2020-04-22 13:01:07] → atoc joined (2fb9d2fc@47.185.210.252)
    [2020-04-22 13:01:24] <Isthmus> First agenda item is trolling the monerobux bot
    [2020-04-22 13:01:43] <sarang> naturally
    [2020-04-22 13:01:53] <sarang> Well, let's move to ROUNDTABLE
    [2020-04-22 13:01:54] <atoc> ooh
    [2020-04-22 13:01:58] <ArticMine> Hi
    [2020-04-22 13:02:15] <sarang> I assume Isthmus would like to share the material he posted on the agenda issue?
    [2020-04-22 13:02:27] <sarang> https://github.com/monero-project/meta/issues/456
    [2020-04-22 13:02:45] <sarang> Specifically: https://github.com/monero-project/meta/issues/456#issuecomment-617883059
    [2020-04-22 13:02:59] <Isthmus> Sure
    [2020-04-22 13:03:03] <sarang> Go ahead!
    [2020-04-22 13:03:09] <UkoeHB_> hi
    [2020-04-22 13:03:27] <Isthmus> Just completed a study quantifying the impact of exchange rate volatility for Monero-denominated delayed payouts.
    [2020-04-22 13:03:42] <Isthmus> Normally I consider exchange rate stuff out of scope for MRL but this is relevant to all CCS-funded contributors
    [2020-04-22 13:04:25] <Isthmus> Hm, I was going to cut and paste from the GitHub issue but everything is slightly too long for IRC
    [2020-04-22 13:05:05] <Isthmus> Basically, I put together a sliding window statistical analysis of the XMR price timeseries to create a framework for volatility risk management
    [2020-04-22 13:05:11] <Isthmus> The TL;DR is this:
    [2020-04-22 13:05:14] <Isthmus> [INPUTS:] X% confidence that a Y-month payout will cover the quote (based on the last Z months of data) can be achieved with an [OUTPUT:] V% volatility buffer.
    [2020-04-22 13:05:46] <Isthmus> Suppose we want to look at the last 24 months of data
    [2020-04-22 13:06:04] <Isthmus> And consider a 4-month sliding window (1 month to fundraise on CCS + 3 months to execute)
    [2020-04-22 13:06:21] <Isthmus> Here are the outcomes based on historical data
    [2020-04-22 13:06:23] <Isthmus> https://usercontent.irccloud-cdn.com/file/tbl4tkZn/image.png
    [2020-04-22 13:06:28] <Isthmus> We observe an unfortunate asymmetry over the past two years, for example: contributors to projects with a 4-month timeline were more than twice as likely to experience a 50% decrease in compensation value (red line) than a 50% increase in compensation value (green line).
    [2020-04-22 13:06:47] <sarang> That's quite the asymmetry
    [2020-04-22 13:06:57] <Isthmus> That's the probability distribution function, the cumulative version is helpful too:
    [2020-04-22 13:07:02] <Isthmus> https://usercontent.irccloud-cdn.com/file/2UBTfPI7/image.png
    [2020-04-22 13:07:07] <Isthmus> The red cross highlights that USD/XMR decreased over 65% of sliding 4-month windows (i.e. only 35% of contributors would receive payouts worth the quote price). The orange cross shows that an 80% likelihood of receiving a sufficient payout would be achieved with a +35% buffer.
    [2020-04-22 13:07:31] <Isthmus> Explaining the orange cross in the framework described above: 80% confidence that a 4-month payout will cover the quote (based on the last 24 months of data) can be achieved with a 35% volatility buffer.
    [2020-04-22 13:07:45] <Isthmus> Now, let's consider what happens if we double the timeframe (so that the data include a bull market as well as cryptowinter). The previous plots spanned the last 2 years (blue dots); now let's extend this to 4 years (blue & green dots).
    [2020-04-22 13:07:47] <Isthmus> https://usercontent.irccloud-cdn.com/file/aCapoFx3/image.png
    [2020-04-22 13:07:53] <Isthmus> oops transparent background, ssorry
    [2020-04-22 13:07:56] <Isthmus> Now that our we include both the bull run leading up to the all time high and the subsequent decay, the extended data set contains new outcomes on both sides of the red breakeven line (+ a few outliers omitted on this plot that are shown in the next).
    [2020-04-22 13:08:02] <Isthmus> https://usercontent.irccloud-cdn.com/file/kiCGTbDh/image.png
    [2020-04-22 13:08:09] <Isthmus> Over the 4 year history, we see that about 60% of the windows receive a payout covering the quoted value (red cross). Since the data set now includes an 8x bubble in its entirety, the volatility insurance rate for 80% confidence rises to a 170% buffer (orange cross).
    [2020-04-22 13:08:14] <Isthmus> https://usercontent.irccloud-cdn.com/file/le8lMFik/image.png
    [2020-04-22 13:08:40] <Isthmus> I'm hoping that having a volatility risk management framework like this will increase funding accessibility for people/businesses that want to contribute but cannot afford speculate on income.
    [2020-04-22 13:08:44] — Isthmus ends ramble
    [2020-04-22 13:09:10] <sarang> This is great data
    [2020-04-22 13:09:19] <sarang> Any questions for Isthmus?
    [2020-04-22 13:10:54] <sgp_> Volatility is expensive
    [2020-04-22 13:11:11] <sgp_> No questions, but thanks for doing this
    [2020-04-22 13:11:16] <Isthmus> ty :)
    [2020-04-22 13:11:31] <sarang> I can share next, if there are no other questions for Isthmus
    [2020-04-22 13:11:37] <ArticMine> More of a comment.
    [2020-04-22 13:11:58] <ArticMine> Thanks for the work
    [2020-04-22 13:12:30] <atoc> Yeah thanks, just for more clarity: what are Monero-denominated delayed payouts?
    [2020-04-22 13:12:41] <ArticMine> What we are dealing with is more like a two bear market as opposed to volatility
    [2020-04-22 13:13:32] <UkoeHB_> It seems like long delays in payouts are not worthwhile. Either donators or donation recipients will lose on fiat-equivalent purchasing power with a good probability
    [2020-04-22 13:13:39] <ArticMine> With the bear trend longer than the term of the typical CCS
    [2020-04-22 13:14:02] <atoc> ah I see what this is now
    [2020-04-22 13:14:17] <atoc> I actually wondered about this previously too. This is definitely good info
    [2020-04-22 13:15:14] <moneromooo> Donators can't lose. They get exactly what they intend in terms of exchange rate. Recipients can lose or win. Other market participants (which could also be the donators or recipients if they choose to play the markets in the meantime) will win or lose.
    [2020-04-22 13:15:49] <UkoeHB_> Donators can lose if recipients justifiably ask for premiums in the name of volatility, so donators are paying for the volatility
    [2020-04-22 13:16:23] <sarang> At any rate, it provides useful information for proposers and potential donors to assess the impacts of volatility
    [2020-04-22 13:16:57] <sarang> Isthmus: did you want to also discuss TheCharlatan's possible work on timelocks?
    [2020-04-22 13:17:02] <sarang> (you just posted to the agenda on it)
    [2020-04-22 13:17:07] <ArticMine> I think volatility is the wrong term here
    [2020-04-22 13:17:42] <Isthmus> @ArticMine yeah, there may be a more precise way to phrase it. Let me know if you have ideas
    [2020-04-22 13:17:47] <Isthmus> @sarang sure
    [2020-04-22 13:17:54] <Isthmus> We discovered a few months ago that Monero's plaintext unlock time leaks information and presents a transaction linkability risk
    [2020-04-22 13:18:08] <Isthmus> An encrypted unlock time is possible and would solve privacy issues, however the design and performance characteristics must be carefully considered.
    [2020-04-22 13:18:13] <sarang> Right
    [2020-04-22 13:18:14] <ArticMine> The issue is a systematic downward trend during the term of the particular CCS
    [2020-04-22 13:18:21] <sarang> We investigated this with the DLSAG preprint
    [2020-04-22 13:18:26] <Isthmus> Insight has put together a proposal for Isthmus & TheCharlatan to research solutions over the summer. Looking for feedback on the plan here: https://github.com/insight-decentralized-consensus-lab/monero_encrypted_unlock_time
    [2020-04-22 13:19:05] <Isthmus> Our goals are:
    [2020-04-22 13:19:06] <sarang> The method from the DLSAG preprint works even without the dual-key output structure, and I have some code demonstrating both the general method and how various LRS constructions could be used for this
    [2020-04-22 13:19:06] <Isthmus> Detailed system design decisions (e.g. unlock_time per output or per transaction?)
    [2020-04-22 13:19:14] <Isthmus> Prototype code to quickly test different approaches , including simulating transaction construction, signing and verification
    [2020-04-22 13:19:16] <Isthmus> Report of quantified space/time/privacy tradeoffs with each mitigation strategy
    [2020-04-22 13:19:19] <Isthmus> Implementation code for Monero source tree, for at least one of the chosen approaches
    [2020-04-22 13:19:23] <Isthmus> Comprehensive research analysis writeup , cross-referenced with code and documentation
    [2020-04-22 13:19:36] <Isthmus> Oh sorry Sarang, go ahead
    [2020-04-22 13:19:45] <sarang> Oh no, just providing some background; please continue
    [2020-04-22 13:20:24] <Isthmus> Oh, that was the end of the list :- )
    [2020-04-22 13:20:30] <sarang> Ha got it!
    [2020-04-22 13:20:38] <sarang> Yeah, so there was already some work on this
    [2020-04-22 13:20:47] <sarang> and I've been discussing it with TheCharlatan
    [2020-04-22 13:21:07] <sarang> Basically you can follow an approach similar to that in DLSAG using any d-LRS construction
    [2020-04-22 13:21:14] <sarang> Meaning MLSAG, CLSAG, Triptych can be used
    [2020-04-22 13:21:28] <sarang> Obviously the scaling will be different in size/time
    [2020-04-22 13:21:54] <sarang> But essentially you increase from a 2-LRS (signing key, amount key) to a 3-LRS (signing key, amount key, timelock key)
    [2020-04-22 13:22:10] <sarang> You also need to change how range proofs are structured, in a nontrivial way
    [2020-04-22 13:22:10] <sgp_> Does unlock time per transaction mean all outputs have the same unlock time?
    [2020-04-22 13:22:15] <sarang> In theory, yes
    [2020-04-22 13:22:29] <sarang> But it would depend on how it's designed
    [2020-04-22 13:22:30] <Isthmus> Yep @sgp_ that's how it works currently
    [2020-04-22 13:23:09] <sarang> Anyway, there's a marginal increase in transaction size to include the necessary auxiliary commitment data
    [2020-04-22 13:23:20] <sarang> But more notably, there's a time cost that scales linearly with the ring size
    [2020-04-22 13:23:21] <sgp_> Maybe market research some come first to see if there's a demand for per-output. Has this been done at all?
    [2020-04-22 13:23:32] <sgp_> *should come
    [2020-04-22 13:23:35] <sarang> This time cost exists regardless of whether the locks are per-output or per-transaction
    [2020-04-22 13:24:03] <sarang> I have C++ timing data for CLSAG to show this, and could modify the new Triptych code similarly
    [2020-04-22 13:24:13] <sarang> (no point doing it for MLSAG)
    [2020-04-22 13:25:03] <sarang> Before there's too much time/effort invested in this, I think it'd be useful to determine what costs people think are acceptable to introduce this
    [2020-04-22 13:25:40] <sarang> The signature stuff is pretty straightforward (from 2-LRS to 3-LRS), but there's additional engineering work for a much different handling of range proofs, which would also need to change the fee structure due to Bulletproofs DoS scaling
    [2020-04-22 13:25:50] <sgp_> Does this impact transactions that use the locks only or all of them?
    [2020-04-22 13:25:53] <sarang> and, of course, the timing hit needs to be considered
    [2020-04-22 13:26:08] <sarang> Well, for maximum uniformity all outputs would need locks
    [2020-04-22 13:26:16] <sarang> The lock could be set to 0
    [2020-04-22 13:26:24] <sarang> but the time cost is the same
    [2020-04-22 13:26:39] <sarang> Since for every ring member, you need to process its lock data
    [2020-04-22 13:26:52] <sarang> and the verifier can't tell which locks are 0 due to the commitment structure
    [2020-04-22 13:26:56] <UkoeHB_> I feel like knaccc since I can't imagine what utility timelocks have
    [2020-04-22 13:27:09] <Isthmus> Crossing borders
    [2020-04-22 13:27:18] <moneromooo> Would encrypting lock times prevent it from being used as a second layer building block ?
    [2020-04-22 13:27:27] <sarang> Constructions involving cross-chain and off-chain channels would need them
    [2020-04-22 13:27:37] <sgp_> Isthmus: how many transactions use these locks again? I lean towards not pursuing this unless there's a known demand
    [2020-04-22 13:27:47] <sarang> moneromooo: encrypting timelocks were originally designed for 2nd layer stuff in DLSAG
    [2020-04-22 13:27:51] <gingeropolous> i thought the second chain requires the kind of time locks that we don';t have yet
    [2020-04-22 13:27:56] <sarang> They aren't required for DLSAG, but they are useful to avoid spend heuristics
    [2020-04-22 13:27:58] <gingeropolous> second layer, sorry
    [2020-04-22 13:28:20] <sarang> e.g. ring members whose locks have just expired may be more likely to be true signers, etc.
    [2020-04-22 13:28:24] <gingeropolous> but i guess both types would need encryption
    [2020-04-22 13:30:00] <sarang> Anyway, if the decision is to support timelocks, requiring the commitment structure is good for mitigating heuristics, but it comes at a definite cost
    [2020-04-22 13:30:29] <sarang> and this cost scales with the ring size
    [2020-04-22 13:31:29] <moneromooo> I'd be ok with a fair cost if it is instrumental having a good second layer, but not really otherwise.
    [2020-04-22 13:31:32] <gingeropolous> it seems pretty integral if we want monero to be programmatic money
    [2020-04-22 13:31:52] → derpy_bridge joined (~derpy_bri@92.223.89.163)
    [2020-04-22 13:31:53] <sarang> To be clear, a solution like DLSAG requires timelocks, but does not require encrypted timelocks
    [2020-04-22 13:32:07] <sarang> It is highly beneficial for uniformity if the timelocks are encrypted, however
    [2020-04-22 13:32:08] <UkoeHB_> Isthmus it might help the proposal if there were some basic estimates of costs related to timelocks (storage requirements, additional EC ops), for both CLSAG and then for Triptych.
    [2020-04-22 13:32:28] <sarang> UkoeHB_: I already have this data for CLSAG, and presented it quite a while ago
    [2020-04-22 13:32:40] <sarang> For Triptych there are estimates (the C++ code didn't exist at the time)
    [2020-04-22 13:32:44] <UkoeHB_> ah, in which case a link would be nice
    [2020-04-22 13:32:48] ⇐ derpy_bridge_ quit (~derpy_bri@92.223.89.162): Ping timeout: 256 seconds
    [2020-04-22 13:32:50] <sarang> I can dig it up after the meeting
    [2020-04-22 13:33:09] <TheCharlatan> That's only the costs for the signature and commitments though, right sarang?
    [2020-04-22 13:33:21] <sarang> FWIW the branch is here for 3-CLSAG: https://github.com/SarangNoether/monero/tree/3-clsag
    [2020-04-22 13:33:36] <sarang> TheCharlatan: the range proof wouldn't necessarily incur any extra costs
    [2020-04-22 13:33:43] <sarang> Depending on if/how the limits are changed
    [2020-04-22 13:34:46] <sarang> If desired, I can update the new Triptych C++ code to support timelocks, for data on performance differences
    [2020-04-22 13:34:53] <sarang> it'd be pretty straightforward to do
    [2020-04-22 13:35:44] <sarang> Anyway, I support the idea if it's based on a solid understanding of the costs, and has general consensus
    [2020-04-22 13:35:45] <sgp_> I only really support the research if we know there's a solution on the table that Monero will use for second layer stuff. The "how to encrypt" question will be answered faster than the audit process. Maybe I'm not understanding the application, but I perceive this bug hurdle as needing to come first
    [2020-04-22 13:35:57] <sarang> sgp_: we know exactly _how_ to do it
    [2020-04-22 13:36:05] <sarang> (in terms of signature handling)
    [2020-04-22 13:36:11] <sgp_> I meant selecting which is best
    [2020-04-22 13:36:19] <sarang> What's not known are specifics related to range proofs, fee structure, etc.
    [2020-04-22 13:36:54] → DeanWeen joined (~dean@gateway/tor-sasl/deanguss)
    [2020-04-22 13:37:09] <UkoeHB_> fee would be pretty simple to update afaik
    [2020-04-22 13:37:43] <sarang> Perhaps. What changes is that the aggregated range proof now needs to account for newly-generated outputs, as well as a proof for each timelock input
    [2020-04-22 13:38:02] <sarang> But it's still something that would need to be considered and completed in the design/deployment process
    [2020-04-22 13:38:10] <UkoeHB_> right
    [2020-04-22 13:38:18] <sarang> and it also complicates things since there are currently no specific input limits
    [2020-04-22 13:38:39] <sarang> whereas Bulletproofs have a ceiling-power-of-2 verification cost, which is why we limit the output count
    [2020-04-22 13:38:55] <sarang> Having a separate bulletproof makes little sense from a size perspective
    [2020-04-22 13:39:05] <UkoeHB_> ah hm
    [2020-04-22 13:39:46] <UkoeHB_> per-input timelocks may be expensive, but I defer to the estimates /o\
    [2020-04-22 13:40:08] <Isthmus> Could we have 1 time per transaction, and an encrypted bit with each output
    [2020-04-22 13:40:15] <Isthmus> 1 = use encrypted timelock
    [2020-04-22 13:40:21] <Isthmus> 0 = default (10 blocks)
    [2020-04-22 13:40:37] <sarang> Isthmus: you still need the signature and range components
    [2020-04-22 13:40:51] <sarang> How you assign timelock commitments to outputs isn't really relevant there
    [2020-04-22 13:41:31] <Isthmus> Mmkay, was just trying to think of a way to bee able to lock 1+ outputs without locking your change (without having an encrypted timelock for each output)
    [2020-04-22 13:41:45] <sarang> That's a pretty minimal size cost
    [2020-04-22 13:41:56] <sarang> The real kicker is verification
    [2020-04-22 13:42:12] <sarang> and the specifics on range proof structure
    [2020-04-22 13:42:26] <Isthmus> Yep, those are key things to nail down first
    [2020-04-22 13:42:51] <sarang> Well, we have CLSAG code to give real numbers on that cost
    [2020-04-22 13:43:01] <sarang> and it's easy to modify Triptych to give its costs
    [2020-04-22 13:43:18] <sarang> What is not known is what time hit is considered reasonable
    [2020-04-22 13:43:30] <sarang> "as low as possible" isn't a design decision
    [2020-04-22 13:43:53] <sgp_> Can I step in since I really need to make sure I understand the big picture here
    [2020-04-22 13:43:59] <sarang> sure
    [2020-04-22 13:44:02] <sarang> of course
    [2020-04-22 13:44:17] <sgp_> In order to add a feature, there should be at least some stated use for it, especially if there are costs
    [2020-04-22 13:44:38] <UkoeHB_> nvm per-output timelocks would be cheap at 8 bytes per additional output, most cost is on input proving side
    [2020-04-22 13:45:01] <sgp_> So the main benefit is the ability to add things like DLSAG and other related protocols that could allow second-layer right? That time locks are necessary for second-layer solutions we know about?
    [2020-04-22 13:45:38] <sarang> Well, and we allow timelocks right now; but they have multiple accepted specifications, and likely introduce spend heuristics
    [2020-04-22 13:45:51] <Isthmus> s/likely/do/
    [2020-04-22 13:46:07] <sarang> So their presence and optionality introduce fingerprinting
    [2020-04-22 13:46:10] <sgp_> right but they aren't used as far as we know for anything in particular?
    [2020-04-22 13:46:13] <sarang> ^^ good point
    [2020-04-22 13:46:25] <Isthmus> Not only are timelocks used
    [2020-04-22 13:46:30] <Isthmus> 5 different formats are used
    [2020-04-22 13:46:33] <Isthmus> See the documentation linked above
    [2020-04-22 13:46:33] <sarang> that's what I meant
    [2020-04-22 13:46:36] <Isthmus> So SOMEBODY is using them
    [2020-04-22 13:46:48] <Isthmus> They're anonymous, unfortunately, so I don't know their use case
    [2020-04-22 13:46:54] <sarang> Requiring a uniform format is an obvious first step
    [2020-04-22 13:46:57] <UkoeHB_> what fraction of all tx have non-zero timelocks?
    [2020-04-22 13:46:57] <TheCharlatan> sgp_ they are also useful for atomic swap purposes, if you are looking for specific features.
    [2020-04-22 13:47:05] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-04-22 13:47:12] <jwinterm> was about to ask same UkoeHB_
    [2020-04-22 13:47:53] <sgp_> https://usercontent.irccloud-cdn.com/file/xIfs2dFC/table
    [2020-04-22 13:47:55] <jwinterm> TheCharlatan, but not in the state that they currently exist, right? I thought atomic swaps require the kind of time locks that bitcoin has - i.e., this tx can't be mined until certain time
    [2020-04-22 13:48:13] <gingeropolous> yeah right now its payment channels (lightning network) and atomic swaps, for the most relevant application of timelocks (i think)
    [2020-04-22 13:48:28] <Isthmus> They're not super widely used, on the order of 10k nonzero locktimes
    [2020-04-22 13:48:33] <Isthmus> Of course, neither are subaddresses ;- )
    [2020-04-22 13:48:46] <jwinterm> total number of txs is 10M order of magnitude?
    [2020-04-22 13:48:52] <Isthmus> 6M
    [2020-04-22 13:48:56] <Isthmus> Almos 7M
    [2020-04-22 13:49:01] <Isthmus> *almost
    [2020-04-22 13:49:09] <jwinterm> .c 1e4/7e6
    [2020-04-22 13:49:09] <monerobux> jwinterm: 0.001428571429
    [2020-04-22 13:49:11] <sgp_> dumb idea: why not threaten to remove this feature entirely unless someone justifies the need?
    [2020-04-22 13:49:18] <jwinterm> 0.1% more than I would've guessed
    [2020-04-22 13:49:56] <TheCharlatan> since we are spitballing a bit, Istmus and I also discussed introducing a more compact format. So if encrypting them is deemed undesirable, I believe we should still change their current behaviour to something more sane and less dangerous.
    [2020-04-22 13:49:57] <sgp_> if these are caused by someone fucking around for no purpose, then why bother having them
    [2020-04-22 13:50:05] ⇐ thrmo_ quit (~Thrmo@unaffiliated/thrmo): Remote host closed the connection
    [2020-04-22 13:50:19] <UkoeHB_> compact format?
    [2020-04-22 13:50:33] <sarang> Do you mean supporting only a single uniform format?
    [2020-04-22 13:50:43] <sarang> Because this seems like a natural first step
    [2020-04-22 13:50:46] <UkoeHB_> iirc they are varints atm, so at most 9 bytes
    [2020-04-22 13:50:52] <sarang> At least removing the fingerprinting possible within the use of timelocks
    [2020-04-22 13:50:53] → thrmo joined (~Thrmo@unaffiliated/thrmo)
    [2020-04-22 13:51:09] <sgp_> in order for the *cool* time-lock applications to come around, we need to agree to implement something else which would come with a large advance notice. This hasn't happened obviously
    [2020-04-22 13:51:34] <sarang> Well, and there is no DLSAG-type payment channel use currently available
    [2020-04-22 13:51:51] <Isthmus> @UkoeHB_ I thought it was uint64. I got a few outputs locked until 18446744073709551614 (about 500 billion years) over the weekend :- P
    [2020-04-22 13:52:06] <sarang> Isthmus: something something store of value
    [2020-04-22 13:52:15] <ArticMine> Using a single format for timelocks seems a sensible first step to me
    [2020-04-22 13:52:18] <UkoeHB_> varints have up to 63 bits of information from what I understand
    [2020-04-22 13:52:30] <Isthmus> oh yea
    [2020-04-22 13:52:46] <sarang> OK, so in the interest of time, what's a good next step in this design process?
    [2020-04-22 13:53:01] <UkoeHB_> cost estimates
    [2020-04-22 13:53:17] <sarang> Isthmus TheCharlatan: let's discuss that after the meeting
    [2020-04-22 13:53:18] <TheCharlatan> Exactly, but a varint for a timelock is completely overblown. There have been a lot of discussions on this in Bitcoin as well, for example to restrict the size to a 1 byte value that is then interpreted as a power of time.
    [2020-04-22 13:53:26] <ArticMine> single format
    [2020-04-22 13:53:27] <sgp_> I say the cost estimate of only the cheapest option to begin with to see if that action is warranted
    [2020-04-22 13:53:28] <TheCharlatan> Personally I would get rid of time based lock times entirely.
    [2020-04-22 13:53:46] <Isthmus> That introduces a correction term when blocktime changes
    [2020-04-22 13:53:53] ⇐ thrmo quit (~Thrmo@unaffiliated/thrmo): Remote host closed the connection
    [2020-04-22 13:54:04] <Isthmus> But that's easy enough to do
    [2020-04-22 13:54:31] <sgp_> TheCharlatan: haha exactly, or at least aggressively ask for justification from people who use them
    [2020-04-22 13:54:40] <sarang> OK, so beyond investigating optimal single-format cleartext use and updated cost estimates, anything else on this topic for right now?
    [2020-04-22 13:54:48] <sarang> (otherwise we could discuss it for hours...)
    [2020-04-22 13:55:09] <sarang> going once
    [2020-04-22 13:55:20] <sarang> going twice
    [2020-04-22 13:55:26] <sarang> sold
    [2020-04-22 13:55:29] <sgp_> nope, I just want to stress that we need to know why they are used before slowing down transactions
    [2020-04-22 13:55:41] <sarang> I can briefly share a couple things in the time we have left
    [2020-04-22 13:55:50] <sarang> I overhauled Triptych verification to support common-key batching
    [2020-04-22 13:55:53] <TheCharlatan> and s/time/two - deleted the wrong word :(
    [2020-04-22 13:56:20] <sarang> New timing data: https://usercontent.irccloud-cdn.com/file/TWAkCeJJ/timing.png
    [2020-04-22 13:56:32] → thrmo joined (~Thrmo@unaffiliated/thrmo)
    [2020-04-22 13:56:42] <sarang> This data represents the input-amortized verification cost for a 2-input set of signatures
    [2020-04-22 13:56:52] <sarang> Assuming the same ring is used across both inputs for Triptych
    [2020-04-22 13:56:57] <sarang> (for MLSAG/CLSAG it doesn't matter)
    [2020-04-22 13:57:21] <sarang> I also overhauled the MLSAG tests for better consistency with the other series
    [2020-04-22 13:57:24] <UkoeHB_> wait isnt that way faster?
    [2020-04-22 13:57:29] <sarang> It should be
    [2020-04-22 13:57:30] <selsta> What are amortized inputs?
    [2020-04-22 13:57:41] <sarang> If you have a 2-input transaction, you need to compute 2 signatures
    [2020-04-22 13:57:50] <sarang> For MLSAG/CLSAG, this takes twice the time as one signature
    [2020-04-22 13:58:02] <sarang> For Triptych, if you use the same ring, you get huge batching benefits
    [2020-04-22 13:58:31] <sarang> So this is the per-input cost for a 2-input transaction
    [2020-04-22 13:58:45] <sarang> For higher-input-count txs that would share rings, the benefits get even better
    [2020-04-22 13:58:59] <UkoeHB_> 🥳
    [2020-04-22 13:59:12] <sarang> The gray crossed lines are centered at the current N=11 MLSAG point
    [2020-04-22 13:59:33] <sarang> This implies that Triptych becomes slower than right now (for 2-input txs) between N=64 and N=128
    [2020-04-22 13:59:46] <sarang> (but you can't split the difference... you need to pick a power of 2)
    [2020-04-22 14:00:03] <sarang> Anyway, hopefully this gives more realistic timing data, at least across 2-input txs
    [2020-04-22 14:00:26] <sgp_> is 128 about the same time as DLSAG 12? 13?
    [2020-04-22 14:00:28] <sarang> You can use my `triptych` branch and `clsag-device` branch to construct this data for yourself
    [2020-04-22 14:00:40] <sarang> I don't have C++ data for DLSAG
    [2020-04-22 14:00:48] <sgp_> soory I meant MLSAG
    [2020-04-22 14:01:09] <sarang> I'd have to run some quick MLSAG tests on those intermediate numbers
    [2020-04-22 14:01:18] <sarang> I can have that shortly after the meeting (need to do a new build)
    [2020-04-22 14:01:24] <sgp_> it's fine, not that important
    [2020-04-22 14:01:31] <sarang> It's easy, just takes a few minutes
    [2020-04-22 14:01:55] <sarang> Anyway, that's what I wanted to share
    [2020-04-22 14:02:04] <sgp_> cool stuff
    [2020-04-22 14:02:08] <sarang> Does anyone else have research to share (we're running a little long, but that's ok)
    [2020-04-22 14:02:08] <UkoeHB_> very cool
    [2020-04-22 14:02:23] <UkoeHB_> hi yes, this proposal went up this week https://github.com/monero-project/monero/issues/6456
    [2020-04-22 14:02:35] <UkoeHB_> it's a synthesis of discussion and research from IRC over the past months
    [2020-04-22 14:03:09] <sarang> It's very comprehensive :)
    [2020-04-22 14:03:20] <sarang> I admit that I haven't had a chance to sit down and devote time to it :/
    [2020-04-22 14:03:34] <sarang> However, do you have any concrete suggestions at this point UkoeHB_?
    [2020-04-22 14:04:41] <UkoeHB_> there needs some debate about whether to pursue Janus, and which solution to adopt, but otherwise tx structure recommendations, sorted tlv, and view tag all seem concrete to me
    [2020-04-22 14:04:57] <sarang> Neat
    [2020-04-22 14:05:03] ⇐ thrmo quit (~Thrmo@unaffiliated/thrmo): Ping timeout: 272 seconds
    [2020-04-22 14:05:11] <sarang> I'll devote time to it before the next meeting for sure
    [2020-04-22 14:05:14] <UkoeHB_> also moving to mandating 1 tx pub key for 2-out tx, and 1 key per output for >2 out tx
    [2020-04-22 14:05:21] <sarang> Many thanks for continuing work on that
    [2020-04-22 14:05:53] <sarang> OK, let's briefly review ACTION ITEMS before we adjourn
    [2020-04-22 14:06:04] <Isthmus> "1 tx pub key for 2-out tx" < is that assuming that every 2-output txn has a change output?
    [2020-04-22 14:06:29] <Isthmus> *change or dummy
    [2020-04-22 14:06:32] <UkoeHB_> we only have to make that assumption if Janus is implemented
    [2020-04-22 14:07:11] <Isthmus> Ok, so then if there's a txn being split between 2 (non-change) recipients, it must be constructed as a 3-output txn with a dummy output, right?
    [2020-04-22 14:07:20] <UkoeHB_> right
    [2020-04-22 14:07:48] <Isthmus> Eh that seems harmless. Is a corner case anyways.
    [2020-04-22 14:07:54] <Isthmus> Sorry @sarang go ahead
    [2020-04-22 14:07:57] <sarang> Someone volunteered to do a review of the CLSAG code, which was very helpful... they also recommended adding Poly1305 authentication to wallet encryption, which is a good idea to prevent chosen-ciphertext adversaries
    [2020-04-22 14:08:24] <sarang> Aside from that, I'll pull up some 3-CLSAG and 3-Triptych data to help the timelock discussion, as well as some stuff on Arcturus
    [2020-04-22 14:08:27] <sarang> that's all for me :)
    [2020-04-22 14:08:29] <sarang> Anyone else?
    [2020-04-22 14:09:32] <Isthmus> I'll expand the timelock proposal with some more references/data/use cases
    [2020-04-22 14:10:17] <Isthmus> And I'll probably finish another quantum-resistance proposal today or tomorrow, currently incorporating feedback into the first draft
    [2020-04-22 14:10:22] <sarang> great
    [2020-04-22 14:11:09] <sarang> Any other final action items before we adjourn?
    [2020-04-22 14:11:10] <Isthmus> Oh yea, and I'll read UkoeHB_ 's epic github issue :- )
    [2020-04-22 14:12:07] <sarang> Righto, we are now adjourned! Thanks to everyone for a great meeting


# Action History
- Created by: SarangNoether | 2020-04-22T14:36:16+00:00
- Closed at: 2020-04-22T18:16:21+00:00
