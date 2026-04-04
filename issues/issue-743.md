---
title: Monero Research Lab Meeting - Wed 19 October 2022
source_url: https://github.com/monero-project/meta/issues/743
author: Rucknium
assignees: []
labels: []
created_at: '2022-10-18T02:07:33+00:00'
updated_at: '2022-10-21T22:27:04+00:00'
type: issue
status: closed
closed_at: '2022-10-21T22:27:04+00:00'
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

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#740 

# Discussion History
## UkoeHB | 2022-10-19T17:57:30+00:00
`[10-19-2022 16:59:58] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/743`
`[10-19-2022 16:59:59] <UkoeHB> 1. greetings`
`[10-19-2022 16:59:59] <UkoeHB> hello`
`[10-19-2022 17:00:40] <hyc> hi`
`[10-19-2022 17:00:45] <rbrunner> Hello`
`[10-19-2022 17:00:58] <ArticMine[m]> Hi`
`[10-19-2022 17:01:19] <Rucknium[m]> Hi`
`[10-19-2022 17:01:42] <dangerousfreedom> Hello`
`[10-19-2022 17:01:42] <jberman[m]> hello`
`[10-19-2022 17:02:33] <UkoeHB> 2. updates, what's everyone working on?`
`[10-19-2022 17:02:35] <xmrack[m]> Hi`
`[10-19-2022 17:03:40] <jberman[m]> me: PR for background sync mode is incoming right after this meeting, then going to do some stress testing on monerod + @rbrunner's pool PR 8076, then jump into Seraphis`
`[10-19-2022 17:05:33] <Rucknium[m]> hyc completed his review of my OSPEAD estimator proposal. isthmus gave me partial feedback. So far, no major changes.`
`[10-19-2022 17:05:39] <UkoeHB> me: finished planned unit testing for balance recovery in a legacy-seraphis transition, wrote a serialization proof-of-concept for seraphis txs https://github.com/UkoeHB/monero/blob/seraphis_lib/tests/unit_tests/seraphis_serialization.cpp , started working on supporting legacy inputs to seraphis multisig txs (right now working on multisig key image recovery for legacy enotes, which could probably be PRd to master at `
`[10-19-2022 17:05:39] <UkoeHB> some point)`
`[10-19-2022 17:06:32] <dangerousfreedom> I'm working on my understanding of wallet2 and simplewallet and trying to create some logical reasoning of what is going on there.`
`[10-19-2022 17:06:54] <hyc> ^ nice. that's some srsly messy code.`
`[10-19-2022 17:07:33] <rbrunner> One more person understanding wallet2 is certainly a plus ...`
`[10-19-2022 17:09:38] <dangerousfreedom> :p`
`[10-19-2022 17:10:05] <UkoeHB> 3. discussion`
`[10-19-2022 17:10:18] <ArticMine[m]> I have been working on fess and following the ZCash attack. There are some changes that can be implemented as part of comprehensive fee and scaling updates. `
`[10-19-2022 17:11:31] <ArticMine[m]> I am moving back to OSPEAD`
`[10-19-2022 17:12:33] <ArticMine[m]> By the way the ZCash attack is continuing `
`[10-19-2022 17:14:50] <UkoeHB> btw, in case anyone missed it https://libera.monerologs.net/monero-dev/20221016#c151626 we can probably fit 2-3 more people without it getting too out of hand (7 devs + sgp attending right now)`
`[10-19-2022 17:15:40] <sgp[m]> Thanks for stepping up to schedule this :)`
`[10-19-2022 17:15:46] <hyc> as an aside: it appears the zcash attackers may have followed our discussions of the attack and improved their methods as a result`
`[10-19-2022 17:16:40] <rbrunner> Hmmm ... Isn't the idea "Just keep attacking" a bit trivial to come up with, even without our help?`
`[10-19-2022 17:16:54] <dangerousfreedom> UkoeHB: Really nice from you :)`
`[10-19-2022 17:17:07] <UkoeHB> sgp yep, somehow the seraphis lib got pretty big lol`
`[10-19-2022 17:17:21] <rbrunner> Yeah, such things happen :)`
`[10-19-2022 17:17:21] <hyc> rbrunner: one would think so, but then why didn't they just do that from the very beginning?`
`[10-19-2022 17:17:28] <ArticMine[m]> It may be the case but I have been discussing this kind of attack for over three years `
`[10-19-2022 17:17:57] <rbrunner> hyc: Good question`
`[10-19-2022 17:18:57] <UkoeHB> ArticMine[m]: any news about zcash planning mitigations?`
`[10-19-2022 17:19:37] <rbrunner> Maybe they just want to get Zcash improved with a non-brain-dead fee model, and when they saw that intermittent attacks do not yet inspire enough sense of urgence, they stepped up the attacks`
`[10-19-2022 17:19:47] <hyc> anyway sure it may all be coincidence, but the fact that their observed behavior changed within a couple days of our discussion seems to point that way`
`[10-19-2022 17:20:01] <monerobull[m]> They want to stop wallets allowing this stuff but only enforce it on protocol level "later"`
`[10-19-2022 17:20:01] <ArticMine[m]> I have not been following that. There is very little in the news`
`[10-19-2022 17:20:58] <ArticMine[m]> The observed behaviour chand around October 10th`
`[10-19-2022 17:21:05] <ArticMine[m]> Changed`
`[10-19-2022 17:21:18] <Rucknium[m]> UkoeHB: Yes. They have a ZIP to alter fees. They are going to change the block template RPC to give low-fee txs a lower probability of being added to a block (strange to me) to avoid forcing all wallet users to upgrade`
`[10-19-2022 17:21:46] <UkoeHB> in any case, it's a good reminder that just because an attack vector isn't being exploited right now, it always can be`
`[10-19-2022 17:22:34] <Rucknium[m]> https://github.com/zcash/zips/pull/631`
`[10-19-2022 17:23:23] <UkoeHB> Rucknium[m]: do they need a wallet upgrade to handle dynamic fees?`
`[10-19-2022 17:23:49] <ArticMine[m]> In my view they have a host of problems with their fee structure going back to Bitcoin. I simply do not know where to start `
`[10-19-2022 17:24:31] <rbrunner> Shhh, don't tell too much, they should take you as a highly paid consultant :)`
`[10-19-2022 17:24:51] <hyc> ;)`
`[10-19-2022 17:24:53] <Rucknium[m]> (My understanding of the Monero fee-blocksize relationship is incomplete) Are we sure that the Monero mining infrastructure (pool software, p2pool) will raise block size when fees spike suddenly? Have we seen it in the wild, in the current hardfork era? `
`[10-19-2022 17:25:40] <hyc> I think you have the causal relation backwards`
`[10-19-2022 17:25:55] <hyc> but yes we've seen the dynamic blocksize adjust as designed`
`[10-19-2022 17:25:56] <ArticMine[m]> We saw the proper behaviour just before the HF`
`[10-19-2022 17:26:14] <Rucknium[m]> UkoeHB: I am not 100% sure, but I would bet that many "third party" wallets have hard-coded the min fee per tx (of any size), which is one zat IIRC`
`[10-19-2022 17:26:15] <ArticMine[m]> Also back in 2017`
`[10-19-2022 17:26:21] <UkoeHB> Rucknium[m]: the block size constraints change automatically based on past block sizes; block sizes are pushed up if fees exceed the block reward penalty (and there are enough txs to exceed the median block size constraint)`
`[10-19-2022 17:27:39] <Rucknium[m]> Ok. Don't XMR miners have to "decide" to forgo some of the 0.6 XMR block reward to add the excess-size txs? It's not completely automatic, right?`
`[10-19-2022 17:28:00] <ArticMine[m]> The kind of massive super low fe tx would not get past node relay`
`[10-19-2022 17:28:11] <ArticMine[m]> Do starters `
`[10-19-2022 17:28:34] <ArticMine[m]> Fot`
`[10-19-2022 17:28:36] <sech1> Rucknium[m] p2pool goes above block size limit if there are enough transactions`
`[10-19-2022 17:29:19] <ArticMine[m]> ... and the proper fee is paid`
`[10-19-2022 17:29:39] <sech1> even if it's the lowest fee level, it can go up to 300k + 1000 bytes or so`
`[10-19-2022 17:29:44] <sech1> as I've seen in practice`
`[10-19-2022 17:30:35] <ArticMine[m]> Then the scaling begins with the rate depending on the fee paid `
`[10-19-2022 17:30:40] <UkoeHB> On this topic, I'd like to recapitulate my idea for upgrading how wallets select fees. Basically, wallets should estimate the confirmation delay for different incremental fee/weight ratios and present them to users in form fee/weight * tx weight (e.g. fee 0.002 = delay 5 blocks, fee 0.01 = delay 0 blocks), then users select which fee they want to pay.`
`[10-19-2022 17:31:08] <rbrunner> sech1: But you had to program this yourself after all, a dumb version of p2pool would not take part in pushing up the blocksize, if I understand correctly?`
`[10-19-2022 17:31:33] <sech1> no, any sane tx selection algorithm will push above block limit`
`[10-19-2022 17:31:50] <sech1> it will keep adding transactions as long as additional fee overweights the penalty`
`[10-19-2022 17:32:00] <sech1> and start from best fee/byte transactions`
`[10-19-2022 17:32:22] <rbrunner> Yes, that "tx selection algorithm" is inside your own code, and you could have built a very primitive version with hardcoded blocksize?`
`[10-19-2022 17:32:47] <sech1> why hardcode blocksize? monerod tells it`
`[10-19-2022 17:32:57] <sech1> p2pool does have the limit though`
`[10-19-2022 17:33:02] <sech1> it's 1000 tx per block currently`
`[10-19-2022 17:33:48] <rbrunner> I try to get a grasp on Rucknium's question: "It's not completely automatic, right?" Seems to me indeed it isn't all automatic.`
`[10-19-2022 17:33:56] <Rucknium[m]> rbrunner: This is the point I was making. Anyway, not a huge concern for spamming since a miner hardcode would limit chain bloat. But would also possibly frustrate users trying to get their txs confirmed`
`[10-19-2022 17:34:31] <ArticMine[m]> It is a very serious concern for scaling `
`[10-19-2022 17:34:40] <UkoeHB> Rucknium[m]: yes there is a block reward penalty when you exceed the median block size, which increases non-linearly as you go farther into the penalty zone; you only add a tx into the penalty zone if the new tx exceeds the penalty and removing any other other tx from the block won't improve the block reward`
`[10-19-2022 17:34:44] <ArticMine[m]> If this is true `
`[10-19-2022 17:35:43] <rbrunner> If different miners all have their own logic how they fill txs into blocks, and how many, *in theory* block growth could fail because of too-stupid such algorithms.`
`[10-19-2022 17:36:34] <ArticMine[m]> A mining pool can refuse to increase the blocksize but they would loose money doing this `
`[10-19-2022 17:37:15] <Rucknium[m]> This particular mechanism requires rational behavior on the part of miners. But maybe it was rational to take a coding shortcut :/ . Just raising the issue. Probably it is OK.`
`[10-19-2022 17:37:24] <hyc> in general, miners don't do any selection themselves. they let monerod select for them.`
`[10-19-2022 17:37:41] <UkoeHB> ArticMine[m]: if enough pools do it, they could force a fee market to arise which would increase rewards`
`[10-19-2022 17:38:04] <rbrunner> Ah yes, there is a call for that after all.`
`[10-19-2022 17:38:34] <ArticMine[m]> There is already a fee market `
`[10-19-2022 17:39:11] <ArticMine[m]> UkoeHB: You mean the Bitcoin scenario `
`[10-19-2022 17:39:18] <UkoeHB> Well, a fee market with fixed supply (i.e. if miners cap block size at the median`
`[10-19-2022 17:39:40] <Rucknium[m]> UkoeHB: Very good point. In the future it could be a nice idea to examine the incentives of miners to check whether they align with what was intended. There are various papers about PoW miners subverting the intention, even for fixed-blocksize chains`
`[10-19-2022 17:40:46] <ArticMine[m]> We need to understand first if this is happening and where. It is a very valid point`
`[10-19-2022 17:40:47] <UkoeHB> a competing pool could easily break that cartel by offering higher block rewards to miners though`
`[10-19-2022 17:41:03] <UkoeHB> er miner shares I guess`
`[10-19-2022 17:42:17] <ArticMine[m]> ... and the hashers would move there`
`[10-19-2022 17:42:20] <Rucknium[m]> This sounds a lot like an economics question :)`
`[10-19-2022 17:42:20] <Rucknium[m]> Industrial Organization, even.`
`[10-19-2022 17:42:39] <ArticMine[m]> It does `
`[10-19-2022 17:43:32] <UkoeHB> ArticMine[m]: yeah, and the supply of hash power might increase which would increase the marginal cost and might push the cartel miners into unprofitability (even though block rewards are nominally higher)`
`[10-19-2022 17:44:03] <rbrunner> I think I found the RPC version: COMMAND_RPC_GETBLOCKTEMPLATE`
`[10-19-2022 17:44:22] <hyc> yes`
`[10-19-2022 17:47:48] <UkoeHB> there is probably a certain percentage of tx volume that a cartel could block without the cartel being broken, but it's probably pretty small since switching pools is fairly simple for miners`
`[10-19-2022 17:48:40] <Rucknium[m]> Speaking of economics, last year Zcash hired some economists to develop their fee model for Zcash Shielded Assets, which do not exist yet. They didn't think to hire them to look at the fee model of ZEC  itself`
`[10-19-2022 17:49:01] <hyc> lol`
`[10-19-2022 17:49:09] <rbrunner> If renting hashpower somehow somewhere is cheaper than the income you get from blackmailing tx submitters into high fees by artificially small blocks, you win :)`
`[10-19-2022 17:49:17] <Rucknium[m]> Few miners switched when minexmr raised their fee though`
`[10-19-2022 17:49:52] <rbrunner> Needs pretty serious hashpower to work however ...`
`[10-19-2022 17:50:06] <UkoeHB> an example of 'small enough'`
`[10-19-2022 17:50:26] <ArticMine[m]> It would be a money loosing proposition for the cartel except if the bigger blocks increased by orphan rate`
`[10-19-2022 17:51:19] <ArticMine[m]> There was a paper way back by Peter Rizun on this`
`[10-19-2022 17:52:25] <ArticMine[m]> He is a BCH community member`
`[10-19-2022 17:53:06] <UkoeHB> anyway we are closing in on the end of the meeting, any last-minute questions/topics?`
`[10-19-2022 17:53:37] <ArticMine[m]> So there is an edge case where this can make senses `
`[10-19-2022 17:53:38] <Rucknium[m]> I will put this on the open research questions list.`
`[10-19-2022 17:53:40] <ArticMine[m]> I will look for it `
`[10-19-2022 17:56:34] <UkoeHB> ok seems like we are done, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-10-18T02:07:33+00:00
- Closed at: 2022-10-21T22:27:04+00:00
