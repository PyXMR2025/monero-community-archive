---
title: Monero Research Lab Meeting - Wed 23 July 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1244
author: Rucknium
assignees: []
labels: []
created_at: '2025-07-22T21:33:15+00:00'
updated_at: '2025-07-31T20:08:41+00:00'
type: issue
status: closed
closed_at: '2025-07-31T20:08:41+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3.  [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

5. [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).

6. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

7. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

8. Rucknium's research agenda.

9.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

10. [Proposal and spec for Proof-of-Work Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

11. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1239 

# Discussion History
## Rucknium | 2025-07-25T20:46:48+00:00
Logs

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Stay hydrated. Will probably be a long meeting.     

> __< s​yntheticbird:monero.social >__ I propose that the "1. Greetings" get replaced by "1. Water check"     

> __< b​en_sepanski:matrix.org >__ Hi all! I'm Ben Sepanski, CSO from Veridise. In light of the upcoming discussion, we wanted to share Veridise's perspective on FCMP++ and SLVer bullet.      

> __< b​en_sepanski:matrix.org >__ Since SLVer Bullet was updated based on the attached concerns (after we shared them directly) and announced before we heard back from Cypher Stack, we wanted to go ahead and share them publicly in case they are found useful by the Monero community or any future reviewers planning to create/analyze security proofs for SLVer Bullet. While we do not intend to perform further review, <clipped messag     

> __< b​en_sepanski:matrix.org >__ based on a brief pass we believe that neither of the two most serious issues raised were addressed by the update:     

> __< b​en_sepanski:matrix.org >__ * The use of explicit curve addition formulas in the derivation of the verification equations results in relations that do not hold at the function field level (and are not equivalent to the expressions proposed by Eagen as claimed). See, for example, the SAGE script above, in which the original equations match the expected expression computed using SAGE's built-in functions, but <clipped messag     

> __< b​en_sepanski:matrix.org >__ SLVer bullet does not. As mentioned, we do not have capacity at this point to perform further reviews of SLVer Bullet, but the underlying issue of applying derivatives to an expression which holds over only a subset of the curve is still present     

> __< b​en_sepanski:matrix.org >__ * The soundness argument contains a flaw in the use of Schwartz-Zippel, which also has not been fixed. SLVer Bullet’s soundness argument (Theorem 3.3.7) relies upon "Sage code 2 (see [Sla25]) giving statistical evidence of that the two cases result in the same distribution of roots, enabling our application of Schwartz-Zippel.” This does not constitute a proof and cannot provi<clipped messag     

> __< b​en_sepanski:matrix.org >__ de the basis for soundness of a cryptographic argument     

> __< b​en_sepanski:matrix.org >__ To avoid multiple rounds of back-and-forth, we plan to continue work along the original line of reasoning based on the ideas of Eagen and implementation by Kayaba, and will share here if we have more updates     

> __< b​en_sepanski:matrix.org >__ As mentioned in the first response, we reiterate our commitment to be actively involved in any constructive endeavour to ensure the correctness of the proofs, the clarity and precision of its exposition and the security of the scheme based on it, and hope this is helpful for any future decision-making. As always, we remain open to any further questions or concerns!     

> __< b​en_sepanski:matrix.org >__ log_deriv.ipynb     

> __< b​en_sepanski:matrix.org >__ https://matrix.monero.social/_matrix/media/v1/download/matrix.org/mrIQjbCrDTXpPLilgKjXsdwb     

> __< b​en_sepanski:matrix.org >__ https://matrix.monero.social/_matrix/media/v1/download/matrix.org/ilabQZKNKVDxZrXZAbQvWROw     

> __< b​en_sepanski:matrix.org >__ https://matrix.monero.social/_matrix/media/v1/download/matrix.org/gNUdNJDsKZsnxOmnriExRNLj     

> __< r​ucknium:monero.social >__ ben_sepanski: Welcome! Thank you for sharing.     

> __< f​reeman:cypherstack.com >__ For the first point, our new numerical values may be found on page 16 and 23, so the provided Sage code is no longer relevant, as it applies to the prior version. For the second, the Schwartz-Zippel issue HAS been addressed, on page 13. Our code was merely intended to provide, as we state, *statistical* numerical evidence, so was never intended to constitute a proof. It seems as i<clipped messag     

> __< f​reeman:cypherstack.com >__ f there are misunderstandings between what we intended and what you have read (no claims as to who is "at fault" here, but we will clarify these issues in future versions). Veridise, we do appreciate your review, and thank you for helping to make Monero better, which is ultimately what we all want! ❤     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1244     

> __< r​ucknium:monero.social >__ 1) Greetings (water check).     

> __< a​rticmine:monero.social >__ Hi     

> __< s​gp_:monero.social >__ hello     

> __< g​ingeropolous:monero.social >__ glass half full     

> __< v​tnerd:monero.social >__ ji     

> __< b​randon:cypherstack.com >__ hola     

> __< rbrunner >__ Hello! Are there leaks?     

> __< v​tnerd:monero.social >__ *hi     

> __< s​packle:monero.social >__ hi     

> __< s​yntheticbird:monero.social >__ hello (hydration check)     

> __< j​effro256:monero.social >__ Howdy     

> __< d​iego:cypherstack.com >__ hi     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< j​berman:monero.social >__ *waves*     

> __< a​ntilt:we2.ee >__ seas     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Analysis supporting changes to the DNS ban list: https://github.com/monero-project/meta/issues/1242 . Evaluated feasibility of setting up "honeypot(s)" to learn more about the infrastructure of the spy node network (seems feasible so far). Guided ditatompel to add MRL/DNS ban list columns to his table of remote nodes: https://github.com/ditatompel/xmr-remote-nodes/issues/191  <clipped message     

> __< r​ucknium:monero.social >__ https://xmr.ditatompel.com/remote-nodes     

> __< v​tnerd:monero.social >__ me: got lwsf into monero_c. but the bindings need to be re-worked and the build process is problematic     

> __< g​ingeropolous:monero.social >__ me: steering these bots to make this monerosim work     

> __< r​ucknium:monero.social >__ 3) [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).     

