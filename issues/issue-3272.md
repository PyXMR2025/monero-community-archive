---
title: Msr mod issues
source_url: https://github.com/xmrig/xmrig/issues/3272
author: Jinxsyns
assignees: []
labels:
- question
created_at: '2023-05-22T22:41:36+00:00'
updated_at: '2023-06-07T14:54:16+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:54:16+00:00'
---

# Original Description
I've tried everything but checking if secure boot is on that I saw in other comments and can't get it to work. Could secure boot be the issue?


 * ABOUT        XMRig/6.19.2 gcc/11.2.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 7950X 16-Core Processor (1) 64-bit AES VM
                L2:16.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       10.8/63.2 GB (17%)
                DIMMA1: <empty>
                DIMMA2: 32 GB DDR5 @ 6000 MHz F5-6000J3238G32G
                DIMMB1: <empty>
                DIMMB2: 32 GB DDR5 @ 6000 MHz F5-6000J3238G32G
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MS-7D78
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://pool.us.woolypooly.com:3110 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-05-22 17:37:29.102]  net      use pool pool.us.woolypooly.com:3110  5.161.112.148
[2023-05-22 17:37:29.102]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575400
[2023-05-22 17:37:29.102]  msr      service WinRing0_1_2_0 already exists, but with a different service name
[2023-05-22 17:37:29.116]  msr      cannot set MSR 0xc0011020 to 0x0004400000000000
[2023-05-22 17:37:29.116]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

# Discussion History
## Jinxsyns | 2023-05-22T23:07:02+00:00
I've turned off secured boot and it still isn't working

## Jinxsyns | 2023-05-22T23:31:24+00:00
So i got the VM i didn't notice it was running in off and the msr mod to apply but I'm still getting the same hashrate I was before and I don't understand why? heres like 3 minutes of it running for y'all to see what I mean

 * ABOUT        XMRig/6.19.2 gcc/11.2.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 7950X 16-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       5.5/63.2 GB (9%)
                DIMMA1: <empty>
                DIMMA2: 32 GB DDR5 @ 6000 MHz F5-6000J3238G32G
                DIMMB1: <empty>
                DIMMB2: 32 GB DDR5 @ 6000 MHz F5-6000J3238G32G
 * MOTHERBOARD  Micro-Star International Co., Ltd. - PRO B650-P WIFI (MS-7D78)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://pool.us.woolypooly.com:3110 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-05-22 18:25:30.511]  net      use pool pool.us.woolypooly.com:3110  5.161.64.47
