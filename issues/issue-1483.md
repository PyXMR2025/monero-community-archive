---
title: Support for OpenCL on CPU?
source_url: https://github.com/xmrig/xmrig/issues/1483
author: mukesh-610
assignees: []
labels:
- question
created_at: '2020-01-04T16:51:46+00:00'
updated_at: '2021-04-12T19:30:01+00:00'
type: issue
status: closed
closed_at: '2020-01-07T16:55:50+00:00'
---

# Original Description
Is there support (current or planned for future) for OpenCL on Intel CPUs?

`xmrig --print-platforms` gives me:

```
  Index:                    0
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 2.1 LINUX
  Name:                     Intel(R) CPU Runtime for OpenCL(TM) Applications
  Vendor:                   Intel(R) Corporation
  Extensions:               cl_khr_icd cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_depth_images cl_khr_3d_image_writes cl_intel_exec_by_local_thread cl_khr_spir cl_khr_fp64 cl_khr_image2d_from_buffer cl_intel_vec_len_hint
```

But running `xmrig --opencl --opencl-platform=0 [...]`
or
 `xmrig --opencl --opencl-platform=0 --opencl-devices=0 [...]`
tells me:

`* OPENCL       disabled (no devices)`

If there is current support for OpenCL on CPU, can you tell me how to enable it? If there is not, is it planned for future?

# Discussion History
## xmrig | 2020-01-04T17:01:38+00:00
Intel OpenCL is very slow and currently broken, so not much reason to ever fix it, but error `no devices` means you platform contains no GPU devices (`CL_DEVICE_TYPE_GPU`). You can verify it by using `clinfo`.
Thank you.

## mukesh-610 | 2020-01-07T16:55:50+00:00
I understand that implementing Intel OpenCL might be inefficient. Thanks and great work!

## gilandriani | 2020-06-04T10:27:33+00:00
I have the same question...

I my case, hardware is detected by CLINFO

Hardware is detected by xmring --print-plataform

Processes start and DIE:
$:~/xmrig/build$ sudo /home/dg1906/xmrig/build/xmrig --opencl --opencl-platform=Intel -o xmr.luxor.tech:700 -u XXXXX -p x -k --verbose --coin monero -a rx/0
 * ABOUT        XMRig/5.11.2_GA gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       7.3/15.5 GB (47%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.luxor.tech:700 coin monero
 * COMMANDS     hashrate, pause, resume
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 2.1 
 * OPENCL GPU   #0 n/a Intel(R) Gen9 HD Graphics NEO 1100 MHz cu:24 mem:4095/12715 MB
 * CUDA         disabled
[2020-06-04 07:25:22.501]  net  use pool xmr.luxor.tech:700  34.107.237.122
[2020-06-04 07:25:22.502]  net  new job from xmr.luxor.tech:700 diff 5000 algo rx/0 height 2113184
[2020-06-04 07:25:22.502]  cpu  use argon2 implementation AVX2
[2020-06-04 07:25:22.505]  msr  0x000001a4:0x000000000000000f -> 0x000000000000000f
[2020-06-04 07:25:22.505]  msr  register values for "intel" preset has been set successfully (3 ms)
[2020-06-04 07:25:22.505]  rx   init dataset algo rx/0 (4 threads) seed fe80b8ac27f04d83...
[2020-06-04 07:25:22.720]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (215 ms)
[2020-06-04 07:25:39.312]  net  new job from xmr.luxor.tech:700 diff 5000 algo rx/0 height 2113184
[2020-06-04 07:25:40.653]  rx   dataset ready (17933 ms)
[2020-06-04 07:25:40.653]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
[2020-06-04 07:25:40.675]  cpu  READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (22 ms)
[2020-06-04 07:25:40.694]  ocl  use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 |     n/a |  384 |  8 |  0 |  - |  8 |  768 | Intel(R) Gen9 HD Graphics NEO
[2020-06-04 07:25:41.576]  ocl  GPU #0 compiling...
free(): invalid pointer
Abortado


[clinfo.txt](https://github.com/xmrig/xmrig/files/4729298/clinfo.txt)

[xmrig_print_platforms.txt](https://github.com/xmrig/xmrig/files/4729304/xmrig_print_platforms.txt)


## bcheeves | 2021-04-12T19:30:01+00:00
@gilandriani 
I see that you're trying to mine randomx with your GPU, which is rather pointless. it's optimized for CPU only, see also:
https://github.com/xmrig/xmrig/issues/1816
if you're mining rx0, remove the opencl commands.

# Action History
- Created by: mukesh-610 | 2020-01-04T16:51:46+00:00
- Closed at: 2020-01-07T16:55:50+00:00