> __< j​berman:monero.social >__ me: drafted a proposed spec for PoW-enabled relay "PoWER" (https://github.com/monero-project/research-lab/issues/133), handled compiler warnings for FCMP++/carrot with some help from jeffro too, set up core tests testing constructing a FCMP++/Carrot tx spending from a pre-rct tx, tests went smooth     

> __< r​ucknium:monero.social >__ I would like a summary and bottom line of what has happened since the SLVer Bullet paper was first released.     

> __< s​gp_:monero.social >__ I think it would be best to hear from CS what they did, and then kayaba or I can summarize what that means for Monero and the implementation     

> __< b​randon:cypherstack.com >__ We put out an update yesterday with extensive changes taking Veridise's review and annotations into account.     

> __< b​randon:cypherstack.com >__ We also were able to prove that our verification equations are just simplifications/reductions of Bassa's/Eagen's     

> __< j​effro256:monero.social >__ Me: getting very close to a first working version of hot/cold wallet implementation for Carrot/FCMP++. Importing/exporting received outputs works, creating transaction proposals works, signing works, and finalizing FCMPs and BP+s on the hot side works. It is completely backwards compatible up until when the FCMP++ fork activates, and shouldn't require much downstream reworking. Th<clipped messag     

> __< j​effro256:monero.social >__ e RPC interface is *almost* unchanged, except for a quirk where b/c of detached FCMP++ signing, the cold wallet doesn't know TXIDs of signed transactions, but that's how tx private keys are fetched in the RPC interface. The hot/cold protocol, as implemented, also supports "stateless" hot/cold interaction, cold-initiated transaction proposals, reduced overhead when hot wallets "rem<clipped messag     

> __< j​effro256:monero.social >__ ember" tx proposals, and Carrot-derived-key wallets in the future     

> __< b​randon:cypherstack.com >__ In a sense, criticisms leveled by one of us toward the other or vice versa are superficial     

> __< b​randon:cypherstack.com >__ we were able to improve soundness bounds and little stuff like that, and improve the arithmetical efficiency of our version over the previous     

> __< b​randon:cypherstack.com >__ we present some statistical* evidence in the paper that our arguments are equivalent to Bassa's and we also provide a calculus-based explanation of why     

> __< b​randon:cypherstack.com >__ we still have some issues we are currently addressing which revolve around kayaba's code     

> __< b​randon:cypherstack.com >__ but other than that, "mysteries are solved," so to speak     

> __< k​ayabanerve:matrix.org >__ Shall I step in with my perspective now?     

> __< b​randon:cypherstack.com >__ don't ask, just do :)     

> __< f​reeman:cypherstack.com >__ Always <3     

> __< k​ayabanerve:matrix.org >__ I know sgp_ wanted to first hear from CS.     

> __< k​ayabanerve:matrix.org >__ Veridise and Cypher Stack, as of a week ago, disagreed with each other's work. Currently, Cypher Stack is signing off on Veridise's work. We have already done the implementation for and audited Veridise's work. That reduces, albeit incredibly so, all of the work of Cypher Stack to one, very long, and with many adjacent threads, review of Veridise's work which has come back with approval.     

> __< k​ayabanerve:matrix.org >__ *is now signing off on     

> __< s​gp_:monero.social >__ to be more specific, it might be best to say "cypher stack believes that eagan's scheme is secure to use"     

> __< d​iego:cypherstack.com >__ Our initial contract was to look over Bassa's / Eagen's stuff. We found it unconvincing, mostly because lack of background, proofs, and skipping over several things we deemed important. Reverse engineering that work to get it to the level of mathematical rigor we were comfortable with was taking quite some time and MRL was putting pressure on us to deliver quick.     

> __< d​iego:cypherstack.com >__ Given the time constraints, we gave a thumbs down, even though our guts told us that it would probably work out correctly. We just didn't have the time to do said rigor.      

> __< d​iego:cypherstack.com >__ We decided to take our own stab at it and made SLVer Bullet. During this current Stack Attack we have shown to our own satisfaction that our methods are equivalent to Veridise's. In so doing, we have fulfilled our original goal of giving a thumbs up or not do Eagen's / Bassa's work, though in a roundabout method.     

> __< k​ayabanerve:matrix.org >__ Right, sorry. Signing off on the result, if not necessarily the methodology and existing work.     

> __< k​ayabanerve:matrix.org >__ The only reasons to discuss Silver Bullet would be if we believed it more efficient to Monero in a way worthwhile of time and effort to migrate (non-trivial). Given how marginal any performance benefit would be _within our context_, I can not endorse investing that effort. That means, for the purposes of our discussions, even if Silver Bullet is an amazing artifact representing mo<clipped message     

> __< k​ayabanerve:matrix.org >__ nths of works, we can simply add it to a list of texts in our library for this line item and move on.     

> __< k​ayabanerve:matrix.org >__ Note the Silver Bullet paper proposes its own contexts/use-cases, and I am thankful to Cypher Stack for their self-organization and investment of their effort to promote Monero's security.     

> __< d​iego:cypherstack.com >__ Given the above, Cypher Stack is, at this point, confident is saying that either Eagen / Bassa's work, or SLVer Bullet is fit for use in Monero.      

> __< d​iego:cypherstack.com >__ Our continued work on SLVer Bullet has yielded several optimizations that we think would help Monero somewhat (though not massively), so we (obviously biased) think it may be worth it to look at the speed ups for SLVer Bullet and see if they would be worth the time to recode. And if not, using Eagen / Bassa's stuff is fine.     

> __< k​ayabanerve:matrix.org >__ _very_ thankful     

> __< b​randon:cypherstack.com >__ <3     

> __< s​gp_:monero.social >__ marginal improvements, in Monero's specific context, are ~1% right kayabanerve ? It may be more efficient in other contexts     

> __< k​ayabanerve:matrix.org >__ Within the context of the FCMP, each invocation of the current proof is _7_ rows in the IPA.     

> __< k​ayabanerve:matrix.org >__ If that was decreased to five, we'd save ~8% of the proof. As the proof is padded to a power of two, we only observe literal performance benefits w.r.t. the summary MSM if we improve performance by 50%.     

> __< k​ayabanerve:matrix.org >__ I'd find five a notable result, yet that doesn't change yes, it's of no effect when we're already at such a small constant.     

> __< k​ayabanerve:matrix.org >__ We can argue the performance of linear constraints, which don't impact the size of the MSM, yet that's the point: they don't impact the size of the MSM. They're so relatively cheap I didn't even find them worth measuring the performance impact of.     

> __< r​ucknium:monero.social >__ Are these numbers for verification time or proving time?     

> __< s​yntheticbird:monero.social >__ inb4 even 1% is welcome on the verification side     

> __< k​ayabanerve:matrix.org >__ And as per the witness size within the dedicated commitments, the one other metric this category of proof could improve in, I believe Cypher Stack agrees the current work is optimal. We currently represent a 256-bit scalar multiplication using: 256 field elements correlating to bits _and_ a 256-degree witness (SB's MakeWitness function) which has up to 256 roots.     

> __< k​ayabanerve:matrix.org >__ > we only observe literal performance benefits w.r.t. the summary MSM if we improve performance by 50%     

> __< b​randon:cypherstack.com >__ we *did* improve our proof size over the previous version     

> __< k​ayabanerve:matrix.org >__ surae: Communication of the Silver Bullet proof, for a 256-bit scalar multiplication, requires the scalar itself _and_ a witness polynomial with at least 256 elements, correct?     

> __< f​reeman:cypherstack.com >__ SyntheticBird thank you, we definitely beat 1%     

> __< k​ayabanerve:matrix.org >__ I understand the prover builds the proof from there. I just want to set the base fact of how that communication is still required.     

> __< k​ayabanerve:matrix.org >__ K, I immediately want to clarify this: Cypher Stack did not build nor propose a proof for usage within a Bulletproof. If we were to adopt Silver Bullet, we'd have to apply the same techniques as seen with the existing work to execute it within a Bulletproof.     

> __< k​ayabanerve:matrix.org >__ The performance benefits claimed, to proof size, proving, and verification, become negligible within the context Monero currently wants to use this proof in _AFAIK_.     

> __< k​ayabanerve:matrix.org >__ In the contexts Cypher Stack proposed, designed, and built, their proof for: Oh yes, much more efficient. No disagreement.     

> __< f​reeman:cypherstack.com >__ *Within* a Bulletproof, we present divisors *applied to* Bulletproof     

> __< f​reeman:cypherstack.com >__ _Within_ a Bulletproof, we present divisors _applied to_ Bulletproofs     

> __< b​randon:cypherstack.com >__ kayabanerve: correct     

> __< b​randon:cypherstack.com >__ re: proof size     

> __< b​randon:cypherstack.com >__ not including a few extra field elements     

> __< k​ayabanerve:matrix.org >__ surae: Right. With the current proof, the only elements we explicitly commit to in Pedersen Vector Commitments is the scalar itself (decomposed) and the 256-element witness polynomial.     

> __< k​ayabanerve:matrix.org >__ If both proofs have that (the statement and the witness polynomial), there is no room for improvement there.     

> __< k​ayabanerve:matrix.org >__ The only improvement, _within our context_, is with regards to the IPA rows (currently a constant `7` which means any improvements are marginal) or with regards to the linear constraints (a negligible part of our performance).     

> __< k​ayabanerve:matrix.org >__ I am not trying to bash Silver Bullet, which proposed new contexts and made great efforts on their efficiency. I just want to keep the discussion focused to our current context due to the amount of discussion we've had on it already, ideally culminating here and now. Introducing yet more doesn't help wrap this up.     

> __< k​ayabanerve:matrix.org >__ But the new contexts proposed are worthy of review and consideration, and I do believe CS deserves acknowledgement for them: I am just asking not right now.     

> __< k​ayabanerve:matrix.org >__ Because Veridise and Cypher Stack agree on the current implementation's definition, the only note is one question I raised with Cypher Stack recently. The Silver Bullet paper defines a `line` function, while my implementation has our own `line` function. The two are distinct. This would imply my proofs... math differently, and yet they are accepted by the verifiers I've defined an<clipped message     

> __< k​ayabanerve:matrix.org >__ d tested with. If my proofs are valid, yet their math is different, why are they valid?     

> __< f​reeman:cypherstack.com >__ That's something we're trying to address right now!     

> __< k​ayabanerve:matrix.org >__ I've asked Cypher Stack for an answer (of which they are not obligated to give, of course), but I believe they've been generous enough to work on to at least some degree. if this one 'discrepancy' is resolved with Cypher Stack, I see no reason not to consider the theory accepted and move on to discussing a second audit of the implementation: as-is.     

> __< k​ayabanerve:matrix.org >__ (including potentially not obtaining a second audit, I'm just noting where the discussion would shift)     

> __< r​ucknium:monero.social >__ I am confused by the current status of the objections raised by ben_sepanski  at Veridise: 1) [Something] does not hold at the function field level. 2) Rigor of proof using Schwartz-Zippel lemma.     

> __< r​ucknium:monero.social >__ I think Cypher Stack thinks it has adequately responded to those objections in the latest version. Does Veridise still think the objections are valid, or not, or has Veridise not yet (and may never) looked at Cypher Stack's responses?     

> __< k​ayabanerve:matrix.org >__ Rucknium: While I'd be happy to let Ben clarify their own position, as I do not want to speak for them, I also don't wish to expect their answer nor demand their time. Their review of Silver Bullet was voluntary. My discussion short-circuited if Veridise agreed with Cypher Stack by nothing both parties agreed on the results worked on by Veridise. That means we don't _need_ Silver <clipped message     

> __< k​ayabanerve:matrix.org >__ Bullet to be agreed upon, as we aren't implementing it.     

> __< f​reeman:cypherstack.com >__ We, to the best of our knowledge, have addressed every "category red" comment that they provided to us, as well as most of the "category orange" comments     

> __< f​reeman:cypherstack.com >__ So we argue that their two big points are not problematic for our case     

> __< rbrunner >__ So you could say that all this brings cryptography forward, but does not immediately influence us on the way to the first FCMP++ hardfork?     

> __< f​reeman:cypherstack.com >__ So we argue that their two big points are not problematic     

> __< k​ayabanerve:matrix.org >__ Though we can also shift back to discussions on hiring Veridise for _mutual agreement_, hiring a third entity to review Veridise's work (with Silver Bullet provided as an auxilliary text), or continuing work on a unified publication regarding divisors _as oriented by Veridise_ to encourage further review. As that last discussion occurs, I'll note I believe Cypher Stack are already<clipped message     

> __< k​ayabanerve:matrix.org >__  continuing with their publication, which should cause any inherent/natural review on their claims (including the claims of equivalency).     

> __< d​iego:cypherstack.com >__ Freeman's response here to their response today     

> __< r​ucknium:monero.social >__ Thank you very much to Veridise for reviewing the work 😁     

> __< b​en_sepanski:matrix.org >__ On (2), we do not believe the Schwartz-Zippel lemma (as written in either version of SLVer Bullet) can be applied. This is essentially because standard Schwartz-Zippel requires sampling variables [x,y] independently. When sampling points on an elliptic curve, the curve equation enforces a relation between x and y     

> __< b​en_sepanski:matrix.org >__ On (1), we have not had time to look in detail at the updated derivations since our initial comments. It sounds like the updated equations match Eagen's, in which case they may be correct     

> __< s​gp_:monero.social >__ kayabanerve: can you clarify the current primary blocker with the implementation? That's the most important thing for everyone to understand in the moment     

> __< r​ucknium:monero.social >__ Thank you, ben_sepanski     

> __< d​iego:cypherstack.com >__ We can continue this part of the conversation in the Research Lounge?     

> __< f​reeman:cypherstack.com >__ The dependency between coefficients vs roots will be equivalent, by Vieta's formula. And our statistical evidence supports our viewpoint     

> __< d​iego:cypherstack.com >__ #monero-research-lounge:monero.social     

> __< k​ayabanerve:matrix.org >__ sgp_: Cypher Stack believes their work equivalent, therefore proving the validity of Veridise's work in their own method. Despite this, Cypher Stack's work suggests my work shouldn't work. As my work appears to work, the _implied result_ of Cypher Stack's _claimed result_ does not _immediately_ hold. I believe this should be fully understood before we continue with the _claimed re<clipped message     

> __< k​ayabanerve:matrix.org >__ sult_, which is that Cypher Stack agrees with the current protocol because it can be proven equivalent to their own work.     

> __< f​reeman:cypherstack.com >__ "based on a brief pass we believe that neither of the two most serious issues raised were addressed by the update" vs "we have not had time to look in detail at the updated derivations since our initial comments. "     

> __< f​reeman:cypherstack.com >__ "based on a brief pass we believe that neither of the two most serious issues raised were addressed by the update" vs "we have not had time to look in detail at the updated derivations since our initial comments. " 😕     

> __< r​ucknium:monero.social >__ If I understand correctly, the two Veridise objections affect SLVer Bullet and not Eagen's original work, right? (I guess this is obvious now, but I want to make sure I have this clear.) Or do they affect the claimed proof in the SLVer Bullet paper that SLVer Bullet and Eagen's work is in some way equivalent?     

> __< s​gp_:monero.social >__ Freeman Slaughter: can you please leave this? In the context of Monero we don't care right now     

> __< k​ayabanerve:matrix.org >__ Rucknium: Correct. Cypher Stack believe Veridise's work is correct because their own work can be argued a method of proving Veridise's work. Veridise believes Cypher Stack's work has faults, and is therefore insufficient as a proof to this claim, but it doesn't change Veridise's work is only invalid _with both parties being wrong_.     

> __< k​ayabanerve:matrix.org >__ This means we do have two independent organizations claiming the security of this result.     

> __< r​ucknium:monero.social >__ Previously, Cypher Stack said that the calculus work in Eagen's paper was "incorrect". How can this be? Was it 1) The calculus was correct, after all, 2) Cypher Stack found another way around the problem that didn't involve the "incorrect" calculus, or 3) Something else?     

