---
title: Monero Research Lab Meeting - Wed 03 April 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/986
author: Rucknium
assignees: []
labels: []
created_at: '2024-04-01T13:44:15+00:00'
updated_at: '2024-04-10T19:37:09+00:00'
type: issue
status: closed
closed_at: '2024-04-10T19:37:09+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Research [Pre-Seraphis Full-Chain Membership Proofs](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86). @kayabaNerve @UkoeHB @AaronFeickert @cypherstack

4. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#983 

# Discussion History
## AaronFeickert | 2024-04-01T16:22:20+00:00
There are a few different research topics for which Cypher Stack's services may be useful; for clarity, I'll briefly outline them here in advance of the meeting.
- **Seraphis papers**. As noted in a recent [proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441), Seraphis has two associated papers: one describes a more general framework for privacy-respecting transaction protocols, and another instantiates this framework to a specific design for use in Monero. The proposal (per recommendation) would review the first paper, with the expectation of a later proposal to review the second. Such review would be important as part of an assertion that the Seraphis design is suitable for implementation.
- **Generalized Bulletproofs for full-chain membership proofs**. The use of curve trees for any full-chain membership proof application (whether for Seraphis or for RingCT) requires a modification to the Bulletproofs arithmetic circuit proving system design. While this modification is known, it has not been formally proven secure, and should be.
- **Full-chain membership proofs on RingCT**. A recent [gist](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86) proposes a design that uses a full-chain membership proof modification as a drop-in replacement to CLSAG signatures for the existing RingCT transaction protocol. This would presumably require review of both the design and the specific circuit implementation used for it.

## Rucknium | 2024-04-03T19:36:56+00:00
Log:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/986     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​gp_:monero.social >__ hello     

> __< a​rticmine:monero.social >__ Hi     

> __< o​ne-horse-wagon:monero.social >__ Hello     

> __< janowitz >__ Hello everybody!     

> __< c​haser:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ Hi     

> __< d​iego:cypherstack.com >__ Hello hello!     

> __< jberman >__ hello     

> __< binaryFate >__ hello     

> __< b​oog900:monero.social >__ Hi     

> __< a​aron:cypherstack.com >__ Heyo     

> __< rbrunner >__ Hello     

> __< dEBRUYNE >__ Hi!     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ Meeting time?     

> __< k​ayabanerve:matrix.org >__ Matrix is broken     

> __< k​ayabanerve:matrix.org >__ I am here     

> __< k​ayabanerve:matrix.org >__ FCMPs, as expected     

> __< r​ucknium:monero.social >__ me: I posted the preliminary report about the suspected black marble flooding: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< janowitz >__ @rucknium Very good read!     

> __< r​ucknium:monero.social >__ As of 12:00 UTC today, estimated mean effective ring size is back up to 14 (assuming the spam was by an adversary creating black marble outputs): https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/empirical-effective-ring-size.png     

> __< jberman >__ me: the asynchronous wallet scanner, ironed out final kinks / started on benchmarking. pushing final changes and marking the PR ready for review today     

> __< r​ucknium:monero.social >__ I am also tracking an anomalous rise in 2nd tier fee transactions. We are over 50% without clear cause in the last 3-4 days: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/share-tx-in-fee-tier-spam-removed.png     

> __< janowitz >__ @rucknium do you think we see another wave of the attack rn with tx above 50k/day or is it rather organic?     

> __< a​rticmine:monero.social >__ I am working on the scaling and fees.     

> __< a​rticmine:monero.social >__ Now that we have estimates for FCMP transactions weights. I can say that a minimum penalty free zone of 600000 bytes is realistic. Also a 2% growth rate. Minimum fee about 5x to 6x the current     

> __< r​ucknium:monero.social >__ j​anowitz: I'm not sure. Maybe the increase of 2nd tier fee txs is the suspected spammer changing behavior. Thanks for your questions.     

> __< dEBRUYNE >__ Blocks don't seem as full as last time though     

> __< dEBRUYNE >__ ^ rucknium     

> __< dEBRUYNE >__ At least for now     

> __< r​ucknium:monero.social >__ I also posted a CCS funding proposal to continue this research to help guide decisions on ring member size increases and fees to defend against black marble attacks. Feedback and questions are welcome :) https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/439     

> __< k​ayabanerve:matrix.org >__ Is it not superseded by FCMPs /s     

> __< r​ucknium:monero.social >__ Yes, block/txpool are not full, which means that the auto fee increase in the CLI/GUI should not have been triggered according to what I understand.     

> __< k​ayabanerve:matrix.org >__ I do support further research on rings, even if I'm hopeful to replace them quite soon     

> __< r​ucknium:monero.social >__ kayabanerve: In seriousness, CLSAG with higher ring size is proven battle-tested technology/cryptography. FCMP is not (yet).     

> __< r​ucknium:monero.social >__ 3) Discussion on Research Pre-Seraphis Full-Chain Membership Proofs. @kayabaNerve @UkoeHB @AaronFeickert @cypherstack https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86     

> __< k​ayabanerve:matrix.org >__ It's also known to be vulnerable, but I wouldn't expect it to be forgeable.     

> __< s​gp_:monero.social >__ see jtgrassie's comment at the bottom; is this description still valid? https://monero.stackexchange.com/a/11658/42     

> __< a​rticmine:monero.social >__ The scaling proposal will include lowering the surge of the short term median from 50 to 16. Combine this with ring 64 CLSAG and the math for a black marble attack gets real tough     

> __< r​ucknium:monero.social >__ sgp_: selsta can answer about what exactly `wallet2` does (or is supposed to do) with automatic fee increases.     

> __< k​ayabanerve:matrix.org >__ I'm available for questions. This meeting, I'd call for agreement FCMPs replacing CLSAG is a valid goal and if it works out, should be integrated and deployed.     

> __< c​haser:monero.social >__ AFAIK the multipliers there are out of date.     

> __< a​rticmine:monero.social >__ Those fee level are for before the last HF in 2022     

> __< k​ayabanerve:matrix.org >__ I'm disinterested in drawing this out for months and having it as delayed as Seraphis. I won't ask to rush it, yet I personally see an efficient path forward and would like to take it.     

> __< janowitz >__ @kayabanerve I am full of hope for FCMPs but I wouldn't rush them too much until they are properly peer reviewed and audited, also their implementation.     

> __< s​gp_:monero.social >__ If someone knowledgeable could update that SE post with the latest info, that would be appreciated :)     

> __< k​ayabanerve:matrix.org >__ The linked proposal is comprehensive to the steps of review and auditing.     

> __< selsta >__ if there is a backlock or the last block is 90% full -> priority 2, otherwise it selects priority 1     

