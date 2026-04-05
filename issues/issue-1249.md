---
title: Continue to mine just for heating without submitting share
source_url: https://github.com/xmrig/xmrig/issues/1249
author: oliverlj
assignees: []
labels: []
created_at: '2019-10-19T06:48:57+00:00'
updated_at: '2021-04-12T15:31:50+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:31:50+00:00'
---

# Original Description
After few days, xmrig continue to mine without job

Start of xmrig

`[2019-10-06 08:36:18.275] SIGHUP received, exiting
 * ABOUT        XMRig/4.2.1-beta gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * CPU          Intel(R) Pentium(R) CPU G4600 @ 3.60GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo cn/r
 * OPENCL       disabled
 * COMMANDS     hashrate, pause, resume
[2019-10-06 08:36:23.622] use pool pool.supportxmr.com:3333  91.121.140.167
[2019-10-06 08:36:23.622] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1938553
[2019-10-06 08:36:23.622]  cpu  use profile  cn  (2 threads) scratchpad 2048 KB
[2019-10-06 08:36:24.577]  cpu  READY threads 2/2 (2) huge pages 2/2 100% memory 4096 KB (954 ms)
[2019-10-06 08:37:23.693] speed 10s/60s/15m 59.9 n/a n/a H/s max 60.5 H/s
[2019-10-06 08:37:50.838] accepted (1/0) diff 10000 (72 ms)
[2019-10-06 08:38:01.828] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1938553
[2019-10-06 08:38:16.757] accepted (2/0) diff 10000 (59 ms)
[2019-10-06 08:38:23.805] speed 10s/60s/15m 58.2 58.7 n/a H/s max 60.5 H/s
[2019-10-06 08:39:02.016] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1938553
`

After few days :
`[2019-10-14 23:44:24.307] speed 10s/60s/15m 64.6 64.6 64.4 H/s max 78.2 H/s
[2019-10-14 23:45:00.893] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1944741
[2019-10-14 23:45:24.362] speed 10s/60s/15m 64.6 64.5 64.3 H/s max 78.2 H/s
[2019-10-14 23:46:01.009] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1944741
[2019-10-14 23:46:24.398] speed 10s/60s/15m 64.6 64.7 64.3 H/s max 78.2 H/s
[2019-10-14 23:47:01.111] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1944741
[2019-10-14 23:47:24.430] speed 10s/60s/15m 64.4 64.3 64.3 H/s max 78.2 H/s
[2019-10-14 23:48:01.220] new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1944741
[2019-10-14 23:48:24.466] speed 10s/60s/15m 64.6 64.5 64.3 H/s max 78.2 H/s
[2019-10-14 23:49:24.511] speed 10s/60s/15m 64.1 64.4 64.3 H/s max 78.2 H/s
[2019-10-14 23:50:24.551] speed 10s/60s/15m 64.7 64.6 64.2 H/s max 78.2 H/s
[2019-10-14 23:51:24.592] speed 10s/60s/15m 64.5 64.5 64.6 H/s max 78.2 H/s
[2019-10-14 23:52:24.635] speed 10s/60s/15m 64.7 64.7 64.6 H/s max 78.2 H/s
[2019-10-14 23:53:24.676] speed 10s/60s/15m 64.2 64.5 64.6 H/s max 78.2 H/s
[2019-10-14 23:54:24.716] speed 10s/60s/15m 64.8 64.6 64.6 H/s max 78.2 H/s
[2019-10-14 23:55:24.757] speed 10s/60s/15m 64.8 64.6 64.6 H/s max 78.2 H/s
[2019-10-14 23:56:24.806] speed 10s/60s/15m 64.6 64.5 64.6 H/s max 78.2 H/s
`

Until I stop the miner, and supportxmr tell me 0h.

my connection is not stable, i'm on lte internet network

# Discussion History
# Action History
- Created by: oliverlj | 2019-10-19T06:48:57+00:00
- Closed at: 2021-04-12T15:31:50+00:00
