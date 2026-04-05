---
title: AMD OpenCL - error CL_INVALID_BUFFER_SIZE - Mesa  Navi22  RX 6700XT (12GiB)
source_url: https://github.com/xmrig/xmrig/issues/3768
author: kallisti5
assignees: []
labels: []
created_at: '2026-01-24T15:34:43+00:00'
updated_at: '2026-01-24T16:46:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
```
 * ABOUT        XMRig/6.25.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.6.0 hwloc/2.12.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       17.7/62.7 GB (28%)
                DIMM_A1: <empty>
                DIMM_A2: 32 GB DDR4 @ 2400 MHz KF3200C16D4/32GX
                DIMM_B1: <empty>
                DIMM_B2: 32 GB DDR4 @ 2400 MHz KF3200C16D4/32GX
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - ROG CROSSHAIR VII HERO
 * DONATE       3%
 * ASSEMBLY     auto:ryzen
 * POOL #1      XXX
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled
 * OPENCL       #0 rusticl/OpenCL 3.0
 * OPENCL GPU   #0 n/a AMD Radeon RX 6700 XT (radeonsi, navi22, LLVM 21.1.5, DRM 3.64, 6.17.9-2-cachyos) 2855 MHz cu:40 mem:2047/12288 MB
 * CUDA         disabled
.
>
2026-01-24 09:29:13.533]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       360 |     8 |    720 | AMD Radeon RX 6700 XT (radeonsi, navi22, LLVM 21.1.5, DRM 3.64, 6.17.9-2-cachyos)
[2026-01-24 09:29:13.533]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080
[2026-01-24 09:29:13.533]  opencl   thread #0 failed with error RandomX dataset is not available
[2026-01-24 09:29:13.533]  opencl   thread #0 self-test failed
[2026-01-24 09:29:13.533]  opencl   disabled (failed to start threads)
```