> __< tevador >__ FWIW, I fully support focusing on FCMP that can replace CLSAG before Seraphis.     

> __< s​gp_:monero.social >__ anowitz: kayaba's proposal is quite thorough with the review process needed; is there any part of this that you feel in inadequate?     

> __< rbrunner >__ Question from a crypto-noob: What is described there in the FCMP gist probably works out, i.e. probably doesn't contain something that totally does not fly?     

> __< k​ayabanerve:matrix.org >__ I have multiple months budgeted for its review in my timeline. One of the first steps on the list is immediately having Aaron Feickert: provide proofs of security for GBPs.     

> __< selsta >__ but i don't know what mobile wallets are doing, it's possible they have different auto fee selection code     

> __< k​ayabanerve:matrix.org >__ It has multiple fallbacks rbrunner     

> __< k​ayabanerve:matrix.org >__ If the super efficient DLog proof fail, we have less efficient ones.     

> __< a​rticmine:monero.social >__ There is a need for clarity on fees. I will address     

> __< rbrunner >__ So if there is a problem it probably a quite subtle one, that only a detailed analysis will show     

> __< k​ayabanerve:matrix.org >__ They're still tolerable IMO. As slow as 3 16-out Bulletproofs.     

> __< r​ucknium:monero.social >__ I will repeat what I said on Monday about time allocation for mathematical security proofs:     

> __< r​ucknium:monero.social >__ IIRC "Fail fast and early" is a project management principle. Maybe a single large CCS by Cypher Stack could have this decision tree: 1) Try to write a security proof for GBP. If succeed: 2a) Research "FCMP on RingCT". If fail: 2b) Do the proposed "Seraphis General Paper Review". (2a) would also require another entity to review the security proofs before mainnet. (2b) could mean t<clipped message     

> __< r​ucknium:monero.social >__ hat another entity tries to write GBP security proofs.     

> __< k​ayabanerve:matrix.org >__ No. Several components may not live up to expectations re: intended performance. If one doesn't, it's still acceptable IMO.     

> __< r​ucknium:monero.social >__ Does the "less efficient ones" still require GBP?     

> __< a​aron:cypherstack.com >__ To be clear, a security review for GBP would apply to both FCMP-for-RingCT and FMCP-for-Seraphis     

> __< k​ayabanerve:matrix.org >__ That leaves with almost everything having to fail for the effort to fail.     

> __< a​aron:cypherstack.com >__ They both use the technique     

> __< k​ayabanerve:matrix.org >__ So I believe it's quite tolerant to setbacks.     

> __< d​angerousfreedom:monero.social >__ kayabanerve:  what are the new crypto libraries that you would need to introduce to have FCMP working now?     

> __< k​ayabanerve:matrix.org >__ I am also calling for proofs of all the components, have extensively timelined review, and it'd start with proofs of GBPs which at the biggest concern re: if they fail to work out.     

> __< tevador >__ BTW, due to kayabanerve's proposal, I revisited my tower-cycle for Ed25519 and managed to find an even better one where both curves have a = -3, which allows for more efficient formulas to be used.     

> __< jberman >__ I +1 FCMPs replacing CLSAG is a valid goal pre-Seraphis     

> __< rbrunner >__ Where do those "GBPs" come from? Somebody else invented them?     

> __< k​ayabanerve:matrix.org >__ Rucknium: We could deploy a non-GBP variant if the divisor technique maintains its performance.     

> __< k​ayabanerve:matrix.org >__ @dangerousfreedom Two curve libs, GBPs, divisors, the circuit, and some util libs     

> __< k​ayabanerve:matrix.org >__ We can near immediately start review + audits of GBPs + divisors     

> __< r​ucknium:monero.social >__ kayabanerve: So we could flow: Try GBP security proofs. If unable: Try security proofs for Eagan's divisor technique. If unable: Start math review of Seraphis.     

> __< r​ucknium:monero.social >__ I mean for CypherStack's work     

> __< k​ayabanerve:matrix.org >__ Happy to hear tevador. I'd love to have you contribute the impls, though they do probably have to be in Rust to minimize FFI traversals :/     

> __< k​ayabanerve:matrix.org >__ (Not an issue on the scale of the proof, an issue on the scale of EC adds)     

> __< v​tnerd:monero.social >__ Sorry forgot about this again, present in meeting now     

> __< r​ucknium:monero.social >__ kayabanerve: Your proposal would require monerod to include Rust code. Is this correct?     

> __< k​ayabanerve:matrix.org >__ rbrunner: Authors of curve trees, with Aaron Feickert: having notated it     

> __< r​ucknium:monero.social >__ What does "notated" mean?     

> __< k​ayabanerve:matrix.org >__ I'd have to check with Aaron Feickert: if they want to work on the divisors.     

> __< k​ayabanerve:matrix.org >__ Eagen claims the techniques are common with BP++'s permutation argument, so Aaron may have prior experience and the appetite. I'd check before assuming.     

> __< rbrunner >__ Is already clear what Monero with FCMPs would probably mean for hardware wallets?     

> __< k​ayabanerve:matrix.org >__ I have a meeting in two hours to discuss divisors and circuit auditing with a firm for what it's worth.     

> __< r​ucknium:monero.social >__ kayabanerve: You are aware that Aaron Feickert was unable to verify Eagan's BP++ security proofs, right? If they are the same as for the divisor technique, then?     

> __< k​ayabanerve:matrix.org >__ Yes to needing Rust, unless completely rewritten.     

