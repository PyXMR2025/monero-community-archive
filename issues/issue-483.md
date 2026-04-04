---
title: 'Research meeting: 15 July 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/483
author: SarangNoether
assignees: []
labels: []
created_at: '2020-07-09T13:05:48+00:00'
updated_at: '2020-07-15T17:24:21+00:00'
type: issue
status: closed
closed_at: '2020-07-15T17:24:21+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 15 July 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-07-15T17:24:21+00:00
    [2020-07-15 13:00:29] <sarang> OK, let's get started!
    [2020-07-15 13:00:35] <sarang> The usual agenda: https://github.com/monero-project/meta/issues/483
    [2020-07-15 13:00:41] <sarang> Logs will be posted there after the meeting
    [2020-07-15 13:00:44] <sarang> First, GREETINGS
    [2020-07-15 13:00:45] <sarang> hello
    [2020-07-15 13:00:48] <ArticMine> Hi
    [2020-07-15 13:00:56] <Isthmus> I probably can't hang around for the full meeting, can I drop quick notes?
    [2020-07-15 13:01:05] <sarang> Sure
    [2020-07-15 13:01:08] <sarang> Go ahead Isthmus
    [2020-07-15 13:01:15] <Isthmus> We're mostly turning our attention towards solutions now, though we did just note yesterday that if Keccak pre-image is the last line of defense against Shor's then with Grover's even with an outside observer it can be potentially be broken. Though the can can be kicked down the road by increasing key size
    [2020-07-15 13:01:38] <Isthmus> Unrelated, I've been looking at 0-value transactions lately
    [2020-07-15 13:01:40] <Isthmus> https://github.com/Mitchellpkt/stingy_spammer
    [2020-07-15 13:01:56] <Isthmus> I don't think this is a big threat for Monero based on default behavior of miners
    [2020-07-15 13:02:25] <sarang> This feels very similar to an attack on Zcash that was reported a long while ago
    [2020-07-15 13:02:44] <Isthmus> I think it's probably applicable to most privacy coins
    [2020-07-15 13:03:38] <Isthmus> Reminiscent of the sapling woodchipper, but I don't think they explored 0-value, just low-value/big-size
    [2020-07-15 13:03:59] <Isthmus> Anywho, that's all from me
    [2020-07-15 13:03:59] <sarang> Sapling doesn't enforce strictly positive values, right?
    [2020-07-15 13:04:19] <sarang> And fees are fixed (or at least, not dependent on factors like size or outputs)
    [2020-07-15 13:04:20] <Isthmus> Not sure. Protocol definitely allows 0-fee txns, I found like 2000 on-chain
    [2020-07-15 13:04:20] <sarang> afaik
    [2020-07-15 13:04:30] <Isthmus> Ehhh
    [2020-07-15 13:04:32] <Isthmus> Not "fixed"
    [2020-07-15 13:04:39] <sarang> Fixed is the wrong term here
    [2020-07-15 13:04:46] <Isthmus> "Recommended" to be 0.0001 ZEC, which about 98% of transactions follow.
    [2020-07-15 13:04:47] <sarang> Fees are independent of size/outputs, right?
    [2020-07-15 13:04:58] <Isthmus> Fees are 100% arbitrary, you can slap anything in there
    [2020-07-15 13:05:00] <sarang> Right, you can just set a fee to be 0.0001 ZEC and have a ton of outputs
    [2020-07-15 13:05:05] <Isthmus> Yep
    [2020-07-15 13:05:06] <sarang> Meaning DoS
    [2020-07-15 13:05:11] <sarang> This is _still_ an issue, right?
    [2020-07-15 13:05:17] <sarang> (off topic, I know)
    [2020-07-15 13:05:53] <ArticMine> Privacy combined with gratis can be deadly since censorship cannot be used to fight spam
    [2020-07-15 13:06:01] <Isthmus> Yeah, I've had some chats with Zcash/ECC folks, and they've discussed the for a better way to handle market selection. (Chats with individuals, not speaking officially)
    [2020-07-15 13:06:16] <sarang> Hmm ok; it was reported quite a while ago, and the reaction seemed to be "shrug"
    [2020-07-15 13:06:22] <sarang> Anyway, hopefully lessons we can learn from that
    [2020-07-15 13:06:38] <sgp_> hello
    [2020-07-15 13:06:43] <sarang> I know some in ECC/ZF are extremely opposed to the idea of fee markets
    [2020-07-15 13:06:47] <sarang> I don't really get that
    [2020-07-15 13:06:49] <sarang> but whatever
    [2020-07-15 13:07:02] <sarang> Anyway, thanks Isthmus
    [2020-07-15 13:07:05] <sarang> Any other updates to share?
    [2020-07-15 13:07:09] <ArticMine> Thanks
    [2020-07-15 13:08:09] <sarang> OK, we can continue with ROUNDTABLE, where anyone is welcome to share research of interest to this group
    [2020-07-15 13:08:17] <sarang> Does anyone have something they wish to share?
    [2020-07-15 13:08:42] <ArticMine> I have completed my fee and scaling analysis with recommendations for issue 70
    [2020-07-15 13:08:51] <sarang> Excellent; go on!
    [2020-07-15 13:08:52] <ArticMine> Will be postig there this week
    [2020-07-15 13:08:56] <sarang> Ah ok
    [2020-07-15 13:09:02] <sarang> Please let us know when this happens Arc
    [2020-07-15 13:09:05] <sarang> ArticMine:
    [2020-07-15 13:09:06] <sarang> *
    [2020-07-15 13:09:20] <ArticMine> The basic idea is a dynamic penalty free zeon based upon the long term median
    [2020-07-15 13:09:52] <ArticMine> In any case I'll post here when issue 70 is updated
    [2020-07-15 13:10:03] <sarang> Great
    [2020-07-15 13:10:42] <sarang> I've been working on CLSAG, Triptych, and Arcturus this week
    [2020-07-15 13:11:12] <sarang> Hardware device support for CLSAG is proceeding nicely, and should be in place for the upgrade
    [2020-07-15 13:11:23] <sarang> Its preprint has been updated, and addresses reviewer recommendations
    [2020-07-15 13:11:33] <sarang> I have a blog post ready to go, as well
    [2020-07-15 13:11:42] <sarang> Triptych and Arcturus received small updates
    [2020-07-15 13:11:52] <sarang> Triptych was submitted to an ESORICS workshop
    [2020-07-15 13:12:15] <sarang> and Arcturus is still under consideration for PoPETs, though I've been working on an improved security model related to that used in Omniring
    [2020-07-15 13:12:25] <sarang> good times
    [2020-07-15 13:13:36] <sarang> There will be a developer meeting this Sunday at 17:00 UTC to discuss the upgrade timeline
    [2020-07-15 13:13:48] <sarang> Are there any questions on these topics?
    [2020-07-15 13:14:09] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-07-15 13:16:44] <sarang> OK, does anyone else wish to share any research topics of interest?
    [2020-07-15 13:17:59] <sgp_> super quick meeting
    [2020-07-15 13:18:09] <sarang> For sure
    [2020-07-15 13:18:31] <sarang> Well, if there aren't any other topics, we can move to ACTION ITEMS, anything people wish to share that they intend to tackle this week
    [2020-07-15 13:19:07] <sarang> I've been working on a bunch of ideas for improving the Omniring security model for use in Triptych/Arcturus, which has been a fun but frustrating challenge
    [2020-07-15 13:19:16] <sarang> as well as on-chain output analysis
    [2020-07-15 13:19:29] <sarang> These will continue this week!
    [2020-07-15 13:20:01] <sarang> As well as working with the CLSAG audit team to finalize their report for public release
    [2020-07-15 13:20:07] <sarang> Anyone else?
    [2020-07-15 13:21:33] <sarang> A super quick meeting indeed :D
    [2020-07-15 13:21:40] <sarang> All right, in that case, we can adjourn!
    [2020-07-15 13:21:44] <sarang> Thanks to everyone for attending
    [2020-07-15 13:21:50] <sarang> Logs will be posted to the GitHub agenda issue shortly


# Action History
- Created by: SarangNoether | 2020-07-09T13:05:48+00:00
- Closed at: 2020-07-15T17:24:21+00:00
