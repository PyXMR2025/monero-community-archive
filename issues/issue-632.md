---
title: no active pools and connection reset by peer xmrig 2.6.2
source_url: https://github.com/xmrig/xmrig/issues/632
author: LiStopaD45
assignees: []
labels: []
created_at: '2018-05-16T17:51:34+00:00'
updated_at: '2018-06-17T18:01:45+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:01:45+00:00'
---

# Original Description
Hi! I use xmrig 2.6.2 (on Windows 10 and Ubuntu 16.04). Maynera work through xmrig-proxy. I constantly see a mistake or "no active pools, stop mining" or "read error: connection reset by peer". Mistakes arise often (from 7 to 15 minutes). 
By one car xmrig and xmrig-nvidia is started. But xmrig-nvidia doesn't report these mistakes. 
Xmrig 2.5 versions didn't create such problems.
In what can be a reason? I ask for your help.

# Discussion History
## xmrig | 2018-05-17T04:13:15+00:00
Please show full logs.
Thank you.

## LiStopaD45 | 2018-05-17T07:40:53+00:00
I have to provide a log of information output in a miner?

## LiStopaD45 | 2018-05-17T17:47:59+00:00
This my miner on Win 10:

```
2018-05-17 14:53:56] new job from pool:443 diff 49590 algo cn/1
[2018-05-17 15:02:02] [pool:443] read error: "connection reset by peer"
[2018-05-17 15:02:02] no active pools, stop mining
[2018-05-17 15:02:07] use pool pool:443 ippool
[2018-05-17 15:02:07] new job from pool:443 diff 49590 algo cn/1
[2018-05-17 15:03:36] speed 2.5s/60s/15m 122.0 120.3 84.7 H/s max: 150.8 H/s
[2018-05-17 15:04:00] new job from pool:443 diff 49590 algo cn/1
[2018-05-17 15:13:36] speed 2.5s/60s/15m 121.7 116.6 109.6 H/s max: 150.8 H/s
[2018-05-17 15:22:25] [pool:443] read error: "connection reset by peer"
[2018-05-17 15:22:25] no active pools, stop mining
[2018-05-17 15:22:31] use pool pool:443 ippool
[2018-05-17 15:22:31] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:23:23] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:23:36] speed 2.5s/60s/15m 121.7 109.8 112.3 H/s max: 150.8 H/s
[2018-05-17 15:23:56] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:24:06] accepted (46/0) diff 49560 (60 ms)
[2018-05-17 15:24:53] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:26:00] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:27:39] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:33:36] speed 2.5s/60s/15m 123.5 123.6 115.8 H/s max: 150.8 H/s
[2018-05-17 15:43:36] speed 2.5s/60s/15m 102.5 113.8 122.1 H/s max: 150.8 H/s
[2018-05-17 15:52:06] dev donate started
[2018-05-17 15:52:06] new job from miner.fee.xmrig.com:6666 diff 100001 algo cn/1
[2018-05-17 15:53:06] dev donate finished
[2018-05-17 15:53:06] new job from pool:443 diff 49560 algo cn/1
[2018-05-17 15:53:07] [pool:443] read error: "connection reset by peer"
[2018-05-17 15:53:07] no active pools, stop mining
[2018-05-17 15:53:12] use pool pool:443 ippool
[2018-05-17 15:53:12] new job from pool:443 diff 49500 algo cn/1
[2018-05-17 15:53:36] speed 2.5s/60s/15m 116.5 98.9 115.1 H/s max: 150.8 H/s
[2018-05-17 15:54:06] new job from pool:443 diff 49500 algo cn/1
[2018-05-17 15:54:20] new job from pool:443 diff 49530 algo cn/1
[2018-05-17 15:54:47] new job from pool:443 diff 49530 algo cn/1
[2018-05-17 15:55:24] new job from pool:443 diff 49530 algo cn/1
[2018-05-17 16:03:36] speed 2.5s/60s/15m 124.2 122.6 107.0 H/s max: 150.8 H/s
```
I have tried to start xmrig 2.5.2 on one computer. I will look at statistics of refusals of this version. There has passed hour, but I don't see a niodny error of connection. I will wait more time.

## LiStopaD45 | 2018-05-18T13:49:15+00:00
I have made an experiment. Version 2.5.2 doesn't give mistakes. Version 2.6.2 of a mistake gives.

## RipZ | 2018-05-18T14:11:02+00:00
try to set custom_diff for workers eq 25000. It's helped me to get rid of messages about lost connections to pool and etc

## LiStopaD45 | 2018-05-21T19:16:52+00:00
I have upgraded to the xmrig 2.5.2 version anew. I on a proxy have set the simple mode. I don't see mistakes in xmrig any more. I tested version 2.5.2 and 2.6.2. I assume that at a proxy operating mode by default the miner fell off on a timeout.

# Action History
- Created by: LiStopaD45 | 2018-05-16T17:51:34+00:00
- Closed at: 2018-06-17T18:01:45+00:00
