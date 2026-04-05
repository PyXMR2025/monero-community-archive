---
title: msr kernel module is not available - probably leading to failing to apply MSR
  mod
source_url: https://github.com/xmrig/xmrig/issues/2069
author: DonDon-9097
assignees: []
labels: []
created_at: '2021-01-29T13:35:03+00:00'
updated_at: '2021-01-29T19:20:52+00:00'
type: issue
status: closed
closed_at: '2021-01-29T19:20:52+00:00'
---

# Original Description
Okay, so I get FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW and I think it is because msr kernel module is nowhere to be found. 
It also fails to allocate RandomX dataset using 1GB pages, although I get the message it's supported.
Any solutions?
(I'm kinda new to linux, so dumb it down a little if necesarry)

╭─dondon at dondon-pc-garuda in ⌁/crypto/xmrig-6.8.0
╰─λ sudo ~/crypto/xmrig-6.8.0/xmrig
 * ABOUT        XMRig/6.8.0 gcc/5.4.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 9 5900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       20.8/23.5 GB (89%)
                DIMM 0: 8 GB DDR4 @ 3600 MHz F4-3600C16-8GVKC
                DIMM 1: 8 GB DDR4 @ 3600 MHz F4-3600C16-8GVKC
                DIMM 0: <empty>
                DIMM 1: 8 GB DDR4 @ 3600 MHz F4-3600C16-8GVKC
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MAG X570 TOMAHAWK WIFI (MS-7C84)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmrpool.eu:5555 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-01-29 14:19:57.104]  net      use pool xmrpool.eu:5555  54.37.7.208
[2021-01-29 14:19:57.104]  net      new job from xmrpool.eu:5555 diff 50000 algo rx/0 height 2285068
[2021-01-29 14:19:57.104]  cpu      use argon2 implementation AVX2
[2021-01-29 14:19:57.109]  msr      msr kernel module is not available
[2021-01-29 14:19:57.109]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-01-29 14:19:57.109]  randomx  init dataset algo rx/0 (24 threads) seed f1a94ed2953f45f4...
[2021-01-29 14:19:57.265]  randomx  failed to allocate RandomX dataset using 1GB pages
[2021-01-29 14:19:57.286]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (176 ms)
[2021-01-29 14:19:59.754]  randomx  dataset ready (2468 ms)
[2021-01-29 14:19:59.754]  cpu      use profile  rx  (24 threads) scratchpad 2048 KB
[2021-01-29 14:19:59.765]  cpu      READY threads 24/24 (24) huge pages 100% 24/24 memory 49152 KB (11 ms)
[2021-01-29 14:20:23.267]  cpu      accepted (1/0) diff 50000 (163 ms)
[2021-01-29 14:20:24.348]  cpu      accepted (2/0) diff 50000 (198 ms)
[2021-01-29 14:20:29.118]  cpu      accepted (3/0) diff 50000 (245 ms)
[2021-01-29 14:20:30.728]  cpu      accepted (4/0) diff 50000 (153 ms)
[2021-01-29 14:20:34.285]  cpu      accepted (5/0) diff 50000 (379 ms)
[2021-01-29 14:20:59.297]  cpu      accepted (6/0) diff 50000 (193 ms)
[2021-01-29 14:20:59.790]  miner    speed 10s/60s/15m 7834.4 n/a n/a H/s max 7835.2 H/s



# Discussion History
## DonDon-9097 | 2021-01-29T19:20:48+00:00
a reboot seems to have fixed it

# Action History
- Created by: DonDon-9097 | 2021-01-29T13:35:03+00:00
- Closed at: 2021-01-29T19:20:52+00:00
