---
title: xmrig job terminated
source_url: https://github.com/xmrig/xmrig/issues/2686
author: meescha
assignees: []
labels: []
created_at: '2021-11-11T20:22:26+00:00'
updated_at: '2021-11-12T18:27:44+00:00'
type: issue
status: closed
closed_at: '2021-11-12T18:27:43+00:00'
---

# Original Description
 im getting this crash everytime i try to run xmrig


* ABOUT        XMRig/6.15.3 gcc/5.4.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 3900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       5.6/31.3 GB (18%)
                DIMM 0: <empty>
                DIMM_A1: 16 GB DDR4 @ 3200 MHz F4-3200C16-16GVK
                DIMM 0: <empty>
                DIMM_B1: 16 GB DDR4 @ 3200 MHz F4-3200C16-16GVK
 * MOTHERBOARD  ASRock - X570M Pro4
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-11-11 21:05:37.003]  config   configuration saved to: "/run/media/***/***/xmrig-6.15.3/config.json"
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-11 21:05:37.127]  net      use pool pool.supportxmr.com:443 TLSv1.2 94.130.12.27
[2021-11-11 21:05:37.127]  net      fingerprint (SHA-256): "***"
[2021-11-11 21:05:37.127]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2491164 (130 tx)
[2021-11-11 21:05:37.127]  cpu      use argon2 implementation AVX2
[2021-11-11 21:05:37.128]  msr      register values for "ryzen_17h" preset have been set successfully (1 ms)
[2021-11-11 21:05:37.128]  randomx  init dataset algo rx/0 (24 threads) seed c7743ee59c670469...
[2021-11-11 21:05:37.539]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (412 ms)
[2021-11-11 21:05:38.928]  randomx  dataset ready (1388 ms)
[2021-11-11 21:05:38.928]  cpu      use profile  rx  (24 threads) scratchpad 2048 KB
[2021-11-11 21:05:38.937]  cpu      READY threads 24/24 (24) huge pages 100% 24/24 memory 49152 KB (9 ms)
[2021-11-11 21:05:40.676]  cpu      accepted (1/0) diff 50000 (36 ms)
[2021-11-11 21:05:41.321]  cpu      accepted (2/0) diff 50000 (37 ms)
[2021-11-11 21:05:43.270]  cpu      accepted (3/0) diff 50000 (39 ms)
[2021-11-11 21:05:48.015]  cpu      accepted (4/0) diff 50000 (37 ms)
[2021-11-11 21:05:50.591]  cpu      accepted (5/0) diff 50000 (37 ms)
[2021-11-11 21:05:50.958]  cpu      accepted (6/0) diff 50000 (36 ms)
[2021-11-11 21:05:51.256]  cpu      accepted (7/0) diff 50000 (39 ms)
[2021-11-11 21:05:51.375]  cpu      accepted (8/0) diff 50000 (24 ms)
[2021-11-11 21:05:53.753]  cpu      accepted (9/0) diff 50000 (23 ms)
[2021-11-11 21:05:54.737]  cpu      accepted (10/0) diff 50000 (36 ms)
[2021-11-11 21:05:58.377]  cpu      accepted (11/0) diff 50000 (39 ms)
[2021-11-11 21:06:01.258]  cpu      accepted (12/0) diff 50000 (36 ms)
[2021-11-11 21:06:01.517]  cpu      accepted (13/0) diff 50000 (39 ms)
[2021-11-11 21:06:11.590]  cpu      accepted (14/0) diff 50000 (24 ms)
[2021-11-11 21:06:13.044]  cpu      accepted (15/0) diff 50000 (24 ms)
[2021-11-11 21:06:16.271]  cpu      accepted (16/0) diff 50000 (23 ms)
[2021-11-11 21:06:19.933]  cpu      accepted (17/0) diff 50000 (38 ms)
[2021-11-11 21:06:20.183]  cpu      accepted (18/0) diff 50000 (24 ms)
[2021-11-11 21:06:22.666]  cpu      accepted (19/0) diff 50000 (37 ms)
[2021-11-11 21:06:24.244]  cpu      accepted (20/0) diff 50000 (27 ms)
[2021-11-11 21:06:25.179]  net      new job from pool.supportxmr.com:443 diff 937561 algo rx/0 height 2491164 (130 tx)
[2021-11-11 21:06:38.985]  miner    speed 10s/60s/15m 14728.3 n/a n/a H/s max 14845.5 H/s
[2021-11-11 21:06:39.262]  net      new job from pool.supportxmr.com:443 diff 937561 algo rx/0 height 2491165 (123 tx)
[2021-11-11 21:06:45.195]  cpu      accepted (21/0) diff 937561 (37 ms)
fish: Job 1, 'sudo ./xmrig' terminated by signal SIGABRT (Abort)

# Discussion History
## meescha | 2021-11-12T18:27:43+00:00
after long tested it seems like it was a unstable overclock, weird that i didnt have issues with prime95 but i did figure it out

# Action History
- Created by: meescha | 2021-11-11T20:22:26+00:00
- Closed at: 2021-11-12T18:27:43+00:00
