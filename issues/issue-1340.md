---
title: error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
source_url: https://github.com/xmrig/xmrig/issues/1340
author: minzak
assignees: []
labels:
- opencl
- randomx
created_at: '2019-11-30T20:01:54+00:00'
updated_at: '2021-04-12T15:17:17+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:17:17+00:00'
---

# Original Description
I'm hear, than ROCM not supported any more.
And it is normal or something wrong?

```
root@z820 /opt/xmrig # ./xmrig
 * ABOUT        XMRig/5.0.1 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * CPU          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES
                L2:4.0 MB L3:40.0 MB 16C/32T NUMA:2
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume
 * HTTP API     0.0.0.0:8080 
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3019.0)
 * OPENCL GPU   #0 43:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900) 1600 MHz cu:64 mem:13912/16368 MB
 * CUDA         disabled
[2019-11-30 21:56:22.770]  net  use pool pool.supportxmr.com:3333  178.63.100.197
[2019-11-30 21:56:22.770]  net  new job from pool.supportxmr.com:3333 diff 50000 algo rx/0 height 1978469
[2019-11-30 21:56:22.770]  rx   init datasets algo rx/0 (32 threads) seed 993ba25f61d47e1e...
[2019-11-30 21:56:23.210]  rx   #1 allocated 2080 MB huge pages 100% (439 ms)
[2019-11-30 21:56:23.704]  rx   #0 allocated 2080 MB huge pages 100% (934 ms)
[2019-11-30 21:56:23.765]  rx   #0 allocated  256 MB huge pages 100% +JIT (60 ms)
[2019-11-30 21:56:23.765]  rx   -- allocated 4416 MB huge pages 100% 2208/2208 (995 ms)
[2019-11-30 21:56:26.531]  rx   #0 dataset ready (2766 ms)
[2019-11-30 21:56:27.157]  rx   #1 dataset ready (626 ms)
[2019-11-30 21:56:27.158]  cpu  use profile  rx  (16 threads) scratchpad 2048 KB
[2019-11-30 21:56:27.180]  cpu  READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (22 ms)
[2019-11-30 21:56:27.180]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 43:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|  1 |   0 | 43:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
[2019-11-30 21:56:27.696]  ocl  GPU #0 compiling...
[2019-11-30 21:56:42.252]  cpu  accepted (1/0) diff 50000 (558 ms)
[2019-11-30 21:56:42.763]  ocl  GPU #0 compilation completed (15067 ms)
[2019-11-30 21:56:42.763]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2019-11-30 21:56:42.763]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2019-11-30 21:56:42.767]  ocl  thread #0 self-test failed
[2019-11-30 21:56:42.778]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2019-11-30 21:56:42.779]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
[2019-11-30 21:56:42.782]  ocl  thread #1 self-test failed
[2019-11-30 21:56:42.782]  ocl  disabled (failed to start threads)
[2019-11-30 21:56:44.841]  cpu  accepted (2/0) diff 50000 (55 ms)
[2019-11-30 21:56:49.645] Ctrl+C received, exiting
[2019-11-30 21:56:49.648]  cpu  stopped (3 ms)
[2019-11-30 21:56:49.648]  ocl  stopped (1 ms)
```


# Discussion History
## minzak | 2019-11-30T20:03:20+00:00
Maybe it is similar to https://github.com/xmrig/xmrig/issues/1333

## xmrig | 2019-12-02T01:20:16+00:00
ROCm not supported, you can try use `"gcn_asm": false,` but hashrate will be extremely low.
Thank you.

## minzak | 2019-12-02T16:29:44+00:00
Hm, I not understand why RX580 work, but Vega FE crashed?
Both on ROCM drivers.

## minzak | 2019-12-02T19:12:33+00:00
@xmrig 
>  try use `"gcn_asm": false`

No, not helps.
Here is part of config:
```
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "rx": [ { "index": 0, "intensity": 976, "worksize": 8, "threads": [-1, -1], "bfactor": 6, "gcn_asm": false, "dataset_host": false } ],
    },
```


```sh
...
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3019.0)
 * OPENCL GPU   #0 43:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900) 1600 MHz cu:64 mem:13912/16368 MB
 * CUDA         disabled
[2019-12-02 21:08:22.177]  net  use pool pool.supportxmr.com:3333  94.130.12.30
[2019-12-02 21:08:22.177]  net  new job from pool.supportxmr.com:3333 diff 50000 algo rx/0 height 1980192
[2019-12-02 21:08:22.178]  rx   init datasets algo rx/0 (32 threads) seed 993ba25f61d47e1e...
[2019-12-02 21:08:22.645]  rx   #0 allocated 2080 MB huge pages 100% (467 ms)
[2019-12-02 21:08:23.106]  rx   #1 allocated 2080 MB huge pages 100% (928 ms)
[2019-12-02 21:08:23.165]  rx   #0 allocated  256 MB huge pages 100% +JIT (59 ms)
[2019-12-02 21:08:23.166]  rx   -- allocated 4416 MB huge pages 100% 2208/2208 (988 ms)
[2019-12-02 21:08:25.891]  rx   #0 dataset ready (2725 ms)
[2019-12-02 21:08:26.544]  rx   #1 dataset ready (653 ms)
[2019-12-02 21:08:26.545]  cpu  use profile  rx  (16 threads) scratchpad 2048 KB
[2019-12-02 21:08:26.848]  cpu  READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (303 ms)
[2019-12-02 21:08:26.868]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 43:00.0 |  976 |  8 |  0 |  - |  8 | 1952 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|  1 |   0 | 43:00.0 |  976 |  8 |  0 |  - |  8 | 1952 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
[2019-12-02 21:08:27.372]  ocl  GPU #0 compiling...
[2019-12-02 21:08:29.428]  cpu  accepted (1/0) diff 50000 (49 ms)
[2019-12-02 21:08:32.346]  cpu  accepted (2/0) diff 50000 (50 ms)
[2019-12-02 21:08:39.290]  cpu  accepted (3/0) diff 50000 (50 ms)
[2019-12-02 21:08:42.314]  cpu  accepted (4/0) diff 50000 (49 ms)
[2019-12-02 21:08:42.519]  ocl  GPU #0 compilation completed (15147 ms)
[2019-12-02 21:08:42.533]  ocl  READY threads 2/2 (15412 ms)
Memory access fault by GPU node-2 (Agent handle: 0x5655170abe90) on address 0x7f2f966cc000. Reason: Page not present or supervisor privilege.
Aborted
```

## minzak | 2020-06-14T19:39:54+00:00
still same - https://github.com/xmrig/xmrig/issues/1734

# Action History
- Created by: minzak | 2019-11-30T20:01:54+00:00
- Closed at: 2021-04-12T15:17:17+00:00
