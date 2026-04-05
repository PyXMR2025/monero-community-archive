---
title: 'error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram  - OR - Memory
  access fault by GPU node-2 (Agent handle: 0x55d56c0f42b0) on address 0x7fcd5f87d000.
  Reason: Page not present or supervisor privilege.'
source_url: https://github.com/xmrig/xmrig/issues/1734
author: minzak
assignees: []
labels: []
created_at: '2020-06-14T19:33:30+00:00'
updated_at: '2021-03-06T21:15:17+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:12:58+00:00'
---

# Original Description
I have latest Debian under ROCM driver + Vega FE.

config.json:
```
    "opencl": {
        "enabled": true,
        "cache": false,
        "loader": "/opt/rocm/lib/libOpenCL.so",
        "platform": "AMD",
        "adl": true,
        "cn": [
            {
                "index": 0,
                "intensity": 1984,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 1024,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ]
    },

```

./xmrig
```
 * ABOUT        XMRig/5.11.3 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2697 v2 @ 2.70GHz (2) x64 AES
                L2:6.0 MB L3:60.0 MB 24C/48T NUMA:2
 * MEMORY       18.9/251.8 GB (7%)
 * DONATE       3%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (3137.0)
 * OPENCL GPU   #0 43:00.0 Device 6863 (gfx900) 1600 MHz cu:64 mem:13912/16368 MB
 * CUDA         disabled
[2020-06-14 22:20:59.551]  net  use pool pool.supportxmr.com:3333  178.63.100.197
[2020-06-14 22:20:59.551]  net  new job from pool.supportxmr.com:3333 diff 200007 algo rx/0 height 2120642
[2020-06-14 22:20:59.551]  cpu  use argon2 implementation SSSE3
[2020-06-14 22:20:59.560]  msr  register values for "intel" preset has been set successfully (9 ms)
[2020-06-14 22:20:59.560]  rx   init datasets algo rx/0 (48 threads) seed b0920b700fc794ff...
[2020-06-14 22:21:00.664]  rx   #0 allocated 2080 MB huge pages 100% (1104 ms)
[2020-06-14 22:21:00.665]  rx   #1 allocated 2080 MB huge pages 100% (1106 ms)
[2020-06-14 22:21:00.739]  rx   #0 allocated  256 MB huge pages 100% +JIT (73 ms)
[2020-06-14 22:21:00.739]  rx   -- allocated 4416 MB huge pages 100% 2208/2208 (1179 ms)
[2020-06-14 22:21:03.740]  rx   #0 dataset ready (3001 ms)
[2020-06-14 22:21:05.081]  rx   #1 dataset ready (1341 ms)
[2020-06-14 22:21:05.081]  cpu  use profile  rx  (24 threads) scratchpad 2048 KB
[2020-06-14 22:21:05.548]  cpu  READY threads 24/24 (24) huge pages 100% 24/24 memory 49152 KB (467 ms)
[2020-06-14 22:21:05.566]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 43:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Device 6863 (gfx900)
|  1 |   0 | 43:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Device 6863 (gfx900)
[2020-06-14 22:21:07.024]  ocl  GPU #0 compiling...
[2020-06-14 22:21:07.628]  cpu  accepted (1/0) diff 200007 (49 ms)
[2020-06-14 22:21:22.364]  ocl  GPU #0 compilation completed (15340 ms)
[2020-06-14 22:21:22.364]  ocl  GPU #0 compiling...
[2020-06-14 22:21:37.670]  ocl  GPU #0 compilation completed (15306 ms)
[2020-06-14 22:21:37.670]  ocl  READY threads 2/2 (31850 ms)
Memory access fault by GPU node-2 (Agent handle: 0x55d56c0f42b0) on address 0x7fcd5f87d000. Reason: Page not present or supervisor privilege.
Aborted
```
If I mage changes in:
```
                "gcn_asm": true,
```
i got: 
./xmrig
```
 * ABOUT        XMRig/5.11.3 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2697 v2 @ 2.70GHz (2) x64 AES
                L2:6.0 MB L3:60.0 MB 24C/48T NUMA:2
 * MEMORY       18.9/251.8 GB (8%)
 * DONATE       3%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (3137.0)
 * OPENCL GPU   #0 43:00.0 Device 6863 (gfx900) 1600 MHz cu:64 mem:13912/16368 MB
 * CUDA         disabled
[2020-06-14 22:27:34.568]  net  use pool pool.supportxmr.com:3333  178.63.100.197
[2020-06-14 22:27:34.569]  net  new job from pool.supportxmr.com:3333 diff 200007 algo rx/0 height 2120644
[2020-06-14 22:27:34.569]  cpu  use argon2 implementation SSSE3
[2020-06-14 22:27:34.577]  msr  register values for "intel" preset has been set successfully (8 ms)
[2020-06-14 22:27:34.577]  rx   init datasets algo rx/0 (48 threads) seed b0920b700fc794ff...
[2020-06-14 22:27:35.684]  rx   #1 allocated 2080 MB huge pages 100% (1106 ms)
[2020-06-14 22:27:35.685]  rx   #0 allocated 2080 MB huge pages 100% (1107 ms)
[2020-06-14 22:27:35.756]  rx   #0 allocated  256 MB huge pages 100% +JIT (71 ms)
[2020-06-14 22:27:35.757]  rx   -- allocated 4416 MB huge pages 100% 2208/2208 (1179 ms)
[2020-06-14 22:27:38.763]  rx   #0 dataset ready (3006 ms)
[2020-06-14 22:27:40.066]  rx   #1 dataset ready (1303 ms)
[2020-06-14 22:27:40.066]  cpu  use profile  rx  (24 threads) scratchpad 2048 KB
[2020-06-14 22:27:40.534]  cpu  READY threads 24/24 (24) huge pages 100% 24/24 memory 49152 KB (467 ms)
[2020-06-14 22:27:40.552]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 43:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Device 6863 (gfx900)
|  1 |   0 | 43:00.0 | 1024 |  8 |  0 |  - |  8 | 2048 | Device 6863 (gfx900)
[2020-06-14 22:27:41.981]  ocl  GPU #0 compiling...
[2020-06-14 22:27:57.348]  ocl  GPU #0 compilation completed (15368 ms)
[2020-06-14 22:27:57.349]  ocl  GPU #0 compiling...
[2020-06-14 22:27:57.349]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2020-06-14 22:27:57.349]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2020-06-14 22:27:57.354]  ocl  thread #0 self-test failed
[2020-06-14 22:28:09.597]  net  new job from pool.supportxmr.com:3333 diff 200007 algo rx/0 height 2120645
[2020-06-14 22:28:12.680]  ocl  GPU #0 compilation completed (15331 ms)
[2020-06-14 22:28:12.680]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2020-06-14 22:28:12.680]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
[2020-06-14 22:28:12.685]  ocl  thread #1 self-test failed
[2020-06-14 22:28:12.685]  ocl  disabled (failed to start threads)
[2020-06-14 22:28:18.718]  cpu  accepted (1/0) diff 200007 (55 ms)
[2020-06-14 22:28:40.374]  ocl  #0 43:00.0   0W  0C    0RPM 0/0MHz
```



