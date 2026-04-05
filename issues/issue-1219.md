---
title: AMD Opteron(TM) Processor 6272 (4) Windows Server 2016 x64 low hashrate
source_url: https://github.com/xmrig/xmrig/issues/1219
author: duku1
assignees: []
labels: []
created_at: '2019-10-04T11:23:46+00:00'
updated_at: '2019-10-04T13:35:26+00:00'
type: issue
status: closed
closed_at: '2019-10-04T13:07:16+00:00'
---

# Original Description
Hi, what wrong? I have 2 times less hashrate than I can see in test from others.

* ABOUT XMRig/4.2.1-beta gcc/9.2.0
    LIBS libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
    HUGE PAGES permission granted
    CPU AMD Opteron(TM) Processor 6272 (4) x64 AES
    L2:64.0 MB L3:48.0 MB 32C/64T NUMA:8
    DONATE 1%
    ASSEMBLY auto:bulldozer
    POOL #1 pool.loki.hashvault.pro:3333 algo auto
    COMMANDS hashrate, pause, resume
    OPENCL disabled
    [2019-10-04 14:07:58.210] use pool pool.loki.hashvault.pro:3333 193.164.16.124
    [2019-10-04 14:07:58.210] new job from pool.loki.hashvault.pro:3333 diff 30000 algo rx/loki height 373018
    [2019-10-04 14:07:58.226] rx init datasets algo rx/loki (6 threads) seed e3e6be0bc7258fd7...
    [2019-10-04 14:07:58.241] rx #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
    [2019-10-04 14:07:58.273] rx #0 allocate done huge pages 1168/1168 100% +JIT (39 ms)
    [2019-10-04 14:08:00.007] new job from pool.loki.hashvault.pro:3333 diff 56250 algo rx/loki height 373018
    [2019-10-04 14:08:12.788] rx #0 init done 1/8 (14556 ms)
   ...
    [2019-10-04 14:09:40.461] rx #7 allocate 2336 MB (2080+256) for RandomX dataset & cache
    [2019-10-04 14:09:40.492] rx #7 allocate done huge pages 1168/1168 100% +JIT (42 ms)
    [2019-10-04 14:09:55.367] rx #7 init done 8/8 (14920 ms)
    [2019-10-04 14:09:55.367] cpu use profile rx (56 threads) scratchpad 2048 KB
    [2019-10-04 14:09:55.398] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373018
    [2019-10-04 14:09:55.414] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373018
    [2019-10-04 14:09:55.414] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373019
    [2019-10-04 14:09:55.414] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373020
    [2019-10-04 14:09:55.555] cpu READY threads 56/56 (56) huge pages 56/56 100% memory 114688 KB (188 ms)
    [2019-10-04 14:10:00.023] new job from pool.loki.hashvault.pro:3333 diff 24999 algo rx/loki height 373020
    [2019-10-04 14:10:00.461] accepted (1/0) diff 24999 (46 ms)
    ...
    [2019-10-04 14:10:54.008] accepted (17/0) diff 24999 (34 ms)
    [2019-10-04 14:10:55.946] speed 10s/60s/15m 4486.4 4481.5 n/a H/s max 4494.1 H/s

# Discussion History
## xmrig | 2019-10-04T11:38:29+00:00
How many memory sticks installed? in addition please provide result of `xmrig.exe --export-topology`.
Thank you.

## duku1 | 2019-10-04T11:49:34+00:00
8x4gb ram
I`m try install Ubuntu and check hashrate.

## xmrig | 2019-10-04T12:09:49+00:00
You need check memory configuration carefully, each NUMA node (CPU die, 2 per package) should have memory installed, it very important.

## duku1 | 2019-10-04T13:06:57+00:00
Yes. you was right. Memory works in single mode.
now in Windows 8386h

# Action History
- Created by: duku1 | 2019-10-04T11:23:46+00:00
- Closed at: 2019-10-04T13:07:16+00:00
