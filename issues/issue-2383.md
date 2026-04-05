---
title: Help wanted ...
source_url: https://github.com/xmrig/xmrig/issues/2383
author: Saikatsaha1996
assignees: []
labels: []
created_at: '2021-05-16T11:39:20+00:00'
updated_at: '2021-07-04T18:33:48+00:00'
type: issue
status: closed
closed_at: '2021-05-27T12:40:53+00:00'
---

# Original Description
Can it support cn/gpu ?..

# Discussion History
## Spudz76 | 2021-05-17T20:28:36+00:00
Support was dropped from this official version but the [MoneroOcean/xmrig](https://github.com/MoneroOcean/xmrig) fork has it re-added.

So yes, but not here.

## Saikatsaha1996 | 2021-07-04T18:33:47+00:00
> Support was dropped from this official version but the [MoneroOcean/xmrig](https://github.com/MoneroOcean/xmrig) fork has it re-added.
> 
> So yes, but not here.

Any solution available ?..

~/clinfo $ ./clinfo
Number of platforms                               1
  Platform Name                                   QUALCOMM Snapdragon(TM)
  Platform Vendor                                 QUALCOMM
  Platform Version                                OpenCL 2.0 QUALCOMM build: commit #191610ae03 changeid #Ic907de5ed0 Date: 09/17/20 Thu Local Branch:  Remote Branch: refs/tags/AU_LINUX_ANDROID_LA.UM.9.12.10.00.00.582.274
  Platform Profile                                FULL_PROFILE
  Platform Extensions

  Platform Name                                   QUALCOMM Snapdragon(TM)
Number of devices                                 1
  Device Name                                     QUALCOMM Adreno(TM)
  Device Vendor                                   QUALCOMM
  Device Vendor ID                                0x5143
  Device Version                                  OpenCL 2.0 Adreno(TM) 650
  Driver Version                                  OpenCL 2.0 QUALCOMM build: commit #191610ae03 changeid #Ic907de5ed0 Date: 09/17/20 Thu Local Branch:  Remote Branch: refs/tags/AU_LINUX_ANDROID_LA.UM.9.12.10.00.00.582.274 Compiler E031.37.12.01
  Device OpenCL C Version                         OpenCL C 2.0 Adreno(TM) 650
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               3
  Max clock frequency                             1MHz
  Device Partition                                (core)
    Max number of sub-devices                     1
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             1024
  Preferred work group size multiple (kernel)     128
  Preferred / native vector sizes
    char                                                 1 / 1
    short                                                1 / 1
    int                                                  1 / 1
    long                                                 1 / 0
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1
    double                                               0 / 0        (n/a)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (n/a)
  Address bits                                    64, Little-Endian
  Global memory size                              3992293376 (3.718GiB)
  Error Correction support                        No
  Max memory allocation                           998073344 (951.8MiB)
  Unified memory for Host and Device              Yes
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Page size (QCOM)                                4096 bytes
  External memory padding (QCOM)                  0 bytes
  Preferred alignment for atomics
    SVM                                           128 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    65536 (64KiB)
  Preferred total size of global vars             1048576 (1024KiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        131072 (128KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   64 bytes
    Pitch alignment for 2D image buffers          64 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             16384x16384x2048 pixels
    Max number of read image args                 128
    Max number of write image args                64
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    6144
  Max pipe packet size                            1024
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     8
  Max constant buffer size                        65536 (64KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)
    Out-of-order execution                        Yes
    Profiling                                     Yes
  Queue properties (on device)
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                655376 (640KiB)
    Max size                                      655376 (640KiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    No
  Profiling timer resolution                      1000ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_3d_image_writes cl_img_egl_image cl_khr_byte_addressable_store cl_khr_depth_images cl_khr_egl_event cl_khr_egl_image cl_khr_fp16 cl_khr_gl_sharing cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_image2d_from_buffer cl_khr_mipmap_image cl_khr_srgb_image_writes cl_khr_subgroups cl_qcom_create_buffer_from_image cl_qcom_ext_host_ptr cl_qcom_ion_host_ptr cl_qcom_perf_hint cl_qcom_other_image cl_qcom_subgroup_shuffle cl_qcom_vector_image_ops cl_qcom_extract_image_plane cl_qcom_android_native_buffer_host_ptr cl_qcom_protected_context cl_qcom_priority_hint cl_qcom_compressed_yuv_image_read cl_qcom_compressed_image cl_qcom_ext_host_ptr_iocoherent cl_qcom_accelerated_image_ops cl_qcom_dot_product8 cl_qcom_reqd_sub_group_size cl_qcom_recordable_queues cl_qcom_ml_ops

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [P0]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 QUALCOMM Snapdragon(TM)
    Device Name                                   QUALCOMM Adreno(TM)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 QUALCOMM Snapdragon(TM)
    Device Name                                   QUALCOMM Adreno(TM)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  Invalid device type for platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 QUALCOMM Snapdragon(TM)
    Device Name                                   QUALCOMM Adreno(TM)
~/clinfo $

![Screenshot_20210704-235822](https://user-images.githubusercontent.com/72664192/124395911-7071cf00-dd24-11eb-849c-c54d51a640ea.png)




# Action History
- Created by: Saikatsaha1996 | 2021-05-16T11:39:20+00:00
- Closed at: 2021-05-27T12:40:53+00:00
