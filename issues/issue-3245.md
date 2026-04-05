---
title: crashed dag file after donate.ssl.xmrig.com
source_url: https://github.com/xmrig/xmrig/issues/3245
author: newsmoneymaker
assignees: []
labels:
- bug
- kawpow
created_at: '2023-04-07T08:41:19+00:00'
updated_at: '2023-06-07T14:57:27+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:57:27+00:00'
---

# Original Description
Hello, crashed dag file after donate.ssl.xmrig.com, in order for the miner to work again, you need to restart

```
[2023-04-07 11:22:33.133]  nvidia   accepted (120/1) diff 43118K (103 ms)
[2023-04-07 11:22:35.434]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305579
[2023-04-07 11:23:09.468]  nvidia   #0 02:00.0   0W 74C 139/3504 MHz
[2023-04-07 11:23:09.468]  miner    speed 10s/60s/15m 0.73 0.72 0.65 MH/s max 1.27 MH/s
[2023-04-07 11:23:24.551]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305580
[2023-04-07 11:24:10.807]  nvidia   #0 02:00.0   0W 74C 164/3504 MHz
[2023-04-07 11:24:10.808]  miner    speed 10s/60s/15m 0.63 0.67 0.65 MH/s max 1.27 MH/s
[2023-04-07 11:24:19.562]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305580
[2023-04-07 11:24:29.406]  net      dev donate started
[2023-04-07 11:24:29.407]  net      new job from donate.ssl.xmrig.com:443 diff 862M algo kawpow height 2744921
[2023-04-07 11:24:35.093]  net      new job from donate.ssl.xmrig.com:443 diff 862M algo kawpow height 2744922
[2023-04-07 11:24:45.310]  miner    KawPow light cache for epoch 365 calculated (15850ms)
[2023-04-07 11:24:45.793]  nvidia   KawPow failed to initialize DAG: <kawpow_prepare>:62 "out of memory"
[2023-04-07 11:24:48.290]  net      new job from donate.ssl.xmrig.com:443 diff 862M algo kawpow height 2744923
[2023-04-07 11:25:15.655]  nvidia   #0 02:00.0   0W  0C 607/405 MHz
[2023-04-07 11:25:15.655]  miner    speed 10s/60s/15m n/a 0.71 0.65 MH/s max 1.27 MH/s
[2023-04-07 11:25:29.406]  net      dev donate finished
[2023-04-07 11:25:29.407]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305580
[2023-04-07 11:25:49.728]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305581
[2023-04-07 11:25:50.745]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305582
[2023-04-07 11:26:07.757]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305583
[2023-04-07 11:26:19.186]  nvidia   #0 02:00.0   0W  0C 607/405 MHz
[2023-04-07 11:26:19.186]  miner    speed 10s/60s/15m n/a n/a 0.65 MH/s max 1.27 MH/s
[2023-04-07 11:26:23.779]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305584
```

# Discussion History
## SChernykh | 2023-04-07T09:20:45+00:00
Dev donate mines RVN, which has bigger DAG than what you're mining (Meowcoin?). How much RAM does your GPU have?

## newsmoneymaker | 2023-04-07T09:55:35+00:00
Yes, Meowcoin. 

```
 * ABOUT        XMRig/6.19.0 gcc/11.2.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i3-1005G1 CPU @ 1.20GHz (1) 64-bit AES
                L2:1.0 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       6.7/7.8 GB (86%)
                DIMM_A0: 4 GB DDR4 @ 2667 MHz ACR26D4S9S1KA-4
                DIMM_B0: 4 GB DDR4 @ 2667 MHz HMA851S6CJR6N-VK
 * MOTHERBOARD  IL - Doc_IL
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      kaw.pool:5010 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         10.2/10.2/6.17.0
 * NVML         10.442.80/442.80 press e for health report
 * CUDA GPU     #0 02:00.0 GeForce MX350 1468/3504 MHz smx:5 arch:61 mem:1642/2048 MB
[2023-04-07 11:44:20.855]  net      use pool kaw.pool:5010  
[2023-04-07 11:44:20.856]  net      new job from kaw.pool:5010 diff 43118K algo kawpow height 305599
[2023-04-07 11:44:20.857]  nvidia   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 02:00.0 |   2621440 |     256 |  10240 |  8 |  25 |   1344 | GeForce MX350
```

## xmrig | 2023-04-07T16:36:29+00:00
Fixed in dev branch.
Thank you.

## newsmoneymaker | 2023-04-07T19:46:51+00:00
Thank you, but I understand correctly that in the next compilation this edit will be included in v6.19.3

## xmrig | 2023-04-08T18:25:16+00:00
Yes, but if you looking for compiled files it can be downloaded here https://download.xmrig.com/xmrig/6.19.3-dev/c4e136314815f6892136f6be604121143fed10f9/ username: `xmrig`, password: `download`.

## newsmoneymaker | 2023-04-08T18:37:52+00:00
Thank you!

# Action History
- Created by: newsmoneymaker | 2023-04-07T08:41:19+00:00
- Closed at: 2023-06-07T14:57:27+00:00
