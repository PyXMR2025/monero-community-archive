---
title: Mining error please fix it
source_url: https://github.com/xmrig/xmrig/issues/2687
author: asumas
assignees: []
labels: []
created_at: '2021-11-12T07:39:55+00:00'
updated_at: '2021-11-16T23:27:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

 * ABOUT        XMRig/6.12.1 MSVC/2019

 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1

 * HUGE PAGES   unavailable

 * 1GB PAGES    unavailable

 * CPU          Intel(R) Core(TM) i3-1005G1 CPU @ 1.20GHz (1) 64-bit AES

                L2:1.0 MB L3:4.0 MB 2C/4T NUMA:1

 * MEMORY       2.1/3.7 GB (56%)

                Bottom - Slot 1 (left): <empty>

                Bottom - Slot 2 (right): 4 GB DDR4 @ 3200 MHz HMA851S6DJR6N-XN    

 * MOTHERBOARD  HP - 86C9

 * DONATE       1%

 * ASSEMBLY     auto:intel

 * POOL #1      rx.unmineable.com:3333 algo rx/0

 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection

 * HTTP API     127.0.0.1:60070 

 * OPENCL       disabled

 * CUDA         disabled

[2021-11-12 14:31:37.899]  net      use pool rx.unmineable.com:3333  139.59.102.100

[2021-11-12 14:31:37.899]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491500

[2021-11-12 14:31:37.899]  cpu      use argon2 implementation AVX-512F

[2021-11-12 14:31:37.900]  msr      to access MSR registers Administrator privileges required.

[2021-11-12 14:31:37.900]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

[2021-11-12 14:31:37.900]  randomx  init dataset algo rx/0 (4 threads) seed c7743ee59c670469...

[2021-11-12 14:31:37.900]  randomx  fast RandomX mode disabled by config

[2021-11-12 14:31:37.900]  randomx  failed to allocate RandomX dataset, switching to slow mode (0 ms)

[2021-11-12 14:31:38.265]  randomx  dataset ready (365 ms)

[2021-11-12 14:31:38.265]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB

[2021-11-12 14:31:38.279]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (14 ms)

[2021-11-12 14:31:38.716]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491500

[2021-11-12 14:31:53.735]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491500

[2021-11-12 14:32:08.778]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491500

[2021-11-12 14:32:13.586]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491501

[2021-11-12 14:32:23.700]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491501

[2021-11-12 14:32:38.665]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491501

[2021-11-12 14:32:39.142]  miner    speed 10s/60s/15m 88.01 79.72 n/a H/s max 90.98 H/s

[2021-11-12 14:33:08.714]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2491501

# Discussion History
## Spudz76 | 2021-11-12T07:46:30+00:00
You need another 4GB stick.  One stick is slow.  Slow mode (due to not enough memory) is even slower.

RandomX needs 2.1GB free to even begin working in fast mode.

## asumas | 2021-11-12T07:54:42+00:00
Is this an error because I did not receive the coin

## Spudz76 | 2021-11-12T08:04:32+00:00
Well that pool has a fixed diff of 100001 which is for hashrates of at minimum 3333.366666667H/s

Even working correctly with enough RAM, [that CPU scores 1260H/s](https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i3-1005G1+CPU+%40+1.20GHz) so that pool will not be ideal.  Probably at current broken slow-mode and no-dual-channel-memory rate of 90H/s you would never get any accepts.

Use a better pool that has autodiff or selectable diff and allows down to 37800 diff (1260 * 30), and fix your lack of RAM so it can run normal fast mode.  I would suggest MoneroOcean since then that weak CPU can run other algos and still be paid out in XMR.  It would score more pay equivalence than 1260H/s running probably astrobwt algo which can use all 4 threads.

## asumas | 2021-11-12T08:19:46+00:00
so what should i do to get my salary i cant upgrade ram i am mining with unMineable on unMineable wed i check but not get mining info while their tool is still running on my machine

## netsbot | 2021-11-15T12:53:38+00:00
You should use another pool

## asumas | 2021-11-16T00:38:12+00:00
@suckma420 do you know a pool that i can mine?

## windows11sucks | 2021-11-16T00:40:18+00:00
I personally mines on MoneroOcean but they ban botnets so you should use a proxy or use 2miners

## asumas | 2021-11-16T23:27:21+00:00
@windows11sucks I'm mining on minerxmr.com follow you there ok no the speed is more stable than 2miner I mine but I don't know if it's reputable anymore

# Action History
- Created by: asumas | 2021-11-12T07:39:55+00:00
