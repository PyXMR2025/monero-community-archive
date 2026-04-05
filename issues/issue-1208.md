---
title: How to increase cpu usage?
source_url: https://github.com/xmrig/xmrig/issues/1208
author: BluCobalt
assignees: []
labels:
- question
created_at: '2019-09-30T04:10:20+00:00'
updated_at: '2019-09-30T22:17:05+00:00'
type: issue
status: closed
closed_at: '2019-09-30T21:57:12+00:00'
---

# Original Description
ok, so, I have a server, and I want to utilize it for monero. after a while, I finally got xmrig working. however, the cpu usage would never go above ~50%. I want to use the server to its full potential, how do I do that? thank you for this awesome miner btw!

# Discussion History
## xmrig | 2019-09-30T09:00:42+00:00
Usually performance limited by L3 cache, not by cores/threads, miner should generate perfect configuration for physical hardware. In addition future RandomX also limited by L2 cache and memory (DDR3 /DDR4, channels count, etc), but memory not directly affect generated configuration.
Thank you.

## BluCobalt | 2019-09-30T14:49:27+00:00
So would 24mb of l3 not be enough to reach 100%? My server has 2x2560's and 48 gbs of ram if that helps. (I'm totally upping my donation time to like 8 minutes for that super quick response btw)

## xmrig | 2019-09-30T18:35:21+00:00
Perhaps you talking about E5-2650 v3, this CPU can run 12 threads (25 / 2 = 12) on current 2 MB scratchpad size cryptonight algorithms and 10 threads (limited by L2 cache) on RandomX, so 24 or 20 threads for pair it's already full potential.
Thank you.

## BluCobalt | 2019-09-30T21:57:09+00:00
I was wrong, I actually meant 2x x5650 6 cores Both at 2.66 ghz, but yeah, you're the one who made it, and I'm just some kid on the internet, thanks anyways though for the help

## xmrig | 2019-09-30T22:17:05+00:00
Same rules apply but CPU limited both by L2 and L3 cache to 6 threads.

# Action History
- Created by: BluCobalt | 2019-09-30T04:10:20+00:00
- Closed at: 2019-09-30T21:57:12+00:00
