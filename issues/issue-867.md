---
title: Monero Research Lab Meeting - Wed 19 July 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/867
author: Rucknium
assignees: []
labels: []
created_at: '2023-07-17T13:57:34+00:00'
updated_at: '2023-08-09T14:49:22+00:00'
type: issue
status: closed
closed_at: '2023-08-09T14:49:22+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#863 

# Discussion History
## plowsof | 2023-08-02T19:11:36+00:00
Logs 
```
17:02:33 <Rucknium-> Meeting time! https://github.com/monero-project/meta/issues/867

17:02:41 <Rucknium-> Greetings

17:02:53 <sgp[m]> hello :)

17:03:00 <rbrunner> Yeah

17:03:41 <Rucknium-> Updates: What is everyone working on?

17:04:45 <vtnerd> noise for monero p2p and subaddress support for lws

17:04:56 <Rucknium-> I have good news and bad news. The good news is that I think I have finished the OSPEAD
troubleshooting I mentioned a few meetings ago.

17:05:15 <sgp[m]> vtnerd: Is there a summary of the noise approach?

17:05:16 <Rucknium-> The bad news is that, I think, the problem is real and cannot be completely fixed in the
short run. The problem is not severe, but it isn't negligible, either. I can give more info in the main
meeting discussion.

17:06:53 <vtnerd> sgp[m]: it strains the code a bit (when compared to SSL/TLS which is already coded), but
leaves less for DPI engines to identify

17:07:34 <vtnerd> however, most monero nodes use the standard port, so its somewhat less relevant until
something is changed about that

17:08:17 <vtnerd> the implementations are also simpler than TLS/SSL, the negotiation/handshake is pretty basic

17:10:31 <Rucknium-> Thanks, vtnerd. Discussion: What do people want to discuss?

17:13:07 <Rucknium-> OSPEAD:: Here is what I think is happening. OSPEAD requires that ring members be
independent. Independence of observations is an extremely common requirement for many estimators to be
consistent. (A consistent estimator gets closer and closer to the true value as sample size goes to infinity.)

17:13:38 <Rucknium-> I think that ring members are not fully independent. It's the Gambler's Fallacy, but this
time the gambler is right. Say that the "first" ring member is drawn from the decoy distribution. Then the
probability that the next ring member is drawn from the real spend age distribution increases from 1/15 to
1/14.

17:14:10 <Rucknium-> In other words, the realizzed value of one of the random variables "affects" the value of
other random variables. That's statistical dependence.

17:14:24 <Rucknium-> Since _exactly one_ of the ring members are the real spend, we have a subtle form of
dependence. We would have independence if every ring member had 1/16 probability of being a real spend. In
that case, some rings would have zero real spends, some would have 1, some would have 2, 3, etc.

17:14:44 <Rucknium-> I have run OSPEAD with this "alternative" of full independence (not every ring has a real
spend) and the estimator is consistent, or seems to be so with the Monte Carlo simulations.

17:15:20 <Rucknium-> In my proposal I noticed this potential issue. But I said "I do not think that this
theoretical problem causes a significant practical problem." Well, I'm eating crow now.

17:16:23 <Rucknium-> In my initial Monte Carlo simulations, we are looking at a KS distance statistic of
around 0.06 to 0.10 from the true real spend distribution when sample size (number of rings) is 200,000+

17:17:15 <Rucknium-> https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test

17:17:51 <Rucknium-> The KS distance statistic is the maximum vertical distance between the cumulative
distribution function (CDF) of two distributions.

17:18:02 <Rucknium-> The maximum is 1. The minimum is 0

17:18:25 <Rucknium-> It's not terrible, but not ideal, either.

17:18:31 <jeffro256[m]> Rucknium-: But since tx outputs appear in a predetermined order on-chain, is there any
way to extract usable information about which outputs per picked first as an external observer?

17:19:48 <Rucknium-> I odn't think so. For statistical estimator, in general, sometimes it is possible to
modify them to properly handle dependence, but doing that is generally difficult.

17:20:47 <Rucknium-> In the long term, we (I) could do some theoretical statistical work to try to figure this
out. But in the long run all rings are dead ((e hope).

17:21:06 <Rucknium-> we hope*

17:22:07 <Rucknium-> I still think this is a pretty good estimator. I plan to adjust the input data to see how
the small inaccuracy changes when the input parameters change.

17:22:10 <rbrunner> Nicely put, lol, in the long rung all rings are dead. Hopefully.

17:22:22 <jeffro256[m]> <Rucknium-> "In my initial Monte Carlo..." <- So in general, assuming that the code
picks decoys based on the gamma distribution w/ correctly no bugs, does this data suggest that people aren't
spending enotes according to the gamma distribution?

17:23:23 <jeffro256[m]> ... Because the comparison distribution is complete independence for all 16 outputs

17:24:05 <Rucknium-> In a Monte Carlo simulation, I control all input data. The whole point of OSPEAD is to
measure how different the real spend distribution is from the wallet2 gamma distribution. Then the estimated
real spend distribution will replace the wallet2 decoy selection algorithm

17:25:23 <Rucknium-> If the real spend age distribution on chain was exactly equal to the wallet2 gamma
distribution, then this estimator would have no problem being consistent. But then it would have no purpose,
either

17:25:41 <Rucknium-> I think I see what you are saying. Does this answer your question^?

17:26:58 <Rucknium-> Imagine the 16 ring members as 16 throws on a roulette table. Let the real spend be red
and the decoys be black.

17:28:06 <Rucknium-> If the "first" 15 are all black, then the last one _must_ be red. The Gambler's Fallacy
of the roulette table being "due" for a red is actually correct.

17:28:53 <Rucknium-> If they were independent throws like a normal casino, then the fact that 15 came up black
would not affect the probability that the 16th would come up red.

17:29:10 <Rucknium-> This is my hypothesis, for now, of what is wrong.

17:29:39 <jeffro256[m]> So is that distance estimate of 0.06-0.10 in a Monte Carlo simulation where you're
assuming everyone spends their true enotes according to a gamma distribution?

17:30:03 <Rucknium-> No.

17:31:29 <Rucknium-> In my Monte Carlo simulation, I assume 80% of "users" are using "wallet2" with the
specified (log) gamma. 15% are using a wallet that has a a log triangular (similar to the old DSA)
distribution. 5% are using one with a completely uniform distribution

17:32:03 <Rucknium-> The real spend of these users are the litecoin spend age distribution (for the Monte
Carlo. Each has a different week of data from 2022

17:32:22 <Rucknium-> The empirical litecoin distribution is different from Gamma.

17:32:42 <rbrunner> Maybe this situation "Gambler's fallacy true for once" case is frequent enough that some
clever people already sought and found a way how to simulate exactly such a scenario?

17:33:10 <Rucknium-> The objective of OSPEAD is to recover the litecoin real spend age. Since I generated the
input data according to the litecoin distribution, I know what the true distribution is. I measure the
distance between the true distribution and the one that OSPEAD estimates

17:34:40 <Rucknium-> rbrunner: I hope so, but inserting that into this estimator would be difficult. I can try
for a few days, but if I don't have a good solution, then probably I would say that the perfect is the enemy
of the good.

17:35:31 <rbrunner> I mean that somewhere somebody already wrote how to cope with the situation at hand, and
the job then would be to find that paoper

17:36:12 <rbrunner> Or maybe I don't understand what you are saying me ...

17:36:40 <Rucknium-> The question would be whether that "solution" would be generalized enough for this
problem. My guess is that outcome would have low probability.

17:37:17 <rbrunner> If max is 1, isn't 0.1 quite a lot already? Or is this only some rarely happening maximum
deviation?

17:37:26 <Rucknium-> With things like this in statistics, usually you cannot just "tack on" a solution

17:39:23 <Rucknium-> IMHO, the decision to be made isn't whether the etsimator perfectly gets the true value.
It's whether this new estimator is better than the old way of doing it (what is in wallet2 now).

17:39:49 <Rucknium-> 0.1 is the maximum distance over the whole CDF

17:41:06 <rbrunner> Is it possible to express in the same frame of reference how far away wallet2 is at max?
Like, 0.25 instead of that 0.1?

17:42:18 <Rucknium-> Yes, sort of. The "sort of" is because the distance would be calculated based on the
(slightly inaccurate) estimate coming out of OSPEAD

17:43:17 <rbrunner> Fascinating stuff :)

17:43:45 <Rucknium-> If you want a general idea, you could follow through with the Monte Carlo and "pretend"
that the empirical litecoin distribution is the real spend. Then just calculate the KS distance statistic
between the LTC and the wallet2 gamma distribution. I can do that in a few minutes

17:45:50 <Rucknium-> I've modified the Monte Carlo a little since i posted this, but it's the general idea:
https://github.com/Rucknium/OSPEAD/blob/main/images/draft-validation-monte-carlo.png

17:46:45 <Rucknium-> In the plot, the maximum distance between the black and blue CDFs is at about 1e+05
seconds

17:47:10 <Rucknium-> The blue is at about 0.2 and the black is about 0.7, so the KS distance statistic there
would be 0.5

17:49:39 <jeffro256[m]> Wow I didn't think that the LTC distribution would favor newer inputs so much harder
than the gamma distribution

17:51:08 <Rucknium-> Pretend that the scenario in the graph is Monero's actual reality. Then OSPEAD would
bring the KS distance stat down from 0.50 to 0.06-0.10

17:51:23 <Rucknium-> It's not perfect, but it would be a big improvvement

17:52:29 <Rucknium-> With LTC, I shifted all spends 20 minutes old so that it would be similar to Monero. But
even with that, probably LTC users spend quicker since they never have to wait.

17:53:27 <Rucknium-> The gamma is also based on really old Monero data. pre-RingCT. Much lower tx volume.

17:53:30 <jeffro256[m]> So IIUC that data says 50% of tx inputs are <= 35 minutes old (before shifting it 20
minutes)?

17:53:50 <jeffro256[m]> *LTC tx inputs

17:53:54 <Rucknium-> Yes

17:54:35 <jeffro256[m]> Dang

17:55:55 <Rucknium-> See Section 8 Inter-Temporal Stability of Spent Output Age Distribution for BTC, BCH,
LTC, and DOGE

17:55:58 <Rucknium-> https://github.com/Rucknium/OSPEAD/blob/main/OSPEAD-Fully-Specified-Estimation-Plan-
PUBLIC.pdf

17:57:11 <jeffro256[m]> Without any context, I would guess that's probably due to automated services like
exchanges, payment servers, micro payment services, etc. If we modify the decoy selection distribution to
match those payment patterns, we would give more anonymity to those services, but could actually hurt normal
users by reducing their anonymity pool. I personally, am not sending/receiving transactions every 35 minutes

17:59:11 <Rucknium-> If you like thinking about that, then you will like the discussion of the lambda
weighting parameter in that same PDF.

17:59:44 <Rucknium-> Lines 325 - 341

18:00:49 <Rucknium-> On the other hand, users interacting closely with CEXes, etc., may need protection "more
than" users who don't interact closely with them

18:03:46 <Rucknium-> I think a lot of users withdraw from CEXes and spend ASAP, too.

18:05:11 <Rucknium-> We'll end the meeting here. Thanks for attending, everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-07-17T13:57:34+00:00
- Closed at: 2023-08-09T14:49:22+00:00