[2023-05-22 18:25:30.512]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575426
[2023-05-22 18:25:30.512]  msr      service WinRing0_1_2_0 already exists, but with a different service name
[2023-05-22 18:25:31.006]  msr      register values for "ryzen_19h_zen4" preset have been set successfully (495 ms)
[2023-05-22 18:25:31.942]  cpu      use profile  ghostrider  (16 threads) scratchpad 2048 KB
[2023-05-22 18:25:32.023]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2023-05-22 18:25:32.023]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2023-05-22 18:25:32.023]  cpu      GhostRider algo 3: cn/fast (2 MB)
[2023-05-22 18:25:32.030]  cpu      READY threads 32/32 (128) huge pages 100% 128/128 memory 262144 KB (88 ms)
[2023-05-22 18:25:32.773]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575426
[2023-05-22 18:25:33.076]  cpu      accepted (1/0) diff 6554 (66 ms)
[2023-05-22 18:25:36.473]  cpu      accepted (2/0) diff 6554 (66 ms)
[2023-05-22 18:25:37.541]  cpu      accepted (3/0) diff 6554 (71 ms)
[2023-05-22 18:25:41.145]  cpu      accepted (4/0) diff 6554 (67 ms)
[2023-05-22 18:25:44.582]  cpu      accepted (5/0) diff 6554 (66 ms)
[2023-05-22 18:25:52.658]  cpu      accepted (6/0) diff 6554 (98 ms)
[2023-05-22 18:25:53.278]  cpu      accepted (7/0) diff 6554 (62 ms)
[2023-05-22 18:25:53.614]  cpu      accepted (8/0) diff 6554 (74 ms)
[2023-05-22 18:25:55.465]  cpu      accepted (9/0) diff 6554 (62 ms)
[2023-05-22 18:25:55.608]  cpu      accepted (10/0) diff 6554 (59 ms)
[2023-05-22 18:25:56.903]  cpu      accepted (11/0) diff 6554 (61 ms)
[2023-05-22 18:26:02.090]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575427
[2023-05-22 18:26:02.091]  cpu      GhostRider algo 1: cn/dark (512 KB)
[2023-05-22 18:26:02.091]  cpu      GhostRider algo 2: cn/dark-lite (256 KB)
[2023-05-22 18:26:02.091]  cpu      GhostRider algo 3: cn/fast (2 MB)
[2023-05-22 18:26:02.772]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575427
[2023-05-22 18:26:02.917]  cpu      accepted (12/0) diff 6554 (55 ms)
[2023-05-22 18:26:03.505]  cpu      accepted (13/0) diff 6554 (65 ms)
[2023-05-22 18:26:03.523]  cpu      accepted (14/0) diff 6554 (56 ms)
[2023-05-22 18:26:03.867]  cpu      accepted (15/0) diff 6554 (63 ms)
[2023-05-22 18:26:05.032]  cpu      accepted (16/0) diff 6554 (59 ms)
[2023-05-22 18:26:05.347]  cpu      accepted (17/0) diff 6554 (59 ms)
[2023-05-22 18:26:06.248]  cpu      accepted (18/0) diff 6554 (57 ms)
[2023-05-22 18:26:06.577]  cpu      accepted (19/0) diff 6554 (57 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   252.5 |     n/a |     n/a |
|        1 |        2 |   263.4 |     n/a |     n/a |
|        2 |        4 |   255.8 |     n/a |     n/a |
|        3 |        6 |   260.0 |     n/a |     n/a |
|        4 |        8 |   257.5 |     n/a |     n/a |
|        5 |       10 |   259.2 |     n/a |     n/a |
|        6 |       12 |   257.5 |     n/a |     n/a |
|        7 |       14 |   265.9 |     n/a |     n/a |
|        8 |       16 |   238.3 |     n/a |     n/a |
|        9 |       18 |   251.6 |     n/a |     n/a |
|       10 |       20 |   252.5 |     n/a |     n/a |
|       11 |       22 |   249.1 |     n/a |     n/a |
|       12 |       24 |   247.5 |     n/a |     n/a |
|       13 |       26 |   251.6 |     n/a |     n/a |
|       14 |       28 |   243.3 |     n/a |     n/a |
|       15 |       30 |   250.0 |     n/a |     n/a |
|        - |        - |  4055.6 |     n/a |     n/a |
[2023-05-22 18:26:07.233]  miner    speed 10s/60s/15m 4055.6 n/a n/a H/s max 4055.6 H/s avg 3615.1 H/s
[2023-05-22 18:26:07.832]  cpu      accepted (20/0) diff 6554 (59 ms)
[2023-05-22 18:26:08.208]  cpu      accepted (21/0) diff 6554 (60 ms)
[2023-05-22 18:26:08.295]  cpu      accepted (22/0) diff 6554 (73 ms)
[2023-05-22 18:26:09.324]  cpu      accepted (23/0) diff 6554 (56 ms)
[2023-05-22 18:26:10.059]  cpu      accepted (24/0) diff 6554 (59 ms)
[2023-05-22 18:26:10.222]  cpu      accepted (25/0) diff 6554 (60 ms)
[2023-05-22 18:26:10.504]  cpu      accepted (26/0) diff 6554 (62 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   277.0 |     n/a |     n/a |
|        1 |        2 |   286.2 |     n/a |     n/a |
|        2 |        4 |   277.8 |     n/a |     n/a |
|        3 |        6 |   282.0 |     n/a |     n/a |
|        4 |        8 |   282.8 |     n/a |     n/a |
|        5 |       10 |   284.5 |     n/a |     n/a |
|        6 |       12 |   280.3 |     n/a |     n/a |
|        7 |       14 |   286.2 |     n/a |     n/a |
|        8 |       16 |   265.2 |     n/a |     n/a |
|        9 |       18 |   273.6 |     n/a |     n/a |
|       10 |       20 |   273.6 |     n/a |     n/a |
|       11 |       22 |   271.1 |     n/a |     n/a |
|       12 |       24 |   270.2 |     n/a |     n/a |
|       13 |       26 |   273.6 |     n/a |     n/a |
|       14 |       28 |   270.2 |     n/a |     n/a |
|       15 |       30 |   271.9 |     n/a |     n/a |
|        - |        - |  4426.4 |     n/a |     n/a |
[2023-05-22 18:26:11.044]  miner    speed 10s/60s/15m 4426.4 n/a n/a H/s max 4426.4 H/s avg 3670.1 H/s
[2023-05-22 18:26:12.726]  cpu      accepted (27/0) diff 6554 (62 ms)
[2023-05-22 18:26:13.175]  cpu      accepted (28/0) diff 6554 (74 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   286.6 |     n/a |     n/a |
|        1 |        2 |   294.2 |     n/a |     n/a |
|        2 |        4 |   284.1 |     n/a |     n/a |
|        3 |        6 |   291.6 |     n/a |     n/a |
|        4 |        8 |   290.8 |     n/a |     n/a |
|        5 |       10 |   290.8 |     n/a |     n/a |
|        6 |       12 |   289.1 |     n/a |     n/a |
|        7 |       14 |   294.2 |     n/a |     n/a |
|        8 |       16 |   277.4 |     n/a |     n/a |
|        9 |       18 |   280.7 |     n/a |     n/a |
|       10 |       20 |   279.9 |     n/a |     n/a |
|       11 |       22 |   278.2 |     n/a |     n/a |
|       12 |       24 |   279.1 |     n/a |     n/a |
|       13 |       26 |   280.7 |     n/a |     n/a |
|       14 |       28 |   277.4 |     n/a |     n/a |
|       15 |       30 |   276.6 |     n/a |     n/a |
|        - |        - |  4551.4 |     n/a |     n/a |
[2023-05-22 18:26:14.735]  miner    speed 10s/60s/15m 4551.4 n/a n/a H/s max 4553.1 H/s avg 3784.0 H/s
[2023-05-22 18:26:16.775]  cpu      accepted (29/0) diff 6554 (74 ms)
[2023-05-22 18:26:18.784]  cpu      accepted (30/0) diff 6554 (60 ms)
[2023-05-22 18:26:21.072]  cpu      accepted (31/0) diff 6554 (57 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   290.5 |     n/a |     n/a |
|        1 |        2 |   296.3 |     n/a |     n/a |
|        2 |        4 |   290.5 |     n/a |     n/a |
|        3 |        6 |   296.0 |     n/a |     n/a |
|        4 |        8 |   292.4 |     n/a |     n/a |
|        5 |       10 |   291.6 |     n/a |     n/a |
|        6 |       12 |   292.4 |     n/a |     n/a |
|        7 |       14 |   296.9 |     n/a |     n/a |
|        8 |       16 |   279.2 |     n/a |     n/a |
|        9 |       18 |   281.0 |     n/a |     n/a |
|       10 |       20 |   281.9 |     n/a |     n/a |
|       11 |       22 |   279.2 |     n/a |     n/a |
|       12 |       24 |   279.2 |     n/a |     n/a |
|       13 |       26 |   281.0 |     n/a |     n/a |
|       14 |       28 |   277.5 |     n/a |     n/a |
|       15 |       30 |   278.4 |     n/a |     n/a |
|        - |        - |  4584.0 |     n/a |     n/a |
[2023-05-22 18:26:22.183]  miner    speed 10s/60s/15m 4581.8 n/a n/a H/s max 4581.8 H/s avg 3868.2 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   289.7 |     n/a |     n/a |
|        1 |        2 |   296.4 |     n/a |     n/a |
|        2 |        4 |   291.4 |     n/a |     n/a |
|        3 |        6 |   296.4 |     n/a |     n/a |
|        4 |        8 |   293.9 |     n/a |     n/a |
|        5 |       10 |   291.4 |     n/a |     n/a |
|        6 |       12 |   292.2 |     n/a |     n/a |
|        7 |       14 |   295.6 |     n/a |     n/a |
|        8 |       16 |   279.7 |     n/a |     n/a |
|        9 |       18 |   281.4 |     n/a |     n/a |
|       10 |       20 |   281.4 |     n/a |     n/a |
|       11 |       22 |   279.7 |     n/a |     n/a |
|       12 |       24 |   278.9 |     n/a |     n/a |
|       13 |       26 |   280.6 |     n/a |     n/a |
|       14 |       28 |   277.2 |     n/a |     n/a |
|       15 |       30 |   278.1 |     n/a |     n/a |
|        - |        - |  4584.1 |     n/a |     n/a |
[2023-05-22 18:26:26.599]  miner    speed 10s/60s/15m 4584.1 n/a n/a H/s max 4584.6 H/s avg 3935.3 H/s
[2023-05-22 18:26:29.096]  cpu      accepted (32/0) diff 6554 (77 ms)
[2023-05-22 18:26:29.818]  cpu      accepted (33/0) diff 6554 (74 ms)
[2023-05-22 18:26:29.956]  cpu      accepted (34/0) diff 6554 (61 ms)
[2023-05-22 18:26:30.096]  cpu      accepted (35/0) diff 6554 (60 ms)
[2023-05-22 18:26:30.708]  cpu      accepted (36/0) diff 6554 (66 ms)
[2023-05-22 18:26:31.251]  cpu      accepted (37/0) diff 6554 (59 ms)
[2023-05-22 18:26:31.795]  miner    speed 10s/60s/15m 4574.3 n/a n/a H/s max 4585.3 H/s avg 4012.7 H/s
[2023-05-22 18:26:32.774]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575427
[2023-05-22 18:26:34.426]  cpu      accepted (38/0) diff 6554 (60 ms)
[2023-05-22 18:26:35.364]  cpu      accepted (39/0) diff 6554 (62 ms)
[2023-05-22 18:26:35.877]  cpu      accepted (40/0) diff 6554 (64 ms)
[2023-05-22 18:26:37.006]  cpu      accepted (41/0) diff 6554 (60 ms)
[2023-05-22 18:26:37.206]  cpu      accepted (42/0) diff 6554 (60 ms)
[2023-05-22 18:26:37.457]  cpu      accepted (43/0) diff 6554 (59 ms)
[2023-05-22 18:26:38.283]  cpu      accepted (44/0) diff 6554 (60 ms)
[2023-05-22 18:26:38.645]  cpu      accepted (45/0) diff 6554 (60 ms)
[2023-05-22 18:26:39.964]  cpu      accepted (46/0) diff 6554 (68 ms)
[2023-05-22 18:26:44.227]  cpu      accepted (47/0) diff 6554 (62 ms)
[2023-05-22 18:26:44.245]  cpu      accepted (48/0) diff 6554 (79 ms)
[2023-05-22 18:26:44.263]  cpu      accepted (49/0) diff 6554 (97 ms)
[2023-05-22 18:26:44.296]  cpu      accepted (50/0) diff 6554 (130 ms)
[2023-05-22 18:26:48.983]  cpu      accepted (51/0) diff 6554 (63 ms)
[2023-05-22 18:26:50.290]  cpu      accepted (52/0) diff 6554 (64 ms)
[2023-05-22 18:26:51.865]  cpu      accepted (53/0) diff 6554 (58 ms)
[2023-05-22 18:26:52.417]  cpu      accepted (54/0) diff 6554 (91 ms)
[2023-05-22 18:26:52.660]  cpu      accepted (55/0) diff 6554 (59 ms)
[2023-05-22 18:26:53.056]  cpu      accepted (56/0) diff 6554 (59 ms)
[2023-05-22 18:26:57.707]  cpu      accepted (57/0) diff 6554 (66 ms)
[2023-05-22 18:27:00.325]  cpu      accepted (58/0) diff 6554 (65 ms)
[2023-05-22 18:27:02.776]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575427
[2023-05-22 18:27:03.224]  cpu      accepted (59/0) diff 6554 (59 ms)
[2023-05-22 18:27:03.404]  cpu      accepted (60/0) diff 6554 (56 ms)
[2023-05-22 18:27:06.646]  cpu      accepted (61/0) diff 6554 (62 ms)
[2023-05-22 18:27:06.828]  cpu      accepted (62/0) diff 6554 (59 ms)
[2023-05-22 18:27:07.745]  cpu      accepted (63/0) diff 6554 (84 ms)
[2023-05-22 18:27:07.993]  cpu      accepted (64/0) diff 6554 (59 ms)
[2023-05-22 18:27:08.326]  cpu      accepted (65/0) diff 6554 (57 ms)
[2023-05-22 18:27:09.456]  cpu      accepted (66/0) diff 6554 (59 ms)
[2023-05-22 18:27:11.105]  cpu      accepted (67/0) diff 6554 (77 ms)
[2023-05-22 18:27:13.295]  cpu      accepted (68/0) diff 6554 (80 ms)
[2023-05-22 18:27:13.955]  cpu      accepted (69/0) diff 6554 (59 ms)
[2023-05-22 18:27:14.491]  cpu      accepted (70/0) diff 6554 (62 ms)
[2023-05-22 18:27:15.288]  cpu      accepted (71/0) diff 6554 (73 ms)
[2023-05-22 18:27:15.438]  cpu      accepted (72/0) diff 6554 (94 ms)
[2023-05-22 18:27:17.627]  cpu      accepted (73/0) diff 6554 (63 ms)
[2023-05-22 18:27:17.978]  cpu      accepted (74/0) diff 6554 (61 ms)
[2023-05-22 18:27:22.251]  cpu      accepted (75/0) diff 6554 (61 ms)
[2023-05-22 18:27:22.298]  cpu      accepted (76/0) diff 6554 (57 ms)
[2023-05-22 18:27:24.854]  cpu      accepted (77/0) diff 6554 (59 ms)
[2023-05-22 18:27:25.693]  cpu      accepted (78/0) diff 6554 (57 ms)
[2023-05-22 18:27:25.957]  cpu      accepted (79/0) diff 6554 (72 ms)
[2023-05-22 18:27:28.113]  net      new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575428
[2023-05-22 18:27:28.113]  cpu      GhostRider algo 1: cn/turtle (256 KB)
[2023-05-22 18:27:28.114]  cpu      GhostRider algo 2: cn/dark (512 KB)
[2023-05-22 18:27:28.114]  cpu      GhostRider algo 3: cn/lite (1 MB)
[2023-05-22 18:27:32.775]  net      new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575428
[2023-05-22 18:27:35.833]  miner    speed 10s/60s/15m 6989.3 4813.8 n/a H/s max 6989.3 H/s avg 4416.8 H/s
[2023-05-22 18:27:43.908]  cpu      accepted (80/0) diff 56976 (66 ms)
[2023-05-22 18:27:45.115]  net      new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575429
[2023-05-22 18:27:45.118]  cpu      GhostRider algo 1: cn/turtle-lite (128 KB)
[2023-05-22 18:27:45.119]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2023-05-22 18:27:45.119]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   473.7 |   310.8 |     n/a |
|        1 |        2 |   514.9 |   367.3 |     n/a |
|        2 |        4 |   503.1 |   356.2 |     n/a |
|        3 |        6 |   514.0 |   367.3 |     n/a |
|        4 |        8 |   515.7 |   365.5 |     n/a |
|        5 |       10 |   514.0 |   366.5 |     n/a |
|        6 |       12 |   496.4 |   340.9 |     n/a |
|        7 |       14 |   518.2 |   371.5 |     n/a |
|        8 |       16 |   477.9 |   342.3 |     n/a |
|        9 |       18 |   488.8 |   353.3 |     n/a |
|       10 |       20 |   491.3 |   355.8 |     n/a |
|       11 |       22 |   484.6 |   348.6 |     n/a |
|       12 |       24 |   488.0 |   350.8 |     n/a |
|       13 |       26 |   491.3 |   355.7 |     n/a |
|       14 |       28 |   487.1 |   349.5 |     n/a |
|       15 |       30 |   487.1 |   352.2 |     n/a |
|        - |        - |  7946.2 |  5654.1 |     n/a |
[2023-05-22 18:27:51.092]  miner    speed 10s/60s/15m 7946.2 5654.1 n/a H/s max 7946.2 H/s avg 4782.3 H/s
[2023-05-22 18:27:51.882]  cpu      accepted (81/0) diff 56976 (58 ms)
[2023-05-22 18:27:52.257]  cpu      accepted (82/0) diff 56976 (54 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   508.4 |   339.0 |     n/a |
|        1 |        2 |   531.9 |   390.6 |     n/a |
|        2 |        4 |   521.9 |   379.7 |     n/a |
|        3 |        6 |   529.4 |   390.1 |     n/a |
|        4 |        8 |   526.9 |   388.7 |     n/a |
|        5 |       10 |   528.6 |   389.1 |     n/a |
|        6 |       12 |   524.4 |   367.8 |     n/a |
|        7 |       14 |   532.8 |   394.2 |     n/a |
|        8 |       16 |   495.9 |   365.0 |     n/a |
|        9 |       18 |   500.9 |   374.0 |     n/a |
|       10 |       20 |   503.4 |   376.7 |     n/a |
|       11 |       22 |   496.7 |   370.1 |     n/a |
|       12 |       24 |   500.1 |   372.1 |     n/a |
|       13 |       26 |   503.4 |   376.7 |     n/a |
|       14 |       28 |   499.2 |   370.8 |     n/a |
|       15 |       30 |   497.5 |   372.8 |     n/a |
|        - |        - |  8201.4 |  6017.4 |     n/a |
[2023-05-22 18:27:56.659]  miner    speed 10s/60s/15m 8201.4 6017.4 n/a H/s max 8201.4 H/s avg 4912.4 H/s
[2023-05-22 18:28:02.780]  net      new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575429
[2023-05-22 18:28:04.643]  cpu      accepted (83/0) diff 56976 (55 ms)
[2023-05-22 18:28:07.130]  net      new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575430
[2023-05-22 18:28:07.132]  cpu      GhostRider algo 1: cn/turtle-lite (128 KB)
[2023-05-22 18:28:07.132]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2023-05-22 18:28:07.133]  cpu      GhostRider algo 3: cn/lite (1 MB)
[2023-05-22 18:28:32.778]  net      new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575430
[2023-05-22 18:28:36.036]  miner    speed 10s/60s/15m 3571.2 5737.0 n/a H/s max 8205.4 H/s avg 4852.7 H/s
[2023-05-22 18:28:46.232]  cpu      accepted (84/0) diff 56976 (69 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   225.4 |   290.5 |     n/a |
|        1 |        2 |   238.8 |   318.3 |     n/a |
|        2 |        4 |   230.9 |   301.5 |     n/a |
|        3 |        6 |   237.0 |   313.3 |     n/a |
|        4 |        8 |   234.4 |   307.9 |     n/a |
|        5 |       10 |   235.3 |   315.0 |     n/a |
|        6 |       12 |   234.4 |   297.1 |     n/a |
|        7 |       14 |   237.9 |   316.7 |     n/a |
|        8 |       16 |   220.3 |   265.3 |     n/a |
|        9 |       18 |   224.7 |   290.8 |     n/a |
|       10 |       20 |   227.3 |   302.0 |     n/a |
|       11 |       22 |   222.1 |   286.2 |     n/a |
|       12 |       24 |   223.8 |   292.3 |     n/a |
|       13 |       26 |   226.5 |   302.0 |     n/a |
|       14 |       28 |   223.8 |   293.6 |     n/a |
|       15 |       30 |   224.7 |   300.0 |     n/a |
|        - |        - |  3666.5 |  4792.7 |     n/a |
[2023-05-22 18:28:49.585]  miner    speed 10s/60s/15m 3668.2 4792.7 n/a H/s max 8205.4 H/s avg 4763.0 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   224.6 |   282.8 |     n/a |
|        1 |        2 |   238.8 |   308.4 |     n/a |
|        2 |        4 |   230.5 |   292.1 |     n/a |
|        3 |        6 |   237.1 |   303.7 |     n/a |
|        4 |        8 |   234.6 |   298.3 |     n/a |
|        5 |       10 |   235.5 |   305.2 |     n/a |
|        6 |       12 |   233.8 |   287.5 |     n/a |
|        7 |       14 |   238.0 |   306.9 |     n/a |
|        8 |       16 |   220.4 |   256.6 |     n/a |
|        9 |       18 |   224.6 |   281.6 |     n/a |
|       10 |       20 |   227.1 |   292.6 |     n/a |
|       11 |       22 |   222.1 |   277.4 |     n/a |
|       12 |       24 |   223.8 |   282.9 |     n/a |
|       13 |       26 |   227.1 |   292.8 |     n/a |
|       14 |       28 |   224.6 |   284.4 |     n/a |
|       15 |       30 |   225.4 |   290.7 |     n/a |
|        - |        - |  3668.1 |  4641.9 |     n/a |
[2023-05-22 18:28:51.419]  miner    speed 10s/60s/15m 3668.1 4671.8 n/a H/s max 8205.4 H/s avg 4756.6 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   224.6 |   278.0 |     n/a |
|        1 |        2 |   237.9 |   305.4 |     n/a |
|        2 |        4 |   230.4 |   289.2 |     n/a |
|        3 |        6 |   237.1 |   300.7 |     n/a |
|        4 |        8 |   234.6 |   295.2 |     n/a |
|        5 |       10 |   235.4 |   302.1 |     n/a |
|        6 |       12 |   233.8 |   284.7 |     n/a |
|        7 |       14 |   237.9 |   303.9 |     n/a |
|        8 |       16 |   221.2 |   254.0 |     n/a |
|        9 |       18 |   225.4 |   278.9 |     n/a |
|       10 |       20 |   227.1 |   289.7 |     n/a |
|       11 |       22 |   222.1 |   274.5 |     n/a |
|       12 |       24 |   224.6 |   280.2 |     n/a |
|       13 |       26 |   226.3 |   289.7 |     n/a |
|       14 |       28 |   223.8 |   281.6 |     n/a |
|       15 |       30 |   224.6 |   287.9 |     n/a |
|        - |        - |  3666.9 |  4595.8 |     n/a |
[2023-05-22 18:28:52.297]  miner    speed 10s/60s/15m 3666.9 4595.8 n/a H/s max 8205.4 H/s avg 4754.4 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   223.9 |   273.3 |     n/a |
|        1 |        2 |   238.9 |   301.0 |     n/a |
|        2 |        4 |   230.6 |   284.5 |     n/a |
|        3 |        6 |   237.3 |   296.3 |     n/a |
|        4 |        8 |   234.8 |   290.7 |     n/a |
|        5 |       10 |   235.6 |   297.6 |     n/a |
|        6 |       12 |   233.1 |   279.9 |     n/a |
|        7 |       14 |   238.1 |   299.4 |     n/a |
|        8 |       16 |   221.4 |   249.6 |     n/a |
|        9 |       18 |   224.7 |   274.7 |     n/a |
|       10 |       20 |   227.2 |   285.6 |     n/a |
|       11 |       22 |   222.2 |   270.2 |     n/a |
|       12 |       24 |   224.7 |   276.0 |     n/a |
|       13 |       26 |   226.4 |   285.6 |     n/a |
|       14 |       28 |   223.9 |   277.4 |     n/a |
|       15 |       30 |   224.7 |   283.8 |     n/a |
|        - |        - |  3667.5 |  4525.7 |     n/a |
[2023-05-22 18:28:52.983]  miner    speed 10s/60s/15m 3667.5 4525.7 n/a H/s max 8205.4 H/s avg 4747.3 H/s
[2023-05-22 18:28:57.830]  cpu      accepted (85/0) diff 56976 (68 ms)
[2023-05-22 18:29:02.775]  net      new job from pool.us.woolypooly.com:3110 diff 106103 algo ghostrider height 575430
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   210.1 |   211.5 |     n/a |
|        1 |        2 |   231.8 |   234.4 |     n/a |
|        2 |        4 |   222.6 |   222.2 |     n/a |
|        3 |        6 |   232.7 |   232.5 |     n/a |
|        4 |        8 |   227.7 |   227.6 |     n/a |
|        5 |       10 |   233.5 |   232.6 |     n/a |
|        6 |       12 |   206.7 |   214.7 |     n/a |
|        7 |       14 |   235.2 |   234.4 |     n/a |
|        8 |       16 |   200.0 |   200.8 |     n/a |
|        9 |       18 |   220.1 |   219.7 |     n/a |
|       10 |       20 |   222.6 |   224.1 |     n/a |
|       11 |       22 |   215.9 |   213.6 |     n/a |
|       12 |       24 |   221.0 |   219.3 |     n/a |
|       13 |       26 |   224.3 |   224.1 |     n/a |
|       14 |       28 |   216.8 |   218.2 |     n/a |
|       15 |       30 |   221.0 |   221.8 |     n/a |
|        - |        - |  3542.2 |  3551.4 |     n/a |
[2023-05-22 18:29:14.379]  miner    speed 10s/60s/15m 3542.2 3551.4 n/a H/s max 8205.4 H/s avg 4632.4 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   217.6 |   213.3 |     n/a |
|        1 |        2 |   236.8 |   234.9 |     n/a |
|        2 |        4 |   225.9 |   222.9 |     n/a |
|        3 |        6 |   235.1 |   232.8 |     n/a |
|        4 |        8 |   231.0 |   228.1 |     n/a |
|        5 |       10 |   233.5 |   232.7 |     n/a |
|        6 |       12 |   212.6 |   215.3 |     n/a |
|        7 |       14 |   236.8 |   234.6 |     n/a |
|        8 |       16 |   206.7 |   202.8 |     n/a |
|        9 |       18 |   222.6 |   220.4 |     n/a |
|       10 |       20 |   225.1 |   224.3 |     n/a |
|       11 |       22 |   219.2 |   214.2 |     n/a |
|       12 |       24 |   222.6 |   219.6 |     n/a |
|       13 |       26 |   225.1 |   224.3 |     n/a |
|       14 |       28 |   220.1 |   218.7 |     n/a |
|       15 |       30 |   222.6 |   222.0 |     n/a |
|        - |        - |  3593.3 |  3561.0 |     n/a |
[2023-05-22 18:29:15.702]  miner    speed 10s/60s/15m 3593.3 3561.0 n/a H/s max 8205.4 H/s avg 4621.9 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   220.1 |   213.7 |     n/a |
|        1 |        2 |   236.8 |   235.0 |     n/a |
|        2 |        4 |   227.6 |   222.8 |     n/a |
|        3 |        6 |   235.1 |   232.8 |     n/a |
|        4 |        8 |   231.8 |   228.2 |     n/a |
|        5 |       10 |   234.3 |   232.7 |     n/a |
|        6 |       12 |   214.2 |   215.4 |     n/a |
|        7 |       14 |   236.8 |   234.7 |     n/a |
|        8 |       16 |   209.2 |   203.1 |     n/a |
|        9 |       18 |   222.6 |   220.5 |     n/a |
|       10 |       20 |   225.1 |   224.3 |     n/a |
|       11 |       22 |   220.1 |   214.5 |     n/a |
|       12 |       24 |   223.4 |   219.9 |     n/a |
|       13 |       26 |   225.1 |   224.2 |     n/a |
|       14 |       28 |   221.8 |   218.7 |     n/a |
|       15 |       30 |   223.4 |   222.2 |     n/a |
|        - |        - |  3607.5 |  3562.6 |     n/a |
[2023-05-22 18:29:16.183]  miner    speed 10s/60s/15m 3607.5 3562.6 n/a H/s max 8205.4 H/s avg 4619.7 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   219.4 |   213.7 |     n/a |
|        1 |        2 |   237.0 |   235.0 |     n/a |
|        2 |        4 |   227.8 |   223.0 |     n/a |
|        3 |        6 |   234.5 |   232.8 |     n/a |
|        4 |        8 |   231.1 |   228.2 |     n/a |
|        5 |       10 |   234.5 |   232.8 |     n/a |
|        6 |       12 |   215.2 |   216.2 |     n/a |
|        7 |       14 |   237.0 |   234.8 |     n/a |
|        8 |       16 |   209.4 |   203.4 |     n/a |
|        9 |       18 |   222.8 |   220.6 |     n/a |
|       10 |       20 |   225.3 |   224.3 |     n/a |
|       11 |       22 |   220.2 |   214.5 |     n/a |
|       12 |       24 |   223.6 |   219.9 |     n/a |
|       13 |       26 |   226.1 |   224.5 |     n/a |
|       14 |       28 |   221.9 |   218.8 |     n/a |
|       15 |       30 |   223.6 |   222.2 |     n/a |
|        - |        - |  3609.3 |  3564.7 |     n/a |
[2023-05-22 18:29:16.599]  miner    speed 10s/60s/15m 3609.3 3564.7 n/a H/s max 8205.4 H/s avg 4619.6 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   217.7 |   213.5 |     n/a |
|        1 |        2 |   236.9 |   235.0 |     n/a |
|        2 |        4 |   226.9 |   223.0 |     n/a |
|        3 |        6 |   234.4 |   232.9 |     n/a |
|        4 |        8 |   231.1 |   228.2 |     n/a |
|        5 |       10 |   233.6 |   232.7 |     n/a |
|        6 |       12 |   215.2 |   216.3 |     n/a |
|        7 |       14 |   236.9 |   234.9 |     n/a |
|        8 |       16 |   209.3 |   203.4 |     n/a |
|        9 |       18 |   222.7 |   220.6 |     n/a |
|       10 |       20 |   225.2 |   224.3 |     n/a |
|       11 |       22 |   220.2 |   214.5 |     n/a |
|       12 |       24 |   222.7 |   219.9 |     n/a |
|       13 |       26 |   225.2 |   224.4 |     n/a |
|       14 |       28 |   221.9 |   218.8 |     n/a |
|       15 |       30 |   223.5 |   222.2 |     n/a |
|        - |        - |  3603.6 |  3564.4 |     n/a |
[2023-05-22 18:29:16.969]  miner    speed 10s/60s/15m 3603.6 3564.4 n/a H/s max 8205.4 H/s avg 4620.2 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   217.6 |   213.8 |     n/a |
|        1 |        2 |   237.1 |   235.1 |     n/a |
|        2 |        4 |   226.5 |   223.1 |     n/a |
|        3 |        6 |   234.4 |   232.9 |     n/a |
|        4 |        8 |   230.0 |   228.2 |     n/a |
|        5 |       10 |   233.6 |   232.7 |     n/a |
|        6 |       12 |   215.9 |   216.6 |     n/a |
|        7 |       14 |   237.1 |   234.8 |     n/a |
|        8 |       16 |   208.8 |   203.4 |     n/a |
|        9 |       18 |   222.1 |   220.5 |     n/a |
|       10 |       20 |   224.7 |   224.3 |     n/a |
|       11 |       22 |   220.3 |   214.7 |     n/a |
|       12 |       24 |   222.9 |   219.9 |     n/a |
|       13 |       26 |   225.6 |   224.4 |     n/a |
|       14 |       28 |   222.1 |   218.8 |     n/a |
|       15 |       30 |   223.8 |   222.1 |     n/a |
|        - |        - |  3602.3 |  3565.4 |     n/a |
[2023-05-22 18:29:17.313]  miner    speed 10s/60s/15m 3602.3 3565.4 n/a H/s max 8205.4 H/s avg 4613.1 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   217.6 |   213.7 |     n/a |
|        1 |        2 |   236.8 |   235.0 |     n/a |
|        2 |        4 |   226.8 |   223.2 |     n/a |
|        3 |        6 |   235.1 |   233.0 |     n/a |
|        4 |        8 |   230.1 |   228.2 |     n/a |
|        5 |       10 |   234.3 |   232.9 |     n/a |
|        6 |       12 |   216.7 |   216.8 |     n/a |
|        7 |       14 |   236.8 |   235.0 |     n/a |
|        8 |       16 |   210.0 |   203.5 |     n/a |
|        9 |       18 |   222.6 |   220.6 |     n/a |
|       10 |       20 |   225.1 |   224.4 |     n/a |
|       11 |       22 |   220.9 |   215.2 |     n/a |
|       12 |       24 |   223.4 |   219.9 |     n/a |
|       13 |       26 |   225.9 |   224.5 |     n/a |
|       14 |       28 |   221.8 |   218.8 |     n/a |
|       15 |       30 |   223.4 |   222.1 |     n/a |
|        - |        - |  3607.5 |  3566.8 |     n/a |
[2023-05-22 18:29:17.650]  miner    speed 10s/60s/15m 3607.5 3566.8 n/a H/s max 8205.4 H/s avg 4614.3 H/s


## Jinxsyns | 2023-05-22T23:39:39+00:00
Now i'm seeing it jump every few minutes from 3,500h/s to roughly 7,500h/s and then back to 3,500h/s

## Jinxsyns | 2023-05-22T23:47:00+00:00
Now i'm running a benchmark and its at 22,500ish average is this just showing me capability over real world performance?

## SChernykh | 2023-05-23T05:17:21+00:00
It's how Ghostrider algorithm works. MSR mod does very little there, and hashrate changes all the time at different block heights. If you don't get MSR mod errors anymore, everything is fine.

## Spudz76 | 2023-05-23T17:00:15+00:00
```
[2023-05-22 18:28:07.130] net new job from pool.us.woolypooly.com:3110 diff 56976 algo ghostrider height 575430
[2023-05-22 18:28:07.132] cpu GhostRider algo 1: cn/turtle-lite (128 KB)
[2023-05-22 18:28:07.132] cpu GhostRider algo 2: cn/fast (2 MB)
[2023-05-22 18:28:07.133] cpu GhostRider algo 3: cn/lite (1 MB)
```

Every time the three stacked algos are remixed like here, the hashrate will change, sometimes wildly.

# Action History
- Created by: Jinxsyns | 2023-05-22T22:41:36+00:00
- Closed at: 2023-06-07T14:54:16+00:00
