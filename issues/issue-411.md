---
title: 'Research meeting: 18 November 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/411
author: SarangNoether
assignees: []
labels: []
created_at: '2019-11-17T23:27:34+00:00'
updated_at: '2019-11-20T15:12:37+00:00'
type: issue
status: closed
closed_at: '2019-11-20T15:12:37+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 18 November 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-11-20T15:12:37+00:00
    [2019-11-18 12:00:07] <sarang> First, GREETINGS
    [2019-11-18 12:00:11] <sarang> Hello
    [2019-11-18 12:00:19] <hyc> heylo
    [2019-11-18 12:00:46] <mikerah> hello
    [2019-11-18 12:01:44] <sarang> For today's ROUNDTABLE, I have a few things of interest to share
    [2019-11-18 12:02:30] <sarang> Updates to the RingCT 3.0 analysis and code reflect its two provably-sound versions: https://github.com/SarangNoether/skunkworks/blob/sublinear/rct3.md
    [2019-11-18 12:03:00] <sarang> One version is the authors' padded-input version that implies some restrictions on the signer count
    [2019-11-18 12:03:23] <sarang> The other version is a backport I did of the exploit fix from their newer version to the original one, with corresponding changes to security proofs
    [2019-11-18 12:03:40] <sarang> Triptych analysis now reflects an optimized multi-signer version: https://github.com/SarangNoether/skunkworks/blob/sublinear/triptych.md
    [2019-11-18 12:03:58] <sarang> as does its code and the draft writeup
    [2019-11-18 12:04:20] <sarang> I have shared the writeup with a few additional researchers as well, in the hope of getting extra eyes on the soundness proof
    [2019-11-18 12:04:52] <sarang> The CLSAG paper was unfortunately rejected for the Financial Cryptography 2020 conference (which only had a 22% acceptance rate, according to the committee)
    [2019-11-18 12:05:00] <sarang> Here are the reviewer comments: https://gist.github.com/SarangNoether/e39db743c3260448c1d67c3622b43f4b
    [2019-11-18 12:05:44] <sarang> Reviewer A, who recommended rejection, made some detailed points about the security model: particularly how ambiguity and linkability are treated relative to some other papers
    [2019-11-18 12:05:54] <sarang> Once suraeNoether returns, I want to discuss the particulars of this
    [2019-11-18 12:06:23] <sarang> I'm not convinced that the more complete linkability treatment (which ties in ambiguity as well) is needed, given the use case
    [2019-11-18 12:06:58] <sarang> However, the recommendation for a more robust treatment of signer ambiguity is fair
    [2019-11-18 12:07:53] <sarang> The notes about the k-OMDL assumption being less common are also fair, but that's the best hardness assumption that was found for the proofs in question
    [2019-11-18 12:09:22] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Remote host closed the connection
    [2019-11-18 12:10:22] <sarang> Related to CLSAG:  Derek at OSTIF tells me that JP Aumasson, who quoted $7200 to review the paper, is available presently to do so, and it's not clear at the moment when he would be unavailable again
    [2019-11-18 12:10:32] <sarang> I didn't sense a lot of broad support for this earlier
    [2019-11-18 12:11:36] <sarang> Given that the FC2020 review comments just came back, the paper should be updated to reflect the notes before being sent off to anyone for additional review
    [2019-11-18 12:12:57] <sarang> So the timeline on this seems unclear right now
    [2019-11-18 12:13:16] <sarang> Does anyone else wish to share interesting news or research?
    [2019-11-18 12:18:57] <sarang> Righto
    [2019-11-18 12:20:21] <sarang> My ACTION items are to address CLSAG reviewer comments to update the preprint, finalize single-signer Triptych analysis and the associated preprint, continue working with others on whether multi-signer soundness is provable using known assumptions,  and examine the current state of suraeNoether's graph-matching work
    [2019-11-18 12:20:33] <sarang> What a quiet meeting =p
    [2019-11-18 12:21:02] <MalMen> normaly this meetings are you talking with suraeNoether :P (at least the lasts I watch)
    [2019-11-18 12:21:27] <MalMen> I am reading the links you posted, thank you for the heads up
    [2019-11-18 12:22:13] <sarang> selsta also posted this link elsewhere, which I found very interesting: https://medium.com/dragonfly-research/breaking-mimblewimble-privacy-model-84bcd67bfe52
    [2019-11-18 12:22:36] <sarang> Looking at a practical attack on Grin using network observation
    [2019-11-18 12:24:04] <MalMen> I did start to understud better how MW work with that research
    [2019-11-18 12:25:24] <MalMen> there is not much they can do about this kinda of attack unless users kinda of "coinjoin" the transactions with know peers before releasing them to the all network
    [2019-11-18 12:25:37] <MalMen> for what I did understund about it
    [2019-11-18 12:26:29] <sarang> It definitely highlights the importance of the network and propagation layer in transactions
    [2019-11-18 12:27:18] <kico> seems like using 8 peers only by default is kinda dangerous
    [2019-11-18 12:27:32] <sarang> vtnerd has been looking into the tricky interactions involved with integrating Dandelion++, I2P, Tor, and the like
    [2019-11-18 12:28:06] <kico> I mean for dandelion to work "properly"
    [2019-11-18 12:28:20] <MalMen> It should be possible to get some farly good level of privacy with MW, but the way the transactions are propagated would need to became more complex in order to ofuscate the way they are made
    [2019-11-18 12:28:35] <sarang> How so? Dandelion++ provides restrictions on stem neighbor selection for a given time epoch
    [2019-11-18 12:28:39] <MalMen> kinda of what Bitcoin think they can do on layer2 to obuscate the linkability on layer1
    [2019-11-18 12:29:26] → TheoStorm joined (~TheoStorm@78-22-87-51.access.telenet.be)
    [2019-11-18 12:30:18] <kico> I guess if one connects to more peers it increases the chance that it aggregates transactions before they're peered to the network for what I understood from that paper
    [2019-11-18 12:33:10] <sarang> A good lesson on how it's tricky to assume things about transactions before they reach the chain, I suppose
    [2019-11-18 12:36:01] <sarang> Well, anything else of interest to discuss before closing the meeting?
    [2019-11-18 12:36:18] <sarang> If anyone has thoughts or comments relating to the CLSAG reviewer notes, I'd be glad to hear them
    [2019-11-18 12:37:03] <MalMen> just one quick question from someone that dont know much abouth CLSAG
    [2019-11-18 12:37:08] <sarang> sure
    [2019-11-18 12:38:05] <MalMen> CLSAG will not make possible second layer networkds (missing the word here) ?
    [2019-11-18 12:38:30] <sarang> No, it doesn't introduce any new functionality toward that
    [2019-11-18 12:38:45] <sarang> Its only purpose is to make signatures smaller and a bit faster
    [2019-11-18 12:39:25] <sarang> Off-chain solutions are limited by a lack of scripting and ambiguity around useful things like non-interactive refunds, etc.
    [2019-11-18 12:39:38] <MalMen> there is something that can possibility second layer in the future for monero  yet or we still far from it ?
    [2019-11-18 12:39:44] <sarang> Introducing such things is tricky (DLSAG is one attempt, but suffers from a linking problem)
    [2019-11-18 12:40:29] <MalMen> ok, thank you for the heads up
    [2019-11-18 12:40:46] <sarang> If you are willing to work through the technical language and definitions, the DLSAG paper has some very clever constructions: https://eprint.iacr.org/2019/595
    [2019-11-18 12:41:06] <sarang> (disclaimer: I am a co-author on the paper, but did not come up with the original idea)
    [2019-11-18 12:41:29] <MalMen> Ok, I will take a look
    [2019-11-18 12:41:45] <sarang> It highlights how tricky it can be to enable swaps, payment channels, and the like, given the protocol and indistinguishability restrictions
    [2019-11-18 12:42:06] <sarang> Oh, I should also add that the DLSAG paper _was_ accepted to the FC2020 conferences
    [2019-11-18 12:42:19] <MalMen> oh, that is good
    [2019-11-18 12:43:03] <MalMen> I believe that it will be almost impossible to make any "Non-Interactive Refund Transactions" (just took it from the paper) seemless as the other transactions
    [2019-11-18 12:43:27] <sarang> DLSAG comes very close, but the linking problem is troublesome
    [2019-11-18 12:43:57] <MalMen> peraphs we would come to a place where we need to choose if we want to acept anything like DLSAG knowing its less private but allow us to have hotswaps and some kind of lightning network working
    [2019-11-18 12:44:18] <MalMen> or just keep with onechain transactions
    [2019-11-18 12:45:32] <sarang> I would not expect broad support for such a tradeoff, but who knows
    [2019-11-18 12:45:53] <sarang> And perhaps a new idea that _does_ solve the problem will arise at some point
    [2019-11-18 12:46:05] <MalMen> we hope so
    [2019-11-18 12:46:17] <sarang> Anyway, are there other topics of interest to bring up before closing the meeting?
    [2019-11-18 12:46:19] <MalMen> well, thats all from me, thanks for your time sarang *
    [2019-11-18 12:46:27] <sarang> no problem
    [2019-11-18 12:47:31] <sarang> OK, the meeting is over! Thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2019-11-17T23:27:34+00:00
- Closed at: 2019-11-20T15:12:37+00:00
