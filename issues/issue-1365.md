---
title: Monero Research Lab Meeting - Wed 01 April 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1365
author: Rucknium
assignees: []
labels: []
created_at: '2026-04-01T15:09:51+00:00'
updated_at: '2026-04-14T21:12:49+00:00'
type: issue
status: closed
closed_at: '2026-04-14T21:12:48+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/issues/166).

5. [Grease Payment Channels](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).

6. [Bulletproofs*: Verifier-Efficient Arithmetic Circuit Proofs via Folding](https://eprint.iacr.org/2026/586). [CCS update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_35351).

7. [CCS proposal: I2P SAMv3 support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1359 

# Discussion History
## Rucknium | 2026-04-08T15:04:02+00:00
Log:

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1365     

> __< rucknium >__ 1. Greetings     

> __< UkoeHB >__ Hi     

> __< vtnerd >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< rbrunner >__ Hello     

> __< emsczkp:matrix.org >__ Hi     

> __< iamnew117:matrix.org >__ hello      

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< vtnerd >__ Me: bug fixes and reviews for monerod, tests for the lws /feed endpoint, working on docker stuff for lws build, and lastly updating lws+lwsf for the API changes in the carrot libs     

> __< jberman >__ waves     

> __< syntheticbird >__ Hi     

> __< jberman >__ me: about to post a CCS proposal for the FCMP++ integration audits, sgp_:monero.social has been in direct comms with a number of candidates on phase 1, various monerod fixes     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< articmine >__ Hi     

> __< jeffro256 >__ Me: talking with Ledger, auditors, and other contributors. Looking into LWS performance leveraging GPU and what happens with CARROT      

> __< jberman >__ Posting a CCS proposal today to request XMR upfront to budget for all 3 phases of the audit, sgp in comms with auditors soliciting quotes for phase 1     

> __< rucknium >__ jeffro256:monero.social: "Looking into LWS performance leveraging GPU" Can you give more info on that?     

> __< jeffro256 >__ Do you know of price points already?     

> __< jberman >__ We're requesting under $50k for each of the 3 phases, so budgeting $150k for the entire audit     

> __< jeffro256 >__ rucknium: Yeah I'm doing a quick detour to see if using the GPU is feasible for performinh bulk scanning of thousands of view-incoming keys      

> __< vtnerd >__ https://github.com/vtnerd/monero-lws/issues/245     

> __< jberman >__ Then leftover funds would get repurposed for auditing the less critical components (like the torsion check)     

> __< endogenic >__ that is elite jeffro     

> __< jeffro256 >__ jberman: That's a decent ceiling. I don't think any of those phases should take more than that.      

> __< rucknium >__ IIRC, Monero Nodo wanted to make its onboard GPU useful for something.     

> __< jberman >__ kayabanerve:matrix.org has also expressed strong interest in GPU scanning for normal wallets     

> __< rucknium >__ Monero Nodo's GPU is "Mali-G610, quad-core"  https://moneronodo.com/product/nodo/     

> __< jberman >__ (tbc, an interest in seeing it explored, not a personal interest in working on it)     

> __< syntheticbird >__ rest in peace to whoever is gonna adventure the great vulkan api     

> __< vtnerd >__ The big unknown is the massive amount of code needed to make it happen, but maybe with view tags and just x25519 scalarmult something could be made of it     

> __< vtnerd >__ Massive is the wrong word, just bigger than ideal      

> __< rucknium >__ Anything more on this agenda item?     

> __< jberman >__ nothing from me     

> __< jeffro256 >__ There's a lot of parallelization that can happen in the field / group math itself which I'm looking at, which would allow the breakdown of the program into many smaller parts, and maybe allow for better throughput      

> __< rucknium >__ 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/issues/166).     

> __< jberman >__ kayaba is working on last remaining task items, then we should be ready to go     

> __< rucknium >__ 5. Grease Payment Channels (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).     

> __< rucknium >__ My list of downsides to this proposal are 1) No trustless Key Escrow Service (KES) yet, 2) The use case is limited so far, 3) The proposal is expensive in XMR terms.     

> __< rucknium >__ I wonder if the Grease team could or would wait to start working on this phase of development until trustless KES was available.     

> __< rucknium >__ Any more discussion of this item?     

