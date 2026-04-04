---
title: Monero Research Lab Meeting - Wed 14 September 2022
source_url: https://github.com/monero-project/meta/issues/734
author: Rucknium
assignees: []
labels: []
created_at: '2022-09-13T12:18:31+00:00'
updated_at: '2022-09-18T20:06:51+00:00'
type: issue
status: closed
closed_at: '2022-09-18T20:06:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

3. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

4. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: dangerousfreedom

Previous meeting agenda/logs:

#731 

# Discussion History
## plowsof | 2022-09-18T19:09:55+00:00
Logs 
```
17:01:15 <dangerousfreedom> 1. Greetings

17:01:25 <one-horse-wagon[> Hello

17:01:27 <jberman[m]> hello

17:01:29 <rbrunner> Hi

17:02:13 <Rucknium[m]> Hi

17:04:21 <dangerousfreedom> 2. What everyone is working on?

17:06:46 <dangerousfreedom> From my side, I finished scanning bp and clsag era using my rust tools and have
been collecting some tasks to do from the next month on. I'm going to the direction of creating auditability
proofs to seraphis and also help developing a minimum useful seraphis wallet with the necessary tasks

17:07:36 <Rucknium[m]> OSPEAD work. Among other things, added a section on classification of rings by Decoy
Selection Algorithm. Included the statement "I consider exploration of ring classification to be out of scope
of this OSPEAD CSS."

17:08:03 <Rucknium[m]> Amazing what you can do if you just use the "out of scope" magic words :P

17:09:34 <rbrunner> No new anomalies turned up while scanning, I guess, dangerousfreedom?

17:09:41 <ajs_[m]> hi

17:10:14 <dangerousfreedom> rbrunner: No. Bulletproofs indeed enforces that we play safe inside the canonical
scalars and points

17:10:27 <rbrunner> Good then!

17:10:50 <dangerousfreedom> Yeah :)

17:12:02 <jberman[m]> me: mostly dev work this past week, various bug fixes. Moving back over to completing
background sync mode next, then looking to begin the dive into Seraphis/Jamtis along with rbrunner  and
dangerousfreedom

17:13:43 <rbrunner> Anybody who wants to check what our little gang is up to with Seraphis and Jamtis can
check this Matrix room: #no-wallet-left-behind:haveno.network

17:14:08 <rbrunner> The project is still nascent, not yet ready for a big announcement, but taking up speed

17:14:15 <one-horse-wagon[> I was intently looking into seeing if there is a way to increase the number of
deterministic builders before a code version is released.  This last version had only 9 people officially sign
off on it before release.  For a multi-billion dollar coin, that could be improved.

17:15:45 <rbrunner> Interesting. Any ideas yet?

17:16:45 <UkoeHB> hi, me: continued working on legacy integration, might have a working demo by next week
(non-multisig)

17:17:43 <one-horse-wagon[> My conclusion thus far is if you get a coder that can do it, he's golden.  The
process cannot be made any more easier  from what I see.

17:18:13 <ajs_[m]> hello, at my end... a small group of us have started making plans for MoneroKon 2023. This
time around, we would like to seek technical co-sponsorship with IEEE Computer Society. Hopefully, this would
attract more researchers to the conference and help with MRL recruitment efforts.

17:21:15 <Rucknium[m]> xmrack's Machine Learning paper is making the rounds. One of my BCH contacts asked me
if I had seen the paper (since CashFusion CoinJoin may be analyzable by ML). I said yes...check the
Acknowledgement section :P

17:22:43 <Rucknium[m]> dangerousfreedom: You temporarily removed your CCS proposal so that you could define
your tasks more precisely. How is the progress on that?

17:23:39 <rbrunner> "Machine Learning Paper": This, right? https://magicgrants.org/Monero-Tracing-Research/

17:24:29 <Rucknium[m]> Yes

17:24:57 <rbrunner> "LORD OF THE RINGS: ... " lol

17:25:06 <dangerousfreedom> Rucknium[m]: Yeah, I've talked to koe, jberman and rbrunner and we are creating
something more structured. I have been a bit lazy too (on purpose) the last two weeks so I can breathe and see
a bit of the big picture. I'm planning to restart working (and asking for a defined CCS) from next month on.

17:25:46 <xmrack[m]> rbrunner: Papers need a catchy name ;)

17:25:53 <chch3003[m]1> Rucknium[m]: Would be fun to analyse Wasabi with this ML hehe

17:25:56 <rbrunner> No, it's good.

17:26:42 <chch3003[m]1> I laughed at lord of rings too 🤣

17:27:13 <dangerousfreedom> Hahaha nice :)

17:30:46 <Rucknium[m]> I want to coincide the release of the disclosable part of OSPEAD fully specified plan
with the beginning of the MAGIC Monero Fund campaign to raise funds for mj-xmr's C++ work for OSPEAD:
https://github.com/MAGICGrants/Monero-Fund/issues/21

17:30:56 <Rucknium[m]> I think that will happen next week

17:34:34 <dangerousfreedom> Cool.

17:34:41 <dangerousfreedom> 3. Anything else to discuss?

17:35:48 <chch3003[m]1> Why having magic grants and CCS ? Are they not serving the same purpose ?

17:36:19 <dangerousfreedom> I guess the funds come from different sources

17:36:48 <chch3003[m]1> Well why not

17:38:13 <Rucknium[m]> With MAGIC: 1) Donations are tax-deductible if donors has U.S. tax liabilities (fully
anonymous donations are still accepted), 2) MAGIC can freeze the value of donations in any currency, reducing
risk from exchange rate volatility, 3) MAGIC is easier to deal with for external developers and researchers
since the process is more clear than CCS

17:39:04 <Rucknium[m]> We have had two recent CCSes slow down development due to exchange rate volatility
(Haveno and Molly.im)

17:39:52 <Rucknium[m]> The main drawback of MAGIC is that grant recipients need to do KYC to the MAGIC board.

17:40:34 <rbrunner> Pick your poison :)

17:41:00 <rbrunner> XMR exchange rate rollercoaster or KYC

17:41:29 <Rucknium[m]> Yes. The CCS doesn't work well for everyone. MAGIC doesn't work well for everyone.
Maybe both don't work well for everyone, so there may be some gaps still

17:41:33 <chch3003[m]1> Haha I see

17:41:40 <chch3003[m]1> Thank you 👍

17:45:24 <one-horse-wagon[> In thinking about quantum computers coming about, we look to be in a period where
it will be difficult to tell how resistant to breaking by them if we cannot test beforehand.  OpenSSL kind of
made mention of that by saying their new version 9 is believed (and I underscore believed) to be quantum
resistant.

17:46:15 <one-horse-wagon[> Big corporations and governments will have them.  The MRL will not at least
initally.

17:50:39 <dangerousfreedom> one-horse-wagon: I'm working with quantum communications and all the things I see
related to quantum computers are so far from being a threat... I guess what we can do is explore the
algorithms that are in the final phase of NIST, tevador put up a list with the algorithms and maybe trying to
do CLSAG or something simple with these underlying crypto would be nice to see how it performs. I guess
someone could start there...

17:53:10 <jberman[m]> link: https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a

18:02:29 <dangerousfreedom> Great. I guess it was already one hour. Thank you everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2022-09-13T12:18:31+00:00
- Closed at: 2022-09-18T20:06:51+00:00
