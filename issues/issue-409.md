---
title: 'Research meeting: 12 November 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/409
author: SarangNoether
assignees: []
labels: []
created_at: '2019-11-09T23:14:31+00:00'
updated_at: '2019-11-12T17:44:17+00:00'
type: issue
status: closed
closed_at: '2019-11-12T17:44:16+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Tuesday, 12 November 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-11-12T17:44:16+00:00
    [2019-11-12 10:58:38] <sarang> Hello all
    [2019-11-12 10:58:55] <sarang> Meeting begins presently
    [2019-11-12 10:59:43] <sgp_> hello
    [2019-11-12 10:59:49] <sarang> First, GREETINGS
    [2019-11-12 11:00:15] <sgp_> darn, beat you to it :)
    [2019-11-12 11:02:08] <sarang> Next up, ROUNDTABLE
    [2019-11-12 11:02:10] <suraeNoether> howdy :D
    [2019-11-12 11:02:22] <suraeNoether> sarang how about you go first
    [2019-11-12 11:02:59] <sarang> I backported the RCT3 exploit fix from the multi-input aggregated proving system to the single-input prover, updated code to reflect this, and checked the relevant security proofs for this construction
    [2019-11-12 11:03:52] <sarang> Also went through some math on ways to support multisignatures securely on the sublinear protocols under consideration, with no good answers
    [2019-11-12 11:04:36] <sarang> As of now, the constructions for RCT3, Omniring, and Triptych all require an output secret key inversion, which is incompatible with the linear-combination method used for doing multisignatures
    [2019-11-12 11:05:11] <sarang> This only comes up for RCT3 and Triptych in the key image generation step, but it's still unfortunate
    [2019-11-12 11:05:40] <suraeNoether> i was reading about some signature schemes that don't use hash functions and do use key inversion the other day... when i review your stuff on triptych soundness later today, i'll see if there is anythingt obvious that jumps out at me
    [2019-11-12 11:05:56] <sarang> Thanks
    [2019-11-12 11:06:07] <suraeNoether> i would assume it's not obvious because you and randomrun are both v diligent
    [2019-11-12 11:06:30] <sarang> A few things are still in progress too
    [2019-11-12 11:06:56] <sarang> Regardless of multisignature support, I'm working up a preprint on Triptych for IACR eprint
    [2019-11-12 11:07:15] <sarang> It'll either be the provably-secure single-signer version, or the multi-signer version if the soundness argument works out
    [2019-11-12 11:08:08] <sarang> It'll include the same PRF-based key image construction as found in RCT3 and Omniring, since that's much more efficient than one based on hashing public keys
    [2019-11-12 11:09:02] <sarang> Now passing the baton to suraeNoether 
    [2019-11-12 11:09:41] <suraeNoether> cool, so for our traceability analysis, i'm collecting data now. i presented some preliminary results from a *single* simulation yesterday that were rather promising, but can't be generalized yet
    [2019-11-12 11:09:59] <sarang> Is the code for those results currently pushed to your repo?
    [2019-11-12 11:10:19] <suraeNoether> indeed, all you do is run playerchallenger.py with python3 and simulation results will be spit out
    [2019-11-12 11:10:38] <sarang> Can you provide the branch and commit for that version, to be sure we're running the same code?
    [2019-11-12 11:10:39] <suraeNoether> of course, the results will vary from simulation to simulation so the precise numbers i provided yesterday will change from simulation to simulation
    [2019-11-12 11:10:42] <sarang> right
    [2019-11-12 11:10:59] <suraeNoether> https://github.com/b-g-goodell/mrl-skunkworks/tree/matching-buttercup/Matching is the present up to date everything
    [2019-11-12 11:11:33] <sarang> Got it, thanks
    [2019-11-12 11:11:37] <suraeNoether> the code isn't complete in a lot of ways (there are always ways to make the weighting scheme selected by Eve to be better and to take into account more data), but it's complete enough to start doing some data analysis to get some hard numbers on churn
    [2019-11-12 11:11:57] <sgp_> How can I configure it to test with different churn parameters?
    [2019-11-12 11:12:02] <suraeNoether> i am currently modifying the code to specifically investigate churn, which requires some changes to the very front end of my simulations; i don't expect it to be done today
    [2019-11-12 11:12:07] <suraeNoether> ^ heh
    [2019-11-12 11:12:13] <sgp_> ok, so stay tuned
    [2019-11-12 11:12:14] <sarang> I'm seeing commit d5076 as most recent
    [2019-11-12 11:12:45] <suraeNoether> indeedindeed, d5076 is most common
    [2019-11-12 11:13:00] <sarang> roger, thanks
    [2019-11-12 11:14:03] <suraeNoether> i think MRL-churn-numbers will have some more satisfying answers later this week
    [2019-11-12 11:14:18] <suraeNoether> other than that: catching up on the RCT, omni, and triptych work that sarang has been doing
    [2019-11-12 11:14:32] <suraeNoether> that's all i have. OH my work report and stuff like that :P
    [2019-11-12 11:15:30] <scoobybejesus> fingers crossed my question makes sense
    [2019-11-12 11:15:36] <scoobybejesus> sarang> This only comes up for RCT3 and Triptych in the key image generation step  <<< could the logistics be made to work such that signing a tx still happens via linear-combination but key image is derivable independently by multisig members?
    [2019-11-12 11:16:11] <sarang> We'd need a secure MPC for the function J(x) = (1/x)*U
    [2019-11-12 11:16:19] <sarang> If there is such a thing, it's all ok
    [2019-11-12 11:16:46] <sarang> (here U is a globally fixed curve group generator)
    [2019-11-12 11:17:50] <sarang> I'm trying to find the paper where that particular PRF was first introduced
    [2019-11-12 11:19:40] <sarang> Cited from Omniring (reference 20): https://www.iacr.org/cryptodb/archive/2005/PKC/3320/3320.pdf
    [2019-11-12 11:23:14] <sarang> Anything else to share or discuss from anybody?
    [2019-11-12 11:23:30] <sarang> Besides me both liking and disliking that particular pseudorandom function =p
    [2019-11-12 11:24:28] <suraeNoether> Just compute the logarithm then add ;)
    [2019-11-12 11:25:24] <sarang> But for real, an MPC for that function based on linear combinations would solve the multisig problem AFAICT
    [2019-11-12 11:25:44] <sarang> It may not be possible while retaining its nice PRF properties
    [2019-11-12 11:25:55] <sarang> (perhaps there's a formal argument that such an MPC couldn't exist)
    [2019-11-12 11:26:51] <suraeNoether> Slightly more seriously: why not compute the inverse of the product of the private keys and instead of a partial sum on the basepoint being passed around, a partial product on the basepoint is passed around...
    [2019-11-12 11:27:26] <suraeNoether> If I have x and you have y, let the combined key be 1/(xy) U
    [2019-11-12 11:28:53] <sarang> If you take away the affine nature of the composite key, I don't see a way to make that work cleanly with the rest of the proof
    [2019-11-12 11:29:10] <sarang> nor do I immediately see what partial key image data would be passed around to construct the full image
    [2019-11-12 11:29:41] <suraeNoether> I send you (1/x)U. You multiply by 1/y...
    [2019-11-12 11:29:55] <suraeNoether> So it's not just an mpc you need but specifically a linear function of the input keys...
    [2019-11-12 11:30:54] <sarang> Perhaps. I was thinking in the context of linear key combinations initially (since the rest of the proofs play nicely with that)
    [2019-11-12 11:31:19] <sarang> The current multisig works nicely because everything plays nicely with linear combinations
    [2019-11-12 11:32:33] <sarang> But point taken that if it were possible to relax that restriction, it could be quite compelling
    [2019-11-12 11:33:12] <sarang> The only point in Triptych and RCT3 that requires the use of a full private key (outside of key image construction) is at the end of the proofs, to construct a particular masked scalar
    [2019-11-12 11:33:39] <suraeNoether> Hmm
    [2019-11-12 11:34:06] <suraeNoether> Ok well I am going to continue reading on triptych and I will try to make a push later today to mess with churn number in my simulations for sgp_
    [2019-11-12 11:34:15] <sarang> Righto
    [2019-11-12 11:34:27] <sarang> Let me know if you have any additional thoughts on multisig/MPC constructions too
    [2019-11-12 11:35:36] <sarang> Oh, and here's a neat paper that came out recently for doing composable zk proofs in a Python library: https://arxiv.org/abs/1911.02459
    [2019-11-12 11:36:01] <sgp_> thanks suraeNoether. I'm interested in testing your model out
    [2019-11-12 11:38:10] <sarang> So perhaps on to ACTION ITEMS now?
    [2019-11-12 11:38:36] <sarang> Mine are to wrap up the Triptych formalization to a preprint as much as possible, while considering options for secure MPC
    [2019-11-12 11:38:53] <sarang> and then I want to do a deeper review of suraeNoether's recent work on his simulation code
    [2019-11-12 11:39:05] <sarang> (and clear a backlog of lit review)
    [2019-11-12 11:40:06] <suraeNoether> My big backlog for matching at  this point is commenting it and documenting how it works for anyone who wants to pick it up
    [2019-11-12 11:40:25] <suraeNoether> But other than that, I am reading today and doing my work reoorts


# Action History
- Created by: SarangNoether | 2019-11-09T23:14:31+00:00
- Closed at: 2019-11-12T17:44:16+00:00