> __< rbrunner >__ (That's also a concern for Seraphis and Jamtis, of course)     

> __< k​ayabanerve:matrix.org >__ Notated means Aaron literally typed up the modifications to the protocol that were proposed by the curve trees authors.     

> __< a​aron:cypherstack.com >__ @Rucknium: we documented the GBP protocol, but did not prove it secure     

> __< a​aron:cypherstack.com >__ It was not documented previously     

> __< k​ayabanerve:matrix.org >__ The curve tree authors only commented the theory of the math, and did an implementation.     

> __< a​aron:cypherstack.com >__ But yes, it is correct that we did not find all BP++ security proofs convincing as written     

> __< k​ayabanerve:matrix.org >__ rbrunner: Hardware wallets would have reduced memory use, actually.     

> __< r​ucknium:monero.social >__ I understand. GBP was "left as an exercise to the reader" in the Curve Trees paper basically.     

> __< a​aron:cypherstack.com >__ Rucknium: correct     

> __< rbrunner >__ I think the "bottleneck" for hardware wallets would be: How much new code, and what kind of code, would they have to implement?     

> __< k​ayabanerve:matrix.org >__ They'd do a addendum proof, not the FCMP. This achieves the same proof separation as Seraphis.     

> __< k​ayabanerve:matrix.org >__ Rucknium: The two sets of proofs are completely distinct.     

> __< k​ayabanerve:matrix.org >__ "They'd" refers to the hardware wallets.     

> __< k​ayabanerve:matrix.org >__ It'd be a generalized schnorr protocol of 4 points and three scalars.     

> __< k​ayabanerve:matrix.org >__ It's a very simple protocol comparable to doing multiple schnorr signatures.     

> __< k​ayabanerve:matrix.org >__ It'd also have the same additive blinding currently used w.r.t to the private spend key.     

> __< rbrunner >__ Sounds like "doable" as you describe it, then     

> __< k​ayabanerve:matrix.org >__ Clarifying here, BP++ claims to use similar algebraic techniques to divisors. I'm aware Aaron wasn't convinced for the BP++ proofs. This is a much smaller topic with much more provenance.     

> __< k​ayabanerve:matrix.org >__ Aaron may be interested in reviewing divisors, or they may not be. I'd have to ask.     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: Would you be interested/claim to be capable of reviewing elliptic curve divisors as posited for use here?     

> __< r​ucknium:monero.social >__ AFAIK the main goal of today's meeting is to get as far as we can on developing a CCS proposal for Cypher Stack (AFAIK Aaron Feickert /Sarang doing most or all of the work) to work on mathematical security proofs and/or review of proposed cryptography for MRL for the next couple of months.     

> __< a​aron:cypherstack.com >__ Would need to know the precise scope of this     

> __< s​yntheticbird:monero.social >__ Noob question, would supporting pre-Seraphis FCMPs require address generation/changes ?     

> __< a​aron:cypherstack.com >__ But yes, I'd like to know what, if any, proposals from Cypher Stack the community would like to see     

> __< a​aron:cypherstack.com >__ Right now Diego Salazar has one open for Seraphis     

> __< k​ayabanerve:matrix.org >__ Eaten posted the calculation of an elliptic curve divisor which interpolates a series of points as useful for proving in-circuit an output point is the sum of a series of points.     

> __< k​ayabanerve:matrix.org >__ *Eagen     

> __< plowsof >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441 CS' open CCS      

> __< a​aron:cypherstack.com >__ I'd previously commented on a few possible research areas https://github.com/monero-project/meta/issues/986#issuecomment-2030089046     

> __< k​ayabanerve:matrix.org >__ They commented specifically on challenged evaluation, preventing forgeries, and using the logarithmic derivative to minimize in-circuit multiplications.     

> __< k​ayabanerve:matrix.org >__ It's quite heavy on the group structure of the curve itself.     

> __< c​haser:monero.social >__ AFAIK no     

> __< k​ayabanerve:matrix.org >__ No new address/privacy pool.     

> __< rbrunner >__ Well, that would probably also kill it as pre-Seraphis thing, no?     

> __< rbrunner >__ So lucky that we don't get new addresses ...     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: I wouldn't mind having you also review divisors. I know you believe the review of the circuit may be best done by others. Would you also volunteer yourself as a candidate for this topic?     

> __< k​ayabanerve:matrix.org >__ Something something Weil, Picard group?     

> __< a​aron:cypherstack.com >__ kayabanerve: Can you remind me the source documentation for this?     

> __< a​aron:cypherstack.com >__ And how you'd intend for this to fit in with any other desired research?     

> __< k​ayabanerve:matrix.org >__ Eagen's EC IP proof using divisors as an IACR preprint.     

> __< k​ayabanerve:matrix.org >__ https://eprint.iacr.org/2022/596     

> __< a​aron:cypherstack.com >__ That's it, thanks     

> __< rbrunner >__ Is the current thinking still that much of the work done for pre-Seraphis FCMPs will carry over to Seraphis without massive additional effort?     

> __< dEBRUYNE >__ <tevador> FWIW, I fully support focusing on FCMP that can replace CLSAG before Seraphis. <= +1     

> __< k​ayabanerve:matrix.org >__ Section 3.2, not 4.*.     

> __< a​aron:cypherstack.com >__ On a brief glance, I don't see any particular security model, formal statements, or security proofs     

> __< a​aron:cypherstack.com >__ Meaning it's not clear what exactly I'd be doing     

> __< k​ayabanerve:matrix.org >__ I want to use the logarithmic derivative to efficiently prove sign-agnostic (x-coordinate only) knowledge of discrete log.     

> __< k​ayabanerve:matrix.org >__ I also want to use the derivative to prove a series of bits is the discrete log.     

> __< k​ayabanerve:matrix.org >__ They do comment on correctness/soundness, albeit potentially briefly.     

> __< k​ayabanerve:matrix.org >__ 3.2.1     

> __< k​ayabanerve:matrix.org >__ 3.3.1, 4.2     

> __< a​aron:cypherstack.com >__ The authors only vaguely refer to the idea of soundness     

> __< a​aron:cypherstack.com >__ TBH I am not interested in trying to extrapolate the intent of the authors     

> __< k​ayabanerve:matrix.org >__ It's legitimately largely commentary on the algebraic nature of curves with a posited usage.     

> __< a​aron:cypherstack.com >__ That is not a good use of time     

> __< a​aron:cypherstack.com >__ If the authors intend to convince readers of formal properties, they need to state those properties and provide proofs     

> __< a​aron:cypherstack.com >__ Sorry to be so blunt :/     

> __< k​ayabanerve:matrix.org >__ rbrunner: The proof itself would largely carry. The circuit would change. The integration would move to being integrated with Seraphis.     

> __< k​ayabanerve:matrix.org >__ But the proof and techniques and review and audits carry.     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: To be fair, I wouldn't ask you to certify the paper. I'd ask you to do the second half.     

> __< a​aron:cypherstack.com >__ Say more about this?     

> __< k​ayabanerve:matrix.org >__ That paper is on techniques and a posited use case. We'd need to design a R1CS gadget building on those techniques to offer a sound proof. That's what would be proven.     

> __< a​aron:cypherstack.com >__ Designing a security model, formalizing the approach, and proving it secure is quite the ask     

> __< a​aron:cypherstack.com >__ Much more than "review this preprint" :D     

> __< k​ayabanerve:matrix.org >__ Also, divisors predate Eagen's writings. They apparently have extensive history when you read into them.     

> __< d​iego:cypherstack.com >__ Things are getting a bit complicated and if they get even more so it really will take resources from something like Seraphis, no?     

> __< a​aron:cypherstack.com >__ Sure, but that's much different than what I see here     

> __< k​ayabanerve:matrix.org >__ Regardless, if they don't work out, we'd fallback to incomplete addition in circuit. It'd be fine.     

> __< rbrunner >__ The idea is to move quickly with this. Seems to me some proof / review work needs some parallelization, i.e. more capacity than simply Aaron's     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: You have to understand the techniques posited and grok the idea of usage to take that next step ;)     

> __< a​aron:cypherstack.com >__ I just want to make clear that "review this preprint" is not the apparent ask here     

> __< r​ucknium:monero.social >__ Incomplete addition in circuit = how much worse performance in verification time and tx size?     

> __< k​ayabanerve:matrix.org >__ You're welcome to bow out and/or sign up for review of the fully posited gadget (again, I'm meeting another group in 2h about this)     

