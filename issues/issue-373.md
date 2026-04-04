---
title: 'Research meeting: 22 July 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/373
author: SarangNoether
assignees: []
labels: []
created_at: '2019-07-19T13:04:11+00:00'
updated_at: '2019-07-22T17:41:01+00:00'
type: issue
status: closed
closed_at: '2019-07-22T17:41:01+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 22 July 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [DEF CON talk/workshop](https://github.com/SarangNoether/skunkworks/tree/defcon-workshop), [RCT3 prototype](https://github.com/SarangNoether/skunkworks/tree/rct3/rct3)
b. Surae
c. Others?

3. General questions

4. Action items
a. Sarang: RCT3 prototype, Omniring proof splitting
b. Surae
c. Others?

# Discussion History
## SarangNoether | 2019-07-22T17:41:01+00:00
    [2019-07-22 12:59:53] <sarang> OK, let's get started
    [2019-07-22 12:59:57] <sarang> GREETINGS
    [2019-07-22 13:00:07] <suraeNoether> hello fellow not-robots
    [2019-07-22 13:01:23] — midipoet waves while sitting to listen a while
    [2019-07-22 13:01:26] <sarang> Let's move on to ROUNDTABLE
    [2019-07-22 13:01:30] <sarang> suraeNoether: care to begin?
    [2019-07-22 13:01:46] <suraeNoether> sure
    [2019-07-22 13:02:05] <suraeNoether> so this weekend i finally posted the konferenco post mortem report, the budget, and markdown'd all the things: https://www.reddit.com/r/Monero/comments/cfsc2m/suraes_content_dump_konferenco_post_morto_budget/
    [2019-07-22 13:02:25] <suraeNoether> this includes my research report for the last quarter and my request for funding for Aug, Sep, Oct.
    [2019-07-22 13:03:04] <suraeNoether> And isthmus pointed out a property of zcash's shielded pool that i am capable of modeling with my matching simulations, so i've spent a few hours this past weekend trying to get those working (still a wip)
    [2019-07-22 13:04:10] <suraeNoether> that's all
    [2019-07-22 13:04:27] <suraeNoether> sarang?
    [2019-07-22 13:04:39] <sarang> Nice!
    [2019-07-22 13:04:55] <sarang> I've posted the handout and some sample code for my upcoming DEF CON workshop
    [2019-07-22 13:05:17] <suraeNoether> nice! thatsafineoutreach.gif
    [2019-07-22 13:05:20] <sarang> (note that you should not use the handout or sample code in production environments, of course... only for playing around)
    [2019-07-22 13:05:40] <sarang> And I have incomplete work on an RCT3 proof of concept implementation
    [2019-07-22 13:05:44] <sarang> with some efficiency improvements
    [2019-07-22 13:06:42] — needmorebtc90 waves
    [2019-07-22 13:07:02] <sarang> the batching opportunities for RCT3 are quite nice
    [2019-07-22 13:07:18] <sarang> as is the fact that the prover and verifier are relatively straightforward
    [2019-07-22 13:07:33] <sarang> also also it can take advantage of any existing rangeproof implementation
    [2019-07-22 13:09:14] <sarang> Any questions on these?
    [2019-07-22 13:09:30] <kenshamir[m]> Hi Sarang, yes
    [2019-07-22 13:09:31] <kenshamir[m]> Do you believe that all of the alternatives; omniring, ringct and lelantus would be a better alternative to the current ringCT even with cLSAG?
    [2019-07-22 13:09:32] <kenshamir[m]> Are you waiting for a feature or an event before choosing a specific alternative?
    [2019-07-22 13:09:55] <kenshamir[m]> better in terms of performance, space savings and anonymity set
    [2019-07-22 13:10:08] <sarang> In terms of practical anonymity set, the sublinear schemes are an improvement at first glance
    [2019-07-22 13:10:09] <sarang> but
    [2019-07-22 13:10:21] <sarang> Lelantus requires a separate output pool and self-spends to avoid tracing
    [2019-07-22 13:10:31] <sarang> Omniring does not support efficient batching
    [2019-07-22 13:10:36] <sarang> RCT3 requires a separate output pool
    [2019-07-22 13:10:59] <sarang> and in all cases, larger anonymity sets require a careful look at handling ring representation, which can become substantial
    [2019-07-22 13:11:18] ⇐ el00ruobuob_[m] quit (~el00ruobu@2a01:e35:2e61:e390:dbb:3b18:1008:9a74): Ping timeout: 252 seconds
    [2019-07-22 13:11:39] <kenshamir[m]> Hmm, so is it fair to say that in their infancy, they are not ready to take over the current ringCT?
    [2019-07-22 13:11:57] <sarang> IMO not without a lot of careful thought on implementation details
    [2019-07-22 13:12:10] <sarang> That being said, I'm looking at two particular things regarding that:
    [2019-07-22 13:12:20] <kenshamir[m]> Do you think it would be better to move away from hiding users in a set of users, to hiding coins in a set of coins?
    [2019-07-22 13:12:24] <sarang> One is determining if/how to efficiently split the rangeproof from Omniring for better verification
    [2019-07-22 13:12:30] <kenshamir[m]> Similar to zcash
    [2019-07-22 13:12:35] <sarang> Two is figuring out if it's possible to use the same key image format with RCT3
    [2019-07-22 13:12:46] <sarang> Full anonymity would be great if we could do it efficiently
    [2019-07-22 13:13:00] <dEBRUYNE> And without a trusted setup :P
    [2019-07-22 13:13:05] <kenshamir[m]> > Two is figuring out if it's possible to use the same key image format with RCT3
    [2019-07-22 13:13:06] <kenshamir[m]> This is very interesting
    [2019-07-22 13:13:15] <suraeNoether> "Do you think it would be better to move away from hiding users in a set of users, to hiding coins in a set of coins?" <-- what's the difference?
    [2019-07-22 13:13:52] <suraeNoether> at a KYC exchange, the exchange knows your personal details and which coins are yours. same same as far as the most common threat model is concerned... unless i'm missing something
    [2019-07-22 13:14:04] <sarang> Oh I totally missed that distinction in what kenshamir[m] said
    [2019-07-22 13:14:14] <sarang> In all cases, users are used to derive coin data
    [2019-07-22 13:14:24] <sarang> Anon sets are considered by coins, not by users
    [2019-07-22 13:16:23] <sarang> Does that answer your question kenshamir[m] ?
    [2019-07-22 13:16:42] <kenshamir[m]> Yep, I was re-reading it to make sure I understood
    [2019-07-22 13:18:17] <kenshamir[m]> <dEBRUYNE "And without a trusted setup :P"> yes this too :)
    [2019-07-22 13:18:24] <sarang> This actually leads neatly into my ACTION ITEMS
    [2019-07-22 13:18:43] <sarang> I'm working on including proper batch verification in the proof of concept code, and integrating into the test transaction flows
    [2019-07-22 13:18:54] <sarang> Then I want to dive more deeply into the two things I mentioned to kenshamir[m] 
    [2019-07-22 13:19:08] <sarang> 1. splitting Omniring proofs for better batching
    [2019-07-22 13:19:30] <sarang> 2. determining the feasibility/security of retaining key image structure in RCT3 to avoid an output pool split
    [2019-07-22 13:19:52] <sarang> And finalizing DEF CON material, of course
    [2019-07-22 13:20:16] <sarang> I'll be giving a talk and leading a workshop in the Monero village, as well as staffing an information table
    [2019-07-22 13:20:24] <sarang> and also doing a panel discussion in the blockchain village
    [2019-07-22 13:20:37] <sarang> suraeNoether: your action items?
    [2019-07-22 13:21:57] <suraeNoether> uhm just working on sims
    [2019-07-22 13:22:15] <suraeNoether> i want to finish the matching stuff soonish to start answering questions rigorously
    [2019-07-22 13:22:35] <suraeNoether> and i want to catch up on your work on the Big Three Trustless Protocols, which is what i'm calling them in my head
    [2019-07-22 13:22:45] <sarang> Yes, IMO the matching stuff is a priority in terms of getting results
    [2019-07-22 13:23:33] <sarang> Moving back in the agenda slightly, does anyone else have either research to present or general questions to ask?
    [2019-07-22 13:24:31] <kenshamir[m]> What was the matching stuff, you guys are referring to?
    [2019-07-22 13:24:54] <sarang> Treating possible spend histories in the tx graph as a graph matching problem
    [2019-07-22 13:25:00] <sarang> and analyzing the structure and complexity
    [2019-07-22 13:25:29] <sarang> In an ideal tx graph, the number of valid matchings (under any data you might already have) should be very high, to provide useful anonymity
    [2019-07-22 13:26:01] <kenshamir[m]> <sarang "Treating possible spend historie"> ohh right, this is very cool research
    [2019-07-22 13:26:10] <sarang> It's one possible metric to examine anonymity
    [2019-07-22 13:26:17] <sarang> (but certainly not a complete one)
    [2019-07-22 13:27:46] <kenshamir[m]> right, it would be interesting to see how much certainty you can produce from such a graph in terms of monero
    [2019-07-22 13:28:11] <sarang> Initial estimates show that it's extremely low
    [2019-07-22 13:28:18] <sarang> but that assumes no external knowledge
    [2019-07-22 13:28:36] <suraeNoether> depends on the size, really.
    [2019-07-22 13:28:53] <kenshamir[m]> I don't know much about it, however I am assuming that it can be used to show how certain one can be that two outputs are linked
    [2019-07-22 13:29:00] <suraeNoether> i mean, a graph where everyone churns 100 times before spending... huge graph... obviously going to have a ton of false results
    [2019-07-22 13:29:17] <sarang> Right, but if done poorly, you can develop heuristics on partial matchings
    [2019-07-22 13:30:35] <kenshamir[m]> I wonder how external data influences the graph, and what type of external data
    [2019-07-22 13:30:47] <sarang> That's the big question on this research
    [2019-07-22 13:30:52] <sarang> Without that, it's purely academic
    [2019-07-22 13:31:22] <kenshamir[m]> As in a real-world scenario, an adversary will have access to external data. I believe the strongest adversary would be an exchange
    [2019-07-22 13:31:32] <kenshamir[m]> oh right
    [2019-07-22 13:31:42] <sarang> Exchanges, governments, entities with broad access to network data
    [2019-07-22 13:32:18] <sarang> It's a big part of why these sublinear schemes are so critical in research
    [2019-07-22 13:32:41] <sarang> At some point, any useful graph data gets lost in the noise of large anon sets
    [2019-07-22 13:32:51] <sarang> (this does not eliminate all types of analysis, of course)
    [2019-07-22 13:32:53] <kenshamir[m]> So the strongest type of external data, would be to know who owns some percentage of outputs and who they are?
    [2019-07-22 13:33:09] <suraeNoether> kenshamir[m]: that's part of it
    [2019-07-22 13:33:14] <kenshamir[m]> <sarang "At some point, any useful graph "> Yep right
    [2019-07-22 13:33:31] <suraeNoether> kenshamir[m]: periodicity can be used to great effect, too
    [2019-07-22 13:33:46] <sarang> True, timing can play a large role
    [2019-07-22 13:34:00] <sarang> both in anon set selection and tx operations
    [2019-07-22 13:34:14] <kenshamir[m]> <suraeNoether "kenshamir: periodicity can be us"> Could you explain?
    [2019-07-22 13:34:25] <suraeNoether> IP data from the network when you ctrl-v your txnid into a block explorer without tor immediately after the transaction is relayed
    [2019-07-22 13:34:32] <kenshamir[m]> Is that "I see a payment being sent every monday at 7pm"
    [2019-07-22 13:34:37] <kenshamir[m]>  * Is that "I see a payment being sent every monday at 7pm"?
    [2019-07-22 13:34:52] <suraeNoether> kenshamir[m]: okay well, imagine you are a churner with a superstitious streak and you like to churn every 88 minutes
    [2019-07-22 13:35:23] <suraeNoether> that chain of churns will stick out like a sore thumb
    [2019-07-22 13:35:50] <sgp_> Joining now and caught up, hello everyone. I agree this matching paper is top priority right now
    [2019-07-22 13:36:05] <suraeNoether> a smart churner selects the age they wait between churns from the wallet distribution. then all the outputs in the ring are drawn from the wallet distribution and no timing data is leaked at all
    [2019-07-22 13:36:43] <kenshamir[m]> Right, that makes sense
    [2019-07-22 13:37:23] <suraeNoether> but any sort of additional data like IP address or timing can be merged together into a big bayesian updating machine and you can develop pretty good (if probabilistic) behavior profiles of users. and this applies to zcash and monero
    [2019-07-22 13:37:24] <kenshamir[m]> suraeNoether: do you mind going into some detail on how you are simulating?
    [2019-07-22 13:37:34] ⇐ rex4539 quit (~rex4539@2a02:587:3514:c700:c828:2c18:5bd4:1273): Quit: rex4539
    [2019-07-22 13:37:45] <sarang> So right now it's a balance between determining how many times to churn (to diffuse the graph) and how not to do it badly
    [2019-07-22 13:37:52] <sarang> To do this, we need better data (e.g. matching)
    [2019-07-22 13:38:03] <suraeNoether> kenshamir[m]: sure, let's do it after the meeting though because it's a little involved
    [2019-07-22 13:38:15] <sarang> OK, any other questions or work to present for this meeting?
    [2019-07-22 13:38:43] <sarang> going once
    [2019-07-22 13:38:53] <sarang> twice
    [2019-07-22 13:39:09] <sarang> OK, we are adjourned! Thanks to everyone for joining us. Logs will be posted to GitHub shortly


# Action History
- Created by: SarangNoether | 2019-07-19T13:04:11+00:00
- Closed at: 2019-07-22T17:41:01+00:00
