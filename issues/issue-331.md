---
title: 'Research meeting: 22 April 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/331
author: SarangNoether
assignees: []
labels: []
created_at: '2019-04-19T18:36:30+00:00'
updated_at: '2019-04-22T17:57:35+00:00'
type: issue
status: closed
closed_at: '2019-04-22T17:57:35+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 22 April 2019 @ 17:00 UTC
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
## b-g-goodell | 2019-04-22T01:21:13+00:00
To discuss under Surae:

1. Using Clemson University as a testbed for academic collaboration with MRL:
    a. Collaborative research at Clemson University with Gao: practical FHE in the RLWE setting, ring signatures in RLWE setting, STARK research, analysis of NIST PQ competition algos, and large-anon-set-authentication.
    b. Collaborative research at Clemson University with Sather-Wagstaff: using homological algebra to make Squaresig go. Hey @SarangNoether what rhymes with "BEST" and takes five semesters of algebra to get defined for you and is based on projective resolutions and totally parameterize short exact sequences of R-modules and so can be used to parameterize Squaresig? Hint: it's on either the left wrist or the right wrist, and I always get them confused.

2. MRL11 update: Newly broken code, new unit tests, etc. Soon^TM


## SarangNoether | 2019-04-22T17:57:35+00:00
    [2019-04-22 12:59:49] <sarang> OK, let's begin. Logs of this meeting will be posted to the GitHub link afterward
    [2019-04-22 12:59:55] <sarang> 1. GREETINGS
    [2019-04-22 12:59:57] <sarang> hello
    [2019-04-22 13:00:58] <sgp_> hello!
    [2019-04-22 13:01:43] ⇐ TheoStorm quit (~TheoStorm@host-g4sn8hj.cbn1.zeelandnet.nl): Remote host closed the connection
    [2019-04-22 13:01:51] <sarang> I assume suraeNoether is also here
    [2019-04-22 13:02:46] <sarang> I suppose we can move to 2. ROUNDTABLE
    [2019-04-22 13:03:22] <sarang> The new output selection algorithm was put into a PR by moneromooo with some additional tests added; many thanks to moneromooo for that work
    [2019-04-22 13:03:25] <sarang> and it's now merged
    [2019-04-22 13:03:50] <sarang> This helps to mitigate the block weighting issues and provide better selection
    [2019-04-22 13:03:59] ⇐ TABulator quit (ac3a989b@gateway/web/freenode/ip.172.58.152.155): Ping timeout: 256 seconds
    [2019-04-22 13:04:14] <sarang> The attempted CLSAG proof reduction to LSAG was not successful because of the way key images are computed, unfortunately
    [2019-04-22 13:04:27] <sarang> However, I've been working on applying the MLSAG proof techniques more directly
    [2019-04-22 13:04:33] → TABulator joined (~androirc@2607:fb90:509a:93cd:e9e3:dd35:708a:462)
    [2019-04-22 13:04:33] <suraeNoether> howdy, sorry
    [2019-04-22 13:04:35] <suraeNoether> distrated
    [2019-04-22 13:04:41] <suraeNoether> I'm here
    [2019-04-22 13:04:58] <sarang> I'm still working with the Lelantus paper author, a Zcoin cryptographer, to offer some collaborative insight on efficiency gains
    [2019-04-22 13:05:14] <sarang> Just about finished with test code refactoring, and some additional fixes
    [2019-04-22 13:05:34] <suraeNoether> what sort of gains are you talking about there?
    [2019-04-22 13:05:40] <suraeNoether> what is lelantus, and why is it interesting?
    [2019-04-22 13:05:45] — suraeNoether devils advocate
    [2019-04-22 13:06:01] <sarang> It's a transaction protocol produced by a Zcoin researcher that uses some of the techniques that StringCT also used
    [2019-04-22 13:06:14] <sarang> but with a more direct balance proof
    [2019-04-22 13:06:40] <sarang> The paper suggested some batching speedups, but I observed that you could apply them much more broadly to the entire set of transaction proofs (there are several)
    [2019-04-22 13:07:06] <suraeNoether> neat! are you two narrowing down on some concrete numbers for comparison in efficiency?
    [2019-04-22 13:07:11] <suraeNoether> what sort of work remains, in that regard?
    [2019-04-22 13:07:40] <sarang> A lot of the batching gains depend heavily on the anonymity set used
    [2019-04-22 13:07:47] <sarang> and there are plenty of open questions about that
    [2019-04-22 13:08:22] <sarang> But, for example, the bulk of a spend proof (ignoring balance proof and range proofs) for a 1024-size anonymity set is probably about 100 ms using Monero timing operations
    [2019-04-22 13:08:33] <suraeNoether> wow
    [2019-04-22 13:08:35] <suraeNoether> wowow
    [2019-04-22 13:08:52] <sarang> This is purely back-of-the-envelope
    [2019-04-22 13:08:52] <suraeNoether> for those in the audience, i tend to think of 50 ms is on the border of too slow
    [2019-04-22 13:08:59] <suraeNoether> does 512 anon set take 50 ms?
    [2019-04-22 13:09:02] <suraeNoether> is it logarithmic?
    [2019-04-22 13:09:11] <sarang> mostly linear
    [2019-04-22 13:09:21] <sarang> keep in mind that batching verification reduces the cost per proof
    [2019-04-22 13:09:38] <sarang> I don't have good numbers for that yet
    [2019-04-22 13:09:38] <suraeNoether> oh man, we should talk about the space-time tradeoff
    [2019-04-22 13:09:45] <suraeNoether> asymptotically
    [2019-04-22 13:09:48] <sarang> Yeah, I'll be working up a set of charts for this
    [2019-04-22 13:09:54] <suraeNoether> fantastic.
    [2019-04-22 13:10:10] <sarang> For reference, an MLSAG verification with 1024 ringsize takes 1.2 s
    [2019-04-22 13:11:20] <sarang> Also the kind of batching that I'm thinking of as being most useful requires the batch to use the same decoy anonymity set
    [2019-04-22 13:11:33] <suraeNoether> oh that's sort of an omniring property
    [2019-04-22 13:11:42] <sarang> You still get some gains without this assumption, but not nearly to the same degree
    [2019-04-22 13:11:57] <suraeNoether> which we'll be learning about at the konferenco, apparently :) real_or_random
    [2019-04-22 13:12:00] <sarang> Using a common set means your multiexp operation uses the same generators across proofs (mostly)
    [2019-04-22 13:12:10] <suraeNoether> of course, i haven't seen omniring yet...
    [2019-04-22 13:12:28] <sarang> Anyway, other questions for me?
    [2019-04-22 13:13:40] <suraeNoether> Good recap, sarang, thanks for describing it to us
    [2019-04-22 13:13:42] <suraeNoether> *claps*
    [2019-04-22 13:13:47] <sarang> Over to you suraeNoether 
    [2019-04-22 13:14:07] ⇐ crCr62U0 quit (~crCr62U0@gateway/tor-sasl/crcr62u0): Ping timeout: 256 seconds
    [2019-04-22 13:14:15] <suraeNoether> well, the past week has been busy for surae
    [2019-04-22 13:14:20] <sarang> https://www.youtube.com/watch?v=0TeFrpLL4-E
    [2019-04-22 13:14:27] — sarang is done now
    [2019-04-22 13:14:30] ⇐ TABulator quit (~androirc@2607:fb90:509a:93cd:e9e3:dd35:708a:462): Ping timeout: 252 seconds
    [2019-04-22 13:14:34] <suraeNoether> MRL 11 update: I finally found the problem with my simulation code, which had to do with passing around an identity for objects like nodes and edges that can be used to retrieve the object, versus passing around the object itself. it's a silly and embarassing mistake, and it took me way too much time to figure out why things were going wrong. :P
    [2019-04-22 13:14:48] → TABulator joined (~androirc@2607:fb90:509a:93cd:e9e3:dd35:708a:462)
    [2019-04-22 13:14:54] <suraeNoether> I made a push this morning to my mrl-skunkworks powerpuff branch after finally realizing the problem
    [2019-04-22 13:15:26] <suraeNoether> that includes the new experimenter class that is actually generating confusion tables... the data it spits out (information for a confusion table) is junk and incorrect, but it doesn't break anything, so I pushed it.... The overall infrastructure is at the point where it may be of interest to #noncesense-research-lab and Isthmus for independent work.
    [2019-04-22 13:15:31] <suraeNoether> or anyone else who is interested
    [2019-04-22 13:15:48] <suraeNoether> https://github.com/b-g-goodell/mrl-skunkworks/tree/matching-powerpuff/Matching
    [2019-04-22 13:15:49] <sarang> What are your next steps for this (jumping ahead a bit)?
    [2019-04-22 13:15:56] <suraeNoether> the main idea is this
    [2019-04-22 13:16:26] <suraeNoether> how accurate is the matching approach as ring size scales up? how accurate is the matching approach as churn number increases? how can we use the answers to these questions to formulate best practices for monero churners?
    [2019-04-22 13:16:42] <sarang> for sure
    [2019-04-22 13:16:43] <suraeNoether> is there a way we can define some concrete threshold we want to attain?
    [2019-04-22 13:17:21] <sarang> Understanding how ring size and some specified churn behaviors affect these matching heuristics can give a much clearer picture of what it would take to hit certain thresholds
    [2019-04-22 13:17:57] <suraeNoether> anyway, that's my progress update on MRL11: soon^TM. I'm actually getting results without breaking anything, and now it's a matter of debugging the code and writing new tests to ensure that the results I'm getting are consistent
    [2019-04-22 13:18:08] <suraeNoether> but I also have a collaborative update, as described in the agenda
    [2019-04-22 13:19:04] → luigi1111w joined (~luigi1111@unaffiliated/luigi1111)
    [2019-04-22 13:19:04] * ChanServ set +o luigi1111w
    [2019-04-22 13:19:05] <suraeNoether> long story short: Clemson University's School of Mathematical and Statistical Sciences is interested in starting a general center for blockchain and cryptocurrency studies.
    [2019-04-22 13:19:15] → crCr62U0 joined (~crCr62U0@gateway/tor-sasl/crcr62u0)
    [2019-04-22 13:19:22] <suraeNoether> and they are interested in involving Monero Research Lab in their efforts.
    [2019-04-22 13:19:31] <endogenic> coolio
    [2019-04-22 13:19:48] <suraeNoether> we have a few interesting research collaboration possibilities with clemson just stand-alone, new shiny blockchain center notwithstanding
    [2019-04-22 13:20:17] <suraeNoether> mainly: Professor Shuhong Gao is in the middle of writing several papers that promise to be rather groundbreaking
    [2019-04-22 13:20:40] <suraeNoether> one of these is reporting a purported attack upon two of the post-quantum nist candidate encryption algorithms
    [2019-04-22 13:20:55] <suraeNoether> one of these is a new approach to fully homomorphic encryption
    [2019-04-22 13:21:25] <sarang> sounds very interesting
    [2019-04-22 13:21:43] <suraeNoether> previous attempts at FHE suffer weird problems. if you want to add two ciphertexts together, it's easy to retain the number of bits. but to do something like multiplication, you need a larger number of bits than either ciphertext... and so previous approahces sort of use this expanding scratchpad of bits and take up lots of space to perform a computation
    [2019-04-22 13:22:02] <suraeNoether> gao has developed a way that improves the space efficiency by several orders of magnitude, bringing *practical* FHE into reality
    [2019-04-22 13:22:29] <suraeNoether> his approaches use the RLWE cryptographic setting, which I've been looking into recently due to its speed (big keys but very fast algorithms)
    [2019-04-22 13:22:31] <sarang> sounds suspiciously interesting
    [2019-04-22 13:22:34] ⇐ dollner quit (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de): Remote host closed the connection
    [2019-04-22 13:22:38] <suraeNoether> yeah, no kidding
    [2019-04-22 13:23:13] <suraeNoether> he has four visiting scholars interested in blockchain and a handful of students, and the next thing on their plate is RLWE-based STARKs efficient enough for use in something like Monero
    [2019-04-22 13:23:25] <suraeNoether> so, basically: I'm super excited about the possibility of collaborating with these folks!
    [2019-04-22 13:23:32] → dollner joined (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de)
    [2019-04-22 13:23:50] <sarang> Nice
    [2019-04-22 13:24:04] ⇐ dollner quit (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de): Remote host closed the connection
    [2019-04-22 13:24:25] <suraeNoether> conflict of interest disclosure: Clemson flew me out to South Carolina last week and put me up in a hotel and fed me. I gave a talk. I received a per diem for food. This is all rather ordinary in that regard.
    [2019-04-22 13:24:48] → dollner joined (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de)
    [2019-04-22 13:24:48] <suraeNoether> so, i'm encouraging that Clemson have a presence at the Monero Konferenco, to come meet members of the monero community in person
    [2019-04-22 13:25:03] <suraeNoether> and I'm encouraging their graduate students to jump in on our research meetings
    [2019-04-22 13:25:45] <endogenic> awesome!
    [2019-04-22 13:25:53] <sarang> Totally; getting more researchers involved is great for the project
    [2019-04-22 13:26:00] — moneromooo approves
    [2019-04-22 13:26:15] <suraeNoether> I want them to come to the Konferenco, meet some of the folks in the Monero community face to face, and contribute to Monero's development. I think this is a good thing both for Monero and Clemson University, and I think a more formal academic collaboration with Monero Research Lab is long overdue.
    [2019-04-22 13:26:18] <suraeNoether> also, for what it's worth
    [2019-04-22 13:26:31] <suraeNoether> the last time I was at clemson, speaking with people about cryptocurrency or privacy as a human right was a hard conversation to have
    [2019-04-22 13:26:40] <suraeNoether> this time, the conversations went... very... very .... differently.
    [2019-04-22 13:26:43] <suraeNoether> a lot changes in 3 years.
    [2019-04-22 13:26:49] <suraeNoether> people are excited about this.
    [2019-04-22 13:27:28] <endogenic> what would you say is the origin of the change in their reactoin?
    [2019-04-22 13:27:38] <endogenic> fungibility?
    [2019-04-22 13:27:42] <suraeNoether> uhm
    [2019-04-22 13:27:49] <endogenic> cause the Snowden disclosures etc came out a long time ago
    [2019-04-22 13:27:50] <suraeNoether> actually, i think it's structural
    [2019-04-22 13:28:03] <suraeNoether> meaning: the right people are in control right now for this to move, if that makes sense
    [2019-04-22 13:28:09] <endogenic> gotcha
    [2019-04-22 13:28:26] <sarang> Any other new work to share suraeNoether ?
    [2019-04-22 13:28:31] <suraeNoether> different people standing between the department and their goals than last time, like deans and provosts...
    [2019-04-22 13:28:34] ⇐ dollner quit (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de): Remote host closed the connection
    [2019-04-22 13:28:43] <suraeNoether> uhm, also, on a totally wild and weird research note
    [2019-04-22 13:28:57] → dollner joined (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de)
    [2019-04-22 13:29:23] <suraeNoether> it turns out a homological algebra construction called Ext that Sarang and I studied in grad school together may be the key to forcing my silly signature scheme using commutative/cartesian squares from last year to work
    [2019-04-22 13:29:52] <suraeNoether> so I'm discussing a paper with another clemson professor
    [2019-04-22 13:30:05] <sarang> very clever
    [2019-04-22 13:30:14] <suraeNoether> that's pretty close to the "pure math" end of the spectrum for this room, so i'm not sure whether i should talk about it before we have some more results
    [2019-04-22 13:30:22] → dollner2 joined (~dollner4@p5B10A396.dip0.t-ipconnect.de)
    [2019-04-22 13:30:34] <suraeNoether> it turns out that Ext can be used to parameterize the zero function between two modules (like, for example, elliptic curve groups)
    [2019-04-22 13:30:47] <suraeNoether> so we are trying to use that to hide information in a function from one to the other
    [2019-04-22 13:30:52] <suraeNoether> it's... bizarre, and it might just work!
    [2019-04-22 13:32:08] <suraeNoether> and tha'ts all I have other than action items
    [2019-04-22 13:32:33] <sarang> neato
    [2019-04-22 13:32:35] <suraeNoether> but this is round-table and perhaps andytoshi or real_or_random or ArticMine have some thoughts on stuff they've been working o.
    [2019-04-22 13:32:42] <sarang> Does anyone else have research work of interest to share?
    [2019-04-22 13:32:42] <suraeNoether> or anyone else, for that matter
    [2019-04-22 13:33:07] ⇐ dollner quit (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de): Ping timeout: 250 seconds
    [2019-04-22 13:34:58] <sarang> righto
    [2019-04-22 13:35:18] <sarang> I guess we can move to 3. QUESTIONS and/or 4. ACTION ITEMS
    [2019-04-22 13:36:16] — Isthmus wanders in lote
    [2019-04-22 13:36:23] <endogenic> eyyyyy
    [2019-04-22 13:36:24] <Isthmus> *late
    [2019-04-22 13:36:24] <suraeNoether> oooh isthmus
    [2019-04-22 13:36:31] <suraeNoether> do you have an update beefore we move onto 3?
    [2019-04-22 13:37:07] <Isthmus> Been working on playing around with camel emission curves, though that window has probably shut for Monero
    [2019-04-22 13:37:43] <Isthmus> Also, @n3ptune and I looked at single-transaction outputs in recentish history. There are O(1000) of them
    [2019-04-22 13:37:47] <Isthmus> https://github.com/monero-project/monero/issues/5399
    [2019-04-22 13:38:21] <Isthmus> https://usercontent.irccloud-cdn.com/file/YyM3h9KG/image.png
    [2019-04-22 13:38:28] <Isthmus> TL;DR:
    [2019-04-22 13:38:29] <Isthmus> There have been over 2500+ single-output transactions since 2017
    [2019-04-22 13:38:33] <Isthmus> Single-output transactions (1OTXs) are a persistent intermittent phenomen
    [2019-04-22 13:38:39] <Isthmus> *phenomena
    [2019-04-22 13:38:44] <Isthmus> There was a surge of 1OTXs around height 1562000
    [2019-04-22 13:38:49] <Isthmus> 1OTXs are observed to this day (data includes 2019)
    [2019-04-22 13:39:07] <suraeNoether> hm
    [2019-04-22 13:39:32] <sarang> Could be made consensus, which has been brought up before without any movement
    [2019-04-22 13:39:33] <Isthmus> They're also linked to a lot of other nasty heuristics - odd ring sizes, fees that stick out by an order of magnitude, etc.
    [2019-04-22 13:42:32] <sarang> that spike is crazy
    [2019-04-22 13:43:34] ⇐ dollner2 quit (~dollner4@p5B10A396.dip0.t-ipconnect.de): Remote host closed the connection
    [2019-04-22 13:43:46] <Isthmus> Yeah, epic churn event. Should be pretty easy to dissect and trace, but I left that as an exercise for the reader.
    [2019-04-22 13:44:14] → dollner joined (~dollner4@p200300E63728070030951A8FE58C08F6.dip0.t-ipconnect.de)
    [2019-04-22 13:44:52] <endogenic> bet that was sgp
    [2019-04-22 13:44:56] <sarang> All right, let's go to action items
    [2019-04-22 13:44:58] <sarang> suraeNoether: ?
    [2019-04-22 13:45:07] <sgp_> This should be consensus. Isthmus opened a GitHub issue, and I don't think anyone has voiced opposition to it
    [2019-04-22 13:46:15] <luigi1111w> 2 output min is good
    [2019-04-22 13:46:26] <sarang> absolutely
    [2019-04-22 13:47:18] <Isthmus> Oh yea, if you have thoughts, leave them here: https://github.com/monero-project/monero/issues/5399
    [2019-04-22 13:47:24] <Isthmus> Otherwise, good to move on
    [2019-04-22 13:47:59] <charuto> could the spike on 1output transactions be somehow related to monero classic/original ? date seems to almost coincide.
    [2019-04-22 13:51:15] <sarang> OK, in the interest of hitting our 1-hour target, I'll work up numbers for batch Lelantus verification at varying anonymity set sizes, and finish up some example code refactoring to complete that project
    [2019-04-22 13:51:56] <sarang> I'm also looking into how a new transaction type could be used to transition RingCT outputs to this
    [2019-04-22 13:52:35] <sarang> Submission of the DLSAG paper is finally happening
    [2019-04-22 13:52:44] <sarang> suraeNoether: ?
    [2019-04-22 13:52:51] <suraeNoether> woops, sorry, my action items all revolve around getting my simulations done and some confusion tables pushed out
    [2019-04-22 13:52:58] <sarang> great, thanks
    [2019-04-22 13:52:58] <suraeNoether> after that i can go do other things
    [2019-04-22 13:53:11] — suraeNoether humbly apologizes
    [2019-04-22 13:53:15] <sarang> Thanks to Isthmus for opening that issue and getting the conversation started again on 1-out txns
    [2019-04-22 13:53:27] <Isthmus> 👍
    [2019-04-22 13:54:08] <sarang> Any other final thoughts before we adjourn and return to general discussion?
    [2019-04-22 13:54:10] <Isthmus> Also, interesting hypothesis @charuto - might be connected. XMC forked off at 1546000 and the 1OTX spike is around 1560000
    [2019-04-22 13:55:21] <sarang> OK, we are now adjourned! Logs will be posted to the GitHub issue shortly. Thanks to everyone for attending; let the discussions continue
    [2019-04-22 13:55:34] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-04-19T18:36:30+00:00
- Closed at: 2019-04-22T17:57:35+00:00