> __< k​ayabanerve:matrix.org >__ Though I still want to understand why the 'implied result' is not immediately understood, which of course Cypher Stack has said they're working on (much to my appreciation).     

> __< f​reeman:cypherstack.com >__ We always argued that Veridise *could* be correct, just that we were not convinced by their proofs. An unjustified proof can never be correct, because it relies on something whose veracity is not supported. The calculus was correct, in a consequentialist sense, but their proofs were confusing enough for us that we were forced to rederive them from scratch (which we only recently f<clipped messag     

> __< f​reeman:cypherstack.com >__ inished to a level that we found sufficient)     

> __< r​ucknium:monero.social >__ From what I understand today, I would prefer that a third firm confirm the correctness or one or both of Veridise's and/or Cypher Stack's claimed proofs of the soundness of Eagen's divisors.     

> __< d​iego:cypherstack.com >__ Rucknium, you're referring to the fact that in a previous MRL meeting, I stated that the calculus was incorrect.     

> __< d​iego:cypherstack.com >__ This was because Brandon had said that Eagen had incorrectly applied the chain rule. The incorrectness comes from the fact that the use of it in that context was not justified.     

> __< f​reeman:cypherstack.com >__ For instance, their usage of the chain rule was not justified, in our view. So any application of it is "incorrect" until that step is justified     

> __< d​iego:cypherstack.com >__ fwiw, I would support getting a third firm involved to look things over.     

> __< s​gp_:monero.social >__ Rucknium: another review of the Eagan technique may still be warranted, yes     

> __< d​iego:cypherstack.com >__ We can move forward with testnets and things in the meantime.     

> __< s​gp_:monero.social >__ But these two firms are currently in agreement with the Eagan scheme being secure     

> __< k​ayabanerve:matrix.org >__ Rucknium: You understand we currently have both research outfits agree the currently defined proof is secure, with independent methodologies, correct?     

> __< r​ucknium:monero.social >__ They don't agree on the same mathematical proof.     

> __< k​ayabanerve:matrix.org >__ The fact they disagree on their methodologies does not shift _both must be wrong_ for the proof to be wrong.     

> __< r​ucknium:monero.social >__ That isn't what I expected.     

> __< k​ayabanerve:matrix.org >__ They disagree on the _security proofs_ for the proof.     

> __< r​ucknium:monero.social >__ I expected CS to agree that Veridise's original proof was correct.     

> __< k​ayabanerve:matrix.org >__ They both agree the proof has the desired mathematic effects w.r.t. elliptic curves.     

> __< d​iego:cypherstack.com >__ Incorrect. They didn't make security proofs to disgree with. :P     

> __< k​ayabanerve:matrix.org >__ They do agree the proof is correct. They disagree the arguments for it, at the time, were convincing.     

> __< s​gp_:monero.social >__ they got to the same result with different work, which wasn't the simplest path but it still a valid option     

> __< r​ucknium:monero.social >__ CS wrote a new proof.     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: While a joking comment, it makes no difference to this discussion.     

> __< s​gp_:monero.social >__ if budget allows, a third review could be commissioned, but it's not really _strictly_ necessary     

> __< k​ayabanerve:matrix.org >__ Rucknium: Which is why we currently have two independent groups, with two independent methodologies, agreeing the defined proof is built on sound theory.     

> __< rbrunner >__ Hmm, doesn't the mountain of material to potentially review grow all the time?     

> __< r​ucknium:monero.social >__ If I understand correctly, the two firms disagree that the other's proof is fully valid.     

> __< k​ayabanerve:matrix.org >__ Which is why I'd prefer to discuss using the budget on a second audit, before discussing a third review of the theory, with the emphasis being I'd like to move forward.     

> __< rbrunner >__ Now already two different proofs, if I understand correctly     

> __< s​gp_:monero.social >__ a third reviewer might in theory make yet a third route to also support security     

> __< rbrunner >__ :)     

> __< k​ayabanerve:matrix.org >__ (all of this assuming the 'implied result' thing gets circled back on, which I expect and believe will occur)     

