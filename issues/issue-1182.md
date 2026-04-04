---
title: Monero Research Lab Meeting - Wed 02 April 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1182
author: Rucknium
assignees: []
labels: []
created_at: '2025-04-01T21:34:57+00:00'
updated_at: '2025-04-11T22:09:20+00:00'
type: issue
status: closed
closed_at: '2025-04-11T22:09:20+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [License for items in `research-lab` GitHub repo](https://github.com/monero-project/research-lab/pull/123). Creative commons for non-code materials?

4. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

5. [Cypher Stack Divisors Conclusion](https://gist.github.com/kayabaNerve/3a32eb393a41f48fe7c183c31dc57680).

6. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). [Analysis of risk of new decoy selection algorithm without a hard fork](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee).

7. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1177 

# Discussion History
## Rucknium | 2025-04-03T21:05:52+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1182     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< v​tnerd:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ Working on various lws-frontend stuff - finishing the lib and improving the build process     

> __< k​ayabanerve:matrix.org >__ Managing audits to various degrees     

> __< r​ucknium:monero.social >__ me: Have worked on more speedups to OSPEAD code. Running OSPEAD with updated data on the new 1TB RAM/256 thread MRL computing machine.     

> __< r​ucknium:monero.social >__ I noticed that you can now authenticate your ORCID in your GitHub profile: https://github.blog/changelog/2024-03-13-authenticate-orcid-id/     

> __< r​ucknium:monero.social >__ https://info.orcid.org/orcid-and-github-sign-memorandum-of-understanding/     

> __< r​ucknium:monero.social >__ When I did it, this was the message for the permissions: "Allow this organization or application [GitHub] to get your 16-character ORCID iD and read information on your ORCID record you have marked as public."     

> __< r​ucknium:monero.social >__ MoneroKon deadline for talks submissions is now April 14: https://cfp.twed.org/mk5/cfp     

> __< r​ucknium:monero.social >__ 3) License for items in research-lab GitHub repo. Creative commons for non-code materials? https://github.com/monero-project/research-lab/pull/123     

> __< r​ucknium:monero.social >__ I merged a dependency update into the `research-lab` repo. It's the first update to the repo in about 7 years. Thanks to Siren  for her review of the PR.     

> __< r​ucknium:monero.social >__ One of the other pending PRs is about the license for the repo, which is BSD.     

> __< j​berman:monero.social >__ me: just submitted a PR for the FCMP++ competition announcement: https://github.com/monero-project/monero-site/pull/2463     

> __< j​berman:monero.social >__ Implemented banning torsioned output pubkeys and commitments at consensus at the fork (after the fork, wallets won't have to do the expensive check for/clear torsion when building the tree), fixed a recently introduced issue with reorg handling in the wallet scanner tree builder, implemented a static table for FCMP++ proof size (calculating it from n inputs and n layers can be slo<clipped message>     

> __< j​berman:monero.social >__ w), implemented banning n_tree_layers >12 to keep the table small and portable (the tree supports a max of ~200 quadrillion outputs at 12 layers by my math)     

> __< j​berman:monero.social >__ This week I'm working on including the tree root in the block's PoW hash so clients can (eventually) verify PoW on the daemon's reported tree root, and therefore have a solid degree of confidence in the tree the client is using to construct or verify txs     

> __< r​ucknium:monero.social >__ But BSD is an open source license, not a license for written research. Actually, AFAIK, the MRL research bulletins do not have explicit licenses at all.     

> __< r​ucknium:monero.social >__ Would it be better to specify a Creative Commons license for MRL PDFs?     

> __< r​ucknium:monero.social >__ For example, this has no explicit license: https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf     

> __< r​ucknium:monero.social >__ BSD doesn't even explicitly cover software documentation, unlike MIT. As I understand it. The research bulletins probably cannot be considered documentation, anyway. Too much of a stretch.     

> __< b​asses:matrix.org >__ yes     

> __< j​berman:monero.social >__ +1 for CC     

> __< rbrunner >__ Not knowing enough about licensing to judge. I just asked myself whether you can give a license to something without one retro-actively without asking the author(s)     

> __< j​berman:monero.social >__ ^that too     

> __< r​ucknium:monero.social >__ Recently, I have been posting my work under CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/     