**Additional context**
```
clinfo
Number of platforms                               1
  Platform Name                                   rusticl
  Platform Vendor                                 Mesa/X.org
  Platform Version                                OpenCL 3.0
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_khr_byte_addressable_store cl_khr_create_command_queue cl_khr_expect_assume cl_khr_extended_bit_ops cl_khr_extended_versioning cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_il_program cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_integer_dot_product cl_khr_spirv_no_integer_wrap_decoration cl_khr_spirv_queries cl_khr_suggested_local_work_size cl_khr_spirv_linkonce_odr cl_khr_fp16 cl_khr_gl_sharing cles_khr_int64 cl_khr_kernel_clock cl_khr_3d_image_writes cl_khr_depth_images cl_ext_image_unorm_int_2_101010 cl_khr_pci_bus_info cl_khr_priority_hints cl_khr_device_uuid cl_khr_subgroup_shuffle cl_khr_subgroup_shuffle_relative cl_arm_shared_virtual_memory cl_ext_buffer_device_address
  Platform Extensions with Version                cl_khr_icd                                                       0x800000 (2.0.0)
                                                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_create_command_queue                                      0x400000 (1.0.0)
                                                  cl_khr_expect_assume                                             0x400000 (1.0.0)
                                                  cl_khr_extended_bit_ops                                          0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_il_program                                                0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_integer_dot_product                                       0x800000 (2.0.0)
                                                  cl_khr_spirv_no_integer_wrap_decoration                          0x400000 (1.0.0)
                                                  cl_khr_spirv_queries                                             0x400000 (1.0.0)
                                                  cl_khr_suggested_local_work_size                                 0x400000 (1.0.0)
                                                  cl_khr_spirv_linkonce_odr                                        0x400000 (1.0.0)
                                                  cl_khr_fp16                                                      0x400000 (1.0.0)
                                                  cl_khr_gl_sharing                                                0x400000 (1.0.0)
                                                  cles_khr_int64                                                   0x400000 (1.0.0)
                                                  cl_khr_kernel_clock                                              0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_khr_depth_images                                              0x400000 (1.0.0)
                                                  cl_ext_image_unorm_int_2_101010                                  0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)
                                                  cl_khr_priority_hints                                            0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle                                          0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle_relative                                 0x400000 (1.0.0)
                                                  cl_arm_shared_virtual_memory                                     0x400000 (1.0.0)
                                                  cl_ext_buffer_device_address                                     0x400002 (1.0.2)
  Platform Numeric Version                        0xc00000 (3.0.0)
  Platform Extensions function suffix             MESA
  Platform Host timer resolution                  1ns

  Platform Name                                   rusticl
Number of devices                                 1
  Device Name                                     AMD Radeon RX 6700 XT (radeonsi, navi22, LLVM 21.1.5, DRM 3.64, 6.17.9-2-cachyos)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 3.0
  Device UUID                                     00000000-0c00-0000-0000-000000000000
  Driver UUID                                     414d442d-4d45-5341-2d44-525600000000
  Valid Device LUID                               No
  Device LUID                                     0000-000000000000
  Device Node Mask                                0
  Device Numeric Version                          0xc00000 (3.0.0)
  Driver Version                                  25.2.7-cachyos1.2
  Device OpenCL C Version                         OpenCL C 1.2
  Device OpenCL C Numeric Version                 0x402000 (1.2.0)
  Device OpenCL C all versions                    OpenCL C                                                         0xc00000 (3.0.0)
                                                  OpenCL C                                                         0x402000 (1.2.0)
                                                  OpenCL C                                                         0x401000 (1.1.0)
                                                  OpenCL C                                                         0x400000 (1.0.0)
  Device OpenCL C features                        __opencl_c_integer_dot_product_input_4x8bit                      0x800000 (2.0.0)
                                                  __opencl_c_integer_dot_product_input_4x8bit_packed               0x800000 (2.0.0)
                                                  __opencl_c_int64                                                 0x400000 (1.0.0)
                                                  __opencl_c_kernel_clock_scope_device                             0x400000 (1.0.0)
                                                  __opencl_c_kernel_clock_scope_sub_group                          0x400000 (1.0.0)
                                                  __opencl_c_images                                                0x400000 (1.0.0)
                                                  __opencl_c_read_write_images                                     0x400000 (1.0.0)
                                                  __opencl_c_3d_image_writes                                       0x400000 (1.0.0)
                                                  __opencl_c_ext_image_unorm_int_2_101010                          0x400000 (1.0.0)
                                                  __opencl_c_subgroups                                             0x400000 (1.0.0)
  Latest conformance test passed                  v0000-01-01-00
  Device Type                                     GPU
  Device PCI bus info (KHR)                       PCI-E, 0000:0c:00.0
  Device Profile                                  EMBEDDED_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               40
  Max clock frequency                             2855MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             1024
  Preferred work group size multiple (device)     64
  Preferred work group size multiple (kernel)     64
  Max sub-groups per work group                   32
  Preferred / native vector sizes
    char                                                 1 / 1
    short                                                1 / 1
    int                                                  1 / 1
    long                                                 1 / 1
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1
    double                                               0 / 0        (n/a)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
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
  Max memory allocation                           2147483647 (2GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   No
    Fine-grained system sharing                   No
    Atomics                                       No
  Shared Virtual Memory (SVM) capabilities (ARM)
    Coarse-grained buffer sharing                 Yes
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
    Max size for 1D images from buffer            134217727 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   0 bytes
    Pitch alignment for 2D image buffers          0 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             8192x8192x8192 pixels
    Max number of read image args                 32
    Max number of write image args                16
    Max number of read/write image args           16
  Pipe support                                    No
  Max number of pipe args                         0
  Max active pipe reservations                    0
  Max pipe packet size                            0
  Local memory type                               Global
  Local memory size                               65536 (64KiB)
  Max number of constant args                     16
  Max constant buffer size                        67108864 (64MiB)
  Generic address space support                   No
  Max size of kernel argument                     4096 (4KiB)
  Queue properties (on host)
    Out-of-order execution                        Yes
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
  Profiling timer resolution                      10ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Non-uniform work-groups                       No
    Work-group collective functions               No
    Sub-group independent forward progress        No
    IL version                                    SPIR-V_1.0 SPIR-V_1.1 SPIR-V_1.2 SPIR-V_1.3 SPIR-V_1.4 SPIR-V_1.5 SPIR-V_1.6
    ILs with version                              SPIR-V                                                           0x400000 (1.0.0)
                                                  SPIR-V                                                           0x401000 (1.1.0)
                                                  SPIR-V                                                           0x402000 (1.2.0)
                                                  SPIR-V                                                           0x403000 (1.3.0)
                                                  SPIR-V                                                           0x404000 (1.4.0)
                                                  SPIR-V                                                           0x405000 (1.5.0)
                                                  SPIR-V                                                           0x406000 (1.6.0)
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_create_command_queue cl_khr_expect_assume cl_khr_extended_bit_ops cl_khr_extended_versioning cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_il_program cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_integer_dot_product cl_khr_spirv_no_integer_wrap_decoration cl_khr_spirv_queries cl_khr_suggested_local_work_size cl_khr_spirv_linkonce_odr cl_khr_fp16 cl_khr_gl_sharing cles_khr_int64 cl_khr_kernel_clock cl_khr_3d_image_writes cl_khr_depth_images cl_ext_image_unorm_int_2_101010 cl_khr_pci_bus_info cl_khr_priority_hints cl_khr_device_uuid cl_khr_subgroup_shuffle cl_khr_subgroup_shuffle_relative cl_arm_shared_virtual_memory cl_ext_buffer_device_address
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_create_command_queue                                      0x400000 (1.0.0)
                                                  cl_khr_expect_assume                                             0x400000 (1.0.0)
                                                  cl_khr_extended_bit_ops                                          0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_il_program                                                0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_integer_dot_product                                       0x800000 (2.0.0)
                                                  cl_khr_spirv_no_integer_wrap_decoration                          0x400000 (1.0.0)
                                                  cl_khr_spirv_queries                                             0x400000 (1.0.0)
                                                  cl_khr_suggested_local_work_size                                 0x400000 (1.0.0)
                                                  cl_khr_spirv_linkonce_odr                                        0x400000 (1.0.0)
                                                  cl_khr_fp16                                                      0x400000 (1.0.0)
                                                  cl_khr_gl_sharing                                                0x400000 (1.0.0)
                                                  cles_khr_int64                                                   0x400000 (1.0.0)
                                                  cl_khr_kernel_clock                                              0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_khr_depth_images                                              0x400000 (1.0.0)
                                                  cl_ext_image_unorm_int_2_101010                                  0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)
                                                  cl_khr_priority_hints                                            0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle                                          0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle_relative                                 0x400000 (1.0.0)
                                                  cl_arm_shared_virtual_memory                                     0x400000 (1.0.0)
                                                  cl_ext_buffer_device_address                                     0x400002 (1.0.2)

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  rusticl
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [MESA]
  clCreateContext(NULL, ...) [default]            Success [MESA]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 rusticl
    Device Name                                   AMD Radeon RX 6700 XT (radeonsi, navi22, LLVM 21.1.5, DRM 3.64, 6.17.9-2-cachyos)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 rusticl
    Device Name                                   AMD Radeon RX 6700 XT (radeonsi, navi22, LLVM 21.1.5, DRM 3.64, 6.17.9-2-cachyos)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 rusticl
    Device Name                                   AMD Radeon RX 6700 XT (radeonsi, navi22, LLVM 21.1.5, DRM 3.64, 6.17.9-2-cachyos)

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.4
  ICD loader Profile                              OpenCL 3.0
```


# Discussion History
## kallisti5 | 2026-01-24T15:35:57+00:00
OpenCL configuration was generated by xmrig, but I tuned a few things down trying to get it to work (it didn't help)
(disabled adl, reduced to 1 thread instead of 2.  Dropped Intensity to 360)
```
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "Mesa",
        "adl": false,
.
.
        "rx": [
            {
                "index": 0,
                "intensity": 360,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
```

## SChernykh | 2026-01-24T16:46:40+00:00
`opencl   thread #0 failed with error RandomX dataset is not available`
GPU driver didn't let it allocate 2+ GB for the dataset. In any case, mining RandomX on GPU is pointless because it's VERY slow and inefficient. You should disable OpenCL in the config if you're mining RandomX.

# Action History
- Created by: kallisti5 | 2026-01-24T15:34:43+00:00
