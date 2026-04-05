---
title: Segmentation fault in android help me
source_url: https://github.com/xmrig/xmrig/issues/1984
author: Saikatsaha1996
assignees: []
labels: []
created_at: '2020-12-17T15:40:55+00:00'
updated_at: '2022-06-12T08:06:33+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:28:12+00:00'
---

# Original Description
**Describe the bug**
Segmentation fault i don't know what is problem

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - 
![Screenshot_20201217-210110](https://user-images.githubusercontent.com/72664192/102509247-546e4f00-40ac-11eb-9618-e5250736b879.png)

 - ./xmrig -a cryptonight/r -o stratum+tcp://cryptonightr.eu.nicehash.com:3375 -u MY-WALL-ADDRESS -p x --opencl-devices 0 --opencl-loader libOpenCL.so --opencl-platform QUALCOMM Snapdragon

 - OS: Android 10
 - For GPU related issues: information about GPUs and driver version.
 - OpenCL 2.0 Qualcomm Adreno TM

**Additional context**
Add any other context about the problem here.


# Discussion History
## xmrig | 2020-12-21T09:24:48+00:00
Using OpenCL on platforms other than AMD is an unsupported configuration and the result is undefined. Also `cn/r` algorithm requires runtime OpenCL code generation and it is an additional point of failure.
Thank you.

## Spudz76 | 2020-12-22T05:28:34+00:00
Likely not enough memory free for compilation to complete without OOM, which fires segmentation fault (can't allocate more segments).  If using caching it should work after it compiles once, try shutting down all other processes (including cpu part of miner) to get max free memory so that initial compilation completes and writes a .cache file.  Then it should load the binary kernel which doesn't need compilation space in system memory.

## Saikatsaha1996 | 2022-01-14T19:49:13+00:00
> Likely not enough memory free for compilation to complete without OOM, which fires segmentation fault (can't allocate more segments). If using caching it should work after it compiles once, try shutting down all other processes (including cpu part of miner) to get max free memory so that initial compilation completes and writes a .cache file. Then it should load the binary kernel which doesn't need compilation space in system memory.

So today proved Mali GPU can mine with xmrig
![IMG_20220115_011426](https://user-images.githubusercontent.com/72664192/149576188-466e8778-7235-4bf4-a291-ed8e7db5dae4.jpg)



## ChaoLine892 | 2022-06-12T04:16:57+00:00
Hello I want to ask a question why the segmentation fault error occurred
Log
~/.../xmrig/build $ ./xmrig -a cn-extremelite/upx2 -o uplexa.herominers.com:10470 -u UPX1kR57JKDEC7mX7VJJnbh79ChR3yr5acaxnkWiUGCHiVdpzDKtYMUhCLHKvAzP5FY8DGaPnamAbBL5tTci9HhY99J4vCGwdo --donate-level 1 -p x --opencl-devices 0 --opencl-loader libOpenCL.so --opencl-platform QUALCOMM --no-cpu
 * ABOUT        XMRig/6.12.1-mo3 clang/14.0.4
 * LIBS         libuv/1.44.1 OpenSSL/3.0.3
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (1) 64-bit AES
                threads:8
 * MEMORY       4.0/7.3 GB (55%)
 * DONATE       1%
 * POOL #1      uplexa.herominers.com:10470 algo cn/upx2
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 QUALCOMM Snapdragon(TM)/OpenCL 2.0 QUALCOMM build: commit #42297a4 changeid #I9e9b240040 Date: 03/19/21 Fri Local Branch:  Remote Branch: refs/tags/AU_LINUX_ANDROID_LA.UM.9.1.R1.11.00.00.604.070
 * OPENCL GPU   #0 n/a QUALCOMM Adreno(TM) 1 MHz cu:2 mem:937/3749 MB
 * CUDA         disabled
[2022-06-12 07:10:18.944]  benchmk   STARTING ALGO PERFORMANCE CALIBRATION (with 10 seconds round)
[2022-06-12 07:10:18.945]  benchmk   Algo cn/r Preparation
[2022-06-12 07:10:18.950]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       400 |     8 |    800 | QUALCOMM Adreno(TM)
[2022-06-12 07:10:19.045]  opencl   GPU #0 compiling...
Segmentation fault
Gpu - Adreno 640
Os - Android 11
Opencl 2.0
Thank you in advance.

## SChernykh | 2022-06-12T08:06:33+00:00
It crashed probably because you tried to use GPU on ARM which has never been tested and is not supported. Also, this is not the official release, but a MoneroOcean version, you should ask them.

# Action History
- Created by: Saikatsaha1996 | 2020-12-17T15:40:55+00:00
- Closed at: 2021-04-12T14:28:12+00:00