> __< j​berman:monero.social >__ (I'm not sure either)     

> __< r​ucknium:monero.social >__ which is a very permissive license IMHO     

> __< r​ucknium:monero.social >__ Probably, it depends if it is copyright the authors or copyright the Monero Project.     

> __< r​ucknium:monero.social >__ Or both     

> __< rbrunner >__ CC BY-SA 4.0 seems to have pretty widespread use     

> __< r​ucknium:monero.social >__ Or we could leave the papers that exist there as they are, and assign a CC license for materials in the future. Either way, I don't know exactly how the BSD license should be handled. Maybe put it in the directories where relevant. Where there is actual code.     

> __< r​ucknium:monero.social >__ I think the "Adapt — remix, transform, and build upon the material for any purpose, even commercially" clause leans toward very permissive. Since in theory someone could take the LaTeX of a document, make a few edits, add their name, and then re-publish it. But that's a strength for work that is unfinished, or could be extended.     

> __< r​ucknium:monero.social >__ Ok. I will make an issue in the repo so that it can be discussed further.     

> __< r​ucknium:monero.social >__ 4) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< r​ucknium:monero.social >__ Anything more to discuss on this?     

> __< k​ayabanerve:matrix.org >__ does "must distribute under" mean "must distribute under" or mean "if distributed, distributed under"? 🤔     

> __< k​ayabanerve:matrix.org >__ GPL has the notable edge where distributions must be licensed but there's no obligation to distribute. People accordingly sell GPL codebases, and while the customers receive it under a GPL license, I can't demand the company provide me a copy for free.     

> __< k​ayabanerve:matrix.org >__ I assume it means if distributed but would like to raise that Q on the choice of CC license     

> __< r​ucknium:monero.social >__ Here is the full text: https://creativecommons.org/licenses/by-sa/4.0/legalcode.en     

> __< j​berman:monero.social >__ "Anything more to discuss on this?" -> nothing from me     

> __< j​berman:monero.social >__ I'll re-raise the blog post PR: https://github.com/monero-project/monero-site/pull/2463     

> __< r​ucknium:monero.social >__ "b. ShareAlike. In addition to the conditions in Section 3(a) , if You Share Adapted Material You produce, the following conditions also apply. "     

> __< j​effro256:monero.social >__ Hi sorry I'm late     

> __< k​ayabanerve:matrix.org >__ Thanks for clarifying, Rucknium!     

> __< r​ucknium:monero.social >__ A different CC license could prevent alteration of the research materials, and only permit free distribution of them.     

> __< r​ucknium:monero.social >__ 5) Cypher Stack Divisors Conclusion. https://gist.github.com/kayabaNerve/3a32eb393a41f48fe7c183c31dc57680     

> __< k​ayabanerve:matrix.org >__ Other than what's in the gist, I don't have much to say other than I'm happy this'll be over.     

> __< j​berman:monero.social >__ Strong +1 on this proposal     

> __< rbrunner >__ Just to be sure: Was it clear for a long time that this will be a part of the way somehow, or has the necessity for this become clear recently?     

> __< r​ucknium:monero.social >__ This is the research product that will tell us that the divisors do not need a range proof because of the FCMP context, correct?     

> __< k​ayabanerve:matrix.org >__ rbrunner: We've incrementally handled the work from Veridise and review of each step has been expected.     

> __< k​ayabanerve:matrix.org >__ No Rucknium:     

> __< k​ayabanerve:matrix.org >__ We had three documents of note from Veridise     

> __< k​ayabanerve:matrix.org >__ Technique     

> __< k​ayabanerve:matrix.org >__ Logarithmic derivatives + no bit constraints     

> __< k​ayabanerve:matrix.org >__ Interactive proof + gadget attestation     

> __< k​ayabanerve:matrix.org >__ We've had the first two reviewed and we all pretty much agree the technique holds, you can take the logarithmic derivative of it     

> __< k​ayabanerve:matrix.org >__ Cypher Stack disagrees we don't need bit constraints because of ambiguity over what's occurring     

> __< k​ayabanerve:matrix.org >__ The technique proves that a collection of points sum to the additive identity (analogous to 0)     

