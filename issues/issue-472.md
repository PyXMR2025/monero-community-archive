---
title: 'Research meeting: 10 June 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/472
author: SarangNoether
assignees: []
labels: []
created_at: '2020-06-05T15:32:08+00:00'
updated_at: '2020-06-10T18:06:50+00:00'
type: issue
status: closed
closed_at: '2020-06-10T18:06:50+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 10 June 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-06-10T18:06:50+00:00
    [2020-06-10 12:58:57] <sarang> OK, just about time to start the meeting
    [2020-06-10 12:59:16] <sarang> First, greetings!
    [2020-06-10 12:59:41] <ArticMine> Hi
    [2020-06-10 13:00:22] <sgp_> hello
    [2020-06-10 13:01:13] <Isthmus> Heya
    [2020-06-10 13:01:20] <sarang> I suppose we can move to the roundtable, where anyone is welcome to share research of interest
    [2020-06-10 13:01:29] <sarang> Does anyone want to go first?
    [2020-06-10 13:02:10] <sarang> If not, I can share a few things
    [2020-06-10 13:02:36] <sarang> Teserakt has sent me a draft of their analysis of the CLSAG preprint
    [2020-06-10 13:02:36] <monerobux> Test failed
    [2020-06-10 13:02:43] <sarang> bad bot
    [2020-06-10 13:03:22] <sarang> The draft report indicates they did not find any major issues with the construction, but they had some comments and suggestions on the formalization that I'm working to update
    [2020-06-10 13:03:30] <sarang> This shouldn't result in any changes to the code
    [2020-06-10 13:04:11] <sarang> Separately from this, I started working on some output merging analysis on the Monero chain
    [2020-06-10 13:04:16] <h4sh3d[m]> Hello
    [2020-06-10 13:04:29] <sarang> I have preliminary data but am still checking it for a few questions I have
    [2020-06-10 13:05:02] <sarang> I'll post a plot here, but note that it should not be relied on until checked more thoroughly
    [2020-06-10 13:05:18] <sarang> https://usercontent.irccloud-cdn.com/file/EHmFolZV/data_all.png
    [2020-06-10 13:05:27] <sarang> An explanation...
    [2020-06-10 13:05:38] → kiwi_87 joined (0ee2e917@gateway/web/cgi-irc/kiwiirc.com/ip.14.226.233.23)
    [2020-06-10 13:06:00] <sarang> I look for "zero-hop" possible merges, where outputs from the same source transaction appear in separate rings in a later destination transaction, and filter only by post-CT confidential transactions
    [2020-06-10 13:06:23] <sarang> Then, for each such possible merge, I look at the height difference of the source and destination transaction, and plot them here
    [2020-06-10 13:06:48] <sarang> The x-axis represents block height difference, and the y-axis is fractional occurrence (note the log scale!)
    [2020-06-10 13:07:07] <kiwi_87> Hi. What you think about interoperability on Monero?
    [2020-06-10 13:07:21] → atoc joined (2fb9e903@47.185.233.3)
    [2020-06-10 13:07:42] ⇐ atoc quit (2fb9e903@47.185.233.3): Remote host closed the connection
    [2020-06-10 13:08:01] <sarang> kiwi_87: one sec
    [2020-06-10 13:08:09] <Isthmus> 👀
    [2020-06-10 13:08:13] <Isthmus> Very interesting
    [2020-06-10 13:08:18] <sarang> https://usercontent.irccloud-cdn.com/file/UPSZyk6P/data_1k.png
    [2020-06-10 13:08:41] <sarang> Here is the same data, but zoomed (and rescaled) to the low end of the x-axis
    [2020-06-10 13:08:43] → atoc joined (2fb9e903@47.185.233.3)
    [2020-06-10 13:09:11] <sarang> Now, these are only possible merges; there's no good ground-truth data set on chain for post-CT confidential transactions
    [2020-06-10 13:09:16] <atoc> hi
    [2020-06-10 13:09:30] <sarang> So I'm going to run a simulation using the same input/output structure and the current decoy selection algorithm
    [2020-06-10 13:09:36] <sarang> and see if/where the distributions diverge
    [2020-06-10 13:09:57] <sarang> kiwi_87: what do you mean by interoperability
    [2020-06-10 13:10:24] <sarang> Oh, and for this data... about 2.3% of post-CT confidential transactions contained at least one possible merge
    [2020-06-10 13:10:38] <sarang> (this data shows all such possible merges, not just a unique one from each transaction)
    [2020-06-10 13:11:42] <Isthmus> @sarang if you want to go deep into the Bayesian weeds, could calculate the probability (always positive, but varying in magnitude) that a pair(+) of these ring members would be selected together if sampled from the standard  algo
    [2020-06-10 13:11:43] <UkoeHB_> Isthmus: do you recall what proportion of transactions don't use the standard gamma distribution (approximately)?
    [2020-06-10 13:12:06] <sarang> UkoeHB_: note that this is _all_ post-CT confidential transactions, regardless of likely selection method
    [2020-06-10 13:12:25] <sarang> I did a filter for that but may have a minor indexing issue that threw off the data
    [2020-06-10 13:12:48] <sarang> Isthmus: yeah, I thought about that too (but didn't run the analysis)
    [2020-06-10 13:13:22] <sarang> The distribution difference is intended to give a very rough idea of how non-ideal this distribution is
    [2020-06-10 13:13:40] <ArticMine> The other question is ring size
    [2020-06-10 13:13:43] <Isthmus> @UkoeHB_ as of Konferenco (last June) about 1% of transactions used obviously uniform selection algorithm
    [2020-06-10 13:14:12] <Isthmus> I haven't updated the analysis pipeline, so can't speak to recent months.
    [2020-06-10 13:14:21] <UkoeHB_> ah if sarang is already filtering those out it's not a big deal
    [2020-06-10 13:14:30] <sarang> I'm not at the moment
    [2020-06-10 13:14:37] <sarang> This is all post-CT confidential transactions
    [2020-06-10 13:14:46] <Isthmus> @sarang what are you coding this in? I have python code to strip those out
    [2020-06-10 13:14:53] <sarang> This is Python as well
    [2020-06-10 13:15:05] <sarang> If you can link the code that'd be great, or I can write something up
    [2020-06-10 13:15:42] <sarang> But uniform selection seems very unlikely to cause the long tail
    [2020-06-10 13:17:16] <sarang> Anyway, this is the start of analysis that I hope will be useful to inform safer output selection
    [2020-06-10 13:17:31] <UkoeHB_> very cool thanks for you effort sarang :)
    [2020-06-10 13:17:36] <sarang> Once I verify this indexing issue, I'll post both the analysis code and the data set
    [2020-06-10 13:17:47] <Isthmus> https://www.irccloud.com/pastebin/BChX6gR9/
    [2020-06-10 13:17:49] <sarang> I can't post _all_ the data (block, transaction, ring, ...) since it's far too big for GitHub
    [2020-06-10 13:17:50] <kiwi_87> @sarang, I mean the interoperability, if it can be made between Monero and other chains, there would be more room for the adoption of XMR. I learn about this from the fact that Bitcoin is entering Ethereum network with the amount that is way larger than which on the layer 2 of Bitcoin. It helps BTC to join the DeFi and increase the adoption for
    [2020-06-10 13:17:50] <kiwi_87> such crypto. Same thing can also happen with XMR, don’t you think?
    [2020-06-10 13:18:02] <sarang> But I can post the resulting possible merges, which are of reasonable size
    [2020-06-10 13:18:19] <sarang> Thanks Isthmus
    [2020-06-10 13:18:51] <Isthmus> https://usercontent.irccloud-cdn.com/file/fZgJlX2o/image.png
    [2020-06-10 13:18:51] <sarang> kiwi_87: operating between Monero and other chains is surprisingly tricky, and even moreso if the goal is to maintain uniformity of transactions
    [2020-06-10 13:18:53] <Isthmus> https://usercontent.irccloud-cdn.com/file/aQVzvAAq/image.png
    [2020-06-10 13:19:09] <sarang> Isthmus: what are these plots?
    [2020-06-10 13:20:28] <Isthmus> Let ring_member_ages be an array of ring member ages [0.5d, 0.7d, ...]
    [2020-06-10 13:20:43] <Isthmus> offset-corrected median age = median(ring_member_ages - min(ring_member_ages)
    [2020-06-10 13:21:14] <Isthmus> The correct decoy algorithm produces OCMA's around 100 - 10000 blocks
    [2020-06-10 13:21:33] <Isthmus> I used 370000 as a conservative "absurdity limit"
    [2020-06-10 13:21:34] <sarang> Small sample => high variance, I assume?
    [2020-06-10 13:22:01] <Isthmus> Might also have to do with fact that algo reacts to txn vol changes
    [2020-06-10 13:22:20] <Isthmus> Anyways, anything above 10^5 is suspect
    [2020-06-10 13:22:23] <Isthmus> Red line is 370000 blolcks
    [2020-06-10 13:22:32] <Isthmus> Anything above that is absolutely not from the correct decoy algo
    [2020-06-10 13:22:47] <sarang> Examining the distribution with that filter will be very interesting
    [2020-06-10 13:22:48] <Isthmus> And in most cases, when I spot checked, were due to apparent uniform decoy selectioin algo
    [2020-06-10 13:23:05] <sarang> I'd expect that it wouldn't change much, but I like being proven wrong
    [2020-06-10 13:24:13] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Ping timeout: 264 seconds
    [2020-06-10 13:24:20] <sarang> Any other speculation about the effects of these selections? (just curious)
    [2020-06-10 13:25:21] <Isthmus> Hmm, I'm interested in the Bayesian analysis, which will tell us whether this is a novelty with 10% predictive power, or a damning tell with 95% predictive power
    [2020-06-10 13:25:24] <sarang> Oh and Isthmus: what transactions does this account for? The entire chain?
    [2020-06-10 13:25:42] <Isthmus> From introduction of RingCT until Konferenco
    [2020-06-10 13:25:58] <sarang> Does it filter out non-CT transactions after the CT cutoff?
    [2020-06-10 13:26:09] <sarang> These are low quantity, but are still present
    [2020-06-10 13:26:17] <sarang> and have very different selection of course
    [2020-06-10 13:26:37] <Isthmus> I usually ignore non-RingCT since I'm more interested in optimizing current privacy than studying historical easter eggs
    [2020-06-10 13:26:44] <sarang> yeah
    [2020-06-10 13:26:51] <Isthmus> I'll have to work my way back in the analysis pipeline to check
    [2020-06-10 13:26:54] <sarang> I also filtered those in the plots above
    [2020-06-10 13:27:08] <Isthmus> Sorry, by "ignore" RingCT, I mean "exclude them from my data set before analyzing"
    [2020-06-10 13:27:13] <sarang> roger
    [2020-06-10 13:27:15] <Isthmus> s/RingCT/non-RingCT
    [2020-06-10 13:27:16] <monerobux> Isthmus meant to say: Sorry, by "ignore" non-RingCT, I mean "exclude them from my data set before analyzing"
    [2020-06-10 13:28:25] <sarang> Oh, and I might have mentioned this last week (don't recall), but I'm still working with those CMU student researchers to confirm some updated deducibility analysis
    [2020-06-10 13:28:34] <sarang> They plan to revise their preprint once again
    [2020-06-10 13:29:07] <sarang> This is especially nice given that their "30% traceable" (or whatever it was) conclusion regarding spend age heuristics is incorrect
    [2020-06-10 13:29:30] <kiwi_87> @sarang. Yeah I know it’s the hardest part. Actually our research at Incognito project is currently on this direction.
    [2020-06-10 13:29:32] <kiwi_87> We have the idea of building a privacy chain learning the technology from Monero, thus allowing the high level of privacy for the chain.
    [2020-06-10 13:29:40] <kiwi_87> Then build a Portal connecting to Monero with a group of decentralized custodians holding & releasing XMR when users going in & going out the layer 2. The same design can be applied to BTC, which brings XMR & BTC to the same privacy layer.
    [2020-06-10 13:29:40] <kiwi_87> What do you guys all think?
    [2020-06-10 13:30:05] <sarang> This might be a better conversation for after the meeting kiwi_87 if it mainly concerns research for another project
    [2020-06-10 13:30:14] <sarang> Unless the group disagrees
    [2020-06-10 13:30:25] <moneromooo> Not this silent part of the group.
    [2020-06-10 13:31:03] <sarang> Were there any other questions on the deducibility or output merging data?
    [2020-06-10 13:32:23] <sarang> If not, does anyone else wish to present research of interest for this group?
    [2020-06-10 13:32:40] <Isthmus> @kiwi_87 cool, I like  seeing these types of projects. 👍
    [2020-06-10 13:32:49] <h4sh3d[m]> I can give some updates about the swap
    [2020-06-10 13:32:54] <sarang> Please do
    [2020-06-10 13:33:14] <sarang> (this may be relevant to you kiwi_87)
    [2020-06-10 13:33:18] <h4sh3d[m]> I started working on it, I plan to have an updated version of the paper next week
    [2020-06-10 13:33:37] <h4sh3d[m]> So, the idea is still the same as before
    [2020-06-10 13:34:21] <kiwi_87> @sarang yeah sure. I’ll talk more about what we are doing in the after-meeting time. Still, I think  interoperability on XMR could be a very bright way to increase the Monero adoption. Would love to talk to other researchers who are also diving in the same direction
    [2020-06-10 13:34:34] <h4sh3d[m]> split the monero spending key in two halfs, and "sell" one half or the other on the bitcoin chain depending if the swap success or not
    [2020-06-10 13:34:47] <sarang> via multisig, I assume
    [2020-06-10 13:35:13] <sarang> "You get the even bytes, and I keep the odd bytes!"
    [2020-06-10 13:35:34] <h4sh3d[m]> Yes, kind of. Before there was the generic zkp for the hash preimage
    [2020-06-10 13:35:39] <kiwi_87> @Isthmus sure. Would love to share more in the after-meeting time. Now let’s make the convo laser-focused on Monero
    [2020-06-10 13:36:06] <sarang> h4sh3d[m]: but you're replacing with a cross-group DL equivalence proof via side channel, correct?
    [2020-06-10 13:36:32] → ferretinjapan joined (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan)
    [2020-06-10 13:36:45] <kiwi_87> @h4sh3d[m] would love to hear about this. Really want to know what’s going on there with the cryptography challenge. Please update us :D
    [2020-06-10 13:36:46] <h4sh3d[m]> Now, by combining dl equality across group + ECDSA one-time VES, we should be able to achieve the same
    [2020-06-10 13:37:10] <h4sh3d[m]> ECDSA one-time VES: https://github.com/LLFourn/one-time-VES/blob/master/main.pdf
    [2020-06-10 13:37:35] <h4sh3d[m]> (it's an ECDSA "adaptor signatures")
    [2020-06-10 13:37:44] <sarang> Remind me: does this approach assume/require any particular timelock capability on the Monero side?
    [2020-06-10 13:37:51] <sarang> If so, to what extent?
    [2020-06-10 13:38:16] <h4sh3d[m]> No, nothing is required on the Monero side, that's the cool part
    [2020-06-10 13:38:21] <sarang> OK, thanks
    [2020-06-10 13:38:49] <sarang> Monero supports a very simple timelock of course
    [2020-06-10 13:39:04] <sarang> but it's a bit inconsistent at the moment, and apparently infrequently used
    [2020-06-10 13:39:13] <sarang> so if it were required, this could present a uniformity issue
    [2020-06-10 13:39:35] <h4sh3d[m]> We create an address where Spend = Spend_alice + Spend_bob (same for view)
    [2020-06-10 13:39:51] <h4sh3d[m]> and send the Monero to <Spend, View> corresponding address
    [2020-06-10 13:40:11] <sarang> Does the address protocol have issues with key cancellation?
    [2020-06-10 13:40:16] <h4sh3d[m]> Each participant has his own half, and one will get the second one
    [2020-06-10 13:40:21] <sarang> Or is there precommitment to address parts?
    [2020-06-10 13:41:24] <h4sh3d[m]> Not sure if I understand what you mean by key cancellation
    [2020-06-10 13:42:46] <sarang> If you hand me a part of a key, maybe I maliciously generate my own "key" such that the sum is any value I want
    [2020-06-10 13:43:11] <h4sh3d[m]> Ah yes, I thought about that
    [2020-06-10 13:43:14] <sarang> If this is problematic, we can each commit to our key portions first, and then check that the keys received match the commitments
    [2020-06-10 13:43:23] <sarang> it ensures that neither party change their mind
    [2020-06-10 13:43:32] <sarang> Adds a communication round
    [2020-06-10 13:44:22] <sarang> There are other methods involving random-oracle linear combinations too, depending on what you need
    [2020-06-10 13:44:28] <h4sh3d[m]> I thought about the commit, but that also mean you don't know your correct "half" (only the destiantion priv/pub), and without priv half, you are not able to continue the protocol
    [2020-06-10 13:44:30] <sarang> But sorry, I'm digressing here
    [2020-06-10 13:44:34] <kiwi_87> @sarang @h4sh3d[m] just thinking out loud, both atomic swap & layer 2 swap are all good for XMR because they make the trustless swap XMR<>BTC. But if we want trustless swap XMR<>other cryptos, we will need more atomic swap designs and Portal designs connecting layer 2 and Monero chain
    [2020-06-10 13:44:46] <h4sh3d[m]> No, it's a good one
    [2020-06-10 13:44:48] <sarang> kiwi_87: let's discuss after the meeting
    [2020-06-10 13:45:28] <sarang> h4sh3d[m]: ok, as long as it's either not necessary or taken care of via a communication round, I suppose
    [2020-06-10 13:45:39] ⇐ iDunk quit (~iDunk@unaffiliated/idunk): Ping timeout: 260 seconds
    [2020-06-10 13:45:44] <sarang> But certainly worth a close eye after the paper is updated
    [2020-06-10 13:46:40] <h4sh3d[m]> when we get the address, and the initialization phase is done (with zkp dl equality e.g.), one send Monero into it
    [2020-06-10 13:46:47] <kiwi_87> @sarang sure
    [2020-06-10 13:47:23] <h4sh3d[m]> at the end, Alice or Bob, will learn the full private spend key = priv_spend_alice + priv_spend_bob
    [2020-06-10 13:47:36] <h4sh3d[m]> So no, nothing fancy required on the Monero side
    [2020-06-10 13:48:02] <atoc> nice
    [2020-06-10 13:48:08] <h4sh3d[m]> You will import the full keys in you wallet and do a regular transaction
    [2020-06-10 13:48:12] <sarang> Definitely look forward to seeing the updated paper h4sh3d[m]!
    [2020-06-10 13:48:40] <atoc> same
    [2020-06-10 13:48:46] <h4sh3d[m]> (keys that are generated withou a seed and a derivation function, so wallet must support "raw" keys)
    [2020-06-10 13:49:18] <h4sh3d[m]> Right now, I'm in the one-time VES paper, and your MRL-0010 one
    [2020-06-10 13:49:27] <sarang> got it
    [2020-06-10 13:49:43] <h4sh3d[m]> * I'm done, thanks for your inputs
    [2020-06-10 13:49:53] <sarang> I might update MRL-0010 to specify that the Pedersen generators need an unknown DL relationship
    [2020-06-10 13:50:15] <sarang> Apparently that wasn't listed specifically, but is generally true for Pedersen commitment security
    [2020-06-10 13:50:16] <sarang> In the interest of time, were there any other research topics that need to be presented before the hour is up?
    [2020-06-10 13:50:46] <Isthmus> Quick update: I’m really happy to share that we’re officially beginning our audit of monero’s security and privacy mechanisms against algorithms that could be exploited by hypothetical quantum adversaries. Thank you to everybody who contributed feedback or funds to our CCS 🙏
    [2020-06-10 13:50:50] <Isthmus> The first step is a formalizing our adversary model and enumerating of mechanisms of interest.
    [2020-06-10 13:50:53] <Isthmus> Right now the attack surface list looks like {Ring Signatures, RingCT, One-time "Stealth" Addresses, Pubkey derivation, Forge amounts?, Bulletproofs, RandomX proof-of-work, Block / Transaction hashing}.
    [2020-06-10 13:50:56] <Isthmus> Please suggest other pieces that you’d like to see audited. :- )
    [2020-06-10 13:51:02] <Isthmus> Earlier I was looking at the wallet generation schematic shared to Reddit, and it has me pondering visual ways to communicate results. https://www.reddit.com/r/Monero/comments/gy0m1u/i_made_an_infographic_on_how_a_monero_wallet_is/
    [2020-06-10 13:51:02] <monerobux> [REDDIT] I made an infographic on how a Monero wallet is generated. Can you find any mistakes? (https://i.redd.it/tv98m10mbd351.png) to r/Monero | 163 points (100.0%) | 18 comments | Posted by Krakataua314 | Created at 2020-06-06 - 22:42:54
    [2020-06-10 13:51:04] <Isthmus> https://i.redd.it/tv98m10mbd351.png
    [2020-06-10 13:51:07] <Isthmus> For example, the ed25519 scalarmult (used for private view key → public viewkey) is a one-way function for traditional computers (assuming hardness of the discrete log problem) but can be reversed if you can apply Shor’s algorithm.
    [2020-06-10 13:51:12] <Isthmus> So perhaps this could be visually annotated with directional arrow for traditional adversaries and bidirectional arrow for hypothetical quantum adversaries. Would that be an intuitive approach?
    [2020-06-10 13:51:33] <sarang> I like that idea
    [2020-06-10 13:51:45] <sarang> that's very clever
    [2020-06-10 13:52:52] ⇐ kiwi_87 quit (0ee2e917@gateway/web/cgi-irc/kiwiirc.com/ip.14.226.233.23): Quit: Connection closed
    [2020-06-10 13:53:14] <sarang> Can you remind us of the expected timeline Isthmus?
    [2020-06-10 13:53:31] <Isthmus> Will be working on this full time for the next 3 months
    [2020-06-10 13:53:36] <sarang> (with the understanding that research often takes unexpected twists)
    [2020-06-10 13:54:05] <Isthmus> Phase 1 should be quick
    [2020-06-10 13:54:14] <sarang> The scope was modified to focus less on deliverable code, right?
    [2020-06-10 13:54:31] <sarang> And more on solid understanding, possible mitigations and relevant work, and communication?
    [2020-06-10 13:54:34] <Isthmus> Just setting the stage for our object of study and attacker, hoping to have a first "final draft" of that done by next MRL meeting
    [2020-06-10 13:54:38] <sarang> Oh nice
    [2020-06-10 13:54:42] <Isthmus> Yep
    [2020-06-10 13:54:44] <sarang> That'll be great to see
    [2020-06-10 13:54:51] <Isthmus> And then working systemically through the cross sections
    [2020-06-10 13:55:17] <Isthmus> (table where each column is a quantum adversary and each row is a piece of Monero tech)
    [2020-06-10 13:55:19] <Isthmus> My guess is that we'll be able to fill 80% of the squares in 20% of the time
    [2020-06-10 13:55:24] <Isthmus> And then 20% of the squares will take 80% of the time
    [2020-06-10 13:55:24] <sarang> Do you expect that the final results will be suitable for broader distribution? Like to journals, refereed conferences, or simply IACR archive?
    [2020-06-10 13:56:14] <Isthmus> Throughout this entire project, the community will receive updates during the weekly #monero-research-lab meetings. During phase 3 however, several specific documents (the key deliverables from this research) will be freely published
    [2020-06-10 13:56:18] <Isthmus> 1. User-friendly writeup: This community-facing writeup will provide an approachable explanation of how hypothetical quantum computers may impact Monero, and possible future mitigations. The writeup should minimize FUD and provide the context that these vulnerabilities apply to almost all cryptocurrencies (not only Monero).
    [2020-06-10 13:56:31] <Isthmus> 2. Technical documentation: An MRL position paper to distill key information for (current and future) researchers and developers. The writeup should formally describe vulnerabilities, and highlight potential strategies and solutions, noting their tradeoffs. Code snippets may be included if appropriate for pedagogical purposes or clarity.
    [2020-06-10 13:56:37] <Isthmus> 3. Non-technical 1-pager: An ELI5 / TL;DR summary will be provided for journalists, Monero Outreach, etc. This blurb will discuss risks and myths with no technical jargon, with key takeaways that a broad audience will appreciate.
    [2020-06-10 13:56:41] <Isthmus> (Results and updates will be also disseminated via Twitter threads, Reddit posts, and Breaking Monero videos.)
    [2020-06-10 13:57:01] <Isthmus> And yea, hopefully we can get a paper or two out of this
    [2020-06-10 13:57:16] <Isthmus> Much of the research will be broadly applicable
    [2020-06-10 13:57:42] <sarang> Great!
    [2020-06-10 13:58:00] <atoc> Nice
    [2020-06-10 13:58:36] <sarang> Getting a better sense of research trends in this direction, even if not presently applicable, will be intriguing to see
    [2020-06-10 13:59:04] <sarang> e.g. there are plenty of ideas for post-quantum constructions, but there are generally huge barriers in efficiency that render them unusable
    [2020-06-10 13:59:09] → iDunk joined (~iDunk@unaffiliated/idunk)
    [2020-06-10 13:59:27] <atoc> btw Isthmus, this may be off topic but can you talk a little more about the Insight program?
    [2020-06-10 13:59:27] <sarang> OK, we're just about out of time
    [2020-06-10 13:59:41] <sarang> atoc: perhaps for right after the meeting?
    [2020-06-10 13:59:44] <atoc> yes
    [2020-06-10 13:59:55] <sarang> Are there any other last questions or comments about these research topics before adjourning?
    [2020-06-10 14:00:19] <sarang> If not, thanks to everyone for attending and participating!


# Action History
- Created by: SarangNoether | 2020-06-05T15:32:08+00:00
- Closed at: 2020-06-10T18:06:50+00:00
