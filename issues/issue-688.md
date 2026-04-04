---
title: Monero Research Lab Meeting - Wed 13 April 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/688
author: Rucknium
assignees: []
labels: []
created_at: '2022-04-12T02:14:17+00:00'
updated_at: '2022-04-16T05:08:43+00:00'
type: issue
status: closed
closed_at: '2022-04-16T05:08:42+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Reduce MRL meeting frequency?

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

#686 

# Discussion History
## UkoeHB | 2022-04-13T19:05:13+00:00
```
[04-13-2022 17:00:00] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/688
[04-13-2022 17:00:00] <UkoeHB> 1. greetings
[04-13-2022 17:00:00] <UkoeHB> hello
[04-13-2022 17:00:16] <endogenic> 👍
[04-13-2022 17:00:21] <Rucknium[m]> Hi
[04-13-2022 17:00:41] <dangerousfreedom> Hello
[04-13-2022 17:01:12] <xmr-ack[m]> hey
[04-13-2022 17:02:53] <jberman[m]> howdy
[04-13-2022 17:02:55] <UkoeHB> 2. in case anyone missed it, we can get this out of the way https://blog.trailofbits.com/2022/04/13/part-1-coordinated-disclosure-of-vulnerabilities-affecting-girault-bulletproofs-and-plonk/
[04-13-2022 17:03:05] <UkoeHB> short story short: does not affect monero
[04-13-2022 17:03:58] <UkoeHB> any questions on that disclosure?
[04-13-2022 17:04:58] <xmr-ack[m]> Not being as familiar with bulletproofs, why exactly does it not affect Monero?
[04-13-2022 17:05:37] <moneromooo> Monero's was written by Sarang, who was careful.
[04-13-2022 17:08:19] <Rucknium[m]> The blog post claims:
[04-13-2022 17:08:19] <Rucknium[m]> >Why is this type of vulnerability so widespread? It really comes down to a combination of ambiguous descriptions in academic papers and a general lack of guidance around these protocols.
[04-13-2022 17:08:51] <Rucknium[m]> Is it true that there is this shortcoming in the cryptography space?
[04-13-2022 17:09:27] <UkoeHB> xmr-ack[m]: The issue was the paper did not have a complete implementation guideline, so anyone going directly off the paper would have made a certain small error in the Fiat-Shamir transform (neglecting to hash some public variables). Monero's implementation followed best practices for FS transforms, which prevented that issue.
[04-13-2022 17:11:56] <UkoeHB> Rucknium[m]: yes, best practices for implementing cryptographic protocols are not well-disseminated among general developers
[04-13-2022 17:13:52] <UkoeHB> Also, afaik most crypto professionals aren't implementing advanced algorithms, they are dealing with data encryption and encrypted channels. It's mainly in the cryptocurrency and experimental crypto spaces that these big protocols are implemented. 
[04-13-2022 17:14:28] <dEBRUYNE> UkoeHB: Does it list the projects that are affected somewhere?
[04-13-2022 17:14:40] <UkoeHB> yes it's in the blog post
[04-13-2022 17:15:50] <UkoeHB> Most crypto professionals aren't rolling their own crypto from scratch *. They are following some highly-scrutizined specification.
[04-13-2022 17:16:31] <UkoeHB> Anyway, we can move on
[04-13-2022 17:16:55] <UkoeHB> 3. updates, what is everyone working on? monerotopia was last week, it was great to meet several people
[04-13-2022 17:18:37] <jberman[m]> Aside from monerotopia which was sweet, been working on PR review (my list atm: 8046 [done], 7760 [in progress], 8076 [in progress]), digging into a sporadic bug with tx broadcast (8251, 6929), and submitted an updated proposal for subaddresses in light wallet servers in collab with endogenic here: https://github.com/monero-project/meta/pull/647
[04-13-2022 17:19:24] <UkoeHB> me: I'm continuing work on my seraphis library. I realized getting an accurate minimum fee oracle will be a huge pita, so I'll probably just make a trivial mockup and move on...
[04-13-2022 17:19:26] <Rucknium[m]> Working with jberman and mj-xmr on translating some C++ to statistics language. And doing some prototyping of statistical models with some simulated data.
[04-13-2022 17:21:56] <dangerousfreedom> Im writing some code and text to understand and explain mlsag and borromean ring signatures. I think I will have something to present by the end of the month. 
[04-13-2022 17:22:59] <UkoeHB> 3. discussion: any topics to discuss? questions/comments?
[04-13-2022 17:23:52] <dEBRUYNE> UkoeHB: Thanks
[04-13-2022 17:23:59] <xmr-ack[m]> Me: Unfortunately, I couldn't attend Monerotopia :(. But I do have some updates in regards to my work with MAGIC. I have a working implementation of two rudimentary machine learning models and have been training them on a preliminary dataset. I want to clarify that the preliminary dataset has many flaws... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/581aa6186c27f11139c90f09926efa9e71009791)
[04-13-2022 17:24:30] <xmr-ack[m]>  * Me: Unfortunately, I couldn't attend Monerotopia :(. But I do have some updates in regards to my work with MAGIC. I have a working implementation of two rudimentary machine learning models and have been training them on a preliminary dataset. I want to clarify that the preliminary dataset has many flaws and that most of the transactions were collected with an (unrealistic) 20-minute uniform delay. I am currently refining the
[04-13-2022 17:24:30] <xmr-ack[m]> process of collecting a new dataset that does reflect real user spending patterns.
[04-13-2022 17:24:30] <xmr-ack[m]> That being said, after training on an undersampled dataset removing the possibility of a guess newest heuristic, I am seeing accuracies upwards of three times random guessing classifying the true spend of an arbitrary ring with no outside information.
[04-13-2022 17:24:30] <xmr-ack[m]> Metrics:
[04-13-2022 17:24:30] <xmr-ack[m]> Random Forest Testing Accuracy:                   23.41%
[04-13-2022 17:24:30] <xmr-ack[m]> Random Forest Weighted F-1 Score:                     19%
[04-13-2022 17:24:30] <xmr-ack[m]> Gradient Boosted Classifier Testing Accuracy:       27.40%
[04-13-2022 17:24:31] <xmr-ack[m]> Gradient Boosted Classifier Weighted F-1 Score:   26%
[04-13-2022 17:24:31] <xmr-ack[m]> Feature Importance (Top 5):
[04-13-2022 17:24:32] <xmr-ack[m]> Inputs.1.Time_Delta_From_Newest_Ring_To_Block:    13.07%
[04-13-2022 17:24:32] <xmr-ack[m]> Total_Block_Tx_Fees:                                  10.97%
[04-13-2022 17:24:33] <xmr-ack[m]> Inputs.0.Time_Deltas_Between_Ring_Members.9_10:   4.98%
[04-13-2022 17:25:46] * xmr-ack[m] uploaded an image: (112KiB) < https://libera.ems.host/_matrix/media/r0/download/matrix.org/dqAGJKuAviBOFlLETUwqOVcZ/image.png >
[04-13-2022 17:27:57] <Rucknium[m]> My commentary (I've seen these results prior to now): This underlines again that when there is a substantial mismatch between the decoy selection algorithm and the real spend age distribution, statistical methods can be used to narrow down which ring member is the real spend.
[04-13-2022 17:28:52] <Rucknium[m]> And here there was a large mismatch, since the "real user behavior" in this synthetic data was uniform over just 20 minutes.
[04-13-2022 17:28:53] <UkoeHB> Thanks xmr-ack[m]
[04-13-2022 17:30:34] <Rucknium[m]> Also the feature importance is interesting, but it is hard to know if there is any real problem with some of these features without some sort of confidence interval or p-value on these estimated feature importance results. Since the feature importance may be nonzero just due to sampling error.
[04-13-2022 17:31:56] <UkoeHB> On a different topic, I want to point out that Monero multisig is capped at 16 group members for efficiency reasons during account generation. I was assuming people who want to use multisig would see that limit in the code, but maybe not... (looking at Thorchain). A different approach to key generation (see the FROST paper) is much more efficient when M < N - 1 (enabling larger groups generically), but my focus was on 
[04-13-2022 17:31:56] <UkoeHB> N-of-N and (N-1)-of-N for efficient escrow. I will probably implement a FROSTy key generation backend for multisig in my seraphis branch (but probably won't port that to master, since current multisig uses round-robin signing but you need aggregation signing for FROST - which I have in my seraphis branch).
[04-13-2022 17:32:00] <Rucknium[m]> In other words, if there is some feature that the machine learning algorithm identifies as helping classify the real spend, then it would make sense to investigate further and see if there is some sort of problem with the code or the protocol.
[04-13-2022 17:33:35] <UkoeHB> Rucknium[m]: I think most features that can affect distinguishability can be manually identified, although it would be helpful to get a sense of their significance in practice.
[04-13-2022 17:35:10] <UkoeHB> isthmus and neptune have done a bunch of research into distinguishable features (numerical counts of different fingerprints), but did not extend that to transaction tracing
[04-13-2022 17:35:21] <moneromooo> One problem is that ground truth is kinda biased due to self selection (I forget the exact term).
[04-13-2022 17:36:03] <moneromooo> ie, the rings you know the real spend for will not be randomly selected from the set of all rings.
[04-13-2022 17:36:24] <moneromooo> So using this as a proxy for ground truth will bias you.
[04-13-2022 17:36:46] <moneromooo> I think. Not a statistician. etc.
[04-13-2022 17:37:22] <UkoeHB> makes sense to me
[04-13-2022 17:38:26] <mj-xmr[m]> The more I think we need to look for the ground truth in what the code generates and simulate the situations, rather than only relying on past data.
[04-13-2022 17:39:01] <mj-xmr[m]> (in search of ground truth, I mean)
[04-13-2022 17:39:56] <UkoeHB> I want to implement binning in seraphis this week. There are two choices: A) completely deterministic binning (selection distribution is baked into consensus), B) partially deterministic binning (only bin members are deterministically distributed around their bin locus, but each bin's locus is manually specified).
[04-13-2022 17:39:59] <jberman[m]> seems a +1 for binning to me too, because the gamma AFAIU is pulled from just a subset of rings in which the real could be identified, rather than all rings. binning mitigates weakness in an incorrect gamma
[04-13-2022 17:42:10] <jberman[m]> reasoning for B was to avoid tying the algo to consensus to allow changes without a hard fork right?
[04-13-2022 17:42:19] <Rucknium[m]> UkoeHB: To go back to the manual identification vs. machine learning identification: the 5th most important feature, according to these preliminary results, is transaction size. I don't know of any obvious issue with transaction size that would help identify the real spend, so this ML approach can extend our knowledge of transaction uniformity defects beyond what was previously theorized by isthmus, neptune, and others.
[04-13-2022 17:42:27] <UkoeHB> The advantages of (A): less data in a tx (maybe 30-80 bytes), less room for implementation variance that can open anonymity puddles.
[04-13-2022 17:42:27] <UkoeHB> The advantages of (B): we aren't stuck with a fixed selection distribution, it's a lot easier to implement.
[04-13-2022 17:43:31] <moneromooo> I can think of one reason tx size identifies the real spend:
[04-13-2022 17:44:23] <UkoeHB> tx size can be decomposed to input/output count + tx extra fields.
[04-13-2022 17:44:33] <moneromooo> A common reason for large txes is many input txes, which are typically made to consolidate small outputs, like dust etc. These are usually old and you consolidate once you have to after spending the rest.
[04-13-2022 17:44:56] <moneromooo> Another is pool payments, paying to many people. High churn so typically new outputs.
[04-13-2022 17:45:25] <moneromooo> First case will have two outputs, first ring member. Second case, more than two outs, last or close to last ring member.
[04-13-2022 17:46:03] * xmr-ack[m] sent a code block: https://libera.ems.host/_matrix/media/r0/download/libera.chat/7e23c0d3faf278d7169c019a2d3614221d8e5a9b
[04-13-2022 17:46:04] <moneromooo> s/many intput txes/many inputs/
[04-13-2022 17:46:14] <Rucknium[m]> UkoeHB: How does deterministic ring member selection affect tx verification time? Also, I have been trying to understand your deterministic ring selection proposal on github, but I feel that I'm missing something. Is there some cryptographic knowledge I need to understand it?
[04-13-2022 17:46:26] <moneromooo> BTW, if you write too long lines, your message gets omitted, and replaced by a url.
[04-13-2022 17:46:43] <UkoeHB> there's no cryptography other than a hash function
[04-13-2022 17:48:01] <UkoeHB> it shouldn't have a noticeable effect on tx verification time
[04-13-2022 17:50:13] <Rucknium[m]> Last time we talked about enforcement of decoy selection, there was enthusiasm for enforcement at the node level rather than the consensus level. Could Seraphis's deterministic decoy selection be written in a way that `monerod` checks it in the mempool, but does not declare blocks invalid if there are txs mined that do not conform?
[04-13-2022 17:51:30] <UkoeHB> You could do that, but I feel it is a bit of scope creep for nodes
[04-13-2022 17:52:48] <jberman[m]> <Rucknium[m]> "UkoeHB: How does deterministic..." <- The mapping probability to cdf to output index was the most difficult part understanding it for me. I wrote up some code that made it click for me a while back that might help, will share once I find it Rucknium  
[04-13-2022 17:53:28] <jberman[m]> This paper is super helpful: https://spar.isi.jhu.edu/~mgreen/mixing.pdf , and a presentation on it was given that helped me too that I can't find right now
[04-13-2022 17:54:44] <Rucknium[m]> jberman: Mainly I don't understand how the real spend is made indistinguishable from the deterministically-selected decoys. Trying to understand that.
[04-13-2022 17:56:46] <UkoeHB> jberman[m]: damn I lost that presentation...
[04-13-2022 17:57:56] <moneromooo> The obvious method is to include an offset, selected to that one of the deterministic picks matches the real spend.
[04-13-2022 17:58:09] <moneromooo> selected so that...
[04-13-2022 17:58:15] <UkoeHB> Rucknium[m]: you generate a random set, then shift that set so a random member lands on the real spend
[04-13-2022 18:00:19] <Rucknium[m]> Ah ok. Great. Might that give you gaps in the beginning or end of the distribution, though? 
[04-13-2022 18:00:38] <UkoeHB> why?
[04-13-2022 18:00:44] <moneromooo> The offset will tend to be large for old spends.
[04-13-2022 18:01:04] <Rucknium[m]> And it seems more feasible with Seraphis-sized ring member counts rather than 11 or 16
[04-13-2022 18:01:16] <UkoeHB> you transform the random set into a uniform space before rotating, then transform back into the real selection space
[04-13-2022 18:01:18] <moneromooo> Though I suppose that, depending on the generation algorithm, you might be able to brute force one with an old spend and small offset...
[04-13-2022 18:01:58] <UkoeHB> we are at the end of the meeting, thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-04-12T02:14:17+00:00
- Closed at: 2022-04-16T05:08:42+00:00
