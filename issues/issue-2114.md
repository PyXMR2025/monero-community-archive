---
title: Does GPU mining need more than 2GB video memory ?
source_url: https://github.com/xmrig/xmrig/issues/2114
author: cql1983
assignees: []
labels: []
created_at: '2021-02-18T05:02:45+00:00'
updated_at: '2021-04-12T14:12:21+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:12:21+00:00'
---

# Original Description
HI,I tested OpenCL mining on my notebook, and the OpenCL environment has been configured, but the following error was prompted when mining. According to the requirements of CPU mining, does graphics card mining need at least 2GB video memory? Is there any way to mine graphics cards with less than 2GB video memory?

` * ABOUT        XMRig/6.8.2 gcc/8.3.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       6.0/7.3 GB (83%)
                DIMM_A0: 8 GB DDR4 @ 2667 MHz HMAA1GS6CMR6N-VK    
                ChannelB-DIMM0: <empty>
 * MOTHERBOARD  LENOVO - LNVNB161216
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3180.7)
 * OPENCL GPU   #0 01:00.0 AMD Radeon Graphics (Iceland) 1024 MHz cu:6 mem:1515/2037 MB
 * CUDA         disabled
[2021-02-18 12:33:41.373]  net      use pool xmr.f2pool.com:13531  127.0.0.1
[2021-02-18 12:33:41.373]  net      new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2299276
[2021-02-18 12:33:41.373]  cpu      use argon2 implementation AVX2
[2021-02-18 12:33:41.377]  msr      register values for "intel" preset have been set successfully (3 ms)
[2021-02-18 12:33:41.377]  randomx  init dataset algo rx/0 (3 threads) seed b353f283ee2e4460...
[2021-02-18 12:33:41.530]  randomx  failed to allocate RandomX dataset using 1GB pages
[2021-02-18 12:33:41.550]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (174 ms)
[2021-02-18 12:33:51.659]  randomx  dataset ready (10109 ms)
[2021-02-18 12:33:51.659]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
[2021-02-18 12:33:51.660]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |        64 |     8 |    128 | AMD Radeon Graphics (Iceland)
|  1 |   0 | 01:00.0 |        64 |     8 |    128 | AMD Radeon Graphics (Iceland)
[2021-02-18 12:33:51.662]  cpu      READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (3 ms)
[2021-02-18 12:33:52.454]  opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with
[2021-02-18 12:33:52.462]  opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with
[2021-02-18 12:33:52.480]  opencl   thread #0 failed with error RandomX dataset is not available
[2021-02-18 12:33:52.482]  opencl   thread #1 failed with error RandomX dataset is not available
[2021-02-18 12:33:52.484]  opencl   thread #0 self-test failed
[2021-02-18 12:33:52.486]  opencl   thread #1 self-test failed
[2021-02-18 12:33:52.486]  opencl   disabled (failed to start threads)
[2021-02-18 12:33:56.234]  signal   Ctrl+C received, exiting
[2021-02-18 12:33:56.235]  cpu      stopped (1 ms)
[2021-02-18 12:33:56.235]  opencl   stopped (1 ms)
`

# Discussion History
## Spudz76 | 2021-02-18T07:12:42+00:00
RandomX isn't worth using on GPUs even if you had enough memory.

CN-Heavy/XHV works good, use a pool that pays XMR for whatever other algos if you want to earn XMR for GPUs.

## ghost | 2021-02-18T11:27:04+00:00
I personally suggest to run BetterHash and set xmrig for cpu and another algo/coin for gpu because monero is not profitable on gpu

## Spudz76 | 2021-02-18T21:25:47+00:00
Also your system ram is too small for RandomX

# Action History
- Created by: cql1983 | 2021-02-18T05:02:45+00:00
- Closed at: 2021-04-12T14:12:21+00:00
