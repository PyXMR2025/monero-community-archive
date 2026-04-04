---
title: Nodes creating block templates that they will reject
source_url: https://github.com/monero-project/monero/issues/3717
author: zawy12
assignees: []
labels: []
created_at: '2018-04-27T18:41:51+00:00'
updated_at: '2018-06-05T11:32:58+00:00'
type: issue
status: closed
closed_at: '2018-06-05T11:32:58+00:00'
---

# Original Description
GraftNetwork experienced an interesting attack based on Cryptnote/Monero settings. It's described [here](https://github.com/graft-project/GraftNetwork/pull/118#issuecomment-384599435) and [here](https://github.com/graft-project/GraftNetwork/issues/116).   Basically a big miner mines a lot of blocks with timestamps set just below the FTL (future time limit of what nodes will accept as a valid timestamp).  He soon "owns the MTP" which means his forwarded timestamps become the basis of the MTP.  MTP = median time past.   If that falsified MTP is > current time, miners submitting blocks with timestamps from honest nodes will be rejected  **The pool or miner needs to change the timestamp to MTP+1 if current time is less than MTP.** ( This is what every clone should be correcting right now). He can then mine without competition for a few blocks.  Apparently honest miners can be locked out a lot of block if they do not request a new block template after the MTP starts being in the past of the node's clock.  

The attack can be performed on Monero with > 58% hash power applied for 35 blocks to briefly stop all miners and pools fro getting blocks accepted.  All clones are vulnerable, except those who had already lowered their FTL to 500 when getting their new marvelous DA. 

To perform the attack, and attacker needs a hashrate of about MTP/FTL + 0.5 multiplied by the baseline hashrate in order to do the attack, where MTP and FTL are in terms of the target solvetime. For Monero, MTP = (60+1)/2 and FTL = 60.  This is if the difficulty algorithm is slow like Monero's.  Difficulty algorithms that try to estimate current hashrate instead of the average of past 24 hours are much less vulnerable.

Someone has said "we do not consider > 51% attacks meaningful" but that's life on an hourly basis if you're not the biggest coin for a given POW.

But anyway, shouldn't nodes be prevented from handing out block templates that they will reject?

# Discussion History
## moneromooo-monero | 2018-04-28T09:28:55+00:00
The fix seems simple enough that even if it's a > 50% thing, it's worth applying I think.
Still, with > 50%, an adversary can obtain all blocks anyway.
Also, someone doing this once the patch is in can push the block times up to 2 hours in the future and keep it advancing there. This will cause some part of the network to reject some of the blocks as they're generated if they're running slow. This doesn't seem too bad since they'll soon accept them though.



## iamsmooth | 2018-04-28T15:51:39+00:00
I agree with this. Its isn't even only a 51% attack. If a mining node accidentally has its clock set too far back then it will uselessly mine auto-rejected blocks. Of course, that's the node operator's own fault but nevertheless it is a clear case of non-rational mining behavior. There is no reason to do this.

However, it seems to me the minimum adjustment that is sufficient would be to set the timestamp equal to the maximum of the median time and the current time, not the median time plus one. That's because the consensus code rejects blocks if their timestamp is below the median, but accepts if equal (someone please check if I'm missing something here).

In fact it seems to me a malicious miner could exploit this is the extra +1 is included. The exploit would be to set the MTL just below the FTL, perhaps a second or two. The malicious miner would not include the +1 (since consensus doesn't require it) but other nodes using the proposed fix would, and their blocks would be more likely to be rejected since the extra +1 means they are more likely to  violate FTL. 

Of course, we have veered into "is this actually worse than a usual 51% attack territory" here, but in any case I still don't see the need for the +1, nor the incentive for a rational miner to add it.

## zawy12 | 2018-04-28T16:10:45+00:00
I do not have any justification for the +1 other than it appearing Zcash may have it in their code.  But I think the attacker would have to get all 31 blocks in 1 second for this negative effect to occur, and the miner getting the +1 would have to do the solve in that same second.  The MTP is the attacker's oldest block out of the 31 needed, not newest.  @jagerman (the patch coder) also appears to be against the +1 on a similar basis of "why?"  

This does not address differences that occur from nodes not agreeing exactly on time (and they should not because they should not rely on a central oracle) and propagation delays. It seems like delays make the attack harder.

## iamsmooth | 2018-04-28T16:39:02+00:00
Yes, I agree it doesn't make a lot of difference in practice. As a miner, I wouldn't add 1, just because I don't see how it can possibly help me and it could possibly hurt me (even if unlikely).

If it had some generally beneficial effect, then it might be justified since the incentive to remove it is low, but I'm not sure what that beneficial effect would be either.

BTW, the attacker doesn't strictly need to solve the blocks in 1 second, they only need to solve the necessary number of blocks with the desired median and then have those blocks presented to the network at an acceptable time (once FTL has advanced). Since they control >50% they can always outpace the rest of the network.

Still, this doesn't make the difference not small.

I just looked and Bitcoin includes the +1, and it seems odd to see the same off-by-one error there too, so I guess maybe they have a reason.

## el00ruobuob | 2018-04-28T17:17:58+00:00
Just wondering: if I have let's say only a bit more than the 20% rejected outstanding timestamp and use a value just below the FTL, then I can have blocks validated, increase the MRL slowly, letting me increase my timestamp (according to the new FTL) and percentage of net hashpower more and more block after block, finally owning the MRL and gaining the 51% by invalidating legit miners one by one. Of course It would take a very long time, so countermeasure could be put in place before I manage to have the 51.
Does it make sense? I'm I wrong? 

## zawy12 | 2018-04-28T20:01:44+00:00
I was sort of suggesting the +1 second based on Zcash who apparently must have got it from BTC.  BTW where in the BTC code is it?   

## iamsmooth | 2018-04-28T20:29:12+00:00
https://github.com/bitcoin/bitcoin/blob/master/src/miner.cpp#L44

## str4d | 2018-04-28T22:34:36+00:00
I traced the `+1`'s current variant back to this commit: https://github.com/bitcoin/bitcoin/commit/5cbf75324d1509a1262b65c5073314a4da3f6d77#diff-118fcbaaba162ba17933c7893247df3aR3085

But it's been there from the very beginning: https://github.com/bitcoin/bitcoin/blob/e071a3f6c06f41068ad17134189a4ac3073ef76b/main.cpp#L2325

The reason is, in Bitcoin block timestamps must always increase relative to the MTP: https://github.com/bitcoin/bitcoin/blob/e071a3f6c06f41068ad17134189a4ac3073ef76b/main.cpp#L1205-L1207

## iamsmooth | 2018-04-28T22:38:01+00:00
Not actually monotonically increasing, just increasing relative to the MTP

But that is interesting and is different from Monero/cryptonote (which checks for < not <=).

https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp#L3135

I wonder if there is a reason requiring that form of increasing is useful. 

## moneromooo-monero | 2018-06-05T11:02:30+00:00
+resolved

# Action History
- Created by: zawy12 | 2018-04-27T18:41:51+00:00
- Closed at: 2018-06-05T11:32:58+00:00
