---
title: Increase ringsize for Monero v15
source_url: https://github.com/monero-project/research-lab/issues/79
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-01-03T20:50:41+00:00'
updated_at: '2024-01-24T20:26:53+00:00'
type: issue
status: closed
closed_at: '2024-01-24T20:26:53+00:00'
---

# Original Description
Monero has used a set ringsize of 11 since v8 (2018-10). Based on recent increases in the number of transactions and the amount of attention on Monero, increasing the ringsize with the (likely) implementation of Bulletproofs+ is an option that we should consider.

Note: this is a recommended increase before Triptych/Arcturus or another next-generation proving system. Initial numbers indicate that ringsize 64 or 128 is more appropriate there if/when we get to implementing that later on.

I personally feel that ringsize 11 is reasonably safe for non-targeted threat models. However, with the increased attention and activity, I think that the "buffer" is lower than I feel comfortable with.

Here's an Excel spreadsheet that you may find useful in this discussion: https://onedrive.live.com/view.aspx?resid=473062B43FF0AD33!23780&ithint=file%2cxlsx&authkey=!AOpTq2h4tkFKeUU

I recommend we consider a mostly modest increase from 11 to 13, 15, or 17. I recommend 15, which will give us a safe buffer in my opinion against non-targeted attacks.

The drawback is that this costs efficiency. If we're adding size and verification here, it should be because we feel the added safety buffer is necessary.

Size and verification comparisons for different ringsizes and different number of inputs with CLSAG are below, courtesy of Sarang. Note that verification is for verification of the signatures and the balance, NOT the verification of the entire transaction. I also added the % of outputs an attacker would need to know (evenly distributed) to deduce the real spent input in arbitrary rings. 0.002% was selected since that's roughly 1 ring per day at current transaction volumes.


ringsize | inputs | outputs | median verification (sig +   balance only) increase from 11 | size in bytes | size increase from 11 | deduce 1% | deduce 0.002%
-- | -- | -- | -- | -- | -- | -- | --
11 | 1 | 2 |   | 1419.9 |   | 63.1% | 33.9%
11 | 2 | 2 |   | 1926.8 |   | 63.1% | 33.9%
13 | 1 | 2 | 18% | 1483.9 | 5% | 68.1% | 40.6%
13 | 2 | 2 | 18% | 2054.8 | 7% | 68.1% | 40.6%
15 | 1 | 2 | 36% | 1547.9 | 9% | 71.8% | 46.2%
15 | 2 | 2 | 36% | 2182.8 | 13% | 71.8% | 46.2%
17 | 1 | 2 | 54% | 1611.9 | 14% | 75.0% | 50.9%
17 | 2 | 2 | 54% | 2310.8 | 20% | 75.0% | 50.9%



There's a history of only using prime numbers for the ringsize. While this is pretty fun, I think that it's not important (no technical reason to), and we will need to select a power of 2 for Triptych/Arcturus anyway, so we better get used to composite numbers :)

# Discussion History
## sethforprivacy | 2021-01-03T21:24:13+00:00
Do you have transaction size numbers (preferrably for 1-in 2-out and 2-in 2-out) for each of the respective proposed ring sizes post-BP+?

Would be good to project out the impact on blockchain size until a theoretical Arcturus/Triptych implementation takes place so we can better understand the long term IBD and storage costs this would have vs. the theoretical privacy benefits.

## sedited | 2021-01-04T21:55:28+00:00
I'll cast my vote (if there is such a thing) for the highest value that somebody reasonably proposes here.
Currently it's: 17

## SamsungGalaxyPlayer | 2021-01-05T01:14:48+00:00
@sethsimmons added to the initial post

## knaccc | 2021-01-05T03:26:12+00:00
Ring size | Churns prior to final tx to achieve minimum anonymity set size of 1 million inputs
--|--
3 | 12
5 | 8
7 | 7
11 | 5
13 | 5
15 | 5
17 | 4
21 | 4
32 | 3
64 | 3
128 | 2
256 | 2
1024 | 1

Formula: churns required  = ceil(log<sub>ring_size</sub> 10<sup>6</sup> - 1) = ceil(log<sub>10</sub> 10<sup>6</sup> / log<sub>10</sub> ring_size - 1)

