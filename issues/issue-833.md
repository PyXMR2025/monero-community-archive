---
title: Increased CPU usage in latest version
source_url: https://github.com/monero-project/monero/issues/833
author: bobfeldbauer
assignees: []
labels: []
created_at: '2016-05-04T03:42:08+00:00'
updated_at: '2016-07-07T20:01:25+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:01:24+00:00'
---

# Original Description
Building from source at current head (8b0d22a2aa5f4a1539f40e276feca3b1879924eb) on Linux results in bitmonerod showing a 5-10x increase in CPU usage at times, compared to the last build I was running from March 28 (0ee87e63050c31405182042868a89d4f3f3ac7c2). Nothing else has changed, there hasn't been any increase in outgoing transactions or mining activity, etc.

bitmonerod is being used for pool mining, nothing changed on the pool side of things and the increase in frequency of high CPU spikes was seen starting immediately after the upgrade. It doesn't occur all the time, but is very frequent and spikes for 'minutes' to 500-600% cpu. Normal cpu usage for bitmonerod would be around 80% typically both before and after the update.

The increased CPU usage doesn't seem related to anything in particular and I haven't identified a cause. I'm happy to provide more information or help track down the issue, but I'm going to need a place to start though.


# Discussion History
## fluffypony | 2016-05-04T07:18:01+00:00
Couple of questions:
1. 32-bit or 64-bit Linux?
2. How much RAM on that box?
3. Spinning disk or SSD?

Thanks for reporting this!


## bobfeldbauer | 2016-05-04T07:24:10+00:00
It's a physical server with 48GB RAM, 64-bit Debian Jessie, at least 8GB RAM free, SSD.


## moneromooo-monero | 2016-05-04T07:24:20+00:00
Try reverting 4cfb4dff3e8ae213cc87b2d0234a519d2e8674b7


## bobfeldbauer | 2016-05-04T07:51:48+00:00
I reverted the changes in 4cfb4dff3e8ae213cc87b2d0234a519d2e8674b7 and am no longer seeing the issue. I'll monitor it for the next 12 hours to be certain, and then post an update here.


## bobfeldbauer | 2016-05-04T16:52:11+00:00
I can confirm now that reverting the changes in 4cfb4dff3e8ae213cc87b2d0234a519d2e8674b7 did resolve this.


## moneromooo-monero | 2016-05-04T16:59:55+00:00
Another interesting test would be to use 4cfb4df again, and apply https://github.com/monero-project/bitmonero/pull/810 and compare CPU usage.


## bobfeldbauer | 2016-05-04T17:02:56+00:00
Sure, let me merge that all together and see how it goes - will update in a few hours with results.


## bobfeldbauer | 2016-05-05T07:32:50+00:00
Adding https://github.com/monero-project/bitmonero/pull/810 to the current Github master HEAD 8b0d22a2aa5f4a1539f40e276feca3b1879924eb does appear to eliminate the spikes I described in this issue, and also reduces typical CPU usage by nearly an order of magnitude (when used as a wallet for a mining pool).


## iamsmooth | 2016-05-16T02:20:39+00:00
Given the discussion in the last dev meeting, our overall suggestion is probably going to be to improve the pool software so it doesn't constantly request new templates for no good reason (check the last block hash instead, which is very low overhead, and only get a new template when that changes or when enough time has passed). While you are free to use #810 if you maintain your own fork of the daemon, it probably won't be merged.


## iamsmooth | 2016-05-16T03:00:36+00:00
Looking back at 4cfb4df I think we could salvage the input validity cache if we cleared it after each block or possibly after any reorg. That might still be sufficient to reduce most of the increased overhead (which comes from repeated verification during different stages of processing) without the issue of validity cache staleness


## fluffypony | 2016-07-07T20:01:24+00:00
Closing as wontfix


# Action History
- Created by: bobfeldbauer | 2016-05-04T03:42:08+00:00
- Closed at: 2016-07-07T20:01:24+00:00
