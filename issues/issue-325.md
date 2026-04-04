---
title: 'Research meeting: 1 April 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/325
author: SarangNoether
assignees: []
labels: []
created_at: '2019-04-01T14:16:17+00:00'
updated_at: '2019-04-01T17:38:41+00:00'
type: issue
status: closed
closed_at: '2019-04-01T17:38:41+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 1 April 2019 @ 17:00 UTC
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
## SarangNoether | 2019-04-01T17:38:41+00:00
    [2019-04-01 12:59:34] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/325. Be excellent to each other.
    [2019-04-01 12:59:41] <suraeNoether> hi everyone!
    [2019-04-01 12:59:45] <sarang> Hello all
    [2019-04-01 12:59:47] <suraeNoether> nice topic choice btw
    [2019-04-01 12:59:48] <sgp_> hello
    [2019-04-01 12:59:49] <sarang> 1. GREETINGS
    [2019-04-01 13:00:21] <Xeagu> Hello!
    [2019-04-01 13:01:10] <sarang> Since others may join over time, let's go ahead and jump to 2. ROUNDTABLE
    [2019-04-01 13:01:31] <sarang> Jointly, suraeNoether and I have been working on formalization of the compact CLSAG signature scheme
    [2019-04-01 13:01:40] <suraeNoether> muah ha ha
    [2019-04-01 13:01:50] ⇐ cardboardoranges quit (~cardboard@65.112.8.6): Quit: cardboardoranges
    [2019-04-01 13:01:52] <sarang> The choice of how keys are aggregated likely affects the security proofs
    [2019-04-01 13:02:04] <sarang> and this also affects the efficiency, so I'll continue investigating the effects of this
    [2019-04-01 13:02:21] <suraeNoether> so, it turns out that one variant of CLSAG is easily provably secure assuming LSAGs are secure, and the variant initially proposed by randomrun is easily proven secure similarly to previous approaches...
    [2019-04-01 13:02:23] <sarang> any thoughts to add on this suraeNoether since it's a project we're both on?
    [2019-04-01 13:02:48] <suraeNoether> yep! so the fun part about this scheme is that it makes ring signatures with R ring members take up R+1 scalars only. previously it was 2R+1, I believe...
    [2019-04-01 13:03:01] <sarang> The original proposal has slightly more efficient computation
    [2019-04-01 13:03:17] <sarang> The variant suraeNoether is thinking of would add perhaps 60 us of verification time (on my test machine)
    [2019-04-01 13:03:17] <suraeNoether> yeah. and while this seems nice and all alone on it's face, but this is actually sort of a deeper compactification than I originally thought...
    [2019-04-01 13:03:27] <suraeNoether> *nod* that variant is the "easily proven secure" variant
    [2019-04-01 13:03:36] <sarang> Yep
    [2019-04-01 13:03:45] <sarang> Certainly worthwhile to get proofs for the original, to save that time
    [2019-04-01 13:04:26] <sarang> I'm working on some modifications to the underlying C++ crypto plumbing to accommodate this
    [2019-04-01 13:04:35] <suraeNoether> so, what's really cool about this is: using our previous signatures, we could pull off "colored coin" transactions in RingCT... but it felt like there could only be one color for the outputs, and the signatures were proportionally sized to the number of colors
    [2019-04-01 13:04:40] <sarang> Nothing major, just a few straightforward extensions to what we have now
    [2019-04-01 13:05:05] <suraeNoether> using this compactification, a really easily written version of colored ringct can be developed where all signatures are R+1-sized, regardless of teh number of colors
    [2019-04-01 13:05:37] <suraeNoether> verification time will take the same amount of time as it would have before, but it removes the dependency of the signature size on the number of colors, which is neat
    [2019-04-01 13:05:43] <sarang> Yeah, the key aggregation idea, coupled with optional changes to key image format, has a lot of neat directions to go
    [2019-04-01 13:05:52] <Xeagu> Wait Monero colored coins?
    [2019-04-01 13:05:59] <suraeNoether> i think i'm on page 6 of a new document describing all the above. proofs and stuff and all... it's pretty much written itself.
    [2019-04-01 13:06:05] <sarang> Xeagu: only as a hypothetical
    [2019-04-01 13:06:10] <suraeNoether> Xeagu it would be *possible* to implement it this way
    [2019-04-01 13:06:13] <suraeNoether> i'm not recommending that we *do*
    [2019-04-01 13:06:25] <Xeagu> Wow very interesting
    [2019-04-01 13:06:30] <suraeNoether> i'm pointing out that one of the technical challenges involving scaling the blockchain to the number of colors has been removed
    [2019-04-01 13:06:46] <suraeNoether> which is neat, but i'm not convinced Monero Gold and Monero Silver need to be a thing. :P
    [2019-04-01 13:06:47] <sarang> For sure. No timeline on CLSAG integration yet, nor formal talk about whether or not we intend to
    [2019-04-01 13:07:14] <suraeNoether> ^ although compactifying our present RingCT is a high priority, because it will save hours or more of sync time within only a year.
    [2019-04-01 13:07:17] <Xeagu> Would such an implementation compete with Tari for digital assets?
    [2019-04-01 13:07:46] <sarang> I don't think the project would want to target that use case
    [2019-04-01 13:08:21] <Xeagu> Got it. Was just thinking that Counterparty works because of colored coins.
    [2019-04-01 13:08:26] <sarang> but it's nice to have such a useful signature scheme available and understood
    [2019-04-01 13:09:22] <sarang> Otherwise, I've been plugging away at an example implementation of the Lelantus transaction protocol, which was recently updated by its author
    [2019-04-01 13:09:33] <sarang> so I'm going back to make changes etc.
    [2019-04-01 13:09:59] <sarang> suraeNoether: other things to report?
    [2019-04-01 13:10:46] <suraeNoether> oh i put an hour or two into a small new side project this weekend i'm thinking of calling SlyHash
    [2019-04-01 13:11:09] <Xeagu> What is SlyHash?
    [2019-04-01 13:11:31] → jtgrassie joined (~jtgrassie@monerop.com)
    [2019-04-01 13:11:47] <suraeNoether> i'm inventing it and naming it after sly and the family stone, the funk band. :P the goal of this project is to design a parazoa-based hash function as a toy (emphasis on toy) proof of work algorithm, with the goal of experimenting with power and timing properties, etc... parazoa is the generalization of the sponge approach used to design keccak
    [2019-04-01 13:12:19] <sarang> You were investigating the applications of this as a VDF, correct?
    [2019-04-01 13:12:41] <suraeNoether> yeah! hopefully. :P
    [2019-04-01 13:12:51] <Xeagu> I don't know what keccak or VDF are
    [2019-04-01 13:13:14] <sarang> Keccak is the algorithm that was used (slightly modified) as SHA-3
    [2019-04-01 13:13:23] <sarang> a VDF is a verifiable delay function
    [2019-04-01 13:13:31] <suraeNoether> but i want to design it to be really dumb to compute, like using permutation polynomials instead of ciphers for permutations, and so on. it's ... a dumb little side thing that may end up evolving into something more sophisticated (so maybe parazoa was a good choice), but for now i'm literally just measuring how close to "ideal" a randomly selected permutation polynomial of a specific form is. if i find a good
    [2019-04-01 13:13:31] <suraeNoether> one in the first 12.5 million cases, i'll implement it. if not, i'm throwing the project out the window
    [2019-04-01 13:13:55] <sarang> neat
    [2019-04-01 13:14:16] <Xeagu> Might consider designing such that it would be cheap/easy to ASIC
    [2019-04-01 13:15:34] <sarang> Any questions for suraeNoether?
    [2019-04-01 13:16:25] <sarang> OK, does anyone else have interesting work to share?
    [2019-04-01 13:16:36] <Xeagu> Yes I have something
    [2019-04-01 13:16:39] <sarang> sure
    [2019-04-01 13:16:44] <Xeagu> A YouTube video I made
    [2019-04-01 13:16:47] <Xeagu> https://youtu.be/7t6ikOnTbcM
    [2019-04-01 13:16:58] <sarang> What is the topic?
    [2019-04-01 13:17:05] <Xeagu> First of a series on something I call CrypARTgraphy
    [2019-04-01 13:17:12] <Xeagu> Using art to encrypt messages
    [2019-04-01 13:17:29] <sarang> Similar to the idea of steganography?
    [2019-04-01 13:18:18] <Xeagu> Not quite no. More like combining related symbology and the relationship between ideas to create paralleled meaning.
    [2019-04-01 13:18:39] <sarang> I'm not really sure what that means, I must admit
    [2019-04-01 13:18:47] <sarang> (but I have not yet watched the video)
    [2019-04-01 13:19:45] <Xeagu> I have some ideas for applying the math of ECC where the variables and prime numbers are substituted with ideas, objects, and art from stories or events
    [2019-04-01 13:20:33] <Xeagu> Math is fundementally logic and stories (art) contain variables with logical relationships
    [2019-04-01 13:21:22] <sarang> Thanks Xeagu 
    [2019-04-01 13:21:34] <sgp_> I have a quick comment
    [2019-04-01 13:21:35] <sarang> I know sgp_ also had something to mention about the upcoming 5-year genesis block anniversary as well?
    [2019-04-01 13:21:39] <sarang> aha go ahead
    [2019-04-01 13:21:40] <sgp_> Yes
    [2019-04-01 13:21:45] <sgp_> https://github.com/monero-project/meta/issues/324
    [2019-04-01 13:22:13] <sgp_> This isn't strictly research-related, but I would like the recommendations and participation of researchers in Monero's upcoming 5 year "Moneroversary"
    [2019-04-01 13:22:31] <sgp_> If you can comment your availability and desired events in the Github issue, that would be greatly appreciated
    [2019-04-01 13:22:45] <sgp_> that's all, unless there are any quick questions
    [2019-04-01 13:22:55] <sarang> It would be neat to take a 30K foot view of how Monero has evolved technically over time
    [2019-04-01 13:23:09] <sarang> What has been accomplished, and what still needs work
    [2019-04-01 13:23:35] <sgp_> Yes, I expect a good portion to cover Monero's history. Focusing on the technical changes over time is an area where you all can help :)
    [2019-04-01 13:24:49] → cardboardoranges joined (~cardboard@65.112.10.91)
    [2019-04-01 13:25:02] <sarang> OK, so that's about 2.5 weeks away
    [2019-04-01 13:25:45] <sarang> thanks sgp_ 
    [2019-04-01 13:25:51] <Xeagu> Konferenco is about 2.5 months away
    [2019-04-01 13:25:55] <sgp_> yes, so the sooner I get feedback, the better
    [2019-04-01 13:25:58] <sarang> Ah, so it is
    [2019-04-01 13:26:22] <sarang> Attendance seems fairly sparse today, but does anyone else have research work to share?
    [2019-04-01 13:26:34] <sarang> Otherwise we can move on with this (fairly quick) agenda
    [2019-04-01 13:26:59] <sgp_> oh one more thing
    [2019-04-01 13:27:32] <sgp_> moneromooo added the ability to "freeze" outputs. These don't show up in the wallet balance and will not be spent until "thawed" https://github.com/monero-project/monero/pull/5333
    [2019-04-01 13:27:42] <sarang> Oh yes, this seems a good idea
    [2019-04-01 13:27:55] <sarang> In case you fear an output may be "poisoned" via some kind of controlled spend
    [2019-04-01 13:28:10] <sgp_> precisely
    [2019-04-01 13:28:15] <suraeNoether> that's super neat
    [2019-04-01 13:28:40] <sarang> Not really a general solution, of course, but one definite way to avoid something you suspect is adversarial
    [2019-04-01 13:29:07] <sarang> OK, on to 3. QUESTIONS
    [2019-04-01 13:29:18] <sarang> Any general questions, or those relating to research discussed here?
    [2019-04-01 13:29:34] <suraeNoether> why are they called elliptic curves
    [2019-04-01 13:29:51] <sarang> -___-
    [2019-04-01 13:29:59] <suraeNoether> think i'm going to start a novelty twitter account called surae_googling
    [2019-04-01 13:30:12] <sarang> is the supermarket open today
    [2019-04-01 13:30:16] <Xeagu> I'll follow
    [2019-04-01 13:30:23] <sarang> heh
    [2019-04-01 13:30:35] <Xeagu> It is April 1st
    [2019-04-01 13:30:42] <sarang> Well, we can wrap up soon... on to 4. ACTION ITEMS
    [2019-04-01 13:30:55] <nioc> surae_ducking
    [2019-04-01 13:31:03] <sarang> I will continue working on CLSAG stuff, to move the testing along
    [2019-04-01 13:31:21] <sarang> and continue Lelantus investigation as available
    [2019-04-01 13:31:26] <sarang> (but this is lower priority of course)
    [2019-04-01 13:31:30] <sarang> suraeNoether: ?
    [2019-04-01 13:31:40] <suraeNoether> i'm finishing up my tech note on teh security and benefits and applications of clsag and pass them onto sarang for review. i want them posted by the end of hte week since the scheme is so straightforward. i'm also going to seek inspiration: https://twitter.com/RikerGoogling/status/1112758935973322752
    [2019-04-01 13:32:07] <sarang> sigh
    [2019-04-01 13:32:13] <sarang> We are all April Fools on this day
    [2019-04-01 13:32:22] <sarang> any other action items of note?
    [2019-04-01 13:32:31] <suraeNoether> btw guys, i'm not kidding about CLSAG being useful for colored monero, even though its' april 1
    [2019-04-01 13:33:00] <suraeNoether> my april 1 jokes are more like "haha i put almond milk in my wife's coffee instead of cow's milk, take that lady"
    [2019-04-01 13:33:01] <dEBRUYNE> When are the conference tickets supposed to go up for sale btw?
    [2019-04-01 13:33:19] <suraeNoether> dEBRUYNE: mere dozens of hours
    [2019-04-01 13:33:39] <suraeNoether> the early bird tickets anyway
    [2019-04-01 13:33:58] ⇐ cardboardoranges quit (~cardboard@65.112.10.91): Ping timeout: 258 seconds
    [2019-04-01 13:34:04] <dEBRUYNE> Cool
    [2019-04-01 13:34:06] <Xeagu> Allergic to almonds
    [2019-04-01 13:34:06] <suraeNoether> i'll post in here and -community and on reddit and twitter when they are available, and i'll ask for some amplification
    [2019-04-01 13:34:14] <dEBRUYNE> Awesome
    [2019-04-01 13:34:41] <suraeNoether> also i have the last pile of abstracts to go through and the schedule to finish organizing.
    [2019-04-01 13:35:07] <sarang> All right, well thanks to everyone for attending this quick research meeting. Discussion on topics can of course continue, but let's go ahead and formally adjourn
    [2019-04-01 13:35:30] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-04-01T14:16:17+00:00
- Closed at: 2019-04-01T17:38:41+00:00
