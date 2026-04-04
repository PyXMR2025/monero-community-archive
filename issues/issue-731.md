---
title: Monero Research Lab Meeting - Wed 05 September 2022
source_url: https://github.com/monero-project/meta/issues/731
author: Rucknium
assignees: []
labels: []
created_at: '2022-09-05T15:45:07+00:00'
updated_at: '2022-09-13T12:18:42+00:00'
type: issue
status: closed
closed_at: '2022-09-13T12:18:42+00:00'
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

#728 

# Discussion History
## UkoeHB | 2022-09-08T18:48:29+00:00
`[09-08-2022 17:00:12] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/731`
`[09-08-2022 17:00:20] <UkoeHB> 1. greetings`
`[09-08-2022 17:00:21] <UkoeHB> hello`
`[09-08-2022 17:00:35] <xmrack[m]> Hey`
`[09-08-2022 17:00:40] <rbrunner> Hi`
`[09-08-2022 17:00:40] <Rucknium[m]> Hi`
`[09-08-2022 17:00:40] <tevador> Hi`
`[09-08-2022 17:00:45] <jberman[m]> hello`
`[09-08-2022 17:00:54] <dangerousfreedom> Hello`
`[09-08-2022 17:01:49] <one-horse-wagon[> Hello.`
`[09-08-2022 17:02:51] <UkoeHB> 2. updates, what has everyone been working on?`
`[09-08-2022 17:03:16] <ArticMine[m]> Hi`
`[09-08-2022 17:04:18] <dangerousfreedom> I'm still scanning the blockchain using some rust tools and learning more about seraphis. I will be collecting a todo list this month so I can start contributing from October on...`
`[09-08-2022 17:04:41] <UkoeHB> me: finished up my vacation, worked on some jamtis updates for better forward secrecy vs an efficient DLP solver; this coming week I plan to finally start updating the seraphis tx protocol so it can spend legacy enotes`
`[09-08-2022 17:04:55] <Rucknium[m]> OSPEAD. I think I will finish it next week. I know this is becoming a Zeno's Paradox :P`
`[09-08-2022 17:04:55] <Rucknium[m]> It's about 70 pages right now with all tables, charts, and references included.`
`[09-08-2022 17:05:54] <Rucknium[m]> I'm wondering if tevador wants to be on the OSPEAD review panel. I want to give the panel 1-1.5 months to review it. I will be able to release some of it publicly immediately though.`
`[09-08-2022 17:06:24] <jberman[m]> Worked on release prep (collab'd with koe to fix multisig seed restore, restoring from encrypted seed + finalizing/reviewing other PR's). Also drafted an email to engage in discussion with Cypher Stack to work on various tasks and discussed with UkoeHB . Will share more about that later in discussion`
`[09-08-2022 17:06:51] <tevador> I did some preliminary post-quantum research of Seraphis, which resulted in a few changes to the addressing scheme that improve forward secrecy. A draft of other post-quantum mitigations can be found here: https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a`
`[09-08-2022 17:07:17] <xmrack[m]> I’ve been answering questions on reddit related to my MAGIC report. SGP and I will be posting a Q&A at some point soon answering some common questions. `
`[09-08-2022 17:08:05] <Rucknium[m]> jberman: Does one of those potential tasks include writing math proofs for Seraphis? I have been thinking that CypherStack could be good for that. And dangerousfreedom could follow up with them.`
`[09-08-2022 17:09:49] <jberman[m]> Yep, agree on that`
`[09-08-2022 17:10:31] <UkoeHB> 3. discussion`
`[09-08-2022 17:11:00] <Rucknium[m]> Maybe some of these funds could be re-purposed? https://ccs.getmonero.org/proposals/cypherstack-sarang-triptych-research.html`
`[09-08-2022 17:11:49] <Rucknium[m]> xmrack: What do you think is actionable about your research?`
`[09-08-2022 17:12:34] <dangerousfreedom> Rucknium[m]: I would be happy to check and I could quickly build some accurate (but slow) Python tools for prototyping and documenting`
`[09-08-2022 17:14:33] <jberman[m]> The 4 tasks I initially included in the draft: (1) security proofs for multisig, (2) reviewing Seraphis and Jamtis, (3) exploring trustless zk-SNARKs in Monero, and (4) vetting bulletproofs++`
`[09-08-2022 17:14:46] <jberman[m]> I initially felt that multisig should be first priority in discussions because it can impact user funds today`
`[09-08-2022 17:15:34] <jberman[m]> UkoeHB responded with a better fleshed out email (makes it clearer exactly what would be useful in pushing Seraphis and Jamtis forwards -- including security proofs for Seraphis), that also shifts prioritizing multisig downwards for the following reason:`
`[09-08-2022 17:15:41] <Rucknium[m]> jberman: Agree on multisig as 1st priority. That is quite the hefty research agenda :)`
`[09-08-2022 17:15:50] <jberman[m]> > I am concerned that a lot of work spent on current Monero multisig would just go to waste once Seraphis goes live. I'd personally be ok with leaving it experimental until wallet2 is deprecated. Note that the above list constitutes a TON of work that needs to be done before Seraphis goes live. Seraphis multisig on its own is a doozy if we want to go all the way.`
`[09-08-2022 17:16:17] <jberman[m]> I am leaning towards this conclusion as well. To support this conclusion further, yesterday I found that encrypted multisig seeds have been un-recoverable for the past ~4 years because of a bug that has gone unreported until issue 8537. To me this suggests multisig has seen very little use, and as such, I think it's reasonable to prioritize looking forwards to land on the future safe form of multisig`
`[09-08-2022 17:17:02] <Rucknium[m]> Well, should the interested parties in the ecosystem take the lead on multisig strengthening then?`
`[09-08-2022 17:17:20] <rbrunner> Hmmm, strange, I think I recovered such a wallet from a seed that RINO provided in their "recovery document"`
`[09-08-2022 17:17:42] <tevador> I agree that Seraphis should be the priority.`
`[09-08-2022 17:17:56] <rbrunner> Does it fail only in certain cases?`
`[09-08-2022 17:17:57] <jberman[m]> rbrunner: encrypted with a seed passphrase?`
`[09-08-2022 17:18:06] <rbrunner> That, no.`
`[09-08-2022 17:18:11] <xmrack[m]> Rucknium: My research found that training various ML/DL models on past transaction information can lead to a slight performance increase over random guessing. Notably one of the highest feature importances was surrounding the tx_extra field. This is likely due to the non-uniform constraints placed on it, as we’ve discussed in the past. `
`[09-08-2022 17:18:11] <xmrack[m]> Temporal and positional relationships of transactions and blocks had a much lower feature importance to the models. Overall, there was less information leakage strictly on-chain than I initially anticipated, which is good news!`
`[09-08-2022 17:19:26] <rbrunner> Ah, I just overlooked the word "encrypted" ...`
`[09-08-2022 17:19:32] <jberman[m]> rbrunner: that's the type that's been unrecoverable. An edge case, but still lends strength I think to the view that it's sensible to prioritize looking forwards`
`[09-08-2022 17:20:20] <rbrunner> Well, I suspect as well that multisig sees very little use, from the non-use of my MMS. Of course not everybody will like that, but with many multisig users some should`
`[09-08-2022 17:21:08] <rbrunner> Nobody told me yet that is does not work with the latest version of PyBitmessage ...`
`[09-08-2022 17:21:47] <rbrunner> "Seraphis multisig on its own is a doozy if we want to go all the way." I don't understand the English word "doozy" in this context. Easy? Simple? Good?`
`[09-08-2022 17:22:13] <Rucknium[m]> xmrack: I have considered a multivariate decoy selection algorithm. Right now, it's purely univariate on output age. I think your research suggests that multivariate might not be necessary since the other variables seem to not leak much exploitable information. Of course, this was an artificial dataset.`
`[09-08-2022 17:22:28] <UkoeHB> I'm not sure if any pre-existing multisig wallets actually work: https://github.com/monero-project/monero/pull/8329#issuecomment-1216946632`
`[09-08-2022 17:22:35] <UkoeHB> I only heard of one complaint`
`[09-08-2022 17:23:20] <UkoeHB> https://libera.monerologs.net/monero/20220816#c136742`
`[09-08-2022 17:23:33] <jberman[m]> rbrunner: it's missing UkoeHB 's context which details a fairly large amount of work involved of formalizing security proofs and vetting multisig as implemented in Seraphis`
`[09-08-2022 17:24:06] <rbrunner> So it's the opposite - it will be hard until production-ready?`
`[09-08-2022 17:24:21] <rbrunner> So better safe our powder for that big work?`
`[09-08-2022 17:24:57] <xmrack[m]> Rucknium: I agree, what were the other variables you were considering?`
`[09-08-2022 17:25:44] <Rucknium[m]> xmrack: Really anything that is not uniform across transactions.`
`[09-08-2022 17:26:04] <UkoeHB> rbrunner: seraphis multisig includes both legacy and seraphis multisig signing`
`[09-08-2022 17:26:11] <UkoeHB> in addition to account migrations`
`[09-08-2022 17:26:27] <ArticMine[m]> Still from a workload and overall efficiency perspective focusing on Seraphis for multi sig is the way to proceed `
`[09-08-2022 17:27:07] <UkoeHB> I suggested starting with BP++ paper review + proof-of-concept, since at least that can be implemented in ringct if seraphis is taking too long`
`[09-08-2022 17:27:52] <rbrunner> Did we hear anything more from ooo about their BP++ implementation, or is it still only those timing results?`
`[09-08-2022 17:28:04] <UkoeHB> selsta: `
`[09-08-2022 17:28:53] <selsta> not yet`
`[09-08-2022 17:29:15] <rbrunner> Ok, that's a known unknown then :)`
`[09-08-2022 17:29:15] <ArticMine[m]> What are the gains with BP++ vs BP+?`
`[09-08-2022 17:29:28] <UkoeHB> ArticMine[m]: https://github.com/monero-project/research-lab/issues/101`
`[09-08-2022 17:29:35] <xmrack[m]> Rucknium: is there a number of de-anonymized mainnet transactions that could be sourced in a federated manner to represent the population? Would this allow you to represent the population and include multiple variables to the new DSA? `
`[09-08-2022 17:30:32] <UkoeHB> the batched verification in that test is -10%, with tx construction -72%, tx size -256 bytes`
`[09-08-2022 17:31:50] <Rucknium[m]> There is the very old Moser et al. (2018) de-anoned data. If we are brainstorming, we could do some sort of cutting-edge differential privacy-compliant technique where people run some sort of estimator or algorithm on their own txs and then send us the results only, protecting privacy somehow.`
`[09-08-2022 17:32:34] <xmrack[m]> Yea I was thinking something along the lines of the latter`
`[09-08-2022 17:32:44] <tevador> is the BP++ test source code available for review?`
`[09-08-2022 17:33:00] <UkoeHB> tevador: no, and I'm skeptical it ever will be`
`[09-08-2022 17:33:29] <UkoeHB> I'm just taking the results at face value as reinforcing the author's perf predictions.`
`[09-08-2022 17:35:17] <ArticMine[m]> UkoeHB:  Thanks `
`[09-08-2022 17:35:20] <rbrunner> Regarding multisig: The idea of throwing every available hour from now on into the direction of Seraphis sounds good to me.`
`[09-08-2022 17:35:42] <rbrunner> Of course there are certain residual risks, lacking proofs and all, but should not be too risky`
`[09-08-2022 17:36:14] <rbrunner> (with current multisig)`
`[09-08-2022 17:36:55] <UkoeHB> multisig still needs PRs 8329 and 8203 at least... then I can use my seraphis lib to do an escrowed exchange demo (my last planned project for monero post-seraphis)`
`[09-08-2022 17:39:25] <rbrunner> How would be pay Cypher Stack? Through CCS?`
`[09-08-2022 17:40:10] <Rucknium[m]> By the way, I include some ring size 128 analysis in OSPEAD. So maybe OSPEAD will be Seraphis-ready :)`
`[09-08-2022 17:40:31] <UkoeHB> with BP++ I think we might be able to justify ring size 256`
`[09-08-2022 17:41:00] <UkoeHB> if it pans out`
`[09-08-2022 17:41:44] <ArticMine[m]> Ring 256 would be great `
`[09-08-2022 17:42:04] <Rucknium[m]> Great to hear. I'll keep my analysis at 128 for now so that I don't sink even more time into it.`
`[09-08-2022 17:42:12] <jberman[m]> Pinging vtnerd to see if he'd be available to review 8329 and 8203 to completion. I'll look into them in a few days if not`
`[09-08-2022 17:42:34] <UkoeHB> 8203 needs to rebase onto 8329`
`[09-08-2022 17:44:16] <jberman[m]> W.r.t. to Cypher Stack, planning to go with koe's suggestions and engage with them with the following priorities in order: bp++, Seraphis core proof modeling, Jamtis design review, Seraphis multisig`
`[09-08-2022 17:45:31] <jberman[m]> On trustless zk-SNARKs, I'm waiting to hear from kayabanerve to get a better idea how best to proceed there. I would personally like to see research into zk-SNARKs pushed forward with high priority, so will probably bring it up in discussions with Cypher Stack anyway too`
`[09-08-2022 17:46:17] <selsta> I thought multisig securtiy proofs would be applicable to seraphis (with some changes) ?`
`[09-08-2022 17:46:31] <selsta> I'm confused what the plan is now with multisig`
`[09-08-2022 17:48:15] <UkoeHB> I'm personally fine with leaving the current stuff experimental until wallet2 and ringct are deprecated.`
`[09-08-2022 17:51:39] <UkoeHB> putting more resources toward current multisig may end up delaying seraphis`
`[09-08-2022 17:52:06] <selsta> I don't see how that would be the case if we fund someone external for it`
`[09-08-2022 17:52:32] <selsta> I just know that we have multiple people in the ecosystem who plan to use multisig soon and not in a couple years`
`[09-08-2022 17:53:16] <vtnerd> I will`
`[09-08-2022 17:53:35] <UkoeHB> external people are also in limited supply`
`[09-08-2022 17:56:02] <ArticMine[m]> I see trustless zk-SNARKS as a possibility after Seraphis; however we must keep in mind that we are dealing with finite anonymity sets in any case, when comparing to 256 Seraphis plus OPSREAD`
`[09-08-2022 17:56:38] <ArticMine[m]> The gain may reach dining returns `
`[09-08-2022 17:56:59] <UkoeHB> ArticMine[m]: the goal would be using a full anonymity set for seraphis membership proofs (a straight upgrade instead of tx protocol replacement)`
`[09-08-2022 17:57:05] <ArticMine[m]> Diminishing `
`[09-08-2022 17:57:25] <rbrunner> I think people who want to use Monero multisig now should replace "experimental" with something like "lacks formal proof / verification" and then see whether that is ok with their risk tolerance`
`[09-08-2022 17:57:41] <selsta> rbrunner: well just a matter until someone exploits it`
`[09-08-2022 17:57:43] <rbrunner> After all, the code *was* reviewed.`
`[09-08-2022 17:59:10] <rbrunner> It's a thorny issue, because it's basically opinion versus opinion, but I for one give some trust to our own reviews by quite competent people. That was not nothing, so to say.`
`[09-08-2022 17:59:12] <ArticMine[m]> UkoeHB: Then it definitely becomes something to look at after the initial Seraphis `
`[09-08-2022 18:00:15] <rbrunner> It can only be a matter of time until someone exploits if there is an exploit to be found - which I don't see as certain.`
`[09-08-2022 18:01:13] <UkoeHB> ok we are at the end of the hour so I'll call it; thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-09-05T15:45:07+00:00
- Closed at: 2022-09-13T12:18:42+00:00
