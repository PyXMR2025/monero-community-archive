---
title: Hilariously low GhostRider hashrate on Epyc 7351
source_url: https://github.com/xmrig/xmrig/issues/3204
author: arpadboda
assignees: []
labels: []
created_at: '2023-02-01T12:23:05+00:00'
updated_at: '2023-02-01T19:28:00+00:00'
type: issue
status: closed
closed_at: '2023-02-01T19:27:59+00:00'
---

# Original Description
Hey,

I'm trying to run xmrig on an Epyc 7351. 
Gigabyte MZ32-AR0 mobo, only 1 memory for testing purpose in c1 slot. 

The results are disappointing, less than 500H/s. 
Okay, this is Zen1, but a 16 core cpu with 64M cache, my old Ryzen 2700 did way better than this.

I think there is something wrong either in the miner's default config for this case or bios or something, so all the hints are welcome.

Happy to attach additional logs or configs, just tell me what you need.

Logs below:

```
Miner:   xmrig-new
Fork:    xmrig
Version: 6.18.1

XMRIG_NEW_CPU_CONFIG is empty, useing autoconfig
OPENCL is disabled
CUDA is disabled

 * ABOUT        XMRig/6.18.1 gcc/9.3.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7351 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:4
 * MEMORY       0.7/15.5 GB (5%)
                DIMM_P0_C1: 16 GB DDR4 @ 2400 MHz M393A2K43CB2-CTD    
 * MOTHERBOARD  GIGABYTE - MZ32-AR0-00
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      eu.flockpool.com:4444 algo ghostrider
 * POOL #2      us.flockpool.com:4444 algo ghostrider
 * POOL #3      us-west.flockpool.com:4444 algo ghostrider
 * POOL #4      asia.flockpool.com:4444 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:60070 
[2023-02-01 14:16:41.071]  config   configuration saved to: "/hive/miners/xmrig-new/xmrig/6.18.1/config.json"
[2023-02-01 14:16:41.144]  net      use pool eu.flockpool.com:4444  23.88.72.40
[2023-02-01 14:16:41.144]  net      new job from eu.flockpool.com:4444 diff 9342 algo ghostrider height 497515
[2023-02-01 14:16:41.147]  msr      register values for "ryzen_17h" preset have been set successfully (3 ms)
[2023-02-01 14:16:42.525]  cpu      use profile  ghostrider  (16 threads) scratchpad 2048 KB
[2023-02-01 14:16:42.526] CPU #04 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #05 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #08 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #06 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #09 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #12 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #13 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #10 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #15 warning: "can't bind memory"
[2023-02-01 14:16:42.526] CPU #11 warning: "can't bind memory"
[2023-02-01 14:16:42.527] CPU #14 warning: "can't bind memory"
[2023-02-01 14:16:42.527] CPU #07 warning: "can't bind memory"
[2023-02-01 14:16:43.167]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2023-02-01 14:16:43.167]  cpu      GhostRider algo 2: cn/dark (512 KB)
[2023-02-01 14:16:43.167]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)
[2023-02-01 14:16:43.715]  cpu      READY threads 32/32 (128) huge pages 100% 128/128 memory 262144 KB (1190 ms)
[2023-02-01 14:17:10.006]  net      new job from eu.flockpool.com:4444 diff 9342 algo ghostrider height 497516
[2023-02-01 14:17:10.009]  cpu      GhostRider algo 1: cn/dark (512 KB)
[2023-02-01 14:17:10.009]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2023-02-01 14:17:10.009]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)
[2023-02-01 14:17:29.922]  net      new job from eu.flockpool.com:4444 diff 19669 algo ghostrider height 497517
[2023-02-01 14:17:30.052]  cpu      GhostRider algo 1: cn/turtle (256 KB)
[2023-02-01 14:17:30.052]  cpu      GhostRider algo 2: cn/turtle-lite (128 KB)
[2023-02-01 14:17:30.052]  cpu      GhostRider algo 3: cn/dark (512 KB)
[2023-02-01 14:17:37.173]  cpu      accepted (1/0) diff 19669 (25 ms)
[2023-02-01 14:17:42.105]  miner    speed 10s/60s/15m 484.7 n/a n/a H/s max 484.8 H/s avg 232.3 H/s
```


# Discussion History
## Spudz76 | 2023-02-01T13:33:53+00:00
Disable hwloc, "can't bind" is serious problem

## arpadboda | 2023-02-01T13:50:32+00:00
@Spudz76 how to do that?

## Spudz76 | 2023-02-01T14:11:55+00:00
recompile with `-DWITH_HWLOC=OFF` there is no runtime disablement

or maybe there is a newer bios for the board without hwloc bugs

or only having one DIMM when there are four NUMA nodes (probably need one DIMM per NUMA)

what hwloc and NUMA do is ensure a CPU is using memory locally wired to itself, can't bind means there was no memory directly wired for that NUMA node (aka memory controller)  you seem to have four NUMA nodes but one DIMM so the other three must ask the directly wired one to hand-off data instead of being direct

## Spudz76 | 2023-02-01T14:12:45+00:00
There could be bios option for disabling NUMA and then it might work

## arpadboda | 2023-02-01T19:27:59+00:00
Thanks @Spudz76 , I installed 4 mem sticks and it works as expected. 
Also many thanks for the quick reply and detailed explanation! 

# Action History
- Created by: arpadboda | 2023-02-01T12:23:05+00:00
- Closed at: 2023-02-01T19:27:59+00:00