> __< k​ayabanerve:matrix.org >__ Do we know 51 qualified research outfits eligible to participate in a ranked-choice vote?     

> __< d​iego:cypherstack.com >__ Is ZK-Security no longer available?     

> __< k​ayabanerve:matrix.org >__ Rucknium: The other's arguments for why the proof is valid. They agree on the proof.     

> __< f​reeman:cypherstack.com >__ Ultimately, any disagreement with our work is a disagreement with Eagen's work, since we've shown them to be equivalent     

> __< k​ayabanerve:matrix.org >__ Rucknium: The other's arguments for why the proof is valid. They agree on the proof we would implement in _some context_.     

> __< k​ayabanerve:matrix.org >__ The proof != the security proofs, as I keep trying to iterate.     

> __< r​ucknium:monero.social >__ AFAIK, Veridise isn't sure that the equivalency holds.     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: I was making a joke on ensuring qualified review.     

> __< f​reeman:cypherstack.com >__ Ultimately, any disagreement with our work is a disagreement with Eagen's work, since we've shown them (the verification equations) to be equivalent     

> __< s​gp_:monero.social >__ but Veridise independently supports the Eagan scheme     

> __< j​berman:monero.social >__ I would advocate for a 3rd independent review before mainnet, but prioritize tasks that move forward toward mainnet     

> __< s​gp_:monero.social >__ both groups agree Eagan's scheme is secure     

> __< r​ucknium:monero.social >__ Why did cryptographers name something "proof" when that term was already taken? 🤔     

> __< d​iego:cypherstack.com >__ Correct. So the actual summation is that:     

> __< d​iego:cypherstack.com >__ 1. Veridise supports Eagen's scheme     

> __< d​iego:cypherstack.com >__ 2. Cypher Stack supports Eagen's scheme in a way that Veridise doesn't agree with (SLVer Bullet)     

> __< d​iego:cypherstack.com >__ the end result is indeed that both firms support Eagen's scheme     

> __< k​ayabanerve:matrix.org >__ Sorry, but to take this back a second: Rucknium, of course, you are allowed to believe a third review is justified. I just want to be clear, both Veridise and Cypher Stack currently agree on a proof to implement. They have independent arguments for why the proof is secure, and disagree with each other's arguments.     

> __< d​iego:cypherstack.com >__ with the caveat that there is disagreement on how the support comes about from Veridise's side     

> __< f​reeman:cypherstack.com >__ We only released v3 the other day, so I would like clarification on if the Veridise comments pertain to this new version or not     

> __< r​ucknium:monero.social >__ I agree with jberman . The "third review" can occur in parallel to the implementation work, and any other code audit work.     

> __< r​ucknium:monero.social >__ If a third review were to occur     

> __< k​ayabanerve:matrix.org >__ If you could confirm your understanding is they disagree on the road, not the destination, that would be great Rucknium.     

> __< j​berman:monero.social >__ Zk Security was prior brought up as a 3rd party to bring in for this review. I think it makes sense to bring them in prioritizing other work at this time, but to keep them in mind for a future 3rd review     

> __< g​ingeropolous:monero.social >__ and/or, the existing can be implemented, and then a third review can review both the math and the implementation     

> __< r​ucknium:monero.social >__ This wouldn't qualify as passing peer review in a journal since the reviewer(s) would have to agree that the author had a valid, specific, proof.     

> __< s​yntheticbird:monero.social >__ i don't think charging the same people for reviwing both the math and implementation is a good idea     

> __< r​ucknium:monero.social >__ I have never seen "Ok, here are two possibly-valid proofs"     

> __< s​yntheticbird:monero.social >__ i don't think charging the same people for reviewing both the math and implementation is a good idea     

> __< r​ucknium:monero.social >__ Choose which one you like     

> __< s​yntheticbird:monero.social >__ at least not at the same time     

> __< f​reeman:cypherstack.com >__ Unfortunately, happens all the time in pure math.... 😅     

> __< r​ucknium:monero.social >__ I think they do agree on the destination.     

> __< k​ayabanerve:matrix.org >__ Are we allowing the axiom of choice?     

> __< s​yntheticbird:monero.social >__ Heresy!     

> __< f​reeman:cypherstack.com >__ Yes, but not the well ordering principle     

> __< r​ucknium:monero.social >__ Axiom of choice is always necessary for any real work.     

> __< rbrunner >__ Insider jokes?     

> __< k​ayabanerve:matrix.org >__ I personally don't believe in free will and have (as inscribed in the universe itself) decided not to be convinced by any proof requiring even the idea of choice     

> __< k​ayabanerve:matrix.org >__ rbrunner: The axiom of choice is an axiom one can use when writing proofs, with extensive debate over if it should be used and the impacts of it.     

> __< l​uke:cypherstack.com >__ There are like 400 distinct proofs of the Pythagorean Theorem. It is incredibly common to come upon a true result with vastly different methods.     

> __< k​ayabanerve:matrix.org >__ The end result is, you can use it or not use it, up to you.     

> __< k​ayabanerve:matrix.org >__ Here, we have two proofs. You can use or use the other. Up to you.     

> __< d​iego:cypherstack.com >__ Unfortunately, this is the way math works sometimes. There are disagreements on subtleties here. We don't think these disagreements will affect Monero in any real sense.     

> __< k​ayabanerve:matrix.org >__ But there will be people who prefer axiom of choice, and be people who prefer not to have it.     

> __< f​reeman:cypherstack.com >__ Zorn's lemma..... well, who really knows?     

> __< r​ucknium:monero.social >__ Luke Szramowski: I agree with you. It is not common for there to be two proofs and the two proof-writers to disagree with each other on the validity of the other.     

> __< k​ayabanerve:matrix.org >__ Obviously, we'll find people convinced either way, and people not convinced of specific proofs regardless of if the axiom of choice was used or not.     

> __< d​iego:cypherstack.com >__ I propose the following:     

> __< d​iego:cypherstack.com >__ 1. Get a third party to look over Eagen's work. Share Veridise's work as well as Cypher Stack's for background.     

> __< d​iego:cypherstack.com >__ 2. Move forward with testnets, since we do have two separate firms giving the ok.     

> __< g​ingeropolous:monero.social >__ we have an n of 2. need to get to that magic n of 3     

> __< k​ayabanerve:matrix.org >__ That doesn't change here, we have two independent research outfits approving the result _as originally desired_.     

> __< r​ucknium:monero.social >__ I agree with Diego Salazar     

> __< j​berman:monero.social >__ I do as well^     

> __< k​ayabanerve:matrix.org >__ A third entity reviewing theory before a second audit would be a notable misuse of funds IMO.     

> __< s​gp_:monero.social >__ I'll get a quote from zksecurity so it can be considered     

> __< rbrunner >__ second audit of what?     

> __< d​iego:cypherstack.com >__ I will discuss with PUP about funding it.     

> __< d​iego:cypherstack.com >__ so MRL doesn't have to hem and haw about misuse of funds     

> __< k​ayabanerve:matrix.org >__ I don't believe, in good faith, I can prioritize a third review of theory (which already has two points of failure) before a second audit of its implementation (a current single point of failure).     

> __< r​ucknium:monero.social >__ PUP = Power-up Privacy     

> __< j​berman:monero.social >__ I also agree with kayabanerve that we should prioritize other work over the 3rd review     

> __< d​iego:cypherstack.com >__ sgp_: please get me the quote (you can tell MRL too obviously), and I'll pass it on to get funded ASAP if PUP is down (Which they probably will be)     

> __< d​iego:cypherstack.com >__ this lets MRL focus on the implementation review     

> __< d​iego:cypherstack.com >__ The one! The only!     

> __< r​ucknium:monero.social >__ I think there may be loose consensus on proceeding with FCMP implementation code-writing and remaining code audits as priority. And a range of views from "indifferent" to "desired" for a third firm to review the Divisor mathematics, especially if it does not require funds from the FCMP research CCS     

> __< k​ayabanerve:matrix.org >__ Diego Salazar: You're welcome to ignore my advisory yet that doesn't change a _cold read_ of your immediate messages is that the solution to a potential misuse of funds is to find a donor who doesn't care about potential misuse. I understand the point, where if we agree it'd be good to do eventually _and_ we have a large enough fund pool, why not, but I'm irked by the near-complet<clipped message     

> __< k​ayabanerve:matrix.org >__ e circumvention of the oversight process not inherently because it's slow, but so we don't have to "hem and haw about misuse of funds" (which yes, was presumably intended as a jokey message where the real issue would be how long the hemming and hawwing takes).     

> __< r​ucknium:monero.social >__ The Divsior review as completely parallel and non-blocking to the other priorities.     

> __< j​berman:monero.social >__ Noting OtterSec looks like a solid candidate to bring in to the mix as well: https://pse.dev/blog/under-constrained-bug-in-binary-merkle-root-circuit-fixed-in-v200     

