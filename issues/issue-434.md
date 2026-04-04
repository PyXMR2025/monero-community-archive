---
title: 'Research meeting: 5 February 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/434
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-30T15:51:59+00:00'
updated_at: '2020-02-05T19:06:16+00:00'
type: issue
status: closed
closed_at: '2020-02-05T19:06:15+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 5 February 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-02-05T04:55:47+00:00
No agenda point here, just some observations.
-  Most transactions have 2 outputs
-  Oddly, there's a bunch of transactions that have 11 outputs (reason unknown)
-  There output use drops dramatically > 2 (note log y-axis) and then slowly decreases to 13. Reasons were proposed related to mining pools, but I don't quite see it yet.

![image](https://user-images.githubusercontent.com/21246742/73811957-dfde3a80-478f-11ea-8413-7bee4ef4be48.png)


## SamsungGalaxyPlayer | 2020-02-05T17:56:34+00:00
I believe the 11 output phenomenon was mentioned in the last meeting as a limitation of some old, less-used pool software.

## SarangNoether | 2020-02-05T19:06:15+00:00
    [2020-02-05 12:59:49] <sarang> OK, let's get started
    [2020-02-05 13:00:03] <sarang> Logs from this meeting will be posted to the agenda issue shortly after the meeting
    [2020-02-05 13:00:09] <sarang> First, GREETINGS
    [2020-02-05 13:00:10] <sarang> hello
    [2020-02-05 13:00:16] <sgp_> hello
    [2020-02-05 13:00:34] <suraeNoether> good mroning
    [2020-02-05 13:00:49] <UkoeHB_> hiya
    [2020-02-05 13:01:27] — sarang will wait a minute for anyone else to arrive
    [2020-02-05 13:03:06] <sarang> On to ROUNDTABLE, where anyone is free to share interesting research
    [2020-02-05 13:03:18] <sarang> I'll go first, since I have a small assortment of things
    [2020-02-05 13:03:51] <sarang> I worked up code and examples for doing hidden data storage within Bulletproofs and Triptych, suitable only for the prover
    [2020-02-05 13:03:53] <Isthmus> I,m kinda here, but on a conference call
    [2020-02-05 13:04:20] <sarang> Several ongoing projects/issues have been moved to monero-project/research-lab issues for comment and discussion
    [2020-02-05 13:05:03] <sarang> The CLSAG code on my monero fork (clsag-plumbing branch) has been cleaned up; thanks to UkoeHB_ for helpful suggestions and comments
    [2020-02-05 13:05:28] <sarang> It includes, among other things, hash function domain separation that we hope to roll out elsewhere for a more robust overall codebase
    [2020-02-05 13:06:02] <sarang> There is also CLSAG Python sample code showing how to do signer index extraction in a clever way, which I assume UkoeHB_ may wish to discuss when he shares
    [2020-02-05 13:06:14] <sarang> I've written up material for ZtM about transaction proofs/assertions
    [2020-02-05 13:06:43] <sarang> And have worked up some new C++ code that updates transaction in/out proofs to have correct Schnorr challenges
    [2020-02-05 13:06:51] <sarang> (still need to write tests for this)
    [2020-02-05 13:07:04] <sarang> That's my update; any particular questions before the baton is passed?
    [2020-02-05 13:07:58] <suraeNoether> quick question: iirc you had done work on encrypted timelocks
    [2020-02-05 13:08:03] <sarang> yes
    [2020-02-05 13:08:06] <suraeNoether> i've been chatting with both isthmus and TheCharlatan about them
    [2020-02-05 13:08:13] <suraeNoether> do you have any notes prepared any place for later reading?
    [2020-02-05 13:08:29] <sarang> On what in particular?
    [2020-02-05 13:08:37] <suraeNoether> alternatively: can we schedule a discussion in this room that will end up in the logs for later this week?
    [2020-02-05 13:09:00] <sarang> Sure
    [2020-02-05 13:09:27] <sarang> Let's table for now, and address at the end
    [2020-02-05 13:09:34] <suraeNoether> if we implement them regardless of if we are using mlsag, clsag, or triptych, there's going to be a cost. i want to see how it's all going to fit into future monero dev
    [2020-02-05 13:09:39] <suraeNoether> word, word, i can go next
    [2020-02-05 13:09:45] <sarang> OK, go ahead suraeNoether
    [2020-02-05 13:09:48] — sarang makes a note about timelocks
    [2020-02-05 13:09:58] <suraeNoether> last week i spent a lot of time on CLSAG and linkable ring signatures security definitions
    [2020-02-05 13:10:22] <suraeNoether> there are a lot of definitions out there and they don't all relate to each other in a clean taxonomy, and it wasn't clear which ones we needed to use, and so on
    [2020-02-05 13:10:43] <suraeNoether> so i started writing this rather large technical note summarizing all this with the intention of writing a second paper about it, but sarang and i have decided to merge the two into a new draft
    [2020-02-05 13:11:12] <suraeNoether> the reason is that even definitions of unforgeability miss absolutely critical stuff becuase they are taken from "ring signatures" and mapped over to "linkable ring signatures" wholesale without regard for linking properties
    [2020-02-05 13:12:04] <suraeNoether> so now the paper will be proposing a new definition of unforgeability specifically for linkable ring signatures that subsumes more than one security definition, and this is going to set the standard for a few years on how unforgeability is considered for all applications of linkable ring signatures.
    [2020-02-05 13:12:09] <suraeNoether> this is good news(tm) for MRL
    [2020-02-05 13:12:20] <Isthmus> sweet
    [2020-02-05 13:12:28] <UkoeHB_> congrats :)
    [2020-02-05 13:12:33] <suraeNoether> thanks :D
    [2020-02-05 13:12:41] <sarang> It makes the preprint all the more valuable
    [2020-02-05 13:12:44] <suraeNoether> In addition to that, I have been preparing my talk for the Blockchain Tech Symposium at the Fields Institute in two weeks, and debugging my matching code.
    [2020-02-05 13:13:01] <suraeNoether> i'm extremely grateful to the peer reviewer who "gently" pointed us towards the backes' paper actually
    [2020-02-05 13:13:03] <sarang> Having both improvements to security models _and_ a new construction seems to be the gold standard these days
    [2020-02-05 13:13:07] <suraeNoether> they did us more of a favor than maybe they realized
    [2020-02-05 13:13:37] <suraeNoether> my work for the week will include finishing up this new draft of CLSAG, and to begin large-scale data collection on matching
    [2020-02-05 13:14:17] <sarang> Thanks suraeNoether
    [2020-02-05 13:14:20] <sarang> Any questions for suraeNoether?
    [2020-02-05 13:14:44] <UkoeHB_> if you want more CLSAG work, it's possible to increase the number of linkable keys up to the total number of pub keys considered :p
    [2020-02-05 13:15:05] <sarang> Sure, but that's not useful for our particular application
    [2020-02-05 13:15:09] <sarang> which is why we didn't consider it
    [2020-02-05 13:15:55] <UkoeHB_> I believe there was an earlier question from nioc about matching
    [2020-02-05 13:16:04] <UkoeHB_> for suraeNoether
    [2020-02-05 13:16:18] <sarang> 12:46 <nioc> my question is, what is the status of the matching project and how will is be used going forward to help select an appropriate ringsize?
    [2020-02-05 13:16:28] <sarang> ^ was the question
    [2020-02-05 13:17:42] <suraeNoether> ah, great question: the matching project is *what appears to be* a single-line bug away from correctly generating simulated ledgers. it already appears to generate correct confusion matrices; once this bug is cleared up, it's a matter of executing a big block of code for a large period of time to get all the sample data, and then analyzing the data that's dumped to file.
    [2020-02-05 13:18:24] <suraeNoether> so... if this bug, just like all the others, is a hydra, then I don't have a good answer, but i suspect i've narrowed down the problems to the source
    [2020-02-05 13:18:39] <UkoeHB_> Is the purpose of the matching project to produce the ledgers?
    [2020-02-05 13:18:56] <suraeNoether> there are several purposes, but here's the main thing
    [2020-02-05 13:19:30] <suraeNoether> we want to estimate how well an adversary can do at finding the "real" history of a monero ledger, given some hints (like it's a KYC exchange)
    [2020-02-05 13:19:44] <suraeNoether> i have a method of computing a maximum likelihood estimate of the real history given some obscured ledger, and all that code works
    [2020-02-05 13:20:02] <suraeNoether> and i have a method of taking an estimate and comparing it to the ground truth, producing a confusion matrix, and all that code works
    [2020-02-05 13:20:17] <suraeNoether> i have a simulator that generates simulated ledgers, and the vast majority of that simulator is working just fine, too
    [2020-02-05 13:21:08] <suraeNoether> the origin of the project came from the idea of developing a game-theoretic description of traceability on the monero ledger: you hand me an obscured ledger and some hints, I hand back to you my best guess, and then success is judged by you comparing the best guess to the ground truth you kept from me the whole time
    [2020-02-05 13:22:04] <suraeNoether> so, the hope is: graph performance against ring size, and see if getting larger than 11 is a waste of space/time or not
    [2020-02-05 13:22:36] <suraeNoether> in the meantime, we hope to also get good data for zcash-style ledgers, so that we can actually rigorously compare the two ledgers against each other, instead of tweeting at each other about fragility
    [2020-02-05 13:22:48] <suraeNoether> but that last bit is farrrrr down the line
    [2020-02-05 13:23:10] <Isthmus> Oh yea, I just remembered that ginger and I talked about generating synthetic blockchains forever ago https://github.com/insight-decentralized-consensus-lab/CryptoNote-Blockchain-GAN/issues/1
    [2020-02-05 13:23:22] — Isthmus has to run to a meeting at :30, sorry >_<
    [2020-02-05 13:23:27] <sarang> OK, any follow-up questions on this?
    [2020-02-05 13:23:37] <suraeNoether> unfortunately, i've not worked on matching since mid-January because CLSAG's security models are critically important
    [2020-02-05 13:24:06] <sarang> and CLSAG needs to get out the door
    [2020-02-05 13:24:21] <sarang> Anything else to share, suraeNoether?
    [2020-02-05 13:25:51] <sarang> Does anyone else wish to share relevant or interesting research?
    [2020-02-05 13:27:02] <Isthmus> I'm taking a break from blockchain logs analysis to do some chat log analysis, analyzing recurring logical fallacies in this space
    [2020-02-05 13:27:04] <suraeNoether> Nope
    [2020-02-05 13:27:11] <suraeNoether> isthmus lol really?
    [2020-02-05 13:27:23] <sarang> ?
    [2020-02-05 13:27:29] <Isthmus> Yeah, actually doing a formal analysis
    [2020-02-05 13:27:35] <suraeNoether> Isthmus: if you are, i have a friend to hook you up with at the university of exeter
    [2020-02-05 13:27:37] <sarang> This channel in particular?
    [2020-02-05 13:27:44] <sarang> Or more broadly in cryptography?
    [2020-02-05 13:27:50] <Isthmus> Somewhat broady
    [2020-02-05 13:27:56] <Isthmus> There's 7 common ones that show up in -lab
    [2020-02-05 13:28:00] <sarang> go on...
    [2020-02-05 13:28:25] <Isthmus> But they break down into combinations of red herrings and something that is *similar* to the slippery slope argument, but not quite the same and I'm still nailing down its technical logical structure
    [2020-02-05 13:28:33] <suraeNoether> dude, please elaborate
    [2020-02-05 13:29:14] <Isthmus> Like when we're debating fixing a tractable privacy leak, and somebody points out that there are other privacy leaks
    [2020-02-05 13:29:23] <UkoeHB_> :O
    [2020-02-05 13:29:50] <suraeNoether> ah yeah
    [2020-02-05 13:29:59] <suraeNoether> or comparing everything to 50% attack costs
    [2020-02-05 13:30:13] <Isthmus> Another one is the hashrate code control fallacy
    [2020-02-05 13:30:34] <suraeNoether> ?
    [2020-02-05 13:30:38] <Isthmus> Confusing a 51% attack on longest chain with a 51% attack on the code
    [2020-02-05 13:30:42] <Isthmus> This came up a few weeks ago actually
    [2020-02-05 13:30:45] <suraeNoether> aaaah
    [2020-02-05 13:31:01] <suraeNoether> i smell some medium articles
    [2020-02-05 13:31:02] <Isthmus> Like why should we bother working on the protocol and code, when one day, somebody might run their own version on a bunch of their own miners
    [2020-02-05 13:31:15] <sarang> Based on what you've analyzed so far, any particular recommendations to avoid such flaws in discussion/thinking?
    [2020-02-05 13:31:16] <Isthmus> That one can be disproven by contradiction
    [2020-02-05 13:31:32] <Isthmus> If 50% of BTC hashrate moved to BCH, does that make BCH the official bitcoin?
    [2020-02-05 13:31:33] <suraeNoether> "why should we patch little leaks in info here and there" styled privacy nihilism/despair
    [2020-02-05 13:31:40] <Isthmus> Oh shit, I gotta be in a meatspace meeting
    [2020-02-05 13:31:43] <Isthmus> ciao!
    [2020-02-05 13:31:57] <sarang> -__-
    [2020-02-05 13:32:20] <sarang> Very interesting stuff
    [2020-02-05 13:32:37] <Isthmus> Erm, not by contradiction. I mean by example demonstrating absurdity
    [2020-02-05 13:32:44] <sarang> We have plenty of time left... does anyone else wish to share anything?
    [2020-02-05 13:32:47] <UkoeHB_> lol 😆
    [2020-02-05 13:32:52] <suraeNoether> lol "i'm going to use machine learning to watch all of your conversations and find out who repeats fallacies most zealously BAIII GOTTA GO GRAB A FREE SLIZE OF 'ZZA FROM THE CORPORATE OVERLORDS" amiright
    [2020-02-05 13:33:06] <UkoeHB_> Here's mine. Worked on write-ups of different ideas -> now Research repo Issues, with good feedback from sarang improving viewspent approach. TxTangle (aka my monero coinjoin protocol) is mostly done and just needs questions answered about network-layer anonymity. Current draft of ZtM2 is here https://www.pdf-archive.com/2020/02/05/zerotomoneromaster-v1-0-23/zerotomoneromaster-v1-0-23.pdf and current
    [2020-02-05 13:33:06] <UkoeHB_> ‘koe’s Ideas’ is here https://www.pdf-archive.com/2020/02/05/moneroideaskoe020520/moneroideaskoe020520.pdf
    [2020-02-05 13:33:30] <sarang> Yeah, the original view/spent idea was broken, but there's a better approach
    [2020-02-05 13:33:44] <sarang> It ties in with the CLSAG index extraction that I mentioned earlier
    [2020-02-05 13:34:26] <sarang> If the signer generates all non-signing scalars via a PRNG `s_i := H(seed,i)` (with appropropriate seed data), then it can be asserted privately what the signing index is
    [2020-02-05 13:35:10] <sarang> It removes the need to add anything to the chain, and hence is good for indistinguishability
    [2020-02-05 13:35:24] <sarang> I dig it, provided the UX is sufficient for reasonable use cases
    [2020-02-05 13:35:37] <UkoeHB_> yeah if view key can regenerate those scalars, it can know when an output has been spent with certainty
    [2020-02-05 13:35:50] <UkoeHB_> of course, it only works if tx author generates scalars like that
    [2020-02-05 13:36:00] <sarang> The problem is still that it's opt-in, so even an accidental use of a non-participating wallet ruins the account balance computation for good
    [2020-02-05 13:36:16] <sarang> So you'd have to be super-clear about presenting that to the user
    [2020-02-05 13:36:24] <sgp_> hmm
    [2020-02-05 13:36:40] <sarang> Of course, a wallet could be doing that right now for all we know
    [2020-02-05 13:36:51] <sarang> it's non-consensus and can't be detected if done properly anyway
    [2020-02-05 13:38:21] <UkoeHB_> it does leave open questions about data stored by nodes, since signature scalars are pruned; perhaps only full nodes, or view-spent enabled nodes can be used
    [2020-02-05 13:38:33] <sarang> IMO that's a completely reasonable trade-off
    [2020-02-05 13:39:04] <sgp_> sounds reasonable to me too
    [2020-02-05 13:39:06] <UkoeHB_> it also may greatly increase data transmitted to view-only wallets by remote nodes
    [2020-02-05 13:39:09] <sarang> Bloating the network for optional functionality benefitting only a single user seems unnecessary
    [2020-02-05 13:39:28] <sarang> But this approach means you can run a full node (good for the network) and have the functionality for your wallets safely
    [2020-02-05 13:40:32] <sgp_> UkoeHB_: I think that's a good thing to point out but probably isn't a showstopper
    [2020-02-05 13:40:53] <UkoeHB_> might need to receive a gigabyte of data to read through a year's worth of tx
    [2020-02-05 13:42:24] <suraeNoether> hmmm
    [2020-02-05 13:42:31] <suraeNoether> i'm a little worried about this in the following sense
    [2020-02-05 13:42:36] <sgp_> I still think that is okay for view-only wallets
    [2020-02-05 13:42:45] <suraeNoether> you are selecting the non-signing scalars deterministically from a PRNG
    [2020-02-05 13:42:52] <sgp_> anyone using them for critical stuff, or viewing multiple wallets, should run their own node
    [2020-02-05 13:43:05] <suraeNoether> one thing we all know about schnorr signatures is that if nonces are selected deterministically, it's possible to extract the private keys
    [2020-02-05 13:43:24] <suraeNoether> at least, under certain constraints
    [2020-02-05 13:43:26] <sarang> suraeNoether: yes, which is why seed selection is very important
    [2020-02-05 13:43:26] <suraeNoether> so my question is
    [2020-02-05 13:43:35] <sarang> UkoeHB_ and I discussed this a bit already earlier
    [2020-02-05 13:44:12] <suraeNoether> if the seed is chosen from a high entropy distribution and kept secret, it's computationally hard to detect that these are computed deterministically
    [2020-02-05 13:44:27] <suraeNoether> i would prefer a method that is more than computationally hard
    [2020-02-05 13:44:37] <sarang> Presumably the seed is a combination of the view secret key, the index, the key image, etc.
    [2020-02-05 13:44:50] <sarang> suraeNoether: how would that even work?
    [2020-02-05 13:45:15] <sarang> Data extraction requires that only the designated parties be able to construct the "expected" output value
    [2020-02-05 13:45:27] <suraeNoether> pfeh, we use PRNGs because statistical RNGs don't really exist :P so ... it wouldn't
    [2020-02-05 13:45:49] <sarang> Well, right now we operate on the assumption that the user has access to something behaving as an RNG
    [2020-02-05 13:45:54] <sarang> this moves to an honest-to-goodness PRNG
    [2020-02-05 13:45:57] <sarang> (and has to)
    [2020-02-05 13:46:06] <sarang> You can't do data extraction with a true RNG AFAICT
    [2020-02-05 13:47:11] <suraeNoether> that... is... true.
    [2020-02-05 13:47:21] <sarang> Anyway, this is an interesting topic that could be useful for a future release
    [2020-02-05 13:47:41] <sarang> but has subtle aspects to seed selection and UX that need further review
    [2020-02-05 13:47:46] <sarang> Let's move on, for the sake of time
    [2020-02-05 13:47:54] <sarang> Any other topics you wish to share, UkoeHB_?
    [2020-02-05 13:48:22] <UkoeHB_> well, I hope people can leave feedback on the repo issues
    [2020-02-05 13:48:27] <sarang> Yes, please do
    [2020-02-05 13:48:37] <sarang> Much easier than only doing IRC comments =p
    [2020-02-05 13:48:37] <UkoeHB_> sorted TLV is probably most important for next hardfork
    [2020-02-05 13:49:06] <sarang> TBH that's probably going to be better for -dev discussion
    [2020-02-05 13:49:20] <sarang> More of an engineering question than a math question :)
    [2020-02-05 13:49:25] <UkoeHB_> true
    [2020-02-05 13:49:38] <sarang> I'd bring it up at a dev meeting, or just in -dev whenever
    [2020-02-05 13:49:45] <sarang> Get a sense of the work involved
    [2020-02-05 13:49:59] <UkoeHB_> ok
    [2020-02-05 13:50:14] <sarang> I know people have brought up tx_extra parsing before, and it's a hot topic
    [2020-02-05 13:50:36] <sarang> Does anyone else wish to discuss other research topics?
    [2020-02-05 13:50:37] <UkoeHB_> ah, CLSAG section was added to ZtM2 for anyone curious
    [2020-02-05 13:50:43] <sarang> excellent
    [2020-02-05 13:51:16] <suraeNoether> uh i saw vtnerd's push on dandelion++
    [2020-02-05 13:51:21] <sarang> Yes
    [2020-02-05 13:51:23] <sarang> Most excellent
    [2020-02-05 13:51:29] <sarang> It's on my list to review later this week
    [2020-02-05 13:51:31] <sarang> Speaking of which
    [2020-02-05 13:51:41] <sarang> Let's briefly move to ACTION ITEMS to respect everyone's time
    [2020-02-05 13:52:42] <sarang> I'll be reviewing the D++ PR, working through some additional transaction assertion/proof stuff, updating sublinear tx protocol MPCs, and writing up examples of RCT3 hidden data storage
    [2020-02-05 13:52:49] <suraeNoether> yes. Mine: Finish CLSAG, start collecting matching data. Also, of primary importance: provide updates twice or three times a day in here until both of these are finished.
    [2020-02-05 13:52:52] <sarang> As well as getting tests written for the new tx in/out proofs
    [2020-02-05 13:53:08] <suraeNoether> i'll be reviewing the D++ pr also once those are both off my plate
    [2020-02-05 13:53:15] <sarang> Yes, looking forward to the CLSAG stuff (will review when ready)
    [2020-02-05 13:53:29] <sarang> Anyone else have action items planned for the week?
    [2020-02-05 13:54:18] <UkoeHB_> To do: focus on multisig all week, hopefully finish txtangle (need a network anonymity expert for advice, any takers?)
    [2020-02-05 13:54:33] <sarang> The most knowledgeable person is probably vtnerd
    [2020-02-05 13:54:59] <sarang> I hear if you say his name 3 times, he gets 3 separate notifications...
    [2020-02-05 13:55:10] <sarang> =p
    [2020-02-05 13:56:00] <sarang> Any last-minute items, questions, etc. before we formally wrap up?
    [2020-02-05 13:56:54] <sarang> (I'm happy to discuss timelocks after we adjourn)
    [2020-02-05 13:56:59] <sarang> Going once...
    [2020-02-05 13:57:22] <sarang> twice...
    [2020-02-05 13:57:44] <sarang> Adjourned! Thanks to everyone for attending; logs will be posted shortly on the agenda issue


# Action History
- Created by: SarangNoether | 2020-01-30T15:51:59+00:00
- Closed at: 2020-02-05T19:06:15+00:00
