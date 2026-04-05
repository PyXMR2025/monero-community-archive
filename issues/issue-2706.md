---
title: MAC M1 GPU Support
source_url: https://github.com/xmrig/xmrig/issues/2706
author: santoshbhor
assignees: []
labels: []
created_at: '2021-11-18T16:02:14+00:00'
updated_at: '2024-01-15T08:02:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi I wanted to check and see if GPU support from MAC M1 can be added and what would take to get this done.
I can possibly help but i am not MAC M1 expert but if some one can guide me i may be able to help to support this?

# Discussion History
## Spudz76 | 2021-11-19T14:06:57+00:00
Already works, OpenCL.

Not that fast since Apple OpenCL is terrible (for example identical AMD cards about 60% performance of AMD OpenCL on Linux).  Won't really work simultaneous with CPU mining since they share lots of the total chip bandwidth (memory bus mostly).

But it definitely should just work in recent versions by simply enabling OpenCL backend.

## cstrouse | 2021-11-23T05:04:39+00:00
I tried out GPU support just for fun on my 8/8 16GB MacBookAir10,1 running macOS 12.0.1 and it doesn't seem to work due to the OpenCL build failing.

Here is the relevant bit of the log:
```
[2021-11-22 21:54:28.255]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       128 |     8 |    256 | Apple M1
[2021-11-22 21:54:28.263]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[2021-11-22 21:54:28.666]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Compilation failed:

program_source:1788:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1399:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1811:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1399:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
[2021-11-22 21:54:28.667]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-11-22 21:54:28.668]  opencl   thread #0 self-test failed
[2021-11-22 21:54:28.668]  opencl   disabled (failed to start threads)
[2021-11-22 21:54:36.434]  signal   Ctrl+C received, exiting
[2021-11-22 21:54:36.437]  cpu      stopped (2 ms)
[2021-11-22 21:54:36.437]  opencl   stopped (0 ms)
```

I know M1 support is not likely a priority since there's not much benefit to be had and probably doesn't make much sense to use for this purpose but hope the log helps someone who is interested in improving support.

## Spudz76 | 2021-11-23T10:35:27+00:00
Well, it used to work.  Not sure what Apple changed.

## cstrouse | 2021-11-23T10:38:39+00:00
Sorry for the noise guys, it does start with some additional arguments it turns out. Try the following and see if you get it to build the OpenCL payload and start.

`./xmrig --coin=RVN --no-cpu --opencl --opencl-platform=0 -o stratum+tcp://stratum.ravenpool.ninja:3333 -u RVNWALLET.WORKERNAME -p x`

I'm able to get 1.76 MH/s using kawpow on 12.0.1 using a Radeon Pro WX 5100 8GB card and the M1 MacBookAir10,1 (8-core CPU, 8-core GPU, 16GB of memory) gets 1.41 MH/s using kawpow. I ran the miner for over an hour on both machines and neither ever submitted any shares to the pool so don't recommend it (on unmineable which I tried first; other pools do seem to work properly).

## Spudz76 | 2021-11-23T15:15:04+00:00
Yes, unmineable has a minimum diff that is too high for "slow" rigs.

I am not sure if RandomX ever worked, besides that it would perform worse than horrible.  Just noticed that other attempt was rx.

## geoffwade | 2021-11-30T03:32:06+00:00
> This worked great on my macbook Air M1.   Seeing about 1.38 MH/s.  Not a lot of info out there for M1 GPU mining and happy to see this worked.  Thank you!



> Sorry for the noise guys, it does start with some additional arguments it turns out. Try the following and see if you get it to build the OpenCL payload and start.
> 
> `./xmrig --coin=RVN --no-cpu --opencl --opencl-platform=0 -o stratum+tcp://stratum.ravenpool.ninja:3333 -u RVNWALLET.WORKERNAME -p x`
> 
> I'm able to get 1.76 MH/s using kawpow on 12.0.1 using a Radeon Pro WX 5100 8GB card and the M1 MacBookAir10,1 (8-core CPU, 8-core GPU, 16GB of memory) gets 1.41 MH/s using kawpow. I ran the miner for over an hour on both machines and neither ever submitted any shares to the pool so don't recommend it (on unmineable which I tried first; other pools do seem to work properly).



