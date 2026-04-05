---
title: new to mining
source_url: https://github.com/xmrig/xmrig/issues/1627
author: voodoopant
assignees: []
labels:
- opencl
created_at: '2020-04-01T09:27:45+00:00'
updated_at: '2020-08-29T04:48:02+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:48:02+00:00'
---

# Original Description
[code] * ABOUT        XMRig/5.10.0 gcc/9.2.0
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          AMD Phenom(tm) II X4 965 Processor (1) x64 -AES
                L2:2.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       1.6/4.0 GB (41%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      monerohash.com:2222 algo auto
 * COMMANDS     hashrate, pause, resume
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3004.
8)
 * OPENCL GPU   #0 01:00.0 Radeon RX550/550 Series (gfx804) 1183 MHz cu:8 mem:17
92/2048 MB
 * CUDA         disabled
[2020-04-01 12:06:30.777]  net  use pool monerohash.com:2222  107.191.99.221
[2020-04-01 12:06:30.781]  net  new job from monerohash.com:2222 diff 50000 algo
 rx/0 height 2067076
[2020-04-01 12:06:30.784]  rx   init dataset algo rx/0 (4 threads) seed a4a9eb6e
5d9b6b44...
[2020-04-01 12:06:30.788]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/116
8 +JIT (0 ms)
[2020-04-01 12:06:42.058]  rx   dataset ready (11268 ms)
[2020-04-01 12:06:42.059]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 01:00.0 |  128 |  8 |  0 |  - |  8 |  256 | Radeon RX550/550 Series
 (gfx804)
|  1 |   0 | 01:00.0 |  128 |  8 |  0 |  - |  8 |  256 | Radeon RX550/550 Series
 (gfx804)
[2020-04-01 12:06:42.463]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when call
ing clCreateBuffer with buffer size 2181038080
[2020-04-01 12:06:42.465]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when call
ing clCreateBuffer with buffer size 2181038080
[2020-04-01 12:06:42.570]  ocl  thread #0 failed with error RandomX dataset is n
ot available
[2020-04-01 12:06:42.575]  ocl  thread #1 failed with error RandomX dataset is n
ot available
[2020-04-01 12:06:42.595]  ocl  thread #0 self-test failed
[2020-04-01 12:06:42.599]  ocl  thread #1 self-test failed
[2020-04-01 12:06:42.600]  ocl  disabled (failed to start threads)[/code]

Help me with the settings !
Thanks !

PS : pagefile 64GB

# Discussion History
# Action History
- Created by: voodoopant | 2020-04-01T09:27:45+00:00
- Closed at: 2020-08-29T04:48:02+00:00
