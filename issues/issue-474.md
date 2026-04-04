---
title: 'Research meeting: 17 June 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/474
author: SarangNoether
assignees: []
labels: []
created_at: '2020-06-17T13:35:30+00:00'
updated_at: '2020-06-17T18:04:17+00:00'
type: issue
status: closed
closed_at: '2020-06-17T18:04:17+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 17 June 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-06-17T17:03:14+00:00
<img width="1051" alt="Screen Shot 2020-06-16 at 5 27 23 PM" src="https://user-images.githubusercontent.com/21246742/84927452-1b680a00-b08a-11ea-9b8a-12b0e89f44e8.png">


## SarangNoether | 2020-06-17T18:04:17+00:00
    [2020-06-17 13:00:11] <sarang> Let's start with GREETINGS
    [2020-06-17 13:00:13] <sarang> Hello!
    [2020-06-17 13:00:52] <h4sh3d[m]> Hi
    [2020-06-17 13:01:54] <Isthmus_> Greetings_
    [2020-06-17 13:03:06] <sgp_> hello
    [2020-06-17 13:03:16] <ArticMine> Hi
    [2020-06-17 13:03:51] <sarang> Righto, on to ROUNDTABLE, where anyone is welcome to share research of interest
    [2020-06-17 13:04:11] <sarang> Isthmus_: noticed you just added to the agenda; care to go first?
    [2020-06-17 13:06:26] <sarang> If Isthmus_ isn't quite ready, I can share a few things
    [2020-06-17 13:06:35] <Isthmus_> Ah come back to me in 5
    [2020-06-17 13:06:41] <Isthmus_> juggling something else real quick
    [2020-06-17 13:06:45] <sarang> I've done some further analysis on transaction tracing
    [2020-06-17 13:06:54] <sarang> I'll post a few plots of interest here... one sec
    [2020-06-17 13:07:29] <sarang> All transactions, by date and type: https://usercontent.irccloud-cdn.com/file/Pqx68K2E/all.png
    [2020-06-17 13:07:56] <sgp_> I like hidden, transition, denominated
    [2020-06-17 13:07:57] <sarang> The same data, scaled: https://usercontent.irccloud-cdn.com/file/Cm4J3FRc/all-scaled.png
    [2020-06-17 13:08:42] <sarang> Deducible transactions, by date and type (same scale as first plot): https://usercontent.irccloud-cdn.com/file/rcPhKQZ4/deducible.png
    [2020-06-17 13:08:55] <sarang> Note that "deducible" means "at least input deducible" for this analysis
    [2020-06-17 13:09:42] <sarang> From the deducible transactions, I ran spend age distributions and further categorized by coinbase and non-coinbase
    [2020-06-17 13:09:55] <sgp_> "at least 1 input deducible"
    [2020-06-17 13:10:02] <sarang> The CDF of this distribution: https://usercontent.irccloud-cdn.com/file/teVxZrIe/cdf.png
    [2020-06-17 13:10:15] <sarang> s/input deducible/1 input deducible/
    [2020-06-17 13:10:15] <monerobux> sarang meant to say: Note that "deducible" means "at least 1 input deducible" for this analysis
    [2020-06-17 13:10:18] <sarang> thanks sgp_ 
    [2020-06-17 13:10:41] <sarang> That CDF plot also includes the gamma distribution used for output selection, and first examined in the Miller et al. paper
    [2020-06-17 13:11:03] <sgp_> yup, for transactions with multiple inputs rings (to the observer, sarang obviously knows this)
    [2020-06-17 13:11:18] <sarang> Notably, coinbase outputs have an essentially identically spend-age distribution to non-coinbase outputs
    [2020-06-17 13:11:29] <sarang> We didn't previously know if/how they might differ
    [2020-06-17 13:11:55] <sarang> A big disclaimer is that _zero_ "hidden"-type transactions are deducible, and don't factor in to this data at all
    [2020-06-17 13:12:08] <sarang> We have _no_ hidden-type transactions to use as a direct ground-truth dataset for this
    [2020-06-17 13:12:12] <sarang> Which is a good thing!
    [2020-06-17 13:13:17] <sarang> The fraction of all transactions (non-cumulative) that have at least one deducible input: https://usercontent.irccloud-cdn.com/file/jiDfKje2/proportion.png
    [2020-06-17 13:13:26] <sgp_> I'm astonished they are so similar tbh
    [2020-06-17 13:13:33] <sarang> One guess as to when the CT crossover happened...
    [2020-06-17 13:13:40] <sgp_> lol
    [2020-06-17 13:14:10] <sarang> UkoeHB_ had asked before the meeting about if/how this distribution changes over the time period of the dataset, which is data I'm presently running and should have later today
    [2020-06-17 13:14:54] <sarang> But at the very least, this is useful since it both shows that the Miller distribution is reasonable, as well as suggests that coinbase outputs do not require any particular special treatment from a spend-age perspective
    [2020-06-17 13:15:07] <sarang> This is not to say that's the only factor in selection
    [2020-06-17 13:15:15] <sarang> but it is one factor that we previously had no data for
    [2020-06-17 13:16:03] <sgp_> but it gives me initial confidence that we should separate the ring types and shouldn't make the selection of a particular different selection algorithm a showstopper
    [2020-06-17 13:17:06] <sarang> I'm also updating a writeup that includes scripts and instructions for how to run this data yourself
    [2020-06-17 13:17:10] <sgp_> BTC data would obviously be nice to confirm since it's more recent
    [2020-06-17 13:17:21] <sarang> as well as supporting incremental updates, to make it straightforward to produce these plots over time in a consistent way
    [2020-06-17 13:17:43] <sarang> I strongly encourage folks to review these scripts once posted and/or run them yourself to verify my conclusions
    [2020-06-17 13:17:56] <sgp_> as will the over time data UkoeHB_ suggested, in the case that Monero coinbase outputs were spent later than average in its early history, for example
    [2020-06-17 13:18:47] <sarang> Unfortunately I don't have the proper setup to run the BTC data
    [2020-06-17 13:19:02] <sarang> I will of course have the time-based Monero data
    [2020-06-17 13:19:21] <sarang> it just takes time to run the deducibility analysis
    [2020-06-17 13:19:44] <sgp_> how will you graph time-based? the average number of blocks after the generation of a coinbase output before it's spent?
    [2020-06-17 13:19:55] <sarang> I'll pull some windows within the dataset and overlay them
    [2020-06-17 13:20:13] <sarang> Using the spend transaction as the target for the window
    [2020-06-17 13:20:21] <sarang> Ages are always relative to the spend transaction
    [2020-06-17 13:20:51] <sarang> This should make it straightforward to see any substantive changes
    [2020-06-17 13:21:24] <sgp_> okay, I'll let you know later if I have concerns or am confused
    [2020-06-17 13:21:26] <sarang> Aside from this, the CLSAG audit by JP Aumasson and his colleague Antony Vennard is continuing
    [2020-06-17 13:21:49] <sarang> That's what I wanted to share today; were there other questions on any of this, before I pass the baton to Isthmus_ or others?
    [2020-06-17 13:22:49] <sarang> Isthmus_: ready to go?
    [2020-06-17 13:22:55] <Isthmus_> Sure
    [2020-06-17 13:22:59] <sarang> Have at it!
    [2020-06-17 13:23:01] <Isthmus_> Here’s our first draft of the audit framework for post-quantum security. Thoughts on mechanisms or algorithms to add?
    [2020-06-17 13:23:07] <Isthmus_> https://usercontent.irccloud-cdn.com/file/mRxqUX65/image.png
    [2020-06-17 13:23:17] <sarang> This is the same image as posted to the agenda?
    [2020-06-17 13:23:30] <sarang> How are you defining the concern types?
    [2020-06-17 13:23:36] <Isthmus_> TL;DR of image is:
    [2020-06-17 13:23:41] <Isthmus_> Adversary definition: {Shor's Algorithm, Grover's algorithm, Fourier Fishing/Checking, Simon's Algorithm, Deutsch–Jozsa algorithm, Bernstein–Vazirani algorithm (Hidden Linear Function Problem), Possibly vulnerable to a future method employed by a Quantum Computer but lacking any known algorithm}
    [2020-06-17 13:23:45] <Isthmus_> Attack surface: {Ring Signatures, RingCT, One-time "Stealth" Addresses, Pubkey derivation, Forge amounts?, Bulletproofs, RandomX proof-of-work, Block / Transaction hashing, PRNG, Fiat-Shamir Transform, Schnorr Signature, ??}
    [2020-06-17 13:24:27] <Isthmus_> Anything jump out that we're missing?
    [2020-06-17 13:24:46] → Dean_Guss joined (~dean@gateway/tor-sasl/deanguss)
    [2020-06-17 13:24:58] ⇐ DeanWeen quit (~dean@gateway/tor-sasl/deanguss): Remote host closed the connection
    [2020-06-17 13:25:09] <sarang> Does the secrecy/privacy of amount commitments fall under RingCT?
    [2020-06-17 13:25:16] <sarang> "RingCT" can be interpreted broadly
    [2020-06-17 13:25:18] <sarang> or not broadly
    [2020-06-17 13:25:42] <Isthmus_> Yea, you could label it either way
    [2020-06-17 13:25:50] <Isthmus_> The questions are essentially 1) forgery, 2) unmasking amounts
    [2020-06-17 13:25:55] <sarang> Perhaps payment IDs could be added as well, since they're intended to be private
    [2020-06-17 13:26:02] <Isthmus_> Oh yea!
    [2020-06-17 13:26:16] <sarang> Also: how are you defining the "concern" types on the chart?
    [2020-06-17 13:26:57] <moneromooo> keccak, (our particular usage of) chacha20
    [2020-06-17 13:27:04] <Isthmus_> Oh, those "concerns" are just our research notes to each other. Not formally part of the table
    [2020-06-17 13:27:14] — Isthmus_ makes note of that
    [2020-06-17 13:27:33] <sarang> Isthmus_: related to mooo's notes... are you concerning yourself with only on-chain stuff, or local stuff too?
    [2020-06-17 13:27:56] <sarang> e.g. is local wallet encryption out of scope
    [2020-06-17 13:28:21] <moneromooo> sarang may want to add any new crypto primitive from triptych ?
    [2020-06-17 13:28:54] <sarang> I'd certainly welcome Triptych proof analysis from that
    [2020-06-17 13:29:00] <sarang> since it's heavily DL based
    [2020-06-17 13:29:20] <gingeropolous> ^^
    [2020-06-17 13:29:21] <sarang> "all DL stuff is toast" :/
    [2020-06-17 13:29:26] <Isthmus_> RE on-chain vs local: Hmm, I had only been considering the on-chain stuff until now, but we could also glance at local :- )
    [2020-06-17 13:29:36] <sarang> I think the local stuff depends on the threat model
    [2020-06-17 13:29:37] <Isthmus_> My #1 priority is attack vectors that enable retroactive deanonymization
    [2020-06-17 13:29:46] <Isthmus_> Which would mostly be on-chain stuff
    [2020-06-17 13:29:47] <sarang> If someone gets on your machine, you have bigger worries
    [2020-06-17 13:31:14] <Isthmus_> If you have ideas for local security mechanisms to check (e.g. local encryption) feel free to let me know and I'll add them to the list
    [2020-06-17 13:31:20] <h4sh3d[m]> Pubkey derivation is very general and is used in other feature/mech as a primitive, or is it more like account and subaddress?
    [2020-06-17 13:31:33] <Isthmus_> Right now it looks like the biggest fundamental issue is that an adversary leveraging Shor’s algorithm can find private keys based on public keys. This means that if you give your public address to somebody, they could create a wallet with your private key and scan your entire account history (circumventing almost all privacy)
    [2020-06-17 13:31:34] <sarang> Yeah I also wondered what that term means
    [2020-06-17 13:31:42] <UkoeHB_> sounds like diffie-hellman
    [2020-06-17 13:31:49] <moneromooo> The proposed recipient encrypted data scheme in the rpd branch uses chacha20 fwiw.
    [2020-06-17 13:31:57] <sarang> :D
    [2020-06-17 13:32:02] <moneromooo> So neither keccak nor this are local only.
    [2020-06-17 13:32:06] <sarang> excellen
    [2020-06-17 13:32:15] <sarang> s/excellen/excellent
    [2020-06-17 13:32:16] <monerobux> sarang meant to say: excellent
    [2020-06-17 13:32:18] <sarang> good bot
    [2020-06-17 13:32:31] <sarang> I'm really looking forward to the results of this analysis
    [2020-06-17 13:32:39] <Isthmus_> Primary key to private key should be breakfast for Shor's algorithm
    [2020-06-17 13:32:46] <Isthmus_> Will also look at subaddresses, etc
    [2020-06-17 13:32:47] <sarang> Isthmus_: do you know of other projects doing this kind of in-depth work? just curious
    [2020-06-17 13:33:23] <sarang> I expect an unfortunate whirlwind of "Monero is not quantum-safe! Run for it!" from this =p
    [2020-06-17 13:33:48] <sarang> But having a solid picture of the protocol relative to a hypothetical quantum adversary will be fascinating
    [2020-06-17 13:33:55] <Isthmus_> Haha, yea we're going to add a lot of "this also applies to Bitcoin, Zcash, and anything else in your portfolio" disclaimers
    [2020-06-17 13:34:05] <Isthmus_> The big question for me is whether stealth addresses are secure. If there’s a way to go from stealth addresses to private keys, we’re all toast.
    [2020-06-17 13:34:20] <Isthmus_> As opposed to only toast if you've given somebody else your address
    [2020-06-17 13:35:26] <sarang> Isthmus_: is there anything you need from this group to assist with your current work on this?
    [2020-06-17 13:35:33] <Isthmus_> Can I ask a silly question?
    [2020-06-17 13:35:36] <sarang> sure
    [2020-06-17 13:35:57] <Isthmus_> If I send sarang a transaction, and then erase my computer, and restore from seed, will I be able to recover your address from the on-chain transaction?
    [2020-06-17 13:36:18] <sarang> Not without external information
    [2020-06-17 13:36:22] <Isthmus_> *PHEW*
    [2020-06-17 13:36:28] <Isthmus_> Okay, otherwise things were going to get scary recursive real fast
    [2020-06-17 13:36:34] <sarang> There have been ideas from time to time to encode this for precisely this reason
    [2020-06-17 13:36:48] <sarang> and you can do this in extra yourself, I suppose
    [2020-06-17 13:37:09] <Isthmus_> It would be bad from this perspective, since if I get pubkeyA, then I derive privkeyA
    [2020-06-17 13:37:17] <sarang> It would
    [2020-06-17 13:37:38] <sarang> and it's certainly a design tradeoff, regardless of quantum considerations
    [2020-06-17 13:38:00] <Isthmus_> Cool, that's all I have for today.
    [2020-06-17 13:38:06] <sarang> Thanks Isthmus_ !
    [2020-06-17 13:38:12] <sarang> Looking forward to future updates for this project
    [2020-06-17 13:38:17] <sarang> Were there other questions for Isthmus_?
    [2020-06-17 13:38:46] <tevador> I think that the likely conclusion is that a quantum adversary would be able to steal everyone's funds, but would not be able to link payments unless they also know your address
    [2020-06-17 13:39:08] <luigi1111w> the "privacy" of stealth addresses shouldn't be obviously compromised by QC, but other far more catastrophic things would be
    [2020-06-17 13:40:10] <sarang> I am personally interested to see how the conclusions from this project compare to the risks of other protocols
    [2020-06-17 13:40:10] <Isthmus_> Yea, I think we're going to look closely at QRL and quantum cryptocash for inspiration to address these fundamental issues first
    [2020-06-17 13:40:21] <luigi1111w> you can't link blockchain to unknown address but you could link known addresses
    [2020-06-17 13:40:24] <sarang> That is, does the Monero protocol do better, worse, or about the same as other protocols with similar goals
    [2020-06-17 13:40:43] <sarang> luigi1111w: AFAIK this is also what Zcash has concluded about their quantum resistance
    [2020-06-17 13:40:50] <sarang> (as a comparison)
    [2020-06-17 13:41:09] <Isthmus_> "you can't link blockchain to unknown address but you could link known addresses" < could you elaborate slightly?
    [2020-06-17 13:41:32] <luigi1111w> given a particular address you could determine if it matches an output
    [2020-06-17 13:41:45] <luigi1111w> but you couldn't derive that address from the output
    [2020-06-17 13:41:58] <Isthmus_> Ah, gotcha
    [2020-06-17 13:42:05] <Isthmus_> When you say "matches an output" do you mean created an output or received an output
    [2020-06-17 13:42:16] <luigi1111w> received
    [2020-06-17 13:42:33] <luigi1111w> although by extension also created because untraceability is compromised
    [2020-06-17 13:42:48] <Isthmus_> Yep, that makes sense and matches our preliminary thining
    [2020-06-17 13:42:56] <Isthmus_> s/ini/inki
    [2020-06-17 13:42:56] <monerobux> Isthmus_ meant to say: Yep, that makes sense and matches our preliminary thinking
    [2020-06-17 13:45:09] <sarang> OK, did anyone else wish to share research of general interest to this group?
    [2020-06-17 13:45:33] <h4sh3d[m]> Yesterday I published an updated version of the swap
    [2020-06-17 13:45:36] <h4sh3d[m]> https://github.com/h4sh3d/xmr-btc-atomic-swap/blob/dl-proof/whitepaper/xmr-btc.pdf
    [2020-06-17 13:46:02] <sarang> Nice!
    [2020-06-17 13:46:07] <sarang> Anything in particular to comment on it here?
    [2020-06-17 13:46:37] <h4sh3d[m]> I corrected the one-time VES usage, and I confirm that it is now correct ; )
    [2020-06-17 13:46:51] <sarang> noted
    [2020-06-17 13:47:25] <sarang> thanks h4sh3d[m]
    [2020-06-17 13:47:44] <h4sh3d[m]> I'll add more details in the paper in the next days but the protocol is done
    [2020-06-17 13:47:55] <sarang> Before moving on, are there any other general questions, or other research topics to address today?
    [2020-06-17 13:48:00] <sarang> (from anyone)
    [2020-06-17 13:51:00] <sarang> OK, on to ACTION ITEMS
    [2020-06-17 13:51:30] <sarang> I'll get my analysis toolset updated and posted, as well as finalize that time-windowed spend-age distribution data and provide it on this channel
    [2020-06-17 13:51:42] <sarang> And continue working with the CLSAG audit team
    [2020-06-17 13:52:00] <sarang> I had to set aside the output merging algorithm design, but will return to it
    [2020-06-17 13:52:09] <sarang> Anyone else have action items they care to share?
    [2020-06-17 13:53:47] <sgp_> I want some confirmation that we think coinbase-only rings make sense for the CLSAG update specifically
    [2020-06-17 13:55:24] <sarang> What data will/do you use to make this assessment?
    [2020-06-17 13:55:51] <sgp_> obviously I support this as-is, even without more coinbase vs non-coinbase data
    [2020-06-17 13:56:47] <sarang> noted
    [2020-06-17 13:57:03] <sarang> Is there particular data you think would help assess this, that we currently do not have?
    [2020-06-17 13:57:19] <sgp_> I see it as an incremental improvement either way, even more so if we can adjust to fit a different selection algo for each
    [2020-06-17 13:57:50] <sarang> Such an algorithm likely wouldn't need to separately account for spend age, as we now know
    [2020-06-17 13:58:23] <sgp_> makes implementation even easier then
    [2020-06-17 13:59:00] <sarang> All right, our hour is just about up
    [2020-06-17 13:59:10] <sarang> Are there any last questions or comments before we adjourn?
    [2020-06-17 13:59:13] <Isthmus_> I have a minimum-age aglorithm on a whiteboard that might help with this
    [2020-06-17 13:59:20] <Isthmus_> but haven't ported over to data queries yet
    [2020-06-17 13:59:21] <sarang> What do you mean Isthmus_?
    [2020-06-17 14:00:30] <Isthmus_> Every single monero output has a minimum plausible age. If you follow up the transaction tree far enough, you'll always encounter coinbases.
    [2020-06-17 14:00:46] <Isthmus_> So I can point at any output and say, "it is no younger that N hops from this coinbase"
    [2020-06-17 14:01:10] <sarang> Ah, got it
    [2020-06-17 14:01:12] <Isthmus_> Ah I'm late for another meeting crap
    [2020-06-17 14:01:13] <Isthmus_> g2g
    [2020-06-17 14:01:16] — Isthmus_ bolts to a zoom room
    [2020-06-17 14:01:17] <sarang> Yeah, would love to see what you come up with
    [2020-06-17 14:01:24] <sarang> OK, I suppose we can adjourn
    [2020-06-17 14:01:32] <sarang> Thanks to everyone for joining in!

# Action History
- Created by: SarangNoether | 2020-06-17T13:35:30+00:00
- Closed at: 2020-06-17T18:04:17+00:00
