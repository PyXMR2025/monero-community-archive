---
title: '[BUG] Out of memory with new CUDA Plugin v6.15.0 / Xmrig v6.15.0 / Windows
  10'
source_url: https://github.com/xmrig/xmrig/issues/2569
author: RainbowMiner
assignees: []
labels: []
created_at: '2021-08-31T09:31:02+00:00'
updated_at: '2021-08-31T11:06:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The new CUDA plugin v6.15.0 + Xmrig v6.15.0 seems to have memory problems on Windows 10, Nvidia Driver v466.74. This happens for many algorithms, including AstroBWT, RandomX, RandomXGraft, KawPow. All cryptonight algorithms plus RandomArq mining worked good.
For testing, I have replaced the CUDA plugin with the prior v6.12.0 + Xmrig v6.15.0 and the memory problems don't appear any more.


```
 * ABOUT        XMRig/6.15.0 MSVC/2019
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Pentium(R) CPU G4560 @ 3.50GHz (1) 64-bit AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       4.8/7.9 GB (61%)
                ChannelA-DIMM0: <empty>
                DIMM_A1: 4 GB DDR4 @ 2133 MHz KHX2133C14D4/4G
                ChannelB-DIMM0: <empty>
                DIMM_B1: 4 GB DDR4 @ 2133 MHz KHX2133C14D4/4G
 * MOTHERBOARD  MSI - Z170A GAMING PRO CARBON (MS-7A12)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://kawpow.mine.zergpool.com:3638 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:35006
 * OPENCL       disabled
 * CUDA         11.3/11.3/6.15.0
 * NVML         disabled
 * CUDA GPU     #6 09:00.0 NVIDIA GeForce RTX 3070 1905/7001 MHz smx:46 arch:86 mem:6686/8192 MB
[2021-08-31 11:26:53.874]  net      use pool kawpow.mine.zergpool.com:3638  51.210.180.98
[2021-08-31 11:26:53.875]  net      new job from kawpow.mine.zergpool.com:3638 diff 2155M algo kawpow height 1909397
[2021-08-31 11:26:53.875]  nvidia   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   6 | 09:00.0 |  24117248 |     256 |  94208 |  6 |  25 |   3056 | NVIDIA GeForce RTX 3070
[2021-08-31 11:26:55.077]  nvidia   thread #0 failed with error <cryptonight_extra_cpu_init>:379 "out of memory"
[2021-08-31 11:26:55.172]  nvidia   thread #0 self-test failed
[2021-08-31 11:26:55.172]  nvidia   disabled (failed to start threads)
```


# Discussion History
## RainbowMiner | 2021-08-31T09:43:12+00:00
Here is another one, trying to mine RandomX
```
 * CUDA GPU     #6 09:00.0 NVIDIA GeForce RTX 3070 1905/7001 MHz smx:46 arch:86 mem:6686/8192 MB
[2021-08-31 11:41:29.694]  net      use pool rx-eu.unmineable.com:3333  159.65.30.104
[2021-08-31 11:41:29.694]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439047 (42 tx)
[2021-08-31 11:41:29.695]  cpu      use argon2 implementation SSSE3
[2021-08-31 11:41:29.750]  msr      register values for "intel" preset have been set successfully (55 ms)
[2021-08-31 11:41:29.750]  randomx  init dataset algo rx/0 (4 threads) seed 872505fbda609445...
[2021-08-31 11:41:29.779]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (29 ms)
[2021-08-31 11:41:35.492]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439047 (42 tx)
[2021-08-31 11:41:43.142]  randomx  dataset ready (13363 ms)
[2021-08-31 11:41:43.142]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   6 | 09:00.0 |      2208 |      32 |     69 |  6 |  25 |   4416 | NVIDIA GeForce RTX 3070
[2021-08-31 11:41:44.173]  nvidia   READY threads 1/1 (1028 ms)
[2021-08-31 11:41:48.183]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-08-31 11:41:48.827]  nvidia   thread #0 failed with error <randomx_prepare>:43 "out of memory"
```

This is AstroBWT:
```
 * CUDA GPU     #6 09:00.0 NVIDIA GeForce RTX 3070 1905/7001 MHz smx:46 arch:86 mem:6686/8192 MB
[2021-08-31 11:41:29.694]  net      use pool rx-eu.unmineable.com:3333  159.65.30.104
[2021-08-31 11:41:29.694]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439047 (42 tx)
[2021-08-31 11:41:29.695]  cpu      use argon2 implementation SSSE3
[2021-08-31 11:41:29.750]  msr      register values for "intel" preset have been set successfully (55 ms)
[2021-08-31 11:41:29.750]  randomx  init dataset algo rx/0 (4 threads) seed 872505fbda609445...
[2021-08-31 11:41:29.779]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (29 ms)
[2021-08-31 11:41:35.492]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439047 (42 tx)
[2021-08-31 11:41:43.142]  randomx  dataset ready (13363 ms)
[2021-08-31 11:41:43.142]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   6 | 09:00.0 |      2208 |      32 |     69 |  6 |  25 |   4416 | NVIDIA GeForce RTX 3070
[2021-08-31 11:41:44.173]  nvidia   READY threads 1/1 (1028 ms)
[2021-08-31 11:41:48.183]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-08-31 11:41:48.827]  nvidia   thread #0 failed with error <randomx_prepare>:43 "out of memory"
```

