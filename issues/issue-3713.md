---
title: Problem with run GPU - RX 5600 XT
source_url: https://github.com/xmrig/xmrig/issues/3713
author: bmxmale
assignees: []
labels: []
created_at: '2025-09-26T11:42:46+00:00'
updated_at: '2025-09-27T07:24:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Ubuntu 24.04, configured ROCm, LLM Studio or OLLAMA work well. XMRIG failing. Any idea?

```
bmxmale@G4M3R:~/xmrig$` ./xmrig
 * ABOUT        XMRig/6.24.0 gcc/13.3.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 5 3600 6-Core Processor (1) 64-bit AES
                L2:3.0 MB L3:32.0 MB 6C/12T NUMA:1
 * MEMORY       4.1/31.3 GB (13%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://stratum.xdag.org:24655 algo rx/0
 * POOL #2      stratum+tcp://stratum.xdag.org:23655 algo rx/0
 * POOL #3      stratum+tcp://stratum.xdag.org:23656 algo rx/0
 * POOL #4      stratum+tcp://stratum.xdag.org:24656 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3662.0)
 * OPENCL GPU   #0 0a:00.0 AMD Radeon RX 5600 XT (gfx1010:xnack-) 1780 MHz cu:18 mem:5208/6128 MB
 * CUDA         disabled
[2025-09-26 13:38:39.649]  net      use pool stratum.xdag.org:24655  116.202.3.220
[2025-09-26 13:38:39.649]  net      new job from stratum.xdag.org:24655 diff 20000 algo rx/0
[2025-09-26 13:38:39.649]  cpu      use argon2 implementation AVX2
[2025-09-26 13:38:39.651]  msr      cannot read MSR 0xc0011020
[2025-09-26 13:38:39.651]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2025-09-26 13:38:39.651]  randomx  init dataset algo rx/0 (12 threads) seed e2d23d90b35d6157...
[2025-09-26 13:38:39.832]  randomx  failed to allocate RandomX dataset using 1GB pages
[2025-09-26 13:38:39.855]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (204 ms)
[2025-09-26 13:38:40.191]  net      new job from stratum.xdag.org:24655 diff 20000 algo rx/0
[2025-09-26 13:38:40.315]  net      new job from stratum.xdag.org:24655 diff 20000 algo rx/0
[2025-09-26 13:38:40.433]  net      new job from stratum.xdag.org:24655 diff 20000 algo rx/0
[2025-09-26 13:38:42.398]  randomx  dataset ready (2543 ms)
[2025-09-26 13:38:42.398]  cpu      use profile  rx  (12 threads) scratchpad 2048 KB
[2025-09-26 13:38:42.399]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 0a:00.0 |       960 |     8 |   1920 | AMD Radeon RX 5600 XT (gfx1010:xnack-)
|  1 |   0 | 0a:00.0 |       960 |     8 |   1920 | AMD Radeon RX 5600 XT (gfx1010:xnack-)
[2025-09-26 13:38:42.410]  cpu      READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (12 ms)
[2025-09-26 13:38:42.458]  cpu      accepted (1/0) diff 20000 (42 ms)
[2025-09-26 13:38:42.745]  opencl   error CL_OUT_OF_HOST_MEMORY when calling clCreateKernel for kernel randomx_run
[2025-09-26 13:38:42.745]  opencl   thread #0 failed with error CL_OUT_OF_HOST_MEMORY
[2025-09-26 13:38:43.330]  cpu      accepted (2/0) diff 20000 (41 ms)
[2025-09-26 13:38:43.535]  opencl   thread #0 self-test failed
[2025-09-26 13:38:43.541]  opencl   error CL_OUT_OF_HOST_MEMORY when calling clCreateKernel for kernel randomx_run
[2025-09-26 13:38:43.543]  opencl   thread #1 failed with error CL_OUT_OF_HOST_MEMORY
[2025-09-26 13:38:43.566]  opencl   thread #1 self-test failed
[2025-09-26 13:38:43.566]  opencl   disabled (failed to start threads)
[2025-09-26 13:38:46.318]  cpu      accepted (3/0) diff 20000 (43 ms)
[2025-09-26 13:38:47.097]  cpu      accepted (4/0) diff 20000 (46 ms)
```

# Discussion History
## geekwilliams | 2025-09-26T15:28:19+00:00
Did you run this as admin?  I noticed MSR mod was not applied

## bmxmale | 2025-09-26T19:01:59+00:00
> Did you run this as admin?  I noticed MSR mod was not applied

With sudo there is no MSR notice, but still GPU cause error and not working on mining 

## geekwilliams | 2025-09-26T22:10:27+00:00
Understood.  I do see an out of memory error related to GPU memory, and it looks like the card you're using has less than 1GB of memory free.  Is that card being used for something else while you're trying to mine with it?   

## bmxmale | 2025-09-27T07:24:08+00:00
> Understood.  I do see an out of memory error related to GPU memory, and it looks like the card you're using has less than 1GB of memory free.  Is that card being used for something else while you're trying to mine with it?   

Nothing else, this is clean Ubuntu. Years ago same setup used for ETH mining, no problem. I think xmrig have problem with this card or some setting..

# Action History
- Created by: bmxmale | 2025-09-26T11:42:46+00:00
