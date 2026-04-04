---
title: 'Research meeting: 29 January 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/432
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-24T21:06:44+00:00'
updated_at: '2020-01-29T19:03:57+00:00'
type: issue
status: closed
closed_at: '2020-01-29T19:03:56+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 29 January 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-01-29T19:03:56+00:00
    [2020-01-29 12:58:29] <sarang> Let's go ahead and get started with GREETINGs
    [2020-01-29 12:58:36] <sarang> Hello
    [2020-01-29 12:58:58] <ArticMine> Hi
    [2020-01-29 12:59:12] → kic00 joined (~kico@gateway/tor-sasl/kico)
    [2020-01-29 12:59:25] <RingSize937> v Greetings
    [2020-01-29 12:59:40] <Isthmus> Heyo
    [2020-01-29 12:59:43] <koe> greetings
    [2020-01-29 12:59:44] * kic00 → kico
    [2020-01-29 13:00:09] <Insight> hello
    [2020-01-29 13:00:27] <atoc> Hi
    [2020-01-29 13:00:41] <sarang> Let's continue with ROUNDTABLE, where anyone is welcome to share research topics of general interest (and discuss any questions arising from them)
    [2020-01-29 13:00:56] ⇐ RingSize937 quit (0c8314ca@12.131.20.202): Remote host closed the connection
    [2020-01-29 13:00:59] <sarang> Since there was so much to discuss last week, I'll try to keep the discussion focused to the extent possible, for clarity
    [2020-01-29 13:01:08] <sarang> I have a few brief things to mention
    [2020-01-29 13:01:38] <sgp_> hello
    [2020-01-29 13:01:40] <sarang> First, I wanted to better understand the effects of including hidden timelocks in CLSAG signatures, and worked up a version of 3-CLSAG in C++ for performance tests
    [2020-01-29 13:01:59] <sarang> Including timelocks would negate the verification time advantages of an MLSAG-CLSAG transition
    [2020-01-29 13:02:02] ⇐ maxwilliamson quit (~maxwillia@gateway/tor-sasl/maxwilliamson): Remote host closed the connection
    [2020-01-29 13:02:06] <sarang> but would still give size benefits over MLSAG
    [2020-01-29 13:02:24] → RingSize9001 joined (0c8314ca@12.131.20.202)
    [2020-01-29 13:02:37] <sarang> A similar approach would work in Triptych, so I extended the Triptych test code to 3-Triptych for this purpose
    [2020-01-29 13:02:57] <sarang> And, just for completeness, updated the Triptych preprint on IACR to a general d-LRS construction
    [2020-01-29 13:03:16] <sarang> Here is the 3-CLSAG test code, for those interested: https://github.com/SarangNoether/monero/commit/db33d18bb889043c4bdea6d8582ffe2f6c581d28
    [2020-01-29 13:03:30] <sarang> And the 3-Triptych concept code: https://github.com/SarangNoether/skunkworks/commit/f7581a385d72baa3dbb60c83e8d856a9335bec1f
    [2020-01-29 13:03:42] <sarang> And the updated Triptych preprint: https://eprint.iacr.org/2020/018
    [2020-01-29 13:03:56] → maxwilliamson joined (~maxwillia@gateway/tor-sasl/maxwilliamson)
    [2020-01-29 13:04:18] <sarang> I also found a very minor change to make in the existing CLSAG test code
    [2020-01-29 13:04:41] <sarang> Finally, suraeNoether and I have been doing more security model stuff
    [2020-01-29 13:04:51] <sarang> Any questions on these items from anyone?
    [2020-01-29 13:05:52] <koe> not directly for sarang, but at Isthmus regarding timelock; what is the prevalence of non-zero timelock for non-coinbase tx?
    [2020-01-29 13:06:09] — Isthmus starts digging around for plots
    [2020-01-29 13:06:18] <Isthmus> Absurdly prevelant
    [2020-01-29 13:06:23] <koe> whether or not to include encrypted time lock depends in part on how much use it actually gets
    [2020-01-29 13:06:26] <koe> used
    [2020-01-29 13:07:10] <sarang> Yeah, and I'm not formally advocating for it at this point; only curious about the implications
    [2020-01-29 13:07:26] <Isthmus> I think our options are to remove the silly timelock field (It's just an arbitrary integer memo field currently) or encrypt it.
    [2020-01-29 13:07:34] <koe> I like that it's a straightforward application of concepts already used in Monero
    [2020-01-29 13:08:03] <sarang> Yeah, conceptually it's really neat
    [2020-01-29 13:08:09] <Isthmus> Will we be the first privacy coin to roll it out?
    [2020-01-29 13:08:15] <Isthmus> I expect that it will become industry standard
    [2020-01-29 13:08:28] <sarang> Does Zcash offer such functionality?
    [2020-01-29 13:08:33] <sarang> (I have not checked)
    [2020-01-29 13:08:42] <sgp_> no clue
    [2020-01-29 13:09:07] <Isthmus> I don't think so, but not 100% confident
    [2020-01-29 13:09:09] <ArticMine> ZCash has serious scaling issues
    [2020-01-29 13:09:27] <sarang> Anyway, whether or not Zcash does it should not be the determining factor IMO :)
    [2020-01-29 13:09:31] <sarang> Merely curious
    [2020-01-29 13:09:32] <Isthmus> Oh wait. Zcash inherited nLockTime from Bitcoin
    [2020-01-29 13:09:40] <Isthmus> 👀
    [2020-01-29 13:09:47] <Isthmus> I'mma fish out their information leaks too
    [2020-01-29 13:09:57] <Isthmus> And OP_CLTV
    [2020-01-29 13:10:00] <sarang> If implemented, it would make the most sense to bundle the timelock range proofs with the existing Bulletproofs
    [2020-01-29 13:10:25] <sarang> So this means the sum of timelock-enabled inputs (all inputs, if mandatory) and outputs is restricted
    [2020-01-29 13:10:34] <koe> for Triptych, what are the steps between now and considering it for replacing RingCT?
    [2020-01-29 13:11:19] <sarang> Formal review, a determination about its effects on multisig (particularly on compute-limited hardware), a decision on Triptych vs something like RCT3
    [2020-01-29 13:11:38] <sarang> I have not yet examined how easy it would be to include timelocks in RCT3 with their security model
    [2020-01-29 13:12:13] <ArticMine> ^ ... and estimated recommended tx size for Triptych
    [2020-01-29 13:12:13] ⇐ maxwilliamson quit (~maxwillia@gateway/tor-sasl/maxwilliamson): Remote host closed the connection
    [2020-01-29 13:12:29] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-01-29 13:13:35] <sarang> Also note that, as I think I mentioned last week, it would not make sense to deploy hidden timelocks with MLSAG due to the poor scaling
    [2020-01-29 13:13:51] <sarang> (though technically possible)
    [2020-01-29 13:13:51] <koe> agreed
    [2020-01-29 13:14:17] <sarang> Anyway, I want to make sure others have time to speak as well
    [2020-01-29 13:14:22] <sarang> Who else wishes to share research topics?
    [2020-01-29 13:14:57] <Isthmus> Zebra network stack looks interesting, potential applications in Monero?
    [2020-01-29 13:15:12] — needmonero90 wanders in and takes a seat in the back
    [2020-01-29 13:15:17] <sarang> I saw that yesterday!
    [2020-01-29 13:15:27] <sarang> Blag post about it: https://www.zfnd.org/blog/a-new-network-stack-for-zcash/
    [2020-01-29 13:15:54] <sgp_> cool, will check out
    [2020-01-29 13:16:08] <sarang> And a corresponding forum post (not much activity there yet): https://forum.zcashcommunity.com/t/a-new-network-stack-for-zcash/35870
    [2020-01-29 13:16:18] → maxwilliamson joined (~maxwillia@gateway/tor-sasl/maxwilliamson)
    [2020-01-29 13:16:24] <sarang> It's from Zcash Foundation research
    [2020-01-29 13:18:29] <Isthmus> Monero maintains a single state across all the peers, right?
    [2020-01-29 13:19:43] <sarang> That's a good question, and I don't know the answer
    [2020-01-29 13:19:53] <sgp_> ping vtnerd
    [2020-01-29 13:20:03] <sarang> I had thought so, but not confident in that
    [2020-01-29 13:20:23] <hyc> not even sure what that means. single state? what is included in that state?
    [2020-01-29 13:20:32] <hyc> there is an aggregate state for bandwidth limiting
    [2020-01-29 13:20:46] <hyc> but sync info is per-connection
    [2020-01-29 13:21:34] <Isthmus> Oh so maybe we already take the Zebra approach?
    [2020-01-29 13:21:39] <Isthmus> It seems pretty elegant.
    [2020-01-29 13:23:11] <sarang> Isthmus: did you have other topics you wanted to bring up as well?
    [2020-01-29 13:23:22] <hyc> "Unlike zcashd, which maintains a fixed number of outbound connections, we attempt to connect to as many peers as possible, subject to resource limits "
    [2020-01-29 13:23:40] <hyc> this approach will be troublesome for them, since they use levelDB/rocksDB for storage
    [2020-01-29 13:23:55] <hyc> lvelDB/rocksDB requires thousands of file descriptors for its storage.
    [2020-01-29 13:24:06] <hyc> that competes with the demand for socket descriptors
    [2020-01-29 13:24:14] <sarang> Interesting... worth bringing up as a question on the forum?
    [2020-01-29 13:24:23] <sarang> One of the developers (Henry) opened the thread
    [2020-01-29 13:24:27] <hyc> not from me. I have no interest in helping zcash project
    [2020-01-29 13:24:30] <sarang> ok
    [2020-01-29 13:25:03] <Isthmus> I'm trying to make the unlock time plot, but my laptop is struggling with the 1.5 GB data set
    [2020-01-29 13:25:08] <hyc> they should have already known by now that their DB choice is inappropriate for a network service that uses lots of connections, but it seems they haven't discovered that yet
    [2020-01-29 13:25:18] <sarang> Isthmus: no rush!
    [2020-01-29 13:25:31] <sarang> In the meantime, koe: did you wish to address anything in particular?
    [2020-01-29 13:25:40] <koe> yes muahaha
    [2020-01-29 13:25:41] <koe> not technically research, my roadmap has been cleaned up a bit; in particular I want to get opinions on item koe_11, which would enable view-only wallets to know when owned outputs have been spent; also item koe_9 which would allow all wallet implementations to more or less deprecate pre-RingCT transaction versions
    [2020-01-29 13:25:41] <koe> https://www.pdf-archive.com/2020/01/29/moneroroadmapkoe012920/moneroroadmapkoe012920.pdf
    [2020-01-29 13:26:13] <hyc> koe_11 sounds like a high priority
    [2020-01-29 13:26:39] <koe> also, sarang helped me work up a decentralized CoinJoin-esque protocol (temporarily named JoinMo), which is available as chapter 9 of current ZtM2 draft
    [2020-01-29 13:26:46] <koe> https://www.pdf-archive.com/2020/01/29/zerotomoneromaster-v1-0-21/zerotomoneromaster-v1-0-21.pdf
    [2020-01-29 13:27:08] <koe> chapter 10*
    [2020-01-29 13:27:42] <sarang> I like the JoinMo approach of using per-participant shared secrets to obscure the input-output mapping
    [2020-01-29 13:27:47] <koe> also, rbrunner at one time investigated OpenBazaar integration, and ran into some roadblocks, so my 'research' has been engineering solutions to those problems, which should be available next week
    [2020-01-29 13:28:04] <sarang> I'm giving extra scrutiny to the specifics around SAG/LSAG since the keys are per-output only
    [2020-01-29 13:28:23] <sarang> I was thinking about the implications of using a separate keyset for inputs as well
    [2020-01-29 13:28:34] <sarang> (keys = per-join participant keys, I mean)
    [2020-01-29 13:28:56] <koe> however, OpenBazaar integration would likely entail a large update to the code-base, to optimize communication rounds
    [2020-01-29 13:29:35] <koe> moreover, multisig in general should be updated to comply with suraeNoether's paper on the subject
    [2020-01-29 13:29:39] <sarang> Yes
    [2020-01-29 13:30:06] <Isthmus> Somewhat related to item 10, I'm still concerned about any blockchain observer being able to identify which transactions do not include any outputs to subaddresses.
    [2020-01-29 13:30:15] <Isthmus> n3ptune and I will make a plot of subaddress adoption over time : -)
    [2020-01-29 13:30:18] <Isthmus> But ideally that should not be possible.3
    [2020-01-29 13:30:25] <sarang> Also yes :)
    [2020-01-29 13:30:53] <sarang> It's been suggested before to standardize on some form of per-output keys for this purpose
    [2020-01-29 13:30:59] <sarang> but it never gained traction
    [2020-01-29 13:31:59] <sgp_> koe: nice list! koe_9 may be controversial since spending pre-rct would stand out more, no?
    [2020-01-29 13:32:15] <atoc> Yeah looks like a nice list koe
    [2020-01-29 13:32:32] <koe> it already stands out like a sore thumb
    [2020-01-29 13:33:07] <koe> but that sort of problem will exist for RingCT as well, since spending ancient outputs is always somewhat unusual
    [2020-01-29 13:33:32] <koe> and my suggestion is to start using pre-ringct outputs as decoys as well
    [2020-01-29 13:33:36] <hyc> If we told everyone to sweep them to themselves, would that also be too obvious? you could assume that every txn with pre-RCT inputs is going back to its sender
    [2020-01-29 13:33:47] <koe> so gamma select over entire site of outputs
    [2020-01-29 13:33:50] <koe> set
    [2020-01-29 13:34:05] <sgp_> koe: do we currently only select rct randomly as decoys?
    [2020-01-29 13:34:30] <koe> yes, and coinbase (not sure if pre-ringct coinbase are included)
    [2020-01-29 13:34:45] <koe> coinbase are included as decoy in normal tx, which is where this idea comes from
    [2020-01-29 13:34:58] <sgp_> then this actually makes spending pre-rct slightly less suspicious, no?
    [2020-01-29 13:35:03] <sarang> And the handling of coinbase outputs is by no means solved
    [2020-01-29 13:35:20] <Isthmus> This is 80% a joke: We implement Koe_9 and sgp_coinbase_only rings, *but* require each and every one to include N coinbases and M pre-ringCT transactions, for fixed consensus parameters N and M
    [2020-01-29 13:35:21] <sarang> sgp_: the distribution tail falls fast
    [2020-01-29 13:35:37] <sgp_> sarang: indeed, but it's near-zero better, not near-zero worse I think
    [2020-01-29 13:36:18] <sarang> Yes, but does provide slightly more information (amount)
    [2020-01-29 13:36:22] <Isthmus> https://usercontent.irccloud-cdn.com/file/R26YQwiJ/image.png
    [2020-01-29 13:36:53] <Isthmus> ^ which is hilarious, because all of these would hypothetically unlock at HEIGHT 2 and HEIGHT 12 back in 2014, IIRC what mooo said
    [2020-01-29 13:37:21] <sarang> Due to the non-standard handling of that field, you mean?
    [2020-01-29 13:37:28] <sarang> (which should be standardized anyway)
    [2020-01-29 13:37:28] <sgp_> Isthmus: hmm, I would need to see a lot more info on how many people actually spend pre-rct (suspected) compared to coinbase. My intuition leans no
    [2020-01-29 13:37:32] <ArticMine> So include a single pre ring CT fake if the real output is not pre ring ct
    [2020-01-29 13:38:57] <Isthmus> @sarang:  Yes, currently, 3 things are being put in the unlock field:
    [2020-01-29 13:39:29] <Isthmus> https://www.irccloud.com/pastebin/0Y87gTTq/
    [2020-01-29 13:39:35] <Isthmus> Argh sorry
    [2020-01-29 13:39:36] <Isthmus> Small integers like "12", presumably to be interpreted as height differences, i.e. "unlock in 12 blocks"
    [2020-01-29 13:39:39] <Isthmus> Large integers like "1980000", presumably to be interpreted as block heights
    [2020-01-29 13:39:41] <Isthmus> Very large integers like "1578561720", presumably to be interpreted as unix timestamps
    [2020-01-29 13:39:51] <sarang> yup
    [2020-01-29 13:40:31] <atoc> I am working on a first version implementation of xmr-btc atomic swap in Rust
    [2020-01-29 13:40:35] <atoc> more info here: https://github.com/h4sh3d/xmr-btc-atomic-swap/blob/master/whitepaper/xmr-btc.pdf
    [2020-01-29 13:40:45] <sarang> atoc: did you identify a suitable zkp?
    [2020-01-29 13:41:45] <sarang> Aside from things like the handling of non-compliant participants etc., the zkp of hash/log preimage was not specified 
    [2020-01-29 13:41:59] <atoc> the paper proposes two transactions for each token
    [2020-01-29 13:42:04] <sarang> yep
    [2020-01-29 13:43:12] <atoc> is there is a zkp not specified I will look at it. So far I have just gotten some initial stuff implemented
    [2020-01-29 13:43:20] <atoc> however I have not gotten to the swap part yet
    [2020-01-29 13:43:31] <atoc> for the implementation, I have read through the paper and it seems sounds
    [2020-01-29 13:43:35] <atoc> sound*
    [2020-01-29 13:44:11] <sarang> Yeah, you'll notice there's a requirement for a particular proof that a hash preimage and discrete log preimage are equal in equal knowledge
    [2020-01-29 13:44:46] <sarang> Something trustless like Bulletproofs could be used for this, with a suitable circuit
    [2020-01-29 13:44:54] <atoc> I see
    [2020-01-29 13:44:57] → nssy2 joined (~nssy@197.237.91.81)
    [2020-01-29 13:45:19] <sarang> The BP paper had data on such a circuit, but I was specifically told it was for testing only and was not yet suitable for any kind of deployment
    [2020-01-29 13:45:38] <atoc> I will take a look at that
    [2020-01-29 13:46:18] <atoc> We will need it. Perhaps we can see if that circuit works okay, and if not hopefully we can look at ways to improve.
    [2020-01-29 13:46:35] <sarang> koe: thanks for that roadmap writeup; it's nice to see many suggestions put together in one place
    [2020-01-29 13:46:59] <sarang> It might be useful to open research-lab issues for those that require ongoing discussion
    [2020-01-29 13:47:11] <sgp_> I still advocate for those two mining pool-related proposals btw :)
    [2020-01-29 13:47:13] <atoc> sarang I send you a link to my repo once I push some changes
    [2020-01-29 13:47:15] <sarang> even though most discussion happens on IRC
    [2020-01-29 13:47:19] <atoc> I will send*
    [2020-01-29 13:47:24] <sarang> Thanks atoc
    [2020-01-29 13:47:36] <atoc> You can take a look and I would like to get your feedback on it
    [2020-01-29 13:47:40] <sarang> Happy to help
    [2020-01-29 13:47:44] <sarang> Thanks for taking a look at that
    [2020-01-29 13:47:52] <atoc> (y)
    [2020-01-29 13:48:31] <koe> sure I can put on research github; was just wondering if koe_11 should go on main repo's issues
    [2020-01-29 13:48:38] <atoc> Np, it seems interesting. This week I was just l familiarizing myself with different atomic swap techniques i.e off-chain and on-chain
    [2020-01-29 13:48:57] <atoc> And looking at the dalek library in Rust
    [2020-01-29 13:49:29] <sarang> koe: I'd say anything that requires ongoing unsolved research is definitely suitable for research-lab
    [2020-01-29 13:49:46] * rottensox_ → rottensox
    [2020-01-29 13:49:57] <sarang> But I don't dictate the scope of issues!
    [2020-01-29 13:50:06] <sarang> OK, we have about 10 minutes left (there's another meeting taking place at 19:00 UTC for the Konferenco)
    [2020-01-29 13:50:18] <koe> ok can put them up there
    [2020-01-29 13:50:19] <sarang> Any research topics that have not yet been brought up, and should be?
    [2020-01-29 13:50:26] <atoc> sarang btw have you considered publishing your list?
    [2020-01-29 13:50:50] <sarang> Of topics I am personally working on? Not really, it's more to help organize my own work
    [2020-01-29 13:50:51] <atoc> The private list that you had of research topics that need attention.
    [2020-01-29 13:51:07] <sarang> I should open issues for them as well
    [2020-01-29 13:51:24] <sarang> TBH github issues for research are not used as well as they could be
    [2020-01-29 13:51:32] <atoc> Yeah I think it would be could to have a public list to look through as important topics for Monero that need attention
    [2020-01-29 13:51:35] <sarang> Since so much of the discussion happens on IRC in real time
    [2020-01-29 13:51:41] <atoc> yes indeed
    [2020-01-29 13:51:51] <sarang> But at least those issues could be used as a central posting location
    [2020-01-29 13:51:59] <atoc> I currently go back to the logs, but that list was helpful.
    [2020-01-29 13:52:01] <sarang> I don't want people to have to scour IRC logs
    [2020-01-29 13:52:09] <sarang> Sure, I'll make some issues
    [2020-01-29 13:52:17] <sarang> We should clear out old issues as well, or request updates
    [2020-01-29 13:52:29] <nioc> peanut gallery here.  Now that suraeNoether 's matching project is complete (?) or nearly so, what is the plan to use it going forward ?
    [2020-01-29 13:52:30] <atoc> 'scouring IRC logs' - story of my life :')
    [2020-01-29 13:52:41] <sarang> nioc: good question for suraeNoether!
    [2020-01-29 13:53:04] <sarang> He has also been working on LRS security models lately
    [2020-01-29 13:53:11] <sarang> (which are a blocker for CLSAG review)
    [2020-01-29 13:53:38] <sarang> OK, let's move to ACTION ITEMS for the time being (discussion can of course continue after we formally adjourn)
    [2020-01-29 13:54:18] <sarang> I am writing up some material on transaction proofs/assertions, and writing up new code for a proposed InProofV2 and OutProofV2
    [2020-01-29 13:54:53] ⇐ cohcho quit (~cohcho@gateway/tor-sasl/cohcho): Remote host closed the connection
    [2020-01-29 13:54:56] <sarang> As well as security model updates, some work on proof rewinding for data storage, and some odds and ends
    [2020-01-29 13:55:01] <sarang> Anyone else?
    [2020-01-29 13:55:08] → cohcho joined (~cohcho@gateway/tor-sasl/cohcho)
    [2020-01-29 13:55:15] <atoc> my action item: mkW my private .git repo (of atomic swap implemntation) public on Githuv
    [2020-01-29 13:55:21] <sarang> neat
    [2020-01-29 13:55:28] <atoc> Github*
    [2020-01-29 13:55:30] <koe> my action items: multisig and escrowed-marketplace protocol writeup, possibly start bulletproof study if time permits
    [2020-01-29 13:55:47] <sarang> BPs for the ZtM writeup?
    [2020-01-29 13:55:48] <Isthmus> I want to make a website where you can type in a stealth address (or list of them) and see what future transactions have used them as ring members
    [2020-01-29 13:55:59] <Isthmus> But need a little bit more backend work before that is ready
    [2020-01-29 13:56:02] <koe> at the very least studying it
    [2020-01-29 13:56:24] <Isthmus> I think the concerning part will be seeing the outputs that have been used in no subsequent rings, and thus have a known spend state and no plausible deniable for spendedness
    [2020-01-29 13:56:26] <sarang> Let me know if you have any particular questions that I may be able to answer
    [2020-01-29 13:56:33] <koe> of course :)
    [2020-01-29 13:56:58] <sarang> Any other action items, or final comments before we adjourn?
    [2020-01-29 13:57:00] <sarang> (from anyone)
    [2020-01-29 13:57:06] <koe> actually spoiled my writeup from several months ago in the latest ztm2 draft whoops
    [2020-01-29 13:57:55] <sarang> It's great to see so much research lately into so many different areas of interest from so many people :D
    [2020-01-29 13:58:06] <sarang> Gets tough to keep up with everything
    [2020-01-29 13:58:14] <sarang> Which is a great problem to have, in some sense
    [2020-01-29 13:58:25] <sarang> Anyway, thanks to everyone for attending; we are now adjourned!


# Action History
- Created by: SarangNoether | 2020-01-24T21:06:44+00:00
- Closed at: 2020-01-29T19:03:56+00:00
