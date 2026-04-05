---
title: 'OpenCL: CL_INVALID_BUFFER_SIZE on RX 6700 XT 12GB with rusticl loader'
source_url: https://github.com/xmrig/xmrig/issues/3335
author: Zipdox2
assignees: []
labels: []
created_at: '2023-09-19T22:21:34+00:00'
updated_at: '2023-09-20T14:38:16+00:00'
type: issue
status: closed
closed_at: '2023-09-20T14:38:15+00:00'
---

# Original Description
**Describe the bug**
```
[2023-09-19 23:08:27.682]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080
```
Looking at other issues, this is usually the case when there is not enough VRAM, but I have 12GB so that shouldn't be the problem. It's possible that the Mesa ICD is to blame and I should file a bug with mesa, but I need to investigate this further first.

**To Reproduce**
- Have a Navi 20 series card with enough VRAM
- Install mesa-opencl-icd (on Debian at least)
- Set the opencl platform config to `Mesa/X.org`
- Set cpu enabled to `false` debugging purposes
- Run `RUSTICL_ENABLE=radeonsi ./xmrig`

```
[2023-09-19 23:08:27.682]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080
```

**Expected behavior**
It Just Werks™

**Required data**
 - [miner.log](https://github.com/xmrig/xmrig/files/12666815/miner.log)
 - [config.json](https://github.com/xmrig/xmrig/files/12666798/config.txt)
 - OS: Debian sid
 - GPU: AMD Radeon RX 6700 XT (navi22, LLVM 15.0.7, DRM 3.54, 6.5.0-1-rt-amd64)

**Additional context**
I managed to figure out how to get OpenCL working with the Mesa rusticl ICD, which is necessary since the old Mesa ICD doesn't support newer Navi cards. I had to set the platform parameters in the opencl part of the configuration to `Mesa/X.org` or I would get a `(selected OpenCL platform NOT found)` error. I also had to set the environment variable `RUSTICL_ENABLE=radeonsi`.

# Discussion History
## SChernykh | 2023-09-20T09:06:00+00:00
Can you post the output of `clinfo` util? Search for `Max memory allocation` there.

## Zipdox2 | 2023-09-20T12:00:55+00:00
Output of `RUSTICL_ENABLE=radeonsi clinfo -d0:0`:

```
  Platform Name                                   rusticl
  Device Name                                     AMD Radeon RX 6700 XT (navi22, LLVM 15.0.7, DRM 3.54, 6.5.0-1-rt-amd64)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 3.0 
  Device Numeric Version                          0xc00000 (3.0.0)
  Driver Version                                  23.1.7-1
  Device OpenCL C Version                         OpenCL C 1.2 
  Device OpenCL C all versions                    OpenCL C                                                         0xc00000 (3.0.0)
                                                  OpenCL C                                                         0x402000 (1.2.0)
                                                  OpenCL C                                                         0x401000 (1.1.0)
                                                  OpenCL C                                                         0x400000 (1.0.0)
  Device OpenCL C features                        __opencl_c_int64                                                 0x400000 (1.0.0)
                                                  __opencl_c_images                                                0x400000 (1.0.0)
                                                  __opencl_c_3d_image_writes                                       0x400000 (1.0.0)
  Latest conformance test passed                  v0000-01-01-00
  Device Type                                     GPU
  Device Profile                                  EMBEDDED_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               40
  Max clock frequency                             2800MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             1024
  Preferred work group size multiple (device)     64
  Preferred work group size multiple (kernel)     64
  Max sub-groups per work group                   0
  Preferred / native vector sizes                 
    char                                                 1 / 1       
    short                                                1 / 1       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 0 / 0        (n/a)
    float                                                1 / 1       
    double                                               0 / 0        (n/a)
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
  Double-precision Floating-point support         (n/a)
  Address bits                                    64, Little-Endian
  Global memory size                              12884901888 (12GiB)
  Error Correction support                        No
  Max memory allocation                           2147483648 (2GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 No
    Fine-grained buffer sharing                   No
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       4096 bits (512 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Atomic memory capabilities                      relaxed, work-group scope
  Atomic fence capabilities                       relaxed, acquire/release, work-group scope
  Max size for global variable                    0
  Preferred total size of global vars             0
  Global Memory cache type                        None
  Image support                                   Yes
    Max number of samplers per kernel             32
    Max size for 1D images from buffer            268435455 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   0 bytes
    Pitch alignment for 2D image buffers          0 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             8192x8192x8192 pixels
    Max number of read image args                 32
    Max number of write image args                16
    Max number of read/write image args           0
  Pipe support                                    No
  Max number of pipe args                         0
  Max active pipe reservations                    0
  Max pipe packet size                            0
  Local memory type                               Global
  Local memory size                               65536 (64KiB)
  Max number of constant args                     16
  Max constant buffer size                        2147483648 (2GiB)
  Generic address space support                   No
  Max size of kernel argument                     67108864 (64MiB)
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Device enqueue capabilities                     (n/a)
  Queue properties (on device)                    
    Out-of-order execution                        No
    Profiling                                     No
    Preferred size                                0
    Max size                                      0
  Max queues on device                            0
  Max events on device                            0
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Non-uniform work-groups                       No
    Work-group collective functions               No
    Sub-group independent forward progress        No
    IL version                                    SPIR-V_1.0 SPIR-V_1.1 SPIR-V_1.2 SPIR-V_1.3 SPIR-V_1.4
    ILs with version                              SPIR-V                                                           0x400000 (1.0.0)
                                                  SPIR-V                                                           0x401000 (1.1.0)
                                                  SPIR-V                                                           0x402000 (1.2.0)
                                                  SPIR-V                                                           0x403000 (1.3.0)
                                                  SPIR-V                                                           0x404000 (1.4.0)
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_il_program cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cles_khr_int64 cl_khr_3d_image_writes
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_il_program                                                0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cles_khr_int64                                                   0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
```
Indeed it appears the rusticl loader only supports 2GB. I'll open an issue with Mesa then.

## Zipdox2 | 2023-09-20T14:38:15+00:00
https://gitlab.freedesktop.org/mesa/mesa/-/issues/9844

# Action History
- Created by: Zipdox2 | 2023-09-19T22:21:34+00:00
- Closed at: 2023-09-20T14:38:15+00:00
