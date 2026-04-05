---
title: Just 1/3 of cores on new AMD Ryzen 5 PRO 4400G
source_url: https://github.com/xmrig/xmrig/issues/1921
author: xsoft
assignees: []
labels: []
created_at: '2020-10-29T11:49:17+00:00'
updated_at: '2021-04-12T14:37:37+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:37:37+00:00'
---

# Original Description
**Describe the bug**
With "AMD Ryzen 5 PRO 4400G" family CPU Im getting mined just on 1/3 of CPU. (this one is 4650G procesor)
Specially 4 of 12 cores are used (linux, htop).
XMRig/6.4.0

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
All cores mining.

**Required data**
Linux, HiveOS, Ive tested this setting on more older AMD Ryzen 3xxx. They were about  6000 - 7 000 H/s. Now Im on 2 000 - 2 500.

**Additional context**
All details (version, cpu...)

```
 * ABOUT        XMRig/6.4.0 gcc/7.4.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 5 PRO 4400G with Radeon Graphics (1) x64 AES
                L2:3.0 MB L3:8.0 MB 6C/12T NUMA:1
 * MEMORY       0.9/7.1 GB (12%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      randomxmonero.eu.nicehash.com:3380 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:60070
[2020-10-29 12:41:28.363]  config   configuration saved to: "/hive/miners/xmrig-new/xmrig/6.4.0/config.json"
 * OPENCL       disabled
 * CUDA         disabled
[2020-10-29 12:41:28.447]  net      use pool randomxmonero.eu.nicehash.com:3380  172.65.200.133
[2020-10-29 12:41:28.447]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 175843 algo rx/0 height 2218886
[2020-10-29 12:41:28.447]  cpu      use argon2 implementation AVX2
[2020-10-29 12:41:28.452]  msr      register values for "ryzen" preset has been set successfully (5 ms)
[2020-10-29 12:41:28.452]  randomx  init dataset algo rx/0 (12 threads) seed 0d053f64821ce740...
[2020-10-29 12:41:28.889]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (436 ms)
[2020-10-29 12:41:32.590]  randomx  dataset ready (3702 ms)
[2020-10-29 12:41:32.590]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2020-10-29 12:41:32.652]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (62 ms)

```


```
 1  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%]   Tasks: 63, 61 thr; 5 running
  2  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%]   Load average: 4.23 4.01 2.59
  3  [|||||||||||||||||||||||                                      33.5%]   Uptime: 00:14:18
  4  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%]
  5  [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%]
  6  [||||                                                          3.9%]
  7  [|                                                             0.7%]
  8  [|                                                             0.7%]
  9  [                                                              0.0%]
  10 [                                                              0.0%]
  11 [                                                              0.0%]
  12 [|                                                             0.7%]
  Mem[||||||||||||||||||||||||||||||||                       2.94G/7.12G]

```

# Discussion History
## Lonnegan | 2020-10-29T18:06:23+00:00
Hi,
everything is correct here. Monero mining needs 2 MB scratchpad size per thread and it's ideal for max. performance when it fits into the CPU's caches. AMD "Renoir" 4650G has only 8 MB L3 cache (precisely 2x 4 MB). So you have 8 MB last level cache and need 2 MB for each thread. That's why the miner only starts 4 threads and not more. Otherwise the system would have to access the slow DRAM.

The older Ryzen 3000 you were talking about was perhaps not an APU but a CPU (Matisse)? They have much more L3 cache, Ryzen 5/7 32 MB, Ryzen 9 64 MB L3 cache. There xmrig can start much more threads until the LLC is full; Ryzen 5/7 up to 16 threads, Ryzen 9 up to 32 threads!

You have the wrong processor for Monero mining. Consider to mine a coin, which needs less data per thread, e.g. Wownero (1 MB; you can run 8 threads) or ArQmA (256 KB; you can fully load all cores/threads without flooding the cache).

## SChernykh | 2020-10-30T08:55:00+00:00
@xsoft See the reply above. That said, if you manage to get higher hashrate with more threads or with some other thread affinity, let us know.

## mr-459 | 2020-11-17T00:04:43+00:00
there is no enough L3 chache
best to mine is mining wownero with this cpu

# Action History
- Created by: xsoft | 2020-10-29T11:49:17+00:00
- Closed at: 2021-04-12T14:37:37+00:00
