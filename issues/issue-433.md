---
title: E5-2620 Hash Rates
source_url: https://github.com/xmrig/xmrig/issues/433
author: kimats
assignees: []
labels:
- NUMA
created_at: '2018-03-08T09:42:51+00:00'
updated_at: '2019-08-02T12:51:08+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:51:08+00:00'
---

# Original Description
Is it normal?
I put 30 threads, since want leave 2 U for other things...

 * VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/5.4.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz (32) x64 AES-NI
 * CPU L2/L3:    256.0 MB/640.0 MB
 * THREADS:      30, cryptonight, av=1, donate=1%
 * POOL #1:      Pool.DERO.CryptoPool.Space:3333
 * COMMANDS:     hashrate, pause, resume
[2018-03-08 17:38:23] use pool Pool.DERO.CryptoPool.Space:3333 198.13.58.131
[2018-03-08 17:38:23] new job from Pool.DERO.CryptoPool.Space:3333 diff 10000
[2018-03-08 17:38:26] accepted (1/0) diff 10000 (106 ms)
[2018-03-08 17:38:33] accepted (2/0) diff 10000 (69 ms)
[2018-03-08 17:39:07] new job from Pool.DERO.CryptoPool.Space:3333 diff 13636
[2018-03-08 17:39:27] speed 2.5s/60s/15m 422.8 432.2 n/a H/s max: 459.6 H/s
[2018-03-08 17:40:07] new job from Pool.DERO.CryptoPool.Space:3333 diff 5769
[2018-03-08 17:40:16] accepted (3/0) diff 5769 (68 ms)
[2018-03-08 17:40:27] accepted (4/0) diff 5769 (67 ms)
[2018-03-08 17:40:27] speed 2.5s/60s/15m 404.6 435.6 n/a H/s max: 459.6 H/s
[2018-03-08 17:40:33] accepted (5/0) diff 5769 (68 ms)
[2018-03-08 17:41:00] accepted (6/0) diff 5769 (67 ms)


# Discussion History
## kimats | 2018-03-08T13:42:15+00:00
by make the thread from 30 to 18, i got 750H/s

## 2010phenix | 2018-03-10T11:58:55+00:00
with CPU L2/L3: 256.0 MB/640.0 MB
if real correct detect L3 you can have much more thread...

## Zelecktor | 2018-03-10T15:37:11+00:00
its a server?

## guigeddos | 2018-03-17T04:50:35+00:00
32 E5-2620？？512thread

## xmrig | 2019-08-02T12:51:08+00:00
#1077 

# Action History
- Created by: kimats | 2018-03-08T09:42:51+00:00
- Closed at: 2019-08-02T12:51:08+00:00
