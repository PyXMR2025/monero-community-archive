---
title: Monero Research Lab Meeting - Wed 26 April 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/830
author: Rucknium
assignees: []
labels: []
created_at: '2023-04-25T15:58:51+00:00'
updated_at: '2023-05-02T15:10:27+00:00'
type: issue
status: closed
closed_at: '2023-05-02T15:10:27+00:00'
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

#829 

# Discussion History
## UkoeHB | 2023-04-29T17:53:55+00:00
`[04-26-2023 17:03:57] <Rucknium[m]> UkoeHB: Meeting time :)`
`[04-26-2023 17:04:12] <ofrnxmr[m]> Greetings`
`[04-26-2023 17:04:30] <vtnerd> hi`
`[04-26-2023 17:07:27] <Rucknium[m]> I guess I will be temporary meeting chair`
`[04-26-2023 17:07:27] <Rucknium[m]> Updates, what is everyone working on?`
`[04-26-2023 17:07:57] <ofrnxmr[m]> Thanks Rucknium. `
`[04-26-2023 17:07:57] <ofrnxmr[m]> meeting agenda: `
`[04-26-2023 17:07:57] <ofrnxmr[m]> https://github.com/monero-project/meta/issues/830`
`[04-26-2023 17:08:29] <Rucknium[m]> Not much Mordinal activity. By my count, only two Mordinals have been minted in the last week. Zero Mordinal transfer txs in the last week: https://gist.github.com/Rucknium/67cc9efdf7e43a40c52417611b322d43`
`[04-26-2023 17:09:56] <Rucknium[m]> A seat has opened on the MAGIC Monero Fund committee. The committee has power to disburse about 300 XMR from its general fund for research and development projects: https://magicgrants.org/Special-Election-for-MAGIC-Monero-Fund-MajesticBank/`
`[04-26-2023 17:10:07] <Rucknium[m]> Apply to run if you are interested`
`[04-26-2023 17:10:11] <ofrnxmr[m]> ive just been testing / running jeffros coincase segregation pr: `
`[04-26-2023 17:10:11] <ofrnxmr[m]> https://github.com/monero-project/monero/pull/8815`
`[04-26-2023 17:11:57] <Rucknium[m]> I'm reviewing some proposed research of Overseer/EAE/EABE attack / churning. Does anyone have thoughts on what this type of research should cover? In other words, a formalization and what sort of aspects should not be simplified out of the problem?`
`[04-26-2023 17:13:16] <Rucknium[m]> Diego Salazar: Any updates about the BP++ paper now that there is the new version with math proofs?`
`[04-26-2023 17:14:13] <vtnerd> DiegoSalazar[m] ^ should ping`
`[04-26-2023 17:14:26] <ofrnxmr[m]> just a note on churning, datahoarder / p2pool has some tools to find likely owned inputs consolidations on p2pool.observer`
`[04-26-2023 17:14:27] <DiegoSalazar[m]> oh yah hi`
`[04-26-2023 17:14:48] <DataHoarder> for last likely ones https://p2pool.observer/sweeps`
`[04-26-2023 17:14:48] <ofrnxmr[m]> plowsof @plowsof:matrix.org:  pinging `
`[04-26-2023 17:14:50] <DiegoSalazar[m]> we'll have an hour estimate to you guys this week`
`[04-26-2023 17:14:57] <DataHoarder> you can lookup any transaction via https://p2pool.observer/transaction-lookup`
`[04-26-2023 17:15:26] <ofrnxmr[m]> Thank you DataHoarder: `
`[04-26-2023 17:15:39] <DataHoarder> I can provide data if desired, it's mostly flagging very certain ones but this could be expanded once I have more time`
`[04-26-2023 17:15:52] <plowsof11> Thanks Diego Salazar !`
`[04-26-2023 17:16:10] <Rucknium[m]> DataHoarder: Thanks. Do you have payout address data from the p2pool sidechains from the beginning? Or only recently?`
`[04-26-2023 17:16:52] <DataHoarder> for main p2pool, from early on but not beggining. for mini, since the beggining. older ones could be backfilled theoretically, using this same data. `
`[04-26-2023 17:17:19] <DataHoarder> some empty spots exist in between but same, can be filled with some heuristics. otherwise it's almost all the block data`
`[04-26-2023 17:18:06] <DataHoarder> 23528 blocks on main vs p2pool.io reported 23779 for main`
`[04-26-2023 17:18:26] <Rucknium[m]> Thanks. I think tests or classifications could be formalized. Would take some effort to do so.`
`[04-26-2023 17:18:48] <DataHoarder> 1763 blocks for mini vs 1763 on p2pool.io`
`[04-26-2023 17:19:00] <DataHoarder> + the old pre-fork chains that keep generating blocks`
`[04-26-2023 17:20:12] <DataHoarder> formalized test/classification would be great, also looking into doing backwards looks to what is the most likely of spends for a given output given all existing decoys - fine tune as it finds new data. Ping me if you want more info around this, also reachable on #p2pool-log (to not hog this meeting)`
`[04-26-2023 17:21:03] <plowsof11> as of this second, my peer lists public rpc nodes consist of  232 nodes not on v18.2.2 and 208 that have updated.. its about 50% for me personally `
`[04-26-2023 17:21:30] <Rucknium[m]> plowsof: Do you know that because you are sending test Mordinals?`
`[04-26-2023 17:22:10] <plowsof11> i send a bogus transaction, and the error returned contains the new field 'tx extra to big' `
`[04-26-2023 17:22:41] <plowsof11> attempt to broadcast a bogus raw tx*`
`[04-26-2023 17:23:40] <Rucknium[m]> Almost 50% is pretty good. Of course, it could be selection bias from your network neighbors`
`[04-26-2023 17:23:56] <Rucknium[m]> Can you test on mining pool nodes?`
`[04-26-2023 17:26:14] <plowsof11> would be better yes ^  data={"tx_as_hex": "did_you_update_lol"} , r = requests.post("http://node.monerodevs.org:18089/sendrawtransaction", json=data, timeout=10),if "tx_extra_too_big" in r.json():`
`[04-26-2023 17:26:31] <ofrnxmr[m]> would need the pools rpc addresses. `
`[04-26-2023 17:26:32] <ofrnxmr[m]> some have been collected, and some are publicly available.`
`[04-26-2023 17:26:32] <ofrnxmr[m]> hashvaults is even unrestricted 👀. `
`[04-26-2023 17:26:32] <ofrnxmr[m]> should be possibke to check a few of the big ones `
`[04-26-2023 17:27:46] <Rucknium[m]> I guess there is no guarantee that their public RPC node is the same version as their node they use to construct the blocks sent to client miners.`
`[04-26-2023 17:29:53] <ofrnxmr[m]> Likely a second node(s),like cake has many to load balance `
`[04-26-2023 17:29:54] <ofrnxmr[m]> http://nodes.hashvault.pro:18081/get_info`
`[04-26-2023 17:29:54] <ofrnxmr[m]> unrestricted though `
`[04-26-2023 17:30:15] <ofrnxmr[m]> I guess they can update and fix config in the same email`
`[04-26-2023 17:32:27] <merope> > <@ofrnxmr:monero.social> Likely a second node(s),like cake has many to load balance `
`[04-26-2023 17:32:27] <merope> > http://nodes.hashvault.pro:18081/get_info`
`[04-26-2023 17:32:27] <merope> > unrestricted though `
`[04-26-2023 17:32:27] <merope> I see a `"restricted": true,` and the version number is missing 🤔`
`[04-26-2023 17:32:48] <merope> Perhaps you're resolving to a different ip though, and that one is misconfigured?`
`[04-26-2023 17:33:15] <ofrnxmr[m]> plowsof just said the same. Definitely a geolocation thing`
`[04-26-2023 17:35:27] <Rucknium[m]> Anything else to discuss?`
`[04-26-2023 17:36:00] * ofrnxmr[m] uploaded an image: (114KiB) < https://libera.ems.host/_matrix/media/v3/download/monero.social/TSdQeaItypHHRgmWULAblwmW/fie1kq69ya7a3mhj.jpg >`
`[04-26-2023 17:36:33] <ofrnxmr[m]> Tevador opened a pr for randomx.. seems like it helps with wowneros recent chainsplit behavior`
`[04-26-2023 17:37:17] <Rucknium[m]> ofrnxmr: Do you know much about the wownero chainsplit? Why did it happen?`
`[04-26-2023 17:37:41] <ofrnxmr[m]> Hard fork split on spril 1`
`[04-26-2023 17:38:05] <ofrnxmr[m]> Chains diverged by 30+- blocks for the first few days`
`[04-26-2023 17:38:36] <ofrnxmr[m]> a few weeks in, nkdes were getting foked off onto a second chain`
`[04-26-2023 17:38:54] <ofrnxmr[m]> At one point they were 25 and 18 mh`
`[04-26-2023 17:39:24] <ofrnxmr[m]> Therr is still at least 2 chains mining, and at the sme hight`
`[04-26-2023 17:39:44] <Rucknium[m]> Both using the post-hardfork consensus rules?`
`[04-26-2023 17:40:44] <ofrnxmr[m]> i think wow may have messed up the hard fork (11.0 vs 11.0.1)`
`[04-26-2023 17:40:58] <merope> ofrnxmr[m]: See what ip address you get with dig or nslookup for that domain`
`[04-26-2023 17:41:25] <ofrnxmr[m]> But yeah, the old chain is using new consensus rules, but i think they updated late `
`[04-26-2023 17:41:27] <ofrnxmr[m]> The split* chains`
`[04-26-2023 17:42:45] <ofrnxmr[m]> Before i forget to link it, tevadors pr:`
`[04-26-2023 17:42:45] <ofrnxmr[m]> https://github.com/tevador/RandomX/pull/265`
`[04-26-2023 17:46:00] <Rucknium[m]> Ok. I don't fully understand what's happened. I hope Wownero community/devs can write a post-mortem when the problem is fixed.`
`[04-26-2023 17:47:36] <Rucknium[m]> Anything else?`
`[04-26-2023 17:48:14] <UkoeHB> ah fell asleep sorry, update is finishing up my 'implementing seraphis' companion paper`
`[04-26-2023 17:48:32] <ofrnxmr[m]> Thats all from me.`
`[04-26-2023 17:48:32] <ofrnxmr[m]> Thanks Ruck (and koe :P)`
`[04-26-2023 17:50:58] <UkoeHB> thanks Rucknium[m] `

# Action History
- Created by: Rucknium | 2023-04-25T15:58:51+00:00
- Closed at: 2023-05-02T15:10:27+00:00