## acrogenesis | 2021-12-04T20:11:40+00:00
> Sorry for the noise guys, it does start with some additional arguments it turns out. Try the following and see if you get it to build the OpenCL payload and start.
> 
> `./xmrig --coin=RVN --no-cpu --opencl --opencl-platform=0 -o stratum+tcp://stratum.ravenpool.ninja:3333 -u RVNWALLET.WORKERNAME -p x`
> 
> I'm able to get 1.76 MH/s using kawpow on 12.0.1 using a Radeon Pro WX 5100 8GB card and the M1 MacBookAir10,1 (8-core CPU, 8-core GPU, 16GB of memory) gets 1.41 MH/s using kawpow. I ran the miner for over an hour on both machines and neither ever submitted any shares to the pool so don't recommend it (on unmineable which I tried first; other pools do seem to work properly).

I'm getting 6.21 MH/s on the M1 max 16" 32GB. Although I do have a lot of windows and apps open

## Spudz76 | 2021-12-04T23:40:56+00:00
Pretty good considering the watts are low, and doing other stuff.

## RetroAndDev | 2024-01-12T11:43:43+00:00
Any help on that ? 
I active the OpenCL backend on M1 and I got this error : 
 * ABOUT        XMRig/6.21.0 clang/13.0.0 (built for macOS x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/3.0.7 hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          VirtualApple @ 2.50GHz (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.9/8.0 GB (99%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rx.unmineable.com:3333 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Nov 11 2023 23:48:03)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
 * CUDA         disabled
[2024-01-12 06:48:30.559]  net      use pool rx.unmineable.com:3333  161.35.34.195
[2024-01-12 06:48:30.560]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 162169
[2024-01-12 06:48:30.560]  cpu      use argon2 implementation SSSE3
[2024-01-12 06:48:30.560]  randomx  init dataset algo rx/0 (8 threads) seed 8d47b82e037755c8...
[2024-01-12 06:48:30.561]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2024-01-12 06:48:37.775]  randomx  dataset ready (7214 ms)
[2024-01-12 06:48:37.796]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       128 |     8 |    256 | Apple M1
[2024-01-12 06:48:37.798]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[2024-01-12 06:48:38.160]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
program_source:1786:1: warning: comparison of integers of different signs: '__private uint32_t' (aka '__private unsigned int') and 'int' [-Wsign-compare]
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1397:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1809:1: warning: comparison of integers of different signs: '__private int32_t' (aka '__private int') and 'unsigned int' [-Wsign-compare]
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1397:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
[2024-01-12 06:48:38.160]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2024-01-12 06:48:38.161]  opencl   thread #0 self-test failed
[2024-01-12 06:48:38.161]  opencl   disabled (failed to start threads)

Any idea ? I used the Intel x86_64 and ARM built and I got the same error.

## SChernykh | 2024-01-12T14:10:21+00:00
OpenCL on MacOS is not supported, and you shouldn't be mining RandomX with a GPU at all.

## RetroAndDev | 2024-01-12T16:42:32+00:00
Ah ! 
It's possible to mine on MacOS with M1 on other miners ? To make profitable my MacBook ?

## SChernykh | 2024-01-12T16:54:03+00:00
You can mine with XMRig on CPU, M1 CPU is supported.

## RetroAndDev | 2024-01-12T16:56:41+00:00
Yeah, but performances are low ? I have 2kH/s and with ETHMiner-M1 Fork is a 2MH/s. That good ?
(I can't use ETHMiner in my pool, don't know why)

## SChernykh | 2024-01-12T17:02:10+00:00
You can't compare hashrates of different algorithms. 2 Kh/s is normal hashrate for M1 on RandomX.

