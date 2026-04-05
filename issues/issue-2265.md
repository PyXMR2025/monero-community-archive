---
title: ' opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram'
source_url: https://github.com/xmrig/xmrig/issues/2265
author: serambca
assignees: []
labels: []
created_at: '2021-04-14T10:16:32+00:00'
updated_at: '2022-06-25T21:54:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

I'm trying minning RVN from 2miners.com or flypool.org from macOS Big Sur with chip Intel (1 macBook Pro i9 and iMac i7)
The macbook pro have Radeon Pro vega 16 and the iMac have Radeon R9 M290X (both AMD)

I tried to open xmrig but in both computers don't work. Could you please help me?
At last, I tried to compile manually in each computer but the result is the same.

<img width="758" alt="Captura de pantalla 2021-04-14 a las 12 15 10" src="https://user-images.githubusercontent.com/25333845/114694700-1d870d80-9d1b-11eb-872e-5f311ac46c1d.png">

Thanks you!!

# Discussion History
## janek33 | 2021-05-09T07:15:49+00:00
Same here. 
HW: MacBook Pro with AMD Radeon Pro 460
OS: Big sur
SW: XMRig/6.12.1 clang/12.0.0

## ganzocrypt | 2021-05-18T16:15:57+00:00
same here on Catalina with dual Xeon and a AMD RX 580 8Gb. Card is recognized.
As soon as I run the xmrig I get the following error:
`./xmrig
[2021-05-18 18:04:04.209] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037`

Here the error at runtime:
`[2021-05-18 18:06:19.980]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Error returned by cvms_element_build_from_source
[2021-05-18 18:06:19.981]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2021-05-18 18:06:19.981]  opencl   GPU #0 compiling...
[2021-05-18 18:06:19.982]  opencl   thread #1 self-test failed
[2021-05-18 18:06:19.983]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Error returned by cvms_element_build_from_source
[2021-05-18 18:06:19.983]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-05-18 18:06:19.984]  opencl   thread #0 self-test failed
[2021-05-18 18:06:19.984]  opencl   disabled (failed to start threads)
`
the cpu mining works fine

## ganzocrypt | 2021-05-26T10:00:51+00:00
I created a branch for the macos fork.

All work credit for adding AMD support goes to @Spudz76.

Please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) and if there are any issues for the xmrig binary post them on the [issue](https://github.com/ganzocrypt/xmrig-macos/issues) section.

## janek33 | 2021-05-26T15:58:22+00:00
Sorry, don’t know how to report properly yet, 
but it’s failing on my Radeon Pro 460 with:


|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   6291456 |   256 |   2957 | Intel(R) HD Graphics 530
|  1 |   1 |     n/a |   4194304 |   256 |   2957 | AMD Radeon Pro 460 Compute Engine
[2021-05-26 23:45:47.353]  opencl   GPU #1 compiling...
[2021-05-26 23:45:47.944]  opencl   GPU #1 compilation completed (590 ms)
[2021-05-26 23:45:47.944]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-05-26 23:45:47.944]  opencl   GPU #0 compiling...
[2021-05-26 23:45:48.750]  opencl   GPU #0 compilation completed (805 ms)
[2021-05-26 23:45:48.750]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-05-26 23:45:48.750]  opencl   READY threads 2/2 (1400 ms)
[2021-05-26 23:45:49.236]  opencl   KawPow program for period 590320 compiled (486ms)
[2021-05-26 23:45:49.704]  opencl   KawPow program for period 590321 compiled (467ms)
[2021-05-26 23:45:50.120]  opencl   KawPow program for period 590320 compiled (416ms)
[2021-05-26 23:45:50.495]  opencl   KawPow program for period 590321 compiled (375ms)
[2021-05-26 23:45:54.878]  miner    KawPow light cache for epoch 236 calculated (5641ms)
[2021-05-26 23:45:54.896]  opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel ethash_calculate_dag_item



> On 26. 5. 2021, at 18:01, ganzocrypt ***@***.***> wrote:
> 
> 
> I created a branch for the macos fork.
> 
> All work credit for adding AMD support goes to @Spudz76 <https://github.com/Spudz76>.
> 
> Please test the release <https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos> and if there are any issues for the xmrig binary post them on the issue section.
> 
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2265#issuecomment-848639592>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AA737HSEJPXKXPXJKLTNUELTPTBGRANCNFSM425CTLSQ>.
> 



## ganzocrypt | 2021-05-26T16:06:31+00:00
@janek33 first you will not be able to mine on the Intel GPU
the Radeon Pro 460 how much memory does it have? if it's less than 4 you cannot mine ETH.
You best bet would be KawPow algo. So remove the Intel GPU from your OpenCL section by selecting only the AMD GPU which in on index 1. Set it in the OpenCL section of the config.

## Spudz76 | 2021-05-26T19:33:05+00:00
They are using KawPow already -- KawPow is Ethash, but smaller -- therefore the Ethash reference in the kawpow kernel.

But agree the Intel is the one messing things up (unfortunately the OpenCL error does not say which GPU had the failure but it is more likely the Intel).


## bossbratox | 2022-01-12T19:55:56+00:00
hello, I'm running into this same error, not sure what to do for it

11th gen intel 11900K + AMD Radeon RX 580 Series (Ellesmere) 1100 MHz

[2022-01-12 14:53:22.877]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (141 ms)
[2022-01-12 14:53:41.539]  randomx  dataset ready (18662 ms)
[2022-01-12 14:53:41.539]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2022-01-12 14:53:41.545]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |   1152 | AMD Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       576 |     8 |   1152 | AMD Radeon RX 580 Series (Ellesmere)
[2022-01-12 14:53:41.633]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (94 ms)
[2022-01-12 14:53:43.454]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-01-12 14:53:43.462]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-01-12 14:53:43.469]  opencl   thread #0 self-test failed
[2022-01-12 14:53:43.493]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-01-12 14:53:43.495]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2022-01-12 14:53:43.500]  opencl   thread #1 self-test failed
[2022-01-12 14:53:43.500]  opencl   disabled (failed to start threads)

## CyberDudeJ | 2022-06-25T21:54:43+00:00
I get this on windows 10.

# Action History
- Created by: serambca | 2021-04-14T10:16:32+00:00