> __< k​ayabanerve:matrix.org >__ I'd like to hem and haw _a reasonable amount_. If the amount of funds available is more notable, the amount we have to hem and haw decreases.     

> __< d​iego:cypherstack.com >__ Wrong. But we can discuss later.     

> __< s​yntheticbird:monero.social >__ I ran out of water     

> __< k​ayabanerve:matrix.org >__ I'd like to delegate the scoping discussions to SGP, as they volunteered and they asked, and hear the response. If they have a reasonable quote for both, we can discuss that, but my priority would be the _audit_ side of things.     

> __< k​ayabanerve:matrix.org >__ Outside contracting zkSecurity for one task, when another task is the better-agreed priority, may delay the overall process.     

> __< k​ayabanerve:matrix.org >__ Rucknium: It isn't completely parallel if it is scheduled sequentially to the same entity.     

> __< rbrunner >__ You got a point :)     

> __< s​gp_:monero.social >__ I think an audit should occur as the main priority regardless. Please feel free to DM me or email me (justin⊙mo) if you have someone in mind for the audit! I can help with that     

> __< k​ayabanerve:matrix.org >__ At this time, I'd also like to delegate to jberman who has the practical commentary on moving forward as the R part of R&D runs in parallel     

> __< r​ucknium:monero.social >__ It is if the elements within the entity working on it would not be the same     

> __< k​ayabanerve:matrix.org >__ "scheduled sequentially"     

> __< r​ucknium:monero.social >__ Ok, so do the third review of divisors after the code audit. That sounds OK to me, if necessary.     

> __< d​iego:cypherstack.com >__ I will respond to this in Monero Research Lounge so as not to clog up the meeting.     

> __< rbrunner >__ I tend to agree, at least right now     

> __< s​gp_:monero.social >__ I     

> __< s​gp_:monero.social >__ sorry, *I'll get some quotes     

> __< r​ucknium:monero.social >__ What else needs to be decided & discussed on Divisors?     

> __< r​ucknium:monero.social >__ Thank you, sgp_     

> __< r​ucknium:monero.social >__ Ready to move on to agenda item 4 of 10?     

> __< j​berman:monero.social >__ I say yes     

> __< a​rticmine:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ 4) [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< r​ucknium:monero.social >__ Thank you, ArticMine  for this write-up.     

> __< j​effro256:monero.social >__ The third review of divisors not need be done by a third-party, and it may be cheaper / more efficient, to have both Veriside / Cypherstack work together to find a methodology that both are happy with. We may contract a third-party and still end up with a nre security proof for the divisors technique that the other two aren't happy with. Yes, there may be 400 proofs for the Pythag<clipped messag     

> __< j​effro256:monero.social >__ orean theorem, but there is probably at least one which basically everyone agrees is valid under certain axioms. If we do more theory review, I think we should try to move towards finding 1 methodology that almost everyone accepts, not 3 methologies which 33% each accept, and the rest partially accept     

> __< a​rticmine:monero.social >__ Any questions or comments     

> __< s​packle:monero.social >__ What the current thinking in regards to adding an additional safety 'ultra-long term' median to the new design?     

> __< j​effro256:monero.social >__ Sorry typing that was slow, I can continue the convo in lounge for now     

> __< a​rticmine:monero.social >__ I look at that.     

> __< a​rticmine:monero.social >__ There is the cost of calculation. ~ 4 years of transactions     

> __< j​berman:monero.social >__ ArticMine: regarding section 5.2 Transaction Weights (Proposed), Input proofs weight, that's the originally proposed weight approach that jeffro256 implemented that I have some thoughts on: https://github.com/seraphis-migration/monero/pull/26#discussion_r2057203539     

> __< j​berman:monero.social >__ TL;DR my thoughts: it would incentivize making more txs spending the same number of inputs, rather than spending them in 1 tx (e.g. spending 3 inputs in a 1-in and 2-in would be cheaper than spending in a 3-in)     

> __< a​rticmine:monero.social >__ We have a conflict in pricing in consensus and node relay     

> __< a​rticmine:monero.social >__ So if we increase the weight in consensus to cover verification time then we also have to further in crease the fee in node relay to avoid soam     

> __< a​rticmine:monero.social >__ This is why I am recommending moving the price difference between actual size and verification time entirely to node relay     

> __< a​rticmine:monero.social >__ Also if the relative cost changes it can then be addressed in node relay     

> __< j​berman:monero.social >__ I don't follow the justification for selecting weights like that though     

> __< a​rticmine:monero.social >__ You mean for number of inputs     

> __< j​berman:monero.social >__ Right, rounding up to powers of 2     

> __< j​berman:monero.social >__ An original justification for that approach was to more closely tie weight to verification time     

> __< a​rticmine:monero.social >__ Is there no cost advantage in size or verification time with powers of 2?     

> __< a​rticmine:monero.social >__ Cost per number of inputs     

> __< j​berman:monero.social >__ The advantage is to increase weight more significantly than it would otherwise be increased using byte size alone, in order to more closely resemble the increasing verification time as n inputs increases     

> __< a​rticmine:monero.social >__ Namely say 3 vs 4 inputs     

> __< a​rticmine:monero.social >__ Yes but we can move this to node rlay     

> __< a​rticmine:monero.social >__ Relay     

> __< j​effro256:monero.social >__ ArticMine: do you have the spreadsheet with exact tx byte sizes for Carrot/FCMP++ txs as-is?     

> __< a​rticmine:monero.social >__ No I was looking for this     

> __< j​berman:monero.social >__ With rounding up to powers of 2, someone is more incentivized to spend 4 inputs instead of 3 if they're able to, which is bad and also not reflective of the actual verification time or byte size     

> __< a​rticmine:monero.social >__ Then you have a point     

> __< j​effro256:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/JsKFvrmjEOzSkGSKoRVGYEFq     

> __< j​effro256:monero.social >__ ^ Assuming divisors and Carrot stay as-is this should be accurate     

> __< j​berman:monero.social >__ well, I guess it's close to verification time since the verification time of 3 is only very slightly less than for 4 inputs     

> __< j​berman:monero.social >__ but that doesn't hold as well for 5 inputs vs 8 inputs e.g.     

> __< a​rticmine:monero.social >__ Then there is an advantage of 4 over 3     

> __< a​rticmine:monero.social >__ I will take a close look at the spreadsheet and review     

> __< j​berman:monero.social >__ Can see the tables here also that include size and verification time for the membership proof alone: https://github.com/seraphis-migration/monero/pull/26#discussion_r2057203539     

> __< j​effro256:monero.social >__ The total verification time for a node for a 1-in FCMP tx and a 3-in FCMP tx is much greater than a 4-in FCMP tx, so this is in fact good, right?     

> __< j​effro256:monero.social >__ We want people to spend a 4 instead of a 3 and a 1 (ignoring privacy for the moment)     

> __< r​ucknium:monero.social >__ This is a question for anyone familiar with the protocol: Is the size of `tx_extra`, usually/always the same size when the number of outputs are the same and the tx is of the same type with respect to paying to an integrated address?     

> __< j​effro256:monero.social >__ If one is using Carrot or our current addressing protocol, basically yes. But there is nothing enforcing this at consensus     

> __< a​rticmine:monero.social >__ Yes but this does not take into account the additional fee per byte needed at node relay     

> __< r​ucknium:monero.social >__ I am asking this because the Transaction weight section on page 6 says "Use actual size." for `tx_extra`.     

> __< j​effro256:monero.social >__ Actually, fun fact, the current code for tx construction can produce a different size of `tx_extra` and leak whether one of the destinations is a subaddress in >2-out transactions     

> __< a​rticmine:monero.social >__ The issue is that a 40k TX requires 16 x the fee of a 10k tx     

> __< r​ucknium:monero.social >__ Minor correction/question: In the right column of page 2, it says, "`f_IL = 0.95f_R` ; Minimum fee per byte". I didn't see `f_R` defined in the right column. I think you changed notation. Should `f_R` be `f_RL`?     

> __< a​rticmine:monero.social >__ Fee per bute     

> __< a​rticmine:monero.social >__ Byte     

> __< j​berman:monero.social >__ that's true. my line of reasoning there was incorrect. The problem with scaling to powers of 2 was not with 3-in+1-in compared to 4-in. It was on 3-in compared to 1-in + 2-in (the latter is incentivzied), and on {5,6,7}-in's not being incentivized compared to lower input combinations     

> __< a​rticmine:monero.social >__ Under the current situation of allowing these over size TXs at the minimum node relay fee applying the weights at consensus works     

> __< j​effro256:monero.social >__ Isn't it more accurate to say that the total fee of all the tx fees is quadratic over the penalty zone, not that each individual transaction needs 4x fee?     

> __< j​effro256:monero.social >__ It may actually need more than 4x or less than 4x, depending on the ratio of the total tx fee to the block subsidy     

> __< a​rticmine:monero.social >__ At the start of the penalty zone it is quadratic     

> __< a​rticmine:monero.social >__ Deep into the penalty zone it approaches linear     

> __< a​rticmine:monero.social >__ The issue is that a spammer can target the large TXs and create spam that low or no cost because the TXs are not mined     

> __< k​ayabanerve:matrix.org >__ Except this is good for privacy.     

> __< a​rticmine:monero.social >__ Yes privacy is the other argument     

> __< j​berman:monero.social >__ Ya feel free to ignore my commentary on 3-in vs 4-in above, that's not where the issue is with scaling to powers of 2 and I was mistaken     

> __< k​ayabanerve:matrix.org >__ I still advocate an 8-input limit.     

> __< j​berman:monero.social >__ But I guess if you want to argue taht it's superior for privacy to have 1-in and 2-in's versus 3-in's, then that's a discussion     

> __< k​ayabanerve:matrix.org >__ Hell, we can even program a sunset such that the amount of inputs halve every three months until they reach the set target.     

> __< a​rticmine:monero.social >__ I am fine with that     

> __< a​rticmine:monero.social >__ 8 input limit     

> __< k​ayabanerve:matrix.org >__ ... or did my long-post with evidence resolve as 16-input? Is it 8 or 16 my final opinion was? 🤔     

> __< k​ayabanerve:matrix.org >__ Regardless, point on an input limit <= 16 _and_ and a sunset can be on the table.     

> __< a​rticmine:monero.social >__ My point is that if more 8 inputs are allowed then the additional pricing at node relay is needed     

> __< a​rticmine:monero.social >__ Emphasis on if     

> __< r​ucknium:monero.social >__ I think this discussion is getting close to PoW-Enabled Relay (PoWER), which is later on the agenda.     

> __< j​berman:monero.social >__ In a past meeting we generally agreed on high input limits with PoWER^. A core benefit of high input limits is atomic high input txs and fewer outputs on chain when spending more inputs, which some seem to want pretty strongly     

> __< j​berman:monero.social >__ Regarding the fee discussion, I'm thinking maybe we give ArticMine more time to review the byte sizes / verification times and potentially adjust the proposal?     

> __< a​rticmine:monero.social >__ I am fine with that     

> __< s​packle:monero.social >__ Returning for a moment to discussing a safety median; the calculation being prohibitive feels like an addressable problem. An example might be to only consider every tenth block over the period of interest.     

> __< s​packle:monero.social >__ No need to stall discussion on this point, but I would like to see it thoroughly considered.     

> __< a​rticmine:monero.social >__ There are alternatives, namely restricting upward bandwidth for TXs before they are mined at node relay     

> __< j​effro256:monero.social >__ We already cache a rolling median in the DB code, doing a billion block median is as simple as a 100K median like we currently have. The issue is if we want wallets to be able to calculate the fees     

> __< r​ucknium:monero.social >__ Don't wallets need nodes to suggest fees, anyway? That cannot really be avoided, AFAIK.     

> __< a​rticmine:monero.social >__ The wallets would not be impacted, all the sanity median does is restrict the growth of the long term median     

> __< a​rticmine:monero.social >__ ... and peg this growth to Nielsen's Law     

> __< r​ucknium:monero.social >__ We will come back to this topic next week, at least.     

> __< j​effro256:monero.social >__ So this is a whole discussion that we could spend another hour on lol. It depends under what assumptions you want the wallet to operate under. If it's an SPV wallet model, we could put block weight rolling medians in the block content so it's attested to by PoW. Then the wallet need only trust the longest chain for valid fee data     

> __< r​ucknium:monero.social >__ 5) [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).     

