---
title: 'Research meeting: 30 September 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/395
author: SarangNoether
assignees: []
labels: []
created_at: '2019-09-26T17:50:20+00:00'
updated_at: '2019-09-30T18:01:09+00:00'
type: issue
status: closed
closed_at: '2019-09-30T18:01:09+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 30 September 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [CLSAG](https://eprint.iacr.org/2019/654) revised/submitted, [Lelantus](https://eprint.iacr.org/2019/373) proof modifications, [RCT3](https://eprint.iacr.org/2019/508) proof-of-concept, [monthly report](https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/77#note_7393)
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-09-30T18:01:09+00:00
    [2019-09-30 13:00:39] <sarang> GREETINGS
    [2019-09-30 13:00:43] <mikerah> Hello
    [2019-09-30 13:00:55] <silur> hi
    [2019-09-30 13:01:25] <gingeropolous> hewro
    [2019-09-30 13:01:27] <sarang> Is suraeNoether here?
    [2019-09-30 13:01:32] <suraeNoether> howdy
    [2019-09-30 13:01:42] <suraeNoether> hi, sorry, i'm going to be in and out this morning
    [2019-09-30 13:01:49] <kinghat> o/
    [2019-09-30 13:01:50] <sarang> ok
    [2019-09-30 13:01:56] <suraeNoether> i can do a real quick rundown, but i have to go :(
    [2019-09-30 13:02:07] <charuto> o/
    [2019-09-30 13:02:23] <sarang> In that case, let's jump into the ROUNDTABLE with suraeNoether 
    [2019-09-30 13:02:49] <suraeNoether> okay, so
    [2019-09-30 13:02:51] <suraeNoether> matching
    [2019-09-30 13:03:13] <suraeNoether> i've been working on the code, and there were some structural problems, and then a failure-to-push-my-damn-commits failure of my local harddrive
    [2019-09-30 13:03:29] <suraeNoether> it's proceeding... slowly
    [2019-09-30 13:03:40] <suraeNoether> i've been sick a lot :(
    [2019-09-30 13:03:49] <suraeNoether> other than that, i don't have anything to chat about right now
    [2019-09-30 13:04:00] <sarang> What would you say the current state of matching simulations is?
    [2019-09-30 13:04:04] <suraeNoether> i'm hoping to push some code later today on my simulations
    [2019-09-30 13:04:11] <suraeNoether> non-functional
    [2019-09-30 13:04:12] <sarang> And is there any part of it that could/should be worked on by others as well?
    [2019-09-30 13:04:22] <sarang> Or of the corresponding theory?
    [2019-09-30 13:05:00] <suraeNoether> the paper has been available and the codebase is available. the matching code itself is working, but my method of comparing it to some simulated ledger is what is taking awhile.
    [2019-09-30 13:05:09] <sgp_> I'm here from where Sarang should be :)
    [2019-09-30 13:05:22] <sarang> >_>
    [2019-09-30 13:05:28] <suraeNoether> anyone can choose to simulate a ledger *some other way* and run my code
    [2019-09-30 13:05:33] <sarang> Ah ok, got it
    [2019-09-30 13:05:52] <suraeNoether> we even have speed numbers for our matching code from you
    [2019-09-30 13:06:02] <suraeNoether> literally, it's a sanity check and comparing against known churn behaviors
    [2019-09-30 13:06:23] <sarang> Righto, any questions for suraeNoether before he must go?
    [2019-09-30 13:06:37] <suraeNoether> okay guys i have to go. expect a push later today. i'm also going back on solid food later today so who knows, maybe i'll have some burst of inspiration
    [2019-09-30 13:06:50] <sarang> Feel better plz
    [2019-09-30 13:07:19] <sarang> I've been working on several things this past week
    [2019-09-30 13:07:26] <charuto> may good health and good fortune go your way mr surae
    [2019-09-30 13:07:36] <sarang> First, the CLSAG paper is now submitted to Financial Cryptography 2020
    [2019-09-30 13:07:45] <sarang> The preprints on the MRL archive and on IACR are updated
    [2019-09-30 13:08:04] <sarang> Or rather, IACR has been updated and an MR exists for the MRL archive
    [2019-09-30 13:08:23] <sarang> The DLSAG paper was also updated and submitted to the same conference
    [2019-09-30 13:08:41] <xmrmatterbridge> <sgp_> https://eprint.iacr.org/2019/654
    [2019-09-30 13:09:00] <sarang> Second, I'm still working with the author of Lelantus on some modifications to avoid its linking problem
    [2019-09-30 13:09:24] <sarang> We'll have a short writeup soon about one possible way, but it doesn't work cleanly with one-time addresses in the way you might want it to
    [2019-09-30 13:09:53] <sarang> There are some techniques involving Schnorr proofs that we still want to investigate
    [2019-09-30 13:10:24] <sarang> Third, I am finalizing proof-of-concept code and spacetime analysis for the updated RCT3 preprint, which has interesting tradeoffs from the earlier version
    [2019-09-30 13:10:42] <xmrmatterbridge> <rehrar> exciting!
    [2019-09-30 13:10:50] <silur> is the PoC code available somewhere?
    [2019-09-30 13:10:59] <sarang> Besides fixing a big flaw, it aggregates proofs together... this means very small proofs at the expense of some verification
    [2019-09-30 13:11:22] <sarang> Code (danger: not for production) is here: https://github.com/SarangNoether/skunkworks/tree/rct3/rct3
    [2019-09-30 13:11:40] <silur> thanks
    [2019-09-30 13:11:55] <sarang> I'll also run numbers on doing non-aggregated proofs, since that would effectively reverse the spacetime tradeoff
    [2019-09-30 13:12:00] <hyc> ^ bets on which xmr fork deploys it first ...
    [2019-09-30 13:12:31] <sgp_> What is "some verification"?
    [2019-09-30 13:13:06] <sarang> My initial estimates suggest a drop in size from 3.1 kB to perhaps 2.3 kB (2-in-2-out)
    [2019-09-30 13:13:58] <sarang> Verification numbers TBD, but not too bad... considering the original 2-2 single verification estimate was 39 ms on a test machine, batched down to 13 ms
    [2019-09-30 13:14:50] <sarang> Back-of-the-envelope is that batched 2-2 txns will see maybe 5% increase from the old version's time
    [2019-09-30 13:15:11] <sarang> but again, you save 25% on space from the old version
    [2019-09-30 13:15:27] <sarang> Pulling apart the aggregation will improve batching time by reusing generators
    [2019-09-30 13:15:32] <sarang> but then space is back up again
    [2019-09-30 13:15:53] <sarang> There are also some structural differences to the proofs that will mean somewhat higher times regardless
    [2019-09-30 13:16:03] <sarang> More details once I have the actual numbers finished
    [2019-09-30 13:17:57] <sarang> Fourth, my monthly report is posted here: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/77#note_7393
    [2019-09-30 13:19:58] <sarang> Fifth, I'll be joining rehrar and Daniel Kim to speak at World Crypto Conference later this month
    [2019-09-30 13:20:26] <sarang> My talk is about the history of cryptographic constructions toward privacy-preserving transactions, and future research directions
    [2019-09-30 13:20:37] <sarang> I'm starting it early to meet their particular deadlines
    [2019-09-30 13:20:41] <xmrmatterbridge> <rehrar> woot!
    [2019-09-30 13:20:44] <xmrmatterbridge> <rehrar> WCC represent
    [2019-09-30 13:21:11] <sarang> I'm trying to think of some good analogies for why terms like "privacy coin" set the wrong baseline
    [2019-09-30 13:21:32] <sarang> For example, you wouldn't visit someone's house and say "oh, you have one of those bathrooms with a door"
    [2019-09-30 13:21:37] <sarang> It should be the default!
    [2019-09-30 13:21:37] <mikerah> Try to frame it in terms of cash
    [2019-09-30 13:21:43] <xmrmatterbridge> <sgp_> "This is a safe car"?
    [2019-09-30 13:22:24] <mikerah> Cash is anonymous, debit/credit cards are tracked by your bank
    [2019-09-30 13:22:30] <xmrmatterbridge> <rehrar> the bathroom door is spot on
    [2019-09-30 13:22:43] <sarang> Anyway, the talk is mainly about cryptography, but I like setting the stage briefly to give motivation for the cryptography
    [2019-09-30 13:23:23] <sarang> And I'm a terrible designer, so I always take longer than expected to make presentations look not-too-horrible :/
    [2019-09-30 13:23:34] <xmrmatterbridge> <rehrar> sarang, bro just send to me?
    [2019-09-30 13:23:45] <sarang> in all its TeX goodness :)
    [2019-09-30 13:23:50] <xmrmatterbridge> <sgp_> your plain presentations are ok imo
    [2019-09-30 13:24:00] <xmrmatterbridge> <rehrar> test, is MM working in this room?
    [2019-09-30 13:24:05] <sarang> hi rehrar
    [2019-09-30 13:24:12] <xmrmatterbridge> <rehrar> bloof
    [2019-09-30 13:24:25] <sarang> So yeah, that's what I've been working on
    [2019-09-30 13:24:30] <sarang> Any particular questions on those items?
    [2019-09-30 13:24:35] <xmrmatterbridge> <serhack> In my opinion, this should depend on audience sarang
    [2019-09-30 13:24:37] <xmrmatterbridge> <rehrar> nah
    [2019-09-30 13:24:44] <sarang> serhack: how so?
    [2019-09-30 13:24:51] <sarang> It's an audience of developers
    [2019-09-30 13:25:05] <xmrmatterbridge> <rehrar> though I have a Research Request (tm) for MRL as a whole
    [2019-09-30 13:25:15] <silur> I'm so missing an audience of developers :D
    [2019-09-30 13:25:15] <sarang> rehrar: go on
    [2019-09-30 13:25:37] <xmrmatterbridge> <sgp_> I have a point to mention after
    [2019-09-30 13:25:44] <sarang> ok
    [2019-09-30 13:25:44] <xmrmatterbridge> <rehrar> It's be asked before with varying degrees of intensity, but I'd like some research done on the 10 confirmation unlock time.
    [2019-09-30 13:26:06] <xmrmatterbridge> <rehrar> 10 confs was kinda chosen arbitrarily? Or did it have reasoning? Research on if this is the ideal number.
    [2019-09-30 13:26:24] <dEBRUYNE> sarang: Have there been any noteworthy developments regarding the CLSAG audits?
    [2019-09-30 13:26:26] <sarang> I see that as really being a question of network topology and propagation, as it relates to reorgs
    [2019-09-30 13:26:28] <xmrmatterbridge> <rehrar> Obviously the hope is to get the conf time down for spendable funds, but if research shows 10 is good (or even increase), well at least we have numbers to back it up
    [2019-09-30 13:26:47] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-yennnpliwhfuevyi): Quit: Connection closed for inactivity
    [2019-09-30 13:26:47] <sarang> I don't have particular data on this... best candidates for that are the noncesense folks
    [2019-09-30 13:27:25] <sarang> dEBRUYNE: OSTIF is working to get the first code audit number (24750 USD) down
    [2019-09-30 13:27:38] <sarang> the math audit number is currently 7200 USD
    [2019-09-30 13:28:07] <dEBRUYNE> OK
    [2019-09-30 13:28:12] <dEBRUYNE> Do we have only one offer for a code audit btw?
    [2019-09-30 13:28:20] <xmrmatterbridge> <serhack> sarang: probably you know this suggestion but I will never tire of repeating it. You have to capture attention of people, in any possible way. So, if you think the presentation graphic could be changed to improve the readability, go for it. If you think you have to remove text and to add more images, go for it.
    [2019-09-30 13:29:06] <nioc> rehrar if you reduce the time to 5 minutes won't you just get questions like,  why I need to wait 5 minutes?
    [2019-09-30 13:30:24] <sarang> AFAIK there is only the single code audit offer right now, but OSTIF is working on this
    [2019-09-30 13:31:18] <sarang> Both to allow the possibility of multiple reviews (if desired) and to promote competition that could reduce the cost of each review
    [2019-09-30 13:34:24] <xmrmatterbridge> <sgp_> This isn't high priority, but I'd like to see an analysis of the number of coinbase outputs in rings on average over time
    [2019-09-30 13:36:34] <sarang> Ah, over the different selection algorithms?
    [2019-09-30 13:37:24] <sarang> I agree that it would be interesting. I ran some numbers on super small datasets and it was a spread that maxed at 1-in-11 IIRC
    [2019-09-30 13:38:01] <sarang> There is always the question of whether a consensus rule of "any ring w/ coinbase must be all coinbase" would be a net benefit
    [2019-09-30 13:38:29] <sarang> I still hold that it shifts the resulting heuristic down the transaction graph one hop, but overall it's probably not a bad idea
    [2019-09-30 13:39:36] ⇐ rex4539 quit (~rex4539@balticom-197-78.balticom.lv): Quit: rex4539
    [2019-09-30 13:40:55] <xmrmatterbridge> <sgp_> You know my view is that it's a net positive, but most people don't agree yet
    [2019-09-30 13:42:04] <silur> I don't get the assumptions itself, aren't coinbases in rings can be used as inputs to any other tx?
    [2019-09-30 13:42:36] <silur> won't making "any ring with coinbase must be all coinbase" that property nonexistent?
    [2019-09-30 13:42:56] <sarang> One claim is that coinbase can be excluded as the true spend for "average transactiosn"
    [2019-09-30 13:43:14] <sarang> as well as questions of pool behavior
    [2019-09-30 13:43:45] <sarang> Prior to the last selection change, coinbase were being overselected as part of a broader weighting issue
    [2019-09-30 13:44:12] <sarang> Now they're selected according to their on-chain frequency, but are otherwise not selected differently
    [2019-09-30 13:45:03] <sarang> Of course, making all-coinbase rings means that you could now identify the outputs of those transactions as heuristically not true spenders where they are used
    [2019-09-30 13:45:46] <silur> on firsth thought that doesn't seem too much of a practical privacy leak
    [2019-09-30 13:46:25] <sarang> It was not good when they were being overselected, but in fact the over/underselection was technically occurring for all selection regions where block density was varied
    [2019-09-30 13:46:37] <sarang> It was just that coinbase were far more visible as an effect of this
    [2019-09-30 13:46:38] <silur> I see
    [2019-09-30 13:47:17] <sarang> So right now you'll usually see 0-1 coinbase or so per ring, but there are certainly outliers with more
    [2019-09-30 13:48:27] <sarang> Anyway, certainly something to keep thinking about. As with most things, it's probably a bit more subtle than it seems at first glance
    [2019-09-30 13:48:42] <sarang> Back to the agenda... did anyone else have research to share?
    [2019-09-30 13:48:47] <sarang> Or other questions?
    [2019-09-30 13:50:10] <sarang> Right, then on to ACTION ITEMS
    [2019-09-30 13:50:12] <mikerah> I have some questions related to what was discussed last week
    [2019-09-30 13:50:22] <sarang> sure mikerah 
    [2019-09-30 13:50:24] <sarang> go ahead
    [2019-09-30 13:50:48] <mikerah> Have you considered using Polynomial commitments
    [2019-09-30 13:51:02] <sarang> For what?
    [2019-09-30 13:51:23] <mikerah> In order to get a SNARK without trusted setup for ring signatures
    [2019-09-30 13:51:44] <sarang> How so?
    [2019-09-30 13:51:55] <mikerah> Current schemes that are coming out are using polynomial commitments in such a way that you can eliminate the need for a trusted setup
    [2019-09-30 13:52:04] <mikerah> Halo and DARKs come to mine.
    [2019-09-30 13:52:37] <silur> afaik those are more generic schemes than what's needed in practice here
    [2019-09-30 13:52:39] <sarang> Well, Halo's big goal is recursive evaluation
    [2019-09-30 13:52:50] <mikerah> These schemes aren't quantum secure and you get larger proof verification sizes as usual
    [2019-09-30 13:52:52] <sarang> and it's not even close in terms of desired efficiency yet; early stages
    [2019-09-30 13:53:18] <kenshamir[m]> <mikerah "Halo and DARKs come to mine."> DARKs can be used, but the polynomial commitment scheme in Halo cannot from what I’ve read and tried
    [2019-09-30 13:53:19] <mikerah> isn't halo's big goal recursive composition + no trusted setup
    [2019-09-30 13:53:33] <sarang> yes
    [2019-09-30 13:53:35] <silur> mikerah: quantum secure schemes have even larger proofs
    [2019-09-30 13:53:52] <silur> usually 2kb+
    [2019-09-30 13:53:56] <silur> at best
    [2019-09-30 13:54:07] <mikerah> kenshamir: If I understand correctly, the polynomial commitment scheme in Halo is derived from Sonic.
    [2019-09-30 13:55:00] <mikerah> silur: There's a lot of research going into quantum secure zk-SNARKs. Although proofs are prohibitely expensive, even more so than current schemes, I expected it to get better in the next 5-10 years
    [2019-09-30 13:55:07] <kenshamir[m]> The paper on the commitment scheme for DARKs is not out yet, it uses class groups, so group sizes will be roughly the same as RSA, but verifier asymptotics will be sublinear
    [2019-09-30 13:56:19] <silur> mikerah: I'm mainly into quantum-safe crypto so I also follow these researches. I'm more optimistic on the matter and expect that breaktrough much sooner :P
    [2019-09-30 13:56:59] <sarang> In the interest of time, let's go ahead and wrap up this meeting; discussions can of course continue after
    [2019-09-30 13:56:59] <kenshamir[m]> <mikerah "kenshamir: If I understand corre"> I read it as a modification of inner product argument that is similar to bulletproofs, I’d need to read sonic though haha, only have ever skimmed it
    [2019-09-30 13:57:18] <kenshamir[m]> The polynomial commitment scheme used in sonic is KZG10 IIRC
    [2019-09-30 13:58:01] <sarang> I'll be working on WCC prep, RCT3 proof review and analysis numbers, and an idea RandomRun had for modifying the Triptych proof to support multiple inputs natively
    [2019-09-30 13:58:01] <mikerah> kenshamir: I also read it as that but if you skim through Halo, they present Sonic and then give the modifications to the sonic scheme in order to achieve amortized succintness
    [2019-09-30 13:58:26] <sarang> For log posting purposes, let's adjourn here and let conversations continue :D


# Action History
- Created by: SarangNoether | 2019-09-26T17:50:20+00:00
- Closed at: 2019-09-30T18:01:09+00:00
