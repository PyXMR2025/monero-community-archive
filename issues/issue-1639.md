---
title: RX580 error  OCL
source_url: https://github.com/xmrig/xmrig/issues/1639
author: palouf34
assignees: []
labels:
- opencl
created_at: '2020-04-08T18:52:53+00:00'
updated_at: '2022-02-07T03:39:26+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:44:28+00:00'
---

# Original Description
When I'm launch the miner whith option for use my radeon RX580 8Go I'm obtain this log

`
 * ABOUT        XMRig/5.10.0 gcc/5.4.0
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz (2) x64 AES
                L2:3.0 MB L3:30.0 MB 12C/24T NUMA:2
 * MEMORY       23.5/31.3 GB (75%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmrpool.eu:3333 algo auto
 * COMMANDS     hashrate, pause, resume
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3098.0)
 * OPENCL GPU   #0 05:00.0 Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (gfx803) 1366 MHz cu:36 mem:6963/8192 MB
 * CUDA         disabled
[2020-04-08 20:47:53.791]  net  use pool xmrpool.eu:3333  54.37.7.208
[2020-04-08 20:47:53.791]  net  new job from xmrpool.eu:3333 diff 25000 algo rx/0 height 2072417
[2020-04-08 20:47:53.796]  msr  msr kernel module is not available
[2020-04-08 20:47:53.796]  rx   init datasets algo rx/0 (24 threads) seed c2e3fe5979575f75...
[2020-04-08 20:47:54.309]  rx   #0 allocated 2080 MB huge pages 100% (513 ms)
[2020-04-08 20:47:54.309]  rx   #1 allocated 2080 MB huge pages   0% (513 ms)
[2020-04-08 20:47:54.384]  rx   #0 allocated  256 MB huge pages 100% +JIT (75 ms)
[2020-04-08 20:47:54.384]  rx   -- allocated 4416 MB huge pages  53% 1168/2208 (588 ms)
[2020-04-08 20:47:58.263]  rx   #0 dataset ready (3879 ms)
[2020-04-08 20:48:00.114]  rx   #1 dataset ready (1851 ms)
[2020-04-08 20:48:00.114]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
[2020-04-08 20:48:00.351]  cpu  READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (237 ms)
[2020-04-08 20:48:00.357]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 05:00.0 |  576 |  8 |  0 |  - |  8 | 1152 | Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (gfx803)
|  1 |   0 | 05:00.0 |  576 |  8 |  0 |  - |  8 | 1152 | Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (gfx803)
[2020-04-08 20:48:04.815]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2020-04-08 20:48:04.815]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2020-04-08 20:48:04.823]  ocl  thread #0 self-test failed
[2020-04-08 20:48:04.832]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2020-04-08 20:48:04.832]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
[2020-04-08 20:48:04.834]  ocl  thread #1 self-test failed
[2020-04-08 20:48:04.834]  ocl  disabled (failed to start threads)
[2020-04-08 20:48:09.517]  cpu  accepted (1/0) diff 25000 (112 ms)
`

in my conf contains this option:
`"api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
	
    },`

I'm use last official drive AMD on untuntu 18.04 LTS

Have you on idea when this  problem  appear? 

thk's for your help

# Discussion History
## palouf34 | 2020-04-14T08:09:51+00:00
I'm upate this version with this remake with src and i'm obtain similary error.

Have you on idea for correct this ?


## minzak | 2020-06-14T19:36:53+00:00
similar issues - https://github.com/xmrig/xmrig/issues/1734

## zella | 2021-08-14T09:46:23+00:00
same issue rx570

## jauhari | 2022-02-07T03:39:26+00:00
any solution about it?

# Action History
- Created by: palouf34 | 2020-04-08T18:52:53+00:00
- Closed at: 2020-08-29T04:44:28+00:00