> __< r​ucknium:monero.social >__ IMHO, a post-mortem of lessons learned on the competition could be nice, but maybe it is better to have another week of time to reflect, given the current time 😅     

> __< j​berman:monero.social >__ Need to write the official writeup. Waiting on clarification from binary fate on the General Fund funding a 2nd place prize. lederstrumpf's submission has been integrated and kayaba has already improved on it. fabrizio's submission is in PR and fabrizio has kindly fixed an internal test failure that I plan on adding to the PR today too     

> __< j​effro256:monero.social >__ Yes I really want to post something like this, because the whole process was very insightful, and there were a few bumps that everyone could've skipped with a bit more planning by us on the front-end of things. And those things aren't necessarily intuitive until you've already done something like this     

> __< r​ucknium:monero.social >__ 6) [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< j​berman:monero.social >__ I would like to move forward on an alpha *testnet, and will give more color on why I say testnet instead of stressnet for the time being     

> __< j​effro256:monero.social >__ Sounds like we can scratch off SLVer bullet from the list based on today's discussion ...     

> __< j​effro256:monero.social >__ Do spackle or ofrnxmr have anything else to add here that wasn't already posted in that GH issue?     

> __< j​berman:monero.social >__ With fabrizio's divisor integrated, prove() time is still quite slow for high input txs (128 input proofs take 5 minutes to construct on a high end Ryzen). I opened a tracking issue for this here: https://github.com/kayabaNerve/fcmp-plus-plus/issues/34     

> __< s​packle:monero.social >__ Mostly a plea for consideration: The planned scaling design allows 32MB blocks in the near term. Ensuring that the daemon can handle blocks of this size is significant. Instead of a spam attack creating a potential issue in the span of hours/days, it would take a couple of months.     

> __< k​ayabanerve:matrix.org >__ That issue is solved by limiting the amount of supported inputs to 8 at the consensus level, which also improves privacy.     

> __< j​berman:monero.social >__ I don't expect we'd be able to bring that prove() time down in the short term. We can discuss action plans on bringing that prove() time down in the medium term. But I don't think it should hold up getting an alpha testnet up and running     

> __< r​ucknium:monero.social >__ Making Monero easy to use for everyone encourages the anonymity set to grow, which improves privacy :P     

> __< j​berman:monero.social >__ So I'd say for this initial alpha network, we have 2 options: 1) integrate very slow prove() times for high input txs, or 2) keep consensus as is at limiting to 8 inputs     

> __< j​berman:monero.social >__ Obviously, kayaba has an opinion on this lol, but worth discussing both routes today     

> __< s​gp_:monero.social >__ for alpha I personally don't care     

> __< k​ayabanerve:matrix.org >__ Or, keep consensus as-is, and simply have people choose whether or not to observe large prove times.     

> __< k​ayabanerve:matrix.org >__ That would be the case if we deployed to mainnet today.     

> __< k​ayabanerve:matrix.org >__ Let testnet model life.     

> __< r​ucknium:monero.social >__ A test/stressnet doesn't necessarily have to have high-input txs. Usually, it must have high-output txs to make it easier on the spam formation.     

> __< r​ucknium:monero.social >__ jberman: I am ok with either of those two options.     

> __< r​ucknium:monero.social >__ For the "wider" non-alpha stressnet, I would want to consider the options again at the time that decision would need to be made.     

> __< j​effro256:monero.social >__ I'd go with #1. We should allow high-input txs, and let those people who want to make high-input txs deal with it for now     

> __< j​berman:monero.social >__ Ok, I'm fine with #1     

> __< j​effro256:monero.social >__ Although in the tx construction APIs, we could perhaps allow a parameter which optionally caps the number of inputs     

> __< j​berman:monero.social >__ How about this plan: we aim to have all code ready to go for an alpha *stressnet* by next week's meeting, and settle on a timeline to stressnet then?     

> __< j​berman:monero.social >__ Tangential point, I also included this in the PoWER proposal     

> __< r​ucknium:monero.social >__ That sounds great to me.     

> __< j​berman:monero.social >__ to allow wallets to use the wallet API without shipping a PoW algo     

> __< r​ucknium:monero.social >__ Of course, I'm not writing any of the code :D     

> __< j​effro256:monero.social >__ That's where I got the idea from ;)     

> __< j​effro256:monero.social >__ Should we add PoWER to the alpha stressnet agenda?     

> __< j​berman:monero.social >__ I don't think so, that's going to take time (and also I've heard we may have an externally  funded dev interested in working on it)     

> __< j​berman:monero.social >__ by external I mean non-CCS     

> __< j​effro256:monero.social >__ K fair enough. Would also be nice to get data on hammering the nodes with high-input txs without PoWER     

> __< r​ucknium:monero.social >__ On to next agenda item?     

> __< b​oog900:monero.social >__ are we on PoWER?     

> __< j​berman:monero.social >__ good with me     

> __< r​ucknium:monero.social >__ boog900: No     

> __< r​ucknium:monero.social >__ 7) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< r​ucknium:monero.social >__ Here was my update pertaining to spy nodes:     

> __< r​ucknium:monero.social >__ Analysis supporting changes to the DNS ban list: https://github.com/monero-project/meta/issues/1242 . Evaluated feasibility of setting up "honeypot(s)" to learn more about the infrastructure of the spy node network (seems feasible so far). Guided ditatompel to add MRL/DNS ban list columns from my network scan data to his table of remote nodes: https://github.com/ditatompel/xmr-rem<clipped message     

> __< r​ucknium:monero.social >__ ote-nodes/issues/191  https://xmr.ditatompel.com/remote-nodes     

> __< r​ucknium:monero.social >__ AFAIK, the Core Team would need to implement any change to the DNS ban list contents. Feel free to comment on the issue and/or thump-up/down.     

> __< r​ucknium:monero.social >__ Any more comments or questions on this agenda item?     

> __< r​ucknium:monero.social >__ 8) Rucknium's research agenda.     

