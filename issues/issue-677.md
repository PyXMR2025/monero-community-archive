---
title: Monero Research Lab Meeting - Wed 23 March 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/677
author: Rucknium
assignees: []
labels: []
created_at: '2022-03-22T03:40:23+00:00'
updated_at: '2022-03-29T14:15:03+00:00'
type: issue
status: closed
closed_at: '2022-03-29T14:15:03+00:00'
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

#674 

# Discussion History
## UkoeHB | 2022-03-23T17:48:57+00:00
```
[03-23-2022 17:03:07] <rbrunner> Meeting time?
[03-23-2022 17:03:34] <Rucknium[m]> Meeting time!
[03-23-2022 17:04:20] <UkoeHB> ah my bad, meeting time
[03-23-2022 17:04:37] <UkoeHB> https://github.com/monero-project/meta/issues/677
[03-23-2022 17:04:37] <UkoeHB> 1. greetings
[03-23-2022 17:04:37] <UkoeHB> hello
[03-23-2022 17:04:45] <UkoeHB> sorry, got distracted writing code :p
[03-23-2022 17:05:19] <rbrunner> Hello
[03-23-2022 17:05:29] <dangerousfreedom> Hi!
[03-23-2022 17:05:34] <wernervasquez[m]> Hi
[03-23-2022 17:05:38] <Rucknium[m]> Hello. (By the way, last meeting's issue (#674) needs to have the meeting log posted.)
[03-23-2022 17:06:06] <jberman[m]> :waves:
[03-23-2022 17:07:50] <UkoeHB> Rucknium[m]: done
[03-23-2022 17:08:00] <UkoeHB> 2. updates, what is everyone working on?
[03-23-2022 17:09:57] <jberman[m]> been working mostly on background wallet scanning-related tasks in Monerujo, planning to provide Ruck with a step-by-step description of the decoy selection algo so they can potentially turn that into a mathematical definition
[03-23-2022 17:10:04] <dangerousfreedom> Im still working on my Monero Python Inflation Checker... I think I understand MLSAG txs now. I also have a Python script working to verify a simple tx.
[03-23-2022 17:10:11] <Rucknium[m]> I am proceeding with a two-pronged strategy to identify nonstandard decoy selection algorithms. The first is by asking wallet and service developers about their algorithms: https://github.com/monero-project/research-lab/issues/99 Thank you to those who have contributed so far.
[03-23-2022 17:11:06] <UkoeHB> me: Still working on multisig stuff. Yesterday I completed a 'multisig account conversion' workflow that lets you convert a group of cryptonote-compatible multisig accounts to seraphis-compatible accounts. This is necessary because the base spendkey of seraphis uses a different generator (generator U instead of G), so the multisig key must be recreated on the new generator. I had to implement a new dual-base vector 
[03-23-2022 17:11:06] <UkoeHB> proof for robustly recreating keys, which is here: https://github.com/UkoeHB/monero/blob/seraphis_lib/src/multisig/dual_base_vector_proof.h.
[03-23-2022 17:11:45] <Rucknium[m]> The second prong is to partition transaction by certain nonstandard features, such as `unlock`_time` and `tx_extra` and examine the ring member age distribution of the different transaction classes.
[03-23-2022 17:13:44] <UkoeHB> 3. Let's try something new today. What are things people want to do / plan to do in the coming weeks?
[03-23-2022 17:14:16] <Rucknium[m]> In the next few days, the MAGIC Monero Fund will have an announcement about xmr-ack  (ACK-J)'s machine learning grant proposal.
[03-23-2022 17:15:53] <rbrunner> As soon as the header files from the Seraphis wallet PoC stabilize and become available I intend to work on wallet migration strategies in earnest 
[03-23-2022 17:16:48] <UkoeHB> me: I have some more work to do related to this PR https://github.com/monero-project/monero/pull/8220. I also want to get multisig seraphis txs implemented (all the pieces are ready now I think: aggregation signing, account conversions, composition proof multisig methods with a robust nonce handler). Monerotopia is coming up in 2 weeks, where I will be presenting about seraphis (still need to get the content figured 
[03-23-2022 17:16:48] <UkoeHB> out).
[03-23-2022 17:17:38] <UkoeHB> rbrunner: yeah sorry, this multisig stuff has been taking a lot longer than expected
[03-23-2022 17:18:00] <rbrunner> No problem :) You mean that 8220 will get some changes?
[03-23-2022 17:18:10] <rbrunner> Thinking about testing that
[03-23-2022 17:18:13] <UkoeHB> only small ones
[03-23-2022 17:18:47] <UkoeHB> however, a workflow change to multisig messaging is coming
[03-23-2022 17:19:15] <rbrunner> ?
[03-23-2022 17:19:23] <UkoeHB> basically you need to re-broadcast the final key generation messages to other participants, once your account is complete
[03-23-2022 17:19:42] <dangerousfreedom> I was wondering if I can open a CCS proposal for that project that I am working on. From my side, it would be awesome at this moment of my life, to work in this project. I believe I can evaluate the workload and the expected results now. From the community side, I believe I could address many of the questions about inflation that people come with frequently. I would also to have closer contact with you guys as I certainly
[03-23-2022 17:19:42] <dangerousfreedom> will need your support for the questions that appear. Do you guys think it is doable? If you guys, think it is a nice idea, I will write the proposal of what I would like to do tonight and send here. Otherwise, I would continue still working on this project but in my pace and answering only my concerns for now. :)
[03-23-2022 17:20:08] <UkoeHB> They can be ignored if you already got those messages from someone else, but this 'rebroadcast' step is necessary for robust/reliable results in the generic case.
[03-23-2022 17:21:26] <UkoeHB> dangerousfreedom: I think the work you have done so far is very impressive, and demonstrates you have the skill and perseverance to get a good end result.
[03-23-2022 17:21:34] <rbrunner> "Do you guys think it is doable?" I don't see what speaks against it. I think you could people getting intererested.
[03-23-2022 17:21:42] <Rucknium[m]> In the next weeks, I will hopefully be setting up the scientific review panel from my OSPEAD CCS proposal, since I am getting close to finishing the completed research plan for exactly how the real spend age distribution will be fit. Right now my working list is Artic Mine, isthmus, binary Fate, jberman, and Syksy. I am open to others joining, but note that members of the panel have to be trusted members of the community. That
[03-23-2022 17:21:42] <Rucknium[m]> way, I will be ready to "hit the ground running" once the hard fork takes effect on mainnet.
[03-23-2022 17:24:39] <rbrunner> UkoeHB: Certainly progress, a more robust workflow, I just wonder whether how much farther into the future that may push the hardfork if we want to include such a heavy change
[03-23-2022 17:24:40] <Rucknium[m]> dangerousfreedom: The question of auditability of the supply and worries about counterfeiting bugs appear pretty frequently on Reddit and Matrix/IRC, so I think you could get support for an independent effort so that we could point to it when the questions come up again
[03-23-2022 17:25:00] <dangerousfreedom> Awesome! I feel confident now to give timelines and expected results. I believe I have a minimum understanding of what should be done, the difficulties and how to get people interested in solving/understanding this issue. It would also be great to address people's concerns and give some good resources for debating this question :)
[03-23-2022 17:25:28] <UkoeHB> rbrunner: it won't affect the RPC interface, but may require changes in MMS, guess we will see
[03-23-2022 17:25:50] <rbrunner> dangerousfreedom: Just mentally prepare for quite a number of people that don't want to get convinced :)
[03-23-2022 17:26:57] <dangerousfreedom> Hahahaha I'm just trying to understand as the others do also :p
[03-23-2022 17:26:57] <dangerousfreedom> If there are questions that I dont understand I will turn to you guys haha
[03-23-2022 17:27:13] <rbrunner> Yeah, after the multisig address gets known, the MMS currently thinks all is well and stops ...
[03-23-2022 17:28:06] <UkoeHB> I'll clarify more about why rebroadcasting is necessary in the PR
[03-23-2022 17:28:15] <jberman[m]> heavy +1 to dangerousfreedom ! What you're working on I think is an awesome complement to educational materials out there like ZtM/Mastering Monero, I think people who want to understand Monero better will find solid value in it, myself included
[03-23-2022 17:28:25] <rbrunner> I don't have an overview anyway where hardfork preparation currently stands ...
[03-23-2022 17:30:42] <UkoeHB> still kinda stuck on multisig stuff sadly
[03-23-2022 17:31:08] <rbrunner> Such a rebroadcast might mess up current MMS workflows pretty badly, if I think about it. Need to check after you documented.
[03-23-2022 17:31:50] <rbrunner> Not that anybody uses the MMS, but hardforking and not having it working at all would be ... suboptimal :)
[03-23-2022 17:33:46] <UkoeHB> should be ready later today
[03-23-2022 17:34:04] <UkoeHB> 4. we can move on - any other topics to discuss? questions/comments?
[03-23-2022 17:34:07] <rbrunner> Splendid.
[03-23-2022 17:34:49] <Rucknium[m]> Maybe this is a -dev topic, but is there a sense of how long the "grace period" should be in the "double fork" where both 11- and 16-size rings are allowed?
[03-23-2022 17:35:38] <rbrunner> Hmmm, as short as possible? I think a former such grace period was only a single day
[03-23-2022 17:36:49] <gingeropolous> yeah, a single day was used in the past. i think its just meant to cover txs that are in the txpool at time of fork
[03-23-2022 17:37:18] <midipoet> I would like to let everyone in MRL know that MoneroKon venue is confirmed and we would really appreciate if researchers would think about presenting some of their research. The CfP is found at monerokon.com
[03-23-2022 17:37:22] <rbrunner> For this, even a day should be generous
[03-23-2022 17:38:44] <midipoet> The goal is to present as high quality research as possible, so it would be great if some here thought about putting in a proposal. Can be for a talk, a workshop, or even a panel discussion. Remote presentations are also possible, if traveling is an issue. The event is June18-19 in Lisbon, Portugal.
[03-23-2022 17:42:41] <Rucknium[m]> midipoet: Thanks! The 1000 character limit for the abstract seems a bit short. Is there an opportunity for applicants to submit an additional attachment explaining the proposed talk/workshop?
[03-23-2022 17:44:16] <midipoet> Rucknium[m]: that is a good question. if you are having trouble with the limit, you could just paste a url in the abstract section, that points to a pdf, etc. 
[03-23-2022 17:44:52] <midipoet> we do prefer brevity, but perhaps the 1000 character limit is a bit too concise
[03-23-2022 17:48:02] <UkoeHB> It seems like we are at the end of the meeting. Thanks for attending everyone.
```

# Action History
- Created by: Rucknium | 2022-03-22T03:40:23+00:00
- Closed at: 2022-03-29T14:15:03+00:00
