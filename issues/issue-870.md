---
title: Monero Research Lab Meeting - Wed 26 July 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/870
author: Rucknium
assignees: []
labels: []
created_at: '2023-07-25T18:11:04+00:00'
updated_at: '2023-08-01T21:11:54+00:00'
type: issue
status: closed
closed_at: '2023-08-01T21:11:54+00:00'
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

#867 

# Discussion History
## plowsof | 2023-08-01T21:03:54+00:00
Logs 
```
17:00:38 <Rucknium[m]> Greetings. Hi.

17:00:40 <vtnerd> hi

17:01:13 <rbrunner> Hello

17:03:13 <Rucknium[m]> Updates: What is everyone working on?

17:03:52 <vtnerd> worked more on webhook/zmq stuff for lws (new-account notification), and a little on noise
in p2p

17:04:27 <rbrunner> Reviewing this, the discussion could also be of wider interest: https://github.com/monero-
project/monero/pull/8619

17:04:39 <Rucknium[m]> me: starting to measure the ring member dependence problem that affects OSPEAD, which I
discussed last week. And searching for solutions.

17:07:44 <Rucknium[m]> rbrunner: With ring size >=128, will the data storage requires of background sync start
to become a problem?

17:08:16 <Rucknium[m]> I assume that with larger ring size the wallet would have to store more candidate
outputs before it loads the spend key.

17:08:57 <rbrunner> Sounds right, yes. Hard to say. Doesn't this cry out for a little simulation? :)

17:09:40 <Rucknium[m]> You could simulate, but it's probably easier to just apply a formula

17:10:43 <Rucknium[m]> data_required_per_detected_ring_inclusion * number_of_outputs_in_wallet * 128, for the
worst case scenario

17:10:47 <rbrunner> My "gut feeling" tells me that this probably won't develop into a real problem.
Transactions are quite small, I think we could hit quite a lot of them until we run into storage problems

17:11:47 <Rucknium[m]> Users likely would not hit the full 128 since they would space out their outputs in
time, plus it takes  a month or more to approach the 128, theoretically

17:12:02 <rbrunner> It stores the transaction plus a bit of extra info per "hit".

17:13:22 <Rucknium[m]> FYI jberman has a new CCS proposal up to work on Seraphis and coding full chain
membership proofs (Curve Trees): https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/401

17:15:32 <Rucknium[m]> If there are no other agenda items, I will discuss the ring member dependence issue.

17:15:37 <Rucknium[m]> Correlation.

17:15:49 <Rucknium[m]> Correlation is a linear measure of the dependence of two random variables. It will not
correctly measure dependence when the dependence is partially or completely nonlinear. This is a standard
caveat.

17:16:07 <Rucknium[m]> I simulated 2 million rings of 16 members each with the gamma distribution as decoys
and the empirical litecoin distribution as real spends.

17:16:22 <Rucknium[m]> I computed the correlation between each pair of ring members. The correlation, after
taking logs of the data, is about -0.0046

17:16:43 <Rucknium[m]> Correlation can range from 1 to -1. A correlation of zero means no correlation (but not
necessarily no dependence).

17:16:47 <Rucknium[m]> Like I said before, the dependence between ring members is subtle. -0.0046 is a small
magnitude.

17:17:13 <Rucknium[m]> I think that the correlation is negative because other ring members have a chance to be
unlike each other. When a specific ring member is from the decoy distribution, that increases the probability
that the other ring members are from the real spend distribution, and vice versa.

17:17:24 <Rucknium[m]> If I set ring size to only 3, then my correlation is -0.10. That makes sense since
there is a much higher probability of ring members being unlike each other when there are two decoys and one
real spend.

17:17:45 <Rucknium[m]> There's the update of more details on the problem. Now for a possible solution.

17:18:07 <Rucknium[m]> I think there is a possible solution. It's not a quick fix at all. It would take time.
I give it a 60-70% probability of "working". By "working" I mean it would give a much better estimate than the
current estimator that assumes independent ring members.

17:19:37 <Rucknium[m]> I think we should give it a shot. The main alternative is to stay with the estimator
that requires independent ring members. It is known to be somewhat inaccurate since ring members are actually
slightly dependent.

17:19:52 <Rucknium[m]> Input?

17:20:52 <rbrunner> Well, as I know pretty much nothing about statistics, I almost automatically go into
"project management" thinking instead

17:21:24 <rbrunner> and there I see trade-off "Make OSPEAD go into service (even) later" and "make OSPEAD (a
bit) better"

17:21:30 <Rucknium[m]> What is your project management input?

17:22:03 <Rucknium[m]> rbrunner: That's what I think the trade-off is, too

17:22:21 <rbrunner> I don't remember, do we need a hardfork to introduce it? Maybe not.

17:23:00 <rbrunner> We already live with more than 1 algorithm :)

17:23:29 <Rucknium[m]> We don't need a hardfork since wallet software selects decoys. But if we don't do it at
a hardfork, then there is some possibility for wallet fingerprinting old vs new versions of wallet2

17:23:55 <rbrunner> So the idea comes to mind to introduce OSPEAD as-is first, and maybe only after that start
an attempt to solve that dependency problem.

17:24:24 <Rucknium[m]> The risk, in probability terms, of fingerprinting could be estimated IMHO, but I
declare it outside the scope of this OSPEAD CCS. It could be in scope of another one

17:25:19 <rbrunner> The problem that OSPEAD saves is tied to rings, right? So if we really manage to get rid
of them, it will retire as well.

17:25:34 <rbrunner> Or, more in general, decoys of course

17:25:40 <Rucknium[m]> rbrunner: That's correct.

17:26:05 <xmrack[m]> Hey sorry I’m late. My update is that k-anonymity is implemented for the block explorer.
thanks to hyc for helping design the theory behind it and jeffro256 for helping make the needed modifications
to db_lmdb.cpp. I am working on performance updates at the moment.

17:26:31 <rbrunner> With the caveat of being a statistics noob, as already confessed, I would probably try to
get into service what we have now.

17:27:41 <xmrack[m]> https://github.com/monero-project/monero/pull/8958

17:28:19 <rbrunner> "Having now" is anyway only having the "system". We don't have working C++ code for it
yet, if I understand correctly.

17:28:36 <Rucknium[m]> Thanks, xmrack

17:28:58 <rbrunner> Sounds like a funny thing, that PR

17:29:16 <rbrunner> (In a positive sense, nice what all gets built.)

17:29:41 <Rucknium[m]> AFAIK, it would be a small amount of code to implement it. Basically substitute out
GAMMA in wallet2 and its parameters for what OSPEAD estimates.

17:30:15 <rbrunner> Ah, ok, then take won't take overly long.

17:31:19 <Rucknium[m]> We don't have to decide now what to do. I will poll others, too.

17:31:49 <rbrunner> Always a good idea. We are not that many people here right now anyway.

17:34:23 <Rucknium[m]> xmrack: Do you have opinions about this ring member dependency issue? You may want to
read the logs from last meeting.

17:35:42 <xmrack[m]> Rucknium: will have to get back to you on this. Out right now and dont have time to read
up

17:36:27 <Rucknium[m]> Any other items to discuss?

17:36:51 <rbrunner> Not from me.

17:38:08 <Rucknium[m]> Let's end the meeting here.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-07-25T18:11:04+00:00
- Closed at: 2023-08-01T21:11:54+00:00
