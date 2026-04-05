---
title: OpenCL failing with RX 460 on XMRig - CL_BUILD_PROGRAM_FAILURE
source_url: https://github.com/xmrig/xmrig/issues/3602
author: Rieidi
assignees: []
labels: []
created_at: '2024-12-17T20:16:07+00:00'
updated_at: '2024-12-18T10:23:19+00:00'
type: issue
status: closed
closed_at: '2024-12-18T10:23:19+00:00'
---

# Original Description
`
I am experiencing an issue when trying to mine with my AMD RX 460 4 GB using OpenCL on XMRig. I get the following errors:
```
error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram  
thread #1 failed with error CL_INVALID_PROGRAM 
``` 
What I have tried so far:
1. Updated AMD Drivers: I am using the latest drivers available from the official AMD website.
2. Operating Systems: I have tested on both Windows 10 and Windows 11.
3. AMD APP SDK 3.0: I have installed the SDK to ensure OpenCL libraries are available.
Note:
I did not use the "Factory Reset" option when installing the AMD drivers, so there may be leftovers from previous GPU driver installations.

What else can I try to resolve the CL_BUILD_PROGRAM_FAILURE error and get the RX 460 working properly on XMRig? Are there any specific configurations for older GPUs or driver-related adjustments I should consider?

logs:
```
C:\Users\RieidiGamer\Desktop\xmrig-6.22.2>xmrig.exe -o pool.hashvault.pro:80 -u  myWallet -p x -t 4 --opencl --no-cpu
 * ABOUT        XMRig/6.22.2 MSVC/2019 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Phenom(tm) II X4 965 Processor (1) 64-bit -AES
                L2:2.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       3.6/8.0 GB (45%)
                DIMM0: <empty>
                DIMM1: <empty>
                DIMM2: 4 GB DDR @ 1600 MHz ModulePartNumber02
                DIMM3: 4 GB DDR @ 1600 MHz ModulePartNumber03
 * MOTHERBOARD  ASUSTeK Computer INC. - M4A78T-E
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      pool.hashvault.pro:80 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3584.0)
 * OPENCL GPU   #0 01:00.0 Radeon(TM) RX 460 Graphics (Baffin) 1212 MHz cu:14 mem:3840/4096 MB
 * CUDA         disabled
[2024-12-17 20:08:35.128]  net      use pool pool.hashvault.pro:80  142.202.242.43
[2024-12-17 20:08:35.129]  net      new job from pool.hashvault.pro:80 diff 36000 algo rx/0 height 3305149 (11 tx)
[2024-12-17 20:08:35.130]  cpu      use argon2 implementation SSE2
[2024-12-17 20:08:36.336]  randomx  init dataset algo rx/0 (4 threads) seed 415b9636e8b263a9...
[2024-12-17 20:08:36.337]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (1 ms)
[2024-12-17 20:08:36.373]  net      new job from pool.hashvault.pro:80 diff 36000 algo rx/0 height 3305149 (20 tx)
[2024-12-17 20:08:47.148]  net      new job from pool.hashvault.pro:80 diff 36000 algo rx/0 height 3305150 (21 tx)
[2024-12-17 20:08:49.767]  randomx  dataset ready (13429 ms)
[2024-12-17 20:08:49.767]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       192 |     8 |    384 | Radeon(TM) RX 460 Graphics (Baffin)
|  1 |   0 | 01:00.0 |       192 |     8 |    384 | Radeon(TM) RX 460 Graphics (Baffin)
[2024-12-17 20:08:51.188]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2024-12-17 20:08:51.192]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2024-12-17 20:08:51.215]  opencl   thread #0 self-test failed
[2024-12-17 20:08:51.296]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2024-12-17 20:08:51.297]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2024-12-17 20:08:51.309]  opencl   thread #1 self-test failed
[2024-12-17 20:08:51.310]  opencl   disabled (failed to start threads)
[2024-12-17 20:08:57.520]  signal   Ctrl+C received, exiting
[2024-12-17 20:08:57.544]  opencl   stopped (24 ms)

C:\Users\RieidiGamer\Desktop\xmrig-6.22.2>
```

# Discussion History
## SChernykh | 2024-12-18T08:05:32+00:00
- You shouldn't try to mine RandomX on GPU, it's too inefficient. You'll get better results mining other algorithms (Kawpow for example)
- You will need AMD drivers from the beginning of 2020 if you really want to compile RandomX code for AMD

## Rieidi | 2024-12-18T10:23:19+00:00
It worked, thanks.

# Action History
- Created by: Rieidi | 2024-12-17T20:16:07+00:00
- Closed at: 2024-12-18T10:23:19+00:00
