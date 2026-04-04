---
title: Monero Research Lab Meeting - Wed 12 October 2022
source_url: https://github.com/monero-project/meta/issues/740
author: Rucknium
assignees: []
labels: []
created_at: '2022-10-11T13:51:14+00:00'
updated_at: '2024-04-02T17:27:54+00:00'
type: issue
status: closed
closed_at: '2022-10-18T02:07:42+00:00'
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

#739 

# Discussion History
## UkoeHB | 2022-10-12T18:05:59+00:00
`[10-12-2022 16:59:49] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/740`
`[10-12-2022 16:59:49] <UkoeHB> 1. greetings`
`[10-12-2022 16:59:49] <UkoeHB> hello`
`[10-12-2022 17:00:13] <hyc> hi`
`[10-12-2022 17:00:18] <rbrunner> Hello`
`[10-12-2022 17:01:01] <Rucknium[m]> Hi`
`[10-12-2022 17:01:01] <one-horse-wagon[> Hello.`
`[10-12-2022 17:01:44] <ArticMine[m]> Hi`
`[10-12-2022 17:02:56] <UkoeHB> 2. updates, what's everyone working on?`
`[10-12-2022 17:05:03] <dangerousfreedom> Hello. I'm still going on through all the math equations in Seraphis and working on the audits framework.`
`[10-12-2022 17:05:19] <dangerousfreedom> s/on//`
`[10-12-2022 17:05:46] <Rucknium[m]> Modifying OpenSats to make a fundraising campaign system for MAGIC (despite not knowing web dev 😶): https://github.com/MAGICGrants/opensatswebsite . I am also happy to report that current MAGIC Monero Fund reserves are at 57,000 USD equivalent. That gives us a good buffer for grants so we don't get wiped out from a single grant. Thanks donors, whoever you are.`
`[10-12-2022 17:06:55] <UkoeHB> me: I got distracted learning about thread pools and concurrent program design for most of the last week (slightly related to monero at least, since I want to figure out the best way to do balance recovery in the background using the current seraphis balance recovery model). In the middle of unit testing balance recovery for the legacy-seraphis transition. Full-featured robust legacy balance recovery has a lot of `
`[10-12-2022 17:06:55] <UkoeHB> annoying edge cases...`
`[10-12-2022 17:08:14] <rbrunner> Looking at the code I had a feeling it's possible you are more robust there than `wallet2` itself ...`
`[10-12-2022 17:08:51] <ArticMine[m]> I have been looking at the cost of the ZCash spam attack in Monero`
`[10-12-2022 17:09:03] <UkoeHB> Well a lot of the edge cases don't show up in practice, because real-world reorgs are pretty benign.`
`[10-12-2022 17:10:44] <rbrunner> ArticMine: Is that ongoing, or do you have estimates already?`
`[10-12-2022 17:11:40] <ArticMine[m]> It is ongoing but I do have some estimates. `
`[10-12-2022 17:12:22] <UkoeHB> 3. we can move to discussion`
`[10-12-2022 17:13:55] <SerHack> Hi! :)`
`[10-12-2022 17:14:30] <UkoeHB> ArticMine[m]: any you'd care to share, or want to hold off until you have a conclusion?`
`[10-12-2022 17:14:55] <Rucknium[m]> IMHO, a good medium-term goal would be to perform a scaling stress test on a private testnet. I don't think it has been done recently. If it had been done a year ago or more, it would have caught the integer truncation bug that jberman  found by code inspection.`
`[10-12-2022 17:15:10] <Rucknium[m]> BCH did one recently: https://bitcoincashresearch.org/t/assessing-the-scaling-performance-of-several-categories-of-bch-network-software/754`
`[10-12-2022 17:15:58] <hyc> so we need an automated wallet to generate txns as fast as possible?`
`[10-12-2022 17:17:05] <Rucknium[m]> Yes. And/or spoof system time. xmrack has a tx spammer`
`[10-12-2022 17:17:15] <rbrunner> jberman told me that he wants to do something at least in the general direction of that shortly`
`[10-12-2022 17:17:15] <hyc> we would also need testnet nodes over some distantly connected networks. these tests are easy to boost on a single high end server`
`[10-12-2022 17:17:58] <rbrunner> E.g. building up a very large mempool and see how management code will react to that, to find bottlenecks`
`[10-12-2022 17:18:50] <rbrunner> This should then also be able to show that my PR #8076 is indeed an improvement and does not get victim of one of those bottlenecks - if they exist`
`[10-12-2022 17:19:14] <Rucknium[m]> xmrack 's stagenet spamming already found a small bug in RPC calls when the mempool was very large`
`[10-12-2022 17:20:05] <rbrunner> I just have a gut feeling that good and realistic stress tests won't come cheap.`
`[10-12-2022 17:20:15] <rbrunner> Those probably mean work :)`
`[10-12-2022 17:20:37] <ArticMine[m]> Ramping up the short term median to the equivalent of the ZCash max blocksize can be around 50-70 K USD . If the attack is stopped for more than 100 min then the median resets, and the spammer has to start again. `
`[10-12-2022 17:20:37] <ArticMine[m]> So the start and stop approach of the ZCash  spammer gets very expensive. `
`[10-12-2022 17:21:05] <Rucknium[m]> This was the bug: https://github.com/monero-project/monero/pull/8388`
`[10-12-2022 17:21:31] <hyc> rbrunner: there's only a few dimensions of potential bottleneck. the main point is using realistic test hardware, and the time required to run a test`
`[10-12-2022 17:24:43] <one-horse-wagon[> Wouldn't 4 or 5 decent computers, spread around the U.S. and Europe, running day and night for a month do a good stress test?`
`[10-12-2022 17:26:14] <hyc> they can be load generators, sure. you also need some simulated users who can actually see the impact, e.g. if it slows down their UX`
`[10-12-2022 17:27:47] <ArticMine[m]> The ZCash approach is far from optimal to attack Monero.`
`[10-12-2022 17:27:47] <ArticMine[m]> I am more concerned with a maintenance attack where the short term median is maintained rather than grown. This is tricky because if the attack is stopping for over 100 min the median resets. `
`[10-12-2022 17:27:47] <ArticMine[m]> So I am looking at ways to further harden against a maintenance attack.`
`[10-12-2022 17:28:32] <hyc> raises the question of why the zcash spammer pauses instead of running continuously`
`[10-12-2022 17:28:50] <rbrunner> As far as I know the biggest impact of the Zcash attack is rendering some wallets pretty much non-functional because they are not up to the task to process those "monster" transactions`
`[10-12-2022 17:28:55] <rbrunner> and not in the numbers they occur`
`[10-12-2022 17:29:04] <rbrunner> I think blockchain bloat is not their main problem, by far`
`[10-12-2022 17:29:08] <hyc> but whatever, assume someone attacking monero will know about the median time constraints`
`[10-12-2022 17:29:18] <UkoeHB> maybe the zcash guy needs to take breaks to rearrange funds`
`[10-12-2022 17:29:35] <ArticMine[m]> Very good point. There is no reason for the ZCash spammer to do this `
`[10-12-2022 17:30:06] <ArticMine[m]> ... but it is a very strong defense for Monero`
`[10-12-2022 17:31:09] <rbrunner> I have read as a short-time bandaid some wallets have stopped to even look at transactions with more than 20 or 50 outputs ...`
`[10-12-2022 17:31:23] <ArticMine[m]> hyc: Of course which is why I am looking at maintenance `
`[10-12-2022 17:32:04] <monerobull[m]> rbrunner: Jup. Their most popular wallets use the official SDK though, which i think hasn't been updated yet`
`[10-12-2022 17:32:23] <Rucknium[m]> The 10 block lock also makes things more difficult for a spammer, but that's something that can be overcome.`
`[10-12-2022 17:33:28] <rbrunner> Yes, where Zcash is more or less begging to get spammed, Monero already has several defenses in place, and altogether certainly does not look like an easy victim`
`[10-12-2022 17:33:32] <ArticMine[m]> monerobull[m]: In Monero the limit is 16 outputs except for coinbase `
`[10-12-2022 17:34:32] <rbrunner> Of course we still should try to improve, no doubt`
`[10-12-2022 17:34:36] <monerobull[m]> ArticMine[m]: Does that mean i could have coins i don't know about `
`[10-12-2022 17:34:36] <one-horse-wagon[> Rucknium[m]: Doesn't the 10 block lock only apply to a single wallet?  A spammer could use the network to tx many wallets, one right after the other, couldn't he?`
`[10-12-2022 17:35:02] <sech1> but coinbase can have unlimited outputs, so a dedicated spammer can solo mine blocks with ~7700 outputs per block`
`[10-12-2022 17:35:05] <sech1> and then use these outputs`
`[10-12-2022 17:35:16] <monerobull[m]> one-horse-wagon[: You also need to fill those wallets first`
`[10-12-2022 17:35:21] <sech1> 300k / 39 ~ 7700 (one output is 39 bytes on average)`
`[10-12-2022 17:36:58] <UkoeHB> hmm, with the advent of p2pool it might be worthwhile for scanning to have an 'ignore coinbase' toggle`
`[10-12-2022 17:37:19] <rbrunner> I think wallet2 has this? Not sure.`
`[10-12-2022 17:37:27] <sech1> wallet2 already has this toggle`
`[10-12-2022 17:37:31] <UkoeHB> oh`
`[10-12-2022 17:37:48] <sech1> set refresh-type = ...`
`[10-12-2022 17:37:50] <sech1> in CLI wallet`
`[10-12-2022 17:37:58] <rbrunner> Right, that was it`
`[10-12-2022 17:37:59] <UkoeHB> TIL`
`[10-12-2022 17:38:38] <sech1> set refresh-type = no-coinbase`
`[10-12-2022 17:38:47] <Rucknium[m]> one-horse-wagon: Yes. No "too" difficult. But it bumps the difficulty up a bit for a weekend warrior hacker`
`[10-12-2022 17:42:26] <monerobull[m]> A big percentage of Lightning went down this week to a 998/999 multisig transaction. Our multisig is limited to like 100, right?`
`[10-12-2022 17:42:45] <UkoeHB> monerobull[m]: 16, and it is all off-chain`
`[10-12-2022 17:43:01] <ArticMine[m]> <sech1> "300k / 39 ~ 7700 (one output is..." <- Interesting but then the spammer is not able to sustain the attack. So we are back to resetting the median `
`[10-12-2022 17:43:31] <monerobull[m]> Would this fall under scriptless script?`
`[10-12-2022 17:43:34] <UkoeHB> I think you can get to 30-60 group members with FROST-style key gen (kayabaNerve ?)`
`[10-12-2022 17:43:53] <rbrunner> As I saw with my TechWallet, if you constantly send transactions with many outputs to yourself, in a few hours you can rack up hundreds of outputs easily`
`[10-12-2022 17:43:55] <Rucknium[m]> monerobull: I think that was basically due to an outdated configuration on an "alternative" BTC node implementation. It wasn't a computational bottleneck. But it does once again point to risks with multiple node implementations.`
`[10-12-2022 17:44:41] <rbrunner> But you will spend then all in a burst attack of sorts, and then it's back to square 1`
`[10-12-2022 17:44:50] <hyc> was reported here https://decrypt.co/111642/enormous-multi-sig-transaction-briefly-crashes-bitcoins-lightning-network`
`[10-12-2022 17:45:21] <sech1> ArticMine[m] why would the spammer be unable to sustain it? If he has enough hashrate to mine blocks, he can mine any size block containing only coinbase outputs, and use them for blocks that he doesn't mine.`
`[10-12-2022 17:48:00] <sech1> actually, 0.6 XMR is enough only for ~3600 1in/2out transactions with current fees...`
`[10-12-2022 17:48:28] <monerobull[m]> Escapethe3r, since you're reading this for your writeup anyways: the write-ups are great, keep em coming :) also agree with retiring TA reports in favor of other content `
`[10-12-2022 17:48:38] <ArticMine[m]> It comes down to the rate of tx generating vs percentage of total hashrate under the spammer's control`
`[10-12-2022 17:48:38] <ArticMine[m]> On can estimate this `
`[10-12-2022 17:49:07] <sech1> my math was wrong, it's enough for ~19500 transactions`
`[10-12-2022 17:49:39] <ArticMine[m]> Per mined block `
`[10-12-2022 17:49:59] <ArticMine[m]> So a stockpiling attack?`
`[10-12-2022 17:50:23] <sech1> what's that?`
`[10-12-2022 17:50:58] <sech1> I can imagine an attacker mining a block and submitting 7.7k transactions to mempool right after that. And again and again`
`[10-12-2022 17:51:22] <ArticMine[m]> The attacker first builds up a supply of outputs `
`[10-12-2022 17:51:30] <ArticMine[m]> Then uses the stockpile to attack `
`[10-12-2022 17:51:42] <sech1> oh btw, coinbase outputs are locked for 60 blocks`
`[10-12-2022 17:52:03] <sech1> so if such attacks ever happens, there's 2 hours advance notice`
`[10-12-2022 17:52:16] <rbrunner> Lol. Cutting it close :)`
`[10-12-2022 17:52:25] <UkoeHB> sech1: would be nice to remove that for seraphis https://github.com/monero-project/research-lab/issues/104`
`[10-12-2022 17:52:29] <monerobull[m]> sech1: Isn't this whole PoW thing an incentive mechanism to... Not do that`
`[10-12-2022 17:52:43] <monerobull[m]> sech1: Emergency hardfork every time`
`[10-12-2022 17:53:37] <ArticMine[m]> This is a good reason to leave the coinbase lock time alone or even increase it`
`[10-12-2022 17:54:15] <sech1> yes, solely because coinbase can have unlimited number of outputs`
`[10-12-2022 17:54:16] <UkoeHB> I don't the coinbase lock time helps at all with this`
`[10-12-2022 17:55:18] <ArticMine[m]> Also coinbase is not private. So good old censorship becomes a defense`
`[10-12-2022 17:55:25] <rbrunner> All it does is shifting the attack 2 hours into the future *once*?`
`[10-12-2022 17:55:38] <UkoeHB> if the attacker is periodically making blocks, it doesn't matter whether their coinbase outputs are 10 blocks old or 1000 blocks old, either way once the setup period is over the rate they can spend outputs is the same`
`[10-12-2022 17:56:37] <monerobull[m]> Not if you increase lock time to infinity 😅`
`[10-12-2022 17:56:38] <hyc> true, so for this it is irrelevant. but a the lock time is a good defense against spending outputs that disappear due to a reorg`
`[10-12-2022 17:57:30] <ArticMine[m]> Yes there is advance notice of attack and which outputs are going to be used `
`[10-12-2022 17:58:09] <rbrunner> Hmm, sure, but will this knowledge give you advantages as a defender?`
`[10-12-2022 17:59:49] <sech1> if outputs are used in 1in/2out, it's hard to filter them out because of decoys`
`[10-12-2022 18:00:00] <ArticMine[m]> In any case the attacker has to build up an arsenal of outputs that are not private and is therefore a target for the defense `
`[10-12-2022 18:00:02] <sech1> so no, scrap this`
`[10-12-2022 18:00:33] <hyc> feels like this discussion is getting lost in the weeds`
`[10-12-2022 18:01:19] <UkoeHB> if anything, there should be a bonus weight on coinbase outputs to account for the network costs, if they are considered problematic`
`[10-12-2022 18:01:23] <ArticMine[m]> Yes `
`[10-12-2022 18:02:10] <UkoeHB> although that would work at cross-purposes to p2pool, a hard design balance`
`[10-12-2022 18:03:32] <UkoeHB> anyway, we are at the end of the hour I so I think we can close out the meeting; thanks for attending everyone`
`[10-12-2022 18:04:03] <hyc> thanks UkoeHB for facilitating`

# Action History
- Created by: Rucknium | 2022-10-11T13:51:14+00:00
- Closed at: 2022-10-18T02:07:42+00:00
