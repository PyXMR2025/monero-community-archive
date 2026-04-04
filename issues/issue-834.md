---
title: Monero Research Lab Meeting - Wed 10 May 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/834
author: Rucknium
assignees: []
labels: []
created_at: '2023-05-09T16:09:28+00:00'
updated_at: '2023-05-13T19:13:04+00:00'
type: issue
status: closed
closed_at: '2023-05-13T19:13:04+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#833 

# Discussion History
## UkoeHB | 2023-05-10T17:29:37+00:00
`[05-10-2023 17:00:14] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/834`
`[05-10-2023 17:00:14] <UkoeHB> 1. greetings`
`[05-10-2023 17:00:14] <UkoeHB> hello`
`[05-10-2023 17:00:17] <vtnerd_> hi`
`[05-10-2023 17:00:58] <Rucknium[m]> Hi`
`[05-10-2023 17:03:29] <Rucknium[m]> I think the bridge is awake now.`
`[05-10-2023 17:03:59] <UkoeHB> low attendance today, will be a short meeting`
`[05-10-2023 17:04:06] <UkoeHB> 2. updates?`
`[05-10-2023 17:04:40] <UkoeHB> me: attended monerotopia`
`[05-10-2023 17:05:17] <Rucknium[m]> I presented "A Statistical Research Agenda for Monero" at Monerotopia.`
`[05-10-2023 17:05:17] <Rucknium[m]> Here are the slides: https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2023-Slides.pdf`
`[05-10-2023 17:05:34] <Rucknium[m]> If you want to hear a decent but unenthusiastic synthesized voice: https://vimeo.com/824376532`
`[05-10-2023 17:05:34] <Rucknium[m]> The video presentation doesn't add a whole lot compared to just reading the slides.`
`[05-10-2023 17:05:54] <vtnerd_> mention tx_extra again lol`
`[05-10-2023 17:05:54] <vtnerd_> or maybe I shouldn't have said even that`
`[05-10-2023 17:06:14] <Rucknium[m]> Maybe I should have titled it "Trustless zk-SNARKs aren't battle-tested + A Statistical Research Agenda for Monero"`
`[05-10-2023 17:07:54] <vtnerd_> I didn't get as much done on bp++ as I would've hoped :/`
`[05-10-2023 17:08:29] <vtnerd_> one problem I have is Ive promised too many things, I think, as Im now getting pressured to do LWS stuff for a small fee (pushing back hard on this at the moment)`
`[05-10-2023 17:09:36] <vtnerd_> but I'll try to wrap my head around this yet, whats intriguing is the c and rust implementation of bp++ appear to do variable bases, not sure why they didnt fix them to one`
`[05-10-2023 17:10:06] <UkoeHB> thanks guys`
`[05-10-2023 17:10:11] <UkoeHB> 3. discussion`
`[05-10-2023 17:10:22] <UkoeHB> I have no topic to discuss`
`[05-10-2023 17:11:42] <vtnerd_> I guess no one does then`
`[05-10-2023 17:12:06] <Rucknium[m]> I have been considering compdec 's (Nathan Borggren) research proposal about EAE-like attacks posted earlier this week in this channel.  Borggren already co-authored two short papers about Monero's potential privacy problems: `
`[05-10-2023 17:12:11] <Rucknium[m]> Borggren & Yao (2020) "Correlations of multi-input Monero transactions."`
`[05-10-2023 17:12:11] <Rucknium[m]> Borggren, Kim, Yao, & Koplik (2020). "Simulated blockchains for machine learning traceability and transaction values in the Monero network."`
`[05-10-2023 17:12:29] <sgp[m]> hello, sorry I'm late`
`[05-10-2023 17:13:14] <Rucknium[m]> I am not familiar at all with one of the main techniques (Topological Data Analysis) proposed in the proposal. That limits the feedback and analysis I can give.`
`[05-10-2023 17:13:41] <Rucknium[m]> Overall, it looks like a strong proposal.`
`[05-10-2023 17:16:28] <Rucknium[m]> Some feedback:`
`[05-10-2023 17:17:45] <Rucknium[m]> 1) We need clear straight lines connecting the methodologies to an attacker's objective: determining the false positive and false negative rate of guessing in an EAE-like attack. `
`[05-10-2023 17:17:58] <Rucknium[m]> 2) Using transaction uniformity defects would be useful, but may be a distraction from the main research question.`
`[05-10-2023 17:17:59] <Rucknium[m]> 3) Doing a testnet set of transactions probably will be harder and just as useful as simulating simple data directly with Python, R, or something like that.`
`[05-10-2023 17:18:09] <Rucknium[m]> The Matrix-IRC bridge maintenance was supposed to be finished by now.`
`[05-10-2023 17:18:57] <Rucknium[m]> In case contact is lost: https://libera.monerologs.net/monero-research-lab`
`[05-10-2023 17:19:51] <UkoeHB> thanks Rucknium[m] `
`[05-10-2023 17:24:50] <UkoeHB> if that is all, we can call it for today`
`[05-10-2023 17:29:03] <UkoeHB> thanks for attending guys`

# Action History
- Created by: Rucknium | 2023-05-09T16:09:28+00:00
- Closed at: 2023-05-13T19:13:04+00:00
