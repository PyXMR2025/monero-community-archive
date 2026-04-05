---
title: CUDA not working on my Debian 11 installation
source_url: https://github.com/xmrig/xmrig/issues/2870
author: ghost
assignees: []
labels: []
created_at: '2022-01-17T14:43:54+00:00'
updated_at: '2022-01-18T14:23:38+00:00'
type: issue
status: closed
closed_at: '2022-01-18T14:23:38+00:00'
---

# Original Description
uname -a
`Linux 5.10.0-10-amd64 #1 SMP Debian 5.10.84-1 (2021-12-08) x86_64 GNU/Linux`


nvidia-smi
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.91.03    Driver Version: 460.91.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 980     On   | 00000000:02:00.0 Off |                  N/A |
| 20%   38C    P8    12W / 300W |      1MiB /  4043MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

```

What I did:
1. Installed Debian 11
2. Followed this https://wiki.debian.org/NvidiaGraphicsDrivers#bullseye-460
3. Compiled xmrig (advanced build) and libxmrig-cuda.so on my main PC then uploaded them to this other system


./xmrig --cuda --cuda-loader=/home/l/libxmrig-cuda.so --url=theurl --user=walletaddress
```
hwloc auto configuration for algorithm "cn-heavy/0" failed.
 * ABOUT        XMRig/6.16.2 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Sempron(tm) 145 Processor (1) 64-bit -AES
                L2:1.0 MB L3:0.0 MB 1C/1T NUMA:1
 * MEMORY       2.7/3.8 GB (70%)
                DIMM1: <empty>
                DIMM2: 2 GB Other @ 533 MHz
                DIMM3: <empty>
                DIMM4: 2 GB Other @ 533 MHz
 * MOTHERBOARD  MSI - 785GM-P45 (MS-7623)
 * DONATE       0%
 * ASSEMBLY     auto:none
 * POOL #1  theurl algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled ((null)
```

# Discussion History
## Spudz76 | 2022-01-17T18:32:20+00:00
Since your driver provides CUDA 11.2 then you must compile with CUDA Toolkit 11.2 maximum...

Betting you used 11.5/11.6 which then won't work against driver providing 11.2 level.

## Spudz76 | 2022-01-17T18:36:13+00:00
Also, compiling on another system unless it is literally identical OS probably won't work great.

## ghost | 2022-01-18T14:23:35+00:00
Fixed after compiling and installing everything on the system I wanted to use xmrig on. Thanks @Spudz76 

# Action History
- Created by: ghost | 2022-01-17T14:43:54+00:00
- Closed at: 2022-01-18T14:23:38+00:00