> __< k​ayabanerve:matrix.org >__ I don't want to push Aaron Feickert: out. I'd explicitly next ask them to work on proving GBPs and suggest a distinct group for the divisor work currently posited.     

> __< jberman >__ What I figure could remain pre and post-Seraphis with FCMPs on the integration side: the flow of adding/removing to/from the tree in lmdb (even though the elements in the tree will be different), setting up the FFI to the Rust code for prove and verify, the logical flow of verify in the daemon     

> __< a​aron:cypherstack.com >__ kayabanerve: I don't fully grok what the ask for divisors is     

> __< k​ayabanerve:matrix.org >__ Rucknium: I believe 2x in time, but I'd have to redo the layout and check. No notable diff in size.     

> __< d​iego:cypherstack.com >__ We decline to do the divisor preprint at this time.     

> __< r​ucknium:monero.social >__ "I'd explicitly next ask them to work on proving GBPs and suggest a distinct group for the divisor work currently posited." That sounds good to me. If we can get more people working on the formal security proofs, great.     

> __< k​ayabanerve:matrix.org >__ rbrunner: Yes, my entire proposal is around multiple parallelized tracks.     

> __< jberman >__ The biggest change for post-Seraphis integration is probably switching curves and all code surrounding that. My initial estimate seems something like 30-50% of the work would be done     

> __< rbrunner >__ On the coding side, right?     

> __< k​ayabanerve:matrix.org >__ jberman: And a lot of the cryptography ;)     

> __< jberman >__ of course, was talking strictly about integration :)     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: , though this was a bit brief.     

> __< rbrunner >__ Doesn't sound too bad.     

> __< k​ayabanerve:matrix.org >__ @jberman If this goes well, it may justify not moving curves. It also may further justify moving.     

> __< rbrunner >__ Together with the estimate that most of the "theory" side will carry over almost effortlessly     

> __< k​ayabanerve:matrix.org >__ rbrunner: Parallelization of coding, review, and auditing.     

> __< rbrunner >__ Hope you don't rush headlong into a burnout with this ...     

> __< rbrunner >__ If all goes well probably have the time of your life :)     

> __< k​ayabanerve:matrix.org >__ We could near immediately start formal review of parts, formal proofs of parts, and audits of parts of the code, while the next steps off those start development so they're ready for review when the prior wave finishes review.     

> __< a​aron:cypherstack.com >__ Stepping back, given this discussion, what would be the desired proposals (if any) from Cypher Stack going forward?     

> __< k​ayabanerve:matrix.org >__ GBP proofs.     

> __< a​aron:cypherstack.com >__ There's no sense having a Seraphis review proposal open if this isn't the desired timeline     

> __< a​aron:cypherstack.com >__ Even with the understanding that this could yield effectively no deliverable?     

> __< k​ayabanerve:matrix.org >__ That's my immediate comment/request/priority/urge from this community.     

> __< r​ucknium:monero.social >__ Suggestion: Create a CCS proposal to put Cypher Stack "on retainer" for `k` months. Have a flexible plan of the menu of things they would be willing and able to do. Start with the plan and then set tasks based on intermediate outcomes of the research. Create a MRL committee to make the decisions about what the task flow should be as results come in.     

> __< k​ayabanerve:matrix.org >__ (as in, it needs the community to agree, and I urge the community to agree)     

> __< k​ayabanerve:matrix.org >__ Literally all of life ;)     

> __< dEBRUYNE >__ The Seraphis proposal can either be rewritten for GBP proofs or temporarily put on hold whilst a new one is put out     

> __< k​ayabanerve:matrix.org >__ So yes     

> __< a​aron:cypherstack.com >__ Rucknium: I'm obviously biased on this topic, but how would tasks be defined and chosen?     

> __< rbrunner >__ I know that people claim differently, but I am pretty sure that Seraphis won't progress much until we hardfork to this new thing. So now review now does not seem to be a big loss.     

> __< a​aron:cypherstack.com >__ I ask because such a committee doesn't currently exist :D     

> __< k​ayabanerve:matrix.org >__ Other suggestion: A CCS proposal for FCMPs pre-Seraphis which covers its needs, with a well-documented set of intents and allowances.     

> __< dEBRUYNE >__ rucknium: If such a proposal would be posted, it would have to at least include some examples of what Cypherstack is going to work on     

> __< d​iego:cypherstack.com >__ I'm sorry to try to streamline things in this meeting, but I'd like to circle back to Cypher Stack's immediate upcoming work.     

> __< r​ucknium:monero.social >__ Choose who will be on the committee. This structure avoids having multiple CCSes and the delay that involves.     