> __< k​ayabanerve:matrix.org >__ You can take the logarithmic derivative of that to reduce the verification cost and that's fine     

> __< k​ayabanerve:matrix.org >__ The issue is regarding selecting which points are claimed to sum to zero.     

> __< k​ayabanerve:matrix.org >__ We can't claim, when proving a scaling of G, that the output point is 1G. Then everyone is using 1G for their random mask.     

> __< k​ayabanerve:matrix.org >__ We instead let the prover select a set constructed from 2**i G for 0 <= i <= 255, where the prover performs this selection via specifying coefficients     

> __< k​ayabanerve:matrix.org >__ That's where the bit constraints come in. Veridise says it still proves a sum regardless. Cypher Stack notes that someone who cannot prove 1 A + 1 B == 0 can forge such a proof by specifying -1 A + -1 B = 0 if that latter condition holds.     

> __< k​ayabanerve:matrix.org >__ So, when we allow the prover to specify the set, it's less proving these points sum to zero and more these points generate a subgroup of the elliptic curve where the prover knows an ordered index of the point at infinity?     

> __< k​ayabanerve:matrix.org >__ And that's fine for our uses. In the scalar multiplication document, this third paper from Veridise, we specifically prove a sums of points for     

> __< k​ayabanerve:matrix.org >__ s_i G_i + 1 R     

> __< k​ayabanerve:matrix.org >__ The prover gets control of s_i and R yet not G_1 nor 1.     

> __< k​ayabanerve:matrix.org >__ *-1 R, nor -1     

> __< k​ayabanerve:matrix.org >__ So yes, the prover specifies *their* point they use as a blinding factor, and yes they can malleate the index specified for that statement to sum to 0, yet they can't malleate the index w.r.t. to their output point: solely the fixed generator.     

> __< k​ayabanerve:matrix.org >__ That's fine for our construction and without issue.     

> __< r​ucknium:monero.social >__ And why doesn't the prover get control of those elements? Who controls them?     

> __< r​ucknium:monero.social >__ Or what     

> __< k​ayabanerve:matrix.org >__ But it's this question of how the bit constraints (/range proof) commentary is pretensed on this intent and context which is why I had a long discussion with CS on how to move forward, creating the resulting quote.     

> __< k​ayabanerve:matrix.org >__ The ZK proof constrains G_i/-1.     

> __< k​ayabanerve:matrix.org >__ It only lets the prover specify G_i and R.     

> __< k​ayabanerve:matrix.org >__ So for s_i G_i + -1 R == 0, we get the rewrite s_i G_i == 1 R. Cypher Stack's note is that lhs can be malleated. We don't care.     

> __< r​ucknium:monero.social >__ The ZK proof (which is maybe used for something else) constraints the elements, so a separate range proof isn't needed. Is that correct?     

> __< k​ayabanerve:matrix.org >__ It's only possible when we give the prover the ability to select points (so it's no longer sums of point, which sure, this malleation would break, yet sums of multisets of points), the sum statement itself holds (albeit malleated), and the malleation still reduces to a consistent index.     

> __< r​ucknium:monero.social >__ separate dedicated range proof     

> __< k​ayabanerve:matrix.org >__ 1) We'd never do a separate proof. We'd do a range proof inside the FCMP     

> __< k​ayabanerve:matrix.org >__ 2) We don't need a range proof     

> __< k​ayabanerve:matrix.org >__ Instead of proving 1 * G + 2 * G == 3 * G, you can prove 0 - 1 * G + 4 * G == 3 * G. You can malleate the lhs.     

> __< r​ucknium:monero.social >__ Who will check this logic? Or is the logic so simple that it need not be checked by review?     

> __< k​ayabanerve:matrix.org >__ You still have to prove you can open the rhs over the generator we specify, for some malleable index. That malleable index, while the prover can create infinite representations, still is only openable as a single index.     

> __< k​ayabanerve:matrix.org >__ It's like, I can send you "Hi" or "Hi ". I then have to tell you the English word I sent you. Regardless of how many spaces I added after, I still can only tell you I sent you "Hi"     

> __< k​ayabanerve:matrix.org >__ So those are the only two properties we need.     

> __< k​ayabanerve:matrix.org >__ 1) That the technique fundamentally holds     

