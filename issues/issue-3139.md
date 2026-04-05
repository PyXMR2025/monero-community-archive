---
title: Rejected shares show up as accepted in p2pool
source_url: https://github.com/xmrig/xmrig/issues/3139
author: pranshuthegamer
assignees: []
labels: []
created_at: '2022-10-18T19:08:28+00:00'
updated_at: '2022-10-18T19:28:37+00:00'
type: issue
status: closed
closed_at: '2022-10-18T19:28:37+00:00'
---

# Original Description
**Describe the bug**
Whenever i see a share that is rejected in xmrig, it accepts that share in p2pool
and any share that is accepted shows up with "couldnt get pow hash" error

**To Reproduce**
install p2pool-2.4-1  xmrig-6.18.0-1 on arch linux
p2pool is running with a public p2pool node

**Expected behavior**
accepted share should be accepted
rejected should be reejcted

**Required data**
 - Miner log as text or screenshot
 ```
  sudo xmrig -o 127.0.0.1:3333 -u x+50000
 * ABOUT        XMRig/6.18.0 gcc/12.1.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1p hwloc/2.8.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 5 5600H with Radeon Graphics (1) 64-bit AES
                L2:3.0 MB L3:16.0 MB 6C/12T NUMA:1
 * MEMORY       4.7/7.1 GB (67%)
                Bottom - Slot 1 (left): 8 GB DDR4 @ 3200 MHz M471A1K43EB1-CWE
                Bottom - Slot 2 (right): <empty>
 * MOTHERBOARD  HP - 88DD
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      127.0.0.1:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-10-18 22:02:07.200]  net      use pool 127.0.0.1:3333  127.0.0.1
[2022-10-18 22:02:07.200]  net      new job from 127.0.0.1:3333 diff 50001 algo rx/0 height 2736376 (1 tx)
[2022-10-18 22:02:07.200]  cpu      use argon2 implementation AVX2
[2022-10-18 22:02:07.201]  msr      register values for "ryzen_19h" preset have been set successfully (0 ms)
[2022-10-18 22:02:07.201]  randomx  init dataset algo rx/0 (12 threads) seed 1da30c750a9c3f9c...
[2022-10-18 22:02:07.512]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (311 ms)
[2022-10-18 22:02:10.198]  randomx  dataset ready (2686 ms)
[2022-10-18 22:02:10.198]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2022-10-18 22:02:10.204]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (6 ms)
[2022-10-18 22:02:21.531]  cpu      rejected (0/1) diff 50001 "Couldn't check PoW" (114 ms)
[2022-10-18 22:02:24.365]  cpu      rejected (0/2) diff 50001 "Couldn't check PoW" (121 ms)
[2022-10-18 22:02:33.668]  cpu      accepted (1/2) diff 50001 (1 ms)
[2022-10-18 22:02:41.860]  cpu      rejected (1/3) diff 50001 "Couldn't check PoW" (113 ms)
[2022-10-18 22:02:47.211]  cpu      accepted (2/3) diff 50001 (0 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   673.5 |     n/a |     n/a |
|        1 |        2 |   679.0 |     n/a |     n/a |
|        2 |        4 |   677.9 |     n/a |     n/a |
|        3 |        6 |   672.0 |     n/a |     n/a |
|        4 |        8 |   543.2 |     n/a |     n/a |
|        5 |       10 |   542.2 |     n/a |     n/a |
|        6 |        9 |   484.7 |     n/a |     n/a |
|        7 |       11 |   483.0 |     n/a |     n/a |
|        - |        - |  4755.6 |     n/a |     n/a |
[2022-10-18 22:02:47.483]  miner    speed 10s/60s/15m 4755.6 n/a n/a H/s max 4770.1 H/s
[2022-10-18 22:02:49.299]  cpu      rejected (2/4) diff 50001 "Couldn't check PoW" (114 ms)
[2022-10-18 22:02:52.972]  cpu      rejected (2/5) diff 50001 "Couldn't check PoW" (113 ms)
[2022-10-18 22:02:58.889]  net      new job from 127.0.0.1:3333 diff 50001 algo rx/0 height 2736377 (11 tx)
[2022-10-18 22:03:07.062]  cpu      rejected (2/6) diff 50001 "Couldn't check PoW" (115 ms)
[2022-10-18 22:03:08.118]  cpu      accepted (3/6) diff 50001 (0 ms)
[2022-10-18 22:03:10.240]  miner    speed 10s/60s/15m 3764.2 n/a n/a H/s max 4770.1 H/s
[2022-10-18 22:03:20.825]  cpu      accepted (4/6) diff 50001 (0 ms)
[2022-10-18 22:03:25.409]  cpu      rejected (4/7) diff 50001 "Couldn't check PoW" (113 ms)
[2022-10-18 22:03:32.573]  cpu      accepted (5/7) diff 50001 (0 ms)
[2022-10-18 22:03:44.364]  net      new job from 127.0.0.1:3333 diff 50001 algo rx/0 height 2736378 (5 tx)
[2022-10-18 22:03:44.796]  cpu      accepted (6/7) diff 50001 (0 ms)
[2022-10-18 22:03:51.020]  cpu      rejected (6/8) diff 50001 "Couldn't check PoW" (115 ms)
[2022-10-18 22:03:53.991]  cpu      rejected (6/9) diff 50001 "Couldn't check PoW" (113 ms)
[2022-10-18 22:04:08.429]  net      127.0.0.1:3333 read error: "end of file"
[2022-10-18 22:04:08.429]  net      no active pools, stop mining
[2022-10-18 22:04:10.276]  miner    speed 10s/60s/15m 3359.9 3982.1 n/a H/s max 4770.1 H/s
[2022-10-18 22:04:10.684]  signal   Ctrl+C received, exiting
[2022-10-18 22:04:10.705]  cpu      stopped (20 ms)
```

 - Config file or command line (without wallets)
 no config
 - OS: [e.g. Windows]
 arch linux


# Discussion History
## pranshuthegamer | 2022-10-18T19:28:37+00:00
sorry dumb mistake
ran p2pool with --no-randomx

# Action History
- Created by: pranshuthegamer | 2022-10-18T19:08:28+00:00
- Closed at: 2022-10-18T19:28:37+00:00
