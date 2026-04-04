---
title: Fresh fullnode does not sync
source_url: https://github.com/monero-project/monero/issues/8209
author: taoeffect
assignees: []
labels: []
created_at: '2022-03-07T17:09:07+00:00'
updated_at: '2022-03-09T19:26:31+00:00'
type: issue
status: closed
closed_at: '2022-03-09T19:26:31+00:00'
---

# Original Description
I tried setting up a monero node on Linux VPS with 0.17.3.0.

It started fast, and then quickly slowed down. It went from saying it would take ~1 to 2 days to fully sync, to now, at block 509704, saying it will take over 11 months to sync.

The Monero website says:

> It is typically much faster to sync from scratch

<img width="960" alt="Screen Shot 2022-03-07 at 9 07 07 AM" src="https://user-images.githubusercontent.com/138706/157082745-594bb5fb-fb85-40dd-9f2a-a314a264f44f.png">
 
Clearly this isn't true. I don't see it ever finishing, which is a big deal as it means no new nodes can come online. No errors are shown in the console. It remains slow even when run with `--out-peers 40 --in-peers 40`.

Is  this a bug in Monero or is it an attack on the network?

# Discussion History
## selsta | 2022-03-07T18:09:29+00:00
What hardware do you have? Where is the blockchain stored? (HDD / SSD / network drive)


## taoeffect | 2022-03-07T20:46:35+00:00
Intel E5 (2.3GHz+) w/RAID5 or RAID10 HDD. I'm pretty sure the server specs are not the bottleneck here, as it seems even a single block takes long to fetch.

## taoeffect | 2022-03-07T20:57:44+00:00
*I shut down the node, and shut down another process that was also writing to the hard drive a lot, and now it seems to have sped up a bit. Down to "4.5 months left" according to a recent message... so I guess that's progress, but it still seems a bit slow, and I'm guessing definitely slower than an import. So my next step will be to try to do the import... which I'm guessing wasn't the ideal setup of how you guys envision this sync to take place.

## selsta | 2022-03-07T20:59:12+00:00
>  and I'm guessing definitely slower than an import

How do you know that? The slow part is the verification process, not the download process. If your HDD is slow then both will take a while. SSD is recommended for a fast sync.

Try to let it run for a bit and see how it proceeds.

## taoeffect | 2022-03-09T19:26:31+00:00
OK, the blockchain-import was also very slow, so maybe that's the bottleneck. I've resumed syncing it and it's down to saying "4.4 days left", which is annoying but not hopeless, so closing for now.

# Action History
- Created by: taoeffect | 2022-03-07T17:09:07+00:00
- Closed at: 2022-03-09T19:26:31+00:00
