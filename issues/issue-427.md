---
title: 'Research meeting: 15 January 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/427
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-13T18:00:55+00:00'
updated_at: '2020-01-16T14:57:12+00:00'
type: issue
status: closed
closed_at: '2020-01-16T14:57:11+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 15 January 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-01-16T14:57:11+00:00
    [2020-01-15 13:01:13] <sarang> GREETINGS
    [2020-01-15 13:01:28] <sgp_> hello
    [2020-01-15 13:01:30] <almutasim> Hi.
    [2020-01-15 13:01:34] <ArticMine> Hi
    [2020-01-15 13:01:50] <koe> hi
    [2020-01-15 13:01:53] <vtnerd> hi
    [2020-01-15 13:02:06] <suraeNoether> Wow what a turnout!
    [2020-01-15 13:02:48] <atoc> Hello
    [2020-01-15 13:02:56] <rehrar> hi
    [2020-01-15 13:03:22] <sarang> Let's continue with ROUNDTABLE discussion
    [2020-01-15 13:03:30] <sarang> suraeNoether: anything of research interest to share?
    [2020-01-15 13:04:16] <xmrmatterbridge> <ajs> ajs archived the channel.
    [2020-01-15 13:05:07] <sgp_> um.... is the channel now gone on Mattermost?
    [2020-01-15 13:05:15] <suraeNoether> not yet... Right now I'm just copy editing CL sag, working on matching code, and looking into possible speedups for triptych
    [2020-01-15 13:05:40] <ajs[m]> ?
    [2020-01-15 13:05:47] <suraeNoether> I expect about an hour before clsag is done
    [2020-01-15 13:05:49] <ajs[m]> I thought it was just for me
    [2020-01-15 13:05:50] <atoc> I noticed it disappeared too.
    [2020-01-15 13:06:04] <sgp_> it's gone
    [2020-01-15 13:06:07] <rehrar> lol
    [2020-01-15 13:06:10] <rehrar> give me a sec
    [2020-01-15 13:06:10] <suraeNoether> Hmm. Who was running it?
    [2020-01-15 13:06:11] <sgp_> sorry for derailing, something to fix later
    [2020-01-15 13:06:15] <suraeNoether> Oh
    [2020-01-15 13:06:27] ⇐ maxwilliamson quit (~maxwillia@gateway/tor-sasl/maxwilliamson): Remote host closed the connection
    [2020-01-15 13:06:29] <suraeNoether> Moving along :) what about you, Sarang?
    [2020-01-15 13:06:32] <sarang> Sure
    [2020-01-15 13:06:37] <koe> for those who want to access logs later: https://monerologs.net
    [2020-01-15 13:06:48] → maxwilliamson joined (~maxwillia@gateway/tor-sasl/maxwilliamson)
    [2020-01-15 13:06:50] <ajs[m]> lol
    [2020-01-15 13:06:56] <sarang> The Triptych preprint has been updated with new efficiency data and some minor typo corrections (IACR 2020/018)
    [2020-01-15 13:07:06] — Isthmus checks in
    [2020-01-15 13:07:11] <sarang> It will appear on monero-site as MR 1197
    [2020-01-15 13:07:31] <sarang> The DLSAG paper is being revised for its publication in the FC 2020 proceedings
    [2020-01-15 13:07:42] <sarang> and we're working on updating the security model for later journal submission
    [2020-01-15 13:08:03] <sarang> I have a monero-site MR ready to go for the CLSAG updates (MR 1202) as soon as suraeNoether's review is complete
    [2020-01-15 13:08:06] ⇐ kico quit (~kico@gateway/tor-sasl/kico): Quit: bbl
    [2020-01-15 13:08:12] <sarang> (and I get it updated on IACR)
    [2020-01-15 13:08:46] <sarang> I did some major overhauls on the curve libraries that I use for ed25519 and ed448 testing (for prototyping only; don't use them in production)
    [2020-01-15 13:09:01] <sarang> That included porting them to a bunch of other research projects
    [2020-01-15 13:09:24] <sarang> I also did some updates on my Lelantus code to fix some Fiat-Shamir transcript issues
    [2020-01-15 13:09:31] <sarang> And that's about it
    [2020-01-15 13:11:50] <sarang> Does anyone else have research to share?
    [2020-01-15 13:12:04] <sarang> We can also have any questions as well
    [2020-01-15 13:12:27] <atoc> Currently I have been just familiarizing myself with Monero Research
    [2020-01-15 13:12:59] <atoc> I have read quite a bit of Zero to Monero, and I also looked at the bipartite matching project: https://github.com/b-g-goodell/mrl-skunkworks/tree/matching-buttercup/Matching
    [2020-01-15 13:13:58] <atoc> I did have some questions, but I can go through them later with surae perhaps?
    [2020-01-15 13:14:11] <suraeNoether> Sure, now is fine with me too
    [2020-01-15 13:14:20] <suraeNoether> It's on topic :P
    [2020-01-15 13:14:30] <sarang> Sure, go ahead
    [2020-01-15 13:15:25] <koe> speaking of ZtM, thanks to Articmine the dynamic fee section has been greatly elaborated; anyone curious about all the justifications and derivation and analysis can find it in the latest draft; all that remains before I can publish are multisigs, bulletproofs, and proofreading (each of which will take a long time admittedly)
    [2020-01-15 13:15:26] <koe> https://www.pdf-archive.com/2020/01/15/zerotomoneroebookmaster-v1-0-17/zerotomoneroebookmaster-v1-0-17.pdf
    [2020-01-15 13:15:47] <atoc> Ok cool, well can you briefly give a high level description of this project? From what I understand so far is that this project will be used for user analysis along with statistical models, but hearing an overview from in your words would be nice.
    [2020-01-15 13:16:12] <rehrar> it's good to see ZtM getting the update :)
    [2020-01-15 13:16:55] <suraeNoether> Gotcha okay so first think about the Monero blockchain using two columns. List all of the one-time output keys from coinbases and from other transactions on the left and list all ring signatures or if you like key images on the right-hand column
    [2020-01-15 13:17:48] <suraeNoether> You can then go and draw edges between one time keys and ring signatures indicating ring membership. So if I publish a ring signature with ring members a b and c, my ring signature on the right would have edges connecting it to the outputs a, b, and c on the left
    [2020-01-15 13:18:28] <suraeNoether> These are what I call red edges in my code, and I also indicate blue edges connecting ring signatures on the right with the new fresh transaction one time keys that are output from their respective transactions on the left
    [2020-01-15 13:18:30] <sarang> koe: I asked this before, but how detailed are you looking to get with bulletproofs?
    [2020-01-15 13:18:44] <sarang> I fear you may end up essentially rewriting their entire paper, with little benefit to the typical reader
    [2020-01-15 13:19:13] <suraeNoether> So the Monero blockchain can be visualized as this two-colored bipartite graph with one-time keys on the left, ring signatures on the right, red edges indicating ring membership, and blue edges indicating output relationships
    [2020-01-15 13:19:42] <Isthmus> Hey @koe I owe you an email. I have some protocol notes, but have just been super swamped.
    [2020-01-15 13:19:45] <atoc> Cool cool, I
    [2020-01-15 13:19:47] <Isthmus> I'll try to get the email out in the next few days
    [2020-01-15 13:19:49] <atoc> I'm with you*
    [2020-01-15 13:19:58] <scoobybejesus> i am sort of busy, but wanted to throw out a question (in other words, don't let this question interrupt the current line of talk).  a response anytime would be great, though
    [2020-01-15 13:20:04] <scoobybejesus> I was thinking about how people complain about outputs getting locked up for 10 blocks.  Consequently one must send to themself a multi-out txn to prevent that from happening.  What if we made the standard tx 2-in and 3-out (2 change)?  And maybe set them to send to different accounts, so they take on independent/divergent decedent txn histories.  Was curious if MRL had thoughts/impressions
    [2020-01-15 13:20:22] <Isthmus> I also got halfway through updating Big Bang paper, but then got distracted. Hoping to finish that this weekend or next.
    [2020-01-15 13:20:31] — Isthmus ends update
    [2020-01-15 13:20:52] <suraeNoether> The ground truth of the situation is that each ring signature has a ring member that is the true signer of the signature, so for every ring signature with a bunch of red edges leading to a bunch of one-time output keys, somebody who's trying to track transactions is trying to pick the true spender from these red edges
    [2020-01-15 13:21:24] <suraeNoether> And this is called the matching problem in the graph theory world, sometimes also called the assignment problem, sometimes called the assigned marriage problem lol
    [2020-01-15 13:21:27] — Isthmus is pondering scoobybejesus 's idea
    [2020-01-15 13:21:57] <suraeNoether> So somebody who is trying to track transactions on the Monero blockchain is really trying to find a maximum matching on the Monero blockchain, linking signatures to true spenders
    [2020-01-15 13:22:03] <sgp_> scoobybejesus: I'd rather find ways to reduce the lock time
    [2020-01-15 13:22:39] <koe> no worries Isthmus :); sarang that's a valid concern and Im really not sure since I don't actually understand bulletproofs yet; I think if the bulletproofs paper is clear enough it will be fine to point people in that direction; I dislike the idea of leaving things open ended, but maybe it's just a useless hangup ^.^
    [2020-01-15 13:22:40] <suraeNoether> The signatures themselves give nothing away about which edge is supposed to be the true spender, so without any additional information the attacker just has to guess, and so every possible maximum matching is equivalently good in this world
    [2020-01-15 13:22:44] <atoc> Ah okay, I see. It seemed as if you were trying to find out if there was a way to trace back transactions.
    [2020-01-15 13:22:57] <suraeNoether> I am kinda
    [2020-01-15 13:23:28] <suraeNoether> So my graph theory python code allows you to build a graph, and then find maximum matchings, and if you wait the edges, it'll find the heaviest weight matching so that somebody using extra metadata can do better than just guessing at random
    [2020-01-15 13:23:35] <suraeNoether> Weight*
    [2020-01-15 13:24:04] <almutasim> How do you assign weights?
    [2020-01-15 13:24:27] <suraeNoether> Right so that's outside of the scope of graph theory and in the scope of my simulations...
    [2020-01-15 13:24:51] <almutasim> Ah. Are they probabilities?
    [2020-01-15 13:24:55] <atoc> Is this where statistical models come into play/
    [2020-01-15 13:25:22] → rubdos joined (~rubdos@2a02:578:859d:700:8b44:5716:382d:a7da)
    [2020-01-15 13:25:41] <suraeNoether> Yep. The way that I'm trying to do this is I'm simulating an economy between Alice, Eve and exchange with KYC information, and Bob representing all background players in the Monero economy. I'm even telling Eve the information about the Markov chain from the beginning, which models eves perfect ability to learn your habits.
    [2020-01-15 13:25:51] <suraeNoether> So this Eve is able to wait the graph using some null hypothesis about user behavior
    [2020-01-15 13:26:08] <suraeNoether> once she does this, even though she doesn't know the ground truth reality of the blockchain, she can find a maximum likelihood estimate which corresponds to a maximum weight matching
    [2020-01-15 13:26:14] <sarang> s/wait/weight/ ?
    [2020-01-15 13:26:18] <suraeNoether> Weight* sorry I'm on voice to text
    [2020-01-15 13:26:51] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-oalmsdzbxmnajqir): 
    [2020-01-15 13:26:57] <suraeNoether> So the simulator simulates an economy, strips information out of the graph that Eve doesn't know, hands the blockchain to Eve, Eve weights the graph and compute some maximum likelihood estimate, and this maximum likelihood estimate is compared to the simulators ground truth
    [2020-01-15 13:27:13] → midipoet joined (uid316937@gateway/web/irccloud.com/x-firubyrjrocunuuv)
    [2020-01-15 13:27:17] <suraeNoether> When things are working I get preliminary data that suggests that Eve is really really bad at this game Even though she's given perfect information about Alice's habits
    [2020-01-15 13:27:35] <suraeNoether> But that's all preliminary because my code is only intermittently working and I am currently in the midst of refactoring it to be simpler.
    [2020-01-15 13:27:36] <almutasim> That's encouraging.
    [2020-01-15 13:28:46] <atoc> Quite interesting surae. I understood about half of it before, but given you're description I see the goal of the project now.
    [2020-01-15 13:33:24] * Socket closed
    [2020-01-15 13:34:26] → Joined channel #monero-research-lab
    [2020-01-15 13:34:26] * ChanServ set +o sarang
    [2020-01-15 13:34:26] <atoc> Ah I see, was MoneroLink done by the Monero community or third-party?
    [2020-01-15 13:34:29] * Channel mode is +cnt
    [2020-01-15 13:34:41] <derpy_bridge> [keybase] <surae>: The fact that it was written by people who had a financial interest in succeeding compared to Monero was viewed as very suspicious by a lot of folks.
    [2020-01-15 13:34:44] <koe> suraeNoether have you collected a list of tracability analysis papers? for example sarang mentioned a preprint earlier; or maybe Isthmus has that list
    [2020-01-15 13:34:54] <derpy_bridge> [keybase] <surae>: Andrew Miller from Zcash and a couple of other folks who were involved with Zcash were authors
    [2020-01-15 13:34:59] → selsta joined (sid124829@gateway/web/irccloud.com/x-yawwnyoshgcrjnaq)
    [2020-01-15 13:35:38] → naughtyfox joined (sid301918@gateway/web/irccloud.com/x-qdesgfgtqqivzeah)
    [2020-01-15 13:36:10] <derpy_bridge> [keybase] <surae>: Actually you know, Sarang may have a better list than I would... A paper came out last year describing a game not dissimilar from my graph theory game and they named it after sun tzu. But I can be more helpful in finding background papers. Basically any papers on the traceability of anonymous communication networks has some degree of applicability to the Monero blockchain
    [2020-01-15 13:36:29] → cohcho joined (~cohcho@gateway/tor-sasl/cohcho)
    [2020-01-15 13:36:50] <derpy_bridge> [keybase] <surae>: "perfect matching disclosure attacks" is a general paper that was critical in the construction of the matching stuff
    [2020-01-15 13:36:54] <atoc> I see I see. So I see a couple of todos listed (unity tests and another). What are some important priorities for this project? I feel I can contribute to this project as a start.
    [2020-01-15 13:38:34] <atoc> Just a little background about myself: I'm an academic researcher in theoretical computer science (neural algorithms).
    [2020-01-15 13:38:36] <derpy_bridge> [keybase] <surae>: Let's talk about that after the meeting
    [2020-01-15 13:38:40] <atoc> sure
    [2020-01-15 13:38:46] <MRL-discord> <Isthmus> Dang, I got bumped off IRC
    [2020-01-15 13:38:51] <MRL-discord> <Isthmus> Can't log back in
    [2020-01-15 13:38:56] <derpy_bridge> [keybase] <surae>: speaking of the meeting, isthmus tells me that he has lost access to IRC... And I also happened to lose access to IRC and I'm just using the keybase bridge
    [2020-01-15 13:38:57] <MRL-discord> <Isthmus> *IRCcloud
    [2020-01-15 13:39:16] <derpy_bridge> [keybase] <surae>: it looks to me like IRC cloud has gone down which means the vast majority of the people in this room are probably not here anymore
    [2020-01-15 13:39:18] <MRL-discord> <Isthmus> @atoc nice to meet you, excited to contribute
    [2020-01-15 13:39:25] <MRL-discord> <Isthmus> *to collaborate
    [2020-01-15 13:39:32] <MRL-discord> <Isthmus> Sorry, I'm in a meatspace meeting too
    [2020-01-15 13:39:51] <derpy_bridge> [keybase] <surae>: So we'll give it a few more minutes and if I receive cloud doesn't come back or if nobody else speaks up, I say we adjourn the meeting
    [2020-01-15 13:39:58] <derpy_bridge> [keybase] <surae>: If irccloud*
    [2020-01-15 13:40:14] <MRL-discord> <Isthmus> So I just realized that we aren't fully utilizing the archival network data. But I'll wait for our IRCcloud comrades to return
    [2020-01-15 13:40:20] <xmrmatterbridge> <sgp_> yes, irccloud seems to be down for everyone
    [2020-01-15 13:40:29] <derpy_bridge> [keybase] <surae>: I had a question for isthmus about the archival network and lock times
    [2020-01-15 13:40:35] <MRL-discord> <Isthmus> sup
    [2020-01-15 13:40:36] ⇐ needmonero90 quit (sid289137@gateway/web/irccloud.com/x-ezlihywbnkxvgjzr): Read error: Connection reset by peer
    [2020-01-15 13:40:42] ⇐ TheoStormCloud quit (sid344770@gateway/web/irccloud.com/x-zjjmvnfwxyhlcang): Ping timeout: 260 seconds
    [2020-01-15 13:40:54] ⇐ endogenic quit (sid145991@gateway/web/irccloud.com/x-nfnhgasksyuxcbgq): Read error: Connection reset by peer
    [2020-01-15 13:41:05] <derpy_bridge> [keybase] <surae>: I want to know the distribution of fork lengths observed so far, and I also want to know the distribution of forklengths experienced by a new node syncing
    [2020-01-15 13:42:23] ⇐ selsta quit (sid124829@gateway/web/irccloud.com/x-yawwnyoshgcrjnaq): Ping timeout: 245 seconds
    [2020-01-15 13:42:23] <atoc> isthmus nice to meet you as well.
    [2020-01-15 13:44:41] <atoc> hmm okay and sorry what do you mean fork lengths?
    [2020-01-15 13:45:33] <derpy_bridge> [keybase] <surae>: As in Nakamura consensus resolving a fork
    [2020-01-15 13:45:40] <derpy_bridge> [keybase] <surae>: Nakamoto
    [2020-01-15 13:45:51] <derpy_bridge> [keybase] <surae>: WTF that was autocorrect too not voice to text
    [2020-01-15 13:46:51] <almutasim> It should be correcting the other way.
    [2020-01-15 13:46:54] <atoc> I see, alright I will begin looking into this.
    [2020-01-15 13:46:59] <derpy_bridge> [keybase] <surae>: Isthmus actually specifically I want an estimate of the parameter r under the null hypothesis that fork lengths are negbinom(p, r)
    [2020-01-15 13:48:14] <derpy_bridge> [keybase] <surae>: I think lock time has to be proportional to r to protect most transactions from most rollbacks
    [2020-01-15 13:48:47] <derpy_bridge> [keybase] <surae>: Okay since irccloud is now fartcloud, I say this meeting is adjourned.
    [2020-01-15 13:49:07] <koe> good meeting! happy day to yall
    [2020-01-15 13:49:16] <derpy_bridge> [keybase] <surae>: Good seeing you around koe
    [2020-01-15 13:49:30] <xmrmatterbridge> <sgp_> thanks
    [2020-01-15 13:49:43] <almutasim> Thanks. Good meeting.


# Action History
- Created by: SarangNoether | 2020-01-13T18:00:55+00:00
- Closed at: 2020-01-16T14:57:11+00:00
