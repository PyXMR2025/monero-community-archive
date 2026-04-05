---
title: Ghostrider ignores affinity
source_url: https://github.com/xmrig/xmrig/issues/2733
author: RainbowMiner
assignees: []
labels: []
created_at: '2021-11-27T23:30:14+00:00'
updated_at: '2021-11-28T15:11:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

How can I make sure, that Xmrig doesn't use specific thread numbers when mining Ghostrider?

This works perfect for all other algorithms by editing the config.json but for Ghostrider. 
It seems, that it's not possible to define a proper affinity (like affinity 0xFFF5, 14 threads, on an 8core/16thread AMD for example). The usage is not predictable - at times it uses only half of all threads, at times all threads.
 

# Discussion History
## Lonnegan | 2021-11-28T00:16:18+00:00
There is a cpu section "ghostrider" and there you can configure, which cores are used. Here for example my ghostrider section in the config.json:

        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14]
        ],

The miner is instructed to use the cores 0, 2, 4, 6, 8, 10, 12 and 14. If you don't want to use the core number 10, delete the line, save the config.json and restart xmrig.

## mynerzulu | 2021-11-28T08:32:40+00:00
I seem to have the same issue.  ( on an AMD 3960x 24C/48T ).  Only 24 cores are used, I have Affinity set to use 36T.

Running on Linux Mint 20.2 (Ubuntu 20.04)
* ABOUT        XMRig/6.16.0 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen Threadripper 3960X 24-Core Processor (1) 64-bit AES
                L2:12.0 MB L3:128.0 MB 24C/48T NUMA:1
 * MEMORY       3.6/31.3 GB (12%)
                DIMM 0: <empty>
                DIMM 1: <empty>
                DIMM 0: <empty>
                DIMM_B1: 16 GB DDR4 @ 1333 MHz F4-3200C16-16GVK
                DIMM 0: <empty>
                DIMM 1: <empty>
                DIMM 0: <empty>
                DIMM_D1: 16 GB DDR4 @ 1333 MHz F4-3200C16-16GVK
 * MOTHERBOARD  Micro-Star International Co., Ltd. - TRX40 PRO 10G (MS-7C60)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://raptorna.011data.com:3032 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled




|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   111.9 |   113.7 |   225.2 |
|        1 |        1 |   164.1 |   163.5 |   218.1 |
|        2 |        2 |   164.1 |   163.8 |   218.0 |
|        3 |        3 |   123.7 |   120.5 |   228.1 |
|        4 |        4 |   163.2 |   164.2 |   218.7 |
|        5 |        5 |   164.1 |   163.9 |   218.6 |
|        6 |        6 |   121.2 |   120.0 |   227.8 |
|        7 |        7 |   161.6 |   161.5 |   217.6 |
|        8 |        8 |   161.6 |   161.9 |   217.6 |
|        9 |        9 |   119.5 |   119.0 |   228.7 |
|       10 |       10 |   162.4 |   162.3 |   217.9 |
|       11 |       11 |   161.6 |   162.0 |   217.9 |
|       12 |       12 |   131.3 |   130.3 |   238.5 |
|       13 |       13 |   163.2 |   162.7 |   218.1 |
|       14 |       14 |   162.4 |   162.1 |   218.0 |
|       15 |       15 |   133.0 |   128.4 |   237.5 |
|       16 |       16 |   163.2 |   162.7 |   218.0 |
|       17 |       17 |   162.4 |   163.0 |   218.0 |
|       18 |       18 |   126.2 |   126.3 |   234.8 |
|       19 |       19 |   160.7 |   160.9 |   217.4 |
|       20 |       20 |   159.9 |   160.7 |   217.4 |
|       21 |       21 |   124.5 |   124.9 |   234.3 |
|       22 |       22 |   160.7 |   161.2 |   217.6 |
|       23 |       23 |   161.6 |   161.3 |   217.6 |
|        - |        - |  3588.1 |  3580.7 |  5341.5 |


## SChernykh | 2021-11-28T09:18:00+00:00
> I seem to have the same issue. ( on an AMD 3960x 24C/48T ). Only 24 cores are used

XMRig runs 2 threads per core, even if it reports 24 at startup, so it's correct. Next version will display 48 threads at startup to avoid confusion.

## RainbowMiner | 2021-11-28T10:11:31+00:00
Using this config on an 8c/16t AMD Ryzen
```
"ghostrider": [
        [8, 0],
        [8, 2],
        [8, 4],
        [8, 6],
        [8, 8],
        [8, 10],
        [8, 12],
        [8, 14]
    ],
```

.. the miner starts using only the 8 cores, but as soon as the cn algorithms change to certain combinations, the load spreads to all 16 threads:

![xmrig-gr](https://user-images.githubusercontent.com/39437538/143763663-d1e3cc3b-0c6a-4eff-924a-88e1815856cb.PNG)

So it seems pretty much that a real affinity is not possible, with Xmrig's ghostrider. I have tried different intensity values (`[2,0],..`) but that causes Xmrig to fail with error.

Question: is it possible to limit the maximum load with `max-threads-hint` in config.json?


## SChernykh | 2021-11-28T10:39:21+00:00
> the miner starts using only the 8 cores, but as soon as the cn algorithms change to certain combinations, the load spreads to all 16 threads:

It's working as intended. `max-threads-hint` should work if there's no config for ghostrider in config.json yet (try values between 0 and 50).

## RainbowMiner | 2021-11-28T12:14:53+00:00
Ok, actually, that makes sense. Thank you for your quick reply.
I have got the impression, that `max-threads-hint` at 88 plus the thread setup in fact does keep the CPU load in check. Is this just wishful thinking, or is this possible?
```
"cpu": {
...
  "max-threads-hint": 88,
  "ghostrider": [
        [8, 0],
        [8, 2],
        [8, 4],
        [8, 6],
        [8, 8],
        [8, 10],
        [8, 12],
        [8, 14]
      ],
...
```

## SChernykh | 2021-11-28T15:11:27+00:00
`max-threads-hint` only works if you don't have `ghostrider` section in config.json - it's used to fill in threads there. As soon as you have it, it will ignore `max-threads-hint`.

# Action History
- Created by: RainbowMiner | 2021-11-27T23:30:14+00:00
