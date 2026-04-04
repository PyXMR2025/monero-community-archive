---
title: 'Research meeting: 15 April 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/454
author: SarangNoether
assignees: []
labels: []
created_at: '2020-04-09T01:21:03+00:00'
updated_at: '2020-04-15T18:16:21+00:00'
type: issue
status: closed
closed_at: '2020-04-15T18:16:21+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 15 April 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-04-15T18:16:21+00:00
    [2020-04-15 12:59:39] <sarang> First, GREETINGS
    [2020-04-15 12:59:42] <sarang> Hello
    [2020-04-15 12:59:52] <ArticMine> Hi
    [2020-04-15 12:59:55] <Isthmus> Heya
    [2020-04-15 12:59:57] <UkoeHB_> hi
    [2020-04-15 13:00:29] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-04-15 13:00:42] <binaryFate> hi!
    [2020-04-15 13:01:01] <sarang> I'll wait a couple of minutes for anyone else to arrive
    [2020-04-15 13:01:15] ⇐ Insight quit (sid415968@gateway/web/irccloud.com/x-bbahcfjkmlxlfhtn): 
    [2020-04-15 13:03:04] <sgp_> hello
    [2020-04-15 13:03:21] <sarang> All right, on to ROUNDTABLE
    [2020-04-15 13:03:31] <sarang> Who would like to share any research of interest?
    [2020-04-15 13:03:43] ⇐ maxwilliamson quit (~maxwillia@gateway/tor-sasl/maxwilliamson): Ping timeout: 240 seconds
    [2020-04-15 13:03:50] <xmrmatterbridge> <cankerwort> Howdy
    [2020-04-15 13:04:11] <UkoeHB_> https://github.com/monero-project/research-lab/issues/73
    [2020-04-15 13:04:17] → gizmanade joined (59faaf6b@gateway/web/cgi-irc/kiwiirc.com/ip.89.250.175.107)
    [2020-04-15 13:04:24] → maxwilliamson joined (~maxwillia@gateway/tor-sasl/maxwilliamson)
    [2020-04-15 13:04:28] <UkoeHB_> Research is a big word, but there's an idea
    [2020-04-15 13:06:10] <sarang> It'd be possible for a recipient to miss spendable funds if this value weren't included properly
    [2020-04-15 13:06:34] <binaryFate> is there any potential issue if the sender does not play "nicely" (purposefully fail the scheme) but can nonetheless prove having sent some outputs to the recipient?
    [2020-04-15 13:06:35] <UkoeHB_> same is true for tx pub keys
    [2020-04-15 13:07:05] <Isthmus> If the sender doesn't follow the rules, recipient won't see a message showing receipt of funds.
    [2020-04-15 13:07:14] <Isthmus> So they'd just ask the sender to make a valid transaction
    [2020-04-15 13:07:28] <sarang> Yep
    [2020-04-15 13:07:41] <Isthmus> Really, the sender hurt themselves
    [2020-04-15 13:07:59] <sarang> It's similar to if a sender sent a bad commitment,e tc.
    [2020-04-15 13:08:06] <sarang> (except for the spendability property)
    [2020-04-15 13:08:20] → TheoStorm joined (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl)
    [2020-04-15 13:08:24] <UkoeHB_> if there is a wallet that doesnt make view tags correctly, it will be a worthless wallet
    [2020-04-15 13:08:29] <Isthmus> Bingo
    [2020-04-15 13:08:29] <UkoeHB_> and quickly get patched
    [2020-04-15 13:08:30] <xmrmatterbridge> <cankerwort> Surely this would be a kind of "fast scan" and if the sender messed it up somehow it would still show up in a normal scan?
    [2020-04-15 13:08:42] <sarang> yes
    [2020-04-15 13:08:43] <binaryFate> They can "DoS" an exchange support easily
    [2020-04-15 13:09:06] ← gizmanade left (59faaf6b@gateway/web/cgi-irc/kiwiirc.com/ip.89.250.175.107): 
    [2020-04-15 13:09:19] → gizmanade joined (59faaf6b@gateway/web/cgi-irc/kiwiirc.com/ip.89.250.175.107)
    [2020-04-15 13:09:31] <binaryFate> Probably hurt them more than the exchange
    [2020-04-15 13:09:53] <UkoeHB_> yeah cankerwort it would be trivial to have fast/normal scan differentiation; the technique is very simple
    [2020-04-15 13:10:26] <sarang> And wallets don't have to use the method to scan at all if they don't want to
    [2020-04-15 13:11:38] <selsta> how would fast scan work together with supercop EC ASM? would ASM still bring a scanning speedup?
    [2020-04-15 13:12:00] <binaryFate> would there be interesting tradeoff too with a bit more or a bit less than a byte? (changing the 1/256 chance)
    [2020-04-15 13:13:04] <Isthmus> The speedup is huge if you're looking for 1-2 addresses, but marginal if you're scanning for 20,000 transactions, right?
    [2020-04-15 13:13:11] <UkoeHB_> my thought is 1 byte is a very standard size, and going lower gets kinda hacky; more than that I can't imagine meaningful improvement
    [2020-04-15 13:13:11] <Isthmus> *1-2 transactions
    [2020-04-15 13:13:44] <UkoeHB_> which speedup?
    [2020-04-15 13:14:52] <UkoeHB_> if somehow you own 80% of all tx, then yeah the view tag only helps you for (255/256)*.2 of the rest
    [2020-04-15 13:15:03] <xmrmatterbridge> <cankerwort> So a scan under this system would scan (1/256 of all transactions) + (actually relevant transactions) - overlap
    [2020-04-15 13:16:03] <UkoeHB_> right
    [2020-04-15 13:16:17] <UkoeHB_> and 'scan' just means perform a few more ec operations
    [2020-04-15 13:16:23] <UkoeHB_> per output
    [2020-04-15 13:16:33] <UkoeHB_> it's actually 1/256 of all outputs, not tx
    [2020-04-15 13:16:50] → asdc_ccc joined (~asdc_cccc@95-178-173-249.dsl.optinet.hr)
    [2020-04-15 13:17:01] <Isthmus> ah yea, ty
    [2020-04-15 13:17:12] <TheCharlatan> why only one byte? Are two bytes too revealing?
    [2020-04-15 13:17:21] <UkoeHB_> diminishing returns
    [2020-04-15 13:17:47] <UkoeHB_> the marginal scan change from 1 byte to 2 byte view tags is tiny
    [2020-04-15 13:18:58] <sarang> OK, noted
    [2020-04-15 13:19:07] <sarang> Any additional questions on this idea at this point?
    [2020-04-15 13:19:34] <UkoeHB_> any objections also?
    [2020-04-15 13:19:48] <Isthmus> I like it
    [2020-04-15 13:19:58] <TheCharlatan> yes :)
    [2020-04-15 13:20:15] <Isthmus> Hopefully this will reduce the "Y MONERO SO SLO TO SYNC" posts on reddit by 1/256 too
    [2020-04-15 13:20:28] <UkoeHB_> one can only dream
    [2020-04-15 13:20:37] → sech11 joined (~sech1@31-208-56-185.cust.bredband2.com)
    [2020-04-15 13:20:38] <xmrmatterbridge> <cankerwort> I suppose generally speaking the fork when transactions get smaller anyway is a good time to introduce these QoL improvements
    [2020-04-15 13:20:46] <binaryFate> this looks great
    [2020-04-15 13:21:07] <sarang> Well, there doesn't seem to be a plan for whether or not to include Janus mitigations, which have been brought up repeatedly before
    [2020-04-15 13:21:19] <xmrmatterbridge> <cankerwort> or is any reduction in transaction sizes already earmarked for bigger ringsizes?
    [2020-04-15 13:21:34] <sarang> There is currently no concrete plan to increase the ring size with CLSAG
    [2020-04-15 13:22:17] <sarang> Note that the move from MLSAG to CLSAG will reduce the typical 2-2 transaction from 2.5 kB to 1.9 kB in size
    [2020-04-15 13:22:25] <sarang> (absent any other changes)
    [2020-04-15 13:22:58] <UkoeHB_> I think the discussion about Janus and tx extra has made some small progress
    [2020-04-15 13:23:13] <sarang> Sure, but small progress != PR
    [2020-04-15 13:23:14] <sarang> :D
    [2020-04-15 13:24:06] ⇐ sech1 quit (~sech1@31-208-56-185.cust.bredband2.com): Ping timeout: 265 seconds
    [2020-04-15 13:24:55] <sarang> Anything else you'd like to discuss UkoeHB_?
    [2020-04-15 13:25:20] <UkoeHB_> dont think so thanks sarang
    [2020-04-15 13:25:26] <sarang> OK thanks UkoeHB_ 
    [2020-04-15 13:25:40] <sarang> Does anyone else wish to share research of interest?
    [2020-04-15 13:25:56] <sarang> If not, I have a couple of things to share
    [2020-04-15 13:26:03] <Isthmus> Hmm, I’m still working on creating a graph formalism for fungibility defects. Made a little bit of progress since last week, but it’s still not quite coherent. Being rigorous is hard. Hopefully will have something to share in a week or two.
    [2020-04-15 13:26:08] <Isthmus> I’m cooking up some stuff with Insight too. One of the Fellows put together a patch to prevent coinbase underclaiming now that we’ve moved away from discretized outputs. I just looked at the code, will clean it up and submit for consideration/review.
    [2020-04-15 13:26:12] <Isthmus> I want to get more of Insight’s engineers working in our ecosystem! Insigght has been pouring a ton of R & D resources into Polkadot, ICON, Zcash, etc. I really want to leverage my team to contribute to the Monero community at this scale too.
    [2020-04-15 13:26:15] <Isthmus> Having a few internal syncs to match Fellows onto open challenges, based on their skills/passions/interests.  Hopefully in the next week or two, I’ll be introducing new contributors. :- )
    [2020-04-15 13:26:35] <sarang> Nice
    [2020-04-15 13:26:38] <Isthmus> More details coming soon as those conversation proceed
    [2020-04-15 13:26:41] <sarang> What kinds of projects?
    [2020-04-15 13:27:11] <Isthmus> Meeting with the candidates this week to nail that down based on their skillsets
    [2020-04-15 13:27:18] <sarang> got it
    [2020-04-15 13:27:25] — Isthmus hands the mic to sarang for other updates
    [2020-04-15 13:27:27] <xmrmatterbridge> <cankerwort> And now I need to go find out wtf is Polkadot and ICON all evening
    [2020-04-15 13:27:32] <sarang> Thanks Isthmus 
    [2020-04-15 13:27:41] <sarang> This PR to speed up Bulletproofs is ready to go: https://github.com/monero-project/monero/pull/6451
    [2020-04-15 13:28:02] <sarang> Applies retroactively, and has some pretty nice improvements
    [2020-04-15 13:28:23] <sarang> Saves 25% on a 64-batch of 2-output proofs
    [2020-04-15 13:28:35] <sarang> Feel free to review if you like
    [2020-04-15 13:28:55] <ArticMine> Excellent
    [2020-04-15 13:28:57] <xmrmatterbridge> <cankerwort> Fantastic news
    [2020-04-15 13:29:03] — binaryFate applause
    [2020-04-15 13:29:21] <sarang> Second, I've been working hard on a Triptych implementation in the codebase, for more accurate real-world testing
    [2020-04-15 13:29:44] <sarang> This is the branch: https://github.com/SarangNoether/monero/tree/triptych
    [2020-04-15 13:29:55] <sarang> (note that this code is not production-ready, and should not be used in anything important)
    [2020-04-15 13:30:21] <sarang> Size data comparison: https://usercontent.irccloud-cdn.com/file/KvolrThG/size.png
    [2020-04-15 13:30:36] <xmrmatterbridge> <cankerwort> Triptych = Tryptych 2? As in did one version supersede the other?
    [2020-04-15 13:30:36] <sarang> Verification timing comparison: https://usercontent.irccloud-cdn.com/file/4CATnXf6/timing.png
    [2020-04-15 13:30:54] <sarang> This is for Triptych, which requires separate proofs per input (much like MLSAG and CLSAG require)
    [2020-04-15 13:31:10] <sarang> The timing plot uses performance test data from this branch
    [2020-04-15 13:31:25] <sarang> The gray lines are centered at the 11-MLSAG point for visual reference
    [2020-04-15 13:31:50] <sarang> The timing data does _not_ include some unfinished optimizations, or batching, or common input sets within the same transactions
    [2020-04-15 13:32:39] <sarang> However, it provides an idea of how MLSAG, CLSAG, and Triptych compare generally
    [2020-04-15 13:33:25] <Isthmus> Noice
    [2020-04-15 13:33:39] <TheCharlatan> what's the gray line intersection with the Triptych line x axis value?
    [2020-04-15 13:34:01] <sarang> The vertical gray line is for ring size 11 across all constructions
    [2020-04-15 13:34:12] <sarang> The horizontal line is the size/time value for MLSAG at ring size 11
    [2020-04-15 13:34:16] <sarang> (again, just for visual reference)
    [2020-04-15 13:34:24] <sarang> To help you compare to what we have in place right now
    [2020-04-15 13:34:28] <ArticMine> What is the impact on tx size
    [2020-04-15 13:35:02] <sarang> Each transaction input (not ring element, spent input) requires a single signature, of whatever construction you prefer
    [2020-04-15 13:36:14] <sarang> Moving from 11-MLSAG to ~32-Triptych would result in no change to signature size
    [2020-04-15 13:36:22] <sarang> and would result in slightly faster verification
    [2020-04-15 13:36:31] <binaryFate> really impressive
    [2020-04-15 13:36:46] <xmrmatterbridge> <cankerwort> These are awesome improvements! But the plan is not to go straight for Triptych right?
    [2020-04-15 13:36:48] <sarang> The size data are final; but again, the verification data is still WIP
    [2020-04-15 13:37:14] <sarang> Triptych (and all other WIP next-gen constructions) require a modification to key images that requires new engineering work for multisig
    [2020-04-15 13:37:20] <sarang> It's very nontrivial
    [2020-04-15 13:37:37] <derpy_bridge> <[keybase] seddd>: sorry 4 late. just finishing review of CLSAG, will send draft report to sarang when done. no big findings :)
    [2020-04-15 13:38:12] <sarang> Thanks seddd, much appreciated
    [2020-04-15 13:39:43] <xmrmatterbridge> <cankerwort> seddd = surae?
    [2020-04-15 13:39:51] <derpy_bridge> <[keybase] seddd>: +1
    [2020-04-15 13:40:14] <derpy_bridge> <[keybase] seddd>: not by a long shot cankerwort
    [2020-04-15 13:40:24] <sarang> Finally, ledger/trezor support for CLSAG is getting finished
    [2020-04-15 13:40:33] <derpy_bridge> <[keybase] seddd>: (surae wayyyy smarter)
    [2020-04-15 13:40:36] <sarang> cslashm made a PR that'll be included in the test branch
    [2020-04-15 13:40:46] <sarang> and ledger has a PR on their side for firmware support that's been completed
    [2020-04-15 13:41:55] <xmrmatterbridge> <cankerwort> Nice that hw wallets are so proactive compared to how exchanges were with subaddresses
    [2020-04-15 13:42:34] <derpy_bridge> <[keybase] seddd>: ah, that's my next step. still haven't reviewed the ledger-side stuffs. looked at cslashm's PR tho
    [2020-04-15 13:42:41] <sarang> It's been very nice to see such quick work for ledger/trezor, that's for sure
    [2020-04-15 13:43:02] <sarang> The goal is to have support ready to go at network upgrade time
    [2020-04-15 13:43:12] <sgp_> really cool numbers
    [2020-04-15 13:43:33] <sarang> Anyway, that's my report: BP speedup, Triptych WIP data, CLSAG device-specific support
    [2020-04-15 13:43:46] <sarang> Any other questions for me about those topics?
    [2020-04-15 13:44:14] <sgp_> Are these numbers *likely* similar to Arcturus?
    [2020-04-15 13:44:25] <sgp_> for non-bath
    [2020-04-15 13:44:28] <sgp_> *batch
    [2020-04-15 13:45:15] <xmrmatterbridge> <cankerwort> what is Arcturus?
    [2020-04-15 13:45:41] <sarang> Ah, I renamed Triptych-2, both to reduce name confusion and because it operates differently
    [2020-04-15 13:45:49] <sarang> I never liked the name Triptych-2; it was more of a placeholder
    [2020-04-15 13:45:53] <xmrmatterbridge> <cankerwort> Noted and appreciated
    [2020-04-15 13:46:04] <sarang> I am not good at clever naming :/
    [2020-04-15 13:46:09] <sarang> Anyway, to answer sgp_'s question
    [2020-04-15 13:46:17] <sarang> Arcturus gives better size scaling
    [2020-04-15 13:46:23] <sarang> Verification timing will be very similar to Triptych
    [2020-04-15 13:46:43] <sgp_> size already looks pretty good
    [2020-04-15 13:47:59] <ArticMine> Still if it can be made smaller then it is an improvement
    [2020-04-15 13:48:06] <sarang> With Arcturus, you only need one proof/signature per _transaction_ instead of per _input_
    [2020-04-15 13:48:17] <Isthmus> Ooooh
    [2020-04-15 13:48:30] <sarang> The magic of generator reuse means the verification would be similar (if you use common anon sets for Triptych for comparison)
    [2020-04-15 13:48:40] <sarang> (this difference is why I renamed it)
    [2020-04-15 13:48:59] <sarang> However, keep in mind that Arcturus relies on a nonstandard hardness assumption
    [2020-04-15 13:49:00] <ArticMine> What if any are the disadvantages?
    [2020-04-15 13:49:06] <sarang> ^^
    [2020-04-15 13:49:16] <xmrmatterbridge> <cankerwort> Is the plan still to get CLSAG audited in time for the next fork? Which are now annually apparently?
    [2020-04-15 13:49:26] <sarang> This is my understanding
    [2020-04-15 13:49:31] <sarang> (but it's not my decision)
    [2020-04-15 13:49:41] <binaryFate> sarang what's your feeling about whether the multisig issue can be solved without foreign primitives?
    [2020-04-15 13:50:08] <sarang> As far as I know, we'd need support for general RSA groups for proper multisig with the next-gen constructions
    [2020-04-15 13:50:20] <sarang> This is for signing only, not verification
    [2020-04-15 13:50:45] <sarang> (even though it's RSA groups, there are no trusted setup problems, FWIW)
    [2020-04-15 13:51:00] <binaryFate> And you're confident about this being a requirement, or it's just that nobody found how to do without yet?
    [2020-04-15 13:51:18] <UkoeHB_> I did a writeup on the multisig question here https://github.com/monero-project/research-lab/issues/72
    [2020-04-15 13:51:34] <sarang> If you can point out a homomorphic public-key scheme that can use arbitrary prime-order groups, I'm all ears
    [2020-04-15 13:51:58] <sarang> Yes, it links to code and a description that I worked out
    [2020-04-15 13:52:04] <UkoeHB_> right ^
    [2020-04-15 13:52:19] <sarang> Paillier encryption is not specifically required
    [2020-04-15 13:52:28] <sarang> but you need an additively homomorphic scheme
    [2020-04-15 13:53:05] ⇐ derpy_bridge quit (~derpy_bri@92.223.89.201): Remote host closed the connection
    [2020-04-15 13:53:44] <sarang> Anyway, I've taken a lot of time in this meeting
    [2020-04-15 13:53:49] <sarang> Was there anything else of interest to share here?
    [2020-04-15 13:53:51] → derpy_bridge joined (~derpy_bri@92.223.89.201)
    [2020-04-15 13:54:50] <TheCharlatan> I made a Rust PoC for including timelock blinding and commitments in transactions. The PoC builds transactions and verifies them with CLSAG signing and the locktime blinding mechanism as described in DLSAG. It looks like the additional size requirements are: input and output commitments, auxiliary (dummy) plaintext locktime, locktime image and a range proof. Thanks to CLSAG, there is no further
    [2020-04-15 13:54:52] <TheCharlatan> increase in the signature size. Contrary to the locktime blinding desription in DLSAG, I think we can spare the range proof on the transaction's output locktime. The main size component therefore is the additional range proof. I also had a discussion about aggregating the locktime range proof in a transaction input with the amount range proof in the output with sarang yesterday (admittedly more
    [2020-04-15 13:54:54] <TheCharlatan> of a lesson from sarang, than a discussion). The gist of it is that in transactions with many outputs and inputs, aggregated range proof verification would become prohibitively slow.
    [2020-04-15 13:55:13] <derpy_bridge> <[keybase] seddd>: oh, awesome! please disregard then, sometimes I derp
    [2020-04-15 13:55:59] <sarang> TheCharlatan: there should be an additional 32 bytes to the signature
    [2020-04-15 13:56:07] <sarang> because of the use of an additional auxiliary linking tag
    [2020-04-15 13:56:59] <TheCharlatan> Ah, right I did not include tags in the description :P
    [2020-04-15 13:57:24] <sarang> However, adding 32 bytes per input is still pretty darn good
    [2020-04-15 13:57:32] <sarang> Note that verification will take a hit
    [2020-04-15 13:57:43] <sarang> I have a CLSAG test branch that shows the difference
    [2020-04-15 13:57:52] <sarang> (but I don't recall the numbers)
    [2020-04-15 13:58:10] <sarang> TheCharlatan: is your code public?
    [2020-04-15 13:58:34] <TheCharlatan> yes: https://github.com/TheCharlatan/rs-xmr-cryp/tree/master/timelock
    [2020-04-15 13:58:48] <sarang> Also: note that Triptych can be easily extended to support this as well, since it's also a d-LRS construction like CLSAG is
    [2020-04-15 13:58:51] <sarang> nice thanks
    [2020-04-15 13:59:02] <derpy_bridge> <[keybase] seddd>: TheCharlatan: that's awesome! was going to live-code CLSAG in Rust this Saturday. glad to have another reference impl :)
    [2020-04-15 13:59:44] <sarang> There's also another CLSAG rust implementation available too
    [2020-04-15 13:59:59] <sarang> https://github.com/crate-crypto
    [2020-04-15 14:00:25] <derpy_bridge> <[keybase] seddd>: so nice! thanks sarang :)
    [2020-04-15 14:00:36] <sarang> (I didn't write that, FWIW)
    [2020-04-15 14:00:58] <derpy_bridge> <[keybase] seddd>: for sure, thanks for the link then :)
    [2020-04-15 14:01:07] <TheCharlatan> The crate-crypto implementation is much nicer, mine is more of a quick script.
    [2020-04-15 14:01:30] <sarang> TheCharlatan: what would be helpful from this group at this point?
    [2020-04-15 14:03:36] <TheCharlatan> so I don't have a good feel on the boundaries of bulletproof scaling yet. So I think some more data there would be helpful.
    [2020-04-15 14:03:55] <sarang> OK, I'm glad to help with that if you like
    [2020-04-15 14:04:08] <sarang> (probably best to save those questions for after the meeting)
    [2020-04-15 14:04:14] <TheCharlatan> yes :)
    [2020-04-15 14:04:31] <sarang> Thanks TheCharlatan
    [2020-04-15 14:04:35] <sarang> OK, we're just past the hour mark
    [2020-04-15 14:04:40] <sarang> Let's move on to ACTION ITEMS
    [2020-04-15 14:04:49] <sarang> What do folks plan to work on this week (that they wish to share)?
    [2020-04-15 14:05:02] <sarang> I plan to finish the last Triptych code optimizations, to finalize that timing data
    [2020-04-15 14:05:32] <sarang> as well as the CLSAG device-specific code integration
    [2020-04-15 14:05:39] <sarang> Others?
    [2020-04-15 14:06:04] <UkoeHB_> I think Ill write a brief proposal for Janus + view tag + extra field, a package update
    [2020-04-15 14:06:16] <UkoeHB_> The concept seems to be coalescing
    [2020-04-15 14:07:05] <derpy_bridge> <[keybase] seddd>: just working on finishing up testing/manual review of CLSAG, writing the draft report, etc
    [2020-04-15 14:07:06] <sarang> Yeah, and there are several related ideas there that could happen concurrently
    [2020-04-15 14:08:12] <derpy_bridge> <[keybase] seddd>: _cedes to UkoeHB__
    [2020-04-15 14:09:58] <sarang> Any last questions or comments before we adjourn?
    [2020-04-15 14:10:17] <UkoeHB_> ArticMine: how is the fee proposal coming along?
    [2020-04-15 14:10:45] <binaryFate> just wants to say that was a lot of impressive developments, feels like christmas
    [2020-04-15 14:10:51] <asdc_ccc> ^
    [2020-04-15 14:11:39] <ArticMine> Still working on the fee part.
    [2020-04-15 14:12:31] <sarang> All right; we are adjourned! Thanks to everyone for participating
    [2020-04-15 14:12:34] <sarang> Lots will be posted shortly
    [2020-04-15 14:12:42] <sarang> Discussions can of course continue :)


# Action History
- Created by: SarangNoether | 2020-04-09T01:21:03+00:00
- Closed at: 2020-04-15T18:16:21+00:00
