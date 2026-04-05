---
title: Resuming from a long pause results in a very low starting difficulty
source_url: https://github.com/xmrig/xmrig/issues/1673
author: bennytehcat
assignees: []
labels:
- question
created_at: '2020-05-08T20:04:07+00:00'
updated_at: '2020-08-28T16:39:48+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:39:48+00:00'
---

# Original Description
It seems that based on the length of a pause the starting difficulty decreases.  Meaning, if you join a server with a starting difficulty of 50000 (appropriate for your hardware), then pause for 30 minutes, and resume, xmrig will not pickup on the server suggested difficulty, or the previously calculated difficulty.  Instead it drops to something like 300.

I've found this to be true on all versions from 5.07 to 5.11, noted on W10 LTSC machines with intel i-series and xeon CPU.  



# Discussion History
## xmrig | 2020-05-08T20:17:16+00:00
When pause, the miner not close connection to a pool, so pool reduces difficulty because miner not submitted shares, you can use fixed difficulty if pool support it.
Thank you.

# Action History
- Created by: bennytehcat | 2020-05-08T20:04:07+00:00
- Closed at: 2020-08-28T16:39:48+00:00
