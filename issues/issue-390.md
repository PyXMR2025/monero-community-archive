---
title: 'Research meeting: 16 September 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/390
author: SarangNoether
assignees: []
labels: []
created_at: '2019-09-13T18:12:54+00:00'
updated_at: '2019-09-16T17:40:01+00:00'
type: issue
status: closed
closed_at: '2019-09-16T17:40:01+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 16 September 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [Triptych](https://github.com/monero-project/research-lab/issues/56) proof-of-concept [code](https://github.com/SarangNoether/skunkworks/tree/lrs/lrs) and [analysis](https://github.com/SarangNoether/skunkworks/blob/sublinear/triptych.md), Lelantus modifications, paper revisions, [funding request](https://ccs.getmonero.org/proposals/sarang-2019-q4.html)
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-09-16T17:40:01+00:00
    [2019-09-16 13:00:12] <sarang> OK, it's time for the meeting!
    [2019-09-16 13:00:17] <sarang> Agenda: https://github.com/monero-project/meta/issues/390
    [2019-09-16 13:00:21] <sarang> Logs posted there afterward
    [2019-09-16 13:00:36] <sarang> GREETINGS
    [2019-09-16 13:00:41] <mikerah> Hello
    [2019-09-16 13:01:04] → kico joined (~kico@gateway/tor-sasl/kico)
    [2019-09-16 13:01:34] <sarang> I'll wait a couple of minutes in case anyone else shows up
    [2019-09-16 13:01:49] → Common-Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-09-16 13:02:01] <kinghat> o/
    [2019-09-16 13:02:27] <kinghat> *the regular crowd shuffles in*
    [2019-09-16 13:02:59] <el00ruobuob> Hi
    [2019-09-16 13:03:08] <sarang> Our pal suraeNoether said he may not be available for today's meeting
    [2019-09-16 13:03:20] <sarang> But I can share some of the things I've been working on for our ROUNDTABLE
    [2019-09-16 13:03:47] <sarang> The ever-clever RandomRun posted an idea for a signature scheme earlier: https://github.com/monero-project/research-lab/issues/56
    [2019-09-16 13:04:08] <sarang> Some updates have been made for efficiency, and I worked up proof-of-concept code: https://github.com/SarangNoether/skunkworks/tree/lrs/lrs
    [2019-09-16 13:04:21] <sarang> And a timing/space analysis: https://github.com/SarangNoether/skunkworks/blob/sublinear/triptych.md
    [2019-09-16 13:04:40] <sarang> (I gave it the name Triptych as a placeholder, so we have a name to use for clarity)
    [2019-09-16 13:04:57] → TurtleCoin joined (~TurtleCoi@turtlecoin/bot/turtlecoin)
    [2019-09-16 13:05:41] ⇐ Common_Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Ping timeout: 276 seconds
    [2019-09-16 13:05:44] <sarang> It actually beats Lelantus in terms of 2-2 transaction size
    [2019-09-16 13:05:54] <sarang> But verification is less efficient
    [2019-09-16 13:06:09] → somewebuser joined (45871d66@rrcs-69-135-29-102.central.biz.rr.com)
    [2019-09-16 13:06:18] <sarang> Also note that security hasn't been proven yet, but it uses a modification by Bootle et al. to a 1-of-N proof by Groth
    [2019-09-16 13:06:23] * somewebuser → atestwebuser
    [2019-09-16 13:06:31] <sarang> and that 1-of-N has good proofs
    [2019-09-16 13:06:56] ⇐ atestwebuser quit (45871d66@rrcs-69-135-29-102.central.biz.rr.com): Remote host closed the connection
    [2019-09-16 13:07:09] <sarang> Aside from that, I've been working with the Lelantus authors on some ideas to fix its self-spend tracing problem
    [2019-09-16 13:07:17] <sarang> And that's coming together nicely
    [2019-09-16 13:07:45] <sarang> The CLSAG paper will be submitted to Financial Cryptography this week
    [2019-09-16 13:08:11] <sarang> And my CCS funding request for next quarter has been opened: https://ccs.getmonero.org/proposals/sarang-2019-q4.html
    [2019-09-16 13:08:53] <sarang> On a more whimsical note, a preprint was just posted that does some analysis on a card-based cipher originally designed by Bruce Schneier for a book: https://arxiv.org/abs/1909.06300
    [2019-09-16 13:09:42] <sarang> It's a neat example of a cipher that appears to resist a good deal of modern cryptanalysis, but can be done using paper, pen, and a deck of playing cards!
    [2019-09-16 13:10:07] <mikerah> ElsieFour also has such properties except without the playing cards.
    [2019-09-16 13:10:15] <sarang> Ah, and I'd be remiss if I didn't mention the trustless recursive SNARK paper, Halo, that was recently posted by the Zcash folks
    [2019-09-16 13:10:27] <sarang> mikerah: I wasn't familiar with that!
    [2019-09-16 13:10:50] <sarang> Has it undergone much analysis?
    [2019-09-16 13:10:55] <mikerah> Here's the preprint: https://eprint.iacr.org/2017/339.pdf
    [2019-09-16 13:11:22] <sarang> neat
    [2019-09-16 13:11:30] <mikerah> I'm not sure if it has gone through much analysis as it's a relatively new construction.
    [2019-09-16 13:11:38] <mikerah> But you can use paper and pen!
    [2019-09-16 13:12:14] <sarang> Halo has some clever ideas in it, but it's worth noting (as usual) that preprints don't undergo peer review, and that Halo currently lacks a soundness proof
    [2019-09-16 13:12:54] <sarang> It will be fun to see the new research that comes from its ideas
    [2019-09-16 13:13:39] <sarang> Any particular questions on the items that I mentioned?
    [2019-09-16 13:14:30] <mikerah> How would the ideas from lelantus get implemented in monero?
    [2019-09-16 13:15:00] <sarang> Its transaction model could, hypothetically, be implemented directly
    [2019-09-16 13:15:12] <sarang> Using a particular kind of migration transaction to transition older outputs
    [2019-09-16 13:15:25] <sarang> It would result initially in a smaller anonymity set
    [2019-09-16 13:15:34] → PauleBert joined (~paulebert@51.75.90.106)
    [2019-09-16 13:15:59] <sarang> Currently Lelantus has a tracing issue that's a deal-breaker IMO
    [2019-09-16 13:16:11] <sarang> but very recent ideas mean that may not be a problem
    [2019-09-16 13:17:30] <mikerah> Would there be traceability problems from the current monero blockchain to this hypothetical lelantus+monero blockchain?
    [2019-09-16 13:17:40] <sarang> How so?
    [2019-09-16 13:17:52] <mikerah> As in, would it be possible to trace transactions between hard forked blockchains
    [2019-09-16 13:17:55] <sarang> In such an implementation, old-style transactions would not be allowed
    [2019-09-16 13:18:21] <sarang> Old outputs would undergo a signer-ambiguous transaction to generate a new output commitment that is Lelantus-compatible
    [2019-09-16 13:18:49] <doxxy> sarang: greets
    [2019-09-16 13:19:08] <sarang> So a migration is trivially distinguishable, but retains the same kind of signer ambiguity that exists now
    [2019-09-16 13:19:14] <sarang> hi
    [2019-09-16 13:19:43] <sarang> To be clear, there are no plans to implement this AFAIK
    [2019-09-16 13:19:45] <mikerah> I see. I guess more work would need to be done on this front.
    [2019-09-16 13:19:46] <sarang> It's all just research
    [2019-09-16 13:20:33] <sarang> Anyway, that's what I've been working on
    [2019-09-16 13:20:39] <sarang> Does anyone else wish to share interesting research?
    [2019-09-16 13:23:13] <sarang> OK!
    [2019-09-16 13:24:11] <sarang> Well, in that case my ACTION ITEMS are administrative stuff for FC submission, ongoing analysis of Lelantus modifications and proofs, and returning to some existing recent proving systems
    [2019-09-16 13:25:12] <sarang> Before we adjourn, is there anything else to discuss?
    [2019-09-16 13:25:41] <gingeropolous> i don't have any research im working on, but im enjoying banging my head regarding the randomx branch prediction problem
    [2019-09-16 13:25:51] <sarang> Go on!
    [2019-09-16 13:26:24] <gingeropolous> so, big chunk of CPU silicon dedicated to branch prediction. Turns out a lot of the methods use neural networks kinda thing (called perceptron at one point).
    [2019-09-16 13:26:45] <gingeropolous> however, problem is that randomx is random - its random whether a branch will be taken
    [2019-09-16 13:27:05] <gingeropolous> and when somethings random, hard for machine-learning / pattern recognition to get any gains
    [2019-09-16 13:27:28] <sarang> Makes sense
    [2019-09-16 13:27:43] <gingeropolous> however, if you try and seed random into the program (such that a branch predictor could find some emergent pattern), this information could be harvested by an ASIC or some other mitigation
    [2019-09-16 13:28:39] <gingeropolous> so, my head sorta got stuck at that point... and if it'd be possible to somehow hide the emergent pattern... and then all the thought threads frayed
    [2019-09-16 13:28:41] <sarang> So, using information from existing CPU architectures in order to develop better specialized hardware?
    [2019-09-16 13:29:19] <sarang> Or information from any kind of well-designed predictor, I suppose
    [2019-09-16 13:29:42] <gingeropolous> well the general randomx problem is to make a PoW that leverages stuff in CPUs.
    [2019-09-16 13:29:52] <gingeropolous> and branch prediction is underleveraged due to the problem i just described
    [2019-09-16 13:30:07] <sarang> Ah, ok
    [2019-09-16 13:30:52] <sarang> I don't know enough about CPU branch prediction to fully appreciate this, but it sounds interesting nonetheless
    [2019-09-16 13:32:31] <sarang> Anything else of interest to share before the meeting ends?
    [2019-09-16 13:33:47] <sarang> All righty then
    [2019-09-16 13:33:55] <sarang> Thanks to everyone for being here; we are now adjourned!
    [2019-09-16 13:33:59] <sarang> Logs will be posted shortly


# Action History
- Created by: SarangNoether | 2019-09-13T18:12:54+00:00
- Closed at: 2019-09-16T17:40:01+00:00
