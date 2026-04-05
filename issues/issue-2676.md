---
title: OpenCL 1.1 & OpenCL 2.0 on Vega 8
source_url: https://github.com/xmrig/xmrig/issues/2676
author: jmthackett
assignees: []
labels: []
created_at: '2021-11-08T23:08:38+00:00'
updated_at: '2021-11-09T21:29:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Running with OpenCL 1.1, I get this:

```
[2021-11-08 22:41:46.967]  opencl   GPU #0 compiling...
[2021-11-08 22:41:47.760]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
input.cl:293:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:808:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:814:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:1047:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
```

Relevant logs and outputs:

```
➜  ~ sudo /usr/bin/xmrig --no-cpu --opencl -o xmr-eu1.nanopool.org:14433 -u redacted --tls --coin monero --opencl-platform=0 --randomx-1gb-pages
 * ABOUT        XMRig/6.15.3 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen Embedded V1605B with Radeon Vega Gfx (1) 64-bit AES
                L2:2.0 MB L3:4.0 MB 4C/8T NUMA:1
 * MEMORY       9.9/14.6 GB (68%)
                DIMM_A0: 16 GB DDR4 @ 2400 MHz TS2GSH64V4B         
                DIMM 0: <empty>
 * MOTHERBOARD  Seco - C40
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-eu1.nanopool.org:14433 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 Clover/OpenCL 1.1 Mesa 21.2.3
 * OPENCL GPU   #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1) 1100 MHz cu:8 mem:2150/3072 MB
 * CUDA         disabled
[2021-11-08 22:41:32.724]  net      use pool xmr-eu1.nanopool.org:14433 TLSv1.3 51.68.143.81
[2021-11-08 22:41:32.724]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-11-08 22:41:32.724]  net      new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2489095 (162 tx)
[2021-11-08 22:41:32.724]  cpu      use argon2 implementation AVX2
[2021-11-08 22:41:32.725]  msr      register values for "ryzen_17h" preset have been set successfully (1 ms)
[2021-11-08 22:41:32.725]  randomx  init dataset algo rx/0 (8 threads) seed fc593341a7cc779b...
[2021-11-08 22:41:35.266]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (2541 ms)
[2021-11-08 22:41:38.958]  net      new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2489095 (186 tx)
[2021-11-08 22:41:46.965]  randomx  dataset ready (11699 ms)
[2021-11-08 22:41:46.965]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       128 |     8 |    256 | AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|  1 |   0 |     n/a |       128 |     8 |    256 | AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
[2021-11-08 22:41:46.967]  opencl   GPU #0 compiling...
[2021-11-08 22:41:47.760]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
input.cl:293:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:808:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:814:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:1047:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier

[2021-11-08 22:41:47.760]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2021-11-08 22:41:47.760]  opencl   thread #1 self-test failed
[2021-11-08 22:41:47.761]  opencl   GPU #0 compiling...
[2021-11-08 22:41:48.492]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
input.cl:293:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:808:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:814:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier
input.cl:1047:12: error: OpenCL C version 1.1 does not support the 'static' storage class specifier

[2021-11-08 22:41:48.492]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-11-08 22:41:48.492]  opencl   thread #0 self-test failed
[2021-11-08 22:41:48.492]  opencl   disabled (failed to start threads)
[2021-11-08 22:42:18.548]  net      new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2489096 (69 tx)
[2021-11-08 22:42:47.026]  opencl   #0 n/a   0W  0C    0RPM 0/0MHz
[2021-11-08 22:42:47.026]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-11-08 22:43:02.507] no results yet
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        1 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        - |        - |      n/a |      n/a |      n/a |
[2021-11-08 22:43:06.585]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        1 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        - |        - |      n/a |      n/a |      n/a |
[2021-11-08 22:43:07.753]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-11-08 22:43:20.362]  net      new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2489096 (105 tx)
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        1 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        - |        - |      n/a |      n/a |      n/a |
[2021-11-08 22:43:24.825]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        1 |       -1 |      n/a |      n/a |      n/a | #0 n/a AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
|        - |        - |      n/a |      n/a |      n/a |
[2021-11-08 22:43:37.217]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-11-08 22:43:47.070]  opencl   #0 n/a   0W  0C    0RPM 0/0MHz
[2021-11-08 22:43:47.070]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-11-08 22:44:06.432]  signal   Ctrl+C received, exiting
[2021-11-08 22:44:06.432]  opencl   stopped (1 ms)

```
Under the second platform (OpenCL 2.0) I get a different error:
```
➜  ~ sudo /usr/bin/xmrig --no-cpu --opencl -o xmr-eu1.nanopool.org:14433 -u redacted --tls --opencl-platform=1 --randomx-1gb-pages --coin monero
 * ABOUT        XMRig/6.15.3 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen Embedded V1605B with Radeon Vega Gfx (1) 64-bit AES
                L2:2.0 MB L3:4.0 MB 4C/8T NUMA:1
 * MEMORY       14.2/14.6 GB (97%)
                DIMM_A0: 16 GB DDR4 @ 2400 MHz TS2GSH64V4B         
                DIMM 0: <empty>
 * MOTHERBOARD  Seco - C40
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-eu1.nanopool.org:14433 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (no devices)
 * CUDA         disabled
[2021-11-08 23:05:09.224]  net      xmr-eu1.nanopool.org:14433 incompatible/disabled algorithm "rx/0" detected, reconnect
[2021-11-08 23:05:09.224]  net      xmr-eu1.nanopool.org:14433 login error code: 6
```
`clinfo` shows - if I'm reading it correctly - that I have functioning OpenCL:
```
➜  ~ clinfo
Number of platforms                               2
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 21.2.3
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (3314.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD

  Platform Name                                   Clover
Number of devices                                 1
  Device Name                                     AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 21.2.3
  Device Numeric Version                          0x401000 (1.1.0)
  Driver Version                                  21.2.3
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               8
  Max clock frequency                             1100MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple (kernel)     64
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 0 / 0        (n/a)
    float                                                4 / 4       
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              3221225472 (3GiB)
  Error Correction support                        No
  Max memory allocation                           2254857830 (2.1GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     16
  Max constant buffer size                        67108864 (64MiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    ILs with version                              (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_fp64                                                      0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  Clover
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [MESA]
  clCreateContext(NULL, ...) [default]            Success [MESA]
  clCreateContext(NULL, ...) [other]              
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Clover
    Device Name                                   AMD Ryzen Embedded V1605B with Radeon Vega Gfx (RAVEN, DRM 3.41.0, 5.13.19-2-MANJARO, LLVM 12.0.1)

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.1
  ICD loader Profile                              OpenCL 3.0
```
And `xmrig` itself detects two platforms:
```
➜  ~ xmrig --print-platforms
Number of platforms:        2

  Index:                    0
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 1.1 Mesa 21.2.3
  Name:                     Clover
  Vendor:                   Mesa
  Extensions:               cl_khr_icd

  Index:                    1
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 2.0 AMD-APP (3314.0)
  Name:                     AMD Accelerated Parallel Processing
  Vendor:                   Advanced Micro Devices, Inc.
  Extensions:               cl_khr_icd cl_amd_event_callback 
```

