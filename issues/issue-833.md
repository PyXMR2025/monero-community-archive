---
title: Monero Research Lab Meeting - Wed 03 May 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/833
author: Rucknium
assignees: []
labels: []
created_at: '2023-05-02T15:10:15+00:00'
updated_at: '2023-05-09T16:09:41+00:00'
type: issue
status: closed
closed_at: '2023-05-09T16:09:41+00:00'
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

#830 

# Discussion History
## UkoeHB | 2023-05-03T17:51:12+00:00
`[05-03-2023 17:00:05] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/833`
`[05-03-2023 17:00:05] <UkoeHB> 1. greetings`
`[05-03-2023 17:00:05] <UkoeHB> hello`
`[05-03-2023 17:00:32] <Rucknium[m]> Hi`
`[05-03-2023 17:00:41] <shalit[m]> Hello`
`[05-03-2023 17:01:07] <vtnerd_> hi`
`[05-03-2023 17:01:14] <jeffro256[m]> Hello`
`[05-03-2023 17:03:56] <UkoeHB> 2. updates, what's everyone working on?`
`[05-03-2023 17:04:31] <UkoeHB> me: finished a draft of the 'implementing seraphis' paper https://github.com/UkoeHB/Seraphis and have been taking a break since then`
`[05-03-2023 17:04:46] <Rucknium[m]> Working on my Monerotopia talk: "A Statistical Research Agenda for Monero"`
`[05-03-2023 17:06:19] <vtnerd_> I was working on LWS unit-tests for webhooks and bp++`
`[05-03-2023 17:06:40] <vtnerd_> Im a little worried about delivering bp++ - the other implementation helps - I'll be able to give more guidance next week`
`[05-03-2023 17:07:07] <UkoeHB> vtnerd_: sounds good`
`[05-03-2023 17:08:18] <Rucknium[m]> vtnerd_: Thanks. What do you mean by "worried about delivering bp++"?`
`[05-03-2023 17:08:38] <vtnerd_> that I wont be able to complete the code`
`[05-03-2023 17:10:05] <Rucknium[m]> Ok. We are still at the stage of figuring out if BP++ is cryptographically sound, so the code implementation can be some time away.`
`[05-03-2023 17:10:07] <UkoeHB> 2. discussion`
`[05-03-2023 17:11:04] <Rucknium[m]> A month ago tevador asked to discuss MRL issue #100. Any takers?`
`[05-03-2023 17:12:12] <UkoeHB> I have no comments`
`[05-03-2023 17:12:28] <ghostway[m]> I'll probably be a lot less active, even more than I was, for the next 2 weeks. But I hope to then return and work on seraphis `
`[05-03-2023 17:12:32] <ghostway[m]> 2-3 weeks `
`[05-03-2023 17:12:42] <shalit[m]> same here`
`[05-03-2023 17:13:58] <jeffro256[m]> Rucknium[m]: Is there a specific requested topic or point to discuss regarding #100? `
`[05-03-2023 17:18:03] <Rucknium[m]> "MRL #100 should be added to the meeting agenda, so we can make some progress there."  https://libera.monerologs.net/monero-research-lab/20230302#c212397`
`[05-03-2023 17:18:21] <Rucknium[m]> That was two months ago`
`[05-03-2023 17:19:55] <Rucknium[m]> Are any trustless zk-SNARKs under a bounty program? I don't think there are any. Anyone know? (Zcash has no bug bounty program.)`
`[05-03-2023 17:19:56] <jeffro256[m]> I think most people agree that eventually Monero should eventually have a membership proof which captures all historical outputs. As I see it, the big question is should we work towards the big step of replacing Ed25519 with a prime order curves with Seraphis so that we could implement it in the future?`
`[05-03-2023 17:20:34] <jeffro256[m]> As opposed to keeping ed25519 with Seraphis and changing the address scheme again later `
`[05-03-2023 17:21:03] <Rucknium[m]> Or....the next step could be quantum-resistant ring signatures :)`
`[05-03-2023 17:22:30] <Rucknium[m]> ...which are less reviewed and battle-tested than trustless zk-SNARKs at this point`
`[05-03-2023 17:24:17] <kayabanerve[m]> The main issue with PQ schemes is the lack of composability.`
`[05-03-2023 17:25:25] <kayabanerve[m]> At this time, AFAIK, there really isn't the academia for PQ Seraphis`
`[05-03-2023 17:25:37] <kayabanerve[m]> jeffro256: It's not just prime order. It's a cycle.`
`[05-03-2023 17:26:15] <kayabanerve[m]> If we don't do it with Seraphis, we'd have to redo the migration. Why would anyone want that?`
`[05-03-2023 17:26:20] <jeffro256[m]> Yes, but composite order EC can never have cycles ;(`
`[05-03-2023 17:26:37] <kayabanerve[m]> And then tevador found a curve competitive with ed25519 which is prime order`
`[05-03-2023 17:26:47] <kayabanerve[m]> We have the academia to move commitments between curves`
`[05-03-2023 17:27:13] <jeffro256[m]> kayabanerve[m]: I tend to lean towards this, but it would add a lot of complexity `
`[05-03-2023 17:27:27] <kayabanerve[m]> Also, as for bounties, I'd have to check zkEVM setups. There are a lot of SNARK-based systems on Immunefi. There may be even been a STARK...`
`[05-03-2023 17:28:10] <jeffro256[m]> kayabanerve[m]: Which curve?`
`[05-03-2023 17:28:21] <kayabanerve[m]> 1) We add the new curve library`
`[05-03-2023 17:28:21] <kayabanerve[m]> 2) We use the COPZ DLog Eq proof`
`[05-03-2023 17:28:21] <kayabanerve[m]> That'd be the only immediate work`
`[05-03-2023 17:28:21] <kayabanerve[m]> (and f+r all ed25519 mentions in Seraphis)`
`[05-03-2023 17:28:28] <Rucknium[m]> There are a few PQ ring sig proposals: https://dl.acm.org/doi/10.1145/3319535.3354200`
`[05-03-2023 17:28:28] <Rucknium[m]> https://link.springer.com/chapter/10.1007/978-3-319-93638-3_32`
`[05-03-2023 17:28:42] <kayabanerve[m]> It's one of their candidates. I've been calling it tevone.`
`[05-03-2023 17:28:48] <Rucknium[m]> ^ AFAIK, they are not ready for production use`
`[05-03-2023 17:29:01] <kayabanerve[m]> (Because they didn't name their most recent recent three candidates, and I've been experimenting with Tevador #1)`
`[05-03-2023 17:29:37] <kayabanerve[m]> Rucknium @rucknium:monero.social: Horrible perf + doesn't fit under seraphis at this time.`
`[05-03-2023 17:32:50] <kayabanerve[m]> I'll also reiterate I don't believe tevadors indirect cycle is possible as we have to prove an EC OP on the tower yet membership on the cycle. I'm unsure we can feasibly maintain ZK through that`
`[05-03-2023 17:42:08] <UkoeHB> does anyone else have anything on their mind? otherwise we can call it here`
`[05-03-2023 17:45:48] <UkoeHB> ok thanks for attending everyone`
`[05-03-2023 17:46:31] <jeffro256[m]> thanks Ukoe`
`[05-03-2023 17:46:36] <kayabanerve[m]> 👋`

# Action History
- Created by: Rucknium | 2023-05-02T15:10:15+00:00
- Closed at: 2023-05-09T16:09:41+00:00
