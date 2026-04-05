---
title: CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST on Android with Termux
source_url: https://github.com/xmrig/xmrig/issues/2403
author: thosoo
assignees: []
labels: []
created_at: '2021-05-22T20:40:33+00:00'
updated_at: '2022-01-15T05:40:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**

I was able to start xmrig with openCL detected on my Huawei P40pro in Termux, which has Android 10 as OS. However, it is not usable, as the error in the title appears.
This may have something to do with the [ocl 1.2 apis](https://github.com/xmrig/xmrig/blob/d82e100e303f6e860506132d009de5d4328c420a/src/backend/opencl/opencl.cmake#L9). 

**To Reproduce**
- Compile xmrig in Termux on Android.
- Try to run with opencl

This error is reproducible with my old Huawei P10.

**Expected behavior**
Should work.

**Required data**
 - Miner log as text or screenshot
```
~/xmrig $ ./mine2.sh
 * ABOUT        XMRig/6.12.1 clang/12.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A55 (1) 64-bit AES
                threads:8
 * MEMORY       6.4/7.2 GB (89%)
 * DONATE       1%
 * POOL #1      mine.uplexapool.com:1111 algo cn/upx2
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 ARM Platform/OpenCL 2.0 v1.r18p0-01rel0.91256554b836fb72cce9d96d095364da
 * OPENCL GPU   #0 n/a Mali-G76 5 MHz cu:16 mem:1024/4096 MB
 * CUDA         disabled
[2021-05-22 22:30:16.485]  net      use pool mine.uplexapool.com:1111  194.163.131.219
[2021-05-22 22:30:16.485]  net      new job from mine.uplexapool.com:1111 diff 50000 algo cn/upx2 height 0
[2021-05-22 22:30:16.485]  cpu      use profile  cn/upx2  (8 threads) scratchpad 128 KB
[2021-05-22 22:30:16.489]  opencl   use profile  cn/upx2  (1 thread) scratchpad 128 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |      1920 |     8 |    240 | Mali-G76
[2021-05-22 22:30:16.491]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 1024 KB (6 ms)
[2021-05-22 22:30:21.255]  cpu      accepted (1/0) diff 50000 (43 ms)
[2021-05-22 22:30:24.979]  cpu      accepted (2/0) diff 50000 (21 ms)
[2021-05-22 22:30:29.550]  cpu      accepted (3/0) diff 50000 (28 ms)
[2021-05-22 22:30:30.577]  cpu      accepted (4/0) diff 50000 (24 ms)
[2021-05-22 22:30:31.588]  cpu      accepted (5/0) diff 50000 (31 ms)
[2021-05-22 22:30:34.779]  net      new job from mine.uplexapool.com:1111 diff 150000 algo cn/upx2 height 0
[2021-05-22 22:30:39.145]  opencl   READY threads 1/1 (22656 ms)
[2021-05-22 22:30:40.252]  cpu      accepted (6/0) diff 150000 (26 ms)
[2021-05-22 22:30:47.167]  opencl   error CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST when calling clEnqueueReadBuffer
[2021-05-22 22:30:47.167]  opencl   thread #0 failed with error CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST
[2021-05-22 22:30:56.778]  cpu      accepted (7/0) diff 150000 (29 ms)
[2021-05-22 22:31:04.678]  net      new job from mine.uplexapool.com:1111 diff 360014 algo cn/upx2 height 0
[2021-05-22 22:31:13.703]  cpu      accepted (8/0) diff 360014 (34 ms)
[2021-05-22 22:31:15.856]  cpu      accepted (9/0) diff 360014 (32 ms)
[2021-05-22 22:31:16.523]  miner    speed 10s/60s/15m 9455.2 n/a n/a H/s max 9897.4 H/s
[2021-05-22 22:31:34.684]  net      new job from mine.uplexapool.com:1111 diff 1080K algo cn/upx2 height 0
[2021-05-22 22:32:04.687]  net      new job from mine.uplexapool.com:1111 diff 661272 algo cn/upx2 height 0
[2021-05-22 22:32:16.565]  miner    speed 10s/60s/15m 9680.0 9742.8 n/a H/s max 9897.4 H/s
[2021-05-22 22:32:47.656]  net      new job from mine.uplexapool.com:1111 diff 661272 algo cn/upx2 height 0
[2021-05-22 22:33:04.694]  net      new job from mine.uplexapool.com:1111 diff 330636 algo cn/upx2 height 0
[2021-05-22 22:33:12.830]  cpu      accepted (10/0) diff 330636 (22 ms)
[2021-05-22 22:33:13.006]  cpu      accepted (11/0) diff 330636 (24 ms)
[2021-05-22 22:33:16.600]  miner    speed 10s/60s/15m 9701.2 9751.7 n/a H/s max 9897.4 H/s
[2021-05-22 22:33:34.698]  net      new job from
```
 - command line:
 - 
```
#!/bin/sh
 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/system/vendor/lib64/
./build/xmrig --opencl --opencl-platform=ARM --opencl-loader=libOpenCL.so -u -o mine.uplexapool.com:1111 -a cn/upx2
```
 - OS: Android 10
 - For GPU related issues: Huawei P40 Pro - Mali-G76

**Additional context**
Add any other context about the problem here.

```
[2021-05-22 22:30:47.167]  opencl   error CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST when calling clEnqueueReadBuffer
[2021-05-22 22:30:47.167]  opencl   thread #0 failed with error CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST
```


# Discussion History
## ghost | 2021-05-22T23:06:47+00:00
Not supporting Mali gpu yet

## HimDek | 2021-05-23T02:51:42+00:00
This is not an answer but can you please share the compiled xmrig for arm64.

## thosoo | 2021-05-23T14:18:44+00:00
> This is not an answer but can you please share the compiled xmrig for arm64.

Compiling it on arm64 linux for yourself is not that hard and ensures that dependencies are met.. 

## Saikatsaha1996 | 2022-01-15T05:40:50+00:00
> 

Just reduce intensity 
![Screenshot_2022-01-15-09-01-56-036_com termux](https://user-images.githubusercontent.com/72664192/149610515-0f38a286-050d-4b05-8c28-963fe7cd2cbd.jpg)


# Action History
- Created by: thosoo | 2021-05-22T20:40:33+00:00