> __< r​ucknium:monero.social >__ In the next day or two I will finish my current CCS and open a proposal for a new one. What should be on my research agenda? I think I should definitely continue to work on short-, medium- and long-term solutions to network-level privacy against spy nodes. I also have a few loose ends that I want to tie up, e.g. final versions of subnet deduplication and black marble MRL bulletins<clipped message     

> __< r​ucknium:monero.social >__ , writeup of results of safety of OSPEAD deployment.     

> __< r​ucknium:monero.social >__ A "new" topic I could start to look into would be mining pool centralization. I would want to explore voluntary pool Pigouvian fee solutions, i.e. pools agree that when their hashpower share gets "too high" that the fee they charge to miners increases, to encourage some miners to switch to a lower-hashpower pool.     

> __< r​ucknium:monero.social >__ I am on the fence about whether to package the OSPEAD results for submission to a peer-reviewed journal like PoPETs. PoPETs has a deadline for submissions every three months, the next being August 31. I would probably need most of August to get the paper in shape.     

> __< r​ucknium:monero.social >__ Any other suggestions are welcome :)     

> __< r​ucknium:monero.social >__ My areas are statistics, economics, and game theory. (But I prefer to make only light use of game theory on the grounds of methodological principles.)     

> __< r​ucknium:monero.social >__ 9) CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).     

> __< r​ucknium:monero.social >__ gingeropolous 's update on this was "me: steering these bots to make this monerosim work"     

> __< r​ucknium:monero.social >__ boog900: PoWER is the next, and final, agenda item.     

> __< r​ucknium:monero.social >__ 10) [Proposal and spec for Proof-of-Work Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).     

> __< j​berman:monero.social >__ kayabanerve: any more thoughts on Equi-X vs RandomX light?     

> __< r​ucknium:monero.social >__ Thank you for the proposed specification, jberman     

> __< j​effro256:monero.social >__ Dynamically increasing miner fees is an interesting idea, and I have held for a long time that minexmr should've done this instead of shutting down, since the practical effect was that people redistributed to other centralized pools, but now there was one fewer big pool     

> __< b​oog900:monero.social >__ I think this is also going to require a change in alt-block handling, otherwise people can get around the 10 block rule by mining lots of blocks and sending them all at once     

> __< j​effro256:monero.social >__ I think that OSPEAD is absolutely still worth working on / polishing up for two main reasons: 1) Monero wallets might use decoy selection for FCMP path fetching, and 2) there will still be other ring-signature-based privacy coins in operation     

> __< j​effro256:monero.social >__ Salvium, Zano, etc     

> __< r​ucknium:monero.social >__ This issue with RandomX being flagged by anti-virus scanners. I think that could be an advantage for Equi-X, right?     

> __< b​oog900:monero.social >__ for example header only sync until we know the chain has enough PoW     

> __< j​berman:monero.social >__ Potentially yep, I noted that in that follow-up comment     

> __< b​oog900:monero.social >__ also I wonder if putting the PoW on inbound connections would be better for preventing P2P node DoS     

> __< k​ayabanerve:matrix.org >__ Equi-X seems the better fit re: purpose.     

> __< r​ucknium:monero.social >__ jeffro256: Thanks for your input. I was also unsure if a journal like PoPETs is "still interested" in ring signatures. It seems that they still are because they just published Christian Cachin & François-Xavier Wicht  "Toxic Decoys: A Path to Scaling Privacy-Preserving Cryptocurrencies" https://crysp.petsymposium.org/popets/2025/popets-2025-0165.php     

> __< r​ucknium:monero.social >__ Moser et al. (2018) is one of their top-cited articles, too, which helps probably.     

> __< j​berman:monero.social >__ thoughts on ASIC resistance being a reasonable +1 for Monero compared to tor?     

> __< r​ucknium:monero.social >__ What is the difference between FPGA and ASIC resistance? I don't understand well, but I thought FPGA was basically a prototype-stage ASIC.     

> __< b​oog900:monero.social >__ seen as this is isn't consensus, I think ours and Tor's requirements are similar here?     

> __< b​oog900:monero.social >__ seen as this isn't consensus, I think ours and Tor's requirements are similar here?     

> __< r​ucknium:monero.social >__ Could one reasonably rent RandomX hashpower to create the PoWER PoW hashes? Or would the usual mining API not support that?     

> __< j​berman:monero.social >__ as in, inside `handle_notify_new_transactions`, only check for PoW on inbound connections rather than outbound?     

> __< b​oog900:monero.social >__ I mean PoW for connection attempts not on txs     

> __< b​oog900:monero.social >__ I think it would solve this issue `Txs sitting in the pool longer than 10 blocks`     

> __< j​berman:monero.social >__ An FPGA can be reprogrammed and repurposed, an ASIC is designed for one specific purpose (and costs a lot to develop, estimated $1mn with citation by tevador in that initial reasoning)     

> __< j​berman:monero.social >__ I'm not going to die on the hill of RandomX light over Equi-X, so if I'm the only one +1'ing RandomX light, I'd defer to Equi-X     

> __< r​ucknium:monero.social >__ Any estimate of the coding work time to integrate RandomX vs Equi-X?     

> __< d​oedl...:zano.org >__ thats to protect miners with 100's of incoming cx     

> __< j​berman:monero.social >__ ah gotcha     

> __< b​oog900:monero.social >__ txs would still need PoW for public RPC nodes FWIW     

> __< b​oog900:monero.social >__ unless you do PoW on RPC connections too 🤔     

> __< j​berman:monero.social >__ PoW on connection actually does make more sense, that's a good point, since a bad actor can only get 1 bad tx before getting dropped anyway     

> __< j​berman:monero.social >__ PoW on RPC connection for wallets that support it, otherwise said wallets can't construct >8-input txs over the connection if the daemon has the startup flag, seems to make sense to me too     

> __< r​ucknium:monero.social >__ To make sure that's true, check the procedure that is followed when a node gets multiple txs in a single message. Does it abort and ban on the first ban tx?     

> __< j​berman:monero.social >__ I think it does, but yes would need to make sure the node does this upon implementing too     

> __< r​ucknium:monero.social >__ Usually, multiple txs are clumped together in normal conditions, anyway.     

> __< r​ucknium:monero.social >__ first bad tx*     

> __< b​oog900:monero.social >__ no ban, but does disconnect it seems: https://github.com/monero-project/monero/blob/fbc242d52d89d9c8021194cd4faae657c94d5a31/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L943     

> __< g​ingeropolous:monero.social >__ yeah, im unclear why tor went with equi-x vs randomx, and if tor chose to go equi-x as a ddos prevention thinger, then aren't we trying to do the same here?     

> __< j​berman:monero.social >__ this was my argument: https://github.com/monero-project/research-lab/issues/133#issuecomment-3100620908     

> __< d​oedl...:zano.org >__ afaik 1 bad tx (doublespend) and connection is not banned right now (to prevent defamation attack)     

> __< b​oog900:monero.social >__ Actually people would be able to create lots of valid txs and send them all at once, do we have a minimum block ref for FCMP?     

> __< j​effro256:monero.social >__ I think that this opens an arguably larger issue: nodes can refuse connection PoW for valid connections and then honest connectors can't reuse that across the next connection. If the PoW is tied to transaction content and a recent block hash only, if my peer denies me, I can turn around and try to send it yo someone else for no extra work. If PoW is connection-based, I can be DoS'<clipped messag     

> __< j​effro256:monero.social >__ sd just trying to make a connection     

> __< b​oog900:monero.social >__ true but they would need a large share of the reachable network addresses to pull off that attack, right?     

> __< d​oedl...:zano.org >__ cx timer ?     

> __< a​rticmine:monero.social >__ I believe there are better alternatives such as higher pricing in node relay for the targeted transactions     