## RetroAndDev | 2024-01-12T17:03:14+00:00
Oh okay. But there is no ways to get the full power of the M1 (CPU+GPU) ?

## SChernykh | 2024-01-12T17:07:54+00:00
You can try to run XMRig on CPU and ETHMiner on GPU, but they will be interfering with each other because both use memory bandwidth for mining.

## RetroAndDev | 2024-01-12T17:09:25+00:00
ETHMiner don't let me mine with unMinable and ETC. Too had

## Spudz76 | 2024-01-14T02:17:01+00:00
Seems like [vk-ethminer](https://github.com/mshzhb/vk-ethminer) might work for ETC on M1 GPUs (using Vulkan instead of buggy/abandoned Apple OpenCL).

## RetroAndDev | 2024-01-14T04:30:59+00:00
Sure !
That's sounds good 👌 
I will try it. Sure that Vulkan is better than OpenCL on Macs

## RetroAndDev | 2024-01-14T09:49:59+00:00
> Seems like [vk-ethminer](https://github.com/mshzhb/vk-ethminer) might work for ETC on M1 GPUs (using Vulkan instead of buggy/abandoned Apple OpenCL).

Got error : 
Fatal : VkResult is -9 in /Users/mshzhb/workspace/vulkan-ethminer/src/miner/vulkanminer.cpp at line 321
ERROR:             vkEnumeratePhysicalDevices: Invalid instance [VUID-vkEnumeratePhysicalDevices-instance-parameter]
zsh: abort      ./vulkan_ethminer --server us1-etc.ethermine.org --port 4444 --wallet  --rig 

Someone know a fix ?
A Vulkan miner for low-power GPU is a great idea. Why there are no (good/big) miner(s) project(s) for passive mining ?

## Spudz76 | 2024-01-14T14:47:44+00:00
Might need to also install [MoltenVK](https://github.com/KhronosGroup/MoltenVK) layer so that Vulkan can get runtime translated to native Metal calls.  Maybe by default Apple has their own also-broken implementation of Vulkan.  They prefer that everything but Metal is broken I think, to increase adoption/conversion.

## RetroAndDev | 2024-01-14T15:15:52+00:00
Yeah but how ? I can't determine where is the issue cause of the source code is not available. 
I opened an issue on the project. Well see if I get answers

## ForbiddenEra | 2024-01-15T08:01:09+00:00
> Sorry for the noise guys, it does start with some additional arguments it turns out. Try the following and see if you get it to build the OpenCL payload and start.
> 
> `./xmrig --coin=RVN --no-cpu --opencl --opencl-platform=0 -o stratum+tcp://stratum.ravenpool.ninja:3333 -u RVNWALLET.WORKERNAME -p x`
> 
> I'm able to get 1.76 MH/s using kawpow on 12.0.1 using a Radeon Pro WX 5100 8GB card and the M1 MacBookAir10,1 (8-core CPU, 8-core GPU, 16GB of memory) gets 1.41 MH/s using kawpow. I ran the miner for over an hour on both machines and neither ever submitted any shares to the pool so don't recommend it (on unmineable which I tried first; other pools do seem to work properly).

Nice.. I couldn't get it working for KAWPOW with the settings I tried in the config.json but this worked. I tried 'MacMiner' which seemed to work but I was getting zero accepted shares on NH.

Doing both randomx[6kH/s] and KAWPOW[9mH/s] on M1 Ultra Mac Studio simultaneously; dual mining CPU+GPU doesn't seem to affect hashrate or either. For comparison though, I'm getting 25mH/s for KAWPOW on both my 3060+2070S. Also for comparison, I get about the same 6kH/s w/32 threads on my 4s*8c/16t (32c/64t) Xeon E4640 0 (albeit running virtualized)

# Action History
- Created by: santoshbhor | 2021-11-18T16:02:14+00:00
