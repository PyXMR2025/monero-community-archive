---
title: ' Monero Research Lab Meeting - Wed 16 February 2022 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/665
author: Rucknium
assignees: []
labels: []
created_at: '2022-02-15T05:13:35+00:00'
updated_at: '2022-02-19T17:12:06+00:00'
type: issue
status: closed
closed_at: '2022-02-19T17:12:06+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Fee policy and dynamic block size discussion for upcoming hard fork: https://github.com/monero-project/meta/issues/630 ; https://github.com/monero-project/monero/pull/7819 ; https://github.com/monero-project/research-lab/issues/70

3. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

4. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

5. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

6. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

7. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

10. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

11. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

12. Any other business

13. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#662 

# Discussion History
## ghost | 2022-02-16T04:49:57+00:00
i'd like to suggest taking a look at moneromooo's [output size reduction PR #8179](https://github.com/monero-project/monero/pull/8179) which greatly reduces the output file size by at least 2/3s to be able to fit on animated QRs for offline tx signing 


## ghost | 2022-02-16T16:13:31+00:00
Please discuss this topic of protecting from mining pools: https://github.com/monero-project/monero/issues/8181

## Rucknium | 2022-02-16T16:52:32+00:00
@jdefgh I expect that this will be discussed at the meeting.

## UkoeHB | 2022-02-16T17:57:47+00:00
```
[02-16-2022 17:00:10] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/665
[02-16-2022 17:00:11] <UkoeHB> 1. greetings
[02-16-2022 17:00:11] <UkoeHB> hello
[02-16-2022 17:00:31] <selsta> hi
[02-16-2022 17:00:34] <rbrunner> Hello
[02-16-2022 17:01:27] <jdefgh[m]> hi
[02-16-2022 17:03:24] <Rucknium[m]> Hi
[02-16-2022 17:04:16] <UkoeHB> it looks like jdefgh[m] has a proposal about pool mining to discuss https://github.com/monero-project/monero/issues/8181
[02-16-2022 17:04:25] <r4v3r23[m]> yo
[02-16-2022 17:04:30] <jdefgh> yes
[02-16-2022 17:05:09] <Rucknium[m]> Yes I think it would be a good time to brainstorm ideas for limiting mining pool centralization.
[02-16-2022 17:05:46] <selsta> banning pool mining has been discussed often in the past, it also was deployed on wownero, but it has downsides
[02-16-2022 17:06:16] <selsta> it doesn't help against botnets, it basically only makes it impossible for smaller miners to contribute to the network as they don't get any rewards for ages
[02-16-2022 17:06:37] <rbrunner> Yeah, I wonder how that propposal compares to what Wownero has live for a while
[02-16-2022 17:06:42] <Rucknium[m]> Previous discussion here:
[02-16-2022 17:06:42] <Rucknium[m]> https://libera.monerologs.net/monero-research-lab/20220120#c65308
[02-16-2022 17:06:45] <UkoeHB> It sounds like the idea is to sign block headers. Since EC operations are pretty expensive, I imagine that would allow ASICs to gain an advantage (one signature per nonce).
[02-16-2022 17:07:10] <sech1> EC operations are 4-5% of hash time in Wownero
[02-16-2022 17:07:39] <UkoeHB> wow that's a beefy hash then lol
[02-16-2022 17:08:33] <UkoeHB> is that like 1-5ms hash time?
[02-16-2022 17:08:50] <sech1> 1-2 ms, depending on CPU
[02-16-2022 17:09:00] <rbrunner> That's RandomX for you :)
[02-16-2022 17:11:17] <merope> Unless somebody figures out a p2pool implementation that work with nonce-signing, it's a no-go in my opinion
[02-16-2022 17:12:12] <Rucknium[m]> My question is whether anyone here has scoured the academic literature on this topic. There have definitely been papers published (and working papers uploaded but not technically published) on this topic. I did a quick search and found plenty.
[02-16-2022 17:13:47] <merope> There are 5-6 orders of magnitude of speed difference between a high-end cpu and the whole network. It would take somewhere between several months and several years for anyone mining on a single cpu to find a block. On average
[02-16-2022 17:14:18] <rbrunner> I think people differ widely how dire and bad they see the pool situation, with equally differing readiness to accept drastic solutions like this one
[02-16-2022 17:15:05] <merope> This is not sustainable for small miners who need to pay their power bills, while big mining farms/botnets would be unaffected
[02-16-2022 17:15:25] <merope> So it would both severely weaken the network and increase hashrate centralization
[02-16-2022 17:15:30] <rbrunner> I for one would jugde halving the network hashrate or so because of making mining harder a larger problem than that 50% pool right now
[02-16-2022 17:15:37] <selsta> It only punishes small miners.
[02-16-2022 17:16:13] <rbrunner> Destroying the village in order to save it, or how did that saying go?
[02-16-2022 17:16:46] <sech1> nonce-signing doesn't work with p2pool. You can't know secret keys of other miners to sign for them
[02-16-2022 17:16:57] <rbrunner> I think Wownero as a quite small coin were threatened in their viability, they might not have had a choice. We are not in the same situation.
[02-16-2022 17:17:34] <rbrunner> sech1: So did already think that through?
[02-16-2022 17:17:53] <sech1> all coinbase tx outputs must be signed with corresponding keys
[02-16-2022 17:17:57] <Rucknium[m]> So no one has looked deeply into the existing research on this? Maybe we should do that.
[02-16-2022 17:18:09] <sech1> even if 1 output is not signed, centralized pools can use that output to get block reward
[02-16-2022 17:18:14] <ArticMine> I believe we need to be very careful with any consensus change here
[02-16-2022 17:18:16] <Rucknium[m]> Maybe there is a paper out there that solves the problem that we don't know about.
[02-16-2022 17:18:19] <wowario[m]> correct. before the fork, one pool had over 70% of the network hash 
[02-16-2022 17:18:40] <rbrunner> Which problem exactly do you mean, Rucknium?
[02-16-2022 17:18:53] <merope> Rucknium: any interesting papers that you've found?
[02-16-2022 17:18:55] <Rucknium[m]> rbrunner: Mining pool centralization.
[02-16-2022 17:19:19] <rbrunner> So not making pools impossible, just keeping them from "centralizing".
[02-16-2022 17:20:01] <sech1> I just searched on google, and 4 out of 5 "How to mine Monero" guides mention minexmr as either a go-to pool or "one of popular pools"
[02-16-2022 17:20:33] <jdefgh[m]> the block reward system could be somehow modified to resemble p2pool's logic
[02-16-2022 17:20:35] <Rucknium[m]> endor00: Not anything that struck me as a silver bullet, but I just looked for a few minutes. I'm just saying that we shouldn't just rely on our own brainstorming to approach this.
[02-16-2022 17:20:46] <rbrunner> Yes, that's the result if you do good work for many years.
[02-16-2022 17:21:30] <sech1> there are a few pools that are arguably better than minexmr
[02-16-2022 17:22:05] <rbrunner> So more of a first / early mover advantage?
[02-16-2022 17:22:33] <sech1> yes, also many guides are copy/paste from many years ago, they just update the date to 2022
[02-16-2022 17:22:56] <Rucknium[m]> Something that would actually solve this is for mining pools to "voluntarily" establish an increasing pool operator fee if their share of hashrate got above a certain level. For example, 0-33% share of hashrate, set fee to 1% (or whatever). From 33% to 50% share of hashrate, set it to an exponential function rising from 1% to 100%.
[02-16-2022 17:23:24] <sech1> From 25%
[02-16-2022 17:23:28] <Rucknium[m]> That's the "economical" way to deal with it. Change the incentives for individual miners.
[02-16-2022 17:23:35] <sech1> or we can get two 33% pools that together can do 51%
[02-16-2022 17:23:42] <merope> hell, there are some copy-paste guides "updated to 2021" that still talked about mining Cryptonight using an RX480 using minergate
[02-16-2022 17:24:58] <Rucknium[m]> sech1: Sure. The exact parameters could be up for debate. Just use a sensible mining pool operator fee policy to push miners away from big pools. That's "voluntary" though.
[02-16-2022 17:24:59] <rbrunner> Usually, if you can't get to #1 on Google organically, you throw money at the problem and buy advertising. A CCS for p2pool ads on Google?
[02-16-2022 17:25:06] <merope> Rucknium: the problem with that system is that it would be completely voluntary, and miners would have an incentive to join a pool that doesn't implement such additional fees
[02-16-2022 17:25:32] <selsta> rbrunner: let's not feed google with money :D
[02-16-2022 17:25:41] <rbrunner> Just brainstorming :)
[02-16-2022 17:26:06] <rbrunner> Maybe less worse than murdering pool mining
[02-16-2022 17:26:41] <merope> The integration of p2pool in the gui wallet is a step in the right direction imo: reduce the barrier of entry to the point where it's just plain easier to do the right thing "by default" rather than having to do extra work
[02-16-2022 17:26:54] <merope> Which makes me think: why not include p2pool in xmrig instead?
[02-16-2022 17:27:05] <UkoeHB> Does hybrid PoS/PoW mitigate the issue?
[02-16-2022 17:27:25] <merope> Make it the default option, so that people would have to go out of their way to pick a different pool instead
[02-16-2022 17:27:39] <rbrunner> How do we stand with the xmrig dev(s), quite in general? Are they open for proposals?
[02-16-2022 17:27:44] <merope> And it wouldn't require keeping the wallet always open while mining
[02-16-2022 17:28:11] <sech1> integrating into xmrig doesn't make sense, you still need Monero node
[02-16-2022 17:28:31] <sech1> if you set up Monero node, you can just as well set up p2pool
[02-16-2022 17:28:40] <rbrunner> UkoeHB: PoS is quite a red flag for many people
[02-16-2022 17:28:45] <sech1> "do one thing and do it well" (c)
[02-16-2022 17:28:55] <merope> Right, but you don't need to run a third piece of software in addition to monerod (which you already have, because you need the wallet) and xmrig (which you already have, because you're mining)
[02-16-2022 17:29:33] <UkoeHB> rbrunner: I'm not well versed in the dynamics of PoS, just wondering if anyone knows how well it handles the 51% issue.
[02-16-2022 17:30:00] <sech1> If someone gets 51% in PoS, they will always have 51%
[02-16-2022 17:30:08] <merope> Keep in mind that the goal is reducing the entry barrier for people who barely know/understand anything about crypto - the same people who blindly join minexmr based on the first guide they found on the internet, because they don't know any better
[02-16-2022 17:30:19] <UkoeHB> There are really only three options for consensus: PoW, PoS, federated Byzantine agreement (SCP or similar). All have relative pros/cons.
[02-16-2022 17:30:33] <sech1> actually, half of minexmr hashrate comes from HUGE whale miners
[02-16-2022 17:30:37] <sech1> I'm talking 100+ MH/s
[02-16-2022 17:30:38] <merope> (The same people who have significant difficulties even running their own node, or need handholding while setting up xmrig)
[02-16-2022 17:30:47] <sech1> why they don't mine solo, I have absolutely no idea
[02-16-2022 17:30:57] <merope> Well, yes, there's that too
[02-16-2022 17:31:25] <merope> But botnets like using public pools because there are no traces leading back to them that way
[02-16-2022 17:32:07] <merope> And some botnet operators are just skiddies who figured out how to download "silentxmr" from github or whatever, so their technical skills are quite limited
[02-16-2022 17:32:27] <rbrunner> In any case p2pool is so new it barely had a good chance to improve the situation. And yet, it's already the 4th largest pool.
[02-16-2022 17:33:03] <rbrunner> I as the CEO of Monero would pour time and energy first into pushing that, before I burry the pools ...
[02-16-2022 17:34:23] <Rucknium[m]> Are we aware of this paper? "Nonoutsourceable Scratch-Off Puzzles to Discourage Bitcoin Mining Coalitions"
[02-16-2022 17:34:23] <Rucknium[m]> https://dl.acm.org/doi/abs/10.1145/2810103.2813621
[02-16-2022 17:35:12] <wowario[m]> how about increasing the cost of running a mega pool by increasing the hashing blob size? 
[02-16-2022 17:37:34] <sech1> we can't increase to more than what get_block_template returns
[02-16-2022 17:37:37] <rbrunner> That cost would be proportional basically to the number of miners?
[02-16-2022 17:37:40] <UkoeHB> wowario[m]: I'm not sure that fundamentally changes anything. Blob size is a per-miner cost, so increasing the size just pushes out marginal miners.
[02-16-2022 17:37:41] <sech1> this is 1-5 KB
[02-16-2022 17:39:20] <jdefgh[m]> Changing parameters isn't really going to change much. The affected miners would just keep mining and the distribution would be affected only slightly
[02-16-2022 17:39:20] <rbrunner> So everybody has more communication, not only mega pools
[02-16-2022 17:41:36] <UkoeHB> We are pretty far along in the meeting now. Are there any other topics people want to bring up? It seems we are getting pretty close to ready for the next HF.
[02-16-2022 17:42:05] <UkoeHB> maybe is h4sh3d around to give an update on 7877 review?
[02-16-2022 17:46:31] <Rucknium[m]> A while ago I brought up the idea of having a collaborative repository of papers about Monero. I think I may have found some open source software that could do it:
[02-16-2022 17:46:31] <Rucknium[m]> https://wikindx.sourceforge.io/web/trunk/
[02-16-2022 17:46:55] <Rucknium[m]> Anyone with any experience with WIKINDX or a similar system? Any comments on the matter?
[02-16-2022 17:49:04] <UkoeHB> sure, if you get it set up I can help add papers
[02-16-2022 17:50:11] <r4v3r23[m]> i'd like to bring attention to #8179, AirGap team is keen on building a QR standard for monero offline txs and this is PR goes along way in making that possible
[02-16-2022 17:50:19] <r4v3r23[m]> https://github.com/monero-project/monero/pull/8179
[02-16-2022 17:51:44] <rbrunner> Must have a look how that amazing reduction was achieved ...
[02-16-2022 17:52:04] <UkoeHB> would be nice to have a summary of changes in the PR...
[02-16-2022 17:52:39] <r4v3r23[m]> reduces the output file sizes drastically so they can fit on animated QR codes
[02-16-2022 17:52:51] <UkoeHB> that's the outcome, not the change
[02-16-2022 17:53:29] <rbrunner> Either you are from the inner circle, or you are not :)
[02-16-2022 17:53:50] <r4v3r23[m]> this is mooo's work, ive just been testing it on random wallets
[02-16-2022 17:56:55] <UkoeHB> ok seems like we are done; thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-02-15T05:13:35+00:00
- Closed at: 2022-02-19T17:12:06+00:00
