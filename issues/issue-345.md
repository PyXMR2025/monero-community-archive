---
title: 'Research meeting: 20 May 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/345
author: SarangNoether
assignees: []
labels: []
created_at: '2019-05-20T00:39:09+00:00'
updated_at: '2019-05-20T18:11:01+00:00'
type: issue
status: closed
closed_at: '2019-05-20T18:11:00+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 20 May 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-05-20T18:11:00+00:00
    [2019-05-20 13:00:34] <suraeNoether> allright everyone
    [2019-05-20 13:00:39] <suraeNoether> welcome to our weekly research meeting
    [2019-05-20 13:00:47] <suraeNoether> sarang is a bit behind this morning, but we'll begin anyhow
    [2019-05-20 13:00:57] <suraeNoether> agenda is here
    [2019-05-20 13:00:58] <suraeNoether> https://github.com/monero-project/meta/issues/345
    [2019-05-20 13:01:07] <suraeNoether> we'll begin with: GREETINGS!
    [2019-05-20 13:01:54] <suraeNoether> howdy everyone, I'm surae
    [2019-05-20 13:02:10] <suraeNoether> anyone else here?
    [2019-05-20 13:02:22] <sarang> Hi, sorry to be late
    [2019-05-20 13:02:26] <sarang> Preparing for travel today
    [2019-05-20 13:03:16] <sarang> How's it going, all?
    [2019-05-20 13:03:36] <suraeNoether> i feel like a roundtable requires more than two people, otherwise it may be more like a linetable amiright
    [2019-05-20 13:03:51] — moneromooo here but nothing interesting to say
    [2019-05-20 13:04:06] <sarang> Eh, no worries. Plenty to catch up on
    [2019-05-20 13:04:13] — moneromooo wants to hear about CLSAG improvements though ^_^
    [2019-05-20 13:04:16] <sarang> Let's move on to roundtable anyway
    [2019-05-20 13:04:22] <sarang> May I go first, with a few tiny things?
    [2019-05-20 13:04:27] <sarang> Then plenty of CLSAG talk
    [2019-05-20 13:04:33] <suraeNoether> fire away brother
    [2019-05-20 13:04:41] <sarang> Neato
    [2019-05-20 13:05:04] <sarang> I'm working with the author of the output-flooding paper so he can get new results using correct network assumptions
    [2019-05-20 13:05:18] <sarang> I've been working on the CLSAG proofs/definitions with suraeNoether (more on that to follow)
    [2019-05-20 13:05:31] <sarang> Assisting hyc et al. with the RandomX audit logistics and planning
    [2019-05-20 13:05:43] <sarang> And a bit more (but not much more) work on the MoJoin scheme
    [2019-05-20 13:05:51] <sarang> That is all!
    [2019-05-20 13:05:58] <sarang> Any questions on those prior to suraeNoether's update?
    [2019-05-20 13:06:24] <moneromooo> I suppose the "not much more" means there's no solution yet for a values ?
    [2019-05-20 13:06:35] <sarang> Not without some trust in the dealer (or a designated player)
    [2019-05-20 13:07:02] <sarang> And now, on to suraeNoether 
    [2019-05-20 13:07:40] <suraeNoether> well, I spent this week writing a new definition of unforgeability for linkable ring signature schemes for the clsag paper, and reading updates on the dlsag paper
    [2019-05-20 13:07:54] <sarang> That CLSAG definition is surprisingly subtle
    [2019-05-20 13:08:25] <suraeNoether> clsag is looking like a 15-20% reduction in rate of growth of blockchain size, 15-20% improvement in verification speed, and we are formally proving signer ambiguity in a way that I think hasn't been done yet
    [2019-05-20 13:08:27] <sarang> To sum up the earlier work, what remains on the proofs in your opinion? (I'll be reviewing its current state today on an aeroplane)
    [2019-05-20 13:08:58] <suraeNoether> the only proof that remains right now is the proof for signer ambiguity and reducing it to the DDH problem
    [2019-05-20 13:09:09] <suraeNoether> but i think it may be another weird variant like k-one-more DDH
    [2019-05-20 13:09:17] <sarang> Eh, even so
    [2019-05-20 13:09:17] <suraeNoether> our unforgeability reduces to k-one-more discrete logarithm, for example
    [2019-05-20 13:09:22] <sarang> yup
    [2019-05-20 13:09:36] <suraeNoether> there has been a back and forth between sarang, myself, and randomrun on the final proof and the utility of the colored coins section
    [2019-05-20 13:09:42] <sarang> RandomRun mentioned a possibility for shifting the auxiliary key over to the other side of the hash
    [2019-05-20 13:09:52] <sarang> key(s)
    [2019-05-20 13:10:01] <sarang> (in the case of multi-type colored transactions)
    [2019-05-20 13:10:02] <suraeNoether> oh yeah, he also noticed a way to aggregate all these dummy key images and it's possible he just made it even freaking smaller
    [2019-05-20 13:10:13] <sarang> I'm not totally convinced of this just yet
    [2019-05-20 13:10:21] <suraeNoether> i want it to be true
    [2019-05-20 13:10:24] <sarang> Heh
    [2019-05-20 13:10:44] <sarang> But essentially classifying the signing and aux keys by their linkability status is interesting
    [2019-05-20 13:10:45] <suraeNoether> oh, also, i have printed the new ringct3.0 paper that was put on IACR this morning, and i imagine that will be a big topic of conversation at this informal monero workshop sarang and I are meeting up at
    [2019-05-20 13:11:00] <sarang> Yes, it uses a Bulletproofs-style proving system
    [2019-05-20 13:11:14] <sarang> and, if correct, is an honest-to-goodness trustless ring signature transaction system
    [2019-05-20 13:11:29] <sarang> Link: https://eprint.iacr.org/2019/508
    [2019-05-20 13:11:49] <suraeNoether> at this point, we have a handful of sublinear ring signature proposals and proving systems on the table for upgrading to Monero 2.0
    [2019-05-20 13:11:57] <suraeNoether> i don't think "electric bugaloo" translates to esperanto well
    [2019-05-20 13:12:08] <suraeNoether> but that's sort of what I would like to come out of MRL over the next 6-9 months
    [2019-05-20 13:12:57] <sarang> What do we all think about the CLSAG timeline, realistically speaking?
    [2019-05-20 13:13:07] <sarang> Presumably we'd be freezing for Carbon Crab in August
    [2019-05-20 13:13:19] <sarang> If we desire to get CLSAG audited, that's additional time
    [2019-05-20 13:13:51] <sarang> I would prefer to release the paper draft as soon as we have the proofs done (and before adding in other extra goodness, like multi-type transactions)
    [2019-05-20 13:14:49] <suraeNoether> well, everything is proven except a single theorem in an appendix, so i'd be comfortable releasing a draft of it today with "DRAFT" plastered all over it, presuming you and randomrun are cool with that
    [2019-05-20 13:15:16] <suraeNoether> i think it's possible that after you read the appendix, youare of the opinon that the proof is unnecessary, but i'd rather err on the side of having it and removing it rather than excluding it
    [2019-05-20 13:15:37] <sarang> That's a great timeline
    [2019-05-20 13:15:47] <suraeNoether> either way, i can't imagine the draft will not be finished before the end of the monero workshop this week, and if we are going to get it audited, we should move on that sooner rather than later
    [2019-05-20 13:16:01] <sarang> It would be nice to get it in for Carbon Crab, but better to wait if it would mean rushing
    [2019-05-20 13:16:22] <sarang> Such an audit would likely be fairly cheap, since the base code changes are quite minimal and straightforward
    [2019-05-20 13:16:34] <suraeNoether> actually
    [2019-05-20 13:17:14] <suraeNoether> i feel like the clsag change is far-reaching, and the scope of an audit could be... well, let's talk about that
    [2019-05-20 13:17:33] <sarang> How so? There are two sides: the math, and the implementation
    [2019-05-20 13:17:47] <suraeNoether> well, consider implementing bulletproofed range proofs
    [2019-05-20 13:17:55] <suraeNoether> drop-in replacement for a little black box that sits inside our code
    [2019-05-20 13:17:55] <sarang> The basic signature functions (and their underlying crypto changes) amount to surprisingly little
    [2019-05-20 13:18:10] <sarang> and you can almost trace line-by-line the changes from MLSAG
    [2019-05-20 13:18:35] <suraeNoether> except it's not for a single small drop-in black box part of a bigger machine
    [2019-05-20 13:18:49] <sarang> It almost is
    [2019-05-20 13:18:50] <suraeNoether> it *is* the machine, in a certain sense
    [2019-05-20 13:19:02] <sarang> Well, that'd be up to an auditor to gauge the complexity of
    [2019-05-20 13:19:18] <suraeNoether> i'm not arguing against an audit, i'm merely wondering aloud about the scope
    [2019-05-20 13:19:21] <sarang> At any rate, once we're confident in it, I can contact some reviewers to get estimates
    [2019-05-20 13:19:35] <sarang> I'd say from the transaction model (full vs simple) onward
    [2019-05-20 13:19:49] <sarang> So, once you hit where MLSAG is directly called, the scope ends
    [2019-05-20 13:20:08] <sarang> This tests whether the security is at _least_ as good as MLSAG
    [2019-05-20 13:20:23] <sarang> Anyway, that's more of a future discussion TBH
    [2019-05-20 13:20:32] <suraeNoether> well, we're going to need more formal specifications for CLSAG for use in such an audit either way, and i agree it's water not yet under this bridge
    [2019-05-20 13:20:57] <sarang> Any other intriguing work to share suraeNoether ?
    [2019-05-20 13:21:08] <sarang> The workshop will certainly bring many more interesting things to the next meeting
    [2019-05-20 13:22:04] <suraeNoether> MRL11 has seen no progress since last week due to the time crunch of clsag and dlsag, but it's a really high priority for me due to the privacy of our users
    [2019-05-20 13:22:19] <suraeNoether> i'd love to put signature scheme downs and work on sims
    [2019-05-20 13:22:30] <sarang> Well, an action item is surely to get CLSAG pushed out for more review
    [2019-05-20 13:22:53] <suraeNoether> yes
    [2019-05-20 13:24:04] <sarang> I shall have to leave momentarily to head to an aeroport
    [2019-05-20 13:24:10] <suraeNoether> any questions for me or sarang?
    [2019-05-20 13:24:23] <sarang> But my action items are to get CLSAG finished up, and continue working on that output flooding data... as well as the workshop this week
    [2019-05-20 13:27:15] <moneromooo> If that new rct3.0 system uses BPs, presumably it lends itself well to multiexps, and then gets to be faster too (pro rata) ?
    [2019-05-20 13:27:25] <moneromooo> ie, still linear, but nice constants ?
    [2019-05-20 13:28:01] <sarang> Possibly
    [2019-05-20 13:28:11] <sarang> There may be issues with generators
    [2019-05-20 13:29:32] <suraeNoether> moneromooo: i'm very excited to compare rct3.0 with a super secret paper sarang and i have been reading for a week or so
    [2019-05-20 13:29:33] <sarang> At least for batching
    [2019-05-20 13:29:53] <suraeNoether> personally i like having more than one sample of similar techniques because it makes it seem like generalizing is easier
    [2019-05-20 13:29:55] <suraeNoether> anyway
    [2019-05-20 13:30:02] <moneromooo> Ah, the secret rct.3.14159 paper...
    [2019-05-20 13:30:16] <suraeNoether> fractional ring sizes are the future
    [2019-05-20 13:30:30] <suraeNoether> differentiable signatures are also the future
    [2019-05-20 13:30:43] <suraeNoether> the future of today's tomorrow... yesterday.^tm
    [2019-05-20 13:31:00] <moneromooo> One could say... differentiable signatures are integral to the future ?
    [2019-05-20 13:31:41] <suraeNoether> damn
    [2019-05-20 13:31:48] <suraeNoether> moneromooo is the best of us
    [2019-05-20 13:32:05] <moneromooo> In stupid puns at least.
    [2019-05-20 13:32:11] <suraeNoether> okay, since sarang has to take off for el aeropuerto and i, also, need to pack
    [2019-05-20 13:32:23] <suraeNoether> i say we bring today's meeting to a close
    [2019-05-20 13:32:39] <suraeNoether> i'll see some of you in person tonight and tomorrow. :P

# Action History
- Created by: SarangNoether | 2019-05-20T00:39:09+00:00
- Closed at: 2019-05-20T18:11:00+00:00
