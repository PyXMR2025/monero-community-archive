---
title: 'CPU #00 warning: "can''t bind memory"'
source_url: https://github.com/xmrig/xmrig/issues/3604
author: ropyu1978
assignees: []
labels: []
created_at: '2024-12-18T10:15:01+00:00'
updated_at: '2025-06-16T19:14:43+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:14:43+00:00'
---

# Original Description
```
* ABOUT        XMRig/6.22.2 MSVC/2019 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD EPYC 7B12 64-Core Processor (2) 64-bit AES
                L2:64.0 MB L3:512.0 MB 128C/256T NUMA:2
 * MEMORY       6.7/255.9 GB (3%)
                DIMM_A1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_A2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_B1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_B2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_C1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_C2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_D1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_D2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_I1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_I2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_J1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_J2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_K1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_K2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_L1: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
                DIMM_L2: 16 GB DDR4 @ 2400 MHz M393A2G40DB1-CRC
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - KNPP-D32-R Series
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      51.79.215.200:17084 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-12-18 14:26:57.867]  net      use pool 51.79.215.200:17084  51.79.215.200
[2024-12-18 14:26:57.868]  net      new job from 51.79.215.200:17084 diff 49349 algo ghostrider height 18575
[2024-12-18 14:27:02.038]  msr      register values for "ryzen_17h" preset have been set successfully (4170 ms)
[2024-12-18 14:27:03.325]  cpu      use profile  ghostrider  (126 threads) scratchpad 2048 KB
[2024-12-18 14:27:03.331] CPU #00 warning: "can't bind memory"
[2024-12-18 14:27:03.332] CPU #52 warning: "can't bind memory"
[2024-12-18 14:27:03.332] CPU #04 warning: "can't bind memory"
[2024-12-18 14:27:03.332] CPU #08 warning: "can't bind memory"
[2024-12-18 14:27:03.333] CPU #14 warning: "can't bind memory"
[2024-12-18 14:27:03.333] CPU #10 warning: "can't bind memory"
[2024-12-18 14:27:03.333] CPU #94 warning: "can't bind memory"
[2024-12-18 14:27:03.333] CPU #104 warning: "can't bind memory"
[2024-12-18 14:27:03.333] CPU #24 warning: "can't bind memory"
[2024-12-18 14:27:03.334] CPU #68 warning: "can't bind memory"
[2024-12-18 14:27:03.334] CPU #16 warning: "can't bind memory"
[2024-12-18 14:27:03.334] CPU #42 warning: "can't bind memory"
[2024-12-18 14:27:03.334] CPU #118 warning: "can't bind memory"
[2024-12-18 14:27:03.334] CPU #28 warning: "can't bind memory"
[2024-12-18 14:27:03.335] CPU #58 warning: "can't bind memory"
[2024-12-18 14:27:03.335] CPU #142 warning: "can't bind memory"
[2024-12-18 14:27:03.335] CPU #06 warning: "can't bind memory"
[2024-12-18 14:27:03.335] CPU #36 warning: "can't bind memory"
[2024-12-18 14:27:03.335] CPU #206 warning: "can't bind memory"
[2024-12-18 14:27:03.335] CPU #216 warning: "can't bind memory"
[2024-12-18 14:27:03.336] CPU #220 warning: "can't bind memory"
[2024-12-18 14:27:03.336] CPU #34 warning: "can't bind memory"
[2024-12-18 14:27:03.336] CPU #74 warning: "can't bind memory"
[2024-12-18 14:27:03.336] CPU #72 warning: "can't bind memory"
[2024-12-18 14:27:03.336] CPU #50 warning: "can't bind memory"
[2024-12-18 14:27:03.336] CPU #12 warning: "can't bind memory"
[2024-12-18 14:27:03.337] CPU #198 warning: "can't bind memory"
[2024-12-18 14:27:03.337] CPU #76 warning: "can't bind memory"
[2024-12-18 14:27:03.337] CPU #84 warning: "can't bind memory"
[2024-12-18 14:27:03.337] CPU #162 warning: "can't bind memory"
[2024-12-18 14:27:03.337] CPU #88 warning: "can't bind memory"
[2024-12-18 14:27:03.337] CPU #90 warning: "can't bind memory"
[2024-12-18 14:27:03.338] CPU #92 warning: "can't bind memory"
[2024-12-18 14:27:03.338] CPU #26 warning: "can't bind memory"
[2024-12-18 14:27:03.338] CPU #238 warning: "can't bind memory"
[2024-12-18 14:27:03.338] CPU #22 warning: "can't bind memory"
[2024-12-18 14:27:03.338] CPU #02 warning: "can't bind memory"
[2024-12-18 14:27:03.338] CPU #106 warning: "can't bind memory"
[2024-12-18 14:27:03.339] CPU #78 warning: "can't bind memory"
[2024-12-18 14:27:03.339] CPU #114 warning: "can't bind memory"
[2024-12-18 14:27:03.339] CPU #56 warning: "can't bind memory"
[2024-12-18 14:27:03.339] CPU #120 warning: "can't bind memory"
[2024-12-18 14:27:03.339] CPU #122 warning: "can't bind memory"
[2024-12-18 14:27:03.339] CPU #128 warning: "can't bind memory"
[2024-12-18 14:27:03.340] CPU #130 warning: "can't bind memory"
[2024-12-18 14:27:03.340] CPU #44 warning: "can't bind memory"
[2024-12-18 14:27:03.340] CPU #134 warning: "can't bind memory"
[2024-12-18 14:27:03.340] CPU #136 warning: "can't bind memory"
[2024-12-18 14:27:03.340] CPU #138 warning: "can't bind memory"
[2024-12-18 14:27:03.340] CPU #98 warning: "can't bind memory"
[2024-12-18 14:27:03.341] CPU #100 warning: "can't bind memory"
[2024-12-18 14:27:03.341] CPU #102 warning: "can't bind memory"
[2024-12-18 14:27:03.341] CPU #186 warning: "can't bind memory"
[2024-12-18 14:27:03.341] CPU #192 warning: "can't bind memory"
[2024-12-18 14:27:03.341] CPU #108 warning: "can't bind memory"
[2024-12-18 14:27:03.342] CPU #110 warning: "can't bind memory"
[2024-12-18 14:27:03.342] CPU #112 warning: "can't bind memory"
[2024-12-18 14:27:03.342] CPU #30 warning: "can't bind memory"
[2024-12-18 14:27:03.342] CPU #116 warning: "can't bind memory"
[2024-12-18 14:27:03.342] CPU #40 warning: "can't bind memory"
[2024-12-18 14:27:03.342] CPU #82 warning: "can't bind memory"
[2024-12-18 14:27:03.343] CPU #86 warning: "can't bind memory"
[2024-12-18 14:27:03.343] CPU #124 warning: "can't bind memory"
[2024-12-18 14:27:03.343] CPU #80 warning: "can't bind memory"
[2024-12-18 14:27:03.343] CPU #184 warning: "can't bind memory"
[2024-12-18 14:27:03.343] CPU #38 warning: "can't bind memory"
[2024-12-18 14:27:03.343] CPU #62 warning: "can't bind memory"
[2024-12-18 14:27:03.344] CPU #46 warning: "can't bind memory"
[2024-12-18 14:27:03.344] CPU #194 warning: "can't bind memory"
[2024-12-18 14:27:03.344] CPU #140 warning: "can't bind memory"
[2024-12-18 14:27:03.344] CPU #144 warning: "can't bind memory"
[2024-12-18 14:27:03.344] CPU #150 warning: "can't bind memory"
[2024-12-18 14:27:03.345] CPU #152 warning: "can't bind memory"
[2024-12-18 14:27:03.345] CPU #164 warning: "can't bind memory"
[2024-12-18 14:27:03.345] CPU #154 warning: "can't bind memory"
[2024-12-18 14:27:03.345] CPU #166 warning: "can't bind memory"
[2024-12-18 14:27:03.345] CPU #18 warning: "can't bind memory"
[2024-12-18 14:27:03.345] CPU #170 warning: "can't bind memory"
[2024-12-18 14:27:03.346] CPU #60 warning: "can't bind memory"
[2024-12-18 14:27:03.346] CPU #222 warning: "can't bind memory"
[2024-12-18 14:27:03.346] CPU #224 warning: "can't bind memory"
[2024-12-18 14:27:03.346] CPU #178 warning: "can't bind memory"
[2024-12-18 14:27:03.346] CPU #232 warning: "can't bind memory"
[2024-12-18 14:27:03.346] CPU #182 warning: "can't bind memory"
[2024-12-18 14:27:03.347] CPU #70 warning: "can't bind memory"
[2024-12-18 14:27:03.347] CPU #240 warning: "can't bind memory"
[2024-12-18 14:27:03.347] CPU #188 warning: "can't bind memory"
[2024-12-18 14:27:03.347] CPU #48 warning: "can't bind memory"
[2024-12-18 14:27:03.347] CPU #248 warning: "can't bind memory"
[2024-12-18 14:27:03.347] CPU #250 warning: "can't bind memory"
[2024-12-18 14:27:03.348] CPU #200 warning: "can't bind memory"
[2024-12-18 14:27:03.348] CPU #202 warning: "can't bind memory"
[2024-12-18 14:27:03.348] CPU #204 warning: "can't bind memory"
[2024-12-18 14:27:03.348] CPU #54 warning: "can't bind memory"
[2024-12-18 14:27:03.348] CPU #208 warning: "can't bind memory"
[2024-12-18 14:27:03.349] CPU #212 warning: "can't bind memory"
[2024-12-18 14:27:03.349] CPU #214 warning: "can't bind memory"
[2024-12-18 14:27:03.349] CPU #148 warning: "can't bind memory"
[2024-12-18 14:27:03.349] CPU #218 warning: "can't bind memory"
[2024-12-18 14:27:03.349] CPU #172 warning: "can't bind memory"
[2024-12-18 14:27:03.349] CPU #174 warning: "can't bind memory"
[2024-12-18 14:27:03.350] CPU #176 warning: "can't bind memory"
[2024-12-18 14:27:03.350] CPU #226 warning: "can't bind memory"
[2024-12-18 14:27:03.350] CPU #228 warning: "can't bind memory"
[2024-12-18 14:27:03.350] CPU #230 warning: "can't bind memory"
[2024-12-18 14:27:03.350] CPU #160 warning: "can't bind memory"
[2024-12-18 14:27:03.351] CPU #234 warning: "can't bind memory"
[2024-12-18 14:27:03.351] CPU #236 warning: "can't bind memory"
[2024-12-18 14:27:03.351] CPU #190 warning: "can't bind memory"
[2024-12-18 14:27:03.351] CPU #132 warning: "can't bind memory"
[2024-12-18 14:27:03.351] CPU #242 warning: "can't bind memory"
[2024-12-18 14:27:03.351] CPU #244 warning: "can't bind memory"
[2024-12-18 14:27:03.352] CPU #246 warning: "can't bind memory"
[2024-12-18 14:27:03.352] CPU #96 warning: "can't bind memory"
[2024-12-18 14:27:03.352] CPU #196 warning: "can't bind memory"
[2024-12-18 14:27:03.352] CPU #252 warning: "can't bind memory"
[2024-12-18 14:27:03.352] CPU #66 warning: "can't bind memory"
[2024-12-18 14:27:03.353] CPU #146 warning: "can't bind memory"
[2024-12-18 14:27:03.353] CPU #64 warning: "can't bind memory"
[2024-12-18 14:27:03.353] CPU #20 warning: "can't bind memory"
[2024-12-18 14:27:03.353] CPU #156 warning: "can't bind memory"
[2024-12-18 14:27:03.353] CPU #158 warning: "can't bind memory"
[2024-12-18 14:27:03.353] CPU #180 warning: "can't bind memory"
[2024-12-18 14:27:03.354] CPU #168 warning: "can't bind memory"
[2024-12-18 14:27:03.354] CPU #32 warning: "can't bind memory"
[2024-12-18 14:27:03.354] CPU #210 warning: "can't bind memory"
[2024-12-18 14:27:03.465]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2024-12-18 14:27:03.466]  cpu      GhostRider algo 2: cn/dark-lite (256 KB)
[2024-12-18 14:27:03.466]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)
```



os: windows11 Enterprise

# Discussion History
## spetterman66 | 2024-12-27T16:58:05+00:00
disable numa

## xmrig | 2025-06-16T19:14:43+00:00
This error means the physical cores don't have direct access to local DDR4 memory because memory sticks are installed in the wrong slots. There should be at least one stick per channel, not two. Like DIMM_A2, DIMM_B2, ...

# Action History
- Created by: ropyu1978 | 2024-12-18T10:15:01+00:00
- Closed at: 2025-06-16T19:14:43+00:00
