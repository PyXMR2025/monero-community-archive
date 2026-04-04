---
title: ' Monero Research Lab Meeting - Wed 29 June 2022'
source_url: https://github.com/monero-project/meta/issues/716
author: Rucknium
assignees: []
labels: []
created_at: '2022-06-27T21:18:27+00:00'
updated_at: '2022-07-05T15:51:28+00:00'
type: issue
status: closed
closed_at: '2022-07-05T15:51:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#715 

# Discussion History
## UkoeHB | 2022-06-29T17:54:10+00:00
```
[06-29-2022 17:02:22] <UkoeHB> oh meeting time
[06-29-2022 17:02:33] <Rucknium[m]> Hi
[06-29-2022 17:02:37] <rbrunner> Hello
[06-29-2022 17:02:41] <neromm[m]> Hi all
[06-29-2022 17:02:45] <xmr-ack[m]> Hi
[06-29-2022 17:02:47] <UkoeHB> https://github.com/monero-project/meta/issues/716
[06-29-2022 17:02:47] <UkoeHB> 1. greetings
[06-29-2022 17:02:47] <UkoeHB> hello (sorry was working lol)
[06-29-2022 17:03:29] <jberman[m]> hello
[06-29-2022 17:03:50] <dangerousfreedom> Hello
[06-29-2022 17:04:35] <UkoeHB> 2. updates, what is everyone working on?
[06-29-2022 17:06:14] <dangerousfreedom> I'm still working on writing the codes and explanations for bulletproofs. I took a week of vacation this month so I will be a about a week late to deliver my second working package. But everything is on track. :)
[06-29-2022 17:07:15] <Rucknium[m]> I think I have found a solution to all the challenges in my outline of the plan for OSPEAD. I think in 3-4 weeks I will have a document to submit to the "scientific review committee". If you want to be on that committee, let me know (subject to checks on substantial involvement in the Monero Project).
[06-29-2022 17:07:26] <neromm[m]> I talked to Ukoe and decided to tackle https://github.com/monero-project/monero/issues/7353 (update InProofV2 to V3) and after that implement UnspentProof as described in Zero to Monero. Will start work on it next week because I still have other things planned for this week, but will start getting the picture this week hopefully :D
[06-29-2022 17:07:28] <dangerousfreedom> I'm still scanning the blockchain too and haven't found anything suspicious (I finished the MLSAG era)
[06-29-2022 17:07:52] <UkoeHB> me: 1) simplified the grootle proof implementation in my seraphis library to be less generic (this makes it a lot easier to read and understand); 2) implemented a 'transcript building' system for seraphis, which at the very least makes writing transcripts a lot easier e.g. https://github.com/UkoeHB/monero/blob/ddc41c018cce347d9b6e8a319e0e5e1c47fe4764/src/seraphis/sp_composition_proof.cpp#L101 ); 3) reviewed the multisig audit 
[06-29-2022 17:07:52] <UkoeHB> report from inference ag https://test.rino.io/rino-report-20220626.pdf (no major findings)
[06-29-2022 17:10:08] <UkoeHB> Rucknium[m]: are you aiming for that to be a public document?
[06-29-2022 17:10:53] <Rucknium[m]> (Also special thanks to kayabaNerve and plowsof for troubleshooting an issue with MoneroResearch.info
[06-29-2022 17:12:01] <UkoeHB> 3. we can move to discussion
[06-29-2022 17:12:21] <Rucknium[m]> UkoeHB: Part of it is OK to be public immediately when ready. For other parts of it, that will be "to be determined". I think several people (jberman, isthmus, ArticMine) are leaning toward making everything public once a solution is estimated.
[06-29-2022 17:14:01] <Rucknium[m]> I'm thinking if we go full public, then I can submit it to IACR and/or something like PoPETs in some form.
[06-29-2022 17:14:05] <UkoeHB> Unless your research describes how to do an active attack on user privacy, there shouldn't be any problems with publicizing your work (since it will be public eventually, unless I'm mistaken)
[06-29-2022 17:14:38] <Rucknium[m]> It does describe such an attack. Well, a "passive" attack.
[06-29-2022 17:15:22] <UkoeHB> elaborate? an active attack means taking some actions on the network/chain
[06-29-2022 17:15:25] <Rucknium[m]> As in, observation of the blockchain data without an observer creating their own transactions.
[06-29-2022 17:16:11] <Rucknium[m]> ^ Did that clarify
[06-29-2022 17:16:18] <UkoeHB> if it's not an active attack, then anyone can do that analysis ex post (unless you need to collect network data that wouldn't otherwise be collected)
[06-29-2022 17:16:41] <Rucknium[m]> Yes, anyone could do it ex-post.
[06-29-2022 17:17:06] <UkoeHB> therefore, is there an advantage to not publicizing?
[06-29-2022 17:17:19] <jberman[m]> +1 I lean toward public. Even FloodXMR is an active attack and that should definitely be public
[06-29-2022 17:18:28] <Rucknium[m]> The main advantage to not publicizing is that it would not directly give chain analysis entities another tool in their toolbox.
[06-29-2022 17:19:05] <Rucknium[m]> Security disclosure is not my area of knowledge, so I would mostly defer to others on this.
[06-29-2022 17:19:27] <UkoeHB> are you implying it wouldn't eventually be disclosed? my question is about the timing of disclosure
[06-29-2022 17:19:50] <UkoeHB> I've never heard of research that wasn't disclosed eventually
[06-29-2022 17:20:48] <rbrunner> Not sure, but I think we have a small number of Hacker One entries that to this day are not public
[06-29-2022 17:21:00] <merope> The benefit would have to outweigh the cost - in this case, potentially endangering a significant number of past transactions
[06-29-2022 17:21:10] <Rucknium[m]> It is possible to avoid disclosure, yes. The improved decoy selection distribution could be disclosed without the method of determining it also being disclosed. I know that in the past there have been severe "issues" with cryptographic primitives not having sufficient justification so as to enable "back-dooring". IMHO, these statistical issues don't work like that, but I understand why people have a concern, for sure.
[06-29-2022 17:22:07] <rbrunner> It's a bit optimistic to think we can keep that secret for years, no?
[06-29-2022 17:22:08] <UkoeHB> rbrunner: sure, but did those lead to major code changes with opaque justifications? (guess it's hard to know for sure)
[06-29-2022 17:22:23] <merope> Perhaps the method could be disclosed a certain amount of time after the solution has been implemented
[06-29-2022 17:22:43] <Rucknium[m]> Main benefits: promote additional research into this area by publishing. Other people can examine my solution. Miantain "user trust" in the decoy selection algorithm
[06-29-2022 17:23:20] <Rucknium[m]> Main benefits to disclosure, that is ^
[06-29-2022 17:24:27] <Rucknium[m]> The main argument for not disclosing up to now is that it doesn't make sense to disclose until we have a full solution ready to implement. But then we can re-open the discussion once we have a full solution.
[06-29-2022 17:24:49] <UkoeHB> sure I suppose that's fine
[06-29-2022 17:25:30] <xmr-ack[m]> I would vote for disclosure and publication once a patch is proposed and verified
[06-29-2022 17:25:56] <UkoeHB> are there any other topics? any questions/comments on the multisig audit?
[06-29-2022 17:26:56] <Rucknium[m]> To be clear, the attack is probabilistic in nature. For many Monero users, a probabilistic attack is not relevant to their threat models.
[06-29-2022 17:28:57] <UkoeHB> 'attack' might not be the right word, since it is just an analysis that exposes weakness in the decoy selection algo (to be a little pedantic :p)
[06-29-2022 17:29:53] <jberman[m]> UkoeHB: what are your thoughts on the optimal path forward with multisig from here :)
[06-29-2022 17:31:08] <Rucknium[m]> To continue...it is important that I have some -dev resources for OSPEAD implementation. There are still some questions about some things that are written in C++ in existing codebases. The current estimation method is slow and can be made faster with a C++ implementation. I'm wondering what jberman plans to do for his next CCS. Are you still interested in decoy work? I think mj-xmr is interested, but I wanted to see if others
[06-29-2022 17:31:08] <Rucknium[m]> are too. 
[06-29-2022 17:32:26] <UkoeHB> at this point I'm fine with merging 8149, doesn't seem like we will get any more reviews or useful comments; would be nice to expedite a fix for the fund burning issue after that; can discuss it more at the dev meeting tomorrow
[06-29-2022 17:33:32] <rbrunner> That's good news
[06-29-2022 17:34:02] <rbrunner> But well, after basically 0 bad surprises from the review not merging would probably hard to defend
[06-29-2022 17:36:05] <jberman[m]> UkoeHB: SGTM
[06-29-2022 17:36:58] <jberman[m]> Rucknium: if mj-xmr is interested they can take it, but yep I'm happy to help/provide eyes/code on it where needed as long as it's settled it'll all be made public. I was thinking for my next CCS to be a month long to complete the background sync cache + do more PR review work
[06-29-2022 17:38:27] <Rucknium[m]> Right. Now I remember that a sticking point is you want to make sure that everything will be disclosed if you were to work on it, which is totally fair.
[06-29-2022 17:39:56] <Rucknium[m]> I am thinking that we will want about two months of post-hardfork data for the final estimation, by the way.
[06-29-2022 17:41:38] <jberman[m]> The reason to segregate post-HF data is because we'll be sure as we can be that everyone running the core wallet software will be running the latest algo?
[06-29-2022 17:43:00] <Rucknium[m]> No, although that helps a bit. We can't be sure that everyone will be running the wallet2 algorithm, but nonstandard ones should be less prevalent. I gave a reason to you and isthmus.
[06-29-2022 17:44:22] <Rucknium[m]> To be clear, on-chain nonstandard decoy selection algorithms will be dealt with in OSPEAD.
[06-29-2022 17:44:31] <ArticMine[m]> I would not mind seeing the reason. I have my suspicions 
[06-29-2022 17:45:16] <Rucknium[m]> ArticMine: I will PM you. Would you like to be on the scientific review panel? I assumed you would.
[06-29-2022 17:45:32] <ArticMine[m]> Which I will not reveal publicly 
[06-29-2022 17:46:02] <ArticMine[m]> Yes I am interested 
[06-29-2022 17:46:13] <Rucknium[m]> isthmus said he is willing to be a "minor reviewer"
[06-29-2022 17:47:47] <UkoeHB> we are closing in on the end of the meeting; anyone have any burning questions to get out?
[06-29-2022 17:52:12] <UkoeHB> ok seems like we are done; thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-06-27T21:18:27+00:00
- Closed at: 2022-07-05T15:51:28+00:00
