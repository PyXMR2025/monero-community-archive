---
title: Monero Research Lab Meeting - Wed 02 February 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/657
author: Rucknium
assignees: []
labels: []
created_at: '2022-01-29T18:14:21+00:00'
updated_at: '2022-02-05T23:49:03+00:00'
type: issue
status: closed
closed_at: '2022-02-05T23:49:03+00:00'
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

#654 

# Discussion History
## UkoeHB | 2022-02-02T18:06:10+00:00
```
[02-02-2022 17:00:44] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/657
[02-02-2022 17:00:45] <UkoeHB> 1. greetings
[02-02-2022 17:00:45] <UkoeHB> hello
[02-02-2022 17:00:49] <ArticMine> Hi
[02-02-2022 17:00:55] <selsta> hi
[02-02-2022 17:00:58] <rbrunner> Hi there
[02-02-2022 17:01:55] <netrik182> hi
[02-02-2022 17:02:09] <jberman[m]> hello
[02-02-2022 17:02:12] <Rucknium[m]> Hi
[02-02-2022 17:02:37] <carrington[m]> Salutations
[02-02-2022 17:02:44] <mj-xmr[m]> Buenos
[02-02-2022 17:02:55] <Scalability> días.
[02-02-2022 17:03:42] <UkoeHB> Today we should focus on fee changes for the upcoming hardfork (and also look into the future). I summarized two concerns here: https://github.com/monero-project/research-lab/issues/70#issuecomment-1024964432
[02-02-2022 17:05:01] <UkoeHB> It sounds like ArticMine agreed to reduce the long term scaling factor from 1.4x -> 2x to 1.4x -> 1.7x (this is maximum growth over 69 days).
[02-02-2022 17:05:17] <ArticMine> Yes that is correct https://github.com/monero-project/research-lab/issues/70#issuecomment-1025334284
[02-02-2022 17:05:19] <UkoeHB> reduce the upcoming change*
[02-02-2022 17:05:46] <ArticMine> sgp value of 1.7 as a compromise
[02-02-2022 17:06:48] <ArticMine> Then we can find consensus for the subsequent HF
[02-02-2022 17:07:06] <UkoeHB> Yes I think that is fine.
[02-02-2022 17:07:32] <carrington[m]> Overall I think 1.7 is a decent compromise for the growth rate, but I think the sanity check hardcap on blocksize should be lowered to something with a basis in reality (like jberman  calculated)
[02-02-2022 17:07:56] <carrington[m]> Also fees should be higher in general
[02-02-2022 17:09:00] <ArticMine> <carrington[m]> Overall I think 1.7 is a decent compromise for the growth rate, but I think the sanity check hardcap on blocksize should be lowered to something with a basis in reality (like jberman  calculated) <--- there are ways of dealing with this without hard coding obsolescence into consensus 
[02-02-2022 17:09:18] <UkoeHB> ArticMine: what is your response to the stability concern I raised?
[02-02-2022 17:11:07] <ArticMine> There are many way to deal with this including effectivly pricing the upload bandwidth of nodes. This doe not require consensus 
[02-02-2022 17:11:33] <jberman[m]> There is a point at which you can't retroactively solve for a chain that has grown too large to verify and sync on commodity hardware, that imo is the only way to lead to obsolescence
[02-02-2022 17:11:35] <Rucknium[m]> Do we still lack an estimate for the cost of a deliberate maximal blockchain-bloating spam incident?
[02-02-2022 17:12:06] <carrington[m]> Yeah long term nodes "catching up" wouldn't be a problem if we had some kind of disposable history, but for now considering there is already a hardcoded sanity check I think tweaking it isn't a permanent problem
[02-02-2022 17:12:11] <UkoeHB> yes it is lacking (I could do it, but I am busy with seraphis... any takers?)
[02-02-2022 17:13:39] <jberman[m]> I can take it on if there are no other takers, seems to be priority #1 for the fork at this point + I'm looking deeper into the fee changes at this point now anyway
[02-02-2022 17:14:07] <ArticMine> Spam costing is something I am prepared to do but not in a rust before the next HF
[02-02-2022 17:14:18] <ArticMine> This is the point of the compromise
[02-02-2022 17:14:36] <UkoeHB> ArticMine: yes, there are ways to improve the performance of nodes. However, those methods aren't a 'solution', they are only a 'bandaid' to the basic problem. The basic problem is unbounded block size growth _cannot_ be supported by casual users (at some point only server centers can handle the load).
[02-02-2022 17:14:48] <carrington[m]> What do you mean by "pricing the upload speed of nodes"?
[02-02-2022 17:15:21] <ArticMine> Prioritizing transactions for relay based upon the fee
[02-02-2022 17:15:43] <rbrunner> Aka fee market?
[02-02-2022 17:15:44] <ArticMine> while keeping the number of broadcast nodes constant
[02-02-2022 17:16:14] <ArticMine> For low bandwidth nodes this effectivly created a fee market
[02-02-2022 17:16:43] <UkoeHB> What does a low bandwidth node do if it gets a huge valid block from a mining pool?
[02-02-2022 17:16:51] <UkoeHB> It just falls behind and oh well?
[02-02-2022 17:16:56] <ArticMine> Keep in mind that many internet connections can ahve a 30x difference in upload and download bandwith
[02-02-2022 17:17:26] <ArticMine> and a Monero node needs easily 12x as more upload than download bandwith
[02-02-2022 17:17:39] <jberman[m]> Bandwidth isn't the issue in my calculations: https://github.com/monero-project/research-lab/issues/70#issuecomment-1027806393
[02-02-2022 17:18:32] <jberman[m]> even if you assume 0 cost bandwidth (aka infinite mb/s upload and download), the time to verify + storage requirements to run a pruned node that verifies the chain would eventually get too large 
[02-02-2022 17:18:51] <ArticMine> ^ I have serious doubts with that. Batch verification is something that can be run in parallel
[02-02-2022 17:18:53] <LyzaL> time for blocks to propogate increases orhphans no? 5-10 sec block upload time seems not great even if other hardware reqs are there - how long does it take a block to fully propogate in that situation?
[02-02-2022 17:19:20] <carrington[m]> I think verification is the issue more than bandwidth?
[02-02-2022 17:19:21] <UkoeHB> ArticMine: this is as much a theoretical problem as it is a numerical one.
[02-02-2022 17:19:22] <jberman[m]> the time to verify is divided by 8, the number of threads on my machine. parallelism is accounted for
[02-02-2022 17:19:24] <ArticMine> There mare solutioon here that de not involve hard caps
[02-02-2022 17:19:42] <Rucknium[m]> I can review jberman 's work and/or work with him on spam cost estimation. 
[02-02-2022 17:20:47] <UkoeHB> LyzaL: that's a good point, since dandelion++ increases propagation time
[02-02-2022 17:20:51] <ArticMine> I just do not see the argument to run verification on a single thread if there are many txs
[02-02-2022 17:21:38] <rbrunner> I wonder how high we would like to see fees for extreme scenarious to feel save. Even with 10s of thousands of USD you could still fear a dedicated enemy with deep pockets.
[02-02-2022 17:21:42] <ArticMine> If the orphan rate increase then mines will require higher fee. There is exisitng reserach on the fpor Bitcoin / Bitcoin cash
[02-02-2022 17:21:45] <jberman[m]> the numbers don't assume verification is running on a single thread
[02-02-2022 17:22:07] <ArticMine> ^ It is critcal to clarifit this
[02-02-2022 17:22:12] <ArticMine> clarify
[02-02-2022 17:22:49] <carrington[m]> On one hand, solutions against a big bang attack in issue 70 already depend on the ability of the community to react within the timeframe of the long term window
[02-02-2022 17:22:50] <ArticMine> UkoeHB was very clear in the simulation on this
[02-02-2022 17:22:52] <UkoeHB> it is only critical when you are defining a hard-coded number... it is irrelevant for my theoretical objections which are being ignored
[02-02-2022 17:23:37] <jberman[m]> orphan rates would increase as a consequence of larger blocks
[02-02-2022 17:23:55] <carrington[m]> So in some sense we are choosing between baking in obsolescence and baking in centralized upgrades
[02-02-2022 17:24:22] <UkoeHB> what do you mean react? iirc those comments did not factor into ArticMine and my analyses
[02-02-2022 17:24:36] <rbrunner> Isn't "obsolence" a bit hard for a hard upper limit on the number of transaction?
[02-02-2022 17:24:37] <LyzaL> personally I favor a conservative growth rate, having a fee market for a few months during a period of big growth isn't the end of the world, but mass centralization is
[02-02-2022 17:24:50] <carrington[m]> rbrunner:  my opinion is that spam attacks should cost the same as 51% attacks for equivalent security guarantees
[02-02-2022 17:24:59] <LyzaL> also L2 seems possible at some point
[02-02-2022 17:25:06] <ArticMine> It is not. Bitcoin is a prime example 
[02-02-2022 17:25:24] <ArticMine> Bandwith has increased 200x in the Bitcoin gensis block
[02-02-2022 17:25:37] <ArticMine> while people keep up the debate on the blocksize
[02-02-2022 17:26:10] <rbrunner> So why not have limits that go up more or less together with technology improving?
[02-02-2022 17:26:12] <UkoeHB> Bitcoin does not have huge expensive blocks...
[02-02-2022 17:26:33] <ArticMine> I posted on the orginat BCT thread that was started in 2010 on increasing the blocksize
[02-02-2022 17:27:04] <ArticMine> <rbrunner> So why not have limits that go up more or less together with technology improving? <--- Bingo That is what I want to work on for the next HF
[02-02-2022 17:27:34] <ArticMine> Which is why 1.7 is a reasonable compromise
[02-02-2022 17:27:44] <carrington[m]> For my comment about "reacting" look at Artic's comments in 70 about "recent network attacks"
[02-02-2022 17:28:16] <LyzaL> to my eyes even 1.4 looks like a massive growth rate
[02-02-2022 17:29:15] <ArticMine> Over nthe long term yes over a 2 - 5 month period no
[02-02-2022 17:31:32] <jberman[m]> If we are relying on the fact that we can adapt and react and change the protocol in the event of unforeseen circumstances, why not err on the side of keeping it at the more conservative growth rate it is at now and react in the direction of allowing for more growth, on the chance that we do not find agreement and the long term gets away from us?
[02-02-2022 17:32:21] <rbrunner> Because maybe that feels a little like defeat :)
[02-02-2022 17:32:40] <ArticMine> Because one can control growth in many ways
[02-02-2022 17:32:49] <ArticMine> if there is an issue
[02-02-2022 17:32:56] <rbrunner> More a psychological than a technical problem ...
[02-02-2022 17:33:31] <ArticMine> ^ I agree and Bitcoin is the prime example
[02-02-2022 17:34:34] <carrington[m]> makes sense to me jberman , a conservative growth rate is nothing like locking things at fixed caps for a decade
[02-02-2022 17:35:37] <ArticMine> We have a compromise. I am not going back to ask for 2 but I will not support less that 1.7 1.7 has been on the table for over a year
[02-02-2022 17:36:07] <ArticMine> This is the critical psycological promlem 
[02-02-2022 17:36:24] <merope> Perhaps a dumb question: why does the growth have to be exponential? Why not linear?
[02-02-2022 17:37:04] <LyzaL> or logarithmic
[02-02-2022 17:37:40] <UkoeHB> pretty sure adoption change is proportional to existing adoption
[02-02-2022 17:37:58] <ArticMine> in the intial stages yes
[02-02-2022 17:41:17] <rbrunner> "will not support less that 1.7" How could that look in the light of a possible result of surprisingly low costs - still, after fee rising - for spam attacks?
[02-02-2022 17:41:36] <rbrunner> Just hypothetically, we don't know yet after all
[02-02-2022 17:41:52] <ArticMine> becasue this has been hased to death
[02-02-2022 17:42:00] <Rucknium[m]> I think it is a good idea to read a few messages in the thread of the first suggestion to increase the bitcoin block size. 
[02-02-2022 17:42:00] <Rucknium[m]> https://bitcointalk.org/index.php?topic=1347.msg15366#msg15366
[02-02-2022 17:42:00] <Rucknium[m]> "If we upgrade now, we don't have to convince as much people later if the bitcoin economy continues to grow."
[02-02-2022 17:42:27] <Rucknium[m]> merope: That's sort of my thinking as well. The functional forms that are being chosen are sort of forcing us into a space that maybe we don't want to be. But if we changed the functional forms, then we would have to re-work many things.
[02-02-2022 17:43:01] <ArticMine> My views in that thread are still valid 
[02-02-2022 17:43:19] <ArticMine> It is the reason I gave up on Bitcoin in 2015
[02-02-2022 17:43:44] <ArticMine> and the rest is history
[02-02-2022 17:44:00] <rbrunner> Yeah, but come on, even with 1.1 instead of 1.7 or whatever we are much better than Bitcoin. Is that even a fair comparison?
[02-02-2022 17:44:41] <ArticMine> Yes it is
[02-02-2022 17:44:50] <ArticMine> look at the hisotory of Bitcoin
[02-02-2022 17:44:54] <ArticMine> history
[02-02-2022 17:45:37] <ArticMine> 1.7 was on the tale for a year
[02-02-2022 17:45:52] <ArticMine> table
[02-02-2022 17:45:57] <carrington[m]> It is not a fair comparison, especially seeing as Monero is in general still being upgraded regularly
[02-02-2022 17:46:12] <ArticMine> So is Bitcoin
[02-02-2022 17:46:12] <rbrunner> I feel you, but how can this help us now to come to a "loose consensus" and go forward with the HF?
[02-02-2022 17:46:39] <ArticMine> I though we had consisus at 1.7 untill this morning
[02-02-2022 17:46:49] <rbrunner> We seem to sit at something like a stalemate now, if you want to be brutally honest
[02-02-2022 17:47:14] <ErCiccione> Don't we have to do 2 hard forks anyway? Maybe better be conservative for this one and in case increase in the next one? Does that make sense?
[02-02-2022 17:47:34] <ArticMine> No
[02-02-2022 17:47:56] <rbrunner> Well, 7 hours ago jberman found out even 1.4 can go to 4.5 TB per year, worst case ...
[02-02-2022 17:48:03] <ErCiccione> i mean the second hard for for seraphis
[02-02-2022 17:48:09] <ArticMine> There was critical work that was done over a two year period 
[02-02-2022 17:48:18] <ErCiccione> but if it doesn't makes sense it'll just shut up 🙂
[02-02-2022 17:48:37] <UkoeHB> ErCiccione: seraphis may be 3 hardforks in the future, if it takes long enough. The next hardfork after this one is likely to be very small (if we have one).
[02-02-2022 17:49:34] <UkoeHB> ArticMine: it might help if you publish your numerical research for us to examine. Your presentation of 'we need 2x' was only backed up by a couple paragraphs.
[02-02-2022 17:50:02] <ArticMine> I am not convicend it will do any help
[02-02-2022 17:50:20] <ArticMine> I o zero response to my comments on 70 untill the very las minute
[02-02-2022 17:50:24] <ArticMine> 'las
[02-02-2022 17:50:29] <ArticMine> last
[02-02-2022 17:51:04] <ArticMine> Take a look at the date of the post on issue 70
[02-02-2022 17:51:17] <ArticMine> There was ample time to ask questions etc
[02-02-2022 17:51:45] <carrington[m]> The maximally bloated scenario is unlikely IMO because of the way the penalty works. A "medium speed" growth rate will probably provide more useful numbers for a given "maximum annual growth"
[02-02-2022 17:51:53] <UkoeHB> ok sure, but we are talking about it now... better late than never
[02-02-2022 17:53:17] <ArticMine> In order to kii the entire proposal
[02-02-2022 17:53:18] <UkoeHB> I don't personally have a big stake in the number chosen, but it would be nice from an engineering PoV to understand the argument with more precision. Right now there feels a lot of vagueness
[02-02-2022 17:54:23] <rbrunner> Seems to me that's almost a given, because you can easily work with quite different assumptions about growth, behaviour of market, of miners, of users ...
[02-02-2022 17:54:44] <rbrunner> Which then may lead to a different "best" growth rate
[02-02-2022 17:55:09] <ArticMine> One can argue against any number by taking edge cases
[02-02-2022 17:56:13] <rbrunner> Realistically, if we go now with 1.7 and something bad comes upon us, we can probably emergency-HF in a month or even less. With this in sight, we should not allow a stalemate ruin our nice HF. IMHO.
[02-02-2022 17:56:15] <selsta> I would go with 1.7, we will still have enough time to do further research on fees in the future
[02-02-2022 17:56:52] <ArticMine> ^ I agree
[02-02-2022 17:57:57] <ArticMine> This is the point of the compromise
[02-02-2022 17:58:39] <jberman[m]> Ok
[02-02-2022 17:59:19] <selsta> also mooo already updated to PR so we have to go with it now :D
[02-02-2022 17:59:30] <UkoeHB> lol
[02-02-2022 17:59:33] <rbrunner> lol
[02-02-2022 17:59:42] <rbrunner> Best argument today :)
[02-02-2022 17:59:52] <mj-xmr[m]> ^ Convinced
[02-02-2022 17:59:57] <rbrunner> Solid engineering
[02-02-2022 18:00:08] * moneromooo tyoped to 2.7 instead of 1.7 so I guess we're going with that.
[02-02-2022 18:00:26] <ArticMine> lol
[02-02-2022 18:01:54] <rbrunner> So maybe this time it's not our famous "loose consensus" but only a very loose one, but the comprimise can go through - barely?
[02-02-2022 18:02:04] <carrington[m]> If we are at "roughly  consensus" on the 1.7 number, does anyone have any insight into this concern of mine:
[02-02-2022 18:02:04] <carrington[m]>  do we know for sure that miner implementations are actually set up to behave "rationally" once we are in the dynamic blocksize regime? i.e. does software like XMRig account for the penalty that will be applied correctly and allow itself to build blocks larger than 300kb under optimal fee environments, or does it naively just keep adding highest-fee transactions beyond the 300kb limit? It seems to me that if the mining
[02-02-2022 18:02:04] <carrington[m]> software is not set up to actually figure this stuff out, the whole dynamic blocksize system will not kick in smoothly.
[02-02-2022 18:03:02] <ArticMine> The dynamic blocksize has kied in before
[02-02-2022 18:03:18] <ArticMine> kicked in
[02-02-2022 18:03:42] <ArticMine> after the RingCT fork in 2017
[02-02-2022 18:03:44] <rbrunner> Don't know, can't imagine miners would put up with this for longtime before they revolt
[02-02-2022 18:04:01] <moneromooo> xmrig doesn't have to care about this.
[02-02-2022 18:04:01] <UkoeHB> Ok we are at the end of the meeting. There seems general consensus to allow 1.7 into the fork. I hope/expect by summer there is a stronger and more precise understanding about scaling, stability, and spam costs around block sizes and block growth. This way we can have compelling arguments about scaling factors and the presence/absence of a hard upper limit.
[02-02-2022 18:04:11] <merope> Xmrig does not know anything about transactions nor fees, only hashing block templates
[02-02-2022 18:04:50] <rbrunner> Well spoken, UkoeHB.
[02-02-2022 18:04:54] <merope> Fees and txes are the responsibility of nodes (or whoever generates the block template to be mined)
[02-02-2022 18:05:09] <carrington[m]> OK I guess I mean pool operators (or whatever algorithms they use)
[02-02-2022 18:05:17] <UkoeHB> thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-01-29T18:14:21+00:00
- Closed at: 2022-02-05T23:49:03+00:00
