---
title: 'Research meeting: 21 October 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/402
author: SarangNoether
assignees: []
labels: []
created_at: '2019-10-18T17:54:35+00:00'
updated_at: '2019-10-21T17:43:08+00:00'
type: issue
status: closed
closed_at: '2019-10-21T17:43:08+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 21 October 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-10-21T17:43:08+00:00
    [2019-10-21 13:04:43] <suraeNoether> Greetings everyone!
    [2019-10-21 13:05:36] <suraeNoether> My work this past week has been fruitful. Right now I'm running simulations. These are not data collection simulations yet, but if they pass testing,  then I'm making a final push my repo and then data collection will begin and I'll be getting *literal answers* later this afternoon.
    [2019-10-21 13:05:46] <suraeNoether> this is the matching/churn project
    [2019-10-21 13:06:41] <sarang> Nice
    [2019-10-21 13:06:49] <suraeNoether> in addition to that, sarang asked yesterday: do we care more about space or time when it comes to replacing signature schemes. luckily, we can literally quantify when it is worth switching to a new scheme
    [2019-10-21 13:07:03] <suraeNoether> Just to remind the audience, here is how that derivation goes
    [2019-10-21 13:07:17] <suraeNoether> Let's say we have two possible ways of encoding a database and verifying its contents.. Case I: Size of file is O(n) and time to verify file is O(n).  Case II: Size of file is O(log(n)) and time to verify file is O(n).
    [2019-10-21 13:07:38] <suraeNoether> When is it worth it to switch from Case I to Case II? In Case I, total download and verification time is a*n/c + b*n/v where a and b are constants, c is average download speed, and v is average verification speed (per bit)
    [2019-10-21 13:08:02] <suraeNoether> In Case II, total download and verification time is A*log(n)/C + B*n/V where A, B, C, and V are other constants, usually different than in Case I (although we can assume c = C for simplicity although often V != v)
    [2019-10-21 13:09:01] <suraeNoether> The total cost in time to download and verify implies that Case II is better than Case I if and only if (a/c) + (b/v) > B/V + (A/c)*(log(n)/n). To give you guys a rough idea, when n > 10^2, log(n)/n is smaller than 0.025, so this term drops pretty quickly
    [2019-10-21 13:09:29] <suraeNoether> Since log(n)/n tends toward zero, if n is remotely large (for a blockchain we are talking about large powers of 10... and n increases as time goes on), we require a/c + b/v > B/V for this ever to be at least asymptotically a good idea to switch, and we realize that asymptotic bound pretty quickly
    [2019-10-21 13:10:42] <suraeNoether> we can run timing tests on some schemes for to estimate ballpark values of a, b, c, v, B, and V (I suspect b = B but a != A...)
    [2019-10-21 13:11:10] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Quit: Leaving
    [2019-10-21 13:11:40] <suraeNoether> (these derivations are why we haven't *yet* switched to a sublinear scheme, by the way!)
    [2019-10-21 13:12:46] <sarang> Well, that and not having a clear winner in terms of overall efficiency+soundness
    [2019-10-21 13:13:18] <sarang> Different constructions don't necessarily scale the same way with transaction input/output structure
    [2019-10-21 13:13:33] <sarang> The logarithmic size scaling is for the size of the specified anonymity set, overall
    [2019-10-21 13:13:45] <sarang> How they handle multiple inputs/outputs makes a difference
    [2019-10-21 13:14:32] <suraeNoether> indeed, all the above is very generalized and specific formulations for specific schemes are required... besides, *none* of the above assumes batching
    [2019-10-21 13:15:16] <suraeNoether> although batching can be approximated by tweaking the parameters b, v, B, and V, it's still just a ballpark back of napkin thing
    [2019-10-21 13:16:35] <sarang> This past week I've worked on a few things
    [2019-10-21 13:17:09] <sarang> First, the IACR/2019/944 optimized IPA verifier was added to kenshamir[m]'s Rust implementation and benchmarked, showing no improvement over the Bulletproofs IPA
    [2019-10-21 13:17:27] <sarang> We sent a note to the authors to share our results and get some clarification on the results from their paper
    [2019-10-21 13:17:53] <sarang> But it definitively answers the question of how useful it would be in practice to use the updated verifier (answer: it wouldn't be)
    [2019-10-21 13:18:11] <mikerah> Do you have a link to @kenshamir's rust crate?
    [2019-10-21 13:18:42] <sarang> https://github.com/kenshamir/qesa
    [2019-10-21 13:19:02] <sarang> I also have Triptych balance proving working
    [2019-10-21 13:19:15] → kico joined (~kico@gateway/tor-sasl/kico)
    [2019-10-21 13:19:15] <sarang> and have completed a writeup of the algorithms
    [2019-10-21 13:19:28] <sarang> Now I'm putting correctness proofs in, which is tedious due to the algebra
    [2019-10-21 13:19:50] <sarang> There were some other modifications for efficiency too, which will need to be examined for soundness
    [2019-10-21 13:20:37] <sarang> Also of note is that last week, a side-channel issue with subaddresses was reported and examined
    [2019-10-21 13:21:12] <sarang> We discussed a fix that would essentially add a Schnorr representation proof to outputs
    [2019-10-21 13:21:38] <sarang> I'm told there is a blog post and corresponding Breaking Monero episode ready to go that describe this
    [2019-10-21 13:22:49] <sarang> This week, I plan to continue work on Triptych proofs: correctness, soundness, zero knowledge
    [2019-10-21 13:23:03] → fullmetalScience joined (~fullmetal@213.152.161.211)
    [2019-10-21 13:23:15] <sarang> Back to you suraeNoether 
    [2019-10-21 13:23:35] <suraeNoether> This week, my action items include posting my funding request for the next quarter, assisting sarang with the soundness proof of triptych, and to actually answer some questions about churn with some rigor
    [2019-10-21 13:24:19] ⇐ fullmetalScience quit (~fullmetal@213.152.161.211): Client Quit
    [2019-10-21 13:24:29] <sarang> Anyone have questions, or other interesting research to share?
    [2019-10-21 13:24:43] <suraeNoether> the work i've put into the infrastructure of this project has paid off, because the actual script running the tests is around 30 lines. the rest of the code is writing output to file etc
    [2019-10-21 13:25:08] <suraeNoether> (the library i wrote is 700 lines with 1200 lines of tests iirc but who counts lines anyway)
    [2019-10-21 13:25:37] — suraeNoether watches Eve weight her graph with increased interest, eye twitching.
    [2019-10-21 13:26:17] <sarang> I'll be interested to see what level of support there is (or is not) for the Schnorr proof modification to avoid the subaddress side-channel attack
    [2019-10-21 13:27:17] <mikerah> I want to pass some ideas by you all around minimal smart contracts on monero.
    [2019-10-21 13:27:23] <sarang> ok
    [2019-10-21 13:27:51] <mikerah> The idea is to use FHE with a DSL to then store in the extra tx_data field of monero transactions
    [2019-10-21 13:28:04] <sarang> DSL?
    [2019-10-21 13:28:15] <mikerah> The main problem with this is that there isn't any actual enforcement of the smart contract logic
    [2019-10-21 13:28:22] <mikerah> DSL = Domain Specific Language
    [2019-10-21 13:28:59] <sarang> It's tricky because ring signatures are, by definition, signer-ambiguous
    [2019-10-21 13:29:36] <sarang> Meaning more complex spend conditions typically don't play nicely with that
    [2019-10-21 13:30:13] → monerobby joined (~monerobby@c-67-173-117-200.hsd1.il.comcast.net)
    [2019-10-21 13:30:38] <mikerah> yeah, agreed. Has anyone looked into bringing the DLSAG construct into production?
    [2019-10-21 13:31:13] <suraeNoether> DLSAG currently has some key image formatting problems :\
    [2019-10-21 13:31:17] <sarang> Not that I know of... its scaling is still linear with the ring size, and it has a tracing problem that hasn't been solved
    [2019-10-21 13:31:22] <suraeNoether> also ^
    [2019-10-21 13:33:52] <sarang> Right, any other questions or comments before we adjourn?
    [2019-10-21 13:34:26] <mikerah> https://eprint.iacr.org/2019/1229.pdf
    [2019-10-21 13:34:33] <mikerah> Has anyone had time to skim that?
    [2019-10-21 13:34:44] <mikerah> It's the new supersonic scheme by BBS
    [2019-10-21 13:34:47] <sarang> Ah yes, I gave it the most cursory of glances
    [2019-10-21 13:35:08] <suraeNoether> it uses groups of unknown order, which is a fun but weird concept that is also used in VDFs
    [2019-10-21 13:35:30] → Coupe420 joined (~Coupe420@170.55.14.86)
    [2019-10-21 13:35:42] <sarang> Even so, with certain instantiations, they estimated 7 kB or so for a 1 million-gate circuit (of some structure that I don't recall)
    [2019-10-21 13:35:46] <mikerah> My issue with constructs using groups of unknown order is what happens if a smart kid finds the order of the group?
    [2019-10-21 13:38:08] <sarang> The hardness assumption has to do with element order IIRC
    [2019-10-21 13:38:15] <sarang> among other hardness assumptions they require
    [2019-10-21 13:38:37] <sarang> Anyway, it's interesting and applicable to different proving systems
    [2019-10-21 13:39:15] * thrmo_ → thrmo
    [2019-10-21 13:41:12] <sarang> OK, I'm gonna get back to work typesetting some correctness proofs
    [2019-10-21 13:41:16] <sarang> Thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2019-10-18T17:54:35+00:00
- Closed at: 2019-10-21T17:43:08+00:00
