---
title: 'Research meeting: 8 April 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/327
author: SarangNoether
assignees: []
labels: []
created_at: '2019-04-06T20:55:34+00:00'
updated_at: '2019-04-08T18:17:19+00:00'
type: issue
status: closed
closed_at: '2019-04-08T18:17:18+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 8 April 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [CLSAG plumbing/timing](https://github.com/SarangNoether/monero/tree/clsag-plumbing), [Dandelion++](https://arxiv.org/abs/1805.11060) ([BIP](https://github.com/bitcoin/bips/blob/master/bip-0156.mediawiki), [Grin](https://github.com/mimblewimble/grin/pull/2628)), [output selection](https://github.com/monero-project/monero/pull/5389)
b. Surae
c. Others?

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-04-08T18:17:18+00:00
    [2019-04-08 12:57:24] <sarang> Agenda: https://github.com/monero-project/meta/issues/327
    [2019-04-08 12:57:26] <dotkc> suraeNoether: I'd enjoy a meeting if you pass through ATL on your upcoming clemson visit
    [2019-04-08 12:58:38] <sarang> Let's go ahead and begin since it's about time to start
    [2019-04-08 12:58:43] <sarang> 1. GREETINGS
    [2019-04-08 12:58:45] <sarang> hello all
    [2019-04-08 12:59:01] <sarang> Who's here today?
    [2019-04-08 12:59:38] <rehrar> hi
    [2019-04-08 12:59:50] <sgp_> hello
    [2019-04-08 13:00:19] <ArticMine> hi
    [2019-04-08 13:00:21] <suraeNoether> holaa
    [2019-04-08 13:00:24] <sarang> Welcome to dotkc, who is fairly new to our channels
    [2019-04-08 13:00:41] <sarang> Let's jump into 2. ROUNDTABLE
    [2019-04-08 13:00:44] <sarang> I have a few things to share
    [2019-04-08 13:01:10] <sarang> First, I have an example branch (link in agenda) of a C++ implementation of CLSAG ring signatures, along with basic timing tests for our current ringsize
    [2019-04-08 13:01:29] <suraeNoether> WHEEE!
    [2019-04-08 13:01:31] <sarang> On my test machine, an 11-member MLSAG (current scheme) takes 13.0 ms to verify
    [2019-04-08 13:01:33] <suraeNoether> clsag is so cool man
    [2019-04-08 13:01:50] <sarang> If we move to CLSAG, an 11-signature takes 10.6 ms to verify
    [2019-04-08 13:02:00] — midipoet waves
    [2019-04-08 13:02:05] <sarang> If we modify the hash coefficients (more later on that), it increases to 11.1 ms
    [2019-04-08 13:02:34] <sarang> This means that if we take these numbers as correct, CLSAG gives us smaller _and_ faster signatures
    [2019-04-08 13:02:54] <sarang> Note that the linked branch is for example purposes only
    [2019-04-08 13:03:12] <sarang> There are a few new underlying functions that would need review
    [2019-04-08 13:03:14] ⇐ cardboardoranges quit (~cardboard@65.112.8.10): Quit: cardboardoranges
    [2019-04-08 13:03:28] <suraeNoether> a 15% gain in verification time, after a year of blockchain growth, is equivalent to a really large gain in overall download+sync time, saving future nodes the time it takes to start mining monero... and that's true even if we boost ring sizes moderately to ring size 13-14, based on sarang's numbers: we will still have an overall gain in download+sync time after a year. i'm not sure if i recommend that yet,
    [2019-04-08 13:03:28] <suraeNoether> though.
    [2019-04-08 13:04:00] <suraeNoether> tiny changes in verification time mean huge swings in space capacity, if we count download+sync time as our metric.
    [2019-04-08 13:04:04] <sarang> Reminder that the space savings are 320 bytes per spent input (each spent input is a separate signature)
    [2019-04-08 13:04:16] <ArticMine> How does size compare?
    [2019-04-08 13:04:21] <sarang> ^^
    [2019-04-08 13:04:35] <suraeNoether> it will be delightful to see the graph of monero blockchain size over time one year from clsag implementation
    [2019-04-08 13:04:41] <suraeNoether> that'll be the good nooch
    [2019-04-08 13:05:21] <sarang> Any questions or comments on CLSAG as it currently stands?
    [2019-04-08 13:05:31] <sarang> There is currently no decision to use this, nor a timeline
    [2019-04-08 13:06:12] <sarang> There is also a Python example implementation: https://github.com/SarangNoether/skunkworks/blob/clsag/clsag/clsag.py
    [2019-04-08 13:06:25] <ArticMine> So a typical tx with two outputs has a ~620 byte savings
    [2019-04-08 13:06:29] <sarang> correct
    [2019-04-08 13:06:33] <sarang> Er, 2 inputs
    [2019-04-08 13:06:45] <sarang> These savings are per spent input (and therefore per signature)
    [2019-04-08 13:06:47] <suraeNoether> oh fwiw
    [2019-04-08 13:06:49] <suraeNoether> i have a quick comment
    [2019-04-08 13:07:39] <sarang> Go ahead suraeNoether !
    [2019-04-08 13:07:50] <suraeNoether> the difference between sarang's 11.1 ms version and 10.6 ms version is that the 11.1 ms version is provably unforgeable as long as LSAG is unforgeable. it's a drop-in version of musig key aggregation (andytoshi ^) for use in confidential transactions, and the proof is very easy
    [2019-04-08 13:07:59] <suraeNoether> for the 10.6 ms version, i'm still tinkering with the proof of unforgeability.
    [2019-04-08 13:08:08] <suraeNoether> but it's less trivial to prove
    [2019-04-08 13:08:17] <sarang> exactly
    [2019-04-08 13:08:29] <suraeNoether> and, fwiw, this is one of the first times in my life i've seen a literal engineering example of the gap between the theoretical and the application :P
    [2019-04-08 13:08:31] <hyc> very cool
    [2019-04-08 13:08:32] <sarang> Right now the timing code has a flag where you can choose which version you want to examine
    [2019-04-08 13:08:34] <suraeNoether> it's kind of neat
    [2019-04-08 13:09:00] <sarang> Anyway, please play around with CLSAG if you find it interesting
    [2019-04-08 13:09:01] <hyc> ^^ more techies need that lightbulb moment
    [2019-04-08 13:09:07] <sarang> Next up: Dandelion__
    [2019-04-08 13:09:10] <sarang> s/__/++
    [2019-04-08 13:09:14] <ArticMine> What is the impact of ring size?
    [2019-04-08 13:09:34] <sarang> ArticMine: it uses 1 additional scalar per ring member (as opposed to 2)
    [2019-04-08 13:09:37] <suraeNoether> ArticMine: we could increase ring size to 13-14 and see similar verificaiton times as our present ring sizes.
    [2019-04-08 13:09:41] <sarang> verification increases linearly
    [2019-04-08 13:09:43] <suraeNoether> afaik
    [2019-04-08 13:10:00] <sarang> Yes, once we hit ringsize 13-14, we hit the same verification time as an 11-MLSAG
    [2019-04-08 13:10:03] <sarang> (approximately)
    [2019-04-08 13:10:36] <sarang> If desired, I can make up a chart with sizes and times
    [2019-04-08 13:10:41] <ArticMine> Still the space saving is significant
    [2019-04-08 13:10:44] <sarang> yes
    [2019-04-08 13:10:53] <sarang> and it's faster
    [2019-04-08 13:11:00] <sgp_> sarang: a quick, rough estimate chart is good enough for me
    [2019-04-08 13:11:20] <sarang> FWIW, an n-CLSAG will always be faster than an n-MLSAG
    [2019-04-08 13:11:37] <sarang> The original question was comparing n-CLSAG to 11-MLSAG
    [2019-04-08 13:11:44] <sarang> and of course there's a crossover point
    [2019-04-08 13:11:58] <sarang> Anyhoo, we've talked informally about Dandelion++
    [2019-04-08 13:12:14] <sarang> I have links to a proposed BIP on this, as well as an updated PR for Grin about it
    [2019-04-08 13:12:37] <sarang> If we want to move forward with Dandelion++ as part of our txn routing, there are some design choices to make
    [2019-04-08 13:12:45] <suraeNoether> d++ is going to be a topic of conversation i believe by vtnerd at the konferenco (ping)
    [2019-04-08 13:13:05] <sarang> Yes, and the usual reminder that it is _not_ a replacement for network-level solutions like Tor/I2P
    [2019-04-08 13:13:36] <sarang> Grin changed their implementation such that a node does not fluff/stem on a per-txn basis, but on a per-epoch basis
    [2019-04-08 13:13:40] <sarang> this is what the original paper says
    [2019-04-08 13:13:48] <sarang> the BIP does not address this (and I believe is incorrect)
    [2019-04-08 13:14:16] <sarang> Grin's implementation is a little more complex than ours would need to be, since they perform txn aggregation
    [2019-04-08 13:14:21] <suraeNoether> sarang: can you provide a few helpful links for the record?
    [2019-04-08 13:14:30] <sarang> links to BIP/Grin in agenda
    [2019-04-08 13:14:34] <suraeNoether> i'm curious on the details of grin's implementation vs the bip
    [2019-04-08 13:14:36] <suraeNoether> ah great thanks
    [2019-04-08 13:14:42] <sarang> Original D++ paper: https://arxiv.org/abs/1805.11060
    [2019-04-08 13:15:08] <sarang> Any questions on D++?
    [2019-04-08 13:15:15] <sarang> I want to see it implemented in Monero
    [2019-04-08 13:15:26] <suraeNoether> i do too
    [2019-04-08 13:15:56] <suraeNoether> i believe the epochal approach taken by grin is the correct one, but maybe there's an argument out there for the difference
    [2019-04-08 13:16:08] <suraeNoether> i wonder if andytoshi or gmaxwell would chime in
    [2019-04-08 13:16:17] <sarang> The epoch approach is correct according to the paper
    [2019-04-08 13:17:04] <sarang> So at each epoch, the node flips a weighted coin to decide which "mode" it is in: fluff or stem
    [2019-04-08 13:17:16] <andytoshi> i don't know anything about dandelion, sorry :)
    [2019-04-08 13:17:23] <sarang> all txns are routed according to that (unless the node detects a black-hole attack)
    [2019-04-08 13:17:36] <sarang> andytoshi: I did reach out once in -wizards to ask about the BIP, but didn't hear anything :/
    [2019-04-08 13:17:50] <sarang> perhaps others have discussed it elsewhere, who knows
    [2019-04-08 13:18:16] <sarang> The last thing I have to share is that moneromooo prepared PR 5389 (link in agenda) regarding output selection
    [2019-04-08 13:18:46] <sarang> it uses the "output lineup" method we've discussed here at length
    [2019-04-08 13:19:26] <sarang> Review on the method/PR would be most welcome
    [2019-04-08 13:19:48] <sarang> That's all for me right now... suraeNoether, your report?
    [2019-04-08 13:20:46] <suraeNoether> great, so I have a few updates
    [2019-04-08 13:21:08] <suraeNoether> first things first: monero konferenco registration is now open on https://monerokon.com
    [2019-04-08 13:21:38] <suraeNoether> second things second: as I mentioned right before the meeting, next week I'm headed out to Clemson University to give a talk and meet with some colleagues
    [2019-04-08 13:22:15] <suraeNoether> I'm meeting with Gao, the lead researcher there in their blockchain group
    [2019-04-08 13:22:45] <suraeNoether> in addition to that, my top priority right now is my most-old project rihgt now, which is MRL-11 and my matching simulations + churn analysis
    [2019-04-08 13:22:58] <sarang> (and let's discuss churn in more detail after your report too)
    [2019-04-08 13:23:10] <suraeNoether> given the recent conversation with dotkc and sgp_ about automated churn, this priority is tippy top
    [2019-04-08 13:23:20] <sgp_> I cannot stress enough how important MRL-11 is
    [2019-04-08 13:23:34] <sarang> Yeah, before we discuss that in depth, do you have anything not related to it to share suraeNoether ?
    [2019-04-08 13:23:53] <dotkc> I have a colleague who might be a great fit to jump in and help MRL-11 efforts
    [2019-04-08 13:23:54] <suraeNoether> not yet: after the meeting i want to have a public discussion about the various behaviors we want to test
    [2019-04-08 13:24:06] <sarang> Righto
    [2019-04-08 13:24:12] <sarang> So yes, let's talk churn
    [2019-04-08 13:24:12] <suraeNoether> i have the infrastructure of matching done and the infrastructure for monte carlo simulations of a blockchain graph done
    [2019-04-08 13:24:31] <sarang> dotkc: you had posted in r/Monero a few things regarding a tool your group is working on; can you introduce yourself to the room?
    [2019-04-08 13:25:07] <sarang> and sgp_ and dotkc have discussed it at length on r/Monero and earlier in this room
    [2019-04-08 13:25:43] <dotkc> i'm nobody, it's a hobby project that materialized into code and my colleagues and I talk a lot about privacy so here we are to help
    [2019-04-08 13:25:49] <sarang> (since dotkc is new here, a reminder that these meeting logs are made public afterward, FYI)
    [2019-04-08 13:26:20] <dotkc> I'm aware and thank you for pointing it out
    [2019-04-08 13:26:25] <sarang> np
    [2019-04-08 13:26:38] <sarang> Can you describe your tool briefly?
    [2019-04-08 13:27:12] <dotkc> we started by gathering every shred of churn-related discussion from around the community
    [2019-04-08 13:27:52] <dotkc> plus our basic familiarity with several chain analysis and network monitoring techniques
    [2019-04-08 13:28:27] <dotkc> the intention is to join you all in researching privacy wrt churn and help users employ "less bad" practices
    [2019-04-08 13:28:48] <dotkc> we don't need to reach "best practices" to improve the network, imo
    [2019-04-08 13:29:16] → cardboardoranges joined (~cardboard@65.112.8.77)
    [2019-04-08 13:29:21] <sarang> The intention of the software tool, from my understanding in reading earlier logs, is to automate certain churn practices according to guidelines that are being developed
    [2019-04-08 13:29:33] <sarang> and that there is a donation component of some kind to support projects
    [2019-04-08 13:29:43] <dotkc> and I'm definitely not going to be manually throwing tons of churn-like transactions onto the network for analysis so our first step was making a tool to automate that
    [2019-04-08 13:29:43] <sarang> this particular point seemed more controversial
    [2019-04-08 13:30:49] <dotkc> donations were certainly controversial. I think many of you will find the concept easier to swallow if you look at the code and see how we have padded donations with sweep_single
    [2019-04-08 13:31:06] <dotkc> then, instead of thinking donation, think possibly-safer-spend
    [2019-04-08 13:31:07] <sarang> What particular churn-related heuristics do you wish to avoid with this automation?
    [2019-04-08 13:31:35] <dotkc> maybe this technique would be better employed to enable a user to reveal less in a transaction to a potential adversary
    [2019-04-08 13:31:46] <sarang> One reason we don't have any formal churn recommendations yet is because of a lack of complete understanding of relevant heuristics that might be employed
    [2019-04-08 13:32:29] <sarang> Some would be timing-based, others purely graph-based, etc.
    [2019-04-08 13:32:38] <dotkc> a few we discussed with @isthmus last week are avoiding sweep_all combining unrelated outputs without any clear benefit to doing so
    [2019-04-08 13:32:59] <sarang> Can you discuss the specific heuristics you want to mitigate or avoid
    [2019-04-08 13:33:00] <sarang> ?
    [2019-04-08 13:33:14] <dotkc> 1. sweep_all combining unrelated
    [2019-04-08 13:33:16] <sarang> (some of this is in GitHub/reddit, but I'd like to hear a summary here too)
    [2019-04-08 13:33:20] <dEBRUYNE> Personal opinion, your tool won't thrive if the donation stuff (where a third output is created) isn't removed
    [2019-04-08 13:33:49] <dotkc> 2. a bunch of sweep_single in a short period of time, from the same IP, relayed to same neighbors, blah blah blah
    [2019-04-08 13:34:32] <dotkc> thanks dEBRUYNE, i moved it to an optional flag after discussions here yesterday
    [2019-04-08 13:34:50] <dotkc> let's take a step back. I don't propose dots living on as a stand alone tool.
    [2019-04-08 13:35:00] <dEBRUYNE> Why can't the donation be part of the churn btw?
    [2019-04-08 13:35:07] <dotkc> it's a tool to research churn that is likely to die in 2 ways
    [2019-04-08 13:35:09] <sarang> And it's certainly a good idea to limit such network tests to testnet until better studied
    [2019-04-08 13:35:32] <dEBRUYNE> dotkc: Normally a sweep_all with 1 input would create 2 outputs, one that goes back to the sender, and one that is sent to a random address
    [2019-04-08 13:35:39] <dotkc> 1. churn found to promote privacy: we'll move these techniques into main wallet
    [2019-04-08 13:35:40] <dEBRUYNE> What if you'd replace that random address with the donation address?
    [2019-04-08 13:35:48] <dEBRUYNE> Then you'd avoid having 3 output transactions
    [2019-04-08 13:35:50] <sgp_> dEBRUYNE: that's what they were doing iirc
    [2019-04-08 13:36:16] <dotkc> 2. churn found to harm privacy, dots helps destroy the delusion of churn==privacy that surrounds this community (particularly less intermediate users)
    [2019-04-08 13:36:34] <dEBRUYNE> I guess that may still provide some leakage, but would be better
    [2019-04-08 13:36:59] <dEBRUYNE> churn==privacy that surrounds this community <= I disagree. I think most of the community is aware that abusing certain features such as churn can hurt one's privacy
    [2019-04-08 13:37:12] <sarang> A concern relating to donation was also that donation to a view-enabled address provides public information relating to churn transactions
    [2019-04-08 13:37:12] <dotkc> yeah, we don't do 3 output transactions, i'm not sure who tossed that into the discussion. seems like they were talking about some old wallet
    [2019-04-08 13:37:29] → spaced0ut joined (~spaced0ut@unaffiliated/spaced0ut)
    [2019-04-08 13:37:39] <dEBRUYNE> sarang: That would be a concern yeah
    [2019-04-08 13:37:50] <sgp_> It was an example of some observable donation behavior someone else attempted that had similar privacy consequences
    [2019-04-08 13:38:53] <dotkc> our "donate" is like this 1. sweep_single 2. spend (donate) 3. sweep the change
    [2019-04-08 13:39:23] <dotkc> which, IF, and that's a big if, churn has benefits then this technique would be the safest way to spend XMR
    [2019-04-08 13:39:35] <dotkc> since we do a pre-spend churn, then spend, then churn the change
    [2019-04-08 13:39:57] <sarang> I question the kinds of fingerprints this could leave in the transaction graph
    [2019-04-08 13:40:02] <sarang> and need to think about it more
    [2019-04-08 13:40:18] <sgp_> dotkc: for the reasons I mentioned yesterday, including donated outputs in any step of the process is incrementally worse for privacy. It would be better to churn those 3 times without donation. I think the pressure to include this donation feature is getting us started on the wrong foot
    [2019-04-08 13:40:19] <dotkc> totally agree
    [2019-04-08 13:40:36] <suraeNoether> i'm in complete agreement with sgp_
    [2019-04-08 13:40:44] <xmrmatterbridge> <oneiric> random time delays b/w pre-spend -> spend -> change-churn ?
    [2019-04-08 13:40:45] <sarang> Good point; we can certainly talk about general churn strategies independently of donation
    [2019-04-08 13:41:09] <dotkc> please remember that it's OPTIONAL and in a very clearly defined test & research tool that is recommended for testnet
    [2019-04-08 13:41:15] <suraeNoether> churn is going to be difficult enough to nail down security details for without trying to model donations built into the process
    [2019-04-08 13:41:19] <suraeNoether> dotkc: please understand
    [2019-04-08 13:41:26] <sarang> Random time delays are certainly important for mitigating timing heuristics
    [2019-04-08 13:41:39] <suraeNoether> we are recommending against it due to the privacy properties of monero that make everyone's privacy sensitive to everyone else's choices.
    [2019-04-08 13:41:44] <sarang> Graph-specific heuristics would depend also on transaction rates (and appearance of outputs in other decoy rings, etc.)
    [2019-04-08 13:42:13] <suraeNoether> if some users optionally want to donate, great, they can construct a transaction on their own to make a donation and do it normally; you are talking about inserting a step into a non-security process designed for security
    [2019-04-08 13:42:32] <suraeNoether> this is like trying to build auto-donations into monero's key exchanges for some reason
    [2019-04-08 13:42:36] <sarang> Right, let's discuss general churn without the donation idea
    [2019-04-08 13:42:51] <suraeNoether> or like riding a tractor on hallucinogens, or dividing by zero. you can do it, you can do a lot of things, doesn't mean you should.
    [2019-04-08 13:42:58] <suraeNoether> so, speaking of churn and modeling it
    [2019-04-08 13:42:59] <midipoet> i am so lost with the talk of 'donations'
    [2019-04-08 13:43:13] <sarang> Right, let's forget about the idea of embedding donations within churn for now
    [2019-04-08 13:43:22] <suraeNoether> i'm simulating an economy where every output is born in a coinbase transaction or a regular transaction. Coinbase transactions have a fixed probability p of being sent to some "marked" party.
    [2019-04-08 13:43:27] <sgp_> I think that's a good idea
    [2019-04-08 13:43:46] <suraeNoether> all other transactions either take all marked inputs or all not marked inputs
    [2019-04-08 13:43:49] <dotkc> most of you seem hung up on the "donate" part, which is why i ask you to consider the same algorithm employed as a "spend" instead
    [2019-04-08 13:44:10] <suraeNoether> a transaction with non-marked inputs has a fixed probability of q of being sent to the same marked party
    [2019-04-08 13:44:12] <dotkc> like if you want to pay someone and you know their wallet will eventually become compromised
    [2019-04-08 13:44:25] <dotkc> it's the same problem as if you send to a donation address with open view key
    [2019-04-08 13:44:44] <suraeNoether> why would you send money to someone who you suspect will lose their wallet password?
    [2019-04-08 13:44:54] <suraeNoether> or give it to a malicious party?
    [2019-04-08 13:44:56] <sgp_> dotkc: yes, but you are suggesting a donation as a PART of the churn PROCESS, not as a payment after you already churn your funds
    [2019-04-08 13:45:24] <xmrmatterbridge> <oneiric> people should be cautious of who they donate to, research required
    [2019-04-08 13:45:25] <suraeNoether> okay check it, i want to have some discussion about formal statistical modeling, and i want to stop talking about donations
    [2019-04-08 13:45:35] <sarang> yes please
    [2019-04-08 13:45:38] <suraeNoether> dotkc: let's chat more about this after the research meeting
    [2019-04-08 13:45:43] <suraeNoether> for now let's talk statistics
    [2019-04-08 13:45:49] <sgp_> I really think we should put discussion about donations aside, since it seems like we are going to keep talking in circles. We can come back to it outside of meeting time
    [2019-04-08 13:45:57] <sarang> ^
    [2019-04-08 13:46:04] <suraeNoether> i'm simulating a ledger where every output is born in a coinbase transaction or a regular transaction. Coinbase transactions have a fixed probability p of being sent to some "marked" party.
    [2019-04-08 13:46:04] <xmrmatterbridge> <oneiric> routing out all the fakes in crypto would be a great research tool
    [2019-04-08 13:46:17] <dotkc> in either case, we want to be able to spend to someone without our privacy depending on them keeping their wallet private
    [2019-04-08 13:46:18] <suraeNoether> all other transactions either take all marked inputs or all not marked inputs
    [2019-04-08 13:46:31] <suraeNoether> a transaction with non-marked inputs has a fixed probability of q of being sent to the same marked party
    [2019-04-08 13:47:01] <suraeNoether> now when an output is created, a lifespan for that output is randomly selected
    [2019-04-08 13:47:13] <suraeNoether> if the output is not marked, the lifespan is drawn from the wallet spend-time distribuiton
    [2019-04-08 13:48:05] <suraeNoether> when a block rolls around, all the outputs flagged as "to be spent' are bundled into transactions using the empirical distribution fo number of inputs and outputs provided by n3ptune, isthmus at #noncesense-research-lab
    [2019-04-08 13:48:24] <suraeNoether> and the process repeats itself
    [2019-04-08 13:48:41] <suraeNoether> the parameters that vary from simulation to simulation is "what does the marked party do with their outputs?"
    [2019-04-08 13:49:07] <suraeNoether> in the churn case with a fixed wait-time between churns, the answer is "send to yourself N times, waiting h blocks between sends each time"
    [2019-04-08 13:50:03] <sarang> After this process, how is the resulting graph evaluated?
    [2019-04-08 13:50:05] <suraeNoether> in the churn case where the churner waits the wallet spend-time distribution (which is statistically identical to the background economy in this simulation), and churns a very large number of times N, it should be clear that an adversary will have zero advantage in identifying the churner
    [2019-04-08 13:50:23] <midipoet> churn is a verb
    [2019-04-08 13:50:49] <suraeNoether> "churn case" is a noun. :D
    [2019-04-08 13:51:08] <suraeNoether> once a simulation is generated, the adversary runs the matching algorithm and we have another set of parameters to test: which models the adversary uses to try to find the true spend pattern
    [2019-04-08 13:51:18] <suraeNoether> So there are two choices i have to make about how this goes: first, i select the distribution the marked party is spending  from. second, i select the model the adversary is going to use to try to match transactions. Then the confusion table I get out of it answers the question "using this adversary's model, X, when the marked party uses model Y, how good is the matching algorithm?"
    [2019-04-08 13:51:34] <suraeNoether> and for each of these choices, i can generate a confusion table
    [2019-04-08 13:51:46] <sarang> Right, and I think what needs to be nailed down is what the adversary is using for its models
    [2019-04-08 13:51:52] <suraeNoether> precisely
    [2019-04-08 13:51:57] <suraeNoether> which is why i want sgp_'s input, for one thing
    [2019-04-08 13:52:10] <sarang> Some are timing-based, which can be avoided by proper delay times
    [2019-04-08 13:52:12] <suraeNoether> but the problem is the adversary can use any heuristic they like to construct a model.
    [2019-04-08 13:52:50] <sarang> Others are purely graph-based, and depend heavily on outputs' use in decoys and the links between true/fake-change outputs in the graph
    [2019-04-08 13:53:54] <xmrmatterbridge> <oneiric> is this spend problem, at least partially, addressed by Dandelion++?
    [2019-04-08 13:53:59] <suraeNoether> BUT! this idea that if the churner is using the background distribution is one side of the coin. I claim this in addition: as the model Y diverges from the wallet spend-time distribution, the quality of the results will become more robust against variations in the choice of X, i.e.\ as long as you aren't too far off from the spend-time distribution, you are mostly indistinguishable, but if your behavior is
    [2019-04-08 13:54:00] <suraeNoether> very far off, you are an easy target.
    [2019-04-08 13:54:16] <sarang> D++ only affects how the relay process works
    [2019-04-08 13:54:26] <suraeNoether> oneiric nah, this has everything to do with the ledger and totally ignores the minnig network
    [2019-04-08 13:54:31] <sarang> it does introduce slight delays, sure
    [2019-04-08 13:54:37] <sarang> but these are very minor
    [2019-04-08 13:54:39] <xmrmatterbridge> <oneiric> re: obfuscating true spend time + origin
    [2019-04-08 13:54:47] <suraeNoether> oneiric this is essentially ledger forensics in the environment of ring signatures. :P
    [2019-04-08 13:54:54] <sarang> D++ helps against network-wide observation, not targeted observation
    [2019-04-08 13:55:17] <midipoet> am i understanding this simulation correctly, in that outputs are in perpetual motion (churned)?
    [2019-04-08 13:55:54] <xmrmatterbridge> <oneiric> ah, think i understand, thanks. has to be dealt with at sig level
    [2019-04-08 13:55:58] <dotkc> i propose naming such behavior maintenance churn
    [2019-04-08 13:56:36] <midipoet> we'll end up with butter
    [2019-04-08 13:56:54] <suraeNoether> midipoet: in my model, yeah, that's how i'm modeling the economy to generate a fake blockchain
    [2019-04-08 13:56:58] <dotkc> and i do agree with @suraeNoether that under his analysis, the appropriate timing makes such moves difficult to unmask
    [2019-04-08 13:57:08] <suraeNoether> after all, the goal of selecting a wallet distribution is that all otuptus will have ages drawn from it (not possible, but the goal)
    [2019-04-08 13:58:03] <suraeNoether> either way, the way i have this experiment set up, it is *necessarily* true that the case in which the churner matches the wallet distribution for N churns in a row will enjoy indistinguishability and the probability of any one edge being traced is R^-N, so we can think of this as an idealized model anyway
    [2019-04-08 13:58:40] <dotkc> this does still neglect many real-world considerations
    [2019-04-08 14:00:01] <suraeNoether> Using a birthday attack argument, a churn with length > 23 is "sufficient." but that's huge, and I suspect we will have, in practice much lower bounds.
    [2019-04-08 14:00:13] <xmrmatterbridge> <oneiric> is it safe to neglect for now, and gradually ramp up to more real-world-like conditions?
    [2019-04-08 14:00:25] <suraeNoether> dotkc: we can model various heuristics using my above approach under the "model X" component of my little rant
    [2019-04-08 14:00:41] <sarang> To what extent have we established a set of candidate heuristics?
    [2019-04-08 14:00:49] <suraeNoether> so the best help i can get for this is ^
    [2019-04-08 14:00:50] <suraeNoether> bingo
    [2019-04-08 14:00:55] <suraeNoether> before i can finish typing, sarang for the win
    [2019-04-08 14:00:55] <sarang> A framework is great, but extremely limited without something to test
    [2019-04-08 14:01:03] <sgp_> they can then be tested using the "made-up" blockchain to find the ground truth
    [2019-04-08 14:01:28] <sarang> I propose that dotkc and suraeNoether work more closely on identifying such heuristics to examine, whether temporal or purely graph-based or whatever
    [2019-04-08 14:01:41] <sarang> Having totally separate research paths for this is likely a waste of resources
    [2019-04-08 14:01:52] <dotkc> agreed and willing
    [2019-04-08 14:02:07] <sarang> and I do agree with sgp_ (and others) that getting this nailed down should be considered a priority
    [2019-04-08 14:02:16] <suraeNoether> right now i'm testing 1) periodic non-random spends, like a magazine subscription, 2) a single exponential wait time, like an impatient churner, but which has some of the statistical characteristics of our wallet spend-time distribution 3) gamma distribution, but tweaking expected wait time up and down smoothly to see the sensitivity of the confusion table to the difference between expected wait times
    [2019-04-08 14:03:14] <sarang> I appreciate your interest and willingness to bring this up dotkc 
    [2019-04-08 14:03:18] <xmrmatterbridge> <oneiric> maybe 4) uniform-random over some given range?
    [2019-04-08 14:03:28] <suraeNoether> 3) also corresponds to an impatient (or paranoid!) churner, but in a way that seems more apples-to-apples
    [2019-04-08 14:03:32] <dotkc> might i propose a few small wins the community might enjoy while the more comprehensive research continues?
    [2019-04-08 14:03:37] <suraeNoether> oneiric cool, i'll throw 4) uniform on there
    [2019-04-08 14:03:37] <sgp_> oneiric yes that's a nice simple one to test
    [2019-04-08 14:03:41] <sarang> What do you mean dotkc ?
    [2019-04-08 14:03:49] <xmrmatterbridge> <oneiric> :)
    [2019-04-08 14:03:53] <sgp_> suraeNoether: I'll PM you at some point with a list
    [2019-04-08 14:04:04] <suraeNoether> ^ bingo bango
    [2019-04-08 14:04:04] <moneromooo> Not sure if it helps, but I have an old patch that split txes to have one input at a time, and sent them at poisson delayed intervals.
    [2019-04-08 14:04:29] <dotkc> top of most search engines is a credible-looking post recommending sweep_all. that most certainly links outputs
    [2019-04-08 14:05:08] <sarang> BTW dotkc are you a developer on the dots code?
    [2019-04-08 14:05:47] <dotkc> there is plenty of advice around the community to churn for privacy and thousands of people view that sweep_all advice (if the page's counter is to be trusted)
    [2019-04-08 14:05:47] <dotkc> the developer, yes
    [2019-04-08 14:06:21] <sarang> Well, I certainly am of the opinion that there is no thorough, well-tested churn advice at this point
    [2019-04-08 14:06:28] <suraeNoether> ^
    [2019-04-08 14:06:35] <suraeNoether> it's a rock and hard place
    [2019-04-08 14:06:39] <dotkc> i agree with that
    [2019-04-08 14:06:51] <dotkc> but could we agree on anythign that's definitely bad?
    [2019-04-08 14:06:52] <sarang> It's fighting against a somewhat unknown set of heuristics (somewhat)
    [2019-04-08 14:07:05] <sarang> That's an interesting way to look at it dotkc 
    [2019-04-08 14:07:15] <dotkc> removing even one "most certainly bad" case is progress that would support user privacy
    [2019-04-08 14:07:20] <sarang> agreed
    [2019-04-08 14:07:58] <suraeNoether> i think the best practice is to spend at the "ground truth" background economy rate of spending, but that's literally impossible to determine. the next best solution is massive anonymity sets so timing analysis on the inputs fails. as the zcash example demonstrates, that doesn't do much for the output end of things.
    [2019-04-08 14:08:09] <sarang> Well, the idea of sweep_all vs single, for example
    [2019-04-08 14:08:11] <suraeNoether> but i'm testing that hypothesis
    [2019-04-08 14:08:14] <dotkc> i was deliberate in aiming at "less bad" with my short term goals for dots
    [2019-04-08 14:08:24] <sarang> as mentioned, linking outputs is a profoundly bad thing (in general, too)
    [2019-04-08 14:08:39] <sarang> and very tough until/unless we enable coinjoin
    [2019-04-08 14:08:40] <suraeNoether> dotkc: the worst thing that could be implemented is periodic behavior
    [2019-04-08 14:08:47] <suraeNoether> dotkc deterministically periodic i mean
    [2019-04-08 14:08:59] <sarang> suraeNoether: worst in terms of timing, perhaps
    [2019-04-08 14:09:09] <sarang> not necessarily in terms of other metadata (in/out counts, for example)
    [2019-04-08 14:09:13] <suraeNoether> yeah, and the vast majority of my work is based on timing alone.
    [2019-04-08 14:09:23] <suraeNoether> but periodic behavior stands out in a power spectrum like a novice at a nudist colony
    [2019-04-08 14:09:36] <sarang> Graph structure certainly interweaves with timing, but there's plenty beyond that too
    [2019-04-08 14:09:43] <dotkc> i agree with you both that sweep_all linkages and trivial temporal linkages seem very bad
    [2019-04-08 14:10:41] <sarang> I consider output linking to be extremely hard to avoid, since it's an inherent part of multi-input txns
    [2019-04-08 14:10:47] <sgp_> it depends on the circumstances, but yes sweep_all is bad if you don't want these outputs associated
    [2019-04-08 14:11:32] <moneromooo> If you don't want them associated, use two accounts ?
    [2019-04-08 14:11:48] <sgp_> moneromooo: yeah, always keep your outputs separate if you can :)
    [2019-04-08 14:11:55] <sarang> dotkc had included some multi-account ideas in GitHub as well, IIRC
    [2019-04-08 14:11:56] <dotkc> this is progress, we've nearly agreed on at least one "bad" behavior!
    [2019-04-08 14:12:11] ⇐ crCr62U0 quit (~crCr62U0@gateway/tor-sasl/crcr62u0): Ping timeout: 256 seconds
    [2019-04-08 14:12:32] <sarang> In the interest of time, let's briefly wrap up and then continue discussion afterward
    [2019-04-08 14:12:40] <sarang> Let's jump to 4. ACTION ITEMS
    [2019-04-08 14:12:44] <dotkc> @sarang: you are correct
    [2019-04-08 14:12:52] <sarang> one sec dotkc 
    [2019-04-08 14:12:55] <suraeNoether> dotkc: periodic behavior or any behavior in timing that is fundamentally unlike the "background rate" of spending will stick out statistically. repetitive behavior is super super linkable. i can tell you that with 100% confidence.
    [2019-04-08 14:13:37] <sarang> Besides contributing to the churn discussion to assist suraeNoether et al. with frameworks, I am finalizing CLSAG material as well as an unfortunate snag in DLSAG security that we're trying to address
    [2019-04-08 14:13:47] <sarang> suraeNoether: your action items?
    [2019-04-08 14:13:57] <suraeNoether>  my action items: simulations for MRL-11. sgp_ was going to send me some links to possible behaviors to investigate. continuing commentary and thought on dlsag and the clsag security proof. uhm...
    [2019-04-08 14:14:21] <suraeNoether> i'll probably do a little bit of recreational coding like spectre later this week after i've put some more hours into matching
    [2019-04-08 14:14:21] <sarang> great
    [2019-04-08 14:14:47] <sarang> Seems all are in agreement that matching/churn should be a priority that's been put to the backburner too long
    [2019-04-08 14:15:05] <sarang> Thanks to everyone for attending. We're now adjourned; logs will be posted to the github issue shortly
    [2019-04-08 14:15:11] <sarang> Let the discussion continue!
    [2019-04-08 14:15:19] <sgp_> Quick Moneroversary reminder, add comments about how you would like to participate: https://github.com/monero-project/meta/issues/324
    [2019-04-08 14:15:29] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-04-06T20:55:34+00:00
- Closed at: 2019-04-08T18:17:18+00:00
