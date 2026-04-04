---
title: 'Research meeting: 24 June 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/477
author: SarangNoether
assignees: []
labels: []
created_at: '2020-06-24T14:54:52+00:00'
updated_at: '2020-06-24T18:08:19+00:00'
type: issue
status: closed
closed_at: '2020-06-24T18:08:19+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 24 June 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-06-24T17:02:14+00:00
Update on quantum audit, here is our preliminary analysis existing vulnerabilities. (Results subject to change as research progresses!)

<img width="799" alt="image" src="https://user-images.githubusercontent.com/21246742/85599849-267ee500-b60a-11ea-819a-07767527a5a9.png">

<img width="1119" alt="image" src="https://user-images.githubusercontent.com/21246742/85599987-48786780-b60a-11ea-89af-11f94be7502c.png">


## SarangNoether | 2020-06-24T18:08:19+00:00
    [2020-06-24 12:59:40] <sarang> First, GREETINGS
    [2020-06-24 12:59:48] <ArticMine> Hi
    [2020-06-24 13:00:25] <I3^RELATIVISM> 0/
    [2020-06-24 13:03:21] <Isthmus> Greetings
    [2020-06-24 13:03:57] <sarang> All right, on to ROUNDTABLE, where anyone is welcome to share research of interest
    [2020-06-24 13:04:03] <sarang> Who would like to go first?
    [2020-06-24 13:05:30] <sarang> Isthmus:?
    [2020-06-24 13:05:38] <Isthmus> Heyo
    [2020-06-24 13:05:46] <Isthmus> Update on quantum audit, here is our preliminary analysis existing vulnerabilities. (Results subject to change as research progresses!)
    [2020-06-24 13:05:52] <Isthmus> https://usercontent.irccloud-cdn.com/file/RKKVcmGZ/image.png
    [2020-06-24 13:06:02] <Isthmus> https://usercontent.irccloud-cdn.com/file/ZPskux3i/image.png
    [2020-06-24 13:06:53] <Isthmus> It's kind of a mixed bag, tbh.
    [2020-06-24 13:07:04] <sarang> To be expected, I suppose
    [2020-06-24 13:07:09] <sarang> There are many components of interest
    [2020-06-24 13:07:09] <Isthmus> Our reliance on DLP is the biggest weak spot right, as expected
    [2020-06-24 13:07:13] <sarang> ya
    [2020-06-24 13:08:12] <Isthmus> That's all on that, any Q's?
    [2020-06-24 13:08:14] <sarang> By "ring signatures" I assume you mean a quantum adversary identifying signing indices via key images?
    [2020-06-24 13:08:36] → TheoStorm joined (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl)
    [2020-06-24 13:08:41] <Isthmus> Yea (or via any mechanism)
    [2020-06-24 13:08:48] <Isthmus> Oh, one thing that we started wondering about
    [2020-06-24 13:09:23] <Isthmus> If you're creating a multisig transactions and one of the signers has a quantum computer, can they gain any extra information about their co-signers
    [2020-06-24 13:10:26] <sarang> Well, you can just derive the whole private key
    [2020-06-24 13:10:37] <sarang> if that's what you mean
    [2020-06-24 13:11:34] <Isthmus> Yea. I need to sit down with ZtM2 to figure out what's passed around, and what should be unknown, just crossed my mind yesterdy
    [2020-06-24 13:12:03] <sarang> That's a good point
    [2020-06-24 13:12:04] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Remote host closed the connection
    [2020-06-24 13:12:19] <sarang> I don't think anyone had specifically mentioned the multisig process during the planning stages of your analysis
    [2020-06-24 13:14:01] <Isthmus> Yea, we just added it. Will probably realize 1 or 2 more aspects to check throughout the next few weeks
    [2020-06-24 13:14:06] <Isthmus> Keep dropping us your ideas :- )
    [2020-06-24 13:14:18] <sarang> Are there particular assumptions made about whether or not the adversary has a public key already?
    [2020-06-24 13:14:35] <sarang> e.g. the adversary suspects a particular address as a destination
    [2020-06-24 13:15:11] <Isthmus> I'm assuming that the adversary is a co-signer on the multisig transaction. They would know the public key with or without a quantum computer, right?
    [2020-06-24 13:15:29] <Isthmus> [erm, well we can consider the adversary both ways, this is just what I had been wondering about yesterday]
    [2020-06-24 13:15:34] <sarang> I mean in general, sorry
    [2020-06-24 13:15:37] <sarang> Not specific to multisig
    [2020-06-24 13:16:32] <Isthmus> Ah yea, quantum computer with your public key and quantum computer without your public key are two adversary models that are considered separately.
    [2020-06-24 13:16:38] <Isthmus> Though TBH the first one is pretty (sadly) easy
    [2020-06-24 13:16:51] <Isthmus> Public key --> [shor's algorithm] --> private key --> init wallet --> game over
    [2020-06-24 13:18:02] <sgp_> sorry I'm late
    [2020-06-24 13:18:04] <sarang> And not even "your" public key
    [2020-06-24 13:18:10] <sarang> But just looking at a given transcation on chain
    [2020-06-24 13:18:18] ⇐ febrezo[m] quit (febrezomat@gateway/shell/matrix.org/x-nmwuqdhiryoaaaqy): Quit: authenticating
    [2020-06-24 13:18:24] → febrezo[m] joined (febrezomat@gateway/shell/matrix.org/x-rbuouyikyggzymnb)
    [2020-06-24 13:18:29] <sarang> If the adversary's goal is to identify as much as possible about keys, addresses, etc.
    [2020-06-24 13:18:43] <sarang> Sending wallet address, receiving wallet address, etc.
    [2020-06-24 13:19:42] <Isthmus> Yea, if an outside observer plucks a transaction at random from the blockchain, with no further knowledge, what can they ascertain about 1) the sender, 2) the transaction, 3) the recipient
    [2020-06-24 13:20:36] <sarang> Right. And then what can they learn if they have an idea of possible addresses
    [2020-06-24 13:20:53] <Isthmus> Bingo
    [2020-06-24 13:23:07] <sarang> I assume that there is (or will be) a more specific write-up with details on what relates to this chart?
    [2020-06-24 13:23:22] <UkoeHB_> Earlier I argued you could brute force output amounts if the DLP is broken (assuming recipient address is unknown), however I'll retract that. Output amounts are information-theoretically secure.
    [2020-06-24 13:23:40] <Isthmus> Gotcha
    [2020-06-24 13:23:44] — Isthmus makes a note
    [2020-06-24 13:25:31] <Isthmus> Yeah, this will all be in the research writeup, and more intuitive parts will be included in the general audience writeup
    [2020-06-24 13:25:31] <sarang> Anything else to consider about your analysis at this point Isthmus?
    [2020-06-24 13:25:44] <Isthmus> We were thinking about some medium articles throughout, just for good measure
    [2020-06-24 13:25:56] <Isthmus> Nope, that's all on the quantum end for now
    [2020-06-24 13:26:03] <sarang> OK great!
    [2020-06-24 13:26:11] <Isthmus> I started going down a rabbit hole of subliminal channels this morning, but will save those thoughts for later
    [2020-06-24 13:26:12] <sarang> Did anyone else wish to present research of interest?
    [2020-06-24 13:27:41] <UkoeHB_> This means even if both DLP and hash preimage are broken, there should not be a way to extract the recipient's address from an output.
    [2020-06-24 13:28:20] <Isthmus> That's a huge relief, or else we could recursively apply Shor's algorithm and move forward through the transaction tree breaking everybody's wallets
    [2020-06-24 13:28:33] — Isthmus exhales a big sigh of relief
    [2020-06-24 13:28:59] → thrmo joined (~thrmo@unaffiliated/thrmo)
    [2020-06-24 13:29:46] <sarang> I'll share a few things
    [2020-06-24 13:30:16] <sarang> Here's a time-windowed CDF of spend age: https://usercontent.irccloud-cdn.com/file/5EccXpmE/cdf_window.png
    [2020-06-24 13:30:48] <sarang> Still tracks the gamma distribution pretty well, but there are differences over time (pre-CT)
    [2020-06-24 13:31:49] <sarang> Related to this, I posted my tracing code: https://github.com/SarangNoether/skunkworks/tree/tracing
    [2020-06-24 13:32:09] <sarang> It now supports iterative updates, which may be useful
    [2020-06-24 13:32:25] <sarang> Unrelated to this, I'm still working with the CLSAG auditors
    [2020-06-24 13:32:47] <sarang> I rewrote the proof for Theorem 1 that relates unforgeability to non-slanderability, and it now addresses the auditors' suggestions
    [2020-06-24 13:33:00] <sarang> There are a bunch of other non-security-related updates to it
    [2020-06-24 13:33:27] <sarang> and I'm now in the process of overhauling the linkability anonymity proof to use a better hardness assumption and method, which is a tedious process
    [2020-06-24 13:33:39] <sarang> but I think that will address their comments and be a stronger result
    [2020-06-24 13:34:04] <sarang> The auditors' conclusion is that the construction seems secure, and that the security model seems appropriate to the use case
    [2020-06-24 13:34:35] <sarang> This was the overall goal of the audit; suggestions relating to presentation, formality, etc. are very useful for later submission, but don't appear security-related
    [2020-06-24 13:38:25] <UkoeHB_> Sounds like the audit is moving along well
    [2020-06-24 13:39:01] <sarang> It is! The code review portion has not begun yet, but there are no changes in code to be made as a result of the preprint audit at this point
    [2020-06-24 13:40:33] <sarang> Any questions on these research topics?
    [2020-06-24 13:43:04] <sarang> OK, did anyone else have anything to share before we move on?
    [2020-06-24 13:43:57] <sgp_> nope
    [2020-06-24 13:44:03] <sarang> If not, we can move on to ACTION ITEMS for the coming week
    [2020-06-24 13:44:46] <sarang> I will be finishing up this linkable anonymity overhaul and incorporating it into the preprint, which will complete the updates needed for the auditors
    [2020-06-24 13:45:31] <sarang> Once that's done, I'll get the preprint in a submittable state
    [2020-06-24 13:45:40] <sarang> Anyone else?
    [2020-06-24 13:47:02] <sgp_> I'll be opening a GitHub issue for segregating coinbase outputs into coinbase-only rings
    [2020-06-24 13:48:30] <sarang> It's a good time to discuss this, with an upcoming network upgrade for CLSAG at some point
    [2020-06-24 13:48:38] <sgp_> yeah I think so too
    [2020-06-24 13:48:39] <sarang> especially given the spend-age data
    [2020-06-24 13:49:01] <sarang> I'd still love to see the corresponding data for bitcoin
    [2020-06-24 13:49:06] <sarang> but I don't have that dataset
    [2020-06-24 13:49:39] <sarang> all the Monero data is necessarily pre-CT because of deducibility
    [2020-06-24 13:49:58] <sarang> and any post-CT deducible data spends old funds and is therefore basically useless for those kinds of distributions
    [2020-06-24 13:50:29] <sgp_> I've been pretty clear that I think this BTC data would be nice but isn't necessary to make this change
    [2020-06-24 13:51:15] <sarang> understood
    [2020-06-24 13:52:12] <sarang> OK, anything else before we adjourn?
    [2020-06-24 13:52:14] <UkoeHB_> Isthmus I have to walk back my walkback (sorry for the interruption sarang). You can definitely brute force it if the DLP and hash preimage are broken. Information-theoretic security means nothing in the face of brute forcing all possibilities (64 bits worth). You'd 1) get the DLP of generator H and the commitment C, 2) pick an amount, 3) compute the possible derivation to scalar, 4) get its hash preimage,
    [2020-06-24 13:52:14] <UkoeHB_> 4a) use the key sequence of bits from the preimage to test the encoded amount and only continue if it matches the guessed amount (very unlikely to match if the guessed amount isn't correct) 5) use the key sequence of bits from the preimage to compute the one time address derivation to scalar, 6) subtract it from the one time address private key to get the nominal private spend key, 7) get the DLP of the
    [2020-06-24 13:52:14] <UkoeHB_> preimage key with respect to the tx pub key to get the nominal private view key, 8) test if the spend key can produce the view key directly (normal address) or if any reasonable sub address index can be used to extract a spend key that produces the view key,  9) repeat 2-8 until you get a match (step 4a will probably catch most mistaken guesses). Let's blame this  mishap on a stray synapse.
    [2020-06-24 13:53:38] <sarang> hmm
    [2020-06-24 13:54:43] <Isthmus> ohhhhhh
    [2020-06-24 13:55:07] <sarang> IIRC preimage on keccak is something like O(2^100) or so
    [2020-06-24 13:55:38] <sarang> but I'd have to check on that
    [2020-06-24 13:55:43] — Isthmus takes notes
    [2020-06-24 13:55:49] <Isthmus> Unrelated: Does ZtM2 talk about variable types or just math? Trying to figure out if fees are uint64 or what
    [2020-06-24 13:56:24] <UkoeHB_> They are varints, which I mention in section 6.3 footnote iirc
    [2020-06-24 13:56:34] <Isthmus> Ah, perfect. Thanks!
    [2020-06-24 13:59:51] <sarang> Righto, let's go ahead and adjourn since it's now 18:00 UTC
    [2020-06-24 13:59:56] <sarang> Thanks to everyone for participating!


# Action History
- Created by: SarangNoether | 2020-06-24T14:54:52+00:00
- Closed at: 2020-06-24T18:08:19+00:00
