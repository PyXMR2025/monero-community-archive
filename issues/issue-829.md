---
title: Monero Research Lab Meeting - Wed 19 April 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/829
author: Rucknium
assignees: []
labels: []
created_at: '2023-04-18T19:09:07+00:00'
updated_at: '2023-04-25T15:59:05+00:00'
type: issue
status: closed
closed_at: '2023-04-25T15:59:05+00:00'
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

#825 

# Discussion History
## UkoeHB | 2023-04-21T20:34:33+00:00
`[04-19-2023 16:59:40] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/829`
`[04-19-2023 16:59:40] <UkoeHB> 1. greetings`
`[04-19-2023 16:59:40] <UkoeHB> hello`
`[04-19-2023 17:00:15] <vtnerd> hi`
`[04-19-2023 17:00:30] <rbrunner> Hello`
`[04-19-2023 17:00:34] <Rucknium[m]> Hi`
`[04-19-2023 17:03:37] <UkoeHB> 2. updates, what's everyone working on?`
`[04-19-2023 17:04:13] <UkoeHB> me: working on 'implementing seraphis' companion paper for the main paper, and need to prep for monerotopia`
`[04-19-2023 17:04:40] <Rucknium[m]> I released my analysis of the privacy impact of Mordinals:`
`[04-19-2023 17:04:40] <Rucknium[m]>  https://www.reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/`
`[04-19-2023 17:05:47] <Rucknium[m]> Things have been quiet on the Mordinals front. Fewer than 50 Mordinals minted in the past week. I am now tracking Mordinal transfer transactions: https://gist.github.com/Rucknium/67cc9efdf7e43a40c52417611b322d43`
`[04-19-2023 17:06:23] <Rucknium[m]> According to my count, there have been 126 Mordinal transfer transactions`
`[04-19-2023 17:07:29] <Rucknium[m]> Considering only outputs from Mordinal minting transactions as black marbles, mean effective ring size is 15.88 as of yesterday.`
`[04-19-2023 17:08:16] <Rucknium[m]> That number will rise toward 16 asymptotically as time goes on unless many more Mordinals are minted.`
`[04-19-2023 17:08:21] <UkoeHB> plowsof: we are past Liam Eagen's self-imposed deadline, any news?`
`[04-19-2023 17:09:24] <vtnerd> Ive mainly focused on lws and serialization, but I am _finally_ shifting back to some bp++. going to be a bit I think`
`[04-19-2023 17:09:32] <vtnerd> koe what was the self-emposed deadline?`
`[04-19-2023 17:09:38] <vtnerd> was he working on the implementation instead?`
`[04-19-2023 17:11:52] <UkoeHB> vtnerd: he's updating the paper`
`[04-19-2023 17:12:55] <xmrack[m]> Hi`
`[04-19-2023 17:13:26] <Rucknium[m]> Could be that BP++ doesn't work.`
`[04-19-2023 17:14:38] <ofrnxmr[m]> <vtnerd> "koe what was the self-emposed..." <- The 14th`
`[04-19-2023 17:16:16] <UkoeHB> at least as late as feb 23rd he was employed by blockstream to work on it`
`[04-19-2023 17:16:23] <UkoeHB> 3. discussion`
`[04-19-2023 17:16:46] <ofrnxmr[m]> Rucknium @rucknium:monero.social:  did some analysis of the distribution of number of outputs in each decoy `
`[04-19-2023 17:19:29] <ofrnxmr[m]> I think very telling in for conversation of standardizing outputs.`
`[04-19-2023 17:19:29] <ofrnxmr[m]> 2 outs are in every decoy (though it seems there were 100 rings where there was only one 2 out decoy). 16 outs have the next highest prevalance and 3-15 are relatively rare `
`[04-19-2023 17:21:01] <Rucknium[m]> Here's the table: https://gist.github.com/Rucknium/0737163a980a07cf9c837700771d0dea`
`[04-19-2023 17:21:16] <Rucknium[m]> There are row >16 there I think because some outputs are selected from very old outputs without the 16 output limit.`
`[04-19-2023 17:21:20] <UkoeHB> is the incidence rate different from what you'd expect?`
`[04-19-2023 17:22:36] <ofrnxmr[m]> personally it was what i expected based on how people spend `
`[04-19-2023 17:22:36] <Rucknium[m]> UkoeHB: was that a question for me? If so, incidence rate of what?`
`[04-19-2023 17:24:27] <UkoeHB> Rucknium[m]: does the distribution in decoys match the expected distribution?`
`[04-19-2023 17:26:24] <Rucknium[m]> I expect it to roughly match the actual output-per-tx distribution on the chain. Since I don't know what that is (yet), it vacuously matches my expectations :)`
`[04-19-2023 17:26:37] <Rucknium[m]> I can produce the tables to see if it is close`
`[04-19-2023 17:26:46] <ofrnxmr[m]> (not technical answer) looks to me like it doesnt descriminate. Ie, looks to be in lin with real spending behavior, but with unlucky/lucky outliers (100 rings with only one 2 out, for example)`
`[04-19-2023 17:26:48] <UkoeHB> ah`
`[04-19-2023 17:28:20] <UkoeHB> are there any other topics we should discuss today?`
`[04-19-2023 17:28:29] <Rucknium[m]> I think ofrnxmr believes that outputs from 16-out txs are not credible decoys  (i.e. are black marbles)for rings that spend from 2-out txs. I am not convinced, but I will keep an open mind.`
`[04-19-2023 17:28:57] <ofrnxmr[m]> oh no`
`[04-19-2023 17:30:53] <ofrnxmr[m]> actually - id more think of them as.. grey.`
`[04-19-2023 17:30:53] <ofrnxmr[m]> they arent standout transactions, but they are obvious not-real-spends if say walmart is accepting xmr in person `
`[04-19-2023 17:33:03] <Rucknium[m]> If someone was paid an output in a batch tx from an exchange or mining pool and then spent that output to the merchant, it's the real spend. IMHO, these are credible decoys`
`[04-19-2023 17:33:48] <plowsof11> BP++: no updates since March 28th where April 14th was promised. no reply to an email sent on the 12th yet`
`[04-19-2023 17:34:09] <ofrnxmr[m]> If the tx the merchant recieves has fifteen 16 outs, and one 2 out, the real soend is clear`
`[04-19-2023 17:34:47] <Rucknium[m]> Yes, but only Mordinals do that. Deliberately.`
`[04-19-2023 17:35:32] <ofrnxmr[m]> The 100 on your chart are morbinals?`
`[04-19-2023 17:35:52] <Rucknium[m]> Mordinal transfer txs`
`[04-19-2023 17:36:33] <Rucknium[m]> I'm pretty sure. I said it in this channel a few days ago.`
`[04-19-2023 17:36:33] <ofrnxmr[m]> Yeah, but those 100 from this chart are confirmed to be morbinals? `
`[04-19-2023 17:36:33] <ofrnxmr[m]> ok. I thought it was an outlier `
`[04-19-2023 17:36:46] <ArticMine[m]> What is the typical tx size when mordinals are involved?`
`[04-19-2023 17:37:20] <Rucknium[m]> Mordinal minting? I can calculate the mean tx size. One moment`
`[04-19-2023 17:38:33] <Rucknium[m]> 370687101 / 43096 = 8601.427 bytes`
`[04-19-2023 17:39:20] <Rucknium[m]> Mordinal transfer txs:`
`[04-19-2023 17:39:26] <Rucknium[m]> 281030 / 126 = 2230.397 bytes`
`[04-19-2023 17:39:45] <ArticMine[m]> There is at least an opportunity for pricing if not looking at tx size limits `
`[04-19-2023 17:40:42] <ArticMine[m]> This is an issue l am looking at in a general sense `
`[04-19-2023 17:40:50] <ArticMine[m]> Tx size pricing and limits`
`[04-19-2023 17:42:03] <Rucknium[m]> The new version of the Mordinals software has a self-imposed fee policy. tx fee rises exponential with ex_extra size`
`[04-19-2023 17:42:22] <Rucknium[m]> Of course, people can just choose to run the old software and avoid the fee`
`[04-19-2023 17:42:23] <ArticMine[m]> That is actually good `
`[04-19-2023 17:42:29] <rbrunner> Yes, they even credit you, ArticMine[m], for the inspiration of the curve :)`
`[04-19-2023 17:43:06] <ArticMine[m]> ... but we can use node relay for this `
`[04-19-2023 17:49:39] <UkoeHB> I think we can end the meeting here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-04-18T19:09:07+00:00
- Closed at: 2023-04-25T15:59:05+00:00
