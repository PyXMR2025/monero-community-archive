---
title: Monero Research Lab Meeting - Wed 24 November 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/632
author: Rucknium
assignees: []
labels: []
created_at: '2021-11-23T06:05:02+00:00'
updated_at: '2021-11-30T20:50:52+00:00'
type: issue
status: closed
closed_at: '2021-11-30T20:50:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss requirements to get [the multisig PR](https://github.com/monero-project/monero/pull/7877) merged.

3. "Seeing a bug in Aeon transactions where multiple inputs in one transaction use the same output. " https://github.com/monero-project/monero/pull/8047

4. Cryptographic performance benchmarks https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks

5. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

7. [The Science of Blockchain Conference 2022 Jan 24-26](https://cbr.stanford.edu/sbc22/#cfp). Submission deadline: November 23, 2021 11:59pm PST

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

10. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

11. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

12. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

13. Any other business

14. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#627  

# Discussion History
## UkoeHB | 2021-11-24T18:02:31+00:00
```
[2021-11-24 17:01:22] <UkoeHB> meeting time ( https://github.com/monero-project/meta/issues/632 )
[2021-11-24 17:01:22] <UkoeHB> 1. greetings
[2021-11-24 17:01:41] <one-horse-wagon[> Hello.
[2021-11-24 17:01:46] <UkoeHB> hello; this week is a holiday in the states, so attendance may be lower
[2021-11-24 17:01:47] <rbrunner> Hi
[2021-11-24 17:01:58] <jberman[m]> hello :)
[2021-11-24 17:03:55] <carrington[m]> Salutations
[2021-11-24 17:04:14] <SerHack> Hi
[2021-11-24 17:05:26] <UkoeHB> 2. let's start with updates
[2021-11-24 17:08:30] <jberman[m]> Submitted the view tag PR (https://github.com/monero-project/monero/pull/8061), and have since been investigating multithreaded performance in the wallet to try to realize its maximal performance gain and to potentially help continue the discussion in that PR on which hash algo to use. I've found some more optimization tweaks, some of which seem to potentially be low hanging fruit that have nothing to do with view tags and can
[2021-11-24 17:08:30] <jberman[m]> make it into the next point release
[2021-11-24 17:08:44] <jberman[m]> Hoping to finish that investigation up today, then moving back over to decoy selection work
[2021-11-24 17:11:59] <one-horse-wagon[> I was reading through Document A as written by Rucknium about statistical attacks.  Would like to know has anyone here ever come up with a  Monero data sample with known inputs on which a statistical attack would be performed?  
[2021-11-24 17:13:03] <one-horse-wagon[> Meant to say could be performed.
[2021-11-24 17:15:35] <UkoeHB> me: I updated the Seraphis paper with an efficiency section (and other miscellaneous improvements) https://github.com/UkoeHB/Seraphis . I also investigated the limits of BP+ batching, which is significant for Seraphis-Squashed since inputs require range proofs. I basically found that an aggregate proof with many range proofs (e.g. a BP+ for a tx with many inputs/outputs) doesn't benefit much from batching with aggregate 
[2021-11-24 17:15:35] <UkoeHB> proofs that have few range proofs (but benefits a lot from batching with proofs of similar size). In practice... 1) txs added to the txpool are singularly-validated (although they could be batch-verified if tx volume were high enough, e.g. high enough to batch-verify every 5 seconds), 2) new blocks are validated on a block-wise basis (any more than that would be pointless), 3) synching an old chain can benefit from 
[2021-11-24 17:15:35] <UkoeHB> cross-block batching (e.g. cache 100 blocks worth of range proofs before validating them) which would have significant benefits. The (1) case is the main performance bottleneck since it determines whether a machine can or can't participate in solo mining competitively (there is an optimization problem: tx flow rate vs batching vs CPU power in the worst-case of maximally-sized txs). Also, since (3) can be faster than 
[2021-11-24 17:15:35] <UkoeHB> (1), a machine that can do (1) can always 'catch up' with (3) to the main chain (although if the rate difference isn't one or two orders of magnitude, then it might take a year+... in which case maybe (3) is the true bottleneck).
[2021-11-24 17:17:23] <UkoeHB> My BP+ investigation did not find any disadvantages to Seraphis-Squashed, just complications for analyzing the upper bound of tx throughput.
[2021-11-24 17:18:23] <UkoeHB> one-horse-wagon[: not that I am aware of
[2021-11-24 17:20:49] <UkoeHB> 3. discussion; anything anyone wants to say/discuss?
[2021-11-24 17:21:47] <UkoeHB> It would be nice to make progress on Seraphis address schemes: https://github.com/monero-project/research-lab/issues/92. Has anyone had any new thoughts about that?
[2021-11-24 17:23:19] <dEBRUYNE> Perhaps it can also be a subject in the upcoming dev meeting
[2021-11-24 17:24:05] <rbrunner> Sounds like a good idea
[2021-11-24 17:25:41] <UkoeHB> We also need to discuss requirements to get the multisig PR merged, in that meeting.
[2021-11-24 17:26:07] <UkoeHB> If no one has anything else to say, we can wrap things up. I'll give it a few more minutes.
[2021-11-24 17:27:11] <carrington[m]> I don't see how we can get the sample as you say one-horse-wagon 
[2021-11-24 17:27:45] <carrington[m]> Unless we copy BTC spend data (shaky ground to begin with) and then implement that in a ring sig simulation
[2021-11-24 17:29:27] <carrington[m]> I think Isthmus is looking at some efficient data structure to follow ring sigs through the chain
[2021-11-24 17:30:05] <jberman[m]> UkoeHB: question on BP+ optimization investigation, sounds like that benefit of cross-block batched verifying could be realized in the next HF introducing BP+?
[2021-11-24 17:30:31] <carrington[m]> But any simulation would have to account for the changing decoy selection algorithm over time
[2021-11-24 17:31:50] <UkoeHB> jberman[m]: I think only in-block batch verification is used right now.
[2021-11-24 17:32:18] <moneromooo> Correct.
[2021-11-24 17:33:19] <moneromooo> I don't think I have a PoC for inter block batching. I do have one for txpool batching though (which was rejected for adding latency).
[2021-11-24 17:34:03] <one-horse-wagon[> carrington[m]: That would complicate coming up with decent sample.  If you  assume no one is interested in the past but only the present (which then turns into the future), you would not need to consider past changes in the algorithm.
[2021-11-24 17:34:32] <one-horse-wagon[> The big problem I see is making sure the sample is not skewed in some manner.
[2021-11-24 17:35:15] <carrington[m]> Taking BTC spend distributions and sticking them into XMR is a big assumption. I don't see how else it would be done though.
[2021-11-24 17:36:36] <LyzaL> I'm a little confused, why invent a dataset whole cloth instead of, Idk, using the real blockchain data, then assuming certain inputs are 'known' ?
[2021-11-24 17:37:04] <LyzaL> I guess they have to actually be known nm picking wrong ones would skew things
[2021-11-24 17:40:23] <carrington[m]> <UkoeHB> "proofs that have few range..." <- "High enough to batch verify every 5 seconds" does this correspond to some volume of common-sized transactions?
[2021-11-24 17:41:52] <carrington[m]> I'm reading what you said as "for batch verifying to be worth it the volume has to be high enough to batch verify every seconds" which I'm not understanding
[2021-11-24 17:43:02] <UkoeHB> I guess it would be 'volume high enough that if you don't batch verify then there is a noticeable perf hit on mining'. Right now there is a lot of down-time between verifying each new tx.
[2021-11-24 17:44:22] <carrington[m]> OK that makes more sense to me, thank you
[2021-11-24 17:47:16] <carrington[m]> So we would ideally want mempool batch verification to automagically kick in at some calculated volume. Batch verification across blocks would benefit all synchronization of post-BP+ blocks and so it is worth doing for an upcoming release (not necessarily a network upgrade)
[2021-11-24 17:47:16] <carrington[m]> ^ is this correct?
[2021-11-24 17:48:03] <UkoeHB> Sounds right
[2021-11-24 17:48:23] <UkoeHB> You can also batch-verify BP blocks.
[2021-11-24 17:48:37] <UkoeHB> But not BP & BP+ together.
[2021-11-24 17:49:15] <isthmus> Hey sorry I'm late, between phone calls
[2021-11-24 17:50:17] <carrington[m]> So there could be an upgrade to wallets in the future which would speed up the verification of the whole BP "epoch". Any sort of percentage speedup estimate?
[2021-11-24 17:50:48] <UkoeHB> On the other hand, there are diminishing returns to batch-verification. If blocks are really big, you may not gain much from batching. The main benefits are batching of 'rare' large-aggregate proofs.
[2021-11-24 17:51:44] <UkoeHB> carrington[m]: I doubt it would be better than 5-10% overall.
[2021-11-24 17:52:59] <isthmus> Sorry to interrupt, have a few quick updates, but I need to bounce in a minute
[2021-11-24 17:52:59] <isthmus> @LyzaL you were the closest guess! These 6 cached outputs have been referenced in 65,000 ring signatures
[2021-11-24 17:52:59] <isthmus> (Brace yourself, these transactions are painful to look at... That's 65k ring sigs with effective ring size = 1...)
[2021-11-24 17:52:59] <isthmus> https://xmrchain.net/tx/02E6D22725E405D680D7135410AF51117F91FA2C6A3CC7BACDE985EAD8A2D9A3
[2021-11-24 17:52:59] <isthmus> ... and it's always the same 6 cached decoys in all 65k of them
[2021-11-24 17:52:59] <isthmus> Also, officially submitted our flood analysis for SBC 22 conference last night :)
[2021-11-24 17:53:01] <isthmus> https://usercontent.irccloud-cdn.com/file/McvtYagf/image.png
[2021-11-24 17:53:09] <isthmus> Fingers crossed the organizers are enticed 🤞
[2021-11-24 17:53:54] <isthmus> There's actually > 100k rings with similar issues and consequently effective ring size = 1 but that cluster is the most dramatic
[2021-11-24 17:54:00] <sgp_> isthmus: ooooooooof size 100
[2021-11-24 17:54:33] <isthmus> h/t @Neptune for surfacing the answer from our DB
[2021-11-24 17:55:29] * isthmus bounces to next call
[2021-11-24 17:55:53] <UkoeHB> isthmus: interesting... is this Hyrum's law (learned it recently)?
[2021-11-24 17:55:54] <LyzaL> oh nice :D
[2021-11-24 17:57:07] <carrington[m]> Maybe "new block" batch verification would be worth it for re-orgs?
[2021-11-24 17:57:46] <LyzaL> <isthmus> "there's actually > 100k rings with similar issues..." 100k out of how many?
[2021-11-24 17:58:28] <UkoeHB> might be worth investigating... just requires some dev hours lol (maybe a lot of hours)
[2021-11-24 17:59:26] <nioc> there was an exchange that sent withdrawals with the same 6 ring members and the customers 
[2021-11-24 17:59:28] <nioc> = 7
[2021-11-24 18:00:01] <LyzaL> gross
[2021-11-24 18:01:08] <nioc> was happening in mid 2018, not sure how much before and after that 
[2021-11-24 18:01:24] <UkoeHB> Anyway, I think we can call the meeting. Thanks for attending everyone.
```

# Action History
- Created by: Rucknium | 2021-11-23T06:05:02+00:00
- Closed at: 2021-11-30T20:50:52+00:00