clinfo
```clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3137.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback 


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 6863
  Device Topology:                               PCI[ B#67, D#0, F#0 ]
  Max compute units:                             64
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1600Mhz
  Address bits:                                  64
  Max memory allocation:                         14588628172
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26723
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            17163091968
  Constant buffer size:                          14588628172
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          1703726284
  Max global variable size:                      14588628172
  Max global variable preferred total size:      17163091968
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:                                
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:                              
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:                            
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7efc0e818cf0
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0 
  Driver version:                                3137.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0 
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

It is error because i use ROCM, or VegaFE not supported?
And yes I know, that GPU mining for XMR is not good idea.

BUT earlier all is was fine!
```
root@z820 /opt/xmrig # ./xmrig
 * ABOUT        XMRig/5.0.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * CPU          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES
                L2:4.0 MB L3:40.0 MB 16C/32T NUMA:2
 * DONATE       3%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:3333 algo cn/r
 * COMMANDS     hashrate, pause, resume
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (2982.0)
 * OPENCL GPU   #0 43:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900) 1600 MHz cu:64 mem:13912/16368 MB
 * CUDA         disabled
[2019-11-14 04:02:19.265]  net  use pool pool.supportxmr.com:3333  178.63.100.197
[2019-11-14 04:02:19.265]  net  new job from pool.supportxmr.com:3333 diff 10000 algo cn/r height 1966455
[2019-11-14 04:02:19.265]  cpu  use profile  cn  (20 threads) scratchpad 2048 KB
[2019-11-14 04:02:19.289]  ocl  use profile  cn/2  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 43:00.0 | 1984 | 16 |  2 |  1 |  8 | 3968 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|  1 |   0 | 43:00.0 | 1984 | 16 |  2 |  1 |  8 | 3968 | Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
[2019-11-14 04:02:20.281]  ocl  READY threads 2/2 (992 ms)
[2019-11-14 04:02:20.409]  cpu  READY threads 20/20 (20) huge pages 100% 20/20 memory 40960 KB (1143 ms)
[2019-11-14 04:02:21.838]  cpu  accepted (1/0) diff 10000 (82 ms)
[2019-11-14 04:02:34.723]  net  new job from pool.supportxmr.com:3333 diff 19980 algo cn/r height 1966455
[2019-11-14 04:02:47.945]  cpu  accepted (2/0) diff 19980 (85 ms)
[2019-11-14 04:02:49.284] speed 10s/60s/15m 1790.2 n/a n/a H/s max 1790.2 H/s
[2019-11-14 04:02:54.141]  cpu  accepted (3/0) diff 19980 (50 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    28.4 |     n/a |     n/a |
|        1 |        1 |    28.3 |     n/a |     n/a |
|        2 |        2 |    44.8 |     n/a |     n/a |
|        3 |        3 |    44.6 |     n/a |     n/a |
|        4 |        4 |    44.6 |     n/a |     n/a |
|        5 |        5 |    44.9 |     n/a |     n/a |
|        6 |        6 |    45.3 |     n/a |     n/a |
|        7 |        7 |    45.5 |     n/a |     n/a |
|        8 |       16 |    28.4 |     n/a |     n/a |
|        9 |       17 |    28.3 |     n/a |     n/a |
|       10 |        8 |    27.7 |     n/a |     n/a |
|       11 |        9 |    27.4 |     n/a |     n/a |
|       12 |       10 |    44.4 |     n/a |     n/a |
|       13 |       11 |    44.4 |     n/a |     n/a |
|       14 |       12 |    44.3 |     n/a |     n/a |
|       15 |       13 |    44.7 |     n/a |     n/a |
|       16 |       14 |    43.5 |     n/a |     n/a |
|       17 |       15 |    44.8 |     n/a |     n/a |
|       18 |       24 |    27.7 |     n/a |     n/a |
|       19 |       25 |    27.4 |     n/a |     n/a |
|        - |        - |   759.5 |     n/a |     n/a |
| OPENCL # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |       -1 |   520.2 |     n/a |     n/a | #0 43:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|        1 |       -1 |   522.1 |     n/a |     n/a | #0 43:00.0 Vega 10 XTX [Radeon Vega Frontier Edition] (gfx900)
|        - |        - |  1042.3 |     n/a |     n/a |
[2019-11-14 04:03:00.642] speed 10s/60s/15m 1801.8 n/a n/a H/s max 1819.0 H/s
[2019-11-14 04:03:01.836]  cpu  accepted (4/0) diff 19980 (87 ms)
[2019-11-14 04:03:02.825] Ctrl+C received, exiting
[2019-11-14 04:03:02.846]  cpu  stopped (20 ms)
[2019-11-14 04:03:04.070]  ocl  stopped (1225 ms)
``` 

# Discussion History
## minzak | 2020-06-14T19:35:32+00:00
https://github.com/xmrig/xmrig/issues/1701 error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram

## SChernykh | 2020-06-14T19:46:12+00:00
`"gcn_asm": true,` works only with amdgpu-pro drivers or on Windows. The `CL_BUILD_PROGRAM_FAILURE` is strange since OpenCL code is correct there and no compilation error is printed. Maybe it's a bug in driver.

## minzak | 2020-06-14T20:01:34+00:00
`Maybe it's a bug in driver.`
How to detect it? For make issues to driver team... 

## SChernykh | 2020-06-14T20:13:59+00:00
Can you double check that you have `"gcn_asm": false,` in config? Even if you get CL_BUILD_PROGRAM_FAILURE, it should also print build log with errors. You can also try to delete `.cache` folder, maybe it tries to use binaries created with older driver and new driver can't load them.

## minzak | 2020-06-15T18:11:18+00:00
Yes, everything is correct.
`.cache` - always manually delete after exit xmrig, if `"cache": true`, but usually I use false mode
`gcn_asm` - false or true - not worked, just different results, as described above.
Can I some run in debug mode or build, or etc, to help to investigate it?

[config.json.txt](https://github.com/xmrig/xmrig/files/4782057/config.json.txt)


## httran13 | 2020-07-05T03:38:22+00:00
same problem here

```
2020-07-04 23:34:11.001] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/6.2.2 clang/11.0.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz (1) x64 AES
                L2:2.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       12.2/16.0 GB (76%)
 * DONATE       3%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
[2020-07-04 23:34:11.008]  config   configuration saved to: "config.json"
[2020-07-04 23:34:11.008] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (May  3 2020 20:15:19)
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1200 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 5500M Compute Engine 95 MHz cu:24 mem:1020/4080 MB
 * CUDA         disabled
[2020-07-04 23:34:11.217]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.244.186
[2020-07-04 23:34:11.217]  net      fingerprint (SHA-256): "676f843ef4cda0f72578b7589eedb13f4ca79f636b6a4e57eb38847c8f679d93"
[2020-07-04 23:34:11.217]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2135294
[2020-07-04 23:34:11.217]  cpu      use argon2 implementation AVX2
[2020-07-04 23:34:11.217]  randomx  init dataset algo rx/0 (16 threads) seed 92ebdefc07085b2e...
[2020-07-04 23:34:11.931]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (714 ms)
[2020-07-04 23:34:12.943]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2135295
[2020-07-04 23:34:14.727]  randomx  dataset ready (2796 ms)
[2020-07-04 23:34:14.727]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2020-07-04 23:34:19.931]  opencl   use profile  rx  (3 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       320 |     8 |    640 | Intel(R) UHD Graphics 630
|  1 |   1 |     n/a |       384 |     8 |    768 | AMD Radeon Pro 5500M Compute Engine
|  2 |   1 |     n/a |       384 |     8 |    768 | AMD Radeon Pro 5500M Compute Engine
[2020-07-04 23:34:20.699]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (5972 ms)
[2020-07-04 23:34:20.705]  opencl   GPU #0 compiling...
[2020-07-04 23:34:20.708]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:816:6: warning: no previous prototype for function 'get_byte32'
uint get_byte32(uint a,uint start_bit) { return (a>>start_bit)&0xFF; }
     ^
<program source>:1068:7: warning: no previous prototype for function 'rotr64'
ulong rotr64(ulong a,ulong shift) { return rotate(a,64-shift); }
      ^
<program source>:1092:6: warning: no previous prototype for function 'blake2b_512_process_single_block'
void blake2b_512_process_single_block(ulong *h,const ulong* m,uint blockTemplateSize)
     ^
<program source>:1153:6: warning: no previous prototype for function 'blake2b_512_process_double_block_32'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1151:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_32
                                              ^
<program source>:1230:6: warning: no previous prototype for funct[2020-07-04 23:34:20.710]  opencl   thread #0 self-test failed
```

## SChernykh | 2020-07-05T07:11:35+00:00
@httran13 Try to remove first GPU (Intel UHD Graphics 630) from config.json.

## JosephMRally | 2021-03-06T21:15:17+00:00
i get this issue too using XMRig/6.9.0 clang/10.0.0. Does not seem to have been fixed.

# Action History
- Created by: minzak | 2020-06-14T19:33:30+00:00
- Closed at: 2020-08-19T01:12:58+00:00
