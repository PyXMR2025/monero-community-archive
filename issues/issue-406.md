---
title: 'Research meeting: 4 November 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/406
author: SarangNoether
assignees: []
labels: []
created_at: '2019-10-31T23:07:40+00:00'
updated_at: '2019-11-06T14:57:22+00:00'
type: issue
status: closed
closed_at: '2019-11-06T14:57:22+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 4 November 2019 @ 17:00 UTC
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
## SarangNoether | 2019-11-06T14:57:22+00:00
    [2019-11-04 12:03:50] <suraeNoether> GREETINGS!
    [2019-11-04 12:04:11] <suraeNoether> I'm surae, I'm a taurus maybe, and i like long walks on the beach with high probability
    [2019-11-04 12:04:57] <sarang> Hi
    [2019-11-04 12:05:42] <suraeNoether> anyone else here?
    [2019-11-04 12:06:15] <suraeNoether> well, public logs will be posted of this meeting either way, so anyone who missed it can find the logs online
    [2019-11-04 12:06:27] ⇐ Dean_Guss quit (~dean@gateway/tor-sasl/deanguss): Remote host closed the connection
    [2019-11-04 12:06:57] <suraeNoether> okay, well, sarang, would you like to start?
    [2019-11-04 12:07:03] <sarang> Sure
    [2019-11-04 12:07:10] <sarang> I've been working on a few things...
    [2019-11-04 12:07:16] → Dean_Guss joined (~dean@gateway/tor-sasl/deanguss)
    [2019-11-04 12:07:26] <sarang> More Triptych work, on math/proof for single inputs, which are fine
    [2019-11-04 12:07:49] <sarang> This includes some CLSAG-style key aggregation and more efficient key images
    [2019-11-04 12:07:56] <sarang> (more on multi-input in a sec)
    [2019-11-04 12:08:04] <sarang> Also gave a talk on transaction protocols
    [2019-11-04 12:08:22] <sarang> And looked at using the existing transaction proofs to mitigate the Janus subaddress attack
    [2019-11-04 12:08:47] <sarang> As to multi-input Triptych, this link is to the Overleaf paper: https://www.overleaf.com/read/ncqsdsydxvjv
    [2019-11-04 12:08:53] <sarang> (multi.tex)
    [2019-11-04 12:09:02] <sarang> The problem with witness extraction is the last equation on page 7
    [2019-11-04 12:09:45] <suraeNoether> you and arthur are planning on submitting for peer review, yes?
    [2019-11-04 12:09:59] <sarang> We could, once/if the proofs work out for multi-input
    [2019-11-04 12:10:14] <sarang> We want to show that for every spent input M, H(M) = r*J
    [2019-11-04 12:10:27] <sarang> where J is the key image
    [2019-11-04 12:10:32] <sarang> and M = rG
    [2019-11-04 12:11:31] <sarang> What we instead show is that a sum of the form \sum_u (\mu_u * H(M_u)) = \sum_u (witness_u J_u)
    [2019-11-04 12:11:53] <suraeNoether> do you have your talk powerpoint up on your github?
    [2019-11-04 12:11:57] <suraeNoether> by chance
    [2019-11-04 12:11:58] <sarang> yes
    [2019-11-04 12:12:26] <sarang> It's also the case that the sum of all witness_u is equal to the witness found for the signing key check
    [2019-11-04 12:12:33] <sarang> Two equations above that one
    [2019-11-04 12:13:05] <suraeNoether> found it: https://github.com/SarangNoether/talks :P
    [2019-11-04 12:13:09] <sarang> I don't see a good line of reasoning to show why such a witness extraction would be equivalent to the honest generation of those key image
    [2019-11-04 12:13:29] <suraeNoether> i'm taking a look now.
    [2019-11-04 12:13:38] <suraeNoether> that shouldn't discourage anyone else from looking tho
    [2019-11-04 12:13:55] <sarang> (you have to swap the two sums in the last equation to get something of the form that's two equations above, but that's fine)
    [2019-11-04 12:14:07] <suraeNoether> janus mitigation right now is extra schnorr signatures, right?
    [2019-11-04 12:14:33] <sarang> Yes, but you can use the existing transaction proof method, provided you check against a complete subaddress
    [2019-11-04 12:14:48] <sarang> It's still off-chain, but functionality that exists now
    [2019-11-04 12:15:11] <suraeNoether> very nice. iirc sgp_ wrote something on the janus vulnerability and made a blog post about it, or has a draft prepared. is that out or does it need updating or anything like that?
    [2019-11-04 12:15:27] ⇐ Dean_Guss quit (~dean@gateway/tor-sasl/deanguss): Remote host closed the connection
    [2019-11-04 12:15:50] <sarang> Probably, but I'd like someone else to confirm that tx proof verification does in fact require external input of the suspected subaddress
    [2019-11-04 12:15:59] → Dean_Guss joined (~dean@gateway/tor-sasl/deanguss)
    [2019-11-04 12:16:09] <sarang> and that it's not pulled from the proof string in any way, or otherwise influenced directly by the prover
    [2019-11-04 12:16:19] <sarang> (since the prover could simply use the Janus-modified subaddress)
    [2019-11-04 12:17:02] <sarang> For this witness extraction, I suspect that it may possible to show that each u-summand in the X-check is in fact equal to a particular r_u term
    [2019-11-04 12:17:22] <sarang> If that's the case, then we could easily show that the u-summand scalars in the Y-check are those _same_ r terms
    [2019-11-04 12:17:32] <suraeNoether> great, does anyone else have any other questions for sarang about his work on triptych, or his work on janus, or questions about his talk?
    [2019-11-04 12:19:07] <suraeNoether> well, my work this week has been on the matching code ( https://github.com/b-g-goodell/mrl-skunkworks/tree/matching-buttercup/Matching ) which has some peculiar failings right now
    [2019-11-04 12:19:36] <suraeNoether> my basic unit tests for graphtheory.py, which handles all the graph theoretic stuff, are passing. nodes and edges are added and deleted correctly, weighted correctly, matches are found, etc.
    [2019-11-04 12:20:31] <suraeNoether> but when i simulate a ledger with my simulator.py tool, the result misses some nodes and/or edges
    [2019-11-04 12:20:41] <suraeNoether> these aren't being caught lower down, but are being caught higher up
    [2019-11-04 12:21:04] <sarang> hmm
    [2019-11-04 12:21:36] <suraeNoether> so anyone with interest in python, graph theory, traceability, etc, can contribute by trying to figure out why my code isn't adding edges/nodes appropriately all the time. it's very bizarre behavior, and i'm sure it comes down to something ridiculous like my previous buffer problem
    [2019-11-04 12:21:58] <suraeNoether> but, i want to put it down for a few days since other folks in theory could help, and i have other things to do like help review triptych's proofs
    [2019-11-04 12:22:13] <sarang> That seems reasonable
    [2019-11-04 12:22:34] <sarang> Is it clear in the code (or errors) where the specific problems are?
    [2019-11-04 12:22:44] <sarang> i.e. if someone wishes to play around with it
    [2019-11-04 12:23:27] <suraeNoether> running sh tests.sh from the tools folder will auto detect all the tests and execute them; i've skipped all the tests i know are currently passing, so it'll go right into the brick wall immediately
    [2019-11-04 12:23:37] <sarang> got it
    [2019-11-04 12:23:57] <sarang> suraeNoether: if you're going to be on IRC this afternoon, we could dive into that witness extraction and see if we can't solve it
    [2019-11-04 12:24:08] <sarang> I have some ideas
    [2019-11-04 12:24:27] <suraeNoether> beyond that, i have a few papers i have begun reading, such as this one https://eprint.iacr.org/2019/1177.pdf on aggregation approaches, and a few others on interactive versions of concensus mechanisms like this one https://eprint.iacr.org/2019/1172.pdf
    [2019-11-04 12:24:41] <suraeNoether> sarang: i'm catching up on the triptych paper now and whiteboarding it
    [2019-11-04 12:24:53] <suraeNoether> if i go all pepe sylvia on the thing i may take a crazed picture for posterity
    [2019-11-04 12:25:07] <sarang> excellent reference
    [2019-11-04 12:25:22] <sarang> I'll add a few more lines to page 7 to show how the X and Y witnesses are related
    [2019-11-04 12:25:30] → Common-Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-11-04 12:25:35] <sarang> since that should come into play in the Y-soundness
    [2019-11-04 12:25:48] — suraeNoether https://www.youtube.com/watch?v=InbaU387Wl8
    [2019-11-04 12:26:19] <suraeNoether> so my action items today are: triptych whiteboarding, janus tx proof validation check (the external input issue you just mentioned)
    [2019-11-04 12:26:33] <sarang> great
    [2019-11-04 12:26:51] <suraeNoether> my action items immediately are to post my work report for last month and request funding for my next quarter, but i hate that and i much prefer coding and math so i'm finding myself v avoidant
    [2019-11-04 12:27:05] <sarang> For this week, I'd (ideally) like to figure out this soundness issue... if it's possible to do so, it provides a very interesting extension to this Groth proof scheme
    [2019-11-04 12:27:21] <suraeNoether> does anyone have any other research to advertise, or other questions for sarang or i?
    [2019-11-04 12:27:26] <sarang> and would make Triptych a competitive option for tx protocol
    [2019-11-04 12:28:29] <suraeNoether> it's such a great name
    [2019-11-04 12:28:34] <sarang> suraeNoether: here are some general notes on the witness structure for ya
    [2019-11-04 12:28:42] <suraeNoether> afk for about 10 minutes
    [2019-11-04 12:28:51] <suraeNoether> sarang ^ yes pls!
    [2019-11-04 12:28:52] ⇐ Common_Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Ping timeout: 264 seconds
    [2019-11-04 12:28:57] <sarang> The prover wants to show that it knows the discrete logs (r-terms, in notation) for each of the signing pubkeys (M terms)
    [2019-11-04 12:29:24] <sarang> so it knows a set of r (indexed by u different spends, no index here for clarity) such that M = rG for each one
    [2019-11-04 12:29:46] <sarang> it also wants to show that H(M) = rJ for each one, where each J is a key image provided by the prover
    [2019-11-04 12:30:04] <sarang> When done honestly, each J is defined such that J = (r^-1)*H(M)
    [2019-11-04 12:30:28] <sarang> In the soundness proof, the "X check" is for signing keys, and the "Y check" is for linking tags
    [2019-11-04 12:31:24] <sarang> X-soundness allows us to extract a witness (which involves certain Vandermonde-related coefficients) r1 such that r1*G = mu_1*M_1 + mu_2*M_2 + ...
    [2019-11-04 12:32:06] <sarang> and we claim (MuSig/CLSAG-style) that knowing this witness r1 implies knowledge of each of the r terms going into the right-hand sum
    [2019-11-04 12:32:48] <sarang> Ideally, for the Y-soundness, we want to extract a related witness that implies knowledge of the same r-terms that go into the linking tag identities
    [2019-11-04 12:33:30] <sarang> If you stare at the rightmost terms of the bottom equation and third-from-bottom equations on page 7, you can see the u-summands match up
    [2019-11-04 12:34:22] <sarang> If we can show (using the form of the Vandermonde coefficients, etc.) that each u-summand in the X-soundness corresponds properly to an r-value, we may be able to make a solid argument about using those same u-summands in the Y-soundness equation (since we need the _same_ r-values there)
    [2019-11-04 12:35:11] <sarang> The construction of the Vandermonde-related coefficients \theta_e is also discussed on page 7 (and can be found in the original Bootle paper's proof)
    [2019-11-04 12:35:17] <suraeNoether> back
    [2019-11-04 12:35:40] <sarang> This might get complicated, since rows of the Vandermonde matrix correspond to different F-S challenges :/
    [2019-11-04 12:35:47] — sarang is done talking now
    [2019-11-04 12:36:12] <sgp_> suraeNoether: yes, the blog post should be updated to include the mitigation
    [2019-11-04 12:36:17] <suraeNoether> hmmmm
    [2019-11-04 12:36:36] <suraeNoether> sgp_: can you link the post for the meeting logs pls?
    [2019-11-04 12:36:39] <sarang> sgp_: once it's been confirmed that the verifier externally provides the expected subaddress
    [2019-11-04 12:37:40] <suraeNoether> showing the correspondence like that has always been a sticking point :\
    [2019-11-04 12:38:27] <sgp_> https://getmonero.org/2019/10/18/subaddress-janus.html
    [2019-11-04 12:39:01] <sarang> suraeNoether: unless you can think of a good argument that having the same summand terms in both the X- and Y-witnesses is sufficient already
    [2019-11-04 12:39:21] <suraeNoether> well, i'll catch up and then i'll see what you mean by that. :P
    [2019-11-04 12:39:23] <sarang> e.g. we already claim that knowledge of that sum-witness in the X-portion is equivalent to knowledge of each discrete log
    [2019-11-04 12:39:25] <sarang> sure
    [2019-11-04 12:39:29] <suraeNoether> *nod*
    [2019-11-04 12:39:58] <sarang> Just remember that the key to the linking is that we show that the _same_ r-terms are used to construct the signing keys _and_ the corresponding linking keys
    [2019-11-04 12:40:12] <sarang> so having the same witnesses should come into play
    [2019-11-04 12:40:44] <sarang> It gets tricky because we don't directly show knowledge of each r-term, just the mu-weighted CLSAG-style combination
    [2019-11-04 12:41:11] <sarang> So I wonder if we in fact already have all the information we need to show this
    [2019-11-04 12:41:29] <sarang> and perhaps don't need to mess with those Vandermonde coefficients (which would be a huge pain to do)
    [2019-11-04 12:41:42] <suraeNoether> okay, does anyone else have any research to talk about, or questions for MRL, or requests/points to bring up/etc?
    [2019-11-04 12:42:04] <suraeNoether> otherwise we can adjourn the meeting and continue chatting about triptych outside of that context
    [2019-11-04 12:42:11] <sarang> roger


# Action History
- Created by: SarangNoether | 2019-10-31T23:07:40+00:00
- Closed at: 2019-11-06T14:57:22+00:00
