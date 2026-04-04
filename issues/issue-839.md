---
title: Monero Research Lab Meeting - Wed 17 May 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/839
author: Rucknium
assignees: []
labels: []
created_at: '2023-05-17T16:01:45+00:00'
updated_at: '2023-05-23T19:46:00+00:00'
type: issue
status: closed
closed_at: '2023-05-23T19:46:00+00:00'
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

#834 

# Discussion History
## UkoeHB | 2023-05-17T17:32:09+00:00
`[05-17-2023 17:02:09] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/839`
`[05-17-2023 17:02:09] <UkoeHB> 1. greetings`
`[05-17-2023 17:02:09] <UkoeHB> hello`
`[05-17-2023 17:02:23] <rbrunner> Hello`
`[05-17-2023 17:02:43] <vtnerd_> hi`
`[05-17-2023 17:02:48] <ArticMine[m]> Hello `
`[05-17-2023 17:03:37] <Rucknium[m]> Hi`
`[05-17-2023 17:04:46] <UkoeHB> 2. updates, what's everyone working on?`
`[05-17-2023 17:05:31] <UkoeHB> me: rebased the seraphis library (and squashed all the commits for easier rebasing - you can see the history of commits in branch seraphis_lib_hist_05_15_23)`
`[05-17-2023 17:05:46] <UkoeHB> now working on escrowed market design for monerokon`
`[05-17-2023 17:06:59] <vtnerd_> I finally fixed all the functional_tests in the serialization replacement : https://github.com/vtnerd/monero/tree/replace_serialization`
`[05-17-2023 17:07:07] <Rucknium[m]> Reviewing compdec 's (Nathan Borggren) research proposal as part of MAGIC Monero Fund committee. Doing some speedup refactoring of some OSPEAD code that is getting me to the point of feasible single-iteration Monte Carlo tests. The tests so far look good.`
`[05-17-2023 17:08:54] <xmrack[m]> Hi`
`[05-17-2023 17:12:12] <UkoeHB> 2. discussion, anything to discuss today?`
`[05-17-2023 17:13:33] <Rucknium[m]> With the Bulleproofs++ paper, are we waiting for the author(s) to upload a new version to IACR with more complete math proofs?`
`[05-17-2023 17:15:34] <Rucknium[m]> I think the steps were: Authors put a version to a conference that was "short" due to page limits & they said they would put up a longer version, Diego Salazar  said that the conference version "offloaded" a lot of...something, and therefore doing a review at this stage may not be a good idea. Is that correct?`
`[05-17-2023 17:20:47] <vtnerd_> yeah Im not the best source, but I had trouble following the equations a bit - the documentation in the c implementation is actually better`
`[05-17-2023 17:21:24] <vtnerd_> as far as it working, thats something else entirely because its different from the prior versions, so someone more qualified would have to review`
`[05-17-2023 17:21:40] <vtnerd_> Diego seemed to be waiting on a newer version last I recall`
`[05-17-2023 17:21:59] <UkoeHB> yeah we need the full version of the paper for a proper review`
`[05-17-2023 17:24:03] <Rucknium[m]> plowsof could reach out to Eagen again.`
`[05-17-2023 17:26:28] <UkoeHB> if there is nothing else to discuss today, we can wrap it up`
`[05-17-2023 17:31:34] <UkoeHB> ok thanks for attending guys`

# Action History
- Created by: Rucknium | 2023-05-17T16:01:45+00:00
- Closed at: 2023-05-23T19:46:00+00:00
