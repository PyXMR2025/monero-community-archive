---
title: OpenCL section hash rate is n/a with xmrig 4.0.0
source_url: https://github.com/xmrig/xmrig/issues/1179
author: noyanergun
assignees: []
labels:
- opencl
created_at: '2019-09-19T08:19:29+00:00'
updated_at: '2021-04-12T15:54:37+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:54:37+00:00'
---

# Original Description
As you see, my hash rate of OpenCL part is n/a.
What can I do about it? 

|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    12.8 |    12.9 |    12.9 |
|        1 |        2 |    44.7 |    45.1 |    45.6 |
|        2 |        1 |    13.0 |    13.0 |    13.1 |
|        - |        - |    70.5 |    71.0 |    71.7 |
| OPENCL # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        1 |     n/a |     n/a |     n/a | #0 01:00.0 AMD Radeon HD 7600M Series (Turks)
|        1 |       -1 |     n/a |     n/a |     n/a | #0 01:00.0 AMD Radeon HD 7600M Series (Turks)
|        - |        - |     n/a |     n/a |     n/a |

# Discussion History
## xmrig | 2019-09-19T08:52:29+00:00
Please show full miner output from beginning and if old xmrig-amd was works, output from xmrig-amd too.
Thank you.

## noyanergun | 2019-09-20T05:45:32+00:00
The output of miner from beginning :
 * ABOUT        XMRig/4.0.0-beta MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz (1) x64 AES
                     L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.minexmr.com:5555 algo cn/r
 * POOL #2      fr.minexmr.com:55555 algo cn/r
 * COMMANDS     hashrate, pause, resume
 * HTTP API     127.0.0.1:7070
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (1800.8)
 * OPENCL GPU   #0 01:00.0 AMD Radeon HD 7600M Series (Turks) 400MHz cu:6 mem:512/1024 MB
[2019-09-20 08:42:12.684] use pool pool.minexmr.com:5555  37.59.45.174
[2019-09-20 08:42:12.686] new job from pool.minexmr.com:5555 diff 15000 algo cn/r height 1927029
[2019-09-20 08:42:12.687]  cpu  use profile  cn  (3 threads) scratchpad 2048 KB
[2019-09-20 08:42:12.689]  ocl  use profile  cn/2  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 01:00.0 |   72 |  8 |  2 |  2 |  8 |  144 | AMD Radeon HD 7600M Series (Turks)
|  1 |   0 | 01:00.0 |   72 |  8 |  2 |  2 |  8 |  144 | AMD Radeon HD 7600M Series (Turks)
[2019-09-20 08:42:12.905]  ocl  READY threads 2 (213 ms)
[2019-09-20 08:42:14.504]  cpu  READY threads 3(3) huge pages 3/3 100% memory 6144 KB (1816 ms)
[2019-09-20 08:42:33.236] new job from pool.minexmr.com:5555 diff 15000 algo cn/r height 1927029
[2019-09-20 08:43:13.150] speed 10s/60s/15m 70.4 n/a n/a H/s max 71.8 H/s
[2019-09-20 08:43:13.721] new job from pool.minexmr.com:5555 diff 15000 algo cn/r height 1927030
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    12.6 |    12.8 |     n/a |
|        1 |        2 |    45.0 |    41.1 |     n/a |
|        2 |        1 |    12.7 |    12.8 |     n/a |
|        - |        - |    70.2 |    66.7 |     n/a |
| OPENCL # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        1 |     n/a |     n/a |     n/a | #0 01:00.0 AMD Radeon HD 7600M Series (Turks)
|        1 |       -1 |     n/a |     n/a |     n/a | #0 01:00.0 AMD Radeon HD 7600M Series (Turks)
|        - |        - |     n/a |     n/a |     n/a |
[2019-09-20 08:43:17.417] speed 10s/60s/15m 70.2 66.7 n/a H/s max 71.8 H/s

xmrig-amd is never work. :)

Thank you again

## lss4 | 2019-11-01T14:32:52+00:00
Same here. The 2.x standalone miner doesn't work, either.

OS: Manjaro Testing (latest)
GPU: Radeon RX 5700 XT 50th Anniversary Edition, detected as "Unknown AMD GPU (gfx1010)".
OpenCL: opencl-amdgpu-pro-pal (installed from AUR, opencl-amd does not work)
Version: v4.4.0-beta

Either there are still issues with Linux amdgpu/OpenCL drivers, or xmrig is currently not yet supported on the new Navi architecture in overall.

## lss4 | 2019-11-17T02:34:58+00:00
EDIT: As of xmrig 5.0.0 with the above configuration it seems OpenCL works, but very unstable as OpenCL hashrate fluctuates heavily. Sometimes I get some hashrate (from 100-600 H/s), but most of the time it's n/a.

# Action History
- Created by: noyanergun | 2019-09-19T08:19:29+00:00
- Closed at: 2021-04-12T15:54:37+00:00
