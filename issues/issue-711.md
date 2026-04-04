---
title: Monero Research Lab Meeting - Wed 01 June 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/711
author: Rucknium
assignees: []
labels: []
created_at: '2022-05-30T19:00:40+00:00'
updated_at: '2022-06-06T19:02:15+00:00'
type: issue
status: closed
closed_at: '2022-06-06T19:02:15+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

7. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

8. Any other business

9. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#709 

# Discussion History
## plowsof | 2022-06-01T23:18:35+00:00
Logs 
```
17:00:11 <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/711

17:00:11 <UkoeHB> 1. greetings

17:00:11 <UkoeHB> hello

17:00:42 <rbrunner> Hello

17:01:38 <jberman[m]> hello

17:01:39 <Rucknium[m]> Hi

17:01:57 <dangerousfreedom> Hello

17:03:05 <UkoeHB> 2. updates, what is everyone working on?

17:03:51 <rbrunner> Busy making multisig txs to test #8149, with 3/5

17:04:02 <rbrunner> So far looking good

17:04:16 <dangerousfreedom> Working on my understanding of BP

17:05:22 <jberman[m]> been working strictly on reviewing 7760 to understand its core logic. I finished
stepping through old code while running the tests to understand exactly what the issues discovered are, and am
working through understanding exactly how the fixes applied solve the tests

17:05:38 <UkoeHB> me: Working on seraphis enote scanning (thinking about how to handle reorgs today), plus did
some miscellaneous robustness improvements to the seraphis library.

17:06:23 <Rucknium[m]> Released my analysis of the U.S. Federal Reserve data on use of cryptocurrency as a
payment means:

17:06:23 <Rucknium[m]>
https://www.reddit.com/r/Monero/comments/uyi6kw/new_data_on_banking_the_unbanked_in_the_us/

17:07:02 <Rucknium[m]> Analyzing Dogecoin output spend age distribution over time. Some very preliminary
result to share if we have time.

17:07:28 <kayabanerve[m]> Afternoon, everyone :)

17:09:13 <rustyrose[m]> Hi all, im a developer but have never worked with Monero before. What's the best way
to get started?

17:09:56 <UkoeHB> rustyrose[m]: is there something in particular you want to work on?

17:10:46 <plowsof[m]> #monero-recruitment:monero.social lets not derail the meeting rustyrose

17:11:24 <UkoeHB> 3. discussion, anything to discuss? comments/questions?

17:13:06 <rbrunner> I guess that #8149 needs a final review, after the changes that happened.

17:13:17 <rbrunner> Maybe we should make that known, to find some brave soul

17:14:07 <rbrunner> The warnings about "experimental multisig" are merged and work wonderfully :)

17:14:19 <rbrunner> Now only the code itself is needed ...

17:14:20 <UkoeHB> lol great

17:15:13 <rustyrose[m]> nothing in particular, but i dont know where to start

17:15:39 <UkoeHB> yes, please someone review 8149

17:15:58 <dangerousfreedom> UkoeHB: Sorry, I didnt have time to look at the multisig documentation but I
promise I will get started this weekend.

17:17:29 <UkoeHB> rustyrose[m]: I'd start by learning something. Use software (maybe you'll find a bug or
needed feature). Read github issues or open PRs. Read the code. Try to build something. We don't have managers
or task lists, everyone is self-driven.

17:17:51 <moneromooo> rustyrose[m]: ask in #monero-dev

17:19:16 <UkoeHB> dangerousfreedom: sweet that would be great :)

17:19:44 <Rucknium[m]> Speaking of needing more people to review critical cryptography, I am putting together
a target list of cryptography-heavy universities and departments that the MAGIC Monero Fund could contact to
fund Monero-specific research. Is anyone aware of a good list to start with?

17:20:19 <UkoeHB> I don't, but you could try contacting sarang for advice

17:23:19 <UkoeHB> Any other topics?

17:24:55 <Rucknium[m]> Like I've mentioned before, I'm looking at the blockchain of other transactional
cryptocurrencies to see how stable the distribution of the age of spent outputs is over time. One way to do
this is to fit parametric distributions to the 2020 data and then see how the fit performs when the 2020 fit
is compared to the distribution in each week of 2021. This sort of simulates what a new decoy selection
algorithm for Monero would

17:24:56 <Rucknium[m]> have to contend with: fit distributions on past data and then use it for future data.

17:25:24 <Rucknium[m]> So far I've looked at Dogecoin.

17:25:49 <Rucknium[m]> Here is a graph of very preliminary results:

17:25:50 <Rucknium[m]> https://github.com/Rucknium/OSPEAD/blob/main/images/non-xmr-dry-
run/dogecoin-2021-spent-output-age.png

17:26:08 <Rucknium[m]> L_FGT is a "privacy impoverishment" measure. L_Welfare is a "welfare" measure. Higher
values indicate worse fit, i.e. higher difference between the "decoy" distribution and the real distribution
during that week.

17:26:33 <Rucknium[m]> Each measure has two different "flavors". Basically, the higher parameter for each
measure indicates that the fit was made with greater risk aversion, i.e. penalizes the distance between real
and "decoy" to a greater extent as the difference increases.

17:27:43 <Rucknium[m]> Consistent with expectations, there are large spikes in the graph when there were
spikes in the Dogecoin fiat exchange rate, number of on-chain txs, or amount of fiat-denominated value moved
on the chain.

17:28:24 <UkoeHB> is it bi-modal? if you take out the connecting lines

17:28:45 <Rucknium[m]> Anyway, I'm not looking for any specific input at this point. Just letting you know the
direction of this research.

17:29:54 <moneromooo> I wonder if the age of inputs just moves with price...

17:30:22 <moneromooo> ie, price increases causes older outs to move.

17:30:49 <moneromooo> That'd suck for the fake out selection.

17:31:41 <Rucknium[m]> UkoeHB: Good question. I think it probably is. Basically, there is a "normal mode" that
may reflect usual spend behaviors, and then when there is a speculative activity, the age distribution changes
-- probably old coins are "waking up" and being sent to exchanges.

17:31:42 <UkoeHB> mitigating that kind of variance is big advantage to binning

17:32:14 <Rucknium[m]> moneromooo: It seems to me that price is a strong driver of shifts in the distribution,
yes. I don't have the paper in front of me, but there was a paper a while ago that said that the majority of
BTC on-chain activity was speculative, involving exchanges.

17:34:16 <Rucknium[m]> Actually, here is that paper: https://www.nber.org/papers/w29396

17:34:31 <Rucknium[m]> >We show that the vast majority of Bitcoin transactions between real entities are for
trading and speculative purposes. Starting from 2015, 75% of real bitcoin volume has been linked to exchanges
or exchange-like entities such as on-line wallets, OTC desks, and large institutional traders.

17:35:16 <jberman[m]> +1 this is building a stronger case for binning

17:35:28 <Rucknium[m]> Ok, maybe the paper isn't from a while ago. Oct. 2021 is the posting date

17:35:30 <jberman[m]> I'm also curious if outputs are younger or older than expected in these spikes

17:35:44 <moneromooo> Why would one link "exchanges or exchange-like entities" to "on-line wallets" ?

17:36:09 <moneromooo> I assume "on-line wallets" means something like mymonero.

17:36:33 <moneromooo> Maybe because it moves the p-value down...

17:36:36 <UkoeHB> mixers?

17:36:51 <rbrunner> Swapping services? They are not yet listed else

17:37:10 <moneromooo> Oh. I am ignorant of what Bitcoin does so I used monero as a proxy. Alright then.

17:37:32 <Rucknium[m]> moneromooo: I'll see if they disaggregate the numbers further

17:40:07 <Rucknium[m]> jberman: Overall in my investigations of Dogecoin and Litecoin, it seems that the
distribution of the age of spent outputs is less stable than I expected. That means that a static decoy
selection algorithm that we have now (and will have with my near-term overhaul of it)  would not do a great
job of covering the distributional shifts over time. Which yes would probably improve the case for binning,

17:42:44 <hyc> David Rosenthal reached similar conclusion https://blog.dshr.org/2022/02/ee380-talk.html

17:42:56 <Rucknium[m]> In the paper, "Figure 3: Decomposition of real volume" shows that 40% of BTC volume
involved exchanges, narrowly defined (I think)

17:42:59 <hyc> only 27k "economically meaningful" bitcoin txns/day

17:43:16 <hyc> 75% are just inter-exchange\

17:44:04 <hyc> only 2.5% of bitcoin txns are p2p

17:45:03 <hyc> hm, he's just referencing the paper you linked

17:46:11 <Rucknium[m]> One caveat here: In theory Monero's adjustments of the decoy selection algorithm based
on number of txs in each block would mitigate this issue to some extent. I did not try to mimic that effect
and adjustment in my work with Dogecoin or Litecoin so far.

17:46:43 <Rucknium[m]> It was clever to implement that adjustment :)

17:47:11 <jberman[m]> This is true, it biases towards greater volume

17:48:19 <jberman[m]> Just curious, is there something that shows the spikes are caused by a higher freq of
older outputs being spent and I'm not seeing it?

17:50:03 <Rucknium[m]> jberman: No. These graphs are a high-level summary. I will work on quantifying exactly
how the distribution shifted. Mean, median, variance, skew, and probably a visualization.

17:52:11 <jberman[m]> Cool :) I could definitely see spikes caused by a higher freq of younger outputs too.
Rabid frenzy to buy/sell/move between exchanges/off to wallets/test txs etc.

17:54:20 <Rucknium[m]> One way to think about these lines in the chart is that they show a metric that is akin
to the Kolmogorov-Smirnov distance between the 2020 distribution and the distribution in each week of 2021. So
it is a measure of difference, but it doesn't show in which ways, exactly, it is different.

17:54:21 <kayabanerve[m]> I haven't really commented as I haven't had much to say, as my work is mostly around
Monero not on it, though I did want to note the burning bug has had been a topic of mine recently, before this
meeting ends. I have an open MRL issue documenting an adjustment to the shared key definition removing it as
an option, along with a suggested alternative by koe, which isn't planned to be adopted (and after further
review doesn't

17:54:21 <kayabanerve[m]> appear possible due to DoS issues). Seraphis itself has the update, and I've reached
out to a few parties to discuss the burning bug, the evolved attack, and mitigations to ensure not only are we
forward thinking, yet making sure no one missed the original memo.

17:55:18 <kayabanerve[m]> Sorry for interrupting the current conversation with that :p

17:55:28 <UkoeHB> no worries, thanks for commenting

18:00:35 <UkoeHB> ok that's the end of the meeting, thanks for attending everyone

18:01:01 <rbrunner> Only the drama was missing :)

18:01:52 <UkoeHB> shaping up to be a calm, productive day



```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## UkoeHB | 2022-06-01T23:19:36+00:00
thanks, I frequently forget to do this...

## plowsof | 2022-06-01T23:24:02+00:00
No problem! 9/10 i read these in the evenings, always happy to help. 

# Action History
- Created by: Rucknium | 2022-05-30T19:00:40+00:00
- Closed at: 2022-06-06T19:02:15+00:00
