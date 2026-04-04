---
title: 'Research meeting: 19 August 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/499
author: SarangNoether
assignees: []
labels: []
created_at: '2020-08-17T13:12:06+00:00'
updated_at: '2020-08-19T18:00:24+00:00'
type: issue
status: closed
closed_at: '2020-08-19T18:00:23+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 19 August 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-08-19T18:00:23+00:00
    [2020-08-19 13:00:00] <sarang> All righty then
    [2020-08-19 13:00:06] <sarang> Let's begin our meeting
    [2020-08-19 13:00:19] <sarang> The usual agenda: https://github.com/monero-project/meta/issues/499
    [2020-08-19 13:00:27] <sarang> As always, logs will be posted there after the meeting
    [2020-08-19 13:00:34] <sarang> First, greetings!
    [2020-08-19 13:00:35] <sarang> hi
    [2020-08-19 13:00:41] <endogenic> ullo
    [2020-08-19 13:01:02] — sarang will wait a couple of minutes for others to arrive
    [2020-08-19 13:01:28] <Isthmus> holup can't find my goggles
    [2020-08-19 13:01:49] ⇐ v1docq47[m] quit (~v1docq47m@89.113.140.59): Ping timeout: 265 seconds
    [2020-08-19 13:01:58] <sarang> safety first
    [2020-08-19 13:02:21] <Isthmus> Oh, under the bed, of course...
    [2020-08-19 13:02:21] <Isthmus> /me puts on goggles and lab coat
    [2020-08-19 13:02:24] <Isthmus> Okay, let's roll
    [2020-08-19 13:02:53] <endogenic> nice hair
    [2020-08-19 13:03:10] — Isthmus closes webcam cover
    [2020-08-19 13:03:26] <sarang> OK, next up is the roundtable, where anyone can share research topics of interest
    [2020-08-19 13:03:33] <sarang> Does anyone wish to go first?
    [2020-08-19 13:04:49] <endogenic> sarang first
    [2020-08-19 13:04:53] <sarang> If not, I have a few items to share
    [2020-08-19 13:04:55] <endogenic> sarang is all you need
    [2020-08-19 13:05:19] <sarang> I'm in discussion with an ISO-affiliated standards committee in the U.S. regarding blockchain-based privacy
    [2020-08-19 13:05:27] <sgp_> hello
    [2020-08-19 13:05:41] <sarang> The goal is to provide accurate technical information about the field
    [2020-08-19 13:05:51] <sarang> More on that as it develops, I suppose
    [2020-08-19 13:05:55] <endogenic> interesting
    [2020-08-19 13:06:04] <sarang> I made some small updates to Arcturus/Triptych code for better storage efficiency
    [2020-08-19 13:06:16] <endogenic> sounds like formalizations of traceability and taint etc will he useful
    [2020-08-19 13:06:17] <endogenic> be
    [2020-08-19 13:06:24] <sarang> Reviewed a delightful Triptych article by the outreach workgroup that I look forward to seeing posted
    [2020-08-19 13:06:38] <sarang> Got a few PRs out the door relating to transaction proofs and message signing
    [2020-08-19 13:06:44] → sdsdsd joined (4131268e@65.49.38.142)
    [2020-08-19 13:06:56] <sarang> One PR, for key encryption, was reverted since its tests were not properly capturing necessary functionality
    [2020-08-19 13:07:15] <sarang> Anyone who happened to test this will find that their wallets work just fine after the reversion (or prior to applying the PR)
    [2020-08-19 13:07:28] <sarang> Thanks to selsta for identifying this problem
    [2020-08-19 13:07:42] <sarang> And finally, I have working proof-of-concept Bulletproofs+ code
    [2020-08-19 13:07:51] <sarang> Initially, the weighted inner product proving system
    [2020-08-19 13:08:04] <sarang> Additionally, aggregated range proofs and a more efficient recursion-unrolled verifier
    [2020-08-19 13:08:18] <endogenic> love that you are doing that code :P
    [2020-08-19 13:08:20] <sarang> That's progressing quite nicely and working precisely as intended
    [2020-08-19 13:08:34] <sarang> I'm working out the full batched BP+ stuff in stages, as I did for BP and some related projects
    [2020-08-19 13:08:41] <sarang> Thanks endogenic!
    [2020-08-19 13:08:47] <endogenic> can i ask again if it'd help to have a coder at your side to do your bidding?
    [2020-08-19 13:08:58] <sarang> I expect to have the full Python-based batch stuff soon, after which migrating to C++ should be straightforward as well
    [2020-08-19 13:09:17] <sarang> endogenic: certainly, as I'm sure there are small optimizations in C++ that would be helpful
    [2020-08-19 13:09:23] <sarang> I should be at that point in a few days
    [2020-08-19 13:09:36] <sarang> Anyway, that's my update
    [2020-08-19 13:09:38] <endogenic> i found the coder-theorist pair almost overpowered in the past
    [2020-08-19 13:09:46] <sarang> I'm happy to take questions on any of these topics
    [2020-08-19 13:11:26] <sarang> Does anyone else wish to share research of interest?
    [2020-08-19 13:12:24] <ArticMine> Amy further thoughts on te risk vs return between  Arcturus and Triptych. I mean tx size vs the newness for  Arcturus?
    [2020-08-19 13:13:13] <sarang> I don't know a good way to assess the practical risk of the nonstandard assumption in Arcturus
    [2020-08-19 13:13:40] <sarang> A reviewer seems to stand by their assertion that the assumption is unsafe, though I disagree with their claimed break
    [2020-08-19 13:13:51] <sarang> and they did not provide any follow-up details beyond standing by their assertion
    [2020-08-19 13:14:03] <sarang> I'll post the claimed break shortly
    [2020-08-19 13:14:26] <sarang> I believe they did not properly read the definition
    [2020-08-19 13:15:32] <sarang> (I intended to post this earlier, but it completely slipped my mind)
    [2020-08-19 13:16:26] <EmmanuelLagos> curious to learn more about how the assumption is unsafe and the consequences that the reviewer imagines....
    [2020-08-19 13:16:44] <sarang> The definition for the assumption has a few conditions on it
    [2020-08-19 13:17:13] <sarang> and it appears that the reviewer's claimed break doesn't apply to all of them (which is precisely why there are multiple conditions)
    [2020-08-19 13:17:39] <sarang> The follow-up response was something like "this can be extended" but with no details
    [2020-08-19 13:18:04] <EmmanuelLagos> ha that is not terribly helpful
    [2020-08-19 13:18:12] <EmmanuelLagos> looking forward to reading the updated later
    [2020-08-19 13:18:14] <EmmanuelLagos> thanks
    [2020-08-19 13:18:18] <sarang> I think the reviewer misread the final condition, which is subtly (but importantly) different than the others
    [2020-08-19 13:18:28] <sarang> But if there is a problem, I certainly want to know
    [2020-08-19 13:18:36] <sarang> this is the point of preprints and review!
    [2020-08-19 13:19:07] <ArticMine> Are there any other opinions on this?
    [2020-08-19 13:19:30] <ArticMine> I know this is real tough
    [2020-08-19 13:20:07] <sarang> It is tricky
    [2020-08-19 13:20:17] <sarang> This is why I hope for a reduction to a known hardness assumption
    [2020-08-19 13:20:24] <sarang> but haven't been able to produce one
    [2020-08-19 13:20:30] ⇐ sdsdsd quit (4131268e@65.49.38.142): Ping timeout: 245 seconds
    [2020-08-19 13:20:37] <sarang> Anyway, I'll post the reviewer's comments shortly
    [2020-08-19 13:20:47] <sarang> (after this meeting; need to hunt down the email)
    [2020-08-19 13:20:47] <ArticMine> Thanks so much
    [2020-08-19 13:20:53] <sarang> np
    [2020-08-19 13:21:30] <Isthmus> Nice work as always :- )
    [2020-08-19 13:21:44] <sarang> Many thanks!
    [2020-08-19 13:21:54] <sarang> Does anyone else wish to share research topics?
    [2020-08-19 13:23:19] <Isthmus> I have a quick update and a quick half-baked question
    [2020-08-19 13:24:05] <Isthmus> Regarding the update, have switched gears to formal documentation. I find this exciting! Instead of "X algo breaks Y feature" we're actually showing step-by-step how mechanism Y could be subverted.
    [2020-08-19 13:24:17] <sarang> Nice!
    [2020-08-19 13:24:22] <Isthmus> Maybe have draft ready for public feedback next week
    [2020-08-19 13:24:29] <Isthmus> It's fun to see the play-by-play attacks imho
    [2020-08-19 13:24:30] <sarang> Super excited to read it :)
    [2020-08-19 13:24:43] <sarang> To clarify, this assumes a hypothetical future quantum adversary?
    [2020-08-19 13:24:45] <endogenic> that's been missing for a while
    [2020-08-19 13:25:00] <Isthmus> No idea about the timeline
    [2020-08-19 13:25:06] <Isthmus> Just looking at the algorithms
    [2020-08-19 13:25:17] <Isthmus> Timeline for building QCs out of scope of research
    [2020-08-19 13:25:32] <sarang> Right, I just mean that such attacks are considered infeasible given current known technology?
    [2020-08-19 13:25:43] <sarang> (to avoid unnecessary FUD and maintain only necessary FUD...)
    [2020-08-19 13:25:55] — Isthmus won't be baited into speculating about the timelines since I don't know about private research
    [2020-08-19 13:26:09] <Isthmus> Given PUBLIC technology, definitely infeasible right now
    [2020-08-19 13:26:15] <sarang> I don't intend to have anyone speculate about quantum computing
    [2020-08-19 13:26:29] <sarang> Thanks :)
    [2020-08-19 13:26:52] <sarang> Great point about focusing on algorithms, and not specific computing ability
    [2020-08-19 13:27:17] <hyc> regardless of public or private research, it's clear that current QC-resistant algos are infeasible on current tech
    [2020-08-19 13:27:34] <sarang> Well, that's part of this research, no?
    [2020-08-19 13:27:36] <hyc> nobody is going to run a network using megabyte+ keys etc...
    [2020-08-19 13:27:41] <sarang> Looking at current research and directions?
    [2020-08-19 13:27:42] <endogenic> challenge accepted
    [2020-08-19 13:28:02] <ArticMine> The question I see is given that this is possible some unknown time in the future, what are the possible mitigations?
    [2020-08-19 13:28:07] <hyc> * infeasible on current classical computers
    [2020-08-19 13:29:43] <hyc> the only machines capable of running QC-resistant algos will be large servers. adopting QC-resistant algos will thus kill decentralization
    [2020-08-19 13:29:54] <sarang> Isthmus: out of sheer curiosity, do you know of any other major projects looking into post-QC vulnerability in this level of detail?
    [2020-08-19 13:30:29] <sarang> I agree with hyc that any proposed post-QC mitigations would need to be balanced against practical considerations, as would any changes
    [2020-08-19 13:30:44] <sarang> but that seems not to be the primary goal of this work, from how I read it
    [2020-08-19 13:31:16] <sarang> Having a better understanding of the areas of the protocol that would be vulnerable is useful
    [2020-08-19 13:31:25] <sarang> as is understanding where research stands today, and where it's headed
    [2020-08-19 13:31:39] <Isthmus> RE other projects, AFAIK Monero is leading the pack for pq-privacy research.
    [2020-08-19 13:31:39] <sarang> But this certainly isn't speaking for Isthmus and his team
    [2020-08-19 13:31:43] <Isthmus> Quantum Resistant Ledger has pq-security mechanisms but no privacy mechanisms.
    [2020-08-19 13:31:45] <sarang> Nice :)
    [2020-08-19 13:31:56] <Isthmus> There have been some papers on Bitcoin, but they tend to only look at 1-2 algorithms, nowhere near the comprehensive treatment that we're executing
    [2020-08-19 13:32:01] <sarang> Yeah, I know of QRL but it seems not widespread at this point in terms of popularity or use?
    [2020-08-19 13:32:32] <sarang> I met one of the QRL leads at a conference, in fact
    [2020-08-19 13:32:32] <Isthmus> They're leaning hard into some cool researh
    [2020-08-19 13:32:46] <Isthmus> ZK-lattice, STARKs, and pq-signature aggregation
    [2020-08-19 13:32:48] <sarang> Isthmus: any good resources on that in particular?
    [2020-08-19 13:32:59] <sarang> I haven't looked into their specific tech in a while (the conference was a while back)
    [2020-08-19 13:33:19] <Isthmus> The QRL whitepaper is actually a pretty easy read and nice summary of security attack surfaces and possible approaches
    [2020-08-19 13:33:30] <midipoet> Isthmus: might be a silly question but will there be a report from the work you are doing?
    [2020-08-19 13:33:32] ← azy left (~azy@unaffiliated/stev3): 
    [2020-08-19 13:34:18] <Isthmus> Side note, https://github.com/theQRL/Whitepaper/blob/master/QRL_whitepaper.pdf
    [2020-08-19 13:34:26] <sarang> Thanks Isthmus
    [2020-08-19 13:34:27] <Isthmus> ^ white paper
    [2020-08-19 13:34:37] <Isthmus> Interestingly, they're moving towards RandomX which is about the only pq-secure part of Monero
    [2020-08-19 13:34:46] <hyc> lol
    [2020-08-19 13:35:24] <sarang> :D
    [2020-08-19 13:35:27] <sarang> I did not know that
    [2020-08-19 13:36:58] <Isthmus> Yea, they follow MRL research
    [2020-08-19 13:37:05] <sarang> cool
    [2020-08-19 13:37:06] — Isthmus waves
    [2020-08-19 13:37:31] <Isthmus> Anyways, that's about all from me. Technical details next week ^_^
    [2020-08-19 13:37:35] <sarang> Great, thanks
    [2020-08-19 13:37:42] <sarang> Any other topics to be discussed today?
    [2020-08-19 13:37:45] <sarang> Or questions?
    [2020-08-19 13:38:13] <midipoet> sarang: any updates on the ISO?
    [2020-08-19 13:38:20] <midipoet> Sorry if I missed these...
    [2020-08-19 13:38:32] <sarang> midipoet: I have not heard back from the person who handles the logistics
    [2020-08-19 13:38:37] <sarang> but I did speak with the chairperson
    [2020-08-19 13:39:34] <sarang> He sent along invitations to relevant meetings, and indicated that participating before completing the paperwork should not be a problem 
    [2020-08-19 13:39:41] <sarang> given the delays that might occur
    [2020-08-19 13:40:56] <hyc> sounds good
    [2020-08-19 13:43:01] <sarang> OK, let's move on to action items, where anyone can share their research plans for the next week or so
    [2020-08-19 13:43:22] <sarang> I'll complete BP+ proof-of-concept code with full batching, and then move to a C++ implementation for timing data and comparison
    [2020-08-19 13:43:40] <sarang> and post the claimed Arcuturus hardness assumption break
    [2020-08-19 13:43:53] <Isthmus> Oh wait, I still had a question (bout non pq stuff)
    [2020-08-19 13:44:01] <sarang> Oh go ahead Isthmus
    [2020-08-19 13:44:11] <Isthmus> https://usercontent.irccloud-cdn.com/file/609yOFnf/image.png
    [2020-08-19 13:44:23] → ErCiccione joined (~ErCiccion@gateway/tor-sasl/erciccione)
    [2020-08-19 13:44:31] <Isthmus> https://usercontent.irccloud-cdn.com/file/WkDekAar/image.png
    [2020-08-19 13:44:38] <Isthmus> https://usercontent.irccloud-cdn.com/file/DVzt3Gr6/image.png
    [2020-08-19 13:44:59] <Isthmus> Raw version for those not afraid of Google: https://docs.google.com/document/d/1TBICG6RFoeTOv-Yn9HEOHvWgSdx2NOtGZ1ckvG9VT8w/edit?usp=sharing
    [2020-08-19 13:45:16] <sarang> please explain
    [2020-08-19 13:45:24] <Isthmus> Stuff in yellow is not expected to be cryptographically random/uniform/etc.
    [2020-08-19 13:45:53] <Isthmus> Stuff in green should be all noise, right
    [2020-08-19 13:46:07] <Isthmus> No repetition/collisions, etc. No patterns if I comb through, etc.
    [2020-08-19 13:46:13] <Isthmus> Correct?
    [2020-08-19 13:46:15] <sarang> But?
    [2020-08-19 13:47:03] <Isthmus> I don't have the `but` yet, just asking whether that is the correct expectation
    [2020-08-19 13:47:29] <sarang> BP data is expected to be uniform across proofs for different commitments, yes
    [2020-08-19 13:48:02] <sarang> It's certainly possible to generate non-uniform signature scalars in a valid signature
    [2020-08-19 13:48:31] — Isthmus nods
    [2020-08-19 13:48:32] <sarang> I assume you're identifying something suggesting non-uniformity?
    [2020-08-19 13:49:04] <sarang> Note for BPs that AFAIK nothing stops commitment reuse...
    [2020-08-19 13:49:15] <sarang> and that's not _necessarily_ dangerous
    [2020-08-19 13:49:19] <sarang> but certainly nonstandard
    [2020-08-19 13:50:16] <sarang> FWIW all but one signature scalar in MLSAG (and CLSAG) is signer-selected and arbitrary
    [2020-08-19 13:50:26] <sarang> You can absolutely have a valid signature with terrible scalars
    [2020-08-19 13:50:47] <Isthmus> Haven't identified anything yet, still in the hypothesis generation and experiment design phase.
    [2020-08-19 13:50:48] <Isthmus> Essentially we will hypothesize that certain fields should be uniform/random/non-colliding, and then look for counterexamples
    [2020-08-19 13:50:53] <sarang> ok
    [2020-08-19 13:51:06] <sarang> It's probably important to separate what's signer-controlled and what isn't
    [2020-08-19 13:51:15] <Isthmus> ^^
    [2020-08-19 13:51:20] <sarang> e.g. almost all MLSAG/CLSAG scalars are signer controlled
    [2020-08-19 13:51:26] <sarang> the same is not the case for BP
    [2020-08-19 13:51:36] <Isthmus> Oh yea, I need 3 categories, not 2 colors
    [2020-08-19 13:51:46] <sarang> So the MLSAG scalars _should be_ random, but don't _need_ to be
    [2020-08-19 13:51:58] <sarang> there's additional layers to BP
    [2020-08-19 13:52:29] <Isthmus> 1) signer controlled, expect patterns (e.g. lock time)
    [2020-08-19 13:52:29] <Isthmus> 2) signer controlled, but should be random (e.g. MLSAG scalar)
    [2020-08-19 13:52:29] <Isthmus> 3) output of cryptographic fxn, expected no patterns (e.g. proof outputs)
    [2020-08-19 13:52:53] <sarang> Interestingly, there was an idea to use a hash function for MLSAG/CLSAG to allow for data hiding or signer identification of the signing index
    [2020-08-19 13:53:03] <sarang> This would, if implemented, help avoid the case of a bad PRNG
    [2020-08-19 13:53:08] <sarang> but can't be enforced, of course
    [2020-08-19 13:53:53] <Isthmus> Ooh that's interesting
    [2020-08-19 13:54:07] <sarang> Yeah, I have some example proof-of-concept code for it
    [2020-08-19 13:54:41] <sarang> You use a hash function for all the signer-controlled scalars, and the remaining one is uniformly distributed
    [2020-08-19 13:54:56] <sarang> The signer can use this to later recover the signing index, but this isn't public
    [2020-08-19 13:55:05] <sarang> it's a cool idea
    [2020-08-19 13:55:37] <Isthmus> Sweet.
    [2020-08-19 13:55:39] <Isthmus> Okay, that's all for today then, I'll work on formalizing and splitting stuff up into the 3 buckets.
    [2020-08-19 13:55:44] <sarang> Great!
    [2020-08-19 13:55:52] <sarang> Any other action items, questions, or the like?
    [2020-08-19 13:56:49] <sarang> If not, we are adjourned!
    [2020-08-19 13:56:53] <sarang> Thanks to everyone for joining
    [2020-08-19 13:56:57] <sarang> Logs will be posted shortly


# Action History
- Created by: SarangNoether | 2020-08-17T13:12:06+00:00
- Closed at: 2020-08-19T18:00:23+00:00