> __< k​ayabanerve:matrix.org >__ 2) That while a single index may have infinite representations, you can't claim one representation is for distinct indexes     

> __< k​ayabanerve:matrix.org >__ And CS's noted malleation, which would be fixed by range proofs, doesn't break those properties (so we don't need range proofs)     

> __< k​ayabanerve:matrix.org >__ The third document from Veridise posits a complete interactive protocol, security proofs for it, and asserts my specification matches (after a pair of typos).     

> __< k​ayabanerve:matrix.org >__ The current quote from CS is for review of the latest document and a summary opinion asserting if they're convinced this is valid for Monero.     

> __< k​ayabanerve:matrix.org >__ My expectation is their work will confirm my inclinations, which I believe they share based on our discussions, their posited malleation doesn't break our use.     

> __< k​ayabanerve:matrix.org >__ This is just such a long discussion because our use is from the third document, and larger context, and CS specifically reviewed the second document prior, where the range proofs could be argued depending on intent.     

> __< k​ayabanerve:matrix.org >__ Hence why this current quote is meant not just to be review yet also a conclusive statement re: Monero's intent and use.     

> __< k​ayabanerve:matrix.org >__ If we all agree the academia is sound, and my specification is, I'd note Veridise is currently contracted to perform the audit my impl matches.     

> __< k​ayabanerve:matrix.org >__ (circling back to who checks the logic)     

> __< k​ayabanerve:matrix.org >__ > So, when we allow the prover to specify the set, it's less proving these points sum to zero and more these points generate a subgroup of the elliptic curve where the prover knows an ordered index of the point at infinity?     

> __< k​ayabanerve:matrix.org >__ This is probably my best technical comment for anyone who wants to understand this better.     

> __< k​ayabanerve:matrix.org >__ It also isn't too horrifically technical and ideally is decently accessible.     

> __< k​ayabanerve:matrix.org >__ Proving you know the index of an output point, over a specified generator, satisfies proving you know the discrete logarithm of the output point over the generator. Even for infinite possible indexes, the discrete logarithm is the index reduced by the curve order.     

> __< r​ucknium:monero.social >__ I hope today we can reach loose consensus on this 175 XMR expense for FCMP research https://gist.github.com/kayabaNerve/3a32eb393a41f48fe7c183c31dc57680     

> __< r​ucknium:monero.social >__ More comments from meeting attendees on this?     

> __< j​berman:monero.social >__ Appreciate the detail kayaba     

> __< rbrunner >__ If I got anything from these explanations, which is not much, frankly, it's this: This review is really needed to clear things up once and (hopefully) for all. +1 from me     

> __< r​ucknium:monero.social >__ Yes, thank you for explaining.     

> __< k​ayabanerve:matrix.org >__ And we do reuse indexes (we prove one point is an index of the subgroup generated by U, then we prove one point is the same index of the distinct subgroup generated by V). That was why I commented we require the indexes, while malleable, cannot have multiple openings. And again, they do not so long as the subgroup generators have the same order (which they do in our use).     

> __< k​ayabanerve:matrix.org >__ rbrunner: pay money to no longer have to think about things     

> __< j​effro256:monero.social >__ Without knowing many details besides what was outlined by Kayaba here, 175 XMR seems a little high considering that the review is more or less an analysis of non-applicability of this malleation issue, which seems already somewhat understood by both parties. That's my two cents     

> __< k​ayabanerve:matrix.org >__ :p     

> __< k​ayabanerve:matrix.org >__ It is not jeffro     

> __< k​ayabanerve:matrix.org >__ It's review of the third document specifying the interactive proof premised on this technique, and the summary opinion     

> __< k​ayabanerve:matrix.org >__ ... also, technically the third document asserts our specification matches the describe interactive proof, so review of that claim includes further review of the fcmp spec     

> __< k​ayabanerve:matrix.org >__ Also, the security proofs for the interactive proof premised on this technique     

> __< rbrunner >__ Right now it sounds a bit like a proof for a trick at a circus that a safety net is not necessary because the artists can do it. Better be damn sure.     

> __< r​ucknium:monero.social >__ Do we have all three documents from Veridise?     

> __< j​berman:monero.social >__ "I'd note Veridise is currently contracted to perform the audit my impl matches" -> isn't this the divisors impl we're discussing? For which we don't have someone contracted yet (as we're ideally waiting on the contest)? Or is that in reference to gadgets/circuit impl audit?     

