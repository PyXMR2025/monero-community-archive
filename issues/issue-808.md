---
title: Monero Research Lab Meeting - Wed 08 March 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/808
author: Rucknium
assignees: []
labels: []
created_at: '2023-03-06T18:39:12+00:00'
updated_at: '2023-03-14T01:00:53+00:00'
type: issue
status: closed
closed_at: '2023-03-14T01:00:53+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Authors of ["A Holistic Security Analysis of Monero Transactions"](https://eprint.iacr.org/2023/321.pdf) join the meeting.

3. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

4. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

5. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

6. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

7. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

8. Any other business

9. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#803 

# Discussion History
## ACK-J | 2023-03-06T22:19:16+00:00
The authors from the paper ["A Holistic Security Analysis of Monero Transactions"](https://eprint.iacr.org/2023/321.pdf)  will be joining to answer any questions.

## UkoeHB | 2023-03-08T18:04:03+00:00
`[03-08-2023 17:01:09] <ghostway[m]> Hello`
`[03-08-2023 17:01:17] <shalit[m]> Hello`
`[03-08-2023 17:01:23] <UkoeHB> meeting time`
`[03-08-2023 17:01:23] <UkoeHB> 1. greetings`
`[03-08-2023 17:01:23] <UkoeHB> hello`
`[03-08-2023 17:01:24] <CasCremers[m]> Hello`
`[03-08-2023 17:01:27] <bewa_c[m]> Hello`
`[03-08-2023 17:01:30] <dangerousfreedom> Hello`
`[03-08-2023 17:01:34] <UkoeHB> agenda: https://github.com/monero-project/meta/issues/808`
`[03-08-2023 17:02:02] <ArticMine[m]> Hello `
`[03-08-2023 17:02:02] <Rucknium[m]> Hi`
`[03-08-2023 17:02:14] <jlo[m]> Hi`
`[03-08-2023 17:02:31] <kayabanerve[m]> Hi`
`[03-08-2023 17:03:36] <hbs[m]> Hi`
`[03-08-2023 17:04:20] <UkoeHB> 2. today we have the authors of this significant new preprint https://eprint.iacr.org/2023/321 here to discuss their paper/answer questions`
`[03-08-2023 17:04:30] <rbrunner> Hello`
`[03-08-2023 17:04:51] <UkoeHB> CasCremers[m]: do you want to briefly introduce your team and your paper?`
`[03-08-2023 17:06:03] <CasCremers[m]> Hi, we are three academics at the CISPA Helmholtz Center for Information Security in Germany `
`[03-08-2023 17:07:23] <CasCremers[m]> Our paper tries to give a more complete analysis of the security of Monero transactions as opposed to the isolated analyses previously`
`[03-08-2023 17:08:02] <CasCremers[m]> Any particular questions you might want to see answered?`
`[03-08-2023 17:08:12] <CasCremers[m]> (We're not terribly familiar with this format)`
`[03-08-2023 17:08:40] <dangerousfreedom> CC: First, thank you for the very nice work. It is nice to see research being done with Monero and I enjoyed reading it :)... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/aebf87ce76793de7899c44055b2d19c988410975>)`
`[03-08-2023 17:09:34] <blankpage[m]> I can't be present throughout this meeting but I'd like to remind attendees of these meetings that they are welcome to submit a proposal to present at Monerokon in Prague in June, and to spread the message to other relevant researchers`
`[03-08-2023 17:09:35] <blankpage[m]> https://cfp.monerokon.com/2023/cfp`
`[03-08-2023 17:09:36] <UkoeHB> CasCremers[m]: thanks, the format is fairly informal. I am currently reviewing your paper, it just came out so I am only ~1/4 through it. Did you find anything interesting/surprising during your research?`
`[03-08-2023 17:10:12] <CasCremers[m]> A1: We have a limitations section that describes part of the analysis that were not completed yet and that would interesting to investigate. (But we currently don't have a project tailored towards this)`
`[03-08-2023 17:12:08] <CasCremers[m]> A2: Our analysis tries to walk the fine line between theoretical and practical. We did check the code for several questions we had, but of course the analysis is theoretical.`
`[03-08-2023 17:13:02] <bewa_c[m]> A3: I briefly looked at the issues you linked. It seems that they are related to the fact that Monero uses Ed25519, i.e., a non-prime order group. As stated in the limitations, we assume that we have a prime order group. This is common in cryptography. `
`[03-08-2023 17:14:42] <Rucknium[m]> Thank you for joining us today. Do you want to get funding for studying Monero multisig? It is still considered experimental since there is not a formal security proof. You can get funding at https://monerofund.org/apply_research or https://ccs.getmonero.org/what-is-ccs/`
`[03-08-2023 17:15:14] <jlo[m]> <UkoeHB> "CC: thanks, the format is fairly..." <- On the practical side, we did not find anything particularly surprising. That is to say, that we confirmed that Monero's transaction system is secure in our model, as expected. However, we encountered many technical obstacles during the proof due to the non-standard uses of the crypto in the Monero transaction system. These make our paper interesting from a theoretical point of view`
`[03-08-2023 17:15:14] <jlo[m]> also`
`[03-08-2023 17:16:33] <UkoeHB> CasCremers[m]: I noticed your ring signature analysis is > 20 pages, and I recall ring signatures have a history of difficult-to-assemble security models. How do you guys feel about your solution?`
`[03-08-2023 17:16:39] <CasCremers[m]> Wrt Ed25519: In a separate context, some of us actually actively worked on this problem: https://eprint.iacr.org/2020/823 `
`[03-08-2023 17:16:39] <CasCremers[m]> but that is not directly used in the Monero proof`
`[03-08-2023 17:16:54] <vtnerd> sorry, just sitting here ignoring this room, now present`
`[03-08-2023 17:18:30] <Rucknium[m]> Formal security proofs for Monero multisig are considered high-to-medium-priority, but there is not an active effort (that we are aware of) to create them.`
`[03-08-2023 17:18:32] <CasCremers[m]> Rucknium[m]: We would be interested in setting up a further project on Monero with PhD students, and would be happy to learn more about the opportunities. Maybe this is something for a dedicated conversation?`
`[03-08-2023 17:18:48] <bewa_c[m]> UkoeHB: The main aspect here is that the standard notions for linkable ring signatures are not enough: For example, the keys that an honest user uses are potentially derived by the adversary from the honest users address. This is why we have to analyze linkable ring signatures with respect to the key derivation. I think this is the main challenge here. `
`[03-08-2023 17:19:34] <Rucknium[m]> CC: Yes that sounds great. I am on the committee that approves grants for the MAGIC Monero Fund, so I can help you there.`
`[03-08-2023 17:19:47] <dangerousfreedom> <bewa_c[m]> "A3: I briefly looked at the..." <- Yes. One issue is about that. The other is that there are some wrong signatures that dont strictly obey the ring signature equations. I am pretty convinced that it is only a serialization problem but anyway it is always good to formally settle things down.`
`[03-08-2023 17:20:06] <dangerousfreedom> Thank you for the answers bewa_c CC  !`
`[03-08-2023 17:21:10] <CasCremers[m]> We would be very interested in removing the limitations, and moving closer to the implementation. However, this is very challenging work and it is not always clear how to compose the results.`
`[03-08-2023 17:22:07] <UkoeHB> bewa_c[m]: I see, yeah your analysis might be the first to unify the consensus/proof side with the address side.`
`[03-08-2023 17:23:00] <CasCremers[m]> For example, we are not yet considering privacy in this work.`
`[03-08-2023 17:24:55] <dangerousfreedom> <CasCremers[m]> "We would be interested in..." <- Nice! I guess Rucknium is the man to talk to. From my side, to be honest, I would be happy also to dedicate 100% of my time to Monero and do a PhD :p`
`[03-08-2023 17:25:02] <jlo[m]> UkoeHB: I am not sure this is quite accurate. We treat the consensus layer as a black box (i.e., assume it is given and works correctly). Our analysis concerns only the security of transactions on the ledger`
`[03-08-2023 17:25:42] <UkoeHB> jlo[m]: by consensus I mean transaction validation rules checked by consensus (e.g. that proofs are valid)`
`[03-08-2023 17:26:29] <UkoeHB> jlo[m]: figure 3 VerTx() basically`
`[03-08-2023 17:26:51] <jlo[m]> Ok, in that case, I agree with your initial comment`
`[03-08-2023 17:27:44] <Rucknium[m]> What motivated you to write this paper? Why did you pick Monero to study?`
`[03-08-2023 17:30:00] <CasCremers[m]> Rucknium[m]: We had been been studying signatures and bip32, and we are interested in real-world constructions an d proof techniques for them`
`[03-08-2023 17:30:07] <CasCremers[m]> > <@rucknium:monero.social> What motivated you to write this paper? Why did you pick Monero to study?`
`[03-08-2023 17:30:07] <CasCremers[m]>  * We had been been studying signatures and bip32, and we are interested in real-world constructions, and proof techniques for them`
`[03-08-2023 17:30:37] <CasCremers[m]> CasCremers[m]: This seemed like a sizeable challenge of scientific interest from a proof technique angle`
`[03-08-2023 17:32:40] <UkoeHB> It's certainly a very impressive paper, and a bit unexpected for me since I assumed the task was too large for anyone to tackle.`
`[03-08-2023 17:33:15] <CasCremers[m]> It took us over a year`
`[03-08-2023 17:33:29] <Rucknium[m]> UkoeHB and others are working on Seraphis, which is a planned next-generation transaction structure for Monero: https://github.com/UkoeHB/Seraphis  I think we expect that the Monero Project will need help with creating formal security proofs for some of Seraphis. `
`[03-08-2023 17:33:36] <UkoeHB> wow no kidding`
`[03-08-2023 17:33:44] <CasCremers[m]> (wall clock time)`
`[03-08-2023 17:34:37] <CasCremers[m]> This sounds very interesting, but also a very substantial task.`
`[03-08-2023 17:34:39] <ArticMine[m]> Also extensive audit work will be required `
`[03-08-2023 17:35:35] <UkoeHB> I think this holistic analysis paper will be a very strong starting point for a security analysis of seraphis`
`[03-08-2023 17:36:31] <ghostway[m]> Btw CC: better to not use fancy matrix features like threads. The irc people (koe between them) don't see it as you do... `
`[03-08-2023 17:36:54] <ghostway[m]> Might (and probably did) create confusion on the ordering `
`[03-08-2023 17:37:24] <CasCremers[m]> So much for that DAG ;-)`
`[03-08-2023 17:38:02] <CasCremers[m]> Q: What is the intended timeline for Seraphis?`
`[03-08-2023 17:38:11] <UkoeHB> is the matrix protocol supposed to be a DAG?`
`[03-08-2023 17:39:13] <UkoeHB> CasCremers[m]: we'd like to get security proofs done this year. The implementation is already basically done, as is the addressing scheme https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024 . There is also a parallel protocol Lelantus Spark that already has security proofs https://eprint.iacr.org/2021/1173`
`[03-08-2023 17:39:47] <xmrack[m]> Hi sorry I’m late`
`[03-08-2023 17:40:23] <UkoeHB> the project is kind of bottlenecked on me, since I have been doing the implementation + migration + theoretical work`
`[03-08-2023 17:40:35] <ghostway[m]> UkoeHB: Probably not, threads are rather new`
`[03-08-2023 17:42:03] <CasCremers[m]> If I am understanding this correctly, maybe UkoeHB & Rucknium and us should have a separate mail discussion about the options. We're definitely interested in further refining our proof techniques on modern applications.`
`[03-08-2023 17:42:40] <Rucknium[m]> Fantastic :)`
`[03-08-2023 17:42:45] <UkoeHB> CasCremers[m]: sounds good to me`
`[03-08-2023 17:43:05] <Alex|LocalMonero> CC: thanks for your work!`
`[03-08-2023 17:43:40] <UkoeHB> yes thank you very much :)`
`[03-08-2023 17:43:44] <ghostway[m]> ^, let's see if I can even try to read that thing, lol`
`[03-08-2023 17:43:50] <CasCremers[m]> It's very often just a combination of our theory knowledge and finding the project context for person power`
`[03-08-2023 17:44:01] <ArticMine[m]> Thank you `
`[03-08-2023 17:44:34] <xmrack[m]> Thanks +1`
`[03-08-2023 17:44:36] <Rucknium[m]> CC: Would you prefer discussion in a separate Matrix room, discussion in this room after the meeting, email, or something else?`
`[03-08-2023 17:44:39] <hbs[m]> Thanks`
`[03-08-2023 17:45:00] <Rucknium[m]> Thanks +1`
`[03-08-2023 17:45:01] <CasCremers[m]> thanks for the kind words! feel free to reach out with more questions`
`[03-08-2023 17:45:31] <CasCremers[m]> We have to leave in 15 mins max; maybe continue over email in first instance? `
`[03-08-2023 17:45:44] <dangerousfreedom> Thank you for your work!`
`[03-08-2023 17:46:21] <Rucknium[m]> CC: Email sounds fine. Thank you.`
`[03-08-2023 17:47:31] <UkoeHB> 3. for the remainder of the meeting, does anyone have a topic they want to discuss? There may not be enough time for the other agenda items.`
`[03-08-2023 17:48:05] <Alex|LocalMonero> MRL #100?`
`[03-08-2023 17:48:16] <ghostway[m]> Is this #100?`
`[03-08-2023 17:48:54] <Rucknium[m]> https://github.com/monero-project/research-lab/issues/100 "Exploring Trustless zk-SNARKs for Monero's payment protocol"`
`[03-08-2023 17:49:23] <ghostway[m]> Oh ok`
`[03-08-2023 17:49:32] <UkoeHB> tevador: kayabanerve[m] can you guys summarize where #100 is heading?`
`[03-08-2023 17:50:52] <tevador> I'm currently looking for curve cycles that are compatible with ed25519 and would work with Curve Trees.`
`[03-08-2023 17:51:44] <tevador> I think the next step would be prototyping curve trees in sage with the seraphis key format.`
`[03-08-2023 17:51:51] <UkoeHB> tevador: is that different from the indirect cycle? https://github.com/monero-project/research-lab/issues/100#issuecomment-1443923679`
`[03-08-2023 17:52:37] <tevador> I'm looking for a better cycle that has 255-bit fields instead of 266 bits for obvious reasons (performance)`
`[03-08-2023 17:53:21] <UkoeHB> tevador: the membership proof piece only needs to work on public keys and generator G, it should be independent of seraphis key format`
`[03-08-2023 17:54:30] <UkoeHB> https://github.com/monero-project/research-lab/issues/100#issuecomment-1115448487`
`[03-08-2023 17:54:40] <tevador> Yes, by seraphis key format I meant Ed25519 keys expressed as K + rG for some scalar r and K is in the accumulator.`
`[03-08-2023 17:54:53] <UkoeHB> gotcha`
`[03-08-2023 17:55:15] <ArticMine[m]> Will this approach require a transaction format change after Seraphis?`
`[03-08-2023 17:55:22] <tevador> This is actually slightly different from curve trees as described in the paper because the "bottom layer" is on a different curve.`
`[03-08-2023 17:56:08] <UkoeHB> ArticMine[m]: it would require switching out the membership proof, and a bunch of implementation work to handle merkle trees`
`[03-08-2023 17:57:51] <UkoeHB> one thing that gets me excited is multisig should require zero changes`
`[03-08-2023 17:58:55] <ArticMine[m]> Any idea on tx size for 2 in 2 out?`
`[03-08-2023 17:59:20] <UkoeHB> idk, tevador ?`
`[03-08-2023 17:59:57] <tevador> The Curve Trees demo was around 4 KB for 2/2, with 1 merged proof for both inputs.`
`[03-08-2023 18:01:14] <ArticMine[m]> Definitely doable from a scaling perspective, given the likely timeframe and Neilsen's vLaw`
`[03-08-2023 18:01:25] <tevador> Note that this also has the range proof in the circuit, which will be separate for us.`
`[03-08-2023 18:03:13] <UkoeHB> we are at the end of the hour so I'll call it, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-03-06T18:39:12+00:00
- Closed at: 2023-03-14T01:00:53+00:00
