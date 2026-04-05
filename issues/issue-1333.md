---
title: CL_INVALID_PROGRAM on RandomX GPU
source_url: https://github.com/xmrig/xmrig/issues/1333
author: pacf531
assignees: []
labels:
- opencl
- randomx
created_at: '2019-11-30T02:58:00+00:00'
updated_at: '2021-04-12T15:18:23+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:18:23+00:00'
---

# Original Description
I get the following output when trying to benchmark RandomX on Ubuntu 18.04 using ROCM 2.10 which was just released while compiling the dev version using my Vega Frontier Edition. CPU works fine. What I find odd here is the lack of information about what was invalid about the OpenCL program. Is ROCM not supported at this point in time?

```
 * ABOUT        XMRig/5.1.0-dev gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * CPU          AMD Ryzen 7 1700X Eight-Core Processor (1) x64 AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       18.7/31.4 GB (60%)
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      randomx-benchmark.xmrig.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3019.0)
 * OPENCL GPU   #0 21:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900) 1600 MHz cu:64 mem:13912/16368 MB
 * CUDA         disabled
[2019-11-29 18:52:09.597]  net  use pool randomx-benchmark.xmrig.com:7777  178.128.242.134
[2019-11-29 18:52:09.598]  net  new job from randomx-benchmark.xmrig.com:7777 diff 79237371 algo rx/0 height 1354268
[2019-11-29 18:52:09.598]  rx   init dataset algo rx/0 (16 threads) seed 9df22d829fdfc780...
[2019-11-29 18:52:09.598]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2019-11-29 18:52:12.661]  rx   dataset ready (3063 ms)
[2019-11-29 18:52:12.661]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-11-29 18:52:12.662]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 21:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|  1 |   0 | 21:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
[2019-11-29 18:52:12.663]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (3 ms)
[2019-11-29 18:52:12.689]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2019-11-29 18:52:12.690]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
[2019-11-29 18:52:12.692]  ocl  thread #1 self-test failed
[2019-11-29 18:52:12.703]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2019-11-29 18:52:12.703]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2019-11-29 18:52:12.705]  ocl  thread #0 self-test failed
```

# Discussion History
## xmrig | 2019-12-02T01:19:43+00:00
ROCm not supported, you can try use `"gcn_asm": false,` but hashrate will be extremely low.
Thank you.

## pacf531 | 2019-12-02T02:00:25+00:00
Ah okay, thanks for the clarification. Are you willing to go into technical detail why this is the case and if this may change in the future?

I am fine using Windows for now but would like to use Linux if possible without the closed source drivers.

Edit: I forgot to add, although I don't plan to run it this way, I followed your suggestion of setting `"gcn_asm": false` but it still did not run, although it failed differently. This is with the latest code in dev compiled.

```
 * ABOUT        XMRig/5.1.0-dev gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * CPU          AMD Ryzen 7 1700X Eight-Core Processor (1) x64 AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       5.8/31.4 GB (18%)
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:443 coin monero
 * COMMANDS     hashrate, pause, resume
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3019.0)
 * OPENCL GPU   #0 2b:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900) 1600 MHz cu:64 mem:16368/16368 MB
 * CUDA         disabled
[2019-12-01 18:02:20.660]  net  use pool pool.supportxmr.com:443 TLSv1.2 192.110.160.114
[2019-12-01 18:02:20.660]  net  fingerprint (SHA-256): "24401543c71bbf0b3ed0724b2e74cdea2a019a3ac9adb10cbd58b265ff797d7c"
[2019-12-01 18:02:20.660]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 1979662
[2019-12-01 18:02:20.660]  rx   init dataset algo rx/0 (16 threads) seed 993ba25f61d47e1e...
[2019-12-01 18:02:20.691]  rx   allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (30 ms)
[2019-12-01 18:02:23.378]  rx   dataset ready (2687 ms)
[2019-12-01 18:02:23.378]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-12-01 18:02:23.519]  cpu  READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (141 ms)
[2019-12-01 18:02:23.539]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 2b:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|  1 |   0 | 2b:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
[2019-12-01 18:02:23.571]  ocl  READY threads 2/2 (31 ms)
Memory access fault by GPU node-1 (Agent handle: 0x556df93a9740) on address 0x7f42e362e000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```

## minzak | 2019-12-02T19:18:18+00:00
If you know C++ use this - https://github.com/SChernykh/RandomX_OpenCL/issues/8#issuecomment-560473097
But i saw 2k+ - https://github.com/SChernykh/RandomX_OpenCL/issues/9

## calvintam236 | 2019-12-13T00:50:56+00:00
Hi @xmrig, it sounds like ROCM will no longer support in the future? I am running xmrig inside docker container, and I wonder how to input `gcn_asm` parameter in the command line? Thanks.

## minzak | 2020-06-14T19:41:33+00:00
similar issues - https://github.com/xmrig/xmrig/issues/1734.

Need test new Debian withouth ROCM. 
I hope it is possible.

# Action History
- Created by: pacf531 | 2019-11-30T02:58:00+00:00
- Closed at: 2021-04-12T15:18:23+00:00
