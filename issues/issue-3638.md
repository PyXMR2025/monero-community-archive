---
title: Network freeze
source_url: https://github.com/xmrig/xmrig/issues/3638
author: team-boo
assignees: []
labels: []
created_at: '2025-02-22T10:45:02+00:00'
updated_at: '2025-03-21T08:11:14+00:00'
type: issue
status: closed
closed_at: '2025-03-21T08:11:13+00:00'
---

# Original Description
When i use more than 50% of resource on mining network stop.
When i use around 20-30% network is slow.

This has to do with CPU-intensive task as is wrote  here  
https://github.com/xmrig/xmrig/issues/3173

This is serious and must be a fix for this.

I can give access to  SChernykh or anyone else that can find what is happening and fix it.


# Discussion History
## SChernykh | 2025-02-24T10:15:55+00:00
**Required data**
 - XMRig version
    - Either the exact link to a release you downloaded from https://github.com/xmrig/xmrig/releases
    - Or the exact command lines that you used to build XMRig
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.


## team-boo | 2025-03-10T07:36:58+00:00
Hello,

"git clone --recursive https://github.com/xmrig/xmrig/ && mkdir xmrig/build && cd xmrig/scripts && ./build_deps.sh && cd ../build && cmake .. -DXMRIG_DEPS=scripts/deps && make"

"./xmrig --cpu-max-threads-hint=20 -o ip:3333"

When i change from 20 to 50 network freezes.

Debian 12.

https://pastebin.com/vHRCU8n0    XMrig logs

Thank you.




## SChernykh | 2025-03-10T08:07:45+00:00
What is your CPU and how many threads does XMRig run with hint=20 and hint=50?

## team-boo | 2025-03-10T08:20:24+00:00
I have 8 E7-8880 V4 .

How to check with how many threads xmrig run?

I just run "./xmrig --cpu-max-threads-hint=20"

## team-boo | 2025-03-10T08:24:34+00:00
I thought that the problem was network card but even after changing driver from r8169 to r8168 
nothing changed.

## SChernykh | 2025-03-10T09:08:55+00:00
> How to check with how many threads xmrig run?

XMRig prints it when it starts mining - "READY threads X/Y ..."

## team-boo | 2025-03-10T09:16:22+00:00
*************************************************************************
 * ABOUT        XMRig/6.22.2 gcc/12.2.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E7-8880 v4 @ 2.20GHz (4) 64-bit AES
                L2:22.0 MB L3:220.0 MB 88C/176T NUMA:8
 * MEMORY       29.3/346.1 GB (8%)
                DIMM 9: 32 GB DDR4 @ 1333 MHz HMA84GR7MFR4N-TF    
                DIMM 9: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 15: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 9: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 15: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 9: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 15: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 9: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 15: 32 GB DDR4 @ 1333 MHz M393A4K40BB1-CRC    
                DIMM 9: 32 GB DDR4 @ 2133 MHz HMA84GR7MFR4N-TF    
                DIMM 15: 32 GB DDR4 @ 1333 MHz HMA84GR7MFR4N-TF    
                DIMM 9: 32 GB DDR4 @ 1333 MHz HMA84GR7MFR4N-TF    
 * MOTHERBOARD  LENOVO - 00YA741
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      1.1.1.1:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2025-03-10 11:15:07.395]  net      use pool 1.1.1.1:3333  1.1.1.1
[2025-03-10 11:15:07.395]  net      new job from 1.1.1.1:3333 diff 500054 algo rx/0 height 3364581 (114 tx)
[2025-03-10 11:15:07.395]  cpu      use argon2 implementation AVX2
[2025-03-10 11:15:07.401]  msr      register values for "intel" preset have been set successfully (6 ms)
[2025-03-10 11:15:07.401]  randomx  init datasets algo rx/0 (35 threads) seed 3732d1bfedb742fe...
[2025-03-10 11:15:08.260]  randomx  #0 allocated 2080 MB huge pages 100% (859 ms)
[2025-03-10 11:15:09.025]  randomx  #1 allocated 2080 MB huge pages 100% (1623 ms)
[2025-03-10 11:15:09.740]  randomx  #2 allocated 2080 MB huge pages 100% (2337 ms)
[2025-03-10 11:15:09.897]  net      new job from 1.1.1.1:3333 diff 500054 algo rx/0 height 3364582 (2 tx)
[2025-03-10 11:15:11.383]  net      new job from 1.1.1.1:3333 diff 500054 algo rx/0 height 3364582 (2 tx)
[2025-03-10 11:15:15.693]  randomx  #4 allocated 2080 MB huge pages 100% (8292 ms)
[2025-03-10 11:15:15.693]  randomx  #6 allocated 2080 MB huge pages 100% (8291 ms)
[2025-03-10 11:15:15.694]  randomx  #5 allocated 2080 MB huge pages 100% (8291 ms)
[2025-03-10 11:15:15.694]  randomx  #7 allocated 2080 MB huge pages 100% (8291 ms)
[2025-03-10 11:15:15.696]  randomx  #0 allocated  256 MB huge pages   0% +JIT (2 ms)
[2025-03-10 11:15:15.696]  randomx  -- allocated 14816 MB huge pages  98% 7280/7408 (8295 ms)
[2025-03-10 11:15:20.609]  randomx  #0 dataset ready (4913 ms)
[2025-03-10 11:15:21.527]  randomx  #1 dataset ready (918 ms)
[2025-03-10 11:15:21.528]  randomx  #5 dataset ready (918 ms)
[2025-03-10 11:15:21.528]  randomx  #7 dataset ready (918 ms)
[2025-03-10 11:15:21.528]  randomx  #2 dataset ready (918 ms)
[2025-03-10 11:15:21.528]  randomx  #4 dataset ready (918 ms)
[2025-03-10 11:15:22.172]  randomx  #6 dataset ready (1562 ms)
[2025-03-10 11:15:22.172]  cpu      use profile  rx  (35 threads) scratchpad 2048 KB
[2025-03-10 11:15:22.269]  cpu      READY threads 35/35 (35) huge pages 100% 35/35 memory 71680 KB (97 ms)

## SChernykh | 2025-03-10T10:12:23+00:00
E7-8880 V4 is a 22-core CPU, so you should have 176 cores/352 threads in your system with 8 CPUs. You only have half of that. Also, you only have 12 memory sticks for 8 CPUs which is a very weird setup and can result in performance issues (E7-8880 V4 is a quad-channel CPU, so it needs 4 sticks per CPU for optimal performance). In any case, you can try to disable NUMA in XMRig (`--randomx-no-numa` in the command line) because this can be a source of issues on such a weird system.

## team-boo | 2025-03-11T12:22:52+00:00
After "--randomx-no-numa" the only thing that changed was hash rate that was lowered to 9000.
When hash rate is low i dont have network issue so something else is happening.

## team-boo | 2025-03-21T08:11:13+00:00
I closed this because the reason was something else.
When iptable has a lot of rules network freezes.

Nothing to do with xmrig.

# Action History
- Created by: team-boo | 2025-02-22T10:45:02+00:00
- Closed at: 2025-03-21T08:11:13+00:00
