---
title: Double GPU
source_url: https://github.com/xmrig/xmrig/issues/1358
author: GehogHeg
assignees: []
labels:
- need feedback
created_at: '2019-12-01T18:57:55+00:00'
updated_at: '2021-04-12T15:13:04+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:13:04+00:00'
---

# Original Description
Hello. Why do I have twice the GPU? I have physically 3 GPUs. After running a new xmrig it shows me 0, 1, 2, 3, 4, 5 GPUs (6 GPUs). When I only plug in one GPU xmrig it shows me 0.1 GPU. Why? What's wrong? Previously there was no problem. Thanks

# Discussion History
## hawk-eye77 | 2019-12-01T19:01:11+00:00
But they are working or not? 

## GehogHeg | 2019-12-01T19:06:31+00:00
Do not work. And xmrig reports as well: CL_MEM_OBJECT_ALLOCATION_FAILURE...

## xmrig | 2019-12-02T01:02:12+00:00
It double threads, 2 threads per GPU, about `CL_MEM_OBJECT_ALLOCATION_FAILURE` please show full miner output.
Thank you.

## GehogHeg | 2019-12-02T02:23:58+00:00
Thank you for your response. I tested the rig with 3x AMD MSI R9 270 and rig 3x 3x AMD MSI RX 480. Both the same problem. I just set up the pool and wallet and turned on the open cl for the GPU (nothing else).... :

 * ABOUT        XMRig/5.1.0 MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   unavailable
 * CPU          Intel(R) Celeron(R) CPU G1840 @ 2.80GHz (1) x64 -AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * MEMORY       2.3/3.9 GB (57%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      pool.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-12-02 03:05:34.724] configuration saved to: "C:\Users\Ge\Desktop\xmrig 5 1 0\config.json"
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (1800.11)
 * OPENCL GPU   #0 03:00.0 AMD Radeon R9 200 Series (Pitcairn) 1150 MHz cu:20 mem:1344/2048 MB
 * OPENCL GPU   #1 01:00.0 AMD Radeon R9 200 Series (Pitcairn) 1150 MHz cu:20 mem:1344/2048 MB
 * OPENCL GPU   #2 04:00.0 AMD Radeon R9 200 Series (Pitcairn) 1150 MHz cu:20 mem:1344/2048 MB
 * CUDA         disabled
[2019-12-02 03:05:34.859]  net  use pool pool.minexmr.com:4444  37.59.44.193
[2019-12-02 03:05:34.860]  net  new job from pool.minexmr.com:4444 diff 75000 algo rx/0 height 1979665
[2019-12-02 03:05:34.861]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f61d47e1e...
[2019-12-02 03:05:34.865]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (4 ms)
[2019-12-02 03:05:52.010]  rx   dataset ready (17144 ms)
[2019-12-02 03:05:52.010]  cpu  use profile  rx  (1 thread) scratchpad 2048 KB
[2019-12-02 03:05:52.032]  cpu  READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (20 ms)
[2019-12-02 03:05:52.043]  ocl  use profile  rx  (6 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 03:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  1 |   0 | 03:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  2 |   1 | 01:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  3 |   1 | 01:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  4 |   2 | 04:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  5 |   2 | 04:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
[2019-12-02 03:05:52.660]  ocl  READY threads 6/6 (557 ms)
[2019-12-02 03:05:52.822]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 03:05:52.832]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 03:05:52.887]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 03:05:52.888]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 03:05:52.922]  ocl  thread #1 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 03:05:52.923]  ocl  thread #4 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 03:05:52.923]  ocl  thread #2 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 03:05:52.924]  ocl  thread #3 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 03:06:52.308] speed 10s/60s/15m 155.4 153.9 n/a H/s max 166.6 H/s
[2019-12-02 03:07:52.347] speed 10s/60s/15m 128.9 144.4 n/a H/s max 166.6 H/s
[2019-12-02 03:08:52.379] speed 10s/60s/15m 150.8 152.4 n/a H/s max 166.6 H/s
[2019-12-02 03:09:12.964]  net  new job from pool.minexmr.com:4444 diff 50000 algo rx/0 height 1979665
[2019-12-02 03:09:52.438] speed 10s/60s/15m 135.7 162.2 n/a H/s max 182.4 H/s
[2019-12-02 03:10:52.484] speed 10s/60s/15m 165.5 156.5 n/a H/s max 182.4 H/s



