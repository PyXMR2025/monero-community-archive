---
title: 'Research meeting: 26 August 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/385
author: SarangNoether
assignees: []
labels: []
created_at: '2019-08-22T20:44:48+00:00'
updated_at: '2019-08-26T17:31:51+00:00'
type: issue
status: closed
closed_at: '2019-08-26T17:31:50+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 26 August 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [CLSAG paper](https://eprint.iacr.org/2019/654) submission, [PR 5707](https://github.com/monero-project/monero/pull/5707), proving systems, [SBC 2020](https://cbr.stanford.edu/sbc20/)
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-08-26T17:31:50+00:00
    [2019-08-26 09:59:32] <sarang> All righty!
    [2019-08-26 09:59:36] <sarang> Let's begin our meeting
    [2019-08-26 09:59:40] <sarang> Agenda: https://github.com/monero-project/meta/issues/385
    [2019-08-26 09:59:46] <sarang> Logs will be posted there after the meeting
    [2019-08-26 09:59:52] <sarang> GREETINGS
    [2019-08-26 10:00:16] → OSNF2P joined (~OsrsNeeds@CPEf0f249490513-CMf0f249490510.cpe.net.cable.rogers.com)
    [2019-08-26 10:00:57] <rehrar> hi
    [2019-08-26 10:00:58] — sarang waits a bit
    [2019-08-26 10:01:04] <parasew[m]> hello
    [2019-08-26 10:01:21] <suraeNoether> good morning
    [2019-08-26 10:02:13] <sarang> Let's move to ROUNDTABLE
    [2019-08-26 10:02:19] <sarang> suraeNoether: care to go first?
    [2019-08-26 10:02:46] <suraeNoether> sure, last week I made a commit to my buttercup branch with some matching algorithm fixes, which is now operating as far as i can tell 100% smoothly
    [2019-08-26 10:03:02] <sarang> Nice! Looking forward to reviewing it
    [2019-08-26 10:03:16] <suraeNoether> i also have the framework for a markov chain simulator of a basic ledger almost ready to push later today, which we will be using to identify best practices while churning, etc
    [2019-08-26 10:03:52] <suraeNoether> in addition to that, I discovered a discrete distribution over the weekend that could be very helpful in working with output selection
    [2019-08-26 10:04:19] <suraeNoether> that's pretty much it. not tremendously eventful, except the matching algo unit tests
    [2019-08-26 10:05:13] <sarang> Will be neat to see if we can adjust output selection to such a distribution efficiently and robustly
    [2019-08-26 10:05:24] <sarang> Low priority in the grand scheme of things, but intriguing nonetheless
    [2019-08-26 10:06:01] <sarang> I am finishing preparation of the CLSAG paper for submission to Financial Cryptography 2020
    [2019-08-26 10:06:11] <hyc> definitely, will be nice to have some exploration of churning that we can document
    [2019-08-26 10:06:29] <sarang> PR 5707 has been updated to simplify the hashing code
    [2019-08-26 10:06:40] <suraeNoether> oh, sarang and i decided we should also submit the thring signature paper to FinCrypt2020 also, sort of doubling our chances (but not really, it's nonlinear :P)
    [2019-08-26 10:06:53] <sarang> Note that this removes `hashToPointSimple` and moves its functionality directly into the relevant unit test
    [2019-08-26 10:07:32] <sarang> `hashToPointSimple` is only used to produce a Pedersen generator, but it's brittle on arbitrary input and not useful elsewhere
    [2019-08-26 10:07:58] <sarang> (unless we updated how we do hash-to-points to use an iterated index, but this is not backwards-compatible)
    [2019-08-26 10:08:13] <sarang> Additional eyes on PR 5707 would be welcome
    [2019-08-26 10:08:31] <sarang> And: Stanford announced the dates and CFP of their next blockchain conference
    [2019-08-26 10:08:48] ⇐ MalMen quit (~malmen@188.250.74.185): Ping timeout: 245 seconds
    [2019-08-26 10:08:49] <sarang> TBH it's probably not worth our time to submit a paper/presentation, given their acceptance rate
    [2019-08-26 10:09:09] <sarang> Unless anyone has an idea for something something zero knowledge ethereum =p
    [2019-08-26 10:09:18] <sarang> I kid, I kid
    [2019-08-26 10:09:23] <suraeNoether> *cough*
    [2019-08-26 10:09:25] <suraeNoether> but not
    [2019-08-26 10:09:53] <hyc> lol
    [2019-08-26 10:09:55] <sarang> Finally, I continue analysis work on proving systems
    [2019-08-26 10:10:15] <suraeNoether> 5707 is for how the second basepoint in our pedersen commitments are selected. if i recall from my conversation with sarang earlier, this PR will make the monero codebase slightly more robust, less brittle, more consistent with the way it works, and more importantly *more easily verified to be correct* by new users, even though it's a relatively small change
    [2019-08-26 10:10:28] <sarang> RingCT3.0 is exploitable in its current form, but I'm told a forthcoming fix likely solves the problem (unclear if provably at this point) with little impact on efficiency
    [2019-08-26 10:10:43] <sarang> suraeNoether: the change only makes it harder to use the wrong hashing method :)
    [2019-08-26 10:11:18] <sarang> and enables slightly more efficient hash-to-point operations under some constructions
    [2019-08-26 10:11:51] <sarang> Anyway, a new preprint (IACR/944) discusses a new proving system for more general constraint systems
    [2019-08-26 10:12:27] <sarang> And there will be a forthcoming preprint with a proving system on pairing groups, which simplifies cleanly to non-pairing groups too
    [2019-08-26 10:12:46] <sarang> I've been looking over that one, since the authors graciously provided an advance copy
    [2019-08-26 10:13:35] <sarang> What will be interesting is whether the Omniring prover relations can be efficiently moved into a more general proving system
    [2019-08-26 10:13:47] <sarang> Making it easier (in theory) to do future changes
    [2019-08-26 10:14:12] <kenshamir[m]> Could you comment on the computational complexity when you simplify the proving system to a non-pairing group?
    [2019-08-26 10:14:21] <sarang> Eventually =p
    [2019-08-26 10:14:28] <sarang> I've only just begun working through that paper
    [2019-08-26 10:14:42] <sarang> FWIW I'm told the preprint is quite imminent
    [2019-08-26 10:14:43] <kenshamir[m]> Ahh alright, any idea when it will be released?
    [2019-08-26 10:14:48] <sarang> ^^
    [2019-08-26 10:15:47] <sarang> Oh and suraeNoether: the primary purpose of 5707 is to speed up MLSAG by removing redundant operations... this led to simplifications of the available hashing operations as a side effect
    [2019-08-26 10:16:23] <suraeNoether> thanks for correcting that! i didn't realize the larger scope (just started going through it)
    [2019-08-26 10:16:24] <sarang> and at that point it seemed like a good idea to remove the brittle `hashToPointSimple` and put it directly into the unit test that enables verification of how `H` was derived
    [2019-08-26 10:16:36] <sarang> There are two commits: the second commit moves the hash stuff around
    [2019-08-26 10:16:41] <sarang> the first commit alters the MLSAG code
    [2019-08-26 10:16:45] <suraeNoether> gotcha
    [2019-08-26 10:17:10] <sarang> All righty
    [2019-08-26 10:17:20] <sarang> Does anyone else wish to share interesting research work?
    [2019-08-26 10:17:45] <rehrar> :/ if I were that smart, sure
    [2019-08-26 10:18:09] <sarang> Don't underestimate yourself!
    [2019-08-26 10:18:26] <sarang> While we're at it, we can also do GENERAL QUESTIONS for anyone
    [2019-08-26 10:18:38] <rehrar> well, I did read a recent paper on hormesis as it relates to beetles.
    [2019-08-26 10:18:46] <sarang> lol
    [2019-08-26 10:19:00] <rehrar> my skills are not going to be helpful here :P
    [2019-08-26 10:19:53] <hyc> oh, you just reminded me of that stream of tweets from Sarah Jamie Lewis yesterday, about ants and alarm pheromones
    [2019-08-26 10:20:12] <sarang> Regarding CLSAG, the plan is to submit to several relevant conferences/journals (in sequence) and hope for acceptance
    [2019-08-26 10:20:32] <hyc> the relevance was to illustrating how localized decision making can be gamed / subverted
    [2019-08-26 10:20:37] <sarang> It falls into an awkward spot: it's a neat improvement on earlier work with good security model/proofs, but isn't profoundly new
    [2019-08-26 10:20:54] <sarang> And unfortunately you can't do simultaneous submissions :/
    [2019-08-26 10:21:10] <hyc> (and thus an argument why you need global consensus)
    [2019-08-26 10:21:22] <sarang> The FC deadline is in September, with notification by November 15
    [2019-08-26 10:21:54] <hyc> lots of stuff isn't profoundly new, but the imporvement still is worth talking about
    [2019-08-26 10:22:10] <sarang> Yeah, but that's tough for publication
    [2019-08-26 10:22:40] <hyc> maybe different forums then. heck, chip manufacturers give big presentations on ~5-10% gains
    [2019-08-26 10:22:47] <sarang> Hence doing a fair bit of rewriting for better context
    [2019-08-26 10:23:28] <hyc> cool. yes, expanding the scope of applicability is also a good angle
    [2019-08-26 10:23:53] <sarang> and page limits (grumble grumble stupid wide margins)
    [2019-08-26 10:24:20] <sarang> Aaaaanyway
    [2019-08-26 10:24:25] <sarang> Perhaps on to ACTION ITEMS
    [2019-08-26 10:24:55] <sarang> I have several, and I don't expect to complete them all this week
    [2019-08-26 10:25:10] <sarang> CLSAG revisions, in preparation for submission
    [2019-08-26 10:25:47] <sarang> My doctoral adviser always recommended putting down a paper for a week after your revisions, so you can revisit it with fresh eyes before submission
    [2019-08-26 10:26:12] <sarang> Second is a better understanding of the reduction of this forthcoming proving system to non-pairing groups
    [2019-08-26 10:26:24] <sarang> Third is going over suraeNoether's completed matching code
    [2019-08-26 10:27:23] <sarang> Since suraeNoether had to step away for a few minutes, I assume his action items are applications of his test-passing matching code, and preparation of the thring signature paper for its submission (he can correct me later)
    [2019-08-26 10:28:04] <sarang> Any last comments or questions or information from anyone?
    [2019-08-26 10:29:27] <sarang> OK, we can adjourn! Thanks to everyone for joining in
    [2019-08-26 10:29:35] <sarang> Logs will be posted shortly to the agenda issue


# Action History
- Created by: SarangNoether | 2019-08-22T20:44:48+00:00
- Closed at: 2019-08-26T17:31:50+00:00
