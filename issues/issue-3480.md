---
title: Segmentation fault when using opencl for cn/2 algo
source_url: https://github.com/xmrig/xmrig/issues/3480
author: OPPO9008
assignees: []
labels: []
created_at: '2024-05-19T06:02:14+00:00'
updated_at: '2025-06-18T22:14:15+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:14:15+00:00'
---

# Original Description
**Describe the bug**
Segmentation fault when using opencl for cn/2 algo

**To Reproduce**
Turn opencl on in the config, setting "enabled" to "true" in the opencl block of config.json

**Expected behavior**
Mining would begin

**Required data**
```
* ABOUT        XMRig/6.21.3-C3Pool clang/18.1.5 (built for Android ARMv8, 64 bit)       * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported                                                                * 1GB PAGES    unavailable
 * CPU          Qualcomm Kryo-4XX-Silver (2) 64-bit AES
                L2:0.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       3.1/5.4 GB (57%)
 * DONATE       0%
 * POOL #1      auto.c3pool.org:19999 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 QUALCOMM Snapdragon(TM)/OpenCL 2.0 QUALCOMM build: commit #9b824c0bed changeid #I6c7bff0fbd Date: 10/09/21 Sat Local Branch:  Remote Branch:
 * OPENCL GPU   #0 n/a QUALCOMM Adreno(TM) 1 MHz cu:1 mem:696/2784 MB
[2024-05-17 22:09:51.946]  config   configuration saved to: "config.json"
[2024-05-17 22:09:51.946]  benchmk   STARTING ALGO PERFORMANCE CALIBRATION (with 20 seconds round)
[2024-05-17 22:09:51.946]  benchmk   Algo ghostrider Preparation
[2024-05-17 22:09:51.946]  cpu      use profile  ghostrider  (8 threads) scratchpad 2048 KB
[2024-05-17 22:09:51.947]  opencl   disabled (no suitable configuration found)
[2024-05-17 22:09:53.442]  cpu      GhostRider algo 1: cn/dark (512 KB)
[2024-05-17 22:09:53.442]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2024-05-17 22:09:53.442]  cpu      GhostRider algo 3: cn/turtle (256 KB)
[2024-05-17 22:09:53.990]  cpu      READY threads 8/8 (64) huge pages 0% 0/64 memory 131072 KB (2044 ms)
[2024-05-17 22:09:58.691]  benchmk   Algo ghostrider Starting test
[2024-05-17 22:10:21.962]  miner    speed 10s/60s/15m 57.22 n/a n/a H/s max 61.43 H/s avg 53.92 H/s
[2024-05-17 22:10:25.940]  benchmk   Algo ghostrider hashrate: 59.739167
[2024-05-17 22:10:25.940]  benchmk   Algo cn/r Preparation
[2024-05-17 22:10:26.913]  cpu      stopped (973 ms)
[2024-05-17 22:10:26.913]  cpu      use profile  cn/2  (8 threads) scratchpad 2048 KB
[2024-05-17 22:10:26.947]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       280 |     8 |    560 | QUALCOMM Adreno(TM)
[2024-05-17 22:10:28.072]  opencl   GPU #0 compiling...
[2024-05-17 22:10:35.415]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (8502 ms)
Segmentation fault
```

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2024-05-19T07:29:44+00:00
> XMRig/6.21.3-C3Pool

This is not the original XMRig, but a heavily modified version, please report this bug to C3Pool. We can't fix software that wasn't created by the original authors.

If you can reproduce the crash with the original binary downloaded from https://github.com/xmrig/xmrig/releases/latest - please post the full config here.

# Action History
- Created by: OPPO9008 | 2024-05-19T06:02:14+00:00
- Closed at: 2025-06-18T22:14:15+00:00
