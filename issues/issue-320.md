---
title: 'Research meeting: 25 March 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/320
author: SarangNoether
assignees: []
labels: []
created_at: '2019-03-22T13:02:04+00:00'
updated_at: '2019-03-25T18:00:57+00:00'
type: issue
status: closed
closed_at: '2019-03-25T18:00:57+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 25 March 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [CLSAG signatures](https://github.com/monero-project/research-lab/issues/52) and [example code](https://github.com/SarangNoether/skunkworks/tree/clsag), [funding request](https://ccs.getmonero.org/proposals/sarang-2019-q2.html)
b. Surae
c. Others?

3. Questions

4. Action items

# Discussion History
## b-g-goodell | 2019-03-25T16:28:36+00:00
MRL-0011 Update: Matching, bipartite graphs, linkability, heuristic traceability.

## SarangNoether | 2019-03-25T18:00:57+00:00
    [2019-03-25 12:58:44] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/320. Be excellent to each other.
    [2019-03-25 12:58:48] <sarang> Our meeting begins presentyl
    [2019-03-25 12:59:20] → alexanarcho joined (~alexanarc@96.9.249.41)
    [2019-03-25 12:59:22] <sarang> Agenda is here, where logs will be posted as well: https://github.com/monero-project/meta/issues/320
    [2019-03-25 12:59:31] → dburkett_ joined (~dburkett@c-71-60-45-57.hsd1.pa.comcast.net)
    [2019-03-25 12:59:35] <suraeNoether> good mornign everyone
    [2019-03-25 12:59:45] <el00ruobuob_[m]> hi
    [2019-03-25 12:59:52] <sarang> 1. GREETINGS
    [2019-03-25 13:00:14] <rehrar> heyo
    [2019-03-25 13:00:21] → ferretinjapan joined (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan)
    [2019-03-25 13:00:32] <sarang> Thanks to everyone for attending today
    [2019-03-25 13:00:33] <[-mugatu-]> o/
    [2019-03-25 13:00:40] <sarang> Let's move to 2. ROUNDTABLE
    [2019-03-25 13:00:49] <sarang> suraeNoether: care to go ahead and discuss your recent work?
    [2019-03-25 13:01:03] <oneiric_> hiyo
    [2019-03-25 13:01:05] <suraeNoether> sure
    [2019-03-25 13:01:27] <suraeNoether> so, in the past week i've been working on MRL-0011, which is rounding the corner of large-scale number crunching
    [2019-03-25 13:01:38] <suraeNoether> MRL-0011 is the churn analysis/matching in bipartite graphs paper
    [2019-03-25 13:02:14] <suraeNoether> i have the graph theoretic stuff passing unit tests, and i've written 1) a simulator that generates a blockchain and 2) an experimenter that tries to link transactions, and then compares it to the "ground truth."
    [2019-03-25 13:02:34] <suraeNoether> these last two have not passed tests yet; my latest commit is here: https://github.com/b-g-goodell/mrl-skunkworks/tree/matching-powerpuff/Matching
    [2019-03-25 13:03:07] <suraeNoether> the simulations are fairly closely linked with our output selection methods, and i'm going to insert more than one output selection method to compare them all
    [2019-03-25 13:03:12] <sarang> Excellent. The idea of using the transaction graph to gain heuristic advantage is an annoying consequence of being decoy-based, and having a solid framework will be useful
    [2019-03-25 13:03:49] <suraeNoether> the goal is to simulate a blockchain in which someone is churning or otherwise spending in an abnormal pattern,a nd we are going to assess the false pos/false negative rate of trying to de-anonymize this individual, and we are going to compare these to the anonymity set sizes ranging from monero-sized ring signatures to zcash sized snarks
    [2019-03-25 13:05:00] <suraeNoether> coding this all up and testing it to make sure it does what we need it to do is taking more time than i had hoped, but now we have the possibility of making some formal recommendations on output selection algorithms and the practicable security of monero's plausible deniability
    [2019-03-25 13:05:36] <sarang> Yeah, a broader question about output selection and transaction behavior has always been a sticking point IMO
    [2019-03-25 13:05:47] <suraeNoether> oh, final update: the DLSAG paper is still being worked on by us and our co-authors but i think we are seeing some movement, and i'll let sarang talk about CLSAG stuff, since that's his bag right now
    [2019-03-25 13:05:53] <sarang> Doing churn correctly, selecting outputs safely to avoid linking, etc.
    [2019-03-25 13:05:57] <suraeNoether> *nod*
    [2019-03-25 13:06:13] <sgp_> It's certainly a necessary piece of research the community can benefit from
    [2019-03-25 13:06:31] ⇐ TheoStorm quit (~TheoStorm@host-g4sn8hj.cbn1.zeelandnet.nl): Quit: Leaving
    [2019-03-25 13:06:31] <suraeNoether> oh oh, isthmus at noncesense research lab has put a fellow of insight's program onto "automated churn based on best practices," so i've been working with him on enumerating our currently known best practices
    [2019-03-25 13:06:32] <alexanarcho> Is there any graphic representation of the transaction graph?
    [2019-03-25 13:06:55] <sarang> Not that I know of
    [2019-03-25 13:07:07] <suraeNoether> alexanarcho i have done no graphics, but my code at that link above dumps into a text file that hopefully is rather readable, and contains all the information to physically draw out a graph by hand (for a small example)
    [2019-03-25 13:07:29] <sarang> There's always the danger of chasing heuristics with this stuff... but hitting the big ones is a good strategy
    [2019-03-25 13:07:36] <suraeNoether> but, again, that simulator is not yet passing unit tests, so it's almost certain to act wonky right now
    [2019-03-25 13:07:45] <sgp_> suraeNoether: that discussion sounds interesting. I'm happy to lend a hand there
    [2019-03-25 13:08:12] <suraeNoether> sgp_: neat, let's chat with Isthmus_ at the end of the meeting
    [2019-03-25 13:08:38] <sarang> Any other work or news to share suraeNoether ?
    [2019-03-25 13:09:17] <suraeNoether> uhm, monero konferenco update: the schedule is coming really soon(tm) like some time this week
    [2019-03-25 13:10:35] <sarang> Excellent
    [2019-03-25 13:10:36] <suraeNoether> we are essentially all full up for speakers, but i'm holding out for a few folks from the electronic frontier foundation, aviv zohar and yonatan sompolinsky (i think one of them are coming) and either benedikt bunz or his coauthor ben... i can't remember his name and i'm looking it up... (i have a verbal commitment that one of these two are coming to present too)
    [2019-03-25 13:10:53] <suraeNoether> so if anyone wants to submit an abstract, now is last minute. :D
    [2019-03-25 13:11:24] <sarang> Any specific questions for suraeNoether on anything he's discussed?
    [2019-03-25 13:12:08] <sarang> righto
    [2019-03-25 13:12:17] <suraeNoether> ben fisch*
    [2019-03-25 13:12:42] <sarang> I have been working much more on the CLSAG signature scheme brought up by RandomRun in the issue linked in the agenda
    [2019-03-25 13:12:50] <sarang> I have three versions coded now (link in agenda)
    [2019-03-25 13:13:24] <sarang> This scheme compresses ring signatures (probably a bad terminology, but oh well) by reducing the required number of scalars in the signature
    [2019-03-25 13:13:38] <sarang> Recall that right now, we have two forms of MLSAG signatures: full and simple
    [2019-03-25 13:14:06] <sarang> Full has an index linking issue when used with multiple inputs, so we only use it for single-input spends
    [2019-03-25 13:14:18] <sarang> Simple signs each input separately, but has no index problem
    [2019-03-25 13:14:53] <sarang> We can use CLSAG for both full and simple, and even extend it to multi-input full signatures if we decided to stop caring about index linking
    [2019-03-25 13:15:00] — suraeNoether notes: instead of "compresses ring signatures," which makes it seems like we take a usual ring signature and then compress it, this is merely a more compact scheme
    [2019-03-25 13:15:12] <sarang> Sure, we can make the C stand for compact
    [2019-03-25 13:15:17] <sarang> (it needed a name)
    [2019-03-25 13:15:36] <sarang> Based on operation counts, we should see no performance hit in verification, and _possibly_ a slight improvement
    [2019-03-25 13:16:11] <suraeNoether> if that's the case, then we actually save big time a year down the line
    [2019-03-25 13:16:29] <sarang> Anyway, if we were to move to this, we'd save 320 bytes per input (at the current ring size)
    [2019-03-25 13:17:17] <sarang> and it would require adding the new sign/verify scheme, as well as a new custom triple-scalarmult function to handle the expanded key operations
    [2019-03-25 13:17:32] <sarang> but that's very straightforward
    [2019-03-25 13:17:51] <sarang> Kudos to RandomRun for this clever idea
    [2019-03-25 13:17:59] <suraeNoether> small changes in verification time now add up over the next year to hours or days of download+sync time, and are exponentially related to similar changes in space usage. the fact that we save space *and* verification time with this signature scheme adds up to crazy wacky gains over the next year...
    [2019-03-25 13:18:44] <sarang> Confirming the verification savings or cost will require a more complete C++ implementation, of course. These are estimates based on operation counts and the new C++ triple-scalarmult that I added and tested
    [2019-03-25 13:18:51] <sarang> Any specific questions on this?
    [2019-03-25 13:18:57] <oneiric_> any downsides?
    [2019-03-25 13:19:15] <crCr62U0> the same question^
    [2019-03-25 13:19:22] <sarang> We'd need a new security proof to account for the new key aggregation (similar to MuSig)
    [2019-03-25 13:19:48] <sarang> But assuming this, and successful verification testing, it's a definite win
    [2019-03-25 13:19:51] <suraeNoether> ^ that's a good question. i know group operations timing can be exploited to great effect, and i wonder if the triple scalar mult method is more or less vulnerable to side channel analysis by timing than our present method
    [2019-03-25 13:20:07] <sarang> We already use variable timing for key operations
    [2019-03-25 13:20:19] <suraeNoether> yeah, no reason to make it a lot worse, though
    [2019-03-25 13:20:42] <sarang> this is a very straightforward extension to the double version we use now
    [2019-03-25 13:20:50] <sarang> it's neither clever nor novel
    [2019-03-25 13:20:59] <sarang> (the triple function, not CLSAG!)
    [2019-03-25 13:21:13] <suraeNoether> okay, fair enough
    [2019-03-25 13:21:32] <sarang> It would be nice if we could use CLSAG for multi-input with a single signature, but oh well
    [2019-03-25 13:21:36] <midipoet> Is "key aggregation" the linking/combination of key images together to form a transaction? Sorry if dumb question
    [2019-03-25 13:21:38] <sarang> (we'd save a huuuuge amount on space and time)
    [2019-03-25 13:21:45] <suraeNoether> i believe the security proof of clsag is a straightforward thing; sarang do you want me to write up a proof for clsag's unforgeability some time this week, or should we wait to see where development goes on it first? iirc the key images changed in the past week or something like that? is that the case?
    [2019-03-25 13:21:55] <sarang> Key aggregation puts the amount and output key operations into a single operation
    [2019-03-25 13:22:04] <sarang> but does so in a way that prevents tomfoolery
    [2019-03-25 13:22:14] <oneiric_> is it desirable to make the functions constant time? if so, how much effort involved?
    [2019-03-25 13:22:17] <midipoet> Understood
    [2019-03-25 13:22:21] <sarang> We technically add a new "key image" for the amount commitments that isn't used in the same way
    [2019-03-25 13:22:43] <sarang> Ah, relating to key images...
    [2019-03-25 13:22:51] <sarang> There are 2 ways to do CLSAG key images
    [2019-03-25 13:23:13] <suraeNoether> midipoet: yes. musig aggregated user keys to make n-of-n threshold keys. the result is each participant has a secret share and the group has an aggregated key from the combined secrets. clsag aggregates together the one-time/stealth keys with the pedersen commitments to the amount in a 2-of-2 way, and forgets the idea of a crowd of people doing it.
    [2019-03-25 13:23:14] <sarang> One of them keeps the current key image format but adds a second one that doesn't need to be checked for linking (it's only to make the math work)
    [2019-03-25 13:23:47] <sarang> Another version changes key image formats to use a fixed generator point, which could decrease verification time by a bit
    [2019-03-25 13:23:59] <sarang> The timing differences are minor
    [2019-03-25 13:24:39] <suraeNoether> minor like less than 1% difference or minor like same big-oh?
    [2019-03-25 13:24:47] <sarang> Perhaps a few %
    [2019-03-25 13:25:07] <sarang> We could even mix old and new key image styles, but this might make the proofs more complex
    [2019-03-25 13:25:36] <sarang> Anyway, I think now is the time to write the proofs, now that we understand the different versions of this scheme
    [2019-03-25 13:25:58] <suraeNoether> hmm. more than 1% difference in timing is sufficient enough to worry about in terms of the effective space savings. we may have to run some numbers
    [2019-03-25 13:26:06] <suraeNoether> i'll start writing them later this week, then
    [2019-03-25 13:26:43] <sarang> FWIW the current image format is x*H(xG), and the alternate one is x*H (for globally fixed point H)
    [2019-03-25 13:27:12] <sarang> So you'd save by avoiding the hash-to-point and by precomputing multiples for the new generator H
    [2019-03-25 13:27:24] <sarang> Anyway, I have both versions in the linked code
    [2019-03-25 13:27:28] <sarang> Any other questions on CLSAG?
    [2019-03-25 13:27:45] <moneromooo> The CN paper does not mention a particular reason for this extra H() ?
    [2019-03-25 13:27:59] <suraeNoether> does knowing xG and xH provide an advantage in computing x, assuming G and H have an unknown discrete log wrt each other??
    [2019-03-25 13:29:02] <sarang> I am mostly confident that the new format provides the same security, but not completely convinced
    [2019-03-25 13:29:29] <sarang> The option still exists to use CLSAG with the current image format
    [2019-03-25 13:29:52] <sarang> suraeNoether: that is exactly the case we have now, except H = H(X) is a function of the output key
    [2019-03-25 13:29:52] <suraeNoether> let's look into this carefully
    [2019-03-25 13:30:02] <sarang> Yes
    [2019-03-25 13:30:25] <sarang> moneromooo: likely to avoid the structure associated with xX = (x^2)G
    [2019-03-25 13:31:00] → kmels joined (~carlos@2803:7000:6000:1cd6:1cac:2754:b362:eb8a)
    [2019-03-25 13:31:16] <sarang> Anyway: I am also continuing to work on test code for the Lelantus transaction protocol, and also deeper dives into other implementations of the Dandelion++ routing protocol
    [2019-03-25 13:31:34] <sarang> I know of proposals/merges for this in Bitcoin, Grin, and Zcoin
    [2019-03-25 13:31:57] <suraeNoether> oh i didn't realize you were implementing lelantus
    [2019-03-25 13:32:08] <suraeNoether> neat
    [2019-03-25 13:32:29] <sarang> I'm determining if it's feasible as is, or if its components have value elsewhere
    [2019-03-25 13:32:51] <sarang> No plans to implement it, of course
    [2019-03-25 13:32:55] <sarang> only investigating more closely
    [2019-03-25 13:33:05] <suraeNoether> i'll be interested to see how it scales compared to our system, if there's a payoff point.
    [2019-03-25 13:33:21] <sarang> I think there will be a sticking point with scaling commitment sets
    [2019-03-25 13:34:05] <sarang> Finally, thanks to the community for supporting my current open funding request for the next few months
    [2019-03-25 13:34:14] <sarang> That's all I have for now
    [2019-03-25 13:34:27] <sarang> Does anyone else have new work or news to share for the roundtable?
    [2019-03-25 13:35:50] <oneiric_> been reading a lot on signature schemes and LEA for I2P related stuffs
    [2019-03-25 13:36:12] <sarang> Anything of particular interest so far oneiric_ ?
    [2019-03-25 13:36:46] <oneiric_> blake2b sha3 and ed25519ctx are being considered as replacements for sha2 in eddsa
    [2019-03-25 13:37:36] <oneiric_> LEA is particularly important for I2P because messages are signed, rather than H(m)
    [2019-03-25 13:38:02] <suraeNoether> blake is a nice hash function
    [2019-03-25 13:38:13] <oneiric_> OpenSSL already has hooks for Sha3
    [2019-03-25 13:38:18] <suraeNoether> plays nicely with the other hash functions, doesn't throw rocks
    [2019-03-25 13:38:26] <oneiric_> suraeNoether: agree, that's what i'd like too
    [2019-03-25 13:38:55] <oneiric_> if sha3 has the highest likelihood for adoption, that may be what gets used
    [2019-03-25 13:39:06] ⇐ sech1 quit (~sech1@31-208-119-248.cust.bredband2.com): Quit: Leaving
    [2019-03-25 13:39:42] <oneiric_> EOF
    [2019-03-25 13:39:44] <sarang> This is probably hard to quantify, but I wonder which has had the most analysis overall
    [2019-03-25 13:40:01] <oneiric_> my hunch would be sha3
    [2019-03-25 13:40:07] <sarang> as would mine
    [2019-03-25 13:40:18] <sarang> Anyway, that's just my idle musings :D
    [2019-03-25 13:40:21] <sarang> thanks oneiric_ 
    [2019-03-25 13:40:24] <oneiric_> but blake2 is really popular too, especially amongst we crypto nerds
    [2019-03-25 13:40:32] <oneiric_> :) np
    [2019-03-25 13:40:45] <sarang> Let's combine them to make a new function: BLAH-3
    [2019-03-25 13:40:47] <sarang> =p
    [2019-03-25 13:40:52] ⇐ vtnerd_ quit (~Lee@173-23-103-30.client.mchsi.com): Ping timeout: 245 seconds
    [2019-03-25 13:40:52] <suraeNoether> i've been reading up on the parazoa extension of the keccak sponge, it's weird and interesting
    [2019-03-25 13:41:00] <oneiric_> lol
    [2019-03-25 13:41:12] <suraeNoether> but that's my "funtime" ie post coffee preshower reading
    [2019-03-25 13:41:28] <sarang> OK, let's move to 3. QUESTIONS
    [2019-03-25 13:41:29] <oneiric_> ooo sounds fancy
    [2019-03-25 13:41:45] <sarang> Any general questions or observations on past, current, or ongoing research before we wrap up?
    [2019-03-25 13:41:51] <OsrsNeedsF2P> Question regarding inputs. We had some discussions last night, but I wanted to bring up how if you only receive 1 input, you can only send 1 transaction at a time. sweep_all works, but it would be better if there was more leniency altogether. Can this be done?
    [2019-03-25 13:42:23] <moneromooo> It can be done, using the settings I mentioned yesterday.
    [2019-03-25 13:42:23] <sarang> Specific qualms with sweep?
    [2019-03-25 13:42:53] <OsrsNeedsF2P> sarang: User experience, and only official wallet supports
    [2019-03-25 13:43:13] <OsrsNeedsF2P> moneromoo: do you have any suggestions on the parameters you were mentioning?
    [2019-03-25 13:43:18] <sarang> Hmm, I wonder how much of this is a UX issue given the current support
    [2019-03-25 13:43:37] <moneromooo> Sure, count to 5, value to 0.
    [2019-03-25 13:44:02] <moneromooo> Of course outputs will dwindle to 1 if you're sending large amounts. In that case, split again.
    [2019-03-25 13:44:35] → vtnerd joined (~Lee@173-23-103-30.client.mchsi.com)
    [2019-03-25 13:44:39] <OsrsNeedsF2P> Is this a wallet level implementation, or is this something the RPC would handle on its own? (might be a dumb question)
    [2019-03-25 13:44:42] <moneromooo> (which can be done at the same time as sending a tx to someone else)
    [2019-03-25 13:44:49] <moneromooo> wallet
    [2019-03-25 13:45:02] <moneromooo> The RPC would also do.
    [2019-03-25 13:45:15] <moneromooo> Oh, speaking of RPC.
    [2019-03-25 13:45:34] <moneromooo> https://github.com/monero-project/monero/pull/5331/commits/c7bfdc356618fd1ccbe0f87fd5009e944cd12e50 will allow people to extract blockchain data (ie, nonces, difficulty, block times, etc) and process them with python.
    [2019-03-25 13:45:46] <sarang> Excellent
    [2019-03-25 13:46:10] <sarang> pinging Isthmus_ and associates, who may be particularly interested in this
    [2019-03-25 13:47:06] <sarang> I look forward to testing this moneromooo 
    [2019-03-25 13:48:18] <sarang> Any other general questions?
    [2019-03-25 13:48:30] <sarang> If not, we'll move to 4. ACTION ITEMS
    [2019-03-25 13:49:44] <sarang> This week, I'll continue wrapping up the initial work on CLSAG, continue coding on Lelantus components, and finalize some observations on Dandelion++ routing
    [2019-03-25 13:49:51] <sarang> suraeNoether: ?
    [2019-03-25 13:50:49] <sarang> (a note that Dandelion is client-opt-in and doesn't require a fork, whereas CLSAG would be)
    [2019-03-25 13:52:29] <midipoet> With regards dandelion++ afaik Grin have just release a rewrite of the code, of that is of any interest
    [2019-03-25 13:52:43] <sarang> aye
    [2019-03-25 13:52:58] <suraeNoether> hi sorry, i got distracted
    [2019-03-25 13:52:58] <oneiric_> link?
    [2019-03-25 13:53:15] <suraeNoether> my action items involve some paperwork with dlsag and generating our simulation results for matching.
    [2019-03-25 13:53:16] <sarang> They have extended their version to include some aspects of input-output collapsing (or whatever they call it)
    [2019-03-25 13:53:33] <suraeNoether> i think there's a good chance we are going to be able to push mrl-11 out the door in the next few weeks
    [2019-03-25 13:53:34] <sarang> Excellent; hopefully we can get the CLSAG proofs hammered out with ease
    [2019-03-25 13:53:59] <suraeNoether> i think clsag proofs will be tomorrow afternoon, tbh
    [2019-03-25 13:54:00] <midipoet> https://github.com/mimblewimble/grin/pull/2628
    [2019-03-25 13:54:08] <suraeNoether> i'm blocking off my 2-5pm time for that sarang
    [2019-03-25 13:54:42] <oneiric_> thanks midipoet
    [2019-03-25 13:54:51] <midipoet> yw
    [2019-03-25 13:55:46] <sarang> Interesting that Grin wanted to address the stem/fluff phase per epoch and not per transaction
    [2019-03-25 13:55:56] <sarang> This was a subtle point in the paper
    [2019-03-25 13:56:11] <sarang> Anyway, other action items to wrap up?
    [2019-03-25 13:57:04] <sarang> Well, thanks to everyone for attending today
    [2019-03-25 13:57:10] <sarang> Logs will be posted to the agenda issue shortly
    [2019-03-25 13:57:15] <sarang> We are now adjourned!
    [2019-03-25 13:57:31] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-03-22T13:02:04+00:00
- Closed at: 2019-03-25T18:00:57+00:00
