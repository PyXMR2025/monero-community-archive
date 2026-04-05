---
title: 'OpenCL: error: use of undeclared identifier ''amd_bfe'''
source_url: https://github.com/xmrig/xmrig/issues/3628
author: gptlang
assignees: []
labels: []
created_at: '2025-02-03T21:46:04+00:00'
updated_at: '2025-02-11T16:50:41+00:00'
type: issue
status: closed
closed_at: '2025-02-11T16:50:41+00:00'
---

# Original Description
**Describe the bug**
Unable to mine on OpenCL AMD GPU

**To Reproduce**
`/xmrig --no-cpu --opencl -o <ANY_POOL> -u <MONERO ADDRESS> -k --opencl-platform=0 --opencl-loader=
/usr/lib64/libOpenCL.so.1.0.0`

**Expected behavior**
Run

**Required data**
 - XMRig version: XMRig 6.22.2-mo1
 - Miner log as text or screenshot
 - OS: Fedora Linux (6.12.11-200.fc41.x86_64)
 - AMD Radeon RX 570 Series [Discrete]

**Additional context**
AMD Drivers are installed by default. `libclc-devel` was also installed to fix `fatal error: 'clc/clc.h' file not found`.


# Discussion History
## ahorek | 2025-02-10T21:08:42+00:00
this is not the repository for the Monero version, but the code in question looks the same.

your gpu driver has to lie about the cl_amd_media_ops2 support https://github.com/xmrig/xmrig/blob/master/src/backend/opencl/cl/cn/wolf-aes.cl#L7
you may try to use the fallback variant

btw is there a reason why you're forcing the OpenCL 1.0 library? I think xmrig needs at least 1.2 which your gpu supports.

## gptlang | 2025-02-10T21:31:52+00:00
> btw is there a reason why you're forcing the OpenCL 1.0 library? I think xmrig needs at least 1.2 which your gpu supports.

That was th only version I could find on Fedora. I've switched to Arch now so I no longer need to override the OpenCL library.

I'm not getting a different problem:
```
[2025-02-10 21:30:46.637]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2025-02-10 21:30:46.637]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2025-02-10 21:30:46.639]  opencl   thread #0 self-test failed
[2025-02-10 21:30:46.654]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2025-02-10 21:30:46.654]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2025-02-10 21:30:46.655]  opencl   thread #1 self-test failed
[2025-02-10 21:30:46.655]  opencl   disabled (failed to start threads)
```

## ahorek | 2025-02-10T21:55:52+00:00
It's difficult to say without a log, but it seems to be a driver related issue. What does "clinfo" report?

do you even have amd drivers installed? Mesa's clover isn't supported, rusticl may work if you have no other option.

## gptlang | 2025-02-11T00:55:08+00:00
<details>

```
Number of platforms                               2
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3380.4)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3635.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     Ellesmere
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 AMD-APP (3380.4)
  Driver Version                                  3380.4 (PAL,HSAIL)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Radeon RX 570 Series
  Device PCI-e ID (AMD)                           0x67df
  Device Topology (AMD)                           PCI-E, 0000:04:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               32
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1340MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     32
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              8589934592 (8GiB)
  Global free memory (AMD)                        8321000 (7.936GiB) 0 (0B)
  Global memory channels (AMD)                    8
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7301444403 (6.8GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    6571299840 (6.12GiB)
  Preferred total size of global vars             8589934592 (8GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            456340275 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                64
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            3006477107 (2.8GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        7301444403 (6.8GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)                    
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1739202954482494835ns (Mon Feb 10 15:55:54 2025)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    Number of async queues (AMD)                  4
    Max real-time compute queues (AMD)            1
    Max real-time compute units (AMD)             0
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_khr_gl_depth_images cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_gl_event cl_khr_depth_images cl_khr_mipmap_image cl_khr_mipmap_image_writes cl_amd_copy_buffer_p2p 

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContext(NULL, ...) [other]              <error: no devices in non-default plaforms>
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   Ellesmere
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   Ellesmere
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   Ellesmere

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.2
  ICD loader Profile                              OpenCL 3.0

```

</details>

There aren't really any additional logs from xmrig

## gptlang | 2025-02-11T01:02:16+00:00
I installed `opencl-rusticl-mesa` with the same error

## ahorek | 2025-02-11T01:58:35+00:00
What coin do you want to mine?

The drivers looks ok, but the opencl code cannot be compiled. Sry, but without a build log I cannot say what the reason could be.

## gptlang | 2025-02-11T02:35:21+00:00
Monero.

How do I get a build log?

## ahorek | 2025-02-11T11:58:27+00:00
The RandomX algorithm (monero) is intentionally engineered to perform poorly on GPUs and ASICs. For instance, the best AMD card (12 times more powerful than yours) 7900 XTX can do 1000h/s while a 14-year-old bulldozer famous for its inefficiency can do 3000h/s with less power.

The existing GPU implementation serves as a proof of concept, demonstrating its inefficiency. It's written in assembly, so older GPUs may not work. Attempting to fix it would be pointless...

If you want to utilize the GPU somehow, mine something else.

# Action History
- Created by: gptlang | 2025-02-03T21:46:04+00:00
- Closed at: 2025-02-11T16:50:41+00:00
