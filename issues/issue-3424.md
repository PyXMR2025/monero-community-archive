---
title: Failed to set MSR on Ubuntu Zen4 laptop
source_url: https://github.com/xmrig/xmrig/issues/3424
author: bringfido-adams
assignees: []
labels: []
created_at: '2024-02-18T18:38:46+00:00'
updated_at: '2024-02-19T19:24:09+00:00'
type: issue
status: closed
closed_at: '2024-02-19T19:24:09+00:00'
---

# Original Description
**Describe the bug**
Receive `FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW` error message while running xmrig on a Ryzen 7940HS laptop (Zen4 Phoenix architecture) running Ubuntu 22.04.

Using grub modification here https://github.com/xmrig/xmrig/issues/2098#issuecomment-791762724

I noticed that it is not detecting the architecture correctly by default so I set wrmsr manually in the config file:

`"wrmsr": ["0xc0011020:0x4400000000000", "0xc0011021:0x4000000000040", "0xc0011022:0x8680000401570000", "0xc001102b:0x2040cc10"],`

I used the values found in https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh

**To Reproduce**
Run `sudo ./xmrig`

**Expected behavior**
Should set MSR values.

**Required data**
```
 * ABOUT        XMRig/6.21.0 gcc/5.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 9 7940HS w/ Radeon 780M Graphics (1) 64-bit AES
                L2:8.0 MB L3:16.0 MB 8C/16T NUMA:2
 * MEMORY       1.9/46.4 GB (4%)
                DIMM_A0: 16 GB DDR5 @ 4800 MHz MTC8C1084S1SC48BA1  
                DIMM_B0: 32 GB DDR5 @ 4800 MHz CMSX32GX5M1A4800C40
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - GA402XV
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      donate.v2.xmrig.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-02-18 12:30:54.621]  net      use pool donate.v2.xmrig.com:3333  199.247.27.41
[2024-02-18 12:30:54.621]  net      new job from donate.v2.xmrig.com:3333 diff 1000K algo rx/0 height 3087120 (46 tx)
[2024-02-18 12:30:54.621]  cpu      use argon2 implementation AVX-512F
[2024-02-18 12:30:54.622]  msr      cannot set MSR 0xc0011020 to 0x0004400000000000
[2024-02-18 12:30:54.622]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-02-18 12:30:54.622]  randomx  init datasets algo rx/0 (16 threads) seed c30a87fd4238c912...
[2024-02-18 12:30:55.049]  randomx  #1 allocated 3072 MB huge pages 100% (428 ms)
[2024-02-18 12:30:55.393]  randomx  #0 allocated 3072 MB huge pages 100% (772 ms)
[2024-02-18 12:30:55.393]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (772 ms)
[2024-02-18 12:30:57.668]  randomx  #1 dataset ready (2274 ms)
[2024-02-18 12:30:57.793]  randomx  #0 dataset ready (126 ms)
[2024-02-18 12:30:57.793]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2024-02-18 12:30:57.800]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (6 ms)
[2024-02-18 12:30:59.182]  signal   Ctrl+C received, exiting
[2024-02-18 12:30:59.185]  cpu      stopped (2 ms)
[2024-02-18 12:30:59.185]  msr      cannot set MSR 0xc0011020 to 0x0004400000000000
[2024-02-18 12:30:59.185]  msr      failed to restore initial state (0 ms)
```

**Additional context**
Please ignore my RAM not being in 2 channel mode :3rd_place_medal: 


# Discussion History
## geekwilliams | 2024-02-18T19:13:39+00:00
Have you disabled secure boot? 

## bringfido-adams | 2024-02-19T19:24:09+00:00
No. Disabling it worked. Thank you for the help!

# Action History
- Created by: bringfido-adams | 2024-02-18T18:38:46+00:00
- Closed at: 2024-02-19T19:24:09+00:00
