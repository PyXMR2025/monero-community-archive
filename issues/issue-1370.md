---
title: Slow Crash on 5.1.0 - Memory Leakage??
source_url: https://github.com/xmrig/xmrig/issues/1370
author: NCarter84
assignees: []
labels:
- bug
- stability
created_at: '2019-12-02T20:39:07+00:00'
updated_at: '2020-08-31T05:49:05+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:49:04+00:00'
---

# Original Description
Ryzen Rig - Windows 1903, 12 gb RAM, running XMRIG 5.1

5 different times - the miner has been "shut off/closed" - GPU miners still running, no issue. I've fallen back to 5.0 and have been stable for 2 hours now... 

Also, Intel CPU, i7 xxx 16 GB RAM, Running XMRIG 5.1

Logged into PC to find a slow decrease in mining speed over time.. Went from 1.9 khs down to under 500 hs... Restarted miner, back to 1.9 khs

# Discussion History
## JeffreyChu2009 | 2019-12-03T01:21:15+00:00
Similar crashing issues for the radical 5.1.0 version on TR2920X@3.9GHz with 64GB DDR4-3200@2933 system.
Using back to 5.0.1-- even though the hashrate is about 3% lower than the latest version.

## FabioFrmg | 2019-12-03T14:47:48+00:00
Similar issue here. 
Most of my miners auto shutdown after a few minutes mining with V5.1.0

## xmrig | 2019-12-04T10:42:28+00:00
v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.
Thank you.

## NCarter84 | 2019-12-05T02:58:38+00:00
Has not been fixed. Ran for under 3 hours prior to shutting down at unknown time.

Only tested on Ryzen rig.

## xmrig | 2020-08-31T05:49:04+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: NCarter84 | 2019-12-02T20:39:07+00:00
- Closed at: 2020-08-31T05:49:04+00:00