> __< k​ayabanerve:matrix.org >__ From developer(s), to CS (if not independently CCS'd), to other groups.     

> __< d​iego:cypherstack.com >__ If the answer is "we don't really have an answer yet, that's fine. That's the answer."     

> __< dEBRUYNE >__ <k​ayabanerve:matrix.org> Other suggestion: A CCS proposal for FCMPs pre-Seraphis which covers its needs, with a well-documented set of intents and allowances. <= Think this would actually be the best, as it will be specific and to the point     

> __< r​ucknium:monero.social >__ Aaron Feickert posted a possible list of things to work on: https://github.com/monero-project/meta/issues/986#issuecomment-2030089046     

> __< k​ayabanerve:matrix.org >__ dEBRUYNE: Seraphis isn't inherently changed by this since it's a composition. We'd prove FCMPs meet the requirements of the composition.     

> __< k​ayabanerve:matrix.org >__ I'm not against a CS retainer, starting with GBPs, and a FCMP slush.     

> __< k​ayabanerve:matrix.org >__ That sounds optimal to me if we can agree on it, with further tasks defined however/whenever.     

> __< dEBRUYNE >__ kayabanerve: Do you prefer a retainer over the specified proposal you mentioned before?     

> __< k​ayabanerve:matrix.org >__ (further tasks re: CS)     

> __< r​ucknium:monero.social >__ AFAIK, no one is speaking up for a Seraphis paper review. If no one wants that in the near term, then that's fine.     

> __< k​ayabanerve:matrix.org >__ The FCMPs side is already well defined     

> __< k​ayabanerve:matrix.org >__ Rucknium: I'll explicitly chime in I don't have thoughts there :p     

> __< k​ayabanerve:matrix.org >__ dEBRUYNE: I don't mind if CS has a retainer, is contracted for GBPs in a CCS, or is contracted for GBPs under the FCMPs slush CCS. It's up to y'all.     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: would appreciate the retainer and I'm sure we have enough work for them, so I'd say retain CS.     

> __< rbrunner >__ Still a bit surprising for me that nobody present here seems to have the slightest reservations to enter this adventure ...     

> __< k​ayabanerve:matrix.org >__ That is distinct to any FCMP slush AFAIC.     

> __< dEBRUYNE >__ From a community perspective, I think this will have best chances of getting funding relatively fast -> A CCS proposal for FCMPs pre-Seraphis which covers its needs, with a well-documented set of intents and allowances.     

> __< k​ayabanerve:matrix.org >__ *AFAIAC     

> __< dEBRUYNE >__ It can even be split up in 2 parts     

> __< r​ucknium:monero.social >__ IMHO retainer is a better idea to reduce delays and maximize time MRL has from CS     

> __< k​ayabanerve:matrix.org >__ rbrunner: I did make a good proposal ;p     

> __< rbrunner >__ Yeah, have to give you that     

> __< dEBRUYNE >__ rbrunner: I think that's why review is sought, to make everyone more aware of potential reservations     

> __< k​ayabanerve:matrix.org >__ Except if the FCMP slush is funded and the first step, GBP review, is held up due it to being on a distinct CCS.     

> __< k​ayabanerve:matrix.org >__ GBPs under FCMPs, separate CCS for retainer after?     

> __< k​ayabanerve:matrix.org >__ *GBP proving     

> __< k​ayabanerve:matrix.org >__ I don't like this :C it'd just solve that concern.     

> __< r​ucknium:monero.social >__ r​brunner: I have reservations. Maybe it hasn't been clear from what I've said. My main reservation is that MRL looks at new shiny objects and doesn't implement anything. Triptych was developed years ago, but Seraphis looked better for multisig IIRC. Now we are on FCMP.     

> __< rbrunner >__ dEBRUYNE: I meant mostly reservations from a "project management" point of view. E.g. "switch horses in the middle of the race" lines of reasoning.     

> __< tobtoht_ >__ I have some preliminary build system work for FCMPs here: https://github.com/tobtoht/monero/pull/2     

> __< tobtoht_ >__ I'm still concerned about the relatively large increase in our software supply chain attack surface (introducing 81 new dependencies from various authors + the rust toolchain) and would prefer a low(er) dependency solution or aggressive vendoring where possible. Also considering the extra maintenance burden that that number of deps would add.     

> __< k​ayabanerve:matrix.org >__ FCMPs are almost like a half Seraphis if it makes you feel better Rucknium, and the whole point is actually getting it done.     

> __< k​ayabanerve:matrix.org >__ Membership + Ownership proof separation     

> __< k​ayabanerve:matrix.org >__ TX chaining, if we so choose.     

> __< k​ayabanerve:matrix.org >__ Great multisig.     

> __< r​ucknium:monero.social >__ There is some type of space travel paradox analogy: It never makes sense to launch a ship to another star system because tech will always improve to outpace the ship you sent.     

> __< rbrunner >__ "MRL looks at new shiny objects and doesn't implement anything" smile     

> __< k​ayabanerve:matrix.org >__ tobtoht: I do want to/plan to bring those down.     

> __< k​ayabanerve:matrix.org >__ We'd audit and lock to specific git commits, if we didn't vendor our own tree entirely.     

> __< r​ucknium:monero.social >__ Do selsta and luigi want Rust in monerod? (And other protocol developers?)     

> __< rbrunner >__ Anyway, that's the normal garden variety IT project. It will at least twice as long as estimed now. Will probably fly nevertheless.     

> __< r​ucknium:monero.social >__ And the Core Team     

> __< k​ayabanerve:matrix.org >__ I have the confidence to make the CCS and move forward on my end. Diego Salazar: CS can be included for the GBP proving under that proposal, if you wish in the name of expediency/expected likelihood, or you can independently seek a retainer for whatever tasks (presumably including GBPs at son point ;) ). I'd leave it to you     

> __< k​ayabanerve:matrix.org >__ rbrunner: one year *is* the twice as long.     

> __< rbrunner >__ Realistically, Rust is probably unavoidable in the middle to long term     

> __< rbrunner >__ Even if we give it a hard pass for now     

> __< rbrunner >__ I am afraid we will have to learn to manage the additional complexity that this will bring     

> __< k​ayabanerve:matrix.org >__ I'm so declarative in my prior message as I'm unsure we'll get stronger commentary this meeting and want to hand the terms of rehrar's engagement to rehrar's choice, in what and how it's funded.     

> __< a​rticmine:monero.social >__ I am going to defer to the consensus in MRL and Dev on this FCMP proposal. I am only speaking for myself here not the whole of corr     

> __< k​ayabanerve:matrix.org >__ rbrunner: I'm happy we will have to learn :D     

> __< k​ayabanerve:matrix.org >__ Rust :D     

> __< d​iego:cypherstack.com >__ My humblest apologies everyone.  My matrix client is acting up and sending and receiving is being finicky.     

> __< a​rticmine:monero.social >__ Core     

> __< k​ayabanerve:matrix.org >__ I'm fine saying I don't speak for core, nor the community, and am moving forward out of my personal view giving me personally sufficiency confidence.     

> __< c​haser:monero.social >__ I can't speak re the implementation route, FCMP+RingCT seems like best of all worlds: fends off black marbles on the mid term, buys time for Seraphis development, but its inefficiencies relative to FCMP+Seraphis incentivize the eventual switch to Seraphis.     

> __< k​ayabanerve:matrix.org >__ *sufficient     

> __< rbrunner >__ We had binaryFate saying hello at the start of the meeting? Any comment from them right now?     

> __< k​ayabanerve:matrix.org >__ My next steps are a CCS and some meetings with third parties, including possibly Diego Salazar:  (who should check monerologs to view messages)     

> __< d​iego:cypherstack.com >__ So all of this to say... I will be opening an FCMP proposal.     

> __< a​aron:cypherstack.com >__ To entail what exactly?     

> __< a​aron:cypherstack.com >__ Which tasks?     

> __< a​aron:cypherstack.com >__ There are many floating around here     

