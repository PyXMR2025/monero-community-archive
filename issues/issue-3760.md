---
title: KawPow (rtx 2060 6gb only 5mh)
source_url: https://github.com/xmrig/xmrig/issues/3760
author: Kazbond1337
assignees: []
labels: []
created_at: '2026-01-17T16:53:04+00:00'
updated_at: '2026-01-18T16:51:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
 ```
 * ABOUT        XMRig/6.25.0 MSVC/2022 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-9700KF CPU @ 3.60GHz (1) 64-bit AES
                L2:2.0 MB L3:12.0 MB 8C/8T NUMA:1
 * MEMORY       10.3/15.9 GB (65%)
                DIMM_A0: 16 GB DDR4 @ 2667 MHz GR3200D464L22S/16G
                DIMM_A1: <empty>
                DIMM_B0: <empty>
                DIMM_B1: <empty>
 * MOTHERBOARD  Micro-Star International Co., Ltd. - H310M PRO-VDH (MS-7B29)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      de.ravencoin.herominers.com:1140 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         12.9/13.1/6.22.1
 * NVML         13.591.74/591.74 press e for health report
 * CUDA GPU     #0 01:00.0 NVIDIA GeForce RTX 2060 1680/7001 MHz smx:30 arch:75 mem:5102/6143 MB
[2026-01-17 20:49:09.741]  net      use pool de.ravencoin.herominers.com:1140  141.95.126.31
[2026-01-17 20:49:09.742]  net      new job from de.ravencoin.herominers.com:1140 diff 1073M algo kawpow height 4199118
[2026-01-17 20:49:09.743]  nvidia   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |  15728640 |     256 |  61440 |  6 |  25 |   5496 | NVIDIA GeForce RTX 2060
[2026-01-17 20:49:09.964]  nvidia   READY threads 1/1 (220 ms)
[2026-01-17 20:49:18.254]  miner    KawPow light cache for epoch 559 calculated (8289ms)
[2026-01-17 20:49:45.664]  net      new job from de.ravencoin.herominers.com:1140 diff 1073M algo kawpow height 4199119
[2026-01-17 20:49:52.087]  nvidia   KawPow DAG for epoch 559 calculated (33833ms)
[2026-01-17 20:49:58.914]  nvidia   #0 01:00.0 115W 57C 1920/6801 MHz fan0:47% fan1:47%
[2026-01-17 20:50:03.519]  nvidia   #0 01:00.0 113W 57C 1920/6801 MHz fan0:47% fan1:47%
[2026-01-17 20:50:03.664]  net      new job from de.ravencoin.herominers.com:1140 diff 1073M algo kawpow height 4199120
|   CUDA # | AFFINITY | 10s MH/s | 60s MH/s | 15m MH/s |
|        0 |       -1 |     5.19 |      n/a |      n/a | #0 01:00.0 NVIDIA GeForce RTX 2060
|        - |        - |     5.20 |      n/a |      n/a |
[2026-01-17 20:50:09.522]  miner    speed 10s/60s/15m 5.20 n/a n/a MH/s max n/a MH/s
[2026-01-17 20:50:11.138]  nvidia   #0 01:00.0 115W 58C 1920/6801 MHz fan0:47% fan1:47%
[2026-01-17 20:50:11.138]  miner    speed 10s/60s/15m 5.21 n/a n/a MH/s max 5.21 MH/s
|   CUDA # | AFFINITY | 10s MH/s | 60s MH/s | 15m MH/s |
|        0 |       -1 |     5.32 |      n/a |      n/a | #0 01:00.0 NVIDIA GeForce RTX 2060
|        - |        - |     5.22 |      n/a |      n/a |
[2026-01-17 20:50:13.119]  miner    speed 10s/60s/15m 5.22 n/a n/a MH/s max 5.22 MH/s
|   CUDA # | AFFINITY | 10s MH/s | 60s MH/s | 15m MH/s |
|        0 |       -1 |     5.32 |      n/a |      n/a | #0 01:00.0 NVIDIA GeForce RTX 2060
|        - |        - |     5.23 |      n/a |      n/a |
[2026-01-17 20:50:13.982]  miner    speed 10s/60s/15m 5.23 n/a n/a MH/s max 5.23 MH/s
|   CUDA # | AFFINITY | 10s MH/s | 60s MH/s | 15m MH/s |
|        0 |       -1 |     5.32 |      n/a |      n/a | #0 01:00.0 NVIDIA GeForce RTX 2060
|        - |        - |     5.23 |      n/a |      n/a |
[2026-01-17 20:50:14.078]  miner    speed 10s/60s/15m 5.23 n/a n/a MH/s max 5.23 MH/s

```
Hello, why is it getting only 5mh/s ? 