> __< rucknium >__ 6. Bulletproofs*: Verifier-Efficient Arithmetic Circuit Proofs via Folding (https://eprint.iacr.org/2026/586). CCS update (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_35351).     

> __< jeffro256 >__ Yeah I have a similar feeling. I understand that they want to keep it out of scope, but it's one of the single most critical components of the system. And from my experience, designing modular systems is cool and all, but usually you want at least one working implementation of a missing module in your system so you get a feel and design for how it would interact in the real word      

> __< rucknium >__ Any more questions or comments for emsczkp:matrix.org ?     

> __< emsczkp:matrix.org >__ Hi!     

> __< jeffro256 >__ Otherwise you have an API which you don't end up using b/c the first implementation reveals things you didn't expect to need in an API      

> __< emsczkp:matrix.org >__ Regarding questions posed in the previous MRL meeting by jberman, which I thank for valuable comments on the paper and questions: the folding prover does not necessarily have to coincide with the NARK prover. The NARK prover knows the original secret witness, whereas the folding prover operates on the NARK proofs.     

> __< emsczkp:matrix.org >__ In BP*, NARK proofs are split into instance and witness parts. The folding prover takes both parts as input and performs the fold. Precisely, the witness data used here are those required by the (modified BP) algebraic verifiers for  constraint checks and the commitment-consistency check. Such witness data differ from the original secret witness.     

> __< emsczkp:matrix.org >__ So, to answer to jberman, the paper designs a folding scheme in which the NARK prover and the folding prover are conceptually decoupled. The folding prover does not need the original secret witness, but it does need the instance-witness parts for the proof and accumulator required by the folding relation. In that sense, a third party could fold already-generated NARK proofs.     

> __< emsczkp:matrix.org >__ I would phrase the application level implications cautiously, since the paper itself at this stage focuses on the folding scheme design rather than a concrete deployment scenario. But, My current intuition is that this decoupling could be useful in applications where one entity produces proofs and another entity folds them.     

> __< emsczkp:matrix.org >__ And that's the case, as also pointed out with jberman: https://github.com/monero-project/research-lab/issues/110     

> __< emsczkp:matrix.org >__       

> __< emsczkp:matrix.org >__ Here, BP* could potentially enable the idea outlined by kayabanerve, where a block producer folds many proofs from many parties without knowing secrets or interacting with parties.      

> __< jberman >__ When we were initially discussing this CCS proposal, I expressed a desire / interest in seeing if the BP* design that could potentially enable exactly that^, so it's exciting to me that this potential is on the table with BP*     

> __< emsczkp:matrix.org >__ thank you!     

> __< jberman >__ I admit my math expertise is not deep enough to give a very strong review of the actual math itself, but it seems to pass a smell test with adequate rigor imo. It would be great to get it reviewed by those with the deeper math expertise, but generally I think this work is potentially bearing larger fruits than was initially even proposed, and I'm cautiously optimistic about the direction     

> __< rucknium >__ emsczkp:matrix.org: Do you plan to submit the paper to a peer-reviewed conference or journal when it is finished?     

> __< emsczkp:matrix.org >__ yes, that's when all future works/steps will be addressed     

> __< rucknium >__ More discussion of this agenda item?     

> __< jberman >__ Thank you emsczkp:matrix.org !!     

> __< emsczkp:matrix.org >__ thank you all !!     

> __< rucknium >__ 7. CCS proposal: I2P SAMv3 support (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650).     

> __< rucknium >__ Last time more discussion was about administrative questions, e.g. funding from the existing bounty or as a fresh CCS proposal.     

> __< jpk68:matrix.org >__ After a fair amount of discussion, I believe that has mostly been resolved (a fresh CCS would be the best approach)     

> __< jpk68:matrix.org >__ Now that the milestones are more solidified, it would be great to hear feedback on it, if any are willing :)     

> __< jpk68:matrix.org >__ Plowsof left a comment regarding the CCS approach, if anyone is interested. It seems the discussion at this point is about who would be the best to do the CCS itself     

> __< rucknium >__ Seeing no discussion for now, I will move to:     

> __< rucknium >__ 8.  Any other business     

> __< rucknium >__ https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/     

> __< rucknium >__ https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf     

> __< rucknium >__ Before the meeting, semisimple:monero.social  suggested a discussion, at some unspecified time, about Google's new lower estimates for breaking the discrete log problem.     

> __< rucknium >__ Maybe people want to discuss a little now or we can agree to put it on the agenda next meeting. I don't know if there is a lot more to say than has already been said except for post-quantum is closer than expected.     