> __< j​berman:monero.social >__ Fees don't help because the txs are invalid     

> __< j​effro256:monero.social >__ Like how the spy nodes are current ~1/2 of the reachable nodes on the network?     

> __< b​oog900:monero.social >__ They only make up like 15% of the outbound connections. Also if we took 50% at face value this "only" doubles the PoW, which should be relatively cheap anyway     

> __< j​effro256:monero.social >__ A timer doesn't help in this scenario. In this scenario that I'm talking about, the node that is presenting the challenge / validating the PoW dishonestly fails verification and refuses to open a connection. Thus the honest challengee / worker must trash that PoW and try another connection, where the same thing may happen     

> __< g​ingeropolous:monero.social >__ otoh, if someone wants to build hardware to dos tor, they could then turn and dos monero (if we use equi-x for this). Then again, same applies to randomx in general i guess.     

> __< j​berman:monero.social >__ right, if we go with Equi-X, we are also in an idirect way increasing the incentive to construct an ASIC to DoS tor     

> __< a​rticmine:monero.social >__ Yes I get it     

> __< b​oog900:monero.social >__ like it could cause some disruption, needing to compute more PoW, as your node connects to the network but once it has connections it should be fine.     

> __< b​oog900:monero.social >__ Also this would presumably remove them from your address book, reducing there presence on the network     

> __< j​berman:monero.social >__ I don't follow this fully. Presumably dishonest nodes can hold connections for some time and then drop today, no?     

> __< j​effro256:monero.social >__ It increases PoW by 15% under the current environment, but in this future with PoW-based connections, there is now a novel incentive to accrue outgoing connections from other nodes, so the percentage of dishonest outgoing connections may rise     

> __< j​effro256:monero.social >__ Yeah but we don't need PoW to connect to nodes today     

> __< b​oog900:monero.social >__ I mean the incentive is already there IMO, but even if they did PoW is not expensive enough where this becomes a problem IMO     

> __< j​effro256:monero.social >__ This also has bad implications for transaction propagation times which is important for network stability     

> __< b​oog900:monero.social >__ I thought this would be better as once connections are made they have sometime before a new connection is made, however with PoW per tx you now need to do a RX hash every hop.     

> __< b​oog900:monero.social >__ I guess that is only for big txs, but I still think this would have no impact on tx propagation     

> __< d​oedl...:zano.org >__ PoW may not be sufficient to protect nodes with 100's of incoming cx ...     

> __< j​effro256:monero.social >__ This is true. It would probably have better average-case performance, but worse worst-case performance     

> __< b​oog900:monero.social >__ what is the worse case for tx propagation in this scenario?     

> __< j​effro256:monero.social >__ Origin node is connected to many dishonest nodes at time of receiving the tx and makes new outgoing connections to propogate tx     

> __< b​oog900:monero.social >__ it should already have connections as it would do so on startup not when a tx comes in     

> __< b​oog900:monero.social >__ ohh wait they disconnected when the tx is sent     

> __< b​oog900:monero.social >__ currently this would just cause a fluff to all connections     

> __< b​oog900:monero.social >__ it is a black hole attack     

> __< b​oog900:monero.social >__ so as long as one is good the tx will propagate, I don't think this is any different than the current protocol     

> __< j​berman:monero.social >__ One other related comment to PoW by tx versus by connection: after serious optimization, let's ballpark that 128 input proofs will take 1 minute to construct, compared to 4-5s for 9 input proofs. We may want PoW for txs with 128 input proofs to be much higher than for 9 input proofs. In theory the initial connection could include some PoW that allows some upper bound on inputs to address this     

> __< j​effro256:monero.social >__ So we add state information and complicate the connection code even more than it already is. What if we want to relay someone else's high input tx? We can't do this with the connection cap     

> __< b​oog900:monero.social >__ I think just target the max allowed for simplicity, 1s to verify a 128-input tx, right? so a 1s PoW?     

> __< j​effro256:monero.social >__ If the PoW is per-tx, then we can add all these stricter requirements for bigger txs, and have the node simply relay the PoW alongside the tx w/ no issues     

> __< j​berman:monero.social >__ I was initially thinking keeping PoW proportional to prove time rather than verify so that dishonest actors are required to expend CPU time comparable to honest actors     

> __< d​oedl...:zano.org >__ what is the current enc/dec time ratio typical?     

> __< b​oog900:monero.social >__ honest users are still doing double the work tho     

> __< j​effro256:monero.social >__ Eh. I think we should just price in verification time since that's what we're trying to protect against     

> __< b​oog900:monero.social >__ as they need to create the tx + PoW     

> __< j​berman:monero.social >__ Very ballpark estimates, high end machine, 1 input - 128 inputs     

> __< j​berman:monero.social >__ Verification: ~20ms - 2s     

> __< j​berman:monero.social >__ Prove: ~1s - 5 minutes     

> __< j​effro256:monero.social >__ What do you mean by enc/dec ?     

> __< j​berman:monero.social >__ I assumed they meant prove/verify     

> __< j​berman:monero.social >__ Going off verify is fine with me     

> __< d​oedl...:zano.org >__ I ttied to figure out: how many dishonest nodes does is take to overpower 1 honest node with "valid" tx's.     

> __< d​oedl...:zano.org >__ *tried     

> __< j​berman:monero.social >__ does "valid" mean invalid?     

> __< b​oog900:monero.social >__ We might even be able to go less, PoW per connection means for an attacker PoW per (connection + bad tx), whereas PoW per tx is just PoW per tx.     

> __< b​oog900:monero.social >__ Meaning with 1 lot of bad PoW an attacker can send it to multiple nodes.     

> __< r​ucknium:monero.social >__ What do you mean by "overpower"?     

> __< d​oedl...:zano.org >__ black marble style     

> __< d​oedl...:zano.org >__ just keeping them busy     

> __< j​effro256:monero.social >__ A black marble attack is an attack on decoy selection for ring signatures     

> __< j​effro256:monero.social >__ It's a privacy issue, not a DoS issue     

> __< d​oedl...:zano.org >__ call it a different name, a load estimate.     

> __< d​oedl...:zano.org >__ but thats what testnet is for, innit?     

> __< r​ucknium:monero.social >__ Given that the meeting's length is potentially deep into record-breaking territory, maybe PoWER can come up for discussion next week. And in the meantime, people can comment on the `research-lab` issue.     

> __< j​berman:monero.social >__ I don't mind switching to Equi-X considering minimal support from anyone else for RandomX light     

> __< j​berman:monero.social >__ Going to keep thinking on the per connection vs per tx argument     

> __< j​berman:monero.social >__ oh and also will change the description to making PoW comparable to verify rather than prove     

> __< j​effro256:monero.social >__ For the record, I like RandomX for TX PoW since the daemon already has a RandomX scratchpad loaded for block verification. IDK how complicated the Equi-X algo is, but if it's anywhere on the level of RandomX, I would prefer to not add the dependency when we have an excellent PoW algo as-is     

> __< j​effro256:monero.social >__ But yeah, I'm fine with continuing this later     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thank you everyone.     

> __< s​packle:monero.social >__ thanks, all     

> __< j​effro256:monero.social >__ Thanks everyone! (I am now hydrated)     

> __< d​oedl...:zano.org >__ the higher the prove/verify time ratio, the higher the gain in network security. That was my point.     

> __< d​oedl...:zano.org >__ bye     

> __< j​berman:monero.social >__ a dishonest actor can create invalid txs in 0 time (aka prove would take 0s), whereas honest prove takes much much longer     

> __< a​rticmine:monero.social >__ But the verify time is finite hence the DDOS attack vector     

> __< d​oedl...:zano.org >__ maybe I got something fundamentally wrong here. But either way, a challenge/response system could get the job done. Sorry to sidetrack.     

> __< k​ayabanerve:matrix.org >__ Shouldn't nodes locally adjust their targets as their proof verification queue fills? Wouldn't that somewhat handle publication of a large batch?     

> __< j​berman:monero.social >__ https://github.com/monero-project/research-lab/issues/133#issuecomment-3109508587     

> __< midipoet >__ "There are like 400 distinct proofs of the Pythagorean Theorem." << after all that scroll back, this is just about all that i managed to comprehend from that MRL meeting today.      

> __< s​yntheticbird:monero.social >__ within these 400 distinct proofs of Pythagorean Theorem. 2% are actually useful, 31% are made bored mathematicians and 67% are made by students that needs to present some last year  work     

> __< s​yntheticbird:monero.social >__ by bored*     

> __*__ midipoet distinctly decides _not_ to apply this newly garnered knowledge regarding Pythagorus' theorem to the divisor's proof malarky     



# Action History
- Created by: Rucknium | 2025-07-22T21:33:15+00:00
- Closed at: 2025-07-31T20:08:41+00:00
