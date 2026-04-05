---
title: How to get Best perfomance for 2x Xeon Silver 4114 ?
source_url: https://github.com/xmrig/xmrig/issues/1793
author: minzak
assignees: []
labels: []
created_at: '2020-07-30T19:17:26+00:00'
updated_at: '2020-07-31T18:00:59+00:00'
type: issue
status: closed
closed_at: '2020-07-31T18:00:58+00:00'
---

# Original Description
I have 2x CPU Intel Xeon Silver 4114
And my default result like this:

```
 * ABOUT        XMRig/6.3.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Silver 4114 CPU @ 2.20GHz (2) x64 AES
                L2:20.0 MB L3:27.5 MB 20C/40T NUMA:2
 * MEMORY       9.2/754.4 GB (1%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:33865 
 * OPENCL       disabled
 * CUDA         disabled
[2020-07-30 21:00:25.478]  net      use pool pool.supportxmr.com:3333  94.130.12.30
[2020-07-30 21:00:25.478]  net      new job from pool.supportxmr.com:3333 diff 50000 algo rx/0 height 2153757
[2020-07-30 21:00:25.478]  cpu      use argon2 implementation AVX-512F
[2020-07-30 21:00:25.488]  msr      register values for "intel" preset has been set successfully (11 ms)
[2020-07-30 21:00:25.489]  randomx  init datasets algo rx/0 (40 threads) seed b0c24be761c254d1...
[2020-07-30 21:00:26.323]  randomx  #1 allocated 2080 MB huge pages 100% (834 ms)
[2020-07-30 21:00:26.323]  net      new job from pool.supportxmr.com:3333 diff 97826 algo rx/0 height 2153757
[2020-07-30 21:00:26.326]  randomx  #0 allocated 2080 MB huge pages 100% (837 ms)
[2020-07-30 21:00:26.381]  randomx  #0 allocated  256 MB huge pages 100% +JIT (55 ms)
[2020-07-30 21:00:26.381]  randomx  -- allocated 4416 MB huge pages 100% 2208/2208 (893 ms)
[2020-07-30 21:00:28.358]  randomx  #0 dataset ready (1976 ms)
[2020-07-30 21:00:29.231]  randomx  #1 dataset ready (873 ms)
[2020-07-30 21:00:29.231]  cpu      use profile  rx  (20 threads) scratchpad 2048 KB
[2020-07-30 21:00:29.620]  cpu      READY threads 20/20 (20) huge pages 100% 20/20 memory 40960 KB (388 ms)
[2020-07-30 21:00:55.926]  miner    speed 10s/60s/15m 9719.6 n/a n/a H/s max 9726.0 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   483.0 |     n/a |     n/a |
|        1 |        2 |   479.0 |     n/a |     n/a |
|        2 |        4 |   488.1 |     n/a |     n/a |
|        3 |        6 |   489.1 |     n/a |     n/a |
|        4 |        8 |   485.8 |     n/a |     n/a |
|        5 |       10 |   478.9 |     n/a |     n/a |
|        6 |       12 |   486.3 |     n/a |     n/a |
|        7 |       14 |   487.9 |     n/a |     n/a |
|        8 |       16 |   492.4 |     n/a |     n/a |
|        9 |       18 |   486.0 |     n/a |     n/a |
|       10 |        1 |   485.7 |     n/a |     n/a |
|       11 |        3 |   479.7 |     n/a |     n/a |
|       12 |        5 |   486.6 |     n/a |     n/a |
|       13 |        7 |   489.5 |     n/a |     n/a |
|       14 |        9 |   488.9 |     n/a |     n/a |
|       15 |       11 |   479.4 |     n/a |     n/a |
|       16 |       13 |   488.4 |     n/a |     n/a |
|       17 |       15 |   488.9 |     n/a |     n/a |
|       18 |       17 |   489.4 |     n/a |     n/a |
|       19 |       19 |   486.9 |     n/a |     n/a |
|        - |        - |  9719.7 |     n/a |     n/a |

```
and my config is:
```
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": true,
        "priority": 1,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    },

```

But CPU has :  **L2:20.0 MB L3:27.5 MB 20C/40T NUMA:2**
I do not believe, that it is maximum for this CPU!
How to get maximum perfomance?
Thanks.
https://github.com/xmrig/xmrig/pull/1351
https://github.com/xmrig/xmrig/issues/563

# Discussion History
## xmrig | 2020-07-31T06:08:27+00:00
It's already a good hashrate for these CPUs, you can increase it a little bit by enabling 1GB pages.
https://raw.githubusercontent.com/xmrig/xmrig/master/doc/screenshot_v5_2_0.png (older version)
Thank you.

## Lonnegan | 2020-07-31T11:34:32+00:00
Xeon Silver 4114 is not ideal for RandomX mining. The CPU doesn't have 20.0 MB L2 cache, it has 10x 1 MB L2. A RandomX thread has 2 MB scratchpad size, so the L2 cache is to small to hold the scratchpad. So we have to look at the L3 cache. It's not very big either, just 13.75 MB or room for 6 threads.

You should try Wownero instead of Monero. It uses a scratchpad size of just 1 MB and would fit into the L2s perfectly :)

## minzak | 2020-07-31T18:00:58+00:00
Yes, currently - it is the maximum.
But I think it is possible to use some L3 cache, but not now, yet.

# Action History
- Created by: minzak | 2020-07-30T19:17:26+00:00
- Closed at: 2020-07-31T18:00:58+00:00
