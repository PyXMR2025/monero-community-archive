---
title: Monero Research Lab Meeting - Wed 18 October 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/910
author: Rucknium
assignees: []
labels: []
created_at: '2023-10-18T15:07:27+00:00'
updated_at: '2023-10-25T15:04:06+00:00'
type: issue
status: closed
closed_at: '2023-10-25T15:04:06+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#908 

# Discussion History
## plowsof | 2023-10-23T12:30:46+00:00
Logs 
> __< Rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/910     

> __< Rucknium >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< j​effro256:monero.social >__ Howdy     

> __< Rucknium >__ 2) Updates. What is everyone working on?     

> __< j​effro256:monero.social >__ I put a PR out to modify decoy selection https://github.com/monero-project/monero/pull/9023     

> __< Rucknium >__ me: Reported nonstandard fee privacy issue to Exodus. They fixed it in the Desktop wallet. Mobile fix still being worked on: https://www.reddit.com/r/Monero/comments/176e1zr/privacy_advisory_exodus_desktop_users_update_to/ . Reviewing jeffro256's guide to wallet2's decoy selection algorithm and converting it to math formulas.     

> __< j​effro256:monero.social >__ How did you initially find out that it was Exodus with the nonstandard fees?     

> __< j​effro256:monero.social >__ B/c they're close source, right?     

> __< j​effro256:monero.social >__ Was it wrong enough that you could just see it just by eyeballing it?     

> __< Rucknium >__ I suspected it was exodus since they released their first working Monero version after the August 2022 hard fork at about the same date that the txs with the specific fee values started to appear.     

> __< Rucknium >__ Then I sent some transactions with the wallet.     

> __< Rucknium >__ I think they just had the wrong tx size. The UI showed tx size about 12 Kb for 1in/2out. If you used that incorrect size to calculate fees, then it would have used 20 nanoneros per byte, which is the standard minimum fee.     

> __< j​effro256:monero.social >__ Oh okay nice     

> __< v​tnerd:monero.social >__ Me: mostly subaddressses, but also answering questions for someone doing a 10k account stress test on LWS.     

> __< v​tnerd:monero.social >__ LWS will be enterprise ready in the not distant future it looks like     

> __< j​effro256:monero.social >__ That's awesome to hear !     

> __< j​effro256:monero.social >__ So the stress test went well?     

> __< j​effro256:monero.social >__ also btw @vtnerd did you have questions about https://github.com/monero-project/monero/pull/9023? I saw you commented on it the other day. Also, I have to apologize for sidelining my review of the serialization read interface; it's next on my list     

> __< v​tnerd:monero.social >__ No, it failed lol. But they didn't know if was the frontend or backend yet. But we'll find out over the next month or so, and have it fixed     

> __< v​tnerd:monero.social >__ Worse case it's in some LWS<->monerod interaction     

> __< Rucknium >__ 3) Discussion. What do we want to discuss?     

> __< o​frnxmr:monero.social >__ ```     

> __< o​frnxmr:monero.social >__ any follow up questions/issues for CypherStack regarding the new scope for the bp++ peer review? : https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/413/diffs     

> __< o​frnxmr:monero.social >__ ```     

> __< o​frnxmr:monero.social >__ from plowsof     

> __< rbrunner >__ Do I get it that this is waiting for word from Core?     

> __< o​frnxmr:monero.social >__ From mrl     

> __< rbrunner >__ Ah, you mean about the modified scope     

> __< o​frnxmr:monero.social >__ Yes sir     

> __< rbrunner >__ Not about the financing     

> __< o​frnxmr:monero.social >__ Right     

> __< rbrunner >__ In this case I am on the same side as you: No clue, not being a cryptographer ...     

> __< Rucknium >__ As a non-cryptographer, the scope changes sound fine to me, except I don't know how important "Optimized binary range proofs" is. Is that a major part of what BP++ uses to get space and verification time savings?     

> __< plowsof >__ ive also shared feedback from zksecurity with koe/jberman - exploratory work on seraphis papers. $10k/week for 2 months (80k) - "deliverables" hard to define but they are open to discussion / setting up a scope of work      

> __< Rucknium >__ Doing a quick search in the paper: "However, while this motivating example provides an intuition for why a norm relation can be preferable over an inner product relation, it turns out that in practice, it is almost always more efficient to use a BP++ reciprocal range proof instead of a BP++ binary range proof."     

> __< Rucknium >__ So would Monero use a BP++ reciprocal range proof?     

> __< Rucknium >__ "For most ranges, the reciprocal range proof is substantially more efficient for the prover and the verifier than a binary range proof. However for some small ranges with B − A < 28, a binary range proof can be more efficient."     

> __< Rucknium >__ "28" should be 2^8     

> __< Rucknium >__ kayabaNerve, would Monero use a binary range proof or a reciprocal range proof? Is it OK that the security proof of the binary range proof for BP++ won't be reviewed by CypherStack?     

> __< Rucknium >__ I plotted the number of transactions that fit the Exodus Desktop fee pattern for the last 8 weeks: https://github.com/Rucknium/misc-research/blob/main/Monero-Nonstandard-Fees/images/Exodus-txs-after-fix-release.png     

> __< Rucknium >__ The fixed Exodus Desktop wallet version was released on October 10. A week later, txs with the Exodus fee have been cut by about 50%. From 600 per day to 300 per day.     

