---
title: 'Research meeting: 23 December 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/422
author: SarangNoether
assignees: []
labels: []
created_at: '2019-12-20T00:14:50+00:00'
updated_at: '2019-12-23T17:32:22+00:00'
type: issue
status: closed
closed_at: '2019-12-23T17:32:22+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 23 December 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-12-23T17:32:22+00:00
    [2019-12-23 12:01:10] <suraeNoether> we'll start with GREETINGS. hiya!
    [2019-12-23 12:01:41] <suraeNoether> mele kalikimaka, etc
    [2019-12-23 12:02:34] <suraeNoether> let's move along to the ROUNTABLE
    [2019-12-23 12:02:54] <suraeNoether> i know isthmus has been up to some interesting stuff with block sizes and fees, but he doesn't appear to be here. sarang, as usual, has been busy. you want to start, sarang?
    [2019-12-23 12:03:23] <sarang> Sure
    [2019-12-23 12:03:45] <sarang> I redid the CLSAG linkability and non-frameability definitions, theorems, and proofs
    [2019-12-23 12:04:06] <sarang> and then did a major reorganization of the preprint for clarity and style/format
    [2019-12-23 12:04:20] <sarang> It's ready for suraeNoether's review, and then posting
    [2019-12-23 12:05:10] <sarang> Additionally, the Triptych preprint draft is ready for suraeNoether to review as well
    [2019-12-23 12:05:15] <sarang> and then it can be posted
    [2019-12-23 12:05:31] <sarang> good times
    [2019-12-23 12:05:39] <suraeNoether> word, word
    [2019-12-23 12:05:44] <suraeNoether> does anyone have any questions for sarang?
    [2019-12-23 12:06:55] <sarang> Apparently not!
    [2019-12-23 12:06:58] <mikerah[m]> I have a question for the MRL team regarding L2 scaling for Monero: Are there any scalability solutions currently deployed on Monero? If not, why not?
    [2019-12-23 12:07:14] <sarang> I assume you mean off-chain?
    [2019-12-23 12:07:24] <mikerah[m]> I do mean off-chain
    [2019-12-23 12:07:30] <suraeNoether> not currently deployed. DLSAG and thring signatures are two fundamental pieces of off-chain scaling
    [2019-12-23 12:07:45] <suraeNoether> DLSAG is currently... uhm... accepted for publication? did iirc?
    [2019-12-23 12:07:52] <sarang> Accepted to FC2020
    [2019-12-23 12:08:00] <suraeNoether> that's a spicy meatball, yes
    [2019-12-23 12:08:02] <sarang> Awaiting some likely rewrites for definitions
    [2019-12-23 12:08:31] <sarang> Downside is that indistinguishable refund-compatible transactions don't play nicely with key image requirements
    [2019-12-23 12:08:36] <suraeNoether> mikerah[m]: requires some more research into how to ensure consistency in key image use
    [2019-12-23 12:08:41] <suraeNoether> ^
    [2019-12-23 12:09:29] <mikerah[m]> So, the current state of the art for monero is DLSAG, thring signatures and the Tari sidechain?
    [2019-12-23 12:09:42] <suraeNoether> tari sidechain is independent
    [2019-12-23 12:09:44] <sarang> Tari is a separate project
    [2019-12-23 12:09:54] <suraeNoether> but built on top of monero, from my understanding
    [2019-12-23 12:09:59] <sarang> No
    [2019-12-23 12:10:06] <suraeNoether> er... sidechain
    [2019-12-23 12:10:15] <suraeNoether> not *on top of*
    [2019-12-23 12:10:15] <sarang> IIRC they're doing a MW-based implementation
    [2019-12-23 12:10:19] <suraeNoether> oh
    [2019-12-23 12:10:24] <suraeNoether> news to me *shrug*
    [2019-12-23 12:10:32] <sarang> Hoping to do merge mining
    [2019-12-23 12:10:46] <sarang> But I have not been following their recent work
    [2019-12-23 12:10:49] <suraeNoether> ah
    [2019-12-23 12:10:54] <mikerah[m]> <suraeNoether "news to me *shrug*"> Me too. I guess the association to fluffypony made me assume that it was Monero related
    [2019-12-23 12:11:25] <suraeNoether> well, for my part of the roundtable, my work this week was to start copy-editing triptych and clsag, and to work on my matching simulations. I just made a push this morning... https://github.com/b-g-goodell/mrl-skunkworks/tree/matching-buttercup/Matching
    [2019-12-23 12:11:47] <suraeNoether> anyone can run tracing.py and it will create a data folder, stash human-readable simulated monero transcripts inside...
    [2019-12-23 12:11:54] <sarang> mikerah[m]: to be clear, DLSAG is not deployed anywhere
    [2019-12-23 12:12:35] <mikerah[m]> <sarang "mikerah: to be clear, DLSAG is n"> Thanks for the clarification.
    [2019-12-23 12:12:48] <suraeNoether> these transcripts say things like "Alice sends key NODE_ID with ring members RING_MEMBERS, authorizing the creation of outputs NEW_NODE_ID owned by Bob." It's a "ground truth" ledger.
    [2019-12-23 12:13:22] <suraeNoether> these transcripts also contain the accusations that Eve makes. "Eve thinks ring signature NODE_ID belongs to Bob. In actuality, it belongs to Alice." sort of thing
    [2019-12-23 12:13:41] <suraeNoether> in theory, anyone can fire up tracing.py, tweak the parameters inside, and see the simulated ledger
    [2019-12-23 12:13:44] <suraeNoether> the ledger is working just fine
    [2019-12-23 12:13:49] <sarang> nice
    [2019-12-23 12:14:10] <suraeNoether> unfortunately, but also fortunately, once i put these transcripts into human readable format it became immediately obvious there was a problem with my Eve
    [2019-12-23 12:14:27] <suraeNoether> she is allegedly granted knowledge of her part of the graph, but she doesn't incorporate that knowledge into her matching solution appropriately.
    [2019-12-23 12:14:55] <suraeNoether> so the previous numbers i shared in here, which i took care to explain where provisional, are lower than what we can expect from a realistic eve.
    [2019-12-23 12:15:02] <suraeNoether> these problems were not being caught by my unit tests
    [2019-12-23 12:15:05] <sarang> What needs to be done to properly account for that?
    [2019-12-23 12:16:08] <suraeNoether> the run_experiment function in tracing.py builds a dictionary called eve_ownership, which is not utilized correctly, and allegedly deletes spurious ring members, but i have some evidence that this isn't being done correctly either
    [2019-12-23 12:16:32] <suraeNoether> what really needs to happen is that eve builds a sub-ledger by deleting all her known information, so that it's purely "uknown" data to Eve, before playing the matching game
    [2019-12-23 12:16:47] <suraeNoether> that, together with reporting her known information, would fix the problem
    [2019-12-23 12:17:04] <suraeNoether> since i have CLSAG and triptych to take care of, and since so much of this code is human readable at this point, i'm putting this project down until the new year
    [2019-12-23 12:17:41] <suraeNoether> especially since "the problem" is easily explainable and I can point to where it's occuring
    [2019-12-23 12:18:19] <suraeNoether> but, for example, if anyone wants to just simulate a ledger using different stochastic matrices or spendtime distributions, they can tweak the parameters inside of tracing.py and generate as many ledgers as they like
    [2019-12-23 12:18:49] <suraeNoether> and now you can read them like a story. the world's least interesting procedurally generated story.
    [2019-12-23 12:19:28] <suraeNoether> i'll be unavailable for the next 72 hours or so (family is coming into town) but i have CLSAG and triptych printed; i'm about 1/3 of the way marking up my copy of triptych
    [2019-12-23 12:19:49] <suraeNoether> that's all i have today. does anyone have any questions for me about that, or other questions on anything research-y?
    [2019-12-23 12:20:22] <sarang> When you're done with Triptych, will suggestions be added as Overleaf review comments?
    [2019-12-23 12:21:27] ⇐ sech1 quit (~sech1111@ppp31-192-141-150.tis-dialog.ru): Remote host closed the connection
    [2019-12-23 12:21:43] → sech1 joined (~sech1111@ppp31-192-141-150.tis-dialog.ru)
    [2019-12-23 12:22:00] <suraeNoether> i was going to add some as comments and send the rest as an email to you
    [2019-12-23 12:22:09] <sarang> Great, thanks
    [2019-12-23 12:22:19] <sarang> You have the line-numbered version?
    [2019-12-23 12:22:59] <suraeNoether> yep
    [2019-12-23 12:23:20] <suraeNoether> okay, let's move onto ACTION ITEMS
    [2019-12-23 12:23:24] <suraeNoether> sarang?
    [2019-12-23 12:23:57] <sarang> I'll be addressing some multisig-related MPC stuff for RCT3 and Omniring
    [2019-12-23 12:24:20] <sarang> Then working on any necessary updates for CLSAG and/or Triptych based on review
    [2019-12-23 12:24:32] <sarang> and then getting both papers posted to IACR
    [2019-12-23 12:25:44] <suraeNoether> Helping sarang finish triptych and clsag; if i finish this before end-of-year, i'll go back to matching
    [2019-12-23 12:28:05] <sarang> Oh, a longer-term action item is to backport the CLSAG security model changes to DLSAG, but that's likely not this week
    [2019-12-23 12:28:31] <sarang> I don't recall the DLSAG reviewers mentioning it, but it should be done anyway
    [2019-12-23 12:28:48] <suraeNoether> allrighty
    [2019-12-23 12:28:53] <suraeNoether> unless anyone has any final quesitons
    [2019-12-23 12:28:59] <suraeNoether> i think we can adjourn
    [2019-12-23 12:29:10] <sarang> Happy Festivus!


# Action History
- Created by: SarangNoether | 2019-12-20T00:14:50+00:00
- Closed at: 2019-12-23T17:32:22+00:00
