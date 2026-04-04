---
title: 'Research meeting: 29 April 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/458
author: SarangNoether
assignees: []
labels: []
created_at: '2020-04-27T21:41:49+00:00'
updated_at: '2020-04-29T18:03:40+00:00'
type: issue
status: closed
closed_at: '2020-04-29T18:03:39+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 29 April 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-04-29T18:03:39+00:00
    [2020-04-29 12:59:31] <sarang> OK, let's get started with the research meeting!
    [2020-04-29 12:59:36] <sarang> First, GREETINGS
    [2020-04-29 12:59:37] <sarang> hi
    [2020-04-29 13:00:32] <ArticMine> hi
    [2020-04-29 13:00:34] <derpy_bridge> <[keybase] unseddd>: o7
    [2020-04-29 13:00:57] <UkoeHB_> hi
    [2020-04-29 13:01:17] — Isthmus boots up
    [2020-04-29 13:02:13] ⇐ asymptotically quit (~asymptoti@gateway/tor-sasl/asymptotically): Remote host closed the connection
    [2020-04-29 13:02:14] <sarang> Let's go ahead and continue with the ROUNDTABLE
    [2020-04-29 13:02:22] <sarang> Anyone is welcome to share research topics of interest
    [2020-04-29 13:02:40] → asymptotically joined (~asymptoti@gateway/tor-sasl/asymptotically)
    [2020-04-29 13:03:18] <sarang> I suppose that I can share a few things
    [2020-04-29 13:03:49] <sarang> Relating to timelocks, I extended CLSAG and Triptych to support them
    [2020-04-29 13:03:59] <sarang> CLSAG: https://github.com/SarangNoether/monero/commit/28f098260c5bb4da57bb78ebc885fe27c9f10c39
    [2020-04-29 13:04:05] <sarang> Triptych: https://github.com/SarangNoether/monero/commit/ed48ab1686b7e7405bd6656c18e37ea21e01fe05
    [2020-04-29 13:04:44] <sarang> Here is corresponding timing data: https://usercontent.irccloud-cdn.com/file/dQXuFH2U/timing.png
    [2020-04-29 13:05:02] <sarang> 3-CLSAG and 3-Triptych are the timelock-friendly data series
    [2020-04-29 13:05:16] <sarang> The other data series are unchanged from when I first shared them
    [2020-04-29 13:05:52] <sarang> I suspect that 3-CLSAG could be optimized by perhaps another 10% or so from what appears on the plot
    [2020-04-29 13:06:47] <sarang> Unrelated to this, I'm updating how in-memory key encryption is handled, which is taking a bit longer than expected
    [2020-04-29 13:07:12] <sarang> and am reviewing the new CLSAG fuzzer tool that unseddd provided
    [2020-04-29 13:07:22] <sarang> That's about it from me!
    [2020-04-29 13:07:30] <sarang> Are there any questions that I can answer?
    [2020-04-29 13:07:52] <Isthmus> Nice work
    [2020-04-29 13:07:57] <sarang> Thanks!
    [2020-04-29 13:08:23] <ArticMine> CLSAG optimization in verification time, size or both
    [2020-04-29 13:08:28] <derpy_bridge> <[keybase] unseddd>: seconded, nice stuff sarang
    [2020-04-29 13:08:49] <sarang> ArticMine: in verification time, and only for the new 3-CLSAG variant that would apply to encrypted timelocks
    [2020-04-29 13:08:49] <ArticMine> Great work by the way
    [2020-04-29 13:09:02] <ArticMine> Thanks
    [2020-04-29 13:09:24] <sarang> When I wrote 3-CLSAG, I used a particular multiscalar multiplication that could likely be made faster for this particular case
    [2020-04-29 13:09:56] <sarang> Also, huge thanks to unseddd for reviewing CLSAG and writing the fuzzer tool
    [2020-04-29 13:10:10] <derpy_bridge> <[keybase] unseddd>: is 3-CLSAG limiting the multisig to three parties?
    [2020-04-29 13:10:25] <derpy_bridge> <[keybase] unseddd>: np :)
    [2020-04-29 13:10:26] <sarang> No, it adds another key component that would be used for timelocks
    [2020-04-29 13:10:46] <sarang> Right now we have two key components: one for the usual signing, and the other for balance purposes
    [2020-04-29 13:10:49] <derpy_bridge> <[keybase] unseddd>: ah, thanks for the clarification
    [2020-04-29 13:11:35] <sarang> Does anyone else wish to share research of interest?
    [2020-04-29 13:12:13] * luigi1113 → luigi1111w
    [2020-04-29 13:12:25] <UkoeHB_> it seems like 3-triptych would reduce the ringsize likely to be selected by a power of 2
    [2020-04-29 13:12:38] <derpy_bridge> <[keybase] unseddd>: not much interesting on my end. just reading formal verification papers + some pq-crypto stuff from Mike Hamburg
    [2020-04-29 13:12:43] <sarang> Adding encrypted timelocks is a nontrivial verification hit
    [2020-04-29 13:13:29] <ArticMine> What is the time ans size cost
    [2020-04-29 13:13:44] <sarang> What might be interesting as an alternative would be to allow cleartext timelocks, but update decoy selection to account for known spend patterns
    [2020-04-29 13:14:00] <sarang> It would not eliminate fingerprinting, but could help to mitigate age-related selection heuristics
    [2020-04-29 13:14:22] <derpy_bridge> <[keybase] unseddd>: are there any leakage issues having the timelock in the clear?
    [2020-04-29 13:14:42] <sarang> ArticMine: going from CLSAG to 3-CLSAG is about 1.4x increase in verification time
    [2020-04-29 13:14:59] <sarang> Which could probably be reduced slightly with some extra work
    [2020-04-29 13:15:45] <sarang> In terms of size it's fairly trivial... adding an extra auxiliary key image (this does not account for other non-signature data)
    [2020-04-29 13:16:04] <sarang> unseddd: for sure
    [2020-04-29 13:16:22] <sarang> I'm not saying that I advocate for such an approach, only that it could be an option
    [2020-04-29 13:16:33] <sarang> and would not imply any size/time hits
    [2020-04-29 13:17:07] <UkoeHB_> it's a ways down the road, but I'd like to mention it now; when deciding ring sizes for next gen tx protocol I feel it should be based on a broader analysis of theoretical maximum tx throughput of the network; this is because the max tx volume is when rings are _least_ useful to defend against non-scaling graph heuristics, and because larger ring sizes actually reduce the max tx volume; it's an optimization
    [2020-04-29 13:17:07] <UkoeHB_> problem
    [2020-04-29 13:17:41] <derpy_bridge> <[keybase] unseddd>: right, from a naive perspective, triptych seems like it has enough savings for the hit from timelocks
    [2020-04-29 13:20:04] <sgp_> sorry I'm late. catching up
    [2020-04-29 13:20:04] <ArticMine> UkoeHB_ The maximum tx throughput is also dependent on external factor tat keep improving over time
    [2020-04-29 13:20:43] <UkoeHB_> unfortunately that optimization depends on the efficacy of ring sizes.. which we don't have a complete understanding of; I hope suraeNoether can return to that topic at some point
    [2020-04-29 13:20:55] <UkoeHB_> ArticMine: true, there are a lot of factors to consider!
    [2020-04-29 13:21:23] → atoc joined (2fb9d2fc@47.185.210.252)
    [2020-04-29 13:21:26] <sarang> At the very least, we now have concrete numbers for the spacetime effects of ring size increases
    [2020-04-29 13:21:33] <atoc> hi
    [2020-04-29 13:22:05] <sgp_> the cost of encrypted timelocks seems extreme to me tbh. I don't want to go there unless we know we need to support them for a good use-case
    [2020-04-29 13:22:42] <sarang> Getting timelock-related spend age data from transparent chains might be helpful if it's decided to continue to allow cleartext timelocks
    [2020-04-29 13:23:01] <sarang> Then output selection could be improved to account for it, and reduce the usefulness of spend-age heuristics
    [2020-04-29 13:23:39] <derpy_bridge> <[keybase] unseddd>: use-case: timelocks necessary for atomic swap, encrypting is the most private
    [2020-04-29 13:24:50] <derpy_bridge> <[keybase] unseddd>: could also see the counter-point for clear timelocks if they are necessary for atomic swaps (interop w/ clear chains maybe)
    [2020-04-29 13:25:37] <sgp_> sarang: I agree, but given the current low utilization, I consider this low priority. The impact to the wider network is negligible
    [2020-04-29 13:25:55] <ArticMine> Payment channels come to mind here
    [2020-04-29 13:26:10] <ArticMine> also escrow
    [2020-04-29 13:26:30] <sarang> Getting that kind of transparent chain data seems pretty straightforward
    [2020-04-29 13:26:30] <sgp_> if there's a payment channel, then we can move to make encrypted mandatory. when that happens
    [2020-04-29 13:26:50] <Isthmus> @sarang, it's on my to-do list for XMR and BTC
    [2020-04-29 13:26:54] <sarang> :D
    [2020-04-29 13:27:12] <sarang> How do you plan to examine spend-age data for XMR?
    [2020-04-29 13:27:57] <sarang> It was examined in Miller for "deducible" outputs (pretty sure that's the term they used) that were the result of chain reactions, which we find don't occur anymore
    [2020-04-29 13:28:25] <Isthmus> Oh, I just meant comparing the unlock time height to block height to see how many of them even make sense
    [2020-04-29 13:28:38] <Isthmus> Not that current usage tells us much about future applications.
    [2020-04-29 13:28:45] <sarang> Ah, got it
    [2020-04-29 13:28:52] <Isthmus> What is it that you were interested in?
    [2020-04-29 13:28:53] <atoc> Isthmus are you thinking about atomic swaps these days at all/
    [2020-04-29 13:29:22] <Isthmus> @sarang sorry I'm in a zoom call and IRC meeting at the same time, and missing little pieces of both
    [2020-04-29 13:29:37] <sarang> I'd like to see the age distribution of spent outputs in a transparent asset (like BTC) relative to lock expiration, to see if it differs substantially from the overall age distribution
    [2020-04-29 13:30:04] <sarang> No problem Isthmus!
    [2020-04-29 13:30:09] <Isthmus> ahhh, yea I can't officially do that for Monero yet. I'll pull it for BTC though.
    [2020-04-29 13:30:33] <UkoeHB_> can't officially? it's possible?
    [2020-04-29 13:30:35] <sarang> Thanks! The overall distribution likely is still similar to the Miller data
    [2020-04-29 13:30:42] <sarang> (for BTC, of course)
    [2020-04-29 13:30:58] <sarang> and having that data would be an interesting check of that
    [2020-04-29 13:31:47] <Isthmus> @UkoeHB_ yeah, I mean my research over the past few years reveals anonymity puddles covering like 20% of transactions. Then change outputs bleed everything, so there's a ton of data  on obviously real spend times. BUT no guarantee that it's representative.
    [2020-04-29 13:32:53] <Isthmus> I'll be supper curious to see the BTC distributions, will try to get that in the next week or so.
    [2020-04-29 13:32:57] <Isthmus> *super
    [2020-04-29 13:33:13] <sarang> Yeah, Miller's team used two different large sets of blocks in BTC for their analysis
    [2020-04-29 13:33:22] <sarang> and found the distributions to be similar
    [2020-04-29 13:33:57] <sarang> but it doesn't appear they accounted for locks
    [2020-04-29 13:37:01] <sarang> OK, did anyone else have a topic to discuss?
    [2020-04-29 13:37:21] <Isthmus> Insight is interested in researching practical post-quantum cryptography for Monero, especially privacy features that will remain secure against retrospective deanonymization by future adversaries that can utilize Shor's algorithm, Grover's algorithm, etc. I want to know what our options are, and their costs (complexity, proof size, generation/verification time, etc)
    [2020-04-29 13:37:23] <Isthmus> https://github.com/insight-decentralized-consensus-lab/post-quantum-monero/blob/master/README.md
    [2020-04-29 13:37:37] <Isthmus> Looking for feedback on the research plan.
    [2020-04-29 13:38:43] <Isthmus> Our goals are to (1) study and simulate the threats listed above to assess vulnerability to quantum computers, (2) evaluate post-quantum cryptography scheme candidates to create a roadmap for hardening Monero against quantum adversaries, and (3) provide open-source proof-of-concept code and demos where applicable.
    [2020-04-29 13:39:16] <derpy_bridge> <[keybase] unseddd>: i like pq stuff :) will take a look
    [2020-04-29 13:39:40] → cryptoIndio joined (~cryptoInd@49.145.96.152)
    [2020-04-29 13:40:02] <sarang> Sounds like a fascinating project
    [2020-04-29 13:40:22] <sarang> I'd be very curious to see what exactly the Phase 3 deliverables would look like
    [2020-04-29 13:40:43] <Isthmus> Me too! ^_^
    [2020-04-29 13:40:55] <sarang> and I think it'd be important to assess any transtion points between constructions/protocols
    [2020-04-29 13:41:07] <sarang> e.g. it was possible to transition from pre-CT to post-CT
    [2020-04-29 13:41:21] <Isthmus> Yeah, we'll have to document both the transition and post-transition costs/tradeoffs
    [2020-04-29 13:41:43] <sarang> New constructions are great, but if it's not possible/feasible to transition on the same chain, that's a sticking point
    [2020-04-29 13:42:01] <derpy_bridge> <[keybase] unseddd>: here is the Hamburg paper i am reading through: https://www.shiftleft.org/papers/qromcca/
    [2020-04-29 13:42:12] <ArticMine> Yes this is a very interesting project
    [2020-04-29 13:42:13] — Isthmus bookmarks paper
    [2020-04-29 13:44:30] <sarang> Are you confident about the timeline?
    [2020-04-29 13:44:37] <sarang> Particularly surrounding the Phase 3 stuff
    [2020-04-29 13:45:06] <sarang> (not that practical quantum computers are expected by the end of summer...)
    [2020-04-29 13:45:49] <Isthmus> There's two types of things we could prototype
    [2020-04-29 13:46:00] <UkoeHB_> it does say May - June, only a couple days away, not sure if a CCS could be approved and funded in time
    [2020-04-29 13:46:08] <derpy_bridge> <[keybase] unseddd>: ten million qubits by fall!!!
    [2020-04-29 13:46:16] — Isthmus makes a note to update the date, thanks.
    [2020-04-29 13:46:34] <Isthmus> (1) demo of a quantum computer breaking a Monero encryption feature (at a reduced keysize, or something like that)
    [2020-04-29 13:46:37] <UkoeHB_> s/June/July
    [2020-04-29 13:46:37] <monerobux> UkoeHB_ meant to say: it does say May - July, only a couple days away, not sure if a CCS could be approved and funded in time
    [2020-04-29 13:46:55] <Isthmus> Adam did this before, got an IBM quantum computer mining bitcoin at shorter hash length
    [2020-04-29 13:47:21] <Isthmus> So that's demo breaking classical crypto
    [2020-04-29 13:47:22] <Isthmus> (2) prototype a possible solution
    [2020-04-29 13:47:34] <Isthmus> (so we'd use traditional computers and prototype a future solution)
    [2020-04-29 13:47:36] <derpy_bridge> <[keybase] unseddd>: _thoroughly impressed_
    [2020-04-29 13:47:46] <Isthmus> Now honestly, I think that #2 would be way cooler. But it also may be hopeful thinking
    [2020-04-29 13:48:03] <Isthmus> I've seen Adam rapidly convert math papers to code before, but this is going to be a pretty serious endeavor
    [2020-04-29 13:48:04] <sarang> Either way, would be fascinating
    [2020-04-29 13:48:21] <Isthmus> here was my note in the writeup
    [2020-04-29 13:48:23] <Isthmus> "Phase 3 deliverables: The best use of time during this final stage depends strongly on results from the exploratory research. Likely deliverables are a proof of concept or prototype tooling for demonstrating a vulnerability or potential solution"
    [2020-04-29 13:48:23] <UkoeHB_> would (1) also include a comparison with a classical computer on the same task? at reduced keysizes, the encryption is weaker on classical computers too
    [2020-04-29 13:48:31] <derpy_bridge> <[keybase] unseddd>: Isthmus: are Adam and you regularly in IRC? what is best communication channel?
    [2020-04-29 13:48:35] <Isthmus> @UkoeHB_ exactly
    [2020-04-29 13:48:45] <Isthmus> Adam'll be on IRC shortly :- )
    [2020-04-29 13:48:59] <Isthmus> We'll probably do a lot of the research in this room, if that's okay with people?
    [2020-04-29 13:49:04] <Isthmus> Or could make #pq-mrl
    [2020-04-29 13:49:12] — Isthmus ops just in case
    [2020-04-29 13:49:19] <sarang> Up to you!
    [2020-04-29 13:49:44] <Isthmus> 👍
    [2020-04-29 13:49:47] ⇐ unknownids quit (~unknownid@unaffiliated/unknownids): Read error: Connection reset by peer
    [2020-04-29 13:50:07] → unknownids joined (~unknownid@unaffiliated/unknownids)
    [2020-04-29 13:50:45] <sarang> OK, any other topics to address before finishing up the meeting?
    [2020-04-29 13:50:52] <UkoeHB_> does anyone have new thoughts on https://github.com/monero-project/monero/issues/6456?
    [2020-04-29 13:51:43] <derpy_bridge> <[keybase] unseddd>: UkoeHB_: unfortunately no, have been consumed elsewhere. many apologies
    [2020-04-29 13:51:44] <sarang> UkoeHB_: I got unexpectedly caught up in other coding, and didn't review in detail yet :/
    [2020-04-29 13:51:45] <Isthmus> Oh! Yeah, I'll look at that by Monday. Hopefullly today
    [2020-04-29 13:51:45] <sarang> my aopologies
    [2020-04-29 13:51:56] <sarang> s/aopologies/apologies
    [2020-04-29 13:51:56] <monerobux> sarang meant to say: my apologies
    [2020-04-29 13:52:11] ⇐ atoc quit (2fb9d2fc@47.185.210.252): Remote host closed the connection
    [2020-04-29 13:52:50] <sarang> All righty, any ACTION ITEMS for the next week to share?
    [2020-04-29 13:52:58] → atoc joined (2fb9d2fc@47.185.210.252)
    [2020-04-29 13:53:48] <sarang> I will be reviewing 6456, reviewing some CLSAG tests, updating some in-memory encryption code, etc.
    [2020-04-29 13:54:03] <Isthmus> I'll probably bump the pq-monero proposal over to CCS by EOW, so shoot me a message (irc or isthmus@getmonero.org works) if you have any suggestions for updates or additions
    [2020-04-29 13:54:03] <UkoeHB_> on a certain level I have nothing else to contribute to the proposal; whether it gets implemented or not is out of my control; keep in mind it likely won't be superseded by anything, so for 'tx extra', 'janus mitigation', 'tx pub keys', and 'view tag', that's the 'final answer' for the forseeable future
    [2020-04-29 13:54:46] <atoc> I'm working on some slides (summary) that details how Grin does their grin-btc atomic swap
    [2020-04-29 13:55:07] <atoc> looking to see if we can get some insight for xmr-btc swaps
    [2020-04-29 13:56:25] <hyc> Iǘe become convinced that itś never in any XMR holders'interest to swap for BTC, due to BTC taint issues
    [2020-04-29 13:57:34] <hyc> but I'd be curious to see how it can work, for future XMR(earth)/XMR(mars) swaps
    [2020-04-29 13:57:40] <derpy_bridge> <[keybase] unseddd>: hyc: even for true DEX scenario?
    [2020-04-29 13:58:09] <derpy_bridge> <[keybase] unseddd>: marsero
    [2020-04-29 13:58:18] <hyc> especially for true DEX, wher eyou can't vet the BTC
    [2020-04-29 13:58:49] <hyc> the benefits are all one-sided, in favor of the BTC seller
    [2020-04-29 13:58:51] <Isthmus> Eh if I've got a wallet full of Monero, but the sandwich shop I'm standing in only takes BTC, I might find that swap useful.
    [2020-04-29 13:59:05] <ArticMine> I have to agree with hyc Selling XMR for BTC on a swap is very dangerous
    [2020-04-29 13:59:06] <derpy_bridge> <[keybase] unseddd>: yeah, i see your point. do you have the same opinion for other swap pairs?
    [2020-04-29 13:59:24] <hyc> if the other pairs also involve transparent coins, yes
    [2020-04-29 13:59:56] <sgp_> +1 concern here
    [2020-04-29 13:59:56] <sarang> Well, in the interest of time (our hour is up), I'll adjourn the meeting for log purposes, but discussion can of course continue


# Action History
- Created by: SarangNoether | 2020-04-27T21:41:49+00:00
- Closed at: 2020-04-29T18:03:39+00:00