## GehogHeg | 2019-12-02T22:22:29+00:00
Thank you for your response. I tested the rig with 3x AMD MSI R9 270 and rig 3x 3x AMD MSI RX 480. Both the same problem. I just set up the pool and wallet and turned on the open cl for the GPU (nothing else)....
 * ABOUT        XMRig/5.1.0 MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   unavailable
 * CPU          Intel(R) Celeron(R) CPU G1840 @ 2.80GHz (1) x64 -AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * MEMORY       1.7/3.9 GB (43%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      pool.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (1800.11)
 * OPENCL GPU   #0 03:00.0 AMD Radeon R9 200 Series (Pitcairn) 1150 MHz cu:20 mem:1344/2048 MB
 * OPENCL GPU   #1 01:00.0 AMD Radeon R9 200 Series (Pitcairn) 1150 MHz cu:20 mem:1344/2048 MB
 * OPENCL GPU   #2 04:00.0 AMD Radeon R9 200 Series (Pitcairn) 1150 MHz cu:20 mem:1344/2048 MB
 * CUDA         disabled
[2019-12-02 23:18:48.417]  net  use pool pool.minexmr.com:4444  37.59.43.136
[2019-12-02 23:18:48.417]  net  new job from pool.minexmr.com:4444 diff 75000 algo rx/0 height 1980273
[2019-12-02 23:18:48.418]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f61d47e1e...
[2019-12-02 23:18:48.423]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (4 ms)
[2019-12-02 23:19:02.721]  net  new job from pool.minexmr.com:4444 diff 75000 algo rx/0 height 1980274
[2019-12-02 23:19:05.665]  rx   dataset ready (17241 ms)
[2019-12-02 23:19:05.666]  cpu  use profile  rx  (1 thread) scratchpad 2048 KB
[2019-12-02 23:19:05.676]  cpu  READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (9 ms)
[2019-12-02 23:19:05.687]  ocl  use profile  rx  (6 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 03:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  1 |   0 | 03:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  2 |   1 | 01:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  3 |   1 | 01:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  4 |   2 | 04:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
|  5 |   2 | 04:00.0 |  320 |  8 |  0 |  - |  8 |  640 | AMD Radeon R9 200 Series (Pitcairn)
[2019-12-02 23:19:06.183]  ocl  READY threads 6/6 (481 ms)
[2019-12-02 23:19:06.227]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 23:19:06.231]  ocl  thread #1 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 23:19:09.045]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 23:19:09.334]  ocl  thread #3 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 23:19:30.783]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 23:19:31.205]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2019-12-02 23:19:31.904]  ocl  thread #4 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 23:19:31.906]  ocl  thread #5 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2019-12-02 23:20:06.073] speed 10s/60s/15m n/a 2.2 n/a H/s max 69.9 H/s
[2019-12-02 23:21:06.126] speed 10s/60s/15m n/a n/a n/a H/s max 69.9 H/s


## d9beuD | 2019-12-04T08:10:23+00:00
Same here since I upgraded XMRig to 5.1.0 for the algo fork.

With latest AMD drivers:
- On my PC (Windows 1903, i7 4790, RX 5700 XT) all is good.
- On my MacBook Pro (Windows 1905 (Boot Camp), i7 9750H, RX 555X) it works
- On my Rig (Windows 1905, 2x RX 380, 2x RX 480, 1x RX 570) 0 GPU is working

![Annotation 2019-12-03 213036](https://user-images.githubusercontent.com/53569029/70124748-bf054600-1675-11ea-9181-dc91095b2619.jpg)


## GehogHeg | 2019-12-04T16:39:40+00:00
Yes, still the same for me. And I've already tried everything I thought to change. Someone who should understand it more than me should comment. Thank you very much.

# Action History
- Created by: GehogHeg | 2019-12-01T18:57:55+00:00
- Closed at: 2021-04-12T15:13:04+00:00