## iamamyth | 2021-01-05T03:46:00+00:00
I support an increase. Too low of a deduction threshold renders the software wholly useless, whereas a bit of added storage, though permanent, does not a catastrophe make (the verification times don't seem like a blocker, as nodes should run fine in steady-state). Given that transactions/day are growing rather quickly and it may be multiple years before a new proving scheme goes live, maintaining ringsize 11 seems a poor wager.

## Gingeropolous | 2021-01-05T03:52:31+00:00
@SamsungGalaxyPlayer for edutainment purposes, can you include in the table some higher numbers, like 37 and 101? 

## SamsungGalaxyPlayer | 2021-01-05T03:57:58+00:00
@Gingeropolous probably not? Ringsizes like those are quite hopeless with CLSAG. The crossover point for CLSAG/Triptych size is about ringsize 16, with Arcturus having even better size performance using historical data. If we need sizes that large, we really should be rushing to implement Triptych or Arcturus instead.

You can pull the last two columns from the spreadsheet for any ringsize >2.

![image](https://user-images.githubusercontent.com/12520755/103604734-97fff000-4ed7-11eb-8bc7-76f0044b4e1a.png)

https://eprint.iacr.org/2020/018.pdf

## Gingeropolous | 2021-01-05T05:26:10+00:00
I obviously support an increase (ringsize a bajillion!). My problem is that these numbers on the low end seem incremental to the point of arbitrariness. Thus, I think we should stick to primes, for now. I have a totally unfounded speculation that somehow by haphazardly using primes we've stumbled upon some unique property of sets that only manifests with primes, in some crazy outlandish self emergent-type nonsense. So there's that. 

However, 13 seems to close to 11 to do much of anything, I frankly don't understand the deduce columns, but i grok that number go down = good. But for 13, you move like 7 points max. Also, you need the same amount of churns as a ringsize 11, so you haven't decreased the tx load on the chain. So 13's out. Even though churns are still magical? 

And it'd be cool to factor in this tx load thing. 

15, same deal. Same churns. 

Well I'll just get to the point.

17 gets us to the next churn level (4 only needed instead of 5). But you say 17 causes 54% increase in verification time and 20% increase size. Ah, but it does not. Because we are down a churn. So if churns are the thing people do to maximize their monero powers (and I guess thats what is done, because if your not maximizing your monero powers, then .... potatoes? I dunno. To churn or not to churn, whats the deal?), then we've gotten rid of an entire transaction on the chain. So, a maximum monerod transaction at our current level takes 5 transactions. Call that 1 kb per tx that takes 10 usec to verify, so thats 5 kb with ringsize 11, and its taken 50 usec to verify. Lets do ringsize 17, 1 kb turns to 1.2kb, and 10 usec turns to 15 usec. Now, we only have 4 tx's for Maximum Power Monero (tm), so its taken 4.8 kb and 60 usec. So, thats actually a 20% increase in verification time, and and the size on the chain has actually *decreased* by 4%. 

And 17 is probably at a sweet spot - I haven't ran the numbers, but I doubt a second drop in churn # won't look as pretty in that equation, mainly because the next ring drop is 37..... ah i see that the tab "summary" in that excel file is kinda doin this. 

Hrm, i just made a bunch of lilly pad hops and came to the conclusion that we need to figure out what the real numbers are for 1024. Because basically, when we switch to arcturius / tryptich, if there's still the requirement to churn to reach maximum monero... well the point is that I don't think churning is a solution. Its a bandaid.  Hrm, ok 2^10 is around 30 kb with CLSAG... hrm. I think I've lost my train of thought. Or I need more numbers for trypturius.

Before the lilly pads, I was gonna say 17 seems like a good arbitrary number in this low end nonsense.

edited because somehow thought 17 was a fibonacci. Ok, time to sleep. 


## nqtronix | 2021-01-05T08:34:03+00:00
>17 gets us to the next *churn level*

*Churn level* is a bit misleading here, as the table says "Churns prior to final tx to achieve minimum anonymity set size of 1 million inputs". This means that with a larger ring size the anonymity improves each step, even if the "level" does not go up.

>But you say 17 causes 54% increase in verification time and 20% increase size. Ah, but it does not. Because we are down a churn.

This assumes that most transactions on the chain are churned transaction. I doubt that is the case. I can't proof it (the blockchain is opaque after all), but based on the prevalant "just use monero for privaty, don't worry about it, it handles all the details"-attitiude I guess that most useres just don't bother.

Ironically this means that the avarage user will benifit most from an increase in ring size. If I approximate the anonymity set with the formula we get:
11 -> 1:120
13 -> 1:170
15 -> 1:225
17 -> 1:290

The main problem with ring size increase is the block chain bloat, right? If we eventually use Triptych with a ringsize of 64/128, we need about 1kB per transaction according to the diagram. And if the blockchain has 1kB transactions sooner or later anyway, why not invest the storage space right now and take the incremental privacy benefit? Therefore it makes sense to me to jump to a size of 17 and upgrade later to Triptych 64/128.

## MoneroArbo | 2021-01-05T14:17:38+00:00
> This assumes that most transactions on the chain are churned transaction. I doubt that is the case.

I had a similar thought. At least, I doubt if many users at all are churning 5 times. Maybe once or twice, and in that case, is a bump to 17 actually enough to get those users to churn less often?

> Note that verification is for verification of the signatures and the balance, NOT the verification of the entire transaction. 

I'm curious how it affects the entire transaction. Like, what would be the net effect on verification times going from, for example, Ringsize 11 with BP to Ringsize 15 with BP+?

## sethforprivacy | 2021-01-05T15:07:09+00:00
Upon seeing the verification/size increase along with churning data from @knaccc I would propose we go with 17 for the next ring size.

If we're going to increase it in the short term it should have a measurable increase on privacy, and needs to buy time for us to further test and implement Arcturus/Triptych, as I'm sure new attacks or attackers will be discovered between now and whenever we can move to a next-gen proving scheme.

## el00ruobuob | 2021-01-05T18:04:22+00:00
It may be interesting to compare the transaction size and verification time with their corresponding values when 11 ring size was implemented (was it two years ago?) And do the math considering the Moore law in the period. In my opinion (which is just a feeling) a ring size of 17 today will not look bad at all on both metrics.

## iamamyth | 2021-01-05T19:11:07+00:00
I'm not sure Moore's law matters:

1. It's no longer an accurate correlation for compute (verification).
2. For online verification (i.e. a node trying to maintain a steady state), transaction growth seems to be the most pertinent factor (there's no doubt nodes can keep up right now and at +50%, the issue would be falling behind with enough transaction traffic, and historical Moore's law findings don't help here). And, for initial synchronization, the question would be forward-looking compute capabilities, which tend towards infinity in a Moore's law world.
3. For storage, a similar argument to (2) applies, except Moore's law arguably still holds for storage, making a backward look all the more irrelevant (current devices can easily fit the blockchain for multiple years in the future assuming a doubling of transactions per year). 

Also, while I don't think the prior increase in ring size was a wrong decision, it's not necessarily reasonable to use it for forward projections. For one thing, the requirement for an integer ring size means 11 could have been a ceiling, so you're using an inexact multiplier. For another, ring size 11 itself could have been a forward-looking projection based on a totally different "shelf life". And, lastly, maybe there were flawed elements of that prior decision calculus which should be revisited. It seems best to consider the matter anew, bringing in whatever arguments from the prior increases that still hold weight.

## knaccc | 2021-01-05T21:10:58+00:00
@SamsungGalaxyPlayer Do you have a formula for getting from ring size to tx size (bytes)?

## Mitchellpkt | 2021-01-06T17:19:38+00:00
> There's a history of only using prime numbers for the ringsize. While this is pretty fun, I think that it's not important (no technical reason to), and we will need to select a power of 2 for Triptych/Arcturus anyway, so we better get used to composite numbers :)

I can't find the citation, but it's known bad luck to use a non-prime parameter for anonymity set size! Don't worry, I'm running a script now to find a prime power of 2 that we can use for Triptych/Arcturus. 😜

## SamsungGalaxyPlayer | 2021-01-06T18:08:22+00:00
@knaccc 32 bytes per additional decoy times the number of inputs.

## knaccc | 2021-01-06T21:31:05+00:00
@SamsungGalaxyPlayer thanks. 

here is the updated table, for 1-in, 2-out txs. Formula for tx size is `size_bytes = 1100+(ring_size-1)*1*32`

Ring size | Churns prior to final tx to achieve min. anonymity set size of 1 million inputs | Individual tx size (bytes) | Combined tx sizes (churns + final tx) (bytes)
--|--|--|--
3 | 12 | 1164 | 15132
5 | 8 | 1228 | 11052
7 | 7 | 1292 | 10336
11 | 5 | 1420 | 8520
13 | 5 | 1484 | 8904
15 | 5 | 1548 | 9288
16 | 4 | 1580 | 7900
17 | 4 | 1612 | 8060
21 | 4 | 1740 | 8700
22 | 4 | 1772 | 8860
23 | 4 | 1804 | 9020
24 | 4 | 1836 | 9180
25 | 4 | 1868 | 9340
26 | 4 | 1900 | 9500
27 | 4 | 1932 | 9660
28 | 4 | 1964 | 9820
29 | 4 | 1996 | 9980
30 | 4 | 2028 | 10140
31 | 4 | 2060 | 10300
32 | 3 | 2092 | 8368
48 | 3 | 2604 | 10416
64 | 3 | 3116 | 12464
128 | 2 | 5164 | 15492
256 | 2 | 9260 | 27780
1024 | 1 | 33836 | 67672

Therefore the sweet spot seems to be at ring size ~~17~~ 16.


## Gingeropolous | 2021-01-07T05:31:48+00:00
> Therefore the sweet spot seems to be at ring size ~~17~~ 16.

Thats blasphemy. You get your hat in the ring of primes or i'll drain your monero account!

32 does look nice. C'mon folks, whats 2 kb. And then we can egg ourselves into a 2kb triptych level, which has gotta be awesome. Remember, we're still enjoying the luxury of coming down from 13 kb. Think of that. The monero system was willing to do 13 kb txs when RingCT came out just to obfuscate transaction amounts. Or we could do 2 kb now and when triptych is implemented get a lower size so we feel good about optimizations or something. 

But I'll be the guy at the far end of the spectrum I guess, and I'll state the obvious. Monero is a beast to use. We already have to do more downloading, more verification, more carrying along of everything (well we can prune some stuff.... thats a good question... how much of that 2 kb can be pruned?). Which, to me, is fine. The goal of monero is to be money. Thus, it needs to be fungible. Ringsigs get us fungibility (along with the other stuff, but ring sigs are a big part of it). Yes, money needs to be usable, but I'll state the obvious again - monero is already a bitch to use. Why not make it just slightly more of a bitch to use (perhaps) and make it super dooper fungible? I mean, i harken back to something I've state elsewhere... if we're not going to increase the ringsize substantially (and 16-17 is not substantial), then perhaps we should consider lowering it. If increasing the number of ring members is so burdensome, then perhaps it should be lowered? (and obviously this is devils advocate here, but seriously).  And its not like a bump to 32 will break anything. No new wallets needed, no new this's or thats. 

## knaccc | 2021-01-07T05:58:28+00:00
min. anonymity set size | total txs including churns required at ring size 16 | totals txs including churns required at ring size 32 | combined tx sizes (churns + final tx) at ring size 16 | combined tx sizes (churns + final tx) at ring size 32 | blockchain storage premium (for ring size 32 vs 16)
-- | -- | -- | -- | -- | --
10,000 | 4 | 3 | 6320 | 6276 | -0.7%
100,000 | 5 | 4 | 7900 | 8368 | 5.9%
1,000,000 | 5 | 4 | 7900 | 8368 | 5.9%
10,000,000 | 6 | 5 | 9480 | 10460 | 10.3%
100,000,000 | 7 | 6 | 11060 | 12552 | 13.5%

## knaccc | 2021-01-07T07:17:21+00:00
ring size | 1-in 2-out individual tx size (bytes) | individual tx size premium (vs ring size   11) | no-churn privacy improvement (vs ring size   11) | combined tx sizes (churns + final tx) for   anonymity set size of 1 million | blockchain storage premium for anonymity set   size of 1 million (vs ring size 11) | individual tx verification time premium (vs   ring size 11) | totals txs including churns required for min.   anonymity size 1 million | combined tx verification time premium (vs   ring size 11)
-- | -- | -- | -- | -- | -- | -- | -- | --
11 | 1420 |   |   | 8520 |   |   | 6 |  
16 | 1580 | 11.3% | 45.5% | 7900 | -7.3% | 45.5% | 5 | 21.2%
32 | 2092 | 47.3% | 190.9% | 8368 | -1.8% | 190.9% | 4 | 93.9%

I think the verification time increase for ring size 32 is probably a deal-breaker.

## knaccc | 2021-01-07T07:31:30+00:00
ring size | 1-in 2-out individual tx size (bytes) | individual tx size premium (vs ring size   11) | no-churn privacy improvement (vs ring size   11) | combined tx sizes (churns + final tx) for   anonymity set size of 1 million | blockchain storage premium for anonymity set   size of 1 million (vs ring size 11) | individual tx verification time premium (vs   ring size 11) | totals txs including churns required for min.   anonymity size 1 million | combined tx verification time premium (vs   ring size 11)
-- | -- | -- | -- | -- | -- | -- | -- | --
2 | 1132 | -20.3% | -81.8% | 22640 | 165.7% | -81.8% | 20 | -39.4%
3 | 1164 | -18.0% | -72.7% | 15132 | 77.6% | -72.7% | 13 | -40.9%
4 | 1196 | -15.8% | -63.6% | 11960 | 40.4% | -63.6% | 10 | -39.4%
5 | 1228 | -13.5% | -54.5% | 11052 | 29.7% | -54.5% | 9 | -31.8%
6 | 1260 | -11.3% | -45.5% | 10080 | 18.3% | -45.5% | 8 | -27.3%
7 | 1292 | -9.0% | -36.4% | 10336 | 21.3% | -36.4% | 8 | -15.2%
8 | 1324 | -6.8% | -27.3% | 9268 | 8.8% | -27.3% | 7 | -15.2%
9 | 1356 | -4.5% | -18.2% | 9492 | 11.4% | -18.2% | 7 | -4.5%
10 | 1388 | -2.3% | -9.1% | 8328 | -2.3% | -9.1% | 6 | -9.1%
11 | 1420 | 0.0% | 0.0% | 8520 | 0.0% | 0.0% | 6 | 0.0%
12 | 1452 | 2.3% | 9.1% | 8712 | 2.3% | 9.1% | 6 | 9.1%
13 | 1484 | 4.5% | 18.2% | 8904 | 4.5% | 18.2% | 6 | 18.2%
14 | 1516 | 6.8% | 27.3% | 9096 | 6.8% | 27.3% | 6 | 27.3%
15 | 1548 | 9.0% | 36.4% | 9288 | 9.0% | 36.4% | 6 | 36.4%
16 | 1580 | 11.3% | 45.5% | 7900 | -7.3% | 45.5% | 5 | 21.2%

Assumption: verification time rises linearly with ring size.

## knaccc | 2021-01-07T07:53:31+00:00
Same table as above, but instead showing blockchain storage/verification times relative to ring size 16


ring size | 1-in 2-out individual tx size (bytes) | individual tx size premium (vs ring size   16) | no-churn privacy improvement (vs ring size   16) | combined tx sizes (churns + final tx) for   anonymity set size of 1 million | blockchain storage premium for anonymity set   size of 1 million (vs ring size 16) | individual tx verification time premium (vs   ring size 16) | totals txs including churns required for min.   anonymity size 1 million | combined tx verification time premium (vs   ring size 16)
-- | -- | -- | -- | -- | -- | -- | -- | --
2 | 1132 | -28.4% | -87.5% | 22640 | 186.6% | -87.5% | 20 | -50.0%
3 | 1164 | -26.3% | -81.3% | 15132 | 91.5% | -81.3% | 13 | -51.3%
4 | 1196 | -24.3% | -75.0% | 11960 | 51.4% | -75.0% | 10 | -50.0%
5 | 1228 | -22.3% | -68.8% | 11052 | 39.9% | -68.8% | 9 | -43.8%
6 | 1260 | -20.3% | -62.5% | 10080 | 27.6% | -62.5% | 8 | -40.0%
7 | 1292 | -18.2% | -56.3% | 10336 | 30.8% | -56.3% | 8 | -30.0%
8 | 1324 | -16.2% | -50.0% | 9268 | 17.3% | -50.0% | 7 | -30.0%
9 | 1356 | -14.2% | -43.8% | 9492 | 20.2% | -43.8% | 7 | -21.3%
10 | 1388 | -12.2% | -37.5% | 8328 | 5.4% | -37.5% | 6 | -25.0%
11 | 1420 | -10.1% | -31.3% | 8520 | 7.8% | -31.3% | 6 | -17.5%
12 | 1452 | -8.1% | -25.0% | 8712 | 10.3% | -25.0% | 6 | -10.0%
13 | 1484 | -6.1% | -18.8% | 8904 | 12.7% | -18.8% | 6 | -2.5%
14 | 1516 | -4.1% | -12.5% | 9096 | 15.1% | -12.5% | 6 | 5.0%
15 | 1548 | -2.0% | -6.3% | 9288 | 17.6% | -6.3% | 6 | 12.5%
16 | 1580 | 0.0% | 0.0% | 7900 | 0.0% | 0.0% | 5 | 0.0%

Conclusion: Since we probably can't advocate to reduce the ring size below 11, the only two clear possibilities, in my opinion, are ring size 11 or 16. We should only move to ring size 16 if we are willing to pay the price of 46% higher individual tx verification times (and 21% higher verification times in churn scenarios due to one fewer churn tx being required at ring size 16).

As noted before, this is based on verification times increasing linearly with ring size. Hopefully someone can chime in on the implications of batch verification speedups.

## iamamyth | 2021-01-07T20:41:50+00:00
> if we're not going to increase the ringsize substantially (and 16-17 is not substantial), then perhaps we should consider lowering it

An increase of x/11, x >= 5, seems pretty substantial by any definition I've ever seen. As a mental exercise, lowering it makes no sense for all the reasons stated previously, namely, the current threshold is "good enough" for most use cases, and folks can churn, etc, as needed, whereas a deduction threshold < 33%, given an almost 2x increase in transactions over the past year, should give anyone pause. The goal should be to maintain a solid safety margin for the typical user, i.e. "reasonably private" as was once stated on getmonero.org.

## SamsungGalaxyPlayer | 2021-01-09T19:35:49+00:00
I just want to note that an "anonymity set size" (definition used loosely) of 1 million is also arbitrarily selected.

While I think churning should be included in this discussion, I'm less interested since churning will be <10% of Monero's use in practice. I think the benefits should be weighted less as a result.

I currently support 15, 16, and 17, with a slight preference for the lowest number 15 for practical reasons.

## knaccc | 2021-01-10T03:34:05+00:00
@SamsungGalaxyPlayer I absolutely agree that most people won't churn.

The most critical question left, therefore, is how to reason about the increased tx verification times. Ring size 15/16/17 will mean verification time increases of 36%/45%/55%.

Btw although the 1 million is arbitrary, it's mainly to demonstrate that the only way to hit really big anonymity set sizes is with churn, and that there is a logarithmic drop-off to the benefit of higher ring sizes when churning (to hit a necessary anonymity set size target). Hitting anonymity set sizes of around 1 million+ is the only way I know of to avoid the EAE/EABE etc traceability problem.





Ring size | Anonymity set size for 3 churns + 1 final   tx | Anonymity set size for 4 churns + 1 final   tx | Anonymity set size for 5 churns + 1 final   tx | Individual tx verification time increase vs   ring size 11
-- | -- | -- | -- | --
11 | 14,641 | 161,051 | 1,771,561 | 0.0%
12 | 20,736 | 248,832 | 2,985,984 | 9.1%
13 | 28,561 | 371,293 | 4,826,809 | 18.2%
14 | 38,416 | 537,824 | 7,529,536 | 27.3%
15 | 50,625 | 759,375 | 11,390,625 | 36.4%
16 | 65,536 | 1,048,576 | 16,777,216 | 45.5%
17 | 83,521 | 1,419,857 | 24,137,569 | 54.5%








## Gingeropolous | 2021-01-12T05:15:56+00:00
> Hitting anonymity set sizes of around 1 million+ is the only way I know of to avoid the EAE/EABE etc traceability problem.

Right, and any person using a tool that offers "reasonable privacy" would expect that if they buy monero from an exchange, then send that monero to a merchant, and then the merchant deposits back on the same exchange, that the person's privacy would be maintained. 

I mean, the only fiat on / off ramps in the USA right now is kraken effectively. So in theory 100% of monero USA users are getting their monero from kraken, and 100% of monero merchants are using kraken if they need fiat. 

> I'm less interested since churning will be <10% of Monero's use in practice. 

There's literally no way to know this for sure. For all we know, 100% of Monero's users could be churning. unless @Mitchellpkt has found a way to identify churns. So, well... I dunno where that leaves us actually. 

It leaves us with really needing triptych. What's the hold up? I always forget. Audits? Time baking in the oven of open source / scientific mindspace? If it's the latter, well, I think the position of "people use monero because it's a pRiVaCy cOiN, and they are therefore churning" probably has a couple of legs to stand on. Maybe even 4 (could be a stool). Maybe even 32 legs. If it's the former then lets get them audits, and do ringsize 17. Hopefully with audits we'll only be using CLSAG's for a little bit more time.

And thats a good piece of information to factor into this decision - how long are we going to be using this proposed ringsize on CLSAG? If its years, then yes, we may want to keep the number dialed down, because years of monstrous verification requirements would be bad. But if its 6 months.... well, we'll just see future users say "man, blocks 2300000 - 2429600 take forever to sync, but it goes really fast after that!". And then they will rejoice when they are synchronized, and do a happy computer dance. 

## SamsungGalaxyPlayer | 2021-01-12T17:35:22+00:00
@Gingeropolous my best estimate is another year for Triptych.

## ArticMine | 2021-01-13T07:17:07+00:00
My recommendation is slightly higher in the 19 to 25 range. 25 being the maximum while keeping the size of a 2 in 2 out transaction under 3000 bytes.after BP+. The 3000 byte figure for the reference transaction size was set in 2018 at 1% of the minimum penalty free zone of 300,000 bytes. The transaction size at the time for 2 in 2 out was about 2740 bytes. The key consideration here is to ensure that block weight (size) can scale with the normal fee. At the time we calculated back to ring 11. 

If we were to move to ring 25 we would be around 2730 bytes for a 2 in 2 out transaction after accounting for ~96 byte reduction due to BP+. in this scenario we invest all the savings in size over the last 2 years into increasing the anonymity set. The downside of course is the increase in verification time ~2.3x for ring 25. vs the current ring 11. We would also end up with a transaction size that would be closer to where the Triptych transaction size will likely end up. I also consider a 2.3x increase in CPU performance over the last 2 years reasonable. https://www.cpubenchmark.net/desktop.html. This would compensate for the increase in verification time if we went all the way to 25. 

So what would be reasonable. I am not opposed to 17, although I find it on the low side. I would also support going all the way to 25. My preference would be 21.significantly increasing the anonymity set while at the same time leaving some size savings on the table. This also keeps the increase in verification time below the increase in CPU performance over the last 2 years. 

If the decision here is below ring 25, I will not be recommending a change in the reference transaction size from the current 3000 bytes, or the minimum penalty free zone from the current 300000 bytes.  





## MoneroArbo | 2021-01-13T15:09:06+00:00
Can anyone quantify verification time in terms of user experience? i.e. does it affect only initial daemon sync? What would be the actual impact on sync times + anything else it affects? I'm assuming +40% verification time doesn't mean corresponding blocks take 40% longer to sync, but can we make an estimate on that kind of thing, or test it?

>  This also keeps the increase in verification time below the increase in CPU performance over the last 2 years.

This seems reasonable if the CPU requirements were in a good place 2 years ago. Were they?

## SamsungGalaxyPlayer | 2021-01-13T16:24:32+00:00
Passmark has some "best value" tables.

Today: https://www.cpubenchmark.net/cpu_value_alltime.html#single-cpu
2018-10-03: http://web.archive.org/web/20181003022658/https://www.cpubenchmark.net/cpu_value_alltime.html

My best interpretation is closer to a 25-50% increase when value-driven.

## knaccc | 2021-01-14T10:29:10+00:00
> Can anyone quantify verification time in terms of user experience?

If someone has tx batch verification timings, we can determine how many hours/days of verification time it would take to verify one year of blockchain data at today's tx rate.

## garlicgambit | 2021-02-14T19:03:50+00:00
Any updates on this issue?  
  
Relevant MRL log: [Monero Research Lab Meeting - 3 February 2021](https://github.com/monero-project/meta/issues/547)

## SamsungGalaxyPlayer | 2021-09-24T15:35:30+00:00
The most evidence-based ringsize to select at this point appears to be 16.

## Gingeropolous | 2021-09-24T17:29:15+00:00
i will once again suggest that we should consider including code that automatically increases the ringsize in relation to block height. For instance, we can bump the ringsize to 16 or whatever for this release, but also include code that will increase the ringsize by 2 every 2 years or something. This will provide a failsafe in the event that we are unable to release / hf again. 

## ArticMine | 2021-09-24T18:42:49+00:00
@Gingeropolous Increasing the ring size by 2 every 2 years is an interesting idea to hedge against the project being unable to release / HF at some point in the future. 

There is a critical issue here. Increasing the ring size has a direct impact on the scaling and fee algorithms. So at ring 26 we would have to increase the minimum penalty free zone, and change fees etc. This is because the size of a 2 in 2 out transaction would approach 3000 bytes, which is used as the reference transaction size. One possible option would be to cap the ring size increases at ring size 24 (8 years). This is in effect a compromise between the high end of the range I recommended and a ring size of 16. 

I refer to

https://github.com/monero-project/research-lab/issues/70 

and

https://github.com/monero-project/monero/pull/7819 

Edit: The other consensus change that would be needed would be to also increase the minimum penalty free zone, Zm every 2 years after we reach ring size 24. 

## Gingeropolous | 2021-09-28T03:29:25+00:00
> There is a critical issue here. Increasing the ring size has a direct impact on the scaling and fee algorithms. So at ring 26 we would have to increase the minimum penalty free zone, and change fees etc. This is because the size of a 2 in 2 out transaction would approach 3000 bytes, which is used as the reference transaction size. One possible option would be to cap the ring size increases at ring size 24 (8 years). 

IMO, an 8 year failsafe isn't enough. I mean, its better than nothing. But its quite the can kick. 

Couldn't there be a way to algorithmify all of it, so there's no hardcoded numbers for these parameters? E.g., every n blocks, the average size of a transaction (or median because we love medians) is calculated and thats whats used as the reference size, and that would carry over to min penalty free zone, fees, etc? 

The damn thing is dynamic. Everythings gotta float. 

## ArticMine | 2021-09-28T05:05:08+00:00
>Couldn't there be a way to algorithmify all of it, so there's no hardcoded numbers for these parameters? E.g., every n blocks, the average size of a transaction (or median because we love medians) is calculated and thats whats used as the reference size, and that would carry over to min penalty free zone, fees, etc?

You increase Zm (currently at 300000 bytes) to keep the ratio of 2 in 2 out transaction to Zm constant. So each ring number increase above 24 is accompanied by a corresponding increase in Zm.

Edit: Since we are changing the size of a transaction by a predetermined amount at each ring size increase, we can also at the same time change Zm to keep the ratio constant. 

## SamsungGalaxyPlayer | 2021-09-28T18:45:16+00:00
I think it's far to close to consider some automatic algo increase. Further, we will need to hard fork again anyway for Lelantus Spark or whatever we go with, and those "ringsizes" will be far larger than anything we would consider with an algo increase.

## MoneroArbo | 2021-09-28T18:50:41+00:00
Agree with sgp but I like the idea of algorithmic ring size increases for inclusion in the Lelantus / whatever fork

## cirocosta | 2021-09-28T19:41:54+00:00
> **SamsungGalaxyPlayer**  I think it's far too close to consider some automatic algo increase.

+1, making it dynamic would be _really_ interesting, but practically speaking, doing bp+ _and_ this initial hardcoded increase is already enough to be absolutely sure we get right, imho.

## BigslimVdub | 2021-10-21T02:28:19+00:00
Looking at the numbers one must remember the cost of adding only a 14% size increase does not seem like much however when total blocks per day have increased over 10k since one year ago and still growing, the additional bloat to chain size should be noted especially if the change is for longer-term waiting for the next move to Triptych, BP+, etc that could alleviate some of this. Storage is cheap but the time to fully sync validating all blocks costs a lot of one's time especially on lower-end hardware. 

Is there I do agree with @iamamyth that the previous discussions on why Monero decided to move to Ring 11 should be revisited to see if the expected output of that change was accomplished after these past few years or not. Has there been any research showing that Ring 11 has been compromised and or not effective? If so would moving to Ring 16 just push the bar back a little further and patch the situation? So far it seems that only what-ifs have been discussed and not the review of prior data/discussions. 

## HardenedSteel | 2021-10-21T19:22:31+00:00
Verification times are already takes so time, increasing ring size will result as more centralized nodes. I don't support increasing.

## Hueristic | 2021-10-21T20:10:37+00:00
Where is a link to the study that shows the ability of nodes to handle this increase?

## Gingeropolous | 2021-10-26T16:11:05+00:00
@Hueristic , what would this study include? Monero is already syncable / usable on various low-end platforms (raspberry pi, pine 64, various phones). Wownero currently has a ringsize of 22 with essentially the same code. The only difference would be creating synthetic new activity to match monero's current level of activity...

## HardenedSteel | 2021-10-27T20:13:20+00:00
> @Hueristic , what would this study include? Monero is already syncable / usable on various low-end platforms (raspberry pi, pine 64, various phones). Wownero currently has a ringsize of 22 with essentially the same code. The only difference would be creating synthetic new activity to match monero's current level of activity...

@Gingeropolous  Not usable for me. I don't keep my computer 24/7 online and my disk can't keep the blockchain synced. 

## trasherdk | 2021-10-28T13:33:11+00:00
@HardenedSteel That's like only turning your freezer on when you want to cook, and expect the content to be frozen.

## HardenedSteel | 2021-10-28T22:10:15+00:00
> @HardenedSteel That's like only turning your freezer on when you want to cook, and expect the content to be frozen.

@trasherdk Most people don't run computers 24/7 like freezers. Verification times should be user friendly.

## carrington1859 | 2021-11-09T13:25:01+00:00
For the benefit of anyone stumbling in here:

During several of the linked MRL meetings this issue was discussed in depth. The loose consensus has gravitated towards a ringsize of 16 for the next upgrade. As well as the reasons discussed above, it was also determined that 16 allows flexibility in the approach to "binning" in the decoy selection algorithm because of the relative number of factors (e.g. it allows options of 8 bins of 2 decoys or 4 bins of 4 decoys). Odd or prime numbers make binning more difficult.

Binning has the potential to massively increase the effectiveness of ring sigs and several independent academic papers studying Monero have come to a recommendation of some form of binning. 

Binning is being worked on mainly by jberman and updates for his current dev work are here: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249

Binning PoC: https://github.com/monero-project/research-lab/issues/88

As for concerns about verification time, there is ongoing work to implement "view tags" which will speed up wallet synchronization by more than 50% (NOTE: does not apply to full initial verification, only to synchronizing wallets). Read more here: https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero

## HardenedSteel | 2021-11-10T14:02:13+00:00
> (NOTE: **does not apply to full initial verification**, only to synchronizing wallets).

Synchronizing wallet already quick enough, the concern is about initial blockchain verification.

## UkoeHB | 2021-11-28T18:02:51+00:00
> Hopefully someone can chime in on the implications of batch verification speedups.

@knaccc Ring size and batch verification are independent. Larger rings are not ameliorated by batching.

## chaserene | 2024-01-16T14:05:22+00:00
the v15 network upgrade happened, I think this can be closed.

# Action History
- Created by: SamsungGalaxyPlayer | 2021-01-03T20:50:41+00:00
- Closed at: 2024-01-24T20:26:53+00:00