> __< r​ucknium:monero.social >__ I think I only have two here. Maybe I am missing one: https://moneroresearch.info/index.php?action=list_LISTSOMERESOURCES_CORE&method=subcategoryProcess&id=1&catId=1     

> __< k​ayabanerve:matrix.org >__ Ugh. I may have yet to upload the third document. I thought SGP had prior...     

> __< k​ayabanerve:matrix.org >__ That'd help clarify for jeffro     

> __< r​ucknium:monero.social >__ I may definitely possibly be missing it in MR.info . But if we can get the doc titles, that would clarify things.     

> __< k​ayabanerve:matrix.org >__ rbrunner: From 0, you understand how proving knowledge of a discrete logarithm is saying you know the integer x such that x * G = O, right?     

> __< k​ayabanerve:matrix.org >__ jberman: This is re: the gadgets which is not the divisor construction.     

> __< j​effro256:monero.social >__ Sorry, I missed that the 175 proposal also includes review of Veridise's R1CS interactive proof. I mixed this up in my head with the other CS reviews of Veridise's work. Reading comprehension :/. That makes it a *lot* more justifiable     

> __< k​ayabanerve:matrix.org >__ rbrunner: We don't specify x. We specify s_i such that x = sum_{i=0}^255 s_i 2**i.     

> __< rbrunner >__ I don't dare to answer out of fear of follow-up questions :)     

> __< k​ayabanerve:matrix.org >__ Cypher Stack's claim is literally, as relevant to our use case, that instead of specifying bits such as 01000000, you can specify 20000000     

> __< k​ayabanerve:matrix.org >__ It has an equivalent evaluation yet is malleated.     

> __< rbrunner >__ I think I see, on a very high conceptual level, what is attempted here, and I am on bord if the review confirms.     

> __< k​ayabanerve:matrix.org >__ I mean, unless I'm horribly wrong and this is all broken, yet that's why we're paying Cypher Stack for their review and summary opinion on Monero's use and its security :p     

> __< k​ayabanerve:matrix.org >__ I just want to be clear it's more a miscommunication than taking a safety net from trapeze artists     

> __< j​berman:monero.social >__ Clarifying also: this proposal is for a summary opinion of divisors generally as used in FCMP++ (which includes addressing the malleation issue as one detail in that summary). I would think there is more beyond just the malleation issue and even just review of the 3rd Veridise doc, that encompasses such a review     

> __< k​ayabanerve:matrix.org >__ As for miscommunications and how the project was managed,     

> __< k​ayabanerve:matrix.org >__ > Other than what's in the gist, I don't have much to say other than I'm happy this'll be over.     

> __< j​effro256:monero.social >__ +1 on the proposal     

> __< r​ucknium:monero.social >__ If the Veridise document that is supposed to be reviewed is not yet publicly available, can it be posted ASAP? Possibly in the next few minutes?     

> __< r​ucknium:monero.social >__ I think it is OK to approve this with less than 24 hours notice, but not having the document that is supposed to be reviewed goes a little far.     

> __< k​ayabanerve:matrix.org >__ If I can message you to upload it, then yes     

> __< k​ayabanerve:matrix.org >__ I truly thought it prior was uploaded to the research CCS. Apologies there.     

> __< k​ayabanerve:matrix.org >__ Sent to Rucknium. I cannot upload it under the research CCS myself for some hours.     

> __< r​ucknium:monero.social >__ Uploading very soon. Is this a 2025 doc or 2024?     

> __< k​ayabanerve:matrix.org >__ I can do charades to try and act out its contents while we wait     

> __< k​ayabanerve:matrix.org >__ Received March 5th, 2025     

> __< j​berman:monero.social >__ sgp_: shared it in MRL chat here via a matrix link that's dead now: https://libera.monerologs.net/monero-research-lab/20250306#c505745 , we just need a more permanent URL (MoneroResearch.info is good for that)     

> __< k​ayabanerve:matrix.org >__ Oh thank God I'm not insane and hoarding documents     

> __< k​ayabanerve:matrix.org >__ Thank you jberman     