# Discussion History
## Kazbond1337 | 2026-01-17T17:43:58+00:00
it should get 16mh :(. can someone help me?

## geekwilliams | 2026-01-17T19:27:59+00:00
Which OS are you running? Also, why is your computer using 65% of ram when starting xmrig?  Do you have other processes running at the same time? 

## SChernykh | 2026-01-17T19:34:09+00:00
You have: `mem:5102/6143 MB`
but you run with
```
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |  15728640 |     256 |  61440 |  6 |  25 |   5496 | NVIDIA GeForce RTX 2060
```
It tries to allocate 5496 MB of memory. Try to reduce blocks from 61440 to 51200

## Kazbond1337 | 2026-01-18T05:18:05+00:00
> Which OS are you running? Also, why is your computer using 65% of ram when starting xmrig? Do you have other processes running at the same time?

Chrome and vscode


## Kazbond1337 | 2026-01-18T05:20:48+00:00
> You have: `mem:5102/6143 MB` but you run with
> 
> ```
> |  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
> |  0 |   0 | 01:00.0 |  15728640 |     256 |  61440 |  6 |  25 |   5496 | NVIDIA GeForce RTX 2060
> ```
> 
> It tries to allocate 5496 MB of memory. Try to reduce blocks from 61440 to 51200

with this values i get 10mh now
{
        "index": 0,
        "threads": 256,
        "blocks": 51200,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }

## UnixCro | 2026-01-18T15:19:30+00:00
Can someone help me?

```
MacBook  xmrig -o stratum+ssl://kawpow.auto.nicehash.com:443  -u $WALLET -p x -a kawpow  --print-time=120 --cpu-priority=0 --nicehash --no-cpu --opencl
 * ABOUT        XMRig/6.16.4 clang/12.0.5
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.9/8.0 GB (99%)
 * DONATE       10%
 * POOL #1      stratum+ssl://kawpow.auto.nicehash.com:443 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Mar  4 2023 12:44:59)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
 * CUDA         disabled
[2026-01-17 18:06:07.166]  net      use pool kawpow.auto.nicehash.com:443 TLSv1.3 35.190.124.115
[2026-01-17 18:06:07.167]  net      fingerprint (SHA-256): "ad7e0955f6dac45aa883f075ffe92b95e0bd3af32b23baf2ab6da4cba444ac82"
[2026-01-17 18:06:07.209]  net      new job from kawpow.auto.nicehash.com:443 diff 536M algo kawpow height 4199133
[2026-01-17 18:06:07.211]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   2097152 |   256 |   5581 | Apple M1
[2026-01-17 18:06:07.216]  opencl   READY threads 1/1 (4 ms)
[2026-01-17 18:06:07.219]  opencl   KawPow program for period 1399711 compiled (3ms)
[2026-01-17 18:06:07.219]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 5771362304
[2026-01-17 18:06:07.219]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE
[2026-01-17 18:06:08.620]  opencl   KawPow program for period 1399712 compiled (1401ms)
```

weird: xmrig says I don't have an L3 cache?

## SChernykh | 2026-01-18T15:41:04+00:00
Reduce intensity until you stop getting this error. You're trying to allocate too much memory. Try intensity = 524288 first.

## UnixCro | 2026-01-18T16:04:23+00:00
Thanks, but why isn't there a parameter for that?

## UnixCro | 2026-01-18T16:25:02+00:00
```
MacBook Pro: xmrig -c config.json
 * ABOUT        XMRig/6.16.4 clang/12.0.5
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.9/8.0 GB (99%)
 * DONATE       10%
 * POOL #1      kawpow.eu.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Mar  4 2023 12:44:59)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
 * CUDA         disabled
[2026-01-18 17:22:55.778]  net      use pool kawpow.eu.nicehash.com:3385  35.190.124.115
[2026-01-18 17:22:55.812]  net      new job from kawpow.eu.nicehash.com:3385 diff 536M algo kawpow height 4200526
[2026-01-18 17:22:55.814]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |    524288 |   256 |   5589 | Apple M1
[2026-01-18 17:22:55.821]  opencl   READY threads 1/1 (6 ms)
[2026-01-18 17:22:55.825]  opencl   KawPow program for period 1400175 compiled (4ms)
[2026-01-18 17:22:55.825]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 5771362304
[2026-01-18 17:22:55.825]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE
[2026-01-18 17:22:55.828]  opencl   KawPow program for period 1400176 compiled (3ms)
[2026-01-18 17:23:46.094]  config   "config.json" was changed, reloading configuration
[2026-01-18 17:23:46.099]  opencl   stopped (5 ms)
[2026-01-18 17:23:46.099]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |    224256 |   256 |   5589 | Apple M1
[2026-01-18 17:23:46.102]  opencl   READY threads 1/1 (3 ms)
[2026-01-18 17:23:46.105]  opencl   KawPow program for period 1400175 compiled (3ms)
[2026-01-18 17:23:46.105]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 5771362304
[2026-01-18 17:23:46.105]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE
[2026-01-18 17:23:46.108]  opencl   KawPow program for period 1400176 compiled (3ms)
[2026-01-18 17:23:47.159]  net      new job from kawpow.eu.nicehash.com:3385 diff 536M algo kawpow height 4200527
```

```
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       768 |   256 |   5589 | Apple M1
[2026-01-18 17:35:15.999]  opencl   READY threads 1/1 (3 ms)
[2026-01-18 17:35:16.004]  opencl   KawPow program for period 1400180 compiled (5ms)
[2026-01-18 17:35:16.004]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 5771362304
[2026-01-18 17:35:16.004]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE
```

## SChernykh | 2026-01-18T16:38:57+00:00
https://minerstat.com/dag-size-calculator says that Ravencoin DAG size is 5.375 GB = 5504 MB, so it won't help you. You need at least 5.5 GB free memory before you can mine on that systemm.

## peme14k | 2026-01-18T16:47:45+00:00
[https://github.com/xmrig/xmrig/issues/3760#issuecomment-3765400849](url)

## SChernykh | 2026-01-18T16:51:51+00:00
TLDR all 6GB GPUs will soon be unable to mine Ravencoin.

# Action History
- Created by: Kazbond1337 | 2026-01-17T16:53:04+00:00
