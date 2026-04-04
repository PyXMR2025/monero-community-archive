---
title: 'Research meeting: 29 July 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/377
author: SarangNoether
assignees: []
labels: []
created_at: '2019-07-25T13:37:54+00:00'
updated_at: '2019-07-29T17:55:22+00:00'
type: issue
status: closed
closed_at: '2019-07-29T17:55:22+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 29 July 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [RCT3 prototype](https://github.com/SarangNoether/skunkworks/tree/rct3/rct3), library updates
b. Surae
c. Others?

3. General questions

4. Action items
a. Sarang: RCT3 prototype, Omniring proof splitting
b. Surae
c. Others?

# Discussion History
## SarangNoether | 2019-07-29T17:55:22+00:00
    [2019-07-29 12:00:33] <sarang> OK, let's begin
    [2019-07-29 12:00:34] <sarang> Hello all
    [2019-07-29 12:00:45] <sarang> Logs of this meeting will be posted to the GitHub agenda issue afterward
    [2019-07-29 12:00:47] <sarang> GREETINGS
    [2019-07-29 12:00:59] <suraeNoether> greetings!
    [2019-07-29 12:01:02] <kenshamir[m]> hey
    [2019-07-29 12:01:05] <sarang> Whoops, here is the current agenda: https://github.com/monero-project/meta/issues/377
    [2019-07-29 12:01:13] * sarang set the topic to Research meeting Mondays @ 17:00 UTC: https://github.com/monero-project/meta/issues/377. Be excellent to each other.
    [2019-07-29 12:02:06] ⇐ Common-Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Read error: Connection reset by peer
    [2019-07-29 12:02:53] → Common-Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-07-29 12:02:57] <sarang> Let's go ahead with ROUNDTABLE
    [2019-07-29 12:03:26] <sarang> I've been working hard on an RCT3 implementation, integrating some nice optimizations and seeing if it's possible to get key images working as expected
    [2019-07-29 12:03:47] <sarang> This also led to a bunch of other library updates that the code relies on
    [2019-07-29 12:03:53] <sarang> So generally just a lot of coding
    [2019-07-29 12:04:07] <sarang> I also gave a fun lecture on the Enigma cipher machine and the math behind it, which is always fun ;)
    [2019-07-29 12:04:17] <suraeNoether> nice, what was that for? a meetup or something?
    [2019-07-29 12:04:49] <sarang> A friend teaches at a university and thought it would be good for an undergrad crypto class
    [2019-07-29 12:04:55] <sarang> Since the Enigma break is all about permutation groups
    [2019-07-29 12:05:37] <suraeNoether> nice
    [2019-07-29 12:06:07] <sarang> I should be able to finish up an integration of the BP inner product verifier optimization into RCT3 shortly
    [2019-07-29 12:06:43] <sarang> Then, of course, DEF CON approaches!
    [2019-07-29 12:07:20] <suraeNoether> neat
    [2019-07-29 12:07:47] <suraeNoether> i have a very dirty branch on my computer with my matching simulations and experiments being worked upon
    [2019-07-29 12:07:54] <sarang> How are those going?
    [2019-07-29 12:08:04] <hyc> defcon - anyone got grasshopper repellent?
    [2019-07-29 12:08:10] <sarang> -____-
    [2019-07-29 12:08:49] <suraeNoether> i've proven all the theorems necessary to prove that the algorithm in graphtheory.py does what i claim it does, and i'm currently testing that my simulated ledgers are doing what i expect.
    [2019-07-29 12:08:58] <sarang> noice
    [2019-07-29 12:09:24] <sarang> Will be very neat to see the results, and to see if/how they can work with the analysis that Isthmus et al. are doing on Monero and Zcash
    [2019-07-29 12:10:03] <suraeNoether> in addition to that, i have a bunch of MAGIC stuff I need to get done, and my discussions with isthmus' digital forensics work are leaning in that direction
    [2019-07-29 12:10:23] <suraeNoether> i'm thinking the content of this project may take up more than two papers :\
    [2019-07-29 12:10:23] <sarang> Cool!
    [2019-07-29 12:10:48] <sarang> Also worth noting that the CLSAG paper has been updated on IACR, thanks mainly to kenshamir[m]'s comments and questions
    [2019-07-29 12:11:05] <sarang> kenshamir[m] has also been working on a Rust implementation of CLSAG/MLSAG using the dalek library
    [2019-07-29 12:11:07] → thrmo joined (~thrmo@unaffiliated/thrmo)
    [2019-07-29 12:11:10] <suraeNoether> hyc: i hear grasshoppers are delicious, i wonder if any of those fancy vegas michelin star restaurants are capitalizing on the swarm
    [2019-07-29 12:11:11] <sarang> Anything you'd like to share on that, kenshamir[m] ?
    [2019-07-29 12:12:47] <kenshamir[m]> Hi, the library is finished, not interopable with monero because it uses a different curve though. The numbers are quite impressive and I believe it is due to the way cLSAG was created
    [2019-07-29 12:13:03] → sfhi2 joined (~sfhi@37.252.225.109)
    [2019-07-29 12:13:09] <sarang> aw shucks
    [2019-07-29 12:13:23] <sarang> Will be great to see your MLSAG vs CLSAG numbers at different ring sizes
    [2019-07-29 12:14:02] <suraeNoether> i believe there was a question re: ristretto and multi-exp like pippenger right before the meeting that would be relevant here?
    [2019-07-29 12:14:23] <sarang> I brought it up a while back because we handle different linear combination sizes _very_ differently in the codebase
    [2019-07-29 12:14:25] <scoobybejesus> is that rust code in a public repo?
    [2019-07-29 12:14:33] <sarang> We use no fewer than 4 methods
    [2019-07-29 12:14:35] <kenshamir[m]> The numbers above were for different ring sizes, I may have mis-typed key sizes by accident
    [2019-07-29 12:14:58] <kenshamir[m]> 256 and 512 were for the decoy sizes; if I was not clear
    [2019-07-29 12:15:05] <sarang> A big part of the reason CLSAG verification is faster than MLSAG is because of the introduction of a new linear combination evaluation algorithm
    [2019-07-29 12:15:15] <sarang> kenshamir[m]: can you link them again for the logs?
    [2019-07-29 12:15:25] <sarang> (if comfortable having them public)
    [2019-07-29 12:15:39] <kenshamir[m]> <scoobybejesus "is that rust code in a public re"> Not the cLSAG code, once I add documentation and sanitise it I can post it in here
    [2019-07-29 12:15:53] <sarang> ty
    [2019-07-29 12:15:56] <kenshamir[m]> <sarang "kenshamir: can you link them aga"> Yep sure
    [2019-07-29 12:15:58] <scoobybejesus> :)
    [2019-07-29 12:16:32] — kenshamir[m] sent a long message:  < https://matrix.org/_matrix/media/v1/download/matrix.org/qyxFtJuthDFQlLNsQifQmhnr >
    [2019-07-29 12:16:39] — kenshamir[m] sent a long message:  < https://matrix.org/_matrix/media/v1/download/matrix.org/DuHfhNbuqOFRLjbkIaQdIXlA >
    [2019-07-29 12:16:50] ⇐ thrmo quit (~thrmo@unaffiliated/thrmo): Ping timeout: 272 seconds
    [2019-07-29 12:16:58] → thrmo joined (~thrmo@unaffiliated/thrmo)
    [2019-07-29 12:17:05] — kenshamir[m] sent a long message:  < https://matrix.org/_matrix/media/v1/download/matrix.org/nwVabRjaqUnwjXywxfnikxtC >
    [2019-07-29 12:17:26] <sarang> What does "without Pippenger/Straus" mean? Simple iterative evaluation of linear combinations?
    [2019-07-29 12:17:28] ⇐ sfhi quit (~sfhi@37.252.225.109): Ping timeout: 272 seconds
    [2019-07-29 12:17:51] <kenshamir[m]> Yep exactly
    [2019-07-29 12:18:06] <sarang> Impressive numbers
    [2019-07-29 12:18:13] <sarang> Of course, it's a different hash function
    [2019-07-29 12:18:25] <kenshamir[m]> I just did scalarbase mult in a for loop
    [2019-07-29 12:18:43] <kenshamir[m]> haha yeah that too
    [2019-07-29 12:18:59] <suraeNoether> hmmmmm
    [2019-07-29 12:19:07] <sarang> But if the hash function is the same across both of your CLSAG/MLSAG, then the relative numbers are good
    [2019-07-29 12:19:29] <suraeNoether> something that is both faster and smaller and with equivalent security is a no-brainer for implementation (pending audits)
    [2019-07-29 12:19:48] <sarang> Speaking of this, still in contact with potential auditors, who are moving very slowly
    [2019-07-29 12:19:53] <sarang> Nothing to report on that front :/
    [2019-07-29 12:20:47] <suraeNoether> the improved space allows for a logarithmic increase in verification time without actually slowing down the network (at least when it comes to new nodes downloading the network). judging by these numbers, a ring size of 16 or 32 is no longer like pouring molasses or concrete onto the network
    [2019-07-29 12:22:21] <sarang> OK, any other interesting research to report?
    [2019-07-29 12:22:55] <gingeropolous> re: audits, or roll-out in general. Is this the kind of thing that could be rolled-out in parallel with existing? i.e., have an overlap, where the network uses the existing as the primary / default, but can optionally use the new thing, and then once new thuing is vetted, just prune the old?
    [2019-07-29 12:23:09] <hyc> ^ slow auditors - a lot of people are on summer holiday now
    [2019-07-29 12:23:11] <gingeropolous> or, switch to the new and no longer have to relay / verify the old style during the overlap?
    [2019-07-29 12:23:33] <suraeNoether> sarang: am i wrong in saying that gingeropolous is correct that clsag could be implemented in parallel before mlsag is deprecated?
    [2019-07-29 12:24:25] <hyc> we had a 24hr overlap in the last hardfork for this sort of thing
    [2019-07-29 12:24:41] <gingeropolous> this would be kinda different.
    [2019-07-29 12:24:52] <sarang> I suppose it could be overlapping, provided the fee model supports it properly
    [2019-07-29 12:25:00] ⇐ thrmo quit (~thrmo@unaffiliated/thrmo): Ping timeout: 244 seconds
    [2019-07-29 12:25:11] <sarang> I don't really see why this would be useful
    [2019-07-29 12:25:32] ⇐ crCr62U0 quit (~crCr62U0@gateway/tor-sasl/crcr62u0): Ping timeout: 260 seconds
    [2019-07-29 12:26:05] <gingeropolous> i dunno. i'm just opening the conversation regarding the model that all new things need to be audited
    [2019-07-29 12:26:13] <gingeropolous> i mean, obvi auditing is great
    [2019-07-29 12:26:17] <sarang> yes
    [2019-07-29 12:26:22] <gingeropolous> but its not perfect
    [2019-07-29 12:26:25] <dEBRUYNE> hyc: Yeah in general, summer constitutes low activity
    [2019-07-29 12:26:32] <sarang> It's good for inspiring confidence, as well as the obvious benefits of catching any errors
    [2019-07-29 12:26:49] <kenshamir[m]> Can Monero benefit from using bulletproofs for arithmetic circuits?
    [2019-07-29 12:26:58] <dEBRUYNE> gingeropolous: Didn't we discuss that kind of model for Bulletproofs or RingCT too?
    [2019-07-29 12:27:03] <sarang> Likely not, with our current tx model
    [2019-07-29 12:27:05] <gingeropolous> yeah dEBRUYNE
    [2019-07-29 12:27:10] <sarang> The scaling isn't great
    [2019-07-29 12:27:10] <dEBRUYNE> I think it was shot down for good reasons, but I cannot remember them exactly :-P
    [2019-07-29 12:27:19] <gingeropolous> i think that was post audit though
    [2019-07-29 12:27:19] <sarang> and we have hash functions, which screw things up
    [2019-07-29 12:28:09] <sarang> Zooko had a slide in some presentation where his team estimated the verification time for a circuit with the complexity of Sapling (Sprout? don't recall)
    [2019-07-29 12:28:18] <sarang> and BP verification was O(1 s)
    [2019-07-29 12:28:43] <sarang> Compared to our current verification time which is probably 1/50th of that
    [2019-07-29 12:29:02] <sarang> maybe 1/100th
    [2019-07-29 12:29:37] <kenshamir[m]> yikes
    [2019-07-29 12:29:40] <suraeNoether> kenshamir: if we designed an arithmetic circuit to describe a ring confidential transaction language, then yes, but that's sort of what RCT3 and omniring and lelantus try to do... sarang, i think zooko was showing "what it would look like for a Sapling transaction language to be proven in the bulletproof setting" not ring confidential transactions, so it's not clear to me whether it'd be slower.
    [2019-07-29 12:29:50] <suraeNoether> in our setting
    [2019-07-29 12:29:58] <suraeNoether> with the exception of our non-AC-compatible hash function
    [2019-07-29 12:30:02] → thrmo joined (~thrmo@unaffiliated/thrmo)
    [2019-07-29 12:30:31] <dEBRUYNE> sarang: That's verification time for fully shielded transactions?
    [2019-07-29 12:30:48] <suraeNoether> dEBRUYNE yeah, iirc
    [2019-07-29 12:31:01] <dEBRUYNE> Yikes
    [2019-07-29 12:31:14] <sarang> Yeah, that timing was just to give an example of what a production-size tx circuit might look like
    [2019-07-29 12:31:29] <dEBRUYNE> Especially given that, as far as I know, you have to run a full node in order to properly perform fully shielded transactions
    [2019-07-29 12:31:44] <dEBRUYNE> Anyway, I digress :-P
    [2019-07-29 12:32:02] <sarang> Anyway, suraeNoether is right in that RCT3 and Omniring try to bring the BP benefits to specific languages used to prove RingCT-type statements
    [2019-07-29 12:32:08] <sarang> which is why we're interested in them
    [2019-07-29 12:32:26] <suraeNoether> yeah, bulletproofs for use in SNARK-style languages is like... uhm... putting a large-diameter turbofan engine into a Mini Cooper. It's not going to do what you think it's going to do.
    [2019-07-29 12:32:54] <sarang> BPs can be much more efficient for languages built for it
    [2019-07-29 12:33:01] <sarang> which is why range proofs are so efficient
    [2019-07-29 12:33:31] <kenshamir[m]> haha
    [2019-07-29 12:33:36] <suraeNoether> indeed
    [2019-07-29 12:33:37] <suraeNoether> moving along
    [2019-07-29 12:35:08] → JOhNKmus joined (JOhNKmus@gateway/vpn/privateinternetaccess/johnkmus)
    [2019-07-29 12:35:28] <sarang> heh
    [2019-07-29 12:35:32] <sarang> ok, other research?
    [2019-07-29 12:35:38] <sarang> Or QUESTIONS, from the agenda?
    [2019-07-29 12:38:15] <sarang> OK then! To ACTION ITEMS
    [2019-07-29 12:38:44] <sarang> I'll be finalizing some things for my DEF CON talk, workshop, and panel; and finalizing some RCT3 integration optimizations
    [2019-07-29 12:40:28] <sarang> suraeNoether: ?
    [2019-07-29 12:40:39] → antanst0673803 joined (~antanst@62.169.219.213)
    [2019-07-29 12:41:12] <suraeNoether> oh gosh sorry
    [2019-07-29 12:41:23] <suraeNoether> i was computing a number sorry about that. :P
    [2019-07-29 12:41:30] <sarang> it's 7
    [2019-07-29 12:41:32] ⇐ antanst067380 quit (~antanst@62.169.219.213): Ping timeout: 272 seconds
    [2019-07-29 12:41:52] <suraeNoether> my action items are: work on sims and the experimenter, and work with isthmus to formalize statistical hypotheses for testing all this
    [2019-07-29 12:42:16] <sarang> Having data from Isthmus's group will be extremely valuable for this kind of analysis
    [2019-07-29 12:42:46] <suraeNoether> actually the number is O(153.58*N), which is the number of bits used to describe the number of possible spend histories at ring size 32 with N outputs.
    [2019-07-29 12:42:51] <suraeNoether> which is nutters
    [2019-07-29 12:43:02] <sarang> This is all assuming no external information?
    [2019-07-29 12:43:17] <sarang> Or other graph-based information on chain reactions and provably-spent outputs?
    [2019-07-29 12:43:19] <suraeNoether> merely the total number of self-consistent spend histories
    [2019-07-29 12:43:38] <sarang> Ah ok, so for a hypothetical graph
    [2019-07-29 12:43:50] <suraeNoether> yeah
    [2019-07-29 12:43:53] <sarang> got it
    [2019-07-29 12:44:43] → crCr62U0 joined (~crCr62U0@gateway/tor-sasl/crcr62u0)
    [2019-07-29 12:45:30] <gingeropolous>  O(153.58*N) ... great. now your math is talking in math
    [2019-07-29 12:46:50] <suraeNoether> well it means that for, say, 1000 transactions at ring size 32, there are 2^(153,580) possible spend histories.
    [2019-07-29 12:47:33] <suraeNoether> anyway
    [2019-07-29 12:47:58] <suraeNoether> (N has to be a lot bigger than the ring size for the above formula to hold btw)
    [2019-07-29 12:48:19] <sarang> which is... quite reasonable
    [2019-07-29 12:48:49] <sarang> Any other final thoughts or questions before we adjourn?
    [2019-07-29 12:50:17] <sarang> OK then! Thanks to everyone for participating. We are adjourned


# Action History
- Created by: SarangNoether | 2019-07-25T13:37:54+00:00
- Closed at: 2019-07-29T17:55:22+00:00