> __< r​ucknium:monero.social >__ I am fine with a CCS that only does GBP security proofs. Or a CCS that does that plus a possible menu of FCMP (if GBP sec proof is obtain) or Seraphis review. I don't really like the idea of a large FCMP-only CCS if the GBP security proofs cannot be established because you may they be wasting time on a protocol that cannot work.     

> __< rbrunner >__ Let's hope no new, even shinier object comes around the corner for quite a while :)     

> __< k​ayabanerve:matrix.org >__ My desired discussion is over proving GBPs. AFAICT, Diego Salazar: can agree to handle that first or agree to handle another task first if a distinct request comes in.     

> __< r​ucknium:monero.social >__ you may then be wasting time*     

> __< k​ayabanerve:matrix.org >__ Literally their company :p     

> __< k​ayabanerve:matrix.org >__ Rucknium: We can fallback from GBPs. I said this earlier     

> __< r​ucknium:monero.social >__ What's the falback?     

> __< a​aron:cypherstack.com >__ ^     

> __< k​ayabanerve:matrix.org >__ rbrunner: FCMPs can be made faster. Beyond that, the only improvements are forward secrecy (Seraphis being the shiny thing there)     

> __< k​ayabanerve:matrix.org >__ BPs, which would still be sufficiently performant with divisors from my estimates. I wouldn't love that though :///     

> __< o​ne-horse-wagon:monero.social >__ Who is going to write the code for what is being proposed here?     

> __< k​ayabanerve:matrix.org >__ And would need to double check the exact flow there.     

> __< k​ayabanerve:matrix.org >__ I and jberman: have commented willingness to step up.     

> __< r​ucknium:monero.social >__ So to get enough performance, we would need GBP to be secure or Eagan's divisor technique to be secure. If both cannot be proven secure, then FCMP must have another cryptographic protocol?     

> __< k​ayabanerve:matrix.org >__ I believe it's only if both fail the effort ends at this time (/ requires a new underlying proof).     

> __< k​ayabanerve:matrix.org >__ If we wait for GBPs to finalize, I'd estimate a 3 month delay.     

> __< r​ucknium:monero.social >__ And Aaron Feickert  and Diego Salazar  said that they will not look at Eagan's divisor. We need someone else to look at that.     

> __< k​ayabanerve:matrix.org >__ I'd rather make the assumption there than continue rings for so much longer. I was fine with Seraphis + FCMPs @ 1.5y. I don't want to hear FCMPs, no Seraphis, is that long :///     

> __< r​ucknium:monero.social >__ We don't need GBP to be proven secure before any other work is done. But if the security proof attempt does not succeed, consider resource allocation toward FCMP. May not make sense if sec proof attempt does not succeed.     

> __< k​ayabanerve:matrix.org >__ I'm tired, frustrated, and just want to move forward, even if that means some financial risk is accrued.     

> __< k​ayabanerve:matrix.org >__ I have a meeting in 2h re: divisors.     

> __< r​ucknium:monero.social >__ As I've said before, my opinion is "prove it".     

> __< binaryFate >__ <rbrunner> We had binaryFate saying hello at the start of the meeting? Any comment from them right now? <--- no specific comment from me. Just following meeting to better grasp various options ahead.     

> __< k​ayabanerve:matrix.org >__ That's what the CCS would do.     

> __< r​ucknium:monero.social >__ But I'm not a cryptographer. But I do know math in other areas. Those areas need proofs too :)     

> __< a​rticmine:monero.social >__ The fallback becomes CLSAG with ring 64 followed by FCMP plus Seraphis     

> __< k​ayabanerve:matrix.org >__ To be clear, do we have new comments or solely debate about a CCS I have yet to put forth? Because the latter will presumably have independent review as all CCSs do.     

> __< s​gp_:monero.social >__ Personally, I don't see a reason to delay prematurely. Some calculated financial risk is acceptable for an accelerated timeline     

> __< rbrunner >__ If the whole FCMP for RingCT venture fails, so some kind of worst case reasoning?     

> __< k​ayabanerve:matrix.org >__ I'd be happy to later discuss the CCS and breaking it down if we now cover research topics.     

> __< s​gp_:monero.social >__ If donors don't want the risk, then we can reevaluate. But if the funding is there, it seems worthwhile to try a faster option     

> __< rbrunner >__ This will get funded in no time, I am sure.     

> __< janowitz >__ I'm pretty sure, it will be funded even with the remaining risks.     

> __< k​ayabanerve:matrix.org >__ @ArticMine I disagree ring 64 is a valid fallback but also don't want to have that disagreement talked through when we're well over the hour :p     

> __< r​ucknium:monero.social >__ sgp_: AFAIK the bottleneck isn't funds. It's Aaron Feickert 's time. Cannot work on FCMP and Seraphis at the same time.     

> __< k​ayabanerve:matrix.org >__ I'm only asking Aaron prove GBPs now, as reusable.     

> __< s​yntheticbird:monero.social >__ I agree with sgp reasoning. I think the community will likely see this venture as a welcoming and worth risking improvement.     

> __< r​ucknium:monero.social >__ Sounds great to me     

> __< jberman >__ I personally think FCMPs are critically important for Monero and are reasonable to prioritize     

