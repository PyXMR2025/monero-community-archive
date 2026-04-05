---
title: Poor mining performence 3990x
source_url: https://github.com/xmrig/xmrig/issues/2701
author: titus-anromedonn
assignees: []
labels: []
created_at: '2021-11-16T20:42:33+00:00'
updated_at: '2021-12-09T13:20:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Running the application in linux I'm getting really poor performance with the 3990x. Any ideas why I'm getting half the reported hash rate as others on the benchmark site?


**specs**

Linux
Ubuntu Server 18.04 LTS
Kernel 4.15
RAM 3200MHz
CPU Ryzen Threadripper 3990X

**To Reproduce**
```bash
xmrig --bench 1M --randomx-1gb-pages
```

**Expected behavior**
Upwards of 50K hash rate.

See below for output after running the command. 

```bash
 * ABOUT        XMRig/6.9.0 gcc/7.5.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen Threadripper 3990X 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:1
 * MEMORY       38.2/62.8 GB (61%)
                DIMM 0: <empty>
                DIMM_A1: 16 GB DDR4 @ 3000 MHz CMK32GX4M2E3200C16
                DIMM 0: <empty>
                DIMM_B1: 16 GB DDR4 @ 3000 MHz CMK32GX4M2E3200C16
                DIMM 0: <empty>
                DIMM_C1: 16 GB DDR4 @ 3000 MHz CMK32GX4M2E3200C16
                DIMM 0: <empty>
                DIMM_D1: 16 GB DDR4 @ 3000 MHz CMK32GX4M2E3200C16
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - PRIME TRX40-PRO
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-16 20:38:40.344]  bench    start benchmark hashes 1M algo rx/0
[2021-11-16 20:38:40.344]  cpu      use argon2 implementation AVX2
[2021-11-16 20:38:40.351]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2021-11-16 20:38:40.351]  randomx  init dataset algo rx/0 (128 threads) seed 0000000000000000...
[2021-11-16 20:38:40.704]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (353 ms)
[2021-11-16 20:38:41.683]  randomx  dataset ready (979 ms)
[2021-11-16 20:38:41.683]  cpu      use profile  rx  (128 threads) scratchpad 2048 KB
[2021-11-16 20:38:41.914]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (231 ms)
[2021-11-16 20:39:13.642]  bench    benchmark finished in 31.894 seconds (31353.9 h/s) hash sum = 898B6E0431C28A6B
[2021-11-16 20:39:13.642]  bench    press Ctrl+C to exit
[2021-11-16 20:39:13.732]  cpu      stopped (3 ms)
```

# Discussion History
## Spudz76 | 2021-11-17T00:03:41+00:00
Note the higher than ~40KH scores all have 8 sticks thus 8-channel memory bus.

You have four.

Also 3000 is not great 3200 or better will achieve closer to the top benchmarks (speeds are also shown in the memory tab of benchmarks).

## titus-anromedonn | 2021-11-17T00:16:27+00:00
> Note the higher than ~40KH scores all have 8 sticks thus 8-channel memory bus.
> 
> 
> 
> You have four.
> 
> 
> 
> Also 3000 is not great 3200 or better will achieve closer to the top benchmarks (speeds are also shown in the memory tab of benchmarks).


Please correct me if I'm wrong, but the 3990x is quad channel. 

Having 8 sticks of ram is irrelevant since max throughout you would get is with 4 sticks for each channel. Only the EPYC have 8+ channels as far as I know

Here is an example from the benchmark with 4 sticks and pulling > 50+K 

https://xmrig.com/benchmark/5xgpts

In regards to the memory clock speeds, I was playing around with different clock speeds to see if they made a difference, the ram is rated for 3200MHz and I ran it at those speeds unsuccessfully

## Spudz76 | 2021-11-17T00:21:19+00:00
Yep my brain inserted EPYC when it saw TR

Only other possible issue is you're running an old xmrig.  There were some updates to Zen core tweaks since then.  That result you linked has the newer code.

## titus-anromedonn | 2021-11-17T00:25:38+00:00
> Yep my brain inserted EPYC when it saw TR
> 
> 
> 
> Only other possible issue is you're running an old xmrig.  There were some updates to Zen core tweaks since then.  That result you linked has the newer code.

I downloaded the latest one and tried it as well, no difference in hash rate. 

I'm running Ubuntu Server 18.04LTS with a 4.15 kernel. Do you think it could be something related to that by any chance? I have tried everything I can think of with no luck. 

I know the newer kernels have better support for Zen3 but I can't imagine there's something that would give me a 20KH+ bump. 

## Spudz76 | 2021-11-17T00:30:28+00:00
Maybe, I don't have any Zen things, but everything else I run works similarly 18 vs 20

You could try one thing before a full dist-up, and enable the backports and install a newer kernel built for 18.04 and see if that alone helps.  Shouldn't be anything else different in userspace that I know of, most likely kernel.  Too bad the benchmarks don't show kernel release string...

## Spudz76 | 2021-11-17T00:33:28+00:00
That RAM should do 3200 with CL16-20-20-38 at 1.35V

Equivalent timings at 3000 would be CL15-19-19-36 approximately

## titus-anromedonn | 2021-11-17T00:47:35+00:00
> That RAM should do 3200 with CL16-20-20-38 at 1.35V
> 
> 
> 
> Equivalent timings at 3000 would be CL15-19-19-36 approximately

Thanks for the suggestion, I'm going to give those specific ram timings a try and get back to you. 

Otherwise I'm pretty much ready to give up haha. 

## titus-anromedonn | 2021-11-17T03:03:04+00:00
> That RAM should do 3200 with CL16-20-20-38 at 1.35V
> 
> Equivalent timings at 3000 would be CL15-19-19-36 approximately

Yea I can't even boot with those timings, it posts in safe mode. I'm going to try on Windows and then a newer Ubuntu Server version. If that doesn't work I guess I have a poor mans 3990x :'( 

## Spudz76 | 2021-11-17T04:13:02+00:00
Seems weird that's generally good RAM I think.  Usually does better than advertised especially with a touch of overvolt.

## titus-anromedonn | 2021-11-18T16:14:39+00:00
> Seems weird that's generally good RAM I think. Usually does better than advertised especially with a touch of overvolt.

Turns out it was just some bad ram. I haven't figured out which stick it was exactly but after popping in some other ram I had, that was advertised for 3200MHz, I was getting around 50Kh/s. 

Not the fastest ram but definitely in the ball park that I was expecting. Thanks for your help, I think you can close this issue!

## Spudz76 | 2021-11-19T14:02:11+00:00
Weirdness located! :)

## xq0404 | 2021-12-01T08:25:20+00:00
> > Seems weird that's generally good RAM I think. Usually does better than advertised especially with a touch of overvolt.
> 
> Turns out it was just some bad ram. I haven't figured out which stick it was exactly but after popping in some other ram I had, that was advertised for 3200MHz, I was getting around 50Kh/s.
> 
> Not the fastest ram but definitely in the ball park that I was expecting. Thanks for your help, I think you can close this issue!

I got around 33Kh/s under Windows 10.  What good ram do you have now? Mine is Kingston  32GB(8G×4) DDR4 3200 Predator, it's genuine 3200HHz at default, no overclocing(XMP) is necessary.

## xq0404 | 2021-12-09T13:20:17+00:00
After upgrading my cooler to  NH-U14S TR4-SP3 and TEAM T-Create Classic DDR4 10L DDR4-3200 2*64GB Memory Kit, I was getting about 47Kh/s. 

# Action History
- Created by: titus-anromedonn | 2021-11-16T20:42:33+00:00