> __< rucknium >__ Some discussion on the MRL GitHub repo: Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography (https://github.com/monero-project/research-lab/issues/131).     

> __< articmine >__ This is making the case for the acceleration of the post quantum issue.     

> __< rucknium >__ > Specifically, we have compiled two quantum circuits (a sequence of quantum gates) that implement Shor's algorithm for ECDLP-256: one that uses less than 1,200 logical qubits and 90 million Toffoli gates and one that uses less than 1,450 logical qubits and 70 million Toffoli gates. We estimate that these circuits can be execu [... too long, see https://mrelay.p2pool.observer/e/_umsnfUKcm9VcEVM ]     

> __< rucknium >__ > This is an approximately 20-fold reduction in the number of physical qubits required to solve ECDLP-256 and a continuation of a long history of gradual optimization in compiling quantum algorithms to fault-tolerant circuits.     

> __< rucknium >__ ^ That is what Google says.     

> __< rucknium >__ I don't know how to interpret that or how many widgets can be stabilized for how long and in what timeline.     

> __< vtnerd >__ They've still got to build a working prototype that does it, which is sort of the frustration in knowing when/if/maybe never     

> __< jberman >__ After all FCMP++ / Carrot research tasks are complete, I'd advocate for a strong concerted effort on designing a complete PQ protocol. tevador has already begun on a PQ key exchange protocol here: https://github.com/monero-project/research-lab/issues/151     

> __< jberman >__ I think it may be worth contracting a research team on a full-time basis for that work     

> __< rbrunner >__ As I see it, that's more or less the only "wiggle room" we realistically have: No more "conventional" improvements after the FCMP++, but directly onwards to PQ resilience     

> __< rbrunner >__ *after the FCMP++ hardfork     

> __< rbrunner >__ Maybe that proposal will be able to get "loose consensus" in the light of this Google paper ...     

> __< rucknium >__ Should post-quantum issues be put on next week's agenda?     

> __< rbrunner >__ I would give it a "why not" :)     

> __< articmine >__ Yes      

> __< syntheticbird >__ Yes     

> __< rucknium >__ I will put it on the agenda.     

> __< rucknium >__ We can end the meeting here. Feel free to continue discussing.     

> __< rbrunner >__ Getting a research team maybe just got a lot more difficult, if many more parties will take it seriously.     

> __< rucknium >__ Or easier, because Monero can build on others' work :)     

> __< rbrunner >__ "Dear Quantum researcher, don't work for Google, don't work at a world-class university, don't work for IBM, and so ... your place is at the side of the Monero team!"     

> __< rbrunner >__ Well, we need post-quantum crypto researchers, but still     

> __< articmine >__ rbrunner: The question is what other chains are taking this issue seriously.     

> __< articmine >__ Starting with chains with a greater market cap than Monero      

> __< endogenic >__ why is that the question?     

> __< endogenic >__ besides, even if monero suddenly was looking to other projects instead of the research for leadership for some reason, would one other major project be sufficient ? https://pq.ethereum.org     

> __< endogenic >__ and isnt btc kind of hosed without a turnstile anyway? (and good luck with that)     

> __< endogenic >__ besides the nuances are so specific to what we actually do that it requires analysis of what we actually do. like randomx is for example probably fine, as i understand it     

> __< endogenic >__ but other things will not be fine. ecc signing and key exchange are broken by a likely imminent or already existent qc     

> __< syntheticbird >__ Regarding assessing monero's vulnerability to quantum computers, I'll just post these two gist from jeffro that for some reason people are tending to forgot: https://gist.github.com/jeffro256/4155401274699e0437ba5b79b93c647f https://gist.github.com/jeffro256/ce35d497f3f191629a6a00da5e6ab828     

> __< endogenic >__ sounds like jeffro's being elite again     

> __< endogenic >__ it's more comfortable to forget     

> __< endogenic >__ sometimes     

> __< endogenic >__ but it won't be possible soon     

> __< sgp_ >__ jberman: Fwiw, MAGIC Grants already has money set aside for this, so we can act on expertise asap     

> __< sgp_ >__ syntheticbird: It's almost like random gists get lost 😅     



# Action History
- Created by: Rucknium | 2026-04-01T15:09:51+00:00
- Closed at: 2026-04-14T21:12:48+00:00
