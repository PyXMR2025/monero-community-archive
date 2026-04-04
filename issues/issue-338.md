---
title: 'Research meeting: 29 April 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/338
author: SarangNoether
assignees: []
labels: []
created_at: '2019-04-27T19:39:58+00:00'
updated_at: '2019-04-29T17:34:28+00:00'
type: issue
status: closed
closed_at: '2019-04-29T17:34:28+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 29 April 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang
b. Surae
c. Others?

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-04-29T17:34:28+00:00
    [2019-04-29 12:59:51] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/338. Be excellent to each other.
    [2019-04-29 13:00:18] <sarang> A reminder that this meeting will be logged to the GitHub agenda issue
    [2019-04-29 13:00:52] <sarang> Let's begin
    [2019-04-29 13:00:54] <sarang> 1. GREETINGS
    [2019-04-29 13:00:55] <sarang> hi
    [2019-04-29 13:01:05] <suraeNoether> hi
    [2019-04-29 13:01:59] <nioc> peanut gallery watching
    [2019-04-29 13:02:39] <sarang> For 2. ROUNDTABLE, do you want to go first suraeNoether ?
    [2019-04-29 13:02:54] <suraeNoether> how about you go first, because i tend to over-explain and write a book. :P
    [2019-04-29 13:03:00] <sarang> Heh, sure
    [2019-04-29 13:03:14] <sarang> My investigation into Lelantus is wrapping up
    [2019-04-29 13:03:32] <sarang> I added multi-input spends using a modified Fiat-Shamir transform in the Groth commitment-to-zero proof protocol
    [2019-04-29 13:03:44] <sarang> and added direct anonymous payments using stealth addresses
    [2019-04-29 13:03:52] <sarang> Along with general refactoring and cleanup
    [2019-04-29 13:04:01] <suraeNoether> you mean you included those things into your test code?
    [2019-04-29 13:04:03] <sarang> aye
    [2019-04-29 13:04:11] <sarang> https://github.com/SarangNoether/skunkworks/tree/lelantus/lelantus
    [2019-04-29 13:04:19] <suraeNoether> neat; was the modified FS the original one you and I discussed that seemed a little sketchy?
    [2019-04-29 13:04:21] <sarang> transaction.py has some example transaction flows
    [2019-04-29 13:04:26] <sarang> test.py has other tests
    [2019-04-29 13:04:30] <sarang> suraeNoether: yes
    [2019-04-29 13:04:38] <suraeNoether> heh, so for the folks in the audience
    [2019-04-29 13:04:41] <sarang> I asked around and the general agreement seemed to be that it's fine if used properly
    [2019-04-29 13:05:13] <suraeNoether> so the idea is to carry out more than one sigma protocol via FS transform simultaneously, using a common challenge across the multiple protocols
    [2019-04-29 13:05:36] <suraeNoether> computed by hashing *all* of the various sigma protocol's first stages in some canonical way
    [2019-04-29 13:06:12] <sarang> Worth noting that's not an MPC perse
    [2019-04-29 13:06:14] <sarang> *per se
    [2019-04-29 13:06:15] <suraeNoether> my radar goes off here, because it appears to me like this gives an adversarial prover the ability to select which hash function they use to carry out the FS transform for one of their batched sigma protocols
    [2019-04-29 13:06:35] <suraeNoether> it probably would be very hard to pull off across all the protocols simultaneously
    [2019-04-29 13:06:35] <sarang> the proofs are always verified in a single batch, so the verifier computes the F-S challenge themselves
    [2019-04-29 13:07:01] <suraeNoether> anyway, this is *lelantus* and they are doing a weird but cool idea that doesn't have a formal security claim behind it, and it's cool, but it definitely sets off my internal radar
    [2019-04-29 13:07:15] <suraeNoether> i'm glad you implemented it
    [2019-04-29 13:07:29] <sarang> Also: I worked up a possible new transaction type for migrating RingCT outputs to Lelantus
    [2019-04-29 13:07:35] <sarang> Brief writeup: https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/migration.md
    [2019-04-29 13:07:58] <suraeNoether> delightful!
    [2019-04-29 13:08:00] <sarang> There's an intermediate commitment stage to avoid the necessity for a churn
    [2019-04-29 13:08:33] <sarang> I also did some generalization work on Bulletproofs
    [2019-04-29 13:08:43] <sarang> I was looking into a way to allow arbitrary-length inputs
    [2019-04-29 13:08:47] <sarang> had it all coded up
    [2019-04-29 13:08:52] <suraeNoether> ooooh
    [2019-04-29 13:09:02] <suraeNoether> we should make that one of our calls later today
    [2019-04-29 13:09:03] <sarang> turns out the original paper authors thought about that method too, and found it was flawed :(
    [2019-04-29 13:09:06] <suraeNoether> er... later this week i mean
    [2019-04-29 13:09:10] → Common_Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-04-29 13:09:28] <sarang> There's another trickier way that shouldn't have this problem, and I'm getting it finished
    [2019-04-29 13:09:49] <sarang> There are some unfortunate space-time tradeoffs with this method, though
    [2019-04-29 13:09:54] <sarang> the scaling gets funky
    [2019-04-29 13:10:09] <suraeNoether> i'm eager to hear about this
    [2019-04-29 13:10:16] <suraeNoether> arbitrary-length input things are always so tricky
    [2019-04-29 13:10:32] <sarang> The prover alternates between doing the inner product folding and sending additional scalar elements to the verifier
    [2019-04-29 13:10:40] <sarang> it depends on some binary decompositions
    [2019-04-29 13:10:54] <sarang> For range proofs it's probably not worth it, but we'll see
    [2019-04-29 13:11:04] <sarang> It's much more useful for circuit applications where the inputs get very large
    [2019-04-29 13:11:46] <suraeNoether> thanks, Sarang
    [2019-04-29 13:11:51] <sarang> Finally, our DLSAG coauthors wanted to submit to a conference with length restrictions
    [2019-04-29 13:12:07] ⇐ Common-Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Ping timeout: 245 seconds
    [2019-04-29 13:12:13] <suraeNoether> oh i didn't hear about the restrictions...
    [2019-04-29 13:12:16] <sarang> I'm antsy to release this thing, but I'll respect their constraints for submission first
    [2019-04-29 13:12:24] <suraeNoether> i've not been following that conversation
    [2019-04-29 13:12:26] <sarang> Yeah they had to shorten it due to page limits
    [2019-04-29 13:12:46] <sarang> There's an unfortunate issue with key images that we don't have a good answer to yet
    [2019-04-29 13:13:03] <sarang> (it doesn't affect anything that's deployed, only new constructions under investigation)
    [2019-04-29 13:13:05] <suraeNoether> do you support a collaboration rule/social norm/expectation at MRL that preprints have to be made public before peer review submission?
    [2019-04-29 13:13:14] <suraeNoether> in the future i mean
    [2019-04-29 13:13:17] <sarang> not really
    [2019-04-29 13:13:21] <suraeNoether> k
    [2019-04-29 13:13:25] <suraeNoether> just a thought
    [2019-04-29 13:13:27] <sarang> It's typical to withhold preprints until submission
    [2019-04-29 13:13:37] <suraeNoether> well, it depends on the journal
    [2019-04-29 13:13:40] <suraeNoether> it used to be very typical
    [2019-04-29 13:13:51] <sarang> Sure, but I understand the desire to avoid getting scooped, etc.
    [2019-04-29 13:13:52] <suraeNoether> it's more and more typical to post pre-prints before seeking publication
    [2019-04-29 13:13:57] <suraeNoether> especially in the crypto space
    [2019-04-29 13:14:17] <sarang> I personally prefer preprints ASAP, but I can respect others' wishes here
    [2019-04-29 13:14:31] <suraeNoether> yeah, but if it's published on arxiv or iacr, you have a timestamp of your idea with your name on it, so the scooping thing never made sense to me
    [2019-04-29 13:14:39] <sarang> that's a good point
    [2019-04-29 13:14:39] <suraeNoether> but that's cool
    [2019-04-29 13:14:48] — sarang is done now
    [2019-04-29 13:15:02] <suraeNoether> thanks again, Sarang
    [2019-04-29 13:15:09] <suraeNoether> does anyone have any questions for Sarang?
    [2019-04-29 13:15:50] <suraeNoether> allrighty
    [2019-04-29 13:16:27] <suraeNoether> for my update: the tail end of last week, some family showed up unexpectedly and I had to host, and this killed my productivity on Thursday and Friday. I spent most of the weekend making up for that shortfall working on simulations and a bit on CLSAG security, which was just extending my work from previously in the week. I also did some work on output selection (see below)
    [2019-04-29 13:16:53] <suraeNoether> signature scheme proofs and analysis: I put this on the back burner last week to work on MRL11 simulations (see below, also related to output selection), so not much movement here. The remaining piece for CLSAG is matching our formal descriptions of what is being tested vs. what is being proven, to meet the theory with the application.
    [2019-04-29 13:17:17] <suraeNoether> Most of CLSAG is within close reach of finishing, but it's a little slower going than I would like. Sarang and I have a call scheduled later today to discuss this (see below). I also sent my thring signatures paper to a colleague to attempt to destroy my security proofs before I attempt a formal peer review.
    [2019-04-29 13:17:48] <suraeNoether> MRL11 simulations and output selection and churn etc: Some deep issues with my code cropped up, which took a lot of last week to figure out. This led to some ground-up reworking of my bipartite graph code and matching code. Finding maximal matchings in bipartite graphs worked just fine, but finding optimal matchings in bipartite graphs had to be corrected...
    [2019-04-29 13:17:57] <suraeNoether> and none of my unit tests were catching the problem. I expect another commit later today once I make a few more changes.
    [2019-04-29 13:18:14] <suraeNoether> Sarang and I are scheduling calls for several days this week to try to tie up some loose ends on a few remaining projects before Concensus/MCC and Monero Workshop next month. Today we are talking about CLSAG and tomorrow about simulations.
    [2019-04-29 13:18:45] <suraeNoether> I'm speaking at Magical Crypto Conference by the way, and I'll be talking about CLSAG, DLSAG, and the general future of Monero, given upcoming signature schemes and key models; if I have time, I may speak about a longer-term future of Monero that requires deeper changes to our protocol. I only have 15 minutes so I'll be compressing the mathyness.
    [2019-04-29 13:18:52] <suraeNoether> anyone who will be in NYC should come heckle me
    [2019-04-29 13:19:24] <suraeNoether> Monero konferenco updates: We are about 8 weeks away! It's a little off-topic to talk about konferenco organization, but people always have questions, so I'm just going ot give a brief update.
    [2019-04-29 13:19:39] <suraeNoether> XMRHaelan and Thunderosa have been working on some great poster and t-shirt designs. I'm uploading the final version of the poster to the konferenco website later today so we don't have a bunch of versions floating around.
    [2019-04-29 13:19:54] <suraeNoether> Anyone here who is a speaker at the Konferenco and has not started arranging travel, please contact me immediately (I do not have a complete list in front of me, but I'll be contacting folks individually again). Also, please check https://monerokon.com under the schedule to see if any information about your talk is incorrect or if you think you are in the incorrect session, or if you need to get your title
    [2019-04-29 13:19:54] <suraeNoether> and abstract to me (*cough* isthmus andytoshi). hyc pointed out that his name was accidentally excluded from a previous version of the poster, for example: we've double and triple checked things, but we are human and miss stuff.
    [2019-04-29 13:20:25] <suraeNoether> Konferenco final touches: speaker rooms are taken care of, flights are almost done being taken care of, and all that remains is ticket and t-shirt sales before the event. If you are a speaker and you have any questions, please contact me. Also, if you are getting tickets, snag them soon because there's only a little over 2 weeks of early-bird pricing left. I'll be posting a budget update some time in the next
    [2019-04-29 13:20:25] <suraeNoether> 3 weeks, and a post-mortem update after the Konferenco.
    [2019-04-29 13:21:07] <andytoshi> ok i'll do title/abstract today
    [2019-04-29 13:21:10] — sarang will fly a Konferenco banner over Denver to drum up excitement
    [2019-04-29 13:21:14] <suraeNoether> so, basically, I'm catching up on Konferenco emails after the meeting, sending travel reimbursements this week, meeting with sarang on CLSAG and simulations, and writing my talk for MCC... and loving life
    [2019-04-29 13:21:20] <suraeNoether> andytoshi: thanks brother!
    [2019-04-29 13:21:36] <suraeNoether> this job is crazy
    [2019-04-29 13:21:39] <suraeNoether> but i love it
    [2019-04-29 13:21:46] <andytoshi> lol
    [2019-04-29 13:22:04] <sarang> Any questions for suraeNoether ?
    [2019-04-29 13:22:15] — suraeNoether definitely wrote a book
    [2019-04-29 13:22:17] — suraeNoether told you so
    [2019-04-29 13:22:22] <sarang> Also, anyone else have relevant research to present here?
    [2019-04-29 13:24:12] → sech1 joined (~sech1111@ppp109-111-151-155.tis-dialog.ru)
    [2019-04-29 13:24:21] <sarang> right right
    [2019-04-29 13:24:42] <sarang> I suppose that takes care of your action items for the week as well, suraeNoether?
    [2019-04-29 13:25:08] <suraeNoether> oh yeah
    [2019-04-29 13:25:19] <suraeNoether> although i just found this morning four separate ring signature papers i need to read
    [2019-04-29 13:25:20] <sarang> word
    [2019-04-29 13:25:23] <suraeNoether> maybe a fifth
    [2019-04-29 13:25:26] <suraeNoether> *sigh*
    [2019-04-29 13:25:32] <sarang> Heh, shoot along some links
    [2019-04-29 13:26:15] <sarang> Since we didn't have additional 3. QUESTIONS
    [2019-04-29 13:26:18] <sarang> We're on 4. ACTION ITEMS
    [2019-04-29 13:26:40] <sarang> I will finish up this (correct) Bulletproofs input length generalization, so we have it available if desired
    [2019-04-29 13:26:59] <sarang> as well as get more feedback for CLSAG formalization
    [2019-04-29 13:27:32] <sarang> I've been wanting to get an implementation of circuit Bulletproofs for a long time, and would like to get started on it if time permits
    [2019-04-29 13:28:12] <sarang> Any last questions or comments, since it's a pretty quiet day today?
    [2019-04-29 13:28:27] <moneromooo> I do have a question:
    [2019-04-29 13:29:19] <moneromooo> I was playing around with merging txes together, and luigi pointed out that Eve can brute force a ridiculously small space to work out which subsets of ins and outs have matching sums to reconnect inputs to outputs.
    [2019-04-29 13:29:48] <moneromooo> So if anyone can find a way to generate these "part" txes so that the merged ins/outs add up, that'd help a lot :)
    [2019-04-29 13:30:05] <moneromooo> (without leaking private information between participants)
    [2019-04-29 13:30:13] <sarang> Yes, I was thinking about that construction earlier moneromooo. No solution yet, unfortunately, from me :(
    [2019-04-29 13:30:39] <sarang> I was playing around with discrete log knowledge proofs
    [2019-04-29 13:31:57] <sarang> Well, rarely does anyone complain that a meeting was too short, so let's go ahead and formally adjourn; research discussions can of course continue here
    [2019-04-29 13:32:02] <sarang> Logs will be posted shortly to the GitHub agenda issue
    [2019-04-29 13:32:07] <sarang> Thanks to everyone for attending!
    [2019-04-29 13:32:21] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-04-27T19:39:58+00:00
- Closed at: 2019-04-29T17:34:28+00:00