> __< rbrunner >__ Probably getting better of time. Funny how the number of transactions vary predictably over the week. Monday is especially busy, it seems :)     

> __< rbrunner >__ *over time     

> __< Rucknium >__ 1. This is pretty conclusive evidence that it was Exodus Desktop wallets creating those transactions. 2. This is the first statistical analysis on the amount of time it takes for users to update their Monero wallets. Obviously, users of other wallets would update at a different pace.     

> __< j​effro256:monero.social >__ Does the exodus desktop app auto-update ?     

> __< Rucknium >__ The lower tx volume for Saturday-Sunday in the Exodus plot is similar to the tx volume for the whole blockchain.     

> __< Rucknium >__ I think the update behavior depends on OS. Different for Windows/Mac/Linux     

> __< Rucknium >__ Exodus releases a new version every two weeks on a schedule.     

> __< Rucknium >__ If wallet2 is updated, there are two steps: 1) Wallet developers who use wallet2 update to the new wallet2 code. 2) Users update their wallets.     

> __< Rucknium >__ Users who use the GUI or CLI wallet would update "directly" to wallet2     

> __< Rucknium >__ Anything else to discuss?     

> __< j​effro256:monero.social >__ That CCS is to review the paper only right?     

> __< j​effro256:monero.social >__ (This is my first time looking at the CCS)     

> __< Rucknium >__ Yes. It is to review the paper's mathematics.     

> __< j​effro256:monero.social >__ vtnerd, you've already done play implementations of bp++ yeah?     

> __< j​effro256:monero.social >__ vtnerd, you've already done PoC implementations of bp++ yeah?     

> __< j​effro256:monero.social >__ I wonder if we should leave out batch verification from the scope ....     

> __< v​tnerd:monero.social >__ no it was unfinished unfortunately, I didn't know how to do the last part. I was hoping the newer paper would clarify some things. Or I could just do a port from the secp code     

> __< Rucknium >__ The CCS proposal is supposed to review what exists in the paper, not create new mathematics. Doing batch verification would require new mathematics I think.     

> __< j​effro256:monero.social >__ > To improve verifier performance, the BP     

> __< j​effro256:monero.social >__ paper suggests a few optimizations, such as using a single multi-exponentiation, batch verification, and an     

> __< j​effro256:monero.social >__ efficient method to compute scalars. The first two optimizations can be directly translated to BP++, but     

> __< j​effro256:monero.social >__ the method to compute scalars has to be slightly adapted from BP’s inner product argument to BP++’s     

> __< j​effro256:monero.social >__ norm linear argument. All three optimizations have been implemented in the benchmarked code.     

> __< j​effro256:monero.social >__ It seems that there is an analagous, already-implemented way to do batch verification in bp++     

> __< j​effro256:monero.social >__ Even if not explicitly mentioned how in the paper     

> __< j​effro256:monero.social >__ Does Cypherstack do code reviews as well or just maths?     

> __< Rucknium >__ They have done code reviews before.     

> __< Rucknium >__ Maybe the question is "does BP++ batch verification have a security proof?"     

> __< Rucknium >__ Does the original BP paper have a security proof for batch verification?     

> __< v​tnerd:monero.social >__ I dont recall any, but I wasn't looking for it either     

> __< j​effro256:monero.social >__ is the newer paper the one that is linked here ? https://eprint.iacr.org/archive/2022/510/20230717:163509     

> __< j​effro256:monero.social >__ Or is that the older one ?     

> __< j​effro256:monero.social >__ There's been one revision on this entry     

> __< Rucknium >__ That's the latest version on the IACR website: https://eprint.iacr.org/archive/versions/2022/510     

> __< Rucknium >__ We will end the meeting here. Discussions on the BP++ review CCS can continue.     

> __< j​effro256:monero.social >__ Looking thru the BP paper, there's no security proof per se, but a rather simple algebraic argument     

> __< j​effro256:monero.social >__ If that really can be extended as easily to BP++, then it may not put much burden on the reviewers as compared to verifiying everything else     

> __< j​effro256:monero.social >__ To be more precise, someone could formally write down the analogous argument for why batch verification is the same algebraically, with "high probability", as verifying each individually, and then we could increase the scope from the paper to the paper plus the batch verification argument     

> __< j​effro256:monero.social >__ I wish the original authors of the paper had expanded upon that in the paper, or else cited the previous work in that case, but I can't be too picky     

> __< k​ayabanerve:matrix.org >__ Rucknium @rucknium:monero.social: the reciprocal range proof, I believe, letting us skip the binary range proof proof so long as it isn't the basis of the reciprocal proof's proof.     

> __< k​ayabanerve:matrix.org >__ Batch verification is trivial.     

> __< k​ayabanerve:matrix.org >__ For any protocol which defines it's verification as group element G1 == G2, redefinition to G1 - G2 == 0 is possible.     

> __< k​ayabanerve:matrix.org >__ Batch verification is just, for a list of G1 and G2s, selecting random scalars to weight the G1s and G2s so they can't mingle.     

> __< k​ayabanerve:matrix.org >__ The performance benefit is that you don't have G1/G2. You have terms summing to them. Multi-scalar multiplications produce summed results far faster than individual components can be calculated.     

> __< Rucknium >__ That sounds like "The revised BP++ review scope is OK"     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-10-18T15:07:27+00:00
- Closed at: 2023-10-25T15:04:06+00:00