> __< jberman >__ Now that we have a potential way to do it before Seraphis and without requiring an address change (Seraphis I'd personally estimate is 3y out from deployment with FCMPs), I think it's reasonable to prioritize FCMPs today     

> __< jberman >__ As such I'm for CS next task advancing the needle toward FCMP, and holding the Seraphis proposal until later     

> __< r​ucknium:monero.social >__ AFAIK I don't see any disagreement with a CCS proposal for Cypher Stack to only try to write GBP security proofs. Except possibly rbrunner. rbrunner, any comments?     

> __< rbrunner >__ It's a bit funny, if not that important of course, that in the Monero subreddit the main argument against Zcash is "unproved moon math" :)     

> __< rbrunner >__ They will have to find something new after we enter this adventure     

> __< k​ayabanerve:matrix.org >__ I've been against that label for a while :/     

> __< rbrunner >__ Lol     

> __< janowitz >__ @rbrunner did Zcash have proper external audits?     

> __< rbrunner >__ No idea.     

> __< r​ucknium:monero.social >__ rbrunner: That's why reviewed security proofs are so important. Zcash had an exploitable flaw in their cryptography that did not have a security proof. There was a security proof for a protocol that was very similar, but not exactly the same as, the Zcash protocol.     

> __< r​ucknium:monero.social >__ Zcash had a detailed writeup on what went wrong     

> __< rbrunner >__ I think we will be able to stay course and really insist on proper proofs, as a community     

> __< a​rticmine:monero.social >__ Fair enough. Ring 64 is the maximum the scaling is designed for and matches the estimated FCMP tx weight. There are lower ring options.      

> __< a​rticmine:monero.social >__ This being said the proper time for this discussion is IF the pre Seraphis FCMP fails. Otherwise it is moot.     

> __< rbrunner >__ It might take longer than now estimated, but still     

> __< r​ucknium:monero.social >__ https://electriccoin.co/blog/zcash-counterfeiting-vulnerability-successfully-remediated     

> __< k​ayabanerve:matrix.org >__ Can confirm proofs are important.     

> __< rbrunner >__ We we plan here is probably bleeding edge alright, but not reckless.     

> __< k​ayabanerve:matrix.org >__ Rucknium: I'm not sure it was unproven vs the proofs were broken.     

> __< r​ucknium:monero.social >__ "This being said the proper time for this discussion is IF the pre Seraphis FCMP fails." Shouldn't discussion of high-ring-size CLSAG still happen in parallel so that there is preparation instead of delay of FCMP does not succeed in its timeline?     

> __< r​ucknium:monero.social >__ kayabanerve: I am sure given my memory of Zcash's writeup     

> __< r​ucknium:monero.social >__ "Importantly, the [BCTV14] construction did not have a dedicated security proof, as noted in [Parno15], and relied mainly on the [PGHR13] security proof and the similarity between the two schemes. The Zcash Company team did attempt to write a security proof in [BGG17], but it did not uncover this vulnerability. Zcash has since upgraded to a new proving system [Groth16] which has m<clipped message     

> __< r​ucknium:monero.social >__ ultiple independent proofs and significantly better analysis."     

> __< k​ayabanerve:matrix.org >__ The 2017 protocol was proven in 2017.     

> __< k​ayabanerve:matrix.org >__ The protocol had a soundness vulnerability per the write up. That doesn't mean they didn't write proofs.     

> __< k​ayabanerve:matrix.org >__ Ah, sorry, the 14 protocol was unproven.     

> __< rbrunner >__ Whatever it was, we probably won't go down the same route     

> __< rbrunner >__ Hopefully     

> __< r​ucknium:monero.social >__ AFAIK, we have reached the goal of this meeting: kayabanerve  will draft a CCS for CypherStack to attempt to write a security proof for Generalized Bulletproofs.     

> __< s​gp_:monero.social >__ The larger point about getting the proofs and the reviews stands in any case     

> __< r​ucknium:monero.social >__ Do we agree we have reached the goal?     

> __< k​ayabanerve:matrix.org >__ Explicit timeline and steps for review, proofs, and auditing included :)     

> __< a​aron:cypherstack.com >__ So there will _not_ be a current review of the (general) Seraphis paper?     

> __< r​ucknium:monero.social >__ Aaron Feickert: I do not see much support for that right now. It will probably come later. Sorry about the switch.     

> __< k​ayabanerve:matrix.org >__ No. I'll make a CCS for FCMPs work. Diego Salazar: may or may not join or may or may not do their own CCS (with retainer?).     

> __< r​ucknium:monero.social >__ What do you mean by "may or may not join"?     

> __< a​aron:cypherstack.com >__ I hate to be too annoying, but can you give a few sentences on what "FCMPs work" will entail?     

> __< a​aron:cypherstack.com >__ There's a lot floating around about this     

> __< a​aron:cypherstack.com >__ and I do not want anything left vague     

> __< k​ayabanerve:matrix.org >__ I will not make a CCS on behalf of Diego nor force their participation.     

> __< k​ayabanerve:matrix.org >__ If they want to be part of my CCS, they may. Else, they won't be.     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: Read my gist.     

> __< k​ayabanerve:matrix.org >__ It's an entire slew of work.     

> __< k​ayabanerve:matrix.org >__ CS would be specifically involved re: proving GBPs.     

> __< r​ucknium:monero.social >__ This is different from what I understood, which is the CCS is _for_ Cypher Stack. Now it is not?     

> __< a​aron:cypherstack.com >__ Right, it describes a fair amount. But I want to confirm what CS's scope is     

> __< k​ayabanerve:matrix.org >__ My CCS was always my CCS.     

> __< a​aron:cypherstack.com >__ "The gist" is not sufficient, sorry     

> __< k​ayabanerve:matrix.org >__ That doesn't mean only I'd be paid. It means I'd write and manage it for the work in the gist.     

> __< a​aron:cypherstack.com >__ If the scope is only "attempt to develop security proofs for the GBP protocol" then excellent, that's suitable     

> __< r​ucknium:monero.social >__ So you would be director of the FCMP project and CS could be a subcontractor?     

> __< rbrunner >__ kayabanerve, "my CCS" is your CCS to get paid for *your* work on FCMPs, right?     

> __< k​ayabanerve:matrix.org >__ No. It's my CCS to manage the FCMPs effort.     

> __< s​gp_:monero.social >__ I think we can leave it to these two groups to spurt out their specific scopes outside of the meeting (imo)     

> __< s​gp_:monero.social >__ *sort     

> __< rbrunner >__ Agree :)     

> __< k​ayabanerve:matrix.org >__ I prior stated I plan to make a CCS comprehensive to not only my work, yet ideally to also create a slush for future funding re: FCMPs.     

> __< rbrunner >__ They will find common ground, after some confusion, I am sure     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: would be welcome to be one of the first line items in that CCS. I will not speak on their behalf.     

> __< rbrunner >__ Will take some time until the dust settles     

> __< k​ayabanerve:matrix.org >__ https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86#steps-forward     

> __< k​ayabanerve:matrix.org >__ Sorry. https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86#steps-and-timeline     

> __< k​ayabanerve:matrix.org >__ Section prior to the one I first linked.     

> __< rbrunner >__ I think it's time to let this poor overworked meeting come to an end. Tomorrow is another day :)     

> __< k​ayabanerve:matrix.org >__ There is an entire slew of proposed work I'd like to create a CCS comprehensive to, so I don't re-request funding every month with new explanations and we don't get burn out from "yet another FCMP proposal".     

> __< a​aron:cypherstack.com >__ I am uncertain what the current ask from CS is at this point :/     

> __< k​ayabanerve:matrix.org >__ While I don't claim it will be perfectly comprehensive, I believe I can create a well-reasoned and agreeable CCS.     

> __< rbrunner >__ And heaven forbid retroactively     

> __< k​ayabanerve:matrix.org >__ Please delay review of my CCS until I actually write and submit it. There's no explicit need to review and debate a document I haven't even written yet.     

> __< k​ayabanerve:matrix.org >__ Rucknium: I don't know if I'd be the director and CS would be a subcontractor. I will not speak for Diego.     

