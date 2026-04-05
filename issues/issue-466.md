---
title: No CUDA device found! (Windows10, cuda_8.0.61, Nvidia NVS310)
source_url: https://github.com/xmrig/xmrig/issues/466
author: minzak
assignees: []
labels: []
created_at: '2018-03-20T22:23:59+00:00'
updated_at: '2018-11-05T13:15:50+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:01:02+00:00'
---

# Original Description
When i Use Cuda 9 in system - My card is detected, but i got other error, that describe in this issue:
[https://github.com/xmrig/xmrig-nvidia/issues/132](https://github.com/xmrig/xmrig-nvidia/issues/132)

But When i Use Cuda 8 - xmrig not found my card.
```
C:\CRYPTO\xmrig-nvidia250\xmrig-nvidia.exe
 * VERSIONS:     XMRig/2.5.0 libuv/1.19.2 CUDA/0.0 MSVC/2015
 * CPU:                Intel(R) Xeon(R) CPU E3-1245 V2 @ 3.40GHz x64 AES-NI
 * ALGO:         cryptonight, donate=1%
 * POOL #1:      pool.supportxmr.com:5555
 * COMMANDS:     hashrate, health, pause, resume
[2018-03-21 00:11:45] No CUDA device found!
```
But other miners like xmr-stak very lucky, all see and all works.

```
-------------------------------------------------------------------
xmr-stak 2.2.0 c4400d19

Brought to you by fireice_uk and psychocrypt under GPLv3.
Based on CPU mining code by wolf9466 (heavily optimized by fireice_uk).
Based on NVIDIA mining code by KlausT and psychocrypt.
Based on OpenCL mining code by wolf9466.

Configurable dev donation level is set to 2.0%

You can use following keys to display reports:
'h' - hashrate
'r' - results
'c' - connection
-------------------------------------------------------------------
[2018-03-21 00:08:48] : Start mining: MONERO
[2018-03-21 00:08:48] : Starting NVIDIA GPU thread 0, no affinity.
[2018-03-21 00:08:48] : WARNING: No AMD OpenCL platform found. Possible driver issues or wrong vendor driver.
[2018-03-21 00:08:48] : WARNING: backend AMD disabled.
[2018-03-21 00:08:48] : Starting 1x thread, affinity: 0.
[2018-03-21 00:08:48] : hwloc: memory pinned
[2018-03-21 00:08:48] : Starting 1x thread, affinity: 2.
[2018-03-21 00:08:48] : hwloc: memory pinned
[2018-03-21 00:08:48] : Starting 1x thread, affinity: 4.
[2018-03-21 00:08:48] : hwloc: memory pinned
[2018-03-21 00:08:48] : Starting 1x thread, affinity: 6.
[2018-03-21 00:08:48] : hwloc: memory pinned
[2018-03-21 00:08:48] : Fast-connecting to pool.supportxmr.com:7777 pool ...
[2018-03-21 00:08:48] : Pool pool.supportxmr.com:7777 connected. Logging in...
[2018-03-21 00:08:49] : Difficulty changed. Now: 25000.
[2018-03-21 00:08:49] : Pool logged in.

HASHRATE REPORT - CPU
| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
|  0 |   60.0 |   59.0 |   (na) |  1 |   63.6 |   62.5 |   (na) |
|  2 |   63.4 |   62.4 |   (na) |  3 |   59.6 |   58.2 |   (na) |
-----------------------------------------------------
HASHRATE REPORT - NVIDIA
| ID |    10s |    60s |    15m |
|  0 |   36.9 |   36.9 |   (na) |
---------------------------
Totals:    283.4  278.9   (na) H/s
Highest:   298.6 H/s
```

I think this is possible to fix, and i ready to test any code.
Thanks.

# Discussion History
## minzak | 2018-11-05T13:07:32+00:00
Cool, just closed, and no any comments. No issues - no problem) 

## xmrig | 2018-11-05T13:14:48+00:00
Driver issue/wrong repository, arch:21 too slow for `cn/2`, xmr-stak aslo removed Fermi support in recent builds, and a lot of time since issue open, if you feel it still actual you can reopen it with new data.
Thank you.

## minzak | 2018-11-05T13:15:50+00:00
Thanks, it is enough to understand. 

# Action History
- Created by: minzak | 2018-03-20T22:23:59+00:00
- Closed at: 2018-11-05T13:01:02+00:00
