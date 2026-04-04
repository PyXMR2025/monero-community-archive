---
title: Monero Research Lab Meeting - Wed 14 December 2022
source_url: https://github.com/monero-project/meta/issues/768
author: Rucknium
assignees: []
labels: []
created_at: '2022-12-12T18:54:10+00:00'
updated_at: '2022-12-20T16:42:03+00:00'
type: issue
status: closed
closed_at: '2022-12-20T16:42:03+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#763 

# Discussion History
## UkoeHB | 2022-12-14T18:04:01+00:00
`[12-14-2022 17:00:11] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/768`
`[12-14-2022 17:00:11] <UkoeHB> 1. greetings`
`[12-14-2022 17:00:11] <UkoeHB> hello`
`[12-14-2022 17:00:23] <vtnerd> hello`
`[12-14-2022 17:00:27] <rbrunner> hello`
`[12-14-2022 17:01:05] <one-horse-wagon[> Hello.`
`[12-14-2022 17:01:19] <Rucknium[m]> Hi`
`[12-14-2022 17:01:23] <ghostway[m]> Hello`
`[12-14-2022 17:01:26] <monerobull[m]1> Hi`
`[12-14-2022 17:01:37] <plowsof11> hi`
`[12-14-2022 17:02:36] <jberman[m]> Hello`
`[12-14-2022 17:02:56] <UkoeHB> 2. updates, what's everyone working on?`
`[12-14-2022 17:03:55] <vtnerd> just started looking at bp++`
`[12-14-2022 17:04:24] <vtnerd> started with the readme and docs this time instead of haskell code. slightly more confident that Ill be able to do something, more details next week hopefully`
`[12-14-2022 17:04:35] <vtnerd> Im still piecing together my internally busted network`
`[12-14-2022 17:05:09] <vtnerd> the haskell is just rough because its math-heavy-crypto code. so its like a terrible crash-course in haskell lol`
`[12-14-2022 17:05:57] <rbrunner> I made my "long addresses" Reddit post: https://old.reddit.com/r/Monero/comments/zl4615/why_seraphis_jamtis_addresses_will_be_so_awfully/`
`[12-14-2022 17:06:05] <Rucknium[m]> I have been looking at fee prediction. It won't be a research topic for several months, but we should be collecting mempool data now. I read Huberman, G., Leshno, J. D., & Moallemi, C. (2021). "Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System." To my surprise, the model assumes that users don't know the mempool contents. The paper's purpose is to discover the long-run fee equilibrium behavior, so`
`[12-14-2022 17:06:06] <Rucknium[m]> it makes sense I guess.`
`[12-14-2022 17:06:18] <Rucknium[m]> I wrote some code to collect mempool txs`
`[12-14-2022 17:06:29] <plowsof11> no resp yet from follow up email to bp++ author. i've kept CypherStack up to date on the delay and they are understanding / will be patient.`
`[12-14-2022 17:06:36] <UkoeHB> me: finished reviewing my multisig changes (vtnerd those will keep you busy all next year :) ), and wrote this overview of the current Seraphis design https://gist.github.com/UkoeHB/f508a6ad973fbf85195403057e87449e (let me know if I am missing anything - I will add a table for tx parameters as requested by Rucknium[m])`
`[12-14-2022 17:06:53] <jberman[m]> Submitting a PR hopefully today implementing a few changes on top of PR 8076 that will help daemons process RPC requests when the tx pool is under heavy load, following this comment: https://github.com/monero-project/monero/pull/8076#issuecomment-1340590787`
`[12-14-2022 17:06:55] <Rucknium[m]> vtnerd: Did you see the MRL log from last meeting about a new Dandelion++ paper?`
`[12-14-2022 17:07:14] <vtnerd> haha my ccs time is just being code-reviews, but everyone keeps saying Im decent at them so why not`
`[12-14-2022 17:08:14] <rbrunner> jberman[m]: Nice. I may have time on Friday to look at it.`
`[12-14-2022 17:10:37] <UkoeHB> 3. discussion`
`[12-14-2022 17:11:49] <rbrunner> Some info about the reactions on Reddit to my post:`
`[12-14-2022 17:11:55] <rbrunner> Pretty favorable, I would say`
`[12-14-2022 17:12:00] <rbrunner> Somebody made another post about possible disruption: https://old.reddit.com/r/Monero/comments/zlr2m4/the_downside_of_jamtis_addresses/`
`[12-14-2022 17:12:15] <rbrunner> That came out a bit more controversial, but not unexpectedly so`
`[12-14-2022 17:12:43] <rbrunner> And I learned that Lightning Network invoices are at least 190 characters long :)`
`[12-14-2022 17:13:19] <rbrunner> In Base32, by the way`
`[12-14-2022 17:16:15] <UkoeHB> might be good to make a reddit post about that seraphis design overview (I'm not on reddit)`
`[12-14-2022 17:16:40] <rbrunner> I can do that, if that's ok with you`
`[12-14-2022 17:16:42] <UkoeHB> everyone might not realize the design has stabilized`
`[12-14-2022 17:16:54] <UkoeHB> and I am not even writing new code for over a week`
`[12-14-2022 17:17:20] <UkoeHB> last new thing was 10 days ago`
`[12-14-2022 17:17:58] <isthmus> That's exciting :)`
`[12-14-2022 17:17:59] <UkoeHB> rbrunner: sure`
`[12-14-2022 17:18:32] <UkoeHB> isthmus: yeah :) now for the long agonizing review process`
`[12-14-2022 17:19:04] <blankpage[m]> Is it fair to say that the seraphis paper is outdated?`
`[12-14-2022 17:19:11] <isthmus> Hey Rucknium, RE "Remote node sends all txs to a wallet, the wallet scans. The wallet takes slightly more time to fully scan an output that belongs to it. Could the remote node infer anything?" `
`[12-14-2022 17:19:12] <isthmus> ^^ you might find this an interesting read https://crypto.stanford.edu/timings/`
`[12-14-2022 17:19:24] <UkoeHB> blankpage[m]: not really, the core design is the same - most of the changes have been with jamtis`
`[12-14-2022 17:19:46] <blankpage[m]> Or has the paper been updated along with the finalization of the design?`
`[12-14-2022 17:21:18] <UkoeHB> blankpage[m]: the paper doesn't have jamtis in it`
`[12-14-2022 17:21:23] <Rucknium[m]> I am going to be a broken record: is there a roadmap for writing Seraphis security proofs? We could ask for outside help like CypherStack if necessary.`
`[12-14-2022 17:21:34] <blankpage[m]> Good to know, that you`
`[12-14-2022 17:21:36] <UkoeHB> I'm considering updating the paper with a case study of jamtis, not sure if that's a good idea or not`
`[12-14-2022 17:22:02] <UkoeHB> Rucknium[m]: no roadmap`
`[12-14-2022 17:22:14] <Rucknium[m]> Or Geometry Labs ;)`
`[12-14-2022 17:23:06] <Rucknium[m]> That means we still don't know for sure if Seraphis is secure.`
`[12-14-2022 17:23:33] <rbrunner> I think that's sure ...`
`[12-14-2022 17:23:38] <UkoeHB> the existence of a security proof doesn't guarantee that, if the proof itself is flawed`
`[12-14-2022 17:24:35] <isthmus> 🤔 ooh writing or analyzing those security proofs would be a fun project`
`[12-14-2022 17:24:39] <Rucknium[m]> Yes. Getting a "candidate" proof is the first step.`
`[12-14-2022 17:24:40] <UkoeHB> the only parts that seem security-proofable to me are the seraphis composition proof and the squashed enote model`
`[12-14-2022 17:25:16] <UkoeHB> security proofing jamtis would be an enormous task`
`[12-14-2022 17:26:39] <rbrunner> Is there an "ELI5" somewhere what, in principle, a "security proof" is? I confess to have no idea at all.`
`[12-14-2022 17:26:39] <UkoeHB> I also wrong a dual-base vector proof for multisig stuff, not sure if we want/need a security proof for that`
`[12-14-2022 17:27:06] <moneromoooo> If you wrong it, we sure do need a proof :D`
`[12-14-2022 17:27:25] <Rucknium[m]> Don't we still need to security proof Jamtis?`
`[12-14-2022 17:27:30] <Rucknium[m]> Even if it's a big task?`
`[12-14-2022 17:27:31] <UkoeHB> moneromoooo: lol`
`[12-14-2022 17:27:56] <UkoeHB> Rucknium[m]: CryptoNote and subaddresses were not security proofed`
`[12-14-2022 17:28:24] <UkoeHB> not to say if someone has a vision about how to security proof jamtis, that would be amazing`
`[12-14-2022 17:28:39] <UkoeHB> just not clear if it's mandatory`
`[12-14-2022 17:29:21] <rbrunner> I guess for starting something like that we would need a pretty strict "feature freeze" first?`
`[12-14-2022 17:29:30] <UkoeHB> probably`
`[12-14-2022 17:29:34] <Rucknium[m]> Is the lack of security proof for Cryptonote related to the counterfeiting bug several years ago?`
`[12-14-2022 17:30:02] <UkoeHB> possibly?`
`[12-14-2022 17:30:53] <dangerousfreedom> Hello. I guess I figured out how to make unspentproofs for seraphis. I will write about it by the weekend.`
`[12-14-2022 17:31:58] <UkoeHB> I guess I should make clear I won't be spending too much effort working on or looking for security proofs. My involvement is winding down as I have accomplished everything I set out to do.`
`[12-14-2022 17:32:22] <Rucknium[m]> Anyone want to answer rbrunner 's ELI question about security proofs? I know "regular" math proofs, but I'm not a cryptographer.`
`[12-14-2022 17:32:40] <isthmus> @rbrunner - security proofs involve formally defining an adversary and what it means for them to break a given aspect of a given system. And then the goal is to prove things like “an adversary being able to convert a public key into a private key would imply that they can break the discrete log problem” and stuff like that. `
`[12-14-2022 17:32:40] <isthmus> So you can sleep a little better if there is a security proof thought to be correct. To push back on a security proof involves identifying an adversary that should have been included in the model, or a issue with the reduction to a “hard” problem like discrete log.`
`[12-14-2022 17:32:40] <isthmus> (take the ELI5 with a grain of salt, I manage GL’s cryptography wing but I am not a cryptographer myself)`
`[12-14-2022 17:33:17] <Rucknium[m]> UkoeHB: Good to know. So we should think about how to get those proofs using alternative means/personnel.`
`[12-14-2022 17:34:19] <rbrunner> Seems to me it's pretty open how to approach this then? Seems to depend on how you assume your adversary to be.`
`[12-14-2022 17:34:44] <rbrunner> Two cryptographers tasked with "Security proofs for Jamtis" might come up with pretty different things?`
`[12-14-2022 17:35:36] <Rucknium[m]> You can have multiple proofs of the same theorem. Basically, different paths to the same destination`
`[12-14-2022 17:37:01] <Rucknium[m]> Writing nontrivial math proofs is generally hard. I don't know how hard it is in cryptography, but also probably hard.`
`[12-14-2022 17:37:35] <Rucknium[m]> It's not just "put in enough effort and you will accomplish the task"`
`[12-14-2022 17:38:24] <rbrunner> I see. It may even be that nobody at all stumbles over the right approach in the cases of Seraphis and Jamtis.`
`[12-14-2022 17:39:06] <plowsof11> increase the hackerone pot would help in the future`
`[12-14-2022 17:39:13] <dangerousfreedom> We have the advantage that many people are looking here too which puts some pressure on the guy doing it as he has to have an authority bigger than the Monero community to say it is not flawed. Who did it when the RCT came?`
`[12-14-2022 17:39:48] <dangerousfreedom> (If it was done)`
`[12-14-2022 17:39:50] <Rucknium[m]> rbrunner: That is why I have brought it up repeatedly: We need someone to find this thing, and we are not sure yet whether this thing exists. If there is a counterexample, then Seraphis will need to be re-worked.`
`[12-14-2022 17:40:34] <Rucknium[m]> By "counterexample" I mean some fact that disproves the conjecture that Seraphis is secure`
`[12-14-2022 17:40:55] <rbrunner> Not sure we understand each other. I was thinking about the case where people try to "construct" such proofs, but nobody is able to.`
`[12-14-2022 17:41:16] <rbrunner> Like famous theorems in math that went unproved for literally centuries.`
`[12-14-2022 17:42:10] <Rucknium[m]> Yes, so we can run into trouble if either (1) no one can come up with a proof or (2) someone proves that Seraphis is insecure. You can find insecurity during the task of trying to prove security.`
`[12-14-2022 17:42:48] <Rucknium[m]> Sarang would obviously be a good person to attempt this since he worked on a similar cryptosystem.`
`[12-14-2022 17:43:03] <rbrunner> Well, I guess there still is review: Somebody traces step by step the constructs and sees whether everything makes sense.`
`[12-14-2022 17:44:17] <Rucknium[m]> I would find it hard to recommend Seraphis implementation on mainnet if we don't have the necessary security proofs.`
`[12-14-2022 17:45:06] <rbrunner> I think we don't have security proofs for the current constructs either :)`
`[12-14-2022 17:46:15] <rbrunner> Maybe we could buy something like 2 or 3 workdays from Sarang to look at it and then tell us whether they would like to try?`
`[12-14-2022 17:46:17] <Rucknium[m]> We have them for some of the constructs. I don't know the complete list of which we have and which we do not.`
`[12-14-2022 17:47:02] <Rucknium[m]> rbrunner: I would support that`
`[12-14-2022 17:50:32] <UkoeHB> we are approaching the end of the meeting - were there any other topics to bring up?`
`[12-14-2022 17:51:08] <one-horse-wagon[> Will someone be following up with Sarang?`
`[12-14-2022 17:52:36] <Rucknium[m]> Is there loose consensus for it? This would be a good project for MAGIC Monero Fund since the decision and funding could be done quickly.`
`[12-14-2022 17:53:01] <one-horse-wagon[> You have my vote.`
`[12-14-2022 17:53:07] <Rucknium[m]> We would need a more formal description of the outcome of the work`
`[12-14-2022 17:55:21] <plowsof11> does magic have a track record of quick funding? `
`[12-14-2022 17:56:22] <Rucknium[m]> We can spend out of our general fund, which has about 50,000 USD IIRC`
`[12-14-2022 17:56:46] <Rucknium[m]> Split between USD and XMR pretty equally`
`[12-14-2022 17:57:26] <plowsof11> fund this one first https://monerofund.org/projects/statistical_attack_reduction`
`[12-14-2022 17:58:02] <Rucknium[m]> That one was approved based on requiring community funding`
`[12-14-2022 17:58:29] <one-horse-wagon[> Like rbrunner said, at least let's get Sarang to look at the problem for a few days as a first step.`
`[12-14-2022 17:59:13] <Rucknium[m]> Diego Salazar: Thoughts on the discussion above?`
`[12-14-2022 18:01:24] <Rucknium[m]> We need CypherStack to give an initial "yes" to some type of work. Then MAGIC Monero Fund committee can approve fund disbursement at its next meeting on Tuesday. MAGIC Board needs to give final approval. That's mostly just conflict-of-interest, in Monero Project scope, and KYC.`
`[12-14-2022 18:02:29] <DiegoSalazar[m]> Always down.`
`[12-14-2022 18:03:12] <UkoeHB> ok we are past the hour so I'll call it here, thanks for attending everyone; discussion about planning can continue as needed`

# Action History
- Created by: Rucknium | 2022-12-12T18:54:10+00:00
- Closed at: 2022-12-20T16:42:03+00:00
