---
title: Having issues w/ Rejected benchmarks
source_url: https://github.com/xmrig/xmrig/issues/2280
author: gbolcer
assignees: []
labels:
- bug
created_at: '2021-04-18T18:24:17+00:00'
updated_at: '2021-12-19T15:42:21+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:42:21+00:00'
---

# Original Description
Any advice where to start looking appreciated. 

Cuda 11.1 (Can use 11.0, 11.1, 11.2)
Win10 Pro 20H2 19042.928
xmrig-cuda-6.5.0-cuda11_1-win64

nvcc --version                                                                                                                              
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2020 NVIDIA Corporation
Built on Mon_Oct_12_20:54:10_Pacific_Daylight_Time_2020
Cuda compilation tools, release 11.1, V11.1.105
Build cuda_11.1.relgpu_drvr455TC455_06.29190527_0

.\xmrig.exe --version                                                                                                                       
XMRig 6.11.2
 built on Apr 11 2021 with GCC 10.1.0
 features: 64-bit AES

libuv/1.41.0
OpenSSL/1.1.1j
hwloc/2.4.1

https://xmrig.com/benchmark/3S5qfS



# Discussion History
## SChernykh | 2021-04-18T18:30:51+00:00
This is probably a sign of instability. Try to run offline benchmark and see if you get green or red hash in the end.

## gbolcer | 2021-04-18T19:08:14+00:00
Feeling like a cuda problem.  --cuda red, w/o green. 

https://gofile.io/d/QF2oJB

Cuda version above.  Nvidia Driver,  466.11, 4/14/2021


## gbolcer | 2021-04-19T23:46:55+00:00
Rebuilt xmrig-cuda 6.5.0 from scratch using latest CUDA 11.3
Still NO love.  (red hashcode) Also tried going backwards with other combinations too, Cuda 11.0 and 6.4.1. No luck either.  

Open to other suggestions.  


PS W:\projects\xmrig\xmrig-6.11.2> .\benchmark_1M.cmd
 * ABOUT        XMRig/6.11.2 gcc/10.1.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 3950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       15.9/127.9 GB (12%)
                DIMM_A1: 32 GB DDR4 @ 2666 MHz F4-3200C16-32GTRS
                DIMM_A2: 32 GB DDR4 @ 2666 MHz F4-3200C16-32GTRS
                DIMM_B1: 32 GB DDR4 @ 2666 MHz F4-3200C16-32GTRS
                DIMM_B2: 32 GB DDR4 @ 2666 MHz F4-3200C16-32GTRS
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - ROG CROSSHAIR VIII HERO
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         11.3/11.3/6.5.0
 * NVML         11.466.11/466.11 press e for health report
 * CUDA GPU     #0 0a:00.0 NVIDIA GeForce RTX 3090 1800/9751 MHz smx:82 arch:86 mem:23328/24576 MB
[2021-04-19 16:41:21.119]  bench    start benchmark hashes 1M algo rx/0
[2021-04-19 16:41:21.120]  cpu      use argon2 implementation AVX2
[2021-04-19 16:41:21.667]  msr      register values for "ryzen_17h" preset have been set successfully (547 ms)
[2021-04-19 16:41:21.668]  randomx  init dataset algo rx/0 (32 threads) seed 0000000000000000...
[2021-04-19 16:41:21.670]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2021-04-19 16:41:23.123]  randomx  dataset ready (1452 ms)
[2021-04-19 16:41:23.123]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2021-04-19 16:41:23.127]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 0a:00.0 |      5248 |      32 |    164 |  6 |  25 |  10496 | NVIDIA GeForce RTX 3090
[2021-04-19 16:41:23.150]  cpu      READY threads 32/32 (32) huge pages 100% 32/32 memory 65536 KB (25 ms)
[2021-04-19 16:41:23.541]  nvidia   READY threads 1/1 (414 ms)
[2021-04-19 16:42:23.063]  bench    benchmark finished in 59.937 seconds (16684.2 h/s) hash sum = 5721BF496B4C2AFA
[2021-04-19 16:42:23.064]  bench    press Ctrl+C to exit
[2021-04-19 16:42:23.494]  cpu      stopped (1 ms)
[2021-04-19 16:42:25.680]  nvidia   stopped (2186 ms)
[2021-04-19 16:42:25.682]  nvidia   #0 0a:00.0 289W 66C 1920/9501 MHz fan0:60% fan1:60%
[2021-04-19 16:42:37.270]  signal   Ctrl+C received, exiting
Press any key to continue . . .
Terminate batch job (Y/N)?
^C
PS W:\projects\xmrig\xmrig-6.11.2>

## gbolcer | 2021-04-20T00:16:14+00:00
I'm starting to wonder if the card is mining-crippled.  

## SChernykh | 2021-04-20T06:21:10+00:00
Wait, are you trying to run benchmark? This is only for CPU.

## Spudz76 | 2021-04-20T10:53:20+00:00
Benchmarks where GPUs are enabled will always be rejected, as benchmarking is only available for CPUs

## gbolcer | 2021-04-20T14:53:13+00:00
In my benchmark_1m file. 
xmrig.exe --algo=cryptonight-heavy --donate-level=0 --print-time=5 --bench=1M --cuda 

So @SChernykh  yes to GPU.   

@Spudz76 I just need to confirm the GPU hash sum is correct.  I don't necessarily need to submit the benchmark. 

## Spudz76 | 2021-04-21T08:56:50+00:00
Well it's ignoring your algo and doing an rx/0 benchmark, mostly because benchmark mode only tests rx/0 or rx/wow

## gbolcer | 2021-04-21T14:28:15+00:00
Well I was trying different combinations as the original of just removing --submit and adding --cuda always comes back with a red checksum.  

xmrig.exe --bench=1m  --> returns green hash sum
xmrig.exe --bench=1m --cuda --> returns red hash sum

I've tried all combinations of xmrig 6.11.2, 6.10.0, xmrig-cuda 6.5.0, 6.4.2-dev, 6.4.1 both binaries and compiling from scratch, different CUDA versions 11.0, 11.0.2, 11.1, 11.1.1, 11.3 and various command line flags just to test if it was some configuration issue.   

I can't get any --cuda hash sum to come back as green. That's the issue I'm trying to figure out. 

See side by side: 
https://gofile.io/d/FjEPOk

## SChernykh | 2021-04-21T14:33:54+00:00
Benchmark was not designed to run with GPU enabled, this is a bug in a sense that it should ignore any GPU settings.

## gbolcer | 2021-04-21T14:44:33+00:00
@SChernykh  Thank you.  I get it now.  

What's the best way to confirm that the GPU is working correctly? 

## SChernykh | 2021-04-21T15:04:56+00:00
Best way is probably to start mining and see if you get all green "accepted" in the log.

## gbolcer | 2021-04-21T15:28:08+00:00
I'll close this issue out, so thank you for the help.  One last question though, even with the log colors:true, the log file seems to not generating colors.  Suggestions?  

# Action History
- Created by: gbolcer | 2021-04-18T18:24:17+00:00
- Closed at: 2021-12-19T15:42:21+00:00
