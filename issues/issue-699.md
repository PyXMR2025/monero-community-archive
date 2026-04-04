---
title: Monero Research Lab Meeting - Wed 4 May 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/699
author: Rucknium
assignees: []
labels: []
created_at: '2022-05-01T20:11:01+00:00'
updated_at: '2022-05-10T15:15:01+00:00'
type: issue
status: closed
closed_at: '2022-05-10T15:15:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Increasing Seraphis address indices from 7 -> 16 bytes (and increasing the address tag MAC from 1 -> 2 bytes). ( https://libera.monerologs.net/monero-research-lab/20220425#c88396 and https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4144862#gistcomment-4144862 )

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

#697 

# Discussion History
## UkoeHB | 2022-05-04T19:15:51+00:00
```
[05-04-2022 17:01:05] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/699
[05-04-2022 17:01:05] <UkoeHB> 1. greetings
[05-04-2022 17:01:05] <UkoeHB> hello
[05-04-2022 17:01:20] <Rucknium[m]> Hi
[05-04-2022 17:01:23] <rbrunner> Hi there
[05-04-2022 17:01:24] <dangerousfreedom> Hi!
[05-04-2022 17:01:55] <jberman[m]> howdy
[05-04-2022 17:02:15] <mj-xmr[m]> o/
[05-04-2022 17:02:34] <sech1> hello
[05-04-2022 17:03:00] <UkoeHB> 2. updates, what is everyone working on?
[05-04-2022 17:03:20] <h4sh3d> Hello
[05-04-2022 17:03:36] <mj-xmr[m]> Decoy selection algo:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/d66c3eaf1e9d569973e5d8ddb921115d615aeab4)
[05-04-2022 17:05:17] <jberman[m]> atm focused on trying to finish reviewing rbrunner's 8076
[05-04-2022 17:05:30] <rbrunner> Very glad to hear you are on it :)
[05-04-2022 17:05:51] <Rucknium[m]> Developing a model to estimate the effect of the 0.1% operator fee hike on minexmr's hashpower share (want to discuss this). Computing the empirical spend age of BTC, BCH, LTC, and DOGE outputs (also want to discuss this).
[05-04-2022 17:06:07] <UkoeHB> me: I implemented 16-byte address indices in my seraphis PoC (using Twofish for the address tag cipher), and fixed a multisig exploit that would let a tx proposer burn funds (both for pr 8149 and seraphis). Next I will implement discretized fees and finally implement an input selection solver.
[05-04-2022 17:07:52] <Rucknium[m]> mj-xmr: How close do you think we are to parity between the wallet2 and your python implementations of the decoy selection algorithm? When can we start statistical testing of equivalency?
[05-04-2022 17:08:25] <mj-xmr[m]> Rucknium: I think I need at least 2 weeks for this.
[05-04-2022 17:09:25] <mj-xmr[m]> It's just that it's not the only thing I do, and I'm continuously dragged for reviewing this and that. Which is good, as it pushes many things forward.
[05-04-2022 17:10:24] <Rucknium[m]> Thanks. Sounds good. Timeline is useful for my planning purposes.
[05-04-2022 17:10:28] <UkoeHB> 3. discussion (if anyone has more updates, feel free to drop them)
[05-04-2022 17:10:40] <UkoeHB> looks like Rucknium[m] is raring to go
[05-04-2022 17:10:45] <dangerousfreedom> I'm still working on my website and monero tools to verify all the txs from the inflation point of view. I bought the domain moneroinflation.com (with xmr of course :p) and my first delivery will be by the end of the month. I believe I am on track regarding my CCS proposal and I am also exploring some algorithms and C++ implementations of these EC point multiplications to better understand what is going in the software
[05-04-2022 17:10:45] <dangerousfreedom> and with my Python implementation.
[05-04-2022 17:12:23] <UkoeHB> Rucknium[m]: did you have something to discuss?
[05-04-2022 17:12:58] <Rucknium[m]> Overall, I would like to "manage expectations" about the minexmr estimations. As has been said, all models are wrong, but some are useful. In time series especially there are many judgment calls to be made about model specification that can be debated. And this statistical problem has particular features, such as the fact that the data is count data, that can make things tricky....
[05-04-2022 17:13:48] <Rucknium[m]> But mainly just a brainstorm about what factors may affect minexmr's share of found blocks. So far I have on-chain difficulty from monerod and fiat/XMR exchange rate
[05-04-2022 17:14:17] <UkoeHB> The rate change seems like it would be too small to affect anything
[05-04-2022 17:14:57] <Rucknium[m]> The main purposes of adding more variables is (1) increases precision of the model and (2) hopefully avoids confusing the rate change increase with other factors that are changing at the same time
[05-04-2022 17:15:56] <Rucknium[m]> UkoeHB: I think in theory you are probably right. Hopefully some statistical analysis can help test that hypothesis.
[05-04-2022 17:16:50] <Rucknium[m]> An implication of the "no effect" hypothesis is that minexmr would have increased their revenue by 10%.
[05-04-2022 17:17:35] <Rucknium[m]> So any other factors that may affect minexmr's share of found blocks? endor00 may have some ideas.
[05-04-2022 17:20:32] <merope> I agree with koe's take: at first glance, the 0.1% fee increase is just more money in their pocket
[05-04-2022 17:20:34] <UkoeHB> probable factors: marketing efforts by different pools (including grassroots eg p2pool), software changes by different pools
[05-04-2022 17:21:37] <UkoeHB> also perception around overall hashrate can influence whether people enter/exit a pool
[05-04-2022 17:21:47] <UkoeHB> hashrate share*
[05-04-2022 17:22:52] <UkoeHB> What did you want to say about empirical spend age?
[05-04-2022 17:23:10] <merope> The choice of the pool is affected by many factors: some "purely rational" and financial (like the impact of the fee on income), others subjective or harder to quantify, such as marketing, perception (like having a nice website, and a good "image" in the community), connection latency, pool stability and uptime, and historical reliability (no exit scams or bad payments)
[05-04-2022 17:23:29] <UkoeHB> good summary
[05-04-2022 17:23:29] <merope> And all that gets thrown into the blender with miner education - there are many newcomers who have no idea about most of this stuff, so they just pick the first on the list and call it a day
[05-04-2022 17:23:57] <merope> Or they even think that bigger is better (which I've had to dispel several times)
[05-04-2022 17:24:17] <Rucknium[m]> endor00: Thanks. I wonder if there is a way to measure some of those factors.
[05-04-2022 17:25:06] <merope> Bonus round: there are many botnets that pick the top pools due to the greater stability of their larger infrastructure
[05-04-2022 17:25:20] <w[m]> Are you already tracking number of mineral per pool?
[05-04-2022 17:25:20] <w[m]> / hashrate migration?
[05-04-2022 17:25:43] <merope> It's why Supportxmr doesn't ban some known botnets, despite their no-botnet policy: if they were to ban them, they would most likely move on Minexmr and make centralization worse
[05-04-2022 17:26:24] <merope> One useful metric would be looking at the historical number of miners on the pool, in relation with the total pool hashrate
[05-04-2022 17:26:32] <w[m]> Hashrate often moves minexmr to and from "unknown" and also to some spikes on pps pools 
[05-04-2022 17:26:59] <Rucknium[m]> w: I think that number of found blocks and number of miners shouldn't be considered independent metrics. One causes the other in a very direct fashion.
[05-04-2022 17:27:38] <merope> Not aware of any platforms that save historical data about this though... Perhaps miningpoolstats.stream? They display the data for the last week or so, but I don't know if they save it further than that
[05-04-2022 17:28:35] <merope> (Though nothing stops you from digging through their page source and finding their api endpoint and saving data yourself - I looked into that a while back, but don't have any data saved)
[05-04-2022 17:29:05] <Rucknium[m]> endor00: Interesting idea. Also, we don't know what the hashpower behind each miner is, so it may be difficult to get any traction. There is probably a large diversity among the miners
[05-04-2022 17:29:12] * w[m] uploaded an image: (200KiB) < https://libera.ems.host/_matrix/media/r0/download/monero.social/UzmOKEzWUfvieyXWKQSVOpkC/Image_110.jpg >
[05-04-2022 17:29:36] <UkoeHB> Rucknium[m]: what did you want to discuss re: empirical spend age?
[05-04-2022 17:29:38] * w[m] uploaded an image: (166KiB) < https://libera.ems.host/_matrix/media/r0/download/monero.social/OynAVotgXmXzrOJFMCKEZIUv/Image_111.jpg >
[05-04-2022 17:29:49] <w[m]> These are from the week leading into Feb 17
[05-04-2022 17:30:46] <w[m]> 30+% of the hashrate came from 200 miners or less
[05-04-2022 17:31:11] <w[m]> * 30+% of the hashrate came from 200 miners or less
[05-04-2022 17:31:11] <w[m]> Edit. In theory.
[05-04-2022 17:31:21] <Rucknium[m]> Ok. On to computing the empirical spend age of BTC, BCH, LTC, and DOGE outputs. I have modified some code I wrote to analyze the BTC/BCH blockchain to extract the necessary data from blockchains that have bitcoin-like RPC calls. I now have preliminary results for LTC and DOGE. 
[05-04-2022 17:31:34] <Rucknium[m]> The purpose for now is to measure the stability of the inter-temporal spend age distributions. This can give us a sense of the "out of sample" risk of a static decoy selection algorithm. In other words, the estimates done on Monero's historical block chain (which are still the most important estimates) cannot tell us what may happen if there is a sudden change in the composition of users or in the behavior of existing users.
[05-04-2022 17:32:04] <Rucknium[m]> This is related to forecasting with mj-xmr 's `tsqsim` software -- what is the risk?
[05-04-2022 17:32:24] <Rucknium[m]> So what other blockchains other than BTC, BCH, LTC, and DOGE would make sense here?
[05-04-2022 17:33:05] <UkoeHB> are there any other simple chains with meaningful tx volume?
[05-04-2022 17:33:20] <Rucknium[m]> (DOGE is in this mix since it has bitcoin-like RPC [with a small modification] and it experienced a sudden rise from obscurity to popularity, which XMR might do one day)
[05-04-2022 17:34:44] <merope> DASH is somewhat comparable to Monero, in terms of tx volume
[05-04-2022 17:34:58] <Rucknium[m]> This issue of the inter-temporal stability of the spend time distribution also is important for any enforcement of decoy selection algorithm down the line with Seraphis or before. I have had an idea to somehow have miners include some information about the dynamic change in the spend age distribution in the block header, to "conduct the orchestra"
[05-04-2022 17:35:14] <merope> And the api should be the same, I think
[05-04-2022 17:35:26] <UkoeHB> Tbh I don't think enforcing decoy selection would work well
[05-04-2022 17:35:36] <UkoeHB> aside from deterministic bins
[05-04-2022 17:36:09] <Rucknium[m]> Yes, I was considering Dash. I think there is a complication with their CoinJoin privacy features, but it may be worth it to compute it and see what it looks like.
[05-04-2022 17:36:18] <UkoeHB> It's really hard to make decoy selection deterministic and not a huge mess that's hard to validate
[05-04-2022 17:37:26] <rbrunner> Say people suddenly start to spend twice as early as before. How would somebody notice this in the first place, with Monero, to do something with it, regarding any analysis?
[05-04-2022 17:37:26] <UkoeHB> deterministic bins on their own are already pretty complex
[05-04-2022 17:37:28] <Rucknium[m]> I thought your proposal did that?
[05-04-2022 17:37:46] <UkoeHB> I just decided to implement the deterministic bins part, but let bin locations be user-defined
[05-04-2022 17:38:01] <UkoeHB> the bin location selector can be injected
[05-04-2022 17:38:28] <UkoeHB> https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis/tx_ref_set_index_mapper.h
[05-04-2022 17:39:06] <UkoeHB> you can see how complex the bins are here: https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis/tx_binned_reference_set_utils.cpp
[05-04-2022 17:39:21] <Rucknium[m]> rbrunner: If there is a substantial mismatch between user behavior and the decoy selection algorithm, statistical methods can be used to narrow down which decoy is the true spend. xmr-ack 's preliminary research with machine learning illustrated that.
[05-04-2022 17:40:41] <rbrunner> My fantasy just fails me when I try to imagine where any "signal" comes from here, that could be machine-learned, but that's probably my innoncence regarding statistics
[05-04-2022 17:41:07] <rbrunner> As you don't really "see" user behaviour, do you?
[05-04-2022 17:41:09] <Rucknium[m]> So a sudden shift in user behavior without a corresponding shift in the decoy selection algorithm can create problems for user privacy.
[05-04-2022 17:41:38] <Rucknium[m]> No, but you see the decoy selection algorithm.
[05-04-2022 17:42:36] <rbrunner> So it's kind of a risk estimation you will do, looking as those "clear" blockchains, and see what happened there regarding factors like "spend speed"?
[05-04-2022 17:42:52] <rbrunner> If such shift happen often, higher risk for Monero
[05-04-2022 17:42:55] <merope> Random thought: could the decoy selection be "parametrized" based on the age of the real spend, such that the "degree of privacy" is maximised each time?
[05-04-2022 17:43:14] <merope> Or does that make no sense, because such parametrization would inherently expose the age?
[05-04-2022 17:44:08] <jberman[m]> rbrunner: you can plot on a graph like this and the blue line would diverge heavily from orange: https://user-images.githubusercontent.com/26468430/130846265-d9fa5363-4b5b-4440-b1e9-fb656c614f4a.png ... so in a way, you can still "see" user behavior
[05-04-2022 17:44:16] <Rucknium[m]> Right. If there are quick shifts, then that will affect the tuning of a decoy selection algorithm. Sort of like if you are holding an asset whose value is very volatile. Your behavior would be different of the asset doesn't change much
[05-04-2022 17:46:04] <Rucknium[m]> endor00: Your second conclusion is correct, IMHO.
[05-04-2022 17:46:21] <rbrunner> "so in a way, you can still "see" user behavior" the aggregate of it, right?
[05-04-2022 17:46:26] <UkoeHB> before the end of the meeting, there are two more items
[05-04-2022 17:46:39] <jberman[m]> right
[05-04-2022 17:47:05] <Rucknium[m]> Basically, you don't want to make the decoy selection algorithm change dependent upon what the real spend of a particular tx is.
[05-04-2022 17:47:29] <h4sh3d> UkoeHB: you mentionned some work to document the multisig protocol with dangerousfreedom, how can I help?
[05-04-2022 17:47:32] <UkoeHB> item 1: I am putting together a workgroup for documenting multisig for use by an auditor. So far, dangerousfreedom and h4sh3d seem interested in participating.
[05-04-2022 17:47:37] <UkoeHB> right
[05-04-2022 17:47:48] <h4sh3d> :) perfect timing
[05-04-2022 17:48:05] <UkoeHB> tbh I'm not sure the best way to do it
[05-04-2022 17:48:34] <h4sh3d> what king of documentation do we want to produce? (IIRC it's for helping audit)
[05-04-2022 17:48:58] <h4sh3d> *kind
[05-04-2022 17:49:14] <UkoeHB> Probably a pdf that describes the algorithms (key generation and signing) with comments and citations justifying different parts of the design.
[05-04-2022 17:50:10] <UkoeHB> It needs a little more technical precision than ZtM2, but that style is probably good.
[05-04-2022 17:51:22] <UkoeHB> I guess the question for this meeting is if anyone else wants to participate.
[05-04-2022 17:52:56] <UkoeHB> Well, maybe not
[05-04-2022 17:53:30] <UkoeHB> We can coordinate more outside the meeting. I will try to put together a communication channel
[05-04-2022 17:53:53] <h4sh3d> perfect, thanks
[05-04-2022 17:54:05] <dangerousfreedom> I will be happy to help h4sh3d with this multisig stuff, thanks
[05-04-2022 17:54:32] <UkoeHB> item 2: this issue was made https://github.com/monero-project/research-lab/issues/100 does anyone have questions/comments? sounds like kayabaNerve will try to demo what a membership proof circuit would look like
[05-04-2022 17:56:40] <rbrunner> The idea wasn't kindly received on Reddit
[05-04-2022 17:56:56] <rbrunner> but it seems thankfully that did not spill over to GitHub ...
[05-04-2022 17:57:26] <UkoeHB> it's not like we will implement something that actually sucks; if it actually doesn't suck, then why not?
[05-04-2022 17:57:40] <rbrunner> Lol ... that's the spirit :)
[05-04-2022 17:58:15] <Rucknium[m]> Poorly-informed question: If we wanted to have defense-in-depth and somehow combined a full ZK cryptographic system with ring signatures (stack one on top of the other?), then would tx size and verification be something like the sum of the two systems or multiplicative or some other function?
[05-04-2022 17:59:03] <Rucknium[m]> From my understanding, MobileCoin (koe please correct me) has defense in depth with ring sigs and secure execution environment.
[05-04-2022 18:00:34] <merope> I thought the secure environment was to hold the user's private viewkey for tx scanning, so that they won't get exposed even in case of a hack
[05-04-2022 18:00:55] <UkoeHB> Would the idea be to merkle proof all the ring members, then do a ring sig on the ring members, all within a circuit? It seems multiplicative
[05-04-2022 18:01:31] <UkoeHB> merope: no that's the Fog service, mobilecoin also validates all txs within SGX then discards signatures when finalizing blocks
[05-04-2022 18:02:19] <merope> Oh I see
[05-04-2022 18:02:44] <merope> Wouldn't that make it impossible for an external user to validate the chain by themselves though? Because they would miss all the signature data
[05-04-2022 18:02:56] <UkoeHB> yes it's part of their trust model
[05-04-2022 18:03:32] <UkoeHB> ok we are at the end of the meeting, thanks for attending everyone
[05-04-2022 18:03:37] <Rucknium[m]> I am out of my depth on this for sure, so I don't know what's possible. I think the broader community is concerned that ZK has not stood the test of time the way that the cryptographic assumptions that underpin ring sigs have. (I know RingCT is technically ZK, but I think the underlying assumptions are different from zk-SNARKS and the like.
[05-04-2022 18:04:43] <UkoeHB> I think it's right to be concerned/attentive when actually funding/implementing something. Zk circuits in monero are just a fancy idea...
[05-04-2022 18:05:33] <rbrunner> And I guess it would be a long, long way to arrive at something that can safely deployed in a hardfork. Mountains of work.
[05-04-2022 18:06:07] <UkoeHB> right, a mountain that begins with actually looking at it lmao (instead of hysterics)
[05-04-2022 18:07:17] <rbrunner> I for one find it interesting what will result from "looking at it", yeah. It's quite nebulous now, it's more or less just "that Zcash thing"
[05-04-2022 18:11:11] <jberman[m]> AFAICT (and excuse this potential over-simplification), these 2 reasons seemed to be the strongest justification for keeping the membership proof separate, and approaching it like that to start:
[05-04-2022 18:11:57] <jberman[m]> (1) future upgrades to the protocol could potentially still build off the same anonymity pool, which is unlike Zcash today which upgrades pools every major change - kayabaNerve's point as I understood it 
[05-04-2022 18:12:08] <jberman[m]> (2) modularity enables tx chaining and a cleaner tx building protocol - UkoeHB 
[05-04-2022 18:12:24] <jberman[m]> Seems like a sensible first step at the problem to me, and to validate those points as it progresses
[05-04-2022 18:17:09] <UkoeHB> good point about the pools
```

# Action History
- Created by: Rucknium | 2022-05-01T20:11:01+00:00
- Closed at: 2022-05-10T15:15:01+00:00
