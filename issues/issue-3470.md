---
title: Is it possible to hide the console thing?
source_url: https://github.com/xmrig/xmrig/issues/3470
author: RyanisyydsTT
assignees: []
labels: []
created_at: '2024-04-29T13:59:10+00:00'
updated_at: '2024-05-02T11:20:39+00:00'
type: issue
status: closed
closed_at: '2024-05-02T11:20:38+00:00'
---

# Original Description
 * ABOUT        XMRig/6.21.0 gcc/5.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 7950X3D 16-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:128.0 MB 16C/32T NUMA:1
 * MEMORY       50.3/125.0 GB (40%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.hashvault.pro:80 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-04-29 13:52:36.337]  net      use pool pool.hashvault.pro:80 TLSv1.3 45.76.89.70
[2024-04-29 13:52:36.337]  net      new job from pool.hashvault.pro:80 diff 7267K algo rx/0 height 240068
[2024-04-29 13:52:36.337]  cpu      use argon2 implementation AVX-512F
[2024-04-29 13:52:36.337]  msr      msr kernel module is not available
[2024-04-29 13:52:36.337]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-04-29 13:52:36.338]  randomx  init dataset algo rx/0 (32 threads) seed 6402fe5ae7b78729...
[2024-04-29 13:52:36.338]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2024-04-29 13:52:58.350]  randomx  dataset ready (22012 ms)
[2024-04-29 13:52:58.350]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2024-04-29 13:52:58.453]  cpu      READY threads 32/32 (32) huge pages 0% 0/32 memory 65536 KB (103 ms)
[2024-04-29 13:53:54.525]  net      new job from pool.hashvault.pro:80 diff 7267K algo rx/0 height 240068
[2024-04-29 13:54:01.326]  miner    speed 10s/60s/15m 565.1 562.6 n/a H/s max 575.6 H/s


I want to hide these^^

# Discussion History
## jojo2357 | 2024-05-01T15:13:07+00:00
pipe your command into `/dev/null` like so: 

`<your command> >/dev/null 2>&1` which will redirect stdout and stderr

## RyanisyydsTT | 2024-05-02T11:20:38+00:00
Ok thx!!

# Action History
- Created by: RyanisyydsTT | 2024-04-29T13:59:10+00:00
- Closed at: 2024-05-02T11:20:38+00:00
