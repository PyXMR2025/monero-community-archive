---
title: combile sucess in termux, but opencl crashed
source_url: https://github.com/xmrig/xmrig/issues/2143
author: '317607692'
assignees: []
labels: []
created_at: '2021-03-01T09:05:55+00:00'
updated_at: '2021-04-12T14:08:55+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:08:55+00:00'
---

# Original Description
phone: meizu mx6
termux combile sucess, cpu mining is worked.
randomX

~/termux-xmrig $ ./xmrig --print-platforms
WARNING: linker: /data/data/com.termux/files/home/termux-xmrig/xmrig: unsupported flags DT_FLAGS_1=0x8000001
Number of platforms:        1

  Index:                    0
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 1.2 v1.r12p0-04rel0.2034b5b303dca12c48abf5518afe7d96
  Name:                     ARM Platform
  Vendor:                   ARM
  Extensions:               cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_3d_image_writes cl_khr_fp64 cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp16 cl_khr_gl_sharing cl_khr_icd cl_khr_egl_event cl_khr_egl_image cl_khr_image2d_from_buffer cl_arm_core_id cl_arm_printf cl_arm_thread_limit_hint cl_arm_non_uniform_work_group_size cl_arm_import_memory

~/termux-xmrig $ ls
gpu-start.sh    libOpenCLIcd.so  mine.zip  xmr-gpu.sh  xmrig-master
libOpenCL64.so  libOpencL.so     start.sh  xmrig       xmrig-master.zip
~/termux-xmrig $ vim gpu-start.sh
~/termux-xmrig $ vim gpu-start.sh
~/termux-xmrig $ cat gpu-start.sh
./xmrig -o stratum+tcp://xmr.f2pool.com:13531 -u 87CzKS7Fw8qS3CRFdD8BB23uWhxmu5G                                                       u7KuyMqYSN5eM7e5AfyA8ZovApAZ4vZT7eeRjwb3WLbSiCTEj8XamqhWJTCKxEsb -p x -k -a --no                                                       -cpu --opencl --opencl-loader=libOpenCL.so --opencl-platform=ARM --randomx-mode=                                                       light
~/termux-xmrig $ bash gpu-start.sh
WARNING: linker: /data/data/com.termux/files/home/termux-xmrig/xmrig: unsupporte                                                       d flags DT_FLAGS_1=0x8000001
 * ABOUT        XMRig/6.9.0 clang/11.1.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (1) 64-bit AES
                threads:1
 * MEMORY       3.0/3.7 GB (83%)
 * DONATE       0%
 * POOL #1      stratum+tcp://xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 ARM Platform/OpenCL 1.2 v1.r12p0-04rel0.2034b5b303dca12c48abf                                                       5518afe7d96
 * OPENCL GPU   #0 n/a Mali-T880 5 MHz cu:4 mem:934/3738 MB
 * CUDA         disabled
[2021-03-01 17:04:43.255]  net      use pool xmr.f2pool.com:13531  203.107.32.16                                                       2
[2021-03-01 17:04:43.257]  net      new job from xmr.f2pool.com:13531 diff 32768                                                        algo rx/0 height 2307356
[2021-03-01 17:04:43.258]  cpu      use argon2 implementation default
[2021-03-01 17:04:43.259]  randomx  init dataset algo rx/0 (1 threads) seed 3e99                                                       5eed94df8c92...
[2021-03-01 17:04:43.259]  randomx  fast RandomX mode disabled by config
[2021-03-01 17:04:43.259]  randomx  failed to allocate RandomX dataset, switchin                                                       g to slow mode (0 ms)
[2021-03-01 17:04:57.898]  randomx  dataset ready (14639 ms)
[2021-03-01 17:04:57.899]  cpu      use profile  rx  (1 thread) scratchpad 2048 KB
[2021-03-01 17:04:57.900]  cpu      READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (1 ms)
[2021-03-01 17:04:57.900]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |        64 |     8 |    128 | Mali-T880

after this, termux crashed and restart ......


# Discussion History
# Action History
- Created by: 317607692 | 2021-03-01T09:05:55+00:00
- Closed at: 2021-04-12T14:08:55+00:00
