---
title: error CL_INVALID_VALUE when calling clGetProgramInfo
source_url: https://github.com/xmrig/xmrig/issues/2985
author: BlrFox
assignees: []
labels: []
created_at: '2022-03-22T21:49:45+00:00'
updated_at: '2023-02-10T11:06:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi I'm just trying to get the OpenCL's on my Gpu's. The issue/errors are down below.
Any advice or wherever I'm going wrong would be appreciated. Thanks


* ABOUT        XMRig/6.16.4 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       7.6/64.0 GB (12%)
                DIMM1: 16 GB DDR3 @ 1866 MHz 0x4D33393342324737304442302D434D412020
                DIMM2: 16 GB DDR3 @ 1866 MHz 0x4D33393342324737304442302D434D412020
                DIMM3: 16 GB DDR3 @ 1866 MHz 0x4D33393342324737304442302D434D412020
                DIMM4: 16 GB DDR3 @ 1866 MHz 0x4D33393342324737304442302D434D412020
 * MOTHERBOARD  Apple Inc. - Mac-F60DEB81FF30ACF6
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo auto
 * POOL #2      xmr.pool.minergate.com:45700 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Jun  8 2020 17:36:15)
 * OPENCL GPU   #0 n/a AMD Radeon HD - FirePro D500 Compute 
 * Engine 150 MHz cu:24 mem:768/3072 MB
 * OPENCL GPU   #1 n/a AMD Radeon HD - FirePro D500 Compute Engine 150 MHz cu:24 mem:768/3072 MB
 * CUDA         disabled


[2022-03-22 16:44:21.067]  opencl   GPU #1 compiling...
[2022-03-22 16:44:21.069]  opencl   GPU #1 compilation completed (2 ms)
[2022-03-22 16:44:21.069]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-03-22 16:44:21.070]  opencl   GPU #1 compiling...
[2022-03-22 16:44:21.071]  opencl   GPU #1 compilation completed (2 ms)
[2022-03-22 16:44:21.072]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-03-22 16:44:21.072]  opencl   READY threads 2/2 (8 ms)
[2022-03-22 16:45:01.206]  net      new job from randomx.xmrig.com:443 diff 1000K algo rx/0 height 2585431 (72 tx)
[2022-03-22 16:45:21.412]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2022-03-22 16:45:25.153]  signal   Ctrl+C received, exiting
[2022-03-22 16:45:34.376]  opencl   stopped (9223 ms)




# Discussion History
## cathino | 2022-06-03T00:45:31+00:00
+1

## kritch83 | 2022-06-08T20:00:40+00:00
same issue...

## Dymoob | 2023-02-09T16:31:37+00:00
Same problem :/

## SChernykh | 2023-02-09T21:43:28+00:00
OpenCL support on Apple is as good as dead, it gets worse and worse with every release and they're switching to their own GPU compute API (Metal).

## Dymoob | 2023-02-10T11:06:00+00:00
Yes, unfortunately I can only try with this machine for now, I will update my equipment soon so I can continue.

# Action History
- Created by: BlrFox | 2022-03-22T21:49:45+00:00
