---
title: Impossible to stress KawPow
source_url: https://github.com/xmrig/xmrig/issues/3246
author: '0x241F31'
assignees: []
labels:
- review later
created_at: '2023-04-07T11:01:36+00:00'
updated_at: '2025-06-18T22:59:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I want to stress on KawPow algorithm to get best overclocking options, but seems like it's impossible:
```
foxpro:~$ sudo xmrig --no-color --stress -a kawpow
 * ABOUT        XMRig/6.19.1 gcc/12.2.1
 * LIBS         libuv/1.44.2 OpenSSL/3.0.8 hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       7.1/15.5 GB (46%)
                DIMM_A0: 8 GB DDR4 @ 2400 MHz M471A1K43BB1-CRC    
                DIMM_B0: 8 GB DDR4 @ 2400 MHz M471A1K43BB1-CRC    
 * MOTHERBOARD  Timi - TM1701
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo kawpow
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-04-07 16:00:05.465]  net      stratum+ssl://randomx.xmrig.com:443 199.247.27.41 connect error: "connection refused"
[2023-04-07 16:00:11.597]  net      stratum+ssl://randomx.xmrig.com:443 read error: "end of file"
[2023-04-07 16:00:17.449]  net      stratum+ssl://randomx.xmrig.com:443 199.247.27.41 connect error: "connection refused"
```


# Discussion History
# Action History
- Created by: 0x241F31 | 2023-04-07T11:01:36+00:00