Should this work with either approach? Am I missing something? 

# Discussion History
## Spudz76 | 2021-11-09T06:38:21+00:00
Probably won't work with vanilla distro drivers.  Definite OpenCL 1.2 minimum for xmrig though, that Mesa platform won't work.  Doesn't work with AMDGPU-Pro which would be ideal (maybe that's the second platform?).  Doesn't allegedly work with mainstream ROCM either.

But the PPA repo linked near [the bottom of this page](https://bruhnspace.com/en/bruhnspace-rocm-for-amd-apus/) claims to be ROCM 3.10 modded to support APU's like the V1605B and then that should work (it worked with [another OpenCL app against ROCM 3.10](https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/issues/398), and maybe not even the Bruhnspace one)

It would probably be worth trying the mainstream ROCM current 4.x version it might work yet be unsupported/unmentioned/untested/uncertified.

## jmthackett | 2021-11-09T08:12:55+00:00
The second platform is indeed AMDGPU-Pro, and I've tried ROCm now as well, both no joy. I'll check out that PPA later. Thanks!

On November 9, 2021 6:38:32 AM UTC, Tony Butler ***@***.***> wrote:
>Probably won't work with vanilla distro drivers.  Definite OpenCL 1.2
>minimum for xmrig though, that Mesa platform won't work.  Doesn't work
>with AMDGPU-Pro which would be ideal (maybe that's the second
>platform?).  Doesn't allegedly work with mainstream ROCM either.
>
>But the PPA repo linked near [the bottom of this
>page](https://bruhnspace.com/en/bruhnspace-rocm-for-amd-apus/) claims
>to be ROCM 3.10 modded to support APU's like the V1605B and then that
>should work (it worked with [another OpenCL app against ROCM
>3.10](https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX/issues/398),
>and maybe not even the Bruhnspace one)
>
>It would probably be worth trying the mainstream ROCM current 4.x
>version it might work yet be
>unsupported/unmentioned/untested/uncertified.
>
>-- 
>You are receiving this because you authored the thread.
>Reply to this email directly or view it on GitHub:
>https://github.com/xmrig/xmrig/issues/2676#issuecomment-963858389

-- Sent from /e/ Mail.

## Lonnegan | 2021-11-09T15:57:09+00:00
Besides: don't mine Monero via GPU! RandomX is a dedicated CPU mining algo, which runs bad on GPUs. Mine something with your GPU which makes sense for GPUs and is profitable! You can run one xmrig process mining Monero CPU-only and the other xmrig process (or any other mining software) mining something GPU friendly GPU-only.

## jmthackett | 2021-11-09T16:08:07+00:00
The monero website suggests it is suitable for CPU and GPU mining - is that not true? https://www.getmonero.org/resources/moneropedia/mining.html

## Lonnegan | 2021-11-09T16:32:58+00:00
No, that's not true anymore! That subpage is old, it's from the days some years ago, when Monero used PoW algo Cryptonight. See the text: "Monero uses a variant of CryptoNight Proof of Work (PoW) algorithm, which is designed for use in ordinary CPUs and GPUs." That's deprecated!

Today's version of Monero uses RandomX as algo and it is completely unsuitable for GPUs. You can reach 10 times higher profitability when you mine something with your GPU which is GPU friendly.

## Spudz76 | 2021-11-09T17:36:58+00:00
Or, mine something other than RandomX and be paid XMR directly, from MoneroOcean or similar pools.

Most of my "XMR" hashrate are GPUs.

## DeeDeeRanged | 2021-11-09T21:27:26+00:00
 pool like gulf.moneroocean.stream where you can mine monero with your CPU and with another miner like PhoenixMiner ethash with your GPU and get paid in monero. Thats what I am using now with one rig works great getting paid in monero. You can choose wich coin you want to mine with your iGPU depending on your vram.

# Action History
- Created by: jmthackett | 2021-11-08T23:08:38+00:00