Here is RandomXGraft

```
 * CUDA GPU     #6 09:00.0 NVIDIA GeForce RTX 3070 1905/7001 MHz smx:46 arch:86 mem:6686/8192 MB
[2021-08-31 12:21:32.369]  net      use pool gulf.moneroocean.stream:10032  195.201.124.214
[2021-08-31 12:21:32.370]  net      new job from gulf.moneroocean.stream:10032 diff 45744 algo rx/graft height 945359 (1 tx)
[2021-08-31 12:21:32.370]  cpu      use argon2 implementation SSSE3
[2021-08-31 12:21:32.400]  msr      register values for "intel" preset have been set successfully (30 ms)
[2021-08-31 12:21:32.400]  randomx  init dataset algo rx/graft (4 threads) seed 7f856bda85faa24c...
[2021-08-31 12:21:32.582]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (182 ms)
[2021-08-31 12:21:41.670]  randomx  dataset ready (9088 ms)
[2021-08-31 12:21:41.671]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   6 | 09:00.0 |      2208 |      32 |     69 |  6 |  25 |   4416 | NVIDIA GeForce RTX 3070
[2021-08-31 12:21:42.480]  nvidia   READY threads 1/1 (809 ms)
[2021-08-31 12:21:46.109]  nvidia   thread #0 failed with error <randomx_prepare>:43 "out of memory"
```

## RainbowMiner | 2021-08-31T11:06:51+00:00
Here is RandomX mining with the prior CUDA plugin v6.12.0:

```
 * ABOUT        XMRig/6.15.0 MSVC/2019
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Pentium(R) CPU G4560 @ 3.50GHz (1) 64-bit AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       3.7/7.9 GB (47%)
                ChannelA-DIMM0: <empty>
                DIMM_A1: 4 GB DDR4 @ 2133 MHz KHX2133C14D4/4G
                ChannelB-DIMM0: <empty>
                DIMM_B1: 4 GB DDR4 @ 2133 MHz KHX2133C14D4/4G
 * MOTHERBOARD  MSI - Z170A GAMING PRO CARBON (MS-7A12)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://rx-eu.unmineable.com:3333 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:35006
 * OPENCL       disabled
 * CUDA         11.3/11.3/6.12.0
 * NVML         disabled
 * CUDA GPU     #6 09:00.0 NVIDIA GeForce RTX 3070 1905/7001 MHz smx:46 arch:86 mem:6686/8192 MB
[2021-08-31 13:03:33.101]  net      use pool rx-eu.unmineable.com:3333  159.65.30.104
[2021-08-31 13:03:33.102]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439079 (82 tx)
[2021-08-31 13:03:33.102]  cpu      use argon2 implementation SSSE3
[2021-08-31 13:03:33.191]  msr      register values for "intel" preset have been set successfully (89 ms)
[2021-08-31 13:03:33.192]  randomx  init dataset algo rx/0 (4 threads) seed 872505fbda609445...
[2021-08-31 13:03:33.205]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (13 ms)
[2021-08-31 13:03:47.145]  randomx  dataset ready (13939 ms)
[2021-08-31 13:03:47.145]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   6 | 09:00.0 |      2208 |      32 |     69 |  6 |  25 |   4416 | NVIDIA GeForce RTX 3070
[2021-08-31 13:03:47.879]  nvidia   READY threads 1/1 (733 ms)
[2021-08-31 13:03:51.328]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439079 (82 tx)
[2021-08-31 13:03:52.150]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-08-31 13:04:02.219]  net      new job from rx-eu.unmineable.com:3333 diff 100001 algo rx/0 height 2439080 (19 tx)
[2021-08-31 13:04:02.297]  nvidia   accepted (1/0) diff 100001 (71 ms)
```

.. works perfect.

Also, AstroBWT mining with CUDA plugin v6.12.0 with xmrig v6.15.0:

```
 * OPENCL       disabled
 * CUDA         11.3/11.3/6.12.0
 * NVML         disabled
 * CUDA GPU     #6 09:00.0 NVIDIA GeForce RTX 3070 1905/7001 MHz smx:46 arch:86 mem:6686/8192 MB
[2021-08-31 12:57:30.190]  net      use pool gulf.moneroocean.stream:10032  195.201.124.214
[2021-08-31 12:57:30.202]  net      new job from gulf.moneroocean.stream:10032 diff 4323 algo astrobwt height 6114555
[2021-08-31 12:57:30.203]  nvidia   use profile  astrobwt  (1 thread) scratchpad 20480 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   6 | 09:00.0 |       672 |      32 |     21 |  6 |  25 |   6248 | NVIDIA GeForce RTX 3070
[2021-08-31 12:57:31.190]  nvidia   READY threads 1/1 (987 ms)
[2021-08-31 12:57:35.373]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-08-31 12:57:35.501]  nvidia   accepted (1/0) diff 4323 (60 ms)
```

# Action History
- Created by: RainbowMiner | 2021-08-31T09:31:02+00:00
