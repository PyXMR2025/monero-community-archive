---
title: speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
source_url: https://github.com/xmrig/xmrig/issues/2624
author: Swishwork
assignees: []
labels: []
created_at: '2021-10-11T17:52:06+00:00'
updated_at: '2025-07-12T00:36:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi there, I'm generating n/a hash rates (eg: speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s

I've implemented the following:

- xmrig-6.15.2-macos-x64.tar.gz 
- I'm using an Intel UHD Graphics 630
- Pool: 2miner us-rvn.2miners.com:6060
- I've set algo to "kawpow", disabled cpu and enabled openCL in the config file

Can anyone tell me why I'm generating n/a hash rates?

# Discussion History
## Spudz76 | 2021-10-11T20:55:32+00:00
Because OpenCL really only works right on AMD with AMD drivers.

Until of course *someone* decides to merge my fixes in #2614, and then it works on almost everything.

You could build from the source in that pull request and it will work.

## Swishwork | 2021-10-13T00:34:16+00:00
Thanks for the response.  

I'm not familiar with how to build from the source in the pull request.

I noticed that XMRIG merged the commit 7627b23 into xmrig:dev which is great.  

Now that there's a merge, Is there a build available that I could try out?

## Spudz76 | 2021-10-13T04:39:31+00:00
Unfortunately there are only builds of `master` branch, the `dev` branch is still compile-your-own to try.

I'm sure a new master is on the horizon soon.

## xmrig | 2021-10-13T04:43:08+00:00
https://download.xmrig.com/xmrig/6.15.3-dev/7627b2321293ba2e69ad900d50e3ee21bbd882c0/ username `xmrig` password `download`.

## Spudz76 | 2021-10-13T04:45:29+00:00
@Swishwork -- lucky you :)

## Swishwork | 2021-10-14T20:29:57+00:00
@xmrig  @Spudz76 Big thanks for the effort and guidance here.  

I've run 6.15.3 and the N/A hash rates remain.

Any more insight towards a resolution?

I'm receiving the following 3 errors:

1. [2021-10-14 15:16:52.410]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
2. [2021-10-14 15:16:59.823]  opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel ethash_calculate_dag_item
3. [2021-10-14 15:16:59.823]  opencl   thread #0 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE

Here is the output:

 * ABOUT        XMRig/6.15.3-dev clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       12.8/16.0 GB (80%)
                DIMM_A0: 8 GB DDR4 @ 2667 MHz HMA81GS6CJR8N-VK    
                DIMM_B0: 8 GB DDR4 @ 2667 MHz HMA81GS6CJR8N-VK    
 * MOTHERBOARD  Apple Inc. - Mac-E1008331FDC96864
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      us-rvn.2miners.com:6060 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Jun 21 2021 21:07:35)
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1150 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 5300M Compute Engine 95 MHz cu:20 mem:1020/4080 MB
 * CUDA         disabled
[2021-10-14 15:16:52.399]  net      use pool us-rvn.2miners.com:6060  135.148.55.16
[2021-10-14 15:16:52.403]  net      new job from us-rvn.2miners.com:6060 diff 4295M algo kawpow height 1973013
[2021-10-14 15:16:52.404]  opencl   use profile  kawpow  (2 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   6291456 |   256 |   3176 | Intel(R) UHD Graphics 630
|  1 |   1 |     n/a |  10485760 |   128 |   3176 | AMD Radeon Pro 5300M Compute Engine
[2021-10-14 15:16:52.409]  opencl   GPU #0 compiling...
[2021-10-14 15:16:52.410]  opencl   GPU #0 compilation completed (1 ms)
[2021-10-14 15:16:52.410]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-10-14 15:16:53.328]  opencl   GPU #1 compiling...
[2021-10-14 15:16:53.516]  opencl   GPU #1 compilation completed (187 ms)
[2021-10-14 15:16:53.516]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-10-14 15:16:53.516]  opencl   READY threads 2/2 (1112 ms)
[2021-10-14 15:16:53.769]  opencl   KawPow program for period 657671 compiled (253ms)
[2021-10-14 15:16:54.016]  opencl   KawPow program for period 657672 compiled (246ms)
[2021-10-14 15:16:54.387]  opencl   KawPow program for period 657671 compiled (371ms)
[2021-10-14 15:16:54.716]  opencl   KawPow program for period 657672 compiled (329ms)
[2021-10-14 15:16:58.876]  miner    KawPow light cache for epoch 263 calculated (5107ms)
[2021-10-14 15:16:59.823]  opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel ethash_calculate_dag_item
[2021-10-14 15:16:59.823]  opencl   thread #0 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2021-10-14 15:17:07.669]  net      new job from us-rvn.2miners.com:6060 diff 4295M algo kawpow height 1973014
[2021-10-14 15:17:18.774]  opencl   KawPow DAG for epoch 263 calculated (18965ms)
[2021-10-14 15:17:36.612]  net      new job from us-rvn.2miners.com:6060 diff 4295M algo kawpow height 1973015
[2021-10-14 15:18:06.207]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s


## Spudz76 | 2021-10-14T20:41:44+00:00
Kawpow needs at least  3.055GB currently (and growing) for the DAG.  And then some more for scratch space, probably.

I don't think either one has enough free memory.  Intel says `mem:384/1536 MB` and AMD says `mem:1020/4080 MB` so something else is camping on most of the VRAM, or there is another max-allocation problem.  The Intel will never do Kawpow even if it was fully empty (1.5GB VRAM), the AMD might if you can figure out what's using 75% of its memory already.

## ghost | 2025-07-12T00:36:46+00:00
I'm generating n/a hash rates as well  "miner speed 10/s/60s/15m n/a n/a n/a h/s 16098.2"

I've implemented the following:

xmrig-6.23.0-windows-x64
gulf.moneroocean.stream:10016

Microsoft Windows 11 Pro 
AMD Ryzen 9 7900X 12-Core Processor, 4.70 GHz 12 Core
ASUS ProArt B650-CREATOR
64.0 GB DDR5 
AMD Radeon RX 7600 8176 MB GDDR6

any help is appreciated.... all drivers are up to date... 





# Action History
- Created by: Swishwork | 2021-10-11T17:52:06+00:00
