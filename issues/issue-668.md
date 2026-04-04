---
title: Monero Research Lab Meeting - Wed 23 February 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/668
author: Rucknium
assignees: []
labels: []
created_at: '2022-02-22T04:03:32+00:00'
updated_at: '2022-02-28T22:04:48+00:00'
type: issue
status: closed
closed_at: '2022-02-28T22:04:48+00:00'
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

#665 

# Discussion History
## UkoeHB | 2022-02-23T17:52:17+00:00
```
[02-23-2022 17:00:03] <UkoeHB> Meeting time ( https://github.com/monero-project/meta/issues/668 )
[02-23-2022 17:00:09] <UkoeHB> 1. Greetings
[02-23-2022 17:00:10] <UkoeHB> Hello
[02-23-2022 17:00:37] <rbrunner> Hi
[02-23-2022 17:00:58] <sgp_> hello
[02-23-2022 17:01:23] <SerHack> Hi
[02-23-2022 17:03:01] <jberman[m]> Hiya
[02-23-2022 17:03:20] <Rucknium[m]> Hi
[02-23-2022 17:04:36] <UkoeHB> sgp_: view tags are already fuzzy
[02-23-2022 17:05:02] <sgp_> UkoeHB: oh yeah, of course duh. Sorry :)
[02-23-2022 17:05:12] <UkoeHB> however if you can compute a view tag then you can also compute a nominal spend key, which reveals more info
[02-23-2022 17:05:59] <UkoeHB> but we need that for efficiency on the client side
[02-23-2022 17:07:52] <UkoeHB> 2. let's do updates, what is everyone working on these days?
[02-23-2022 17:09:04] <Rucknium[m]> The MAGIC Monero Fund has its first research grant application, by xmr-ack :
[02-23-2022 17:09:04] <Rucknium[m]> https://github.com/MAGICGrants/Monero-Fund/issues/15
[02-23-2022 17:09:52] <UkoeHB> me: I finished my CCS ( https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256#note_15087 ) and plan to make a new one today.
[02-23-2022 17:10:29] <Rucknium[m]> The general idea is to see how accurately machine learning techniques can identify the real spend in a ring, using a synthetic dataset.
[02-23-2022 17:11:09] <Rucknium[m]> The MAGIC Monero Fund is asking MRL for feedback on the grant application. Of course, the final decision rests with the committee.
[02-23-2022 17:11:34] <Rucknium[m]> Maybe isthmus would have some input given his experience with machine learning.
[02-23-2022 17:12:04] <rbrunner> Is that the background of the currently very high tx traffic on testnet?
[02-23-2022 17:12:20] <Rucknium[m]> rbrunner: Yes.
[02-23-2022 17:12:36] <rbrunner> Sounds like an interesting project.
[02-23-2022 17:12:49] <rbrunner> For a layman like me, at least
[02-23-2022 17:14:15] <UkoeHB> I'm wondering how you translate results/models obtained for a synthetic data set to the real data set.
[02-23-2022 17:14:31] <gingeropolous> oh jesus he's using the public testnet?
[02-23-2022 17:14:53] <rbrunner> You did not notice that huuuuuge amount of traffic there over the last 3 weeks? :)
[02-23-2022 17:15:09] <gingeropolous> ugh thats unnecessary
[02-23-2022 17:18:09] <rbrunner> Not sure. As soon as somebody wants to confirm results, a public blockchain may be very handy
[02-23-2022 17:18:36] <Rucknium[m]> Also, plowsof and I set up an instance of WIKINDX at https://moneroresearch.info/ . It's a place to collect Monero-related papers and annotate them. My hope is that it can help onboard new researchers and help us establish a workflow for reviewing new papers that are written about Monero.
[02-23-2022 17:19:55] <Rucknium[m]> I've disabled public user registrations to avoid vandalism, but if anyone wants to create a user to be able to add, edit, and add annotations to papers, just message me and I will create one for you.
[02-23-2022 17:20:22] <gingeropolous> also, stagenet might potentially be better. testnet could get hella ugly if/when we actually test the new release. the randomx testnet was brutal
[02-23-2022 17:21:06] <gingeropolous> but yeah rbrunner re: public blockchain reproducibility considerations.
[02-23-2022 17:22:08] <rbrunner> Hopefully that WIKINDX thing does not need to much babysitting and does not surprise with new security holes every fortnight :)
[02-23-2022 17:23:46] <Rucknium[m]> rbrunner: WIKINDX has been around since 2003 apparently. It was hard to set up, but hopefully it is "mature" by now.
[02-23-2022 17:23:51] <UkoeHB> 3. I guess we can move to discussion. Any items to discuss? Perhaps from the agenda
[02-23-2022 17:23:54] <gingeropolous> and UkoeHB re: synthetic vs. real data. I share the same curiosity, and i'd propose to use the bitcoin blockchain with ring sigs superimposed somehow
[02-23-2022 17:24:24] <gingeropolous> but, its good to do things in multiple ways i guess
[02-23-2022 17:25:02] <rbrunner> I have a question that may be of wider interest and was brought up by a recent video about Seraphis:
[02-23-2022 17:25:10] <rbrunner> I refer to the following article: https://www.getmonero.org/2021/12/22/what-is-seraphis.html
[02-23-2022 17:25:15] <UkoeHB> gingeropolous: yeah you could probably generate the bitcoin blockchain with ring sigs all offline.
[02-23-2022 17:25:21] <rbrunner> Under "membership proof delegation" it mentions that this may open up the following possibility:
[02-23-2022 17:25:28] <rbrunner> Ignore 10-block lock time when transacting with a *trusted* party (i.e. allow them to make your tx's membership proofs and submit the tx to the network on your behalf).
[02-23-2022 17:25:35] <rbrunner> Is that still current? And if yes can you sketch what that means and how that could work in practice?
[02-23-2022 17:26:34] <UkoeHB> rbrunner: You would send a `PartialTx` to your friend, and then later they can make membership proofs for the tx and submit it.
[02-23-2022 17:27:04] <UkoeHB> this guy: https://github.com/UkoeHB/monero/blob/bd46a0f92079080a3abde92041cd81160b8cb91d/src/seraphis/txtype_squashed_v1.cpp#L183
[02-23-2022 17:27:45] <UkoeHB> err actually would be this one in practice lol: https://github.com/UkoeHB/monero/blob/bd46a0f92079080a3abde92041cd81160b8cb91d/src/seraphis/txtype_squashed_v1.cpp#L201
[02-23-2022 17:27:59] <rbrunner> And it's trusted because by building such a partial tx and sending it to my friend, I still could spend faster and cheat?
[02-23-2022 17:29:10] <UkoeHB> that and your friend will know the real spends
[02-23-2022 17:29:43] <rbrunner> But I could send such a partial tx very early, within the 10-block spend limit?
[02-23-2022 17:29:50] <xmr-ack[m]> <UkoeHB> "I'm wondering how you translate..." <- This is the reason I choose to collect it on the test-net, I need the data to resemble main-net as close as possible. With machine learning, small discrepancies in the training dataset compared to the testing dataset could result in large inaccuracies. I understand a large amount of traffic on the test-net is not ideal, so I'll soon be delaying transactions based on real-user
[02-23-2022 17:29:50] <xmr-ack[m]> spending patterns.
[02-23-2022 17:30:35] <gingeropolous> but where are u getting those spending patterns?
[02-23-2022 17:30:46] <UkoeHB> rbrunner: yes
[02-23-2022 17:31:16] <xmr-ack[m]> <gingeropolous> "also, stagenet might potentially..." <- This might be a good common ground.
[02-23-2022 17:31:38] <gingeropolous> yeah. testnet has the potential to get restarted, or rolled back, during dev testing etc
[02-23-2022 17:31:46] <gingeropolous> could really muck up your work
[02-23-2022 17:31:47] <rbrunner> Alright, so that's only a "reduction" or "circumvention" of the 10-block limit in quite special circumstances. And I guess final submit has to wait then?
[02-23-2022 17:32:11] <Rucknium[m]> xmr-ack: One good reason to do it on testnet or stagenet would be if you were using network data as features for the machine learning algorithm.
[02-23-2022 17:32:33] <UkoeHB> rbrunner: right
[02-23-2022 17:32:40] <rbrunner> Ok, thanks!
[02-23-2022 17:33:31] <gingeropolous> stagenet shouldn't be fiddled with in that way. stagenet is meant to mimic mainnet, just not have any value. testnet is meant to test consensus rules etc. at least thats the thought. but testnet only really got mucked with during the randomx testing as far as i recall.
[02-23-2022 17:33:37] <UkoeHB> delegation is more useful for multisig, tx chaining, collaborative funding
[02-23-2022 17:34:31] <xmr-ack[m]> gingeropolous: The gamma distribution proposed in Moser et al. Additionally, I'm going to run an experiment soon where I crawl the last 1,000,000 transactions on main-net using the onion block explorer and calculate the distribution of transaction fees to simulate that as well.
[02-23-2022 17:35:08] <xmr-ack[m]> gingeropolous: I didn't know this. That could be a problem
[02-23-2022 17:36:20] <UkoeHB> xmr-ack[m]: is there an advantage to generating real txs? your database just reduces to {block height, {reference heights}}
[02-23-2022 17:36:22] <rbrunner> Well, testnet was quite stable for a long time now.
[02-23-2022 17:36:33] <gingeropolous> we haven't had to test new consensus rules :)
[02-23-2022 17:36:51] <rbrunner> True.
[02-23-2022 17:37:14] <gingeropolous> i mean, the new ones shouldn't be that fiddly, but who knows
[02-23-2022 17:37:34] <xmr-ack[m]> <Rucknium[m]> "xmr-ack: One good reason to do..." <- I have thought about incorporating network features and even ran some experiments in the past where a 1D conv-net was able to differentiate between remote node network traffic with a > 90% accuracy. But that was a quite small dataset and only preliminary results.
[02-23-2022 17:40:25] <jberman[m]> UkoeHB: I have some code here that simulates different wallet version strategies to arrive at this FWIW: https://github.com/j-berman/monero/commit/4baf4c99b002583905b4389402d9a5081d168059
[02-23-2022 17:40:54] <gingeropolous> i dunno about network features. the permanent thing is the blockchain
[02-23-2022 17:42:18] <xmr-ack[m]> <UkoeHB> "xmr-ack: is there an advantage..." <- My reasons so far include:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/8816854db00368e85005a07d2021036b621cd66d)
[02-23-2022 17:42:19] <Rucknium[m]> Monero adversaries almost certainly are collecting more than just blockchain data.
[02-23-2022 17:42:23] <xmr-ack[m]> gingeropolous: I agree
[02-23-2022 17:43:35] <xmr-ack[m]> Rucknium: They are but I think specifically for this research project that is out of scope. I may continue my research down the road and look into fingerprinting network patterns between: peers, remote nodes, etc...
[02-23-2022 17:44:12] <xmr-ack[m]> Fingerprinting network patterns is really cool because you can pretty much bypass all encryption.
[02-23-2022 17:44:59] <rbrunner> Uh, you may elaborate a bit, otherwise people will freak out reading the log of this meeting ...
[02-23-2022 17:45:02] <xmr-ack[m]> * all encryption. Granted you can only classify high level actions ( ex. user spent monero vs user recieved blocks)
[02-23-2022 17:45:30] <xmr-ack[m]> Yea I just edited hahah I realized that needed more context
[02-23-2022 17:45:57] <xmr-ack[m]> Let me find a good paper for anyone thats interested
[02-23-2022 17:46:03] <rbrunner> "Monero researcher finally admits: Monero *is* traceable" :)
[02-23-2022 17:46:26] <xmr-ack[m]> ~never~
[02-23-2022 17:46:40] <Rucknium[m]> Dandelion++ is supposed to reduce the efficacy of de-anonymization efforts based on monitoring network data, I believe.
[02-23-2022 17:46:56] <rbrunner> Had the same thought, yes
[02-23-2022 17:49:33] <UkoeHB> I think we can call the meeting here, unless anyone has any last minute comments/questions.
[02-23-2022 17:50:34] <UkoeHB> ok thanks for attending everyone
[02-23-2022 17:50:50] <xmr-ack[m]> Rucknium[m]: Yea good point. To clarify, the research scenario where traffic patterns could be fingerprinted were only tested in a highly privileged network location. ( ex. a local adversary that could view encrypted packet patterns )
[02-23-2022 17:51:21] <xmr-ack[m]> * packet patterns before the traffic reached the remote node)
```

# Action History
- Created by: Rucknium | 2022-02-22T04:03:32+00:00
- Closed at: 2022-02-28T22:04:48+00:00