> __< k​ayabanerve:matrix.org >__ I would like to explicitly request CS do the GBPs proving, as I have said many times. I will offer to Diego Salazar to be included under my CCS. I cannot confirm they're willing to be present under it.     

> __< k​ayabanerve:matrix.org >__ If they do their own CCS/retainer, that is up to them. That just means my CCS has one less responsibility.     

> __< r​ucknium:monero.social >__ Yes, I think we can end the meeting. kayabanerve , Aaron Feickert , Diego Salazar  you can discuss the details.     

> __< k​ayabanerve:matrix.org >__ 👍     

> __< tobtoht_ >__ kayabanerve: Ok, plans to reduce deps sounds good. "We'd audit and lock to specific git commits" <- Yes, prerequisite for reproducible builds. The thing is we can't realistically pin a commit forever. If we'd ever need to bump our Rust toolchain (e.g. to add platform support), I'd expect a number of deps to not build (deprecations, breaking     

> __< tobtoht_ >__ changes, whatever), so we'd have to update those along with their transitive dependencies, which means lots of external code to review in different places.     

> __< c​haser:monero.social >__ if large-ring CLSAG is interesting at all in any aspect, I think it's as a privacy hedge *before* FCMP, not instead of it.     

> __< a​rticmine:monero.social >__ It can. I just do not want to create yet another distraction. The  "new shiny thing" is a vintage  restoration.  It is also dependent on the development of code for parallel processing on CPUs and the future state of technology.     

> __< p​y.verse:matrix.org >__ I agree with that one     

> __< a​aron:cypherstack.com >__ As a hypothetical... suppose we are not able to prove GBP secure. What would be the consequences?     

> __< a​aron:cypherstack.com >__ It's possible to do Seraphis without them, but this is very suboptimal     

> __< a​aron:cypherstack.com >__ (without them == without FCMPs, which require GBP for efficiency)     

> __< k​ayabanerve:matrix.org >__ Assuming you mean FCMPs. We'd become reliant on a new proof (as in "of security", or as in protocol) or effectively require divisors to be performant.     

> __< k​ayabanerve:matrix.org >__ And that'd still have notably degraded performance :/ If divisors are optimal though, I believe it'd still work out.     

> __< s​gp_:monero.social >__ is the correct read of this: We would still consider other less-efficient FCMP options first     

> __< a​aron:cypherstack.com >__ Keep in mind that if CS were unable to prove GBP secure, it is entirely possible that someone else could produce a convincing proof     

> __< a​aron:cypherstack.com >__ (Though I'm equally sure that someone else could produce a non-convincing proof!)     

> __< k​ayabanerve:matrix.org >__ Hence why I said we'd need a proof, potentially "of security" and not as in protocol ;)     

> __< s​gp_:monero.social >__ hey its me, I can provide an unconvincing proof!     

> __< a​aron:cypherstack.com >__ Our failure mode would _not_ be "a proof is not possible"     

> __< k​ayabanerve:matrix.org >__ Because yes, exactly that. One person's lack of doing so in a timely manner doesn't preclude it ever happening.     

> __< k​ayabanerve:matrix.org >__ sgp_: Yeah, we'd need failures at multiple layers for this effort to go into stasis.     

> __< a​aron:cypherstack.com >__ Also keep in mind that Seraphis does work with non-FCMP techniques (like Groth/Bootle proofs)     

> __< a​aron:cypherstack.com >__ albeit with footguns attached...     

> __< k​ayabanerve:matrix.org >__ Oh, Seraphis would not go into statis. It'd just lose FCMPs.     

> __< k​ayabanerve:matrix.org >__ (as you note)     

> __< k​ayabanerve:matrix.org >__ *stasis     

> __< s​gp_:monero.social >__ Thanks everyone for the discussion today     

> __< k​ayabanerve:matrix.org >__ Thanks y'all. Sorry for any contention at the end     

> __< a​rticmine:monero.social >__ Then we are looking at large ring sizes under Seraphis     

> __< a​rticmine:monero.social >__ Which may not require an increase in the minimum penalty free zone.     

> __< a​aron:cypherstack.com >__ I must say that I don't like the idea of CS not being able to produce a deliverable :/     

> __< a​aron:cypherstack.com >__ Given that we work hard to provide good value     

> __< d​iego:cypherstack.com >__ Alright finally home     

> __< d​iego:cypherstack.com >__ My mobile element was really crapping out so things have been spotty, my apologies     

> __< a​aron:cypherstack.com >__ And I say this with full knowledge that research does not always yield desired results!     

> __< a​aron:cypherstack.com >__ matrix gonna matrix     

> __< c​haser:monero.social >__ thank you all, and special thanks to Rucknium for the marbles paper and Kayaba for the new FCMP draft.     

> __< a​rticmine:monero.social >__ Thank you all.     

> __< o​ne-horse-wagon:monero.social >__ Aaron Feickert: Research is expensive and can be fruitless but you have to do it to get ahead.     

> __< d​iego:cypherstack.com >__ We at Cypher Stack would prefer to do our own proposal for this.     

> __< d​iego:cypherstack.com >__ I'll draft one up for GBP since that seems to be the direction things are going.     

> __< a​aron:cypherstack.com >__ Diego Salazar: definitely be super-duper clear about the nontrivial failure risk     

> __< d​iego:cypherstack.com >__ Although my own personal opinion is that the Seraphis general review would need to get done one way or another, and that it would get the community the most bang for their buck at present.     

> __< d​iego:cypherstack.com >__ If MRL wants to discuss a retainer-type scenario for CS, we would be open to this. But we would need a lot of things to be crystal clear around how this would happen.     

> __< dEBRUYNE >__ <k​ayabanerve:matrix.org> While I don't claim it will be perfectly comprehensive, I believe I can create a well-reasoned and agreeable CCS. <= Looking forward to it!     

> __< dEBRUYNE >__ kayabanerve: Just to confirm, FMCP doesn't require some sort of trusted set up right?     

> __< r​ucknium:monero.social >__ Diego Salazar: I would support a retainer, but I didn't see much support for this during the meeting. I don't want to go against the general sentiment as meeting chairperson.     

> __< d​iego:cypherstack.com >__ I think it just needs to be a line item unto itself Rucknium     

> __< r​ucknium:monero.social >__ By the way, meeting chairperson can be taken by someone else if they want or it can rotate. It doesn't have much formal role anyway.     

> __< d​iego:cypherstack.com >__ with a million thoughts swirling around about a thousand things, a lot falls through the cracks     

> __< d​iego:cypherstack.com >__ We're happy to do one proposal at a time, however.   

# Action History
- Created by: Rucknium | 2024-04-01T13:44:15+00:00
- Closed at: 2024-04-10T19:37:09+00:00