> __< r​ucknium:monero.social >__ Sorry, I must have missed that     

> __< r​ucknium:monero.social >__ Here: https://moneroresearch.info/259     

> __< r​ucknium:monero.social >__ Any more comments on this proposed expenditure for FCMP research?     

> __< r​ucknium:monero.social >__ +1 from me on https://gist.github.com/kayabaNerve/3a32eb393a41f48fe7c183c31dc57680     

> __< j​berman:monero.social >__ btw still keeping this FCMP++ Research Tracking spreadsheet updated: https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/     

> __< r​ucknium:monero.social >__ I see loose consensus here in favor of 175 XMR for "Cypher Stack Divisors Conclusion" https://gist.github.com/kayabaNerve/3a32eb393a41f48fe7c183c31dc57680     

> __< r​ucknium:monero.social >__ 6) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork. https://github.com/Rucknium/OSPEAD  https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee     

> __< r​ucknium:monero.social >__ I posted some analysis code in the gist ^. I don't really have any new results to share. I have been working on code speed improvements: https://github.com/Rucknium/OSPEAD/commits/main/     

> __< r​ucknium:monero.social >__ and actually re-running the OSPEAD estimates on the new MRL research machine. Using 100 threads and 800 GB of RAM :D     

> __< r​ucknium:monero.social >__ The machine has 256 threads, but not using all of them at the moment.     

> __< r​ucknium:monero.social >__ Thank you to CCS donors for supporting the 1TB of RAM purchase.     

> __< rbrunner >__ Yeah, we don't want to overdo it, do we :)     

> __< r​ucknium:monero.social >__ And thank you to gingeropolous  for setting up and managing the machine.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< j​effro256:monero.social >__ When deploy OSPEAD Hadoop cluster?     

> __< j​effro256:monero.social >__ Just for fun, could you potentially imagine designing the data processing to use something like MapReduce? Is it possible/productive to parallelize it this way?     

> __< r​ucknium:monero.social >__ jeffro256: `bjr()` has the capability to send jobs to separate machines in the same cluster. It uses an SSH connection, basically. I did that on previous runs, but not this one. There is overhead because you have to send data over the wire to the other machines. It's probably not worth the overhead now that `bjr()` is much faster.     

> __< r​ucknium:monero.social >__ But you could split the processing by week of data, and send that over the wire.     

> __< r​ucknium:monero.social >__ Some of the steps in the whole process aren't very parallelized. Pulling data from `monerod`? That's as parallel as I can get it. The multiple R threads are waiting on the node to respond. Even if I have multiple nodes on the same storage medium, I don't get much speedup, so it's probably I/O bounded. Then, the actual optimization in https://rucknium.github.io/OSPEAD/CCS-milestone<clipped message     

> __< r​ucknium:monero.social >__ -2/OSPEAD-docs/_book/parametric-fit.html , which takes about a day, can't be parallelized much. The optimization process to numerically find the minimum of the function depends on the results of previous iterations.     

> __< r​ucknium:monero.social >__ "aren't very parallelizable", I mean     

> __< b​oog900:monero.social >__ have you tried reading directly from monerod's DB?     

> __< r​ucknium:monero.social >__ No, because it's not documented AFAIK     

> __< p​reland:monero.social >__ I second this, I don’t think it’s documented (or at least not documented well)     

> __< p​reland:monero.social >__ It also is very finicky when trying to open it in standard database viewers     

> __< b​oog900:monero.social >__ SyntheticBird: made this: https://github.com/Cuprate/old_book/tree/main/src/monero/database, also I made this tool in Rust: https://github.com/Boog900/monero-db-rs/     

> __< r​ucknium:monero.social >__ If I wanted to work on a speedup for that part of my workflow, it would be setting up incremental updates. As of now, I re-build the database in RAM from scratch, from the first RingCT block. But with incremental updates, if I want to add a new variable to the database, I would have to re-build from scratch again.i     

> __< r​ucknium:monero.social >__ It only takes about 12 hours to pull the necessary data from the node.     

> __< r​ucknium:monero.social >__ boog900: Thanks.     



# Action History
- Created by: Rucknium | 2025-04-01T21:34:57+00:00
- Closed at: 2025-04-11T22:09:20+00:00
