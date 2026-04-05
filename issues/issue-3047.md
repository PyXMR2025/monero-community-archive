---
title: arm64 macos version , seems to integrate with built in opencl driver but not
  hardware
source_url: https://github.com/xmrig/xmrig/issues/3047
author: Amy-Ames
assignees: []
labels: []
created_at: '2022-05-10T16:26:44+00:00'
updated_at: '2025-06-28T10:37:07+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:37:07+00:00'
---

# Original Description
**Describe the bug**
arm64 macos version works fine as a cpu miner, but is partially recognized by opencl, why wouldnt you optimize xmrig to function in that manner? (it gets extremely hot with xmrig, but compiled ethminer can run 24/7 here and not afffect temperature at all)

**To Reproduce**
enable opencl

**Expected behavior**
I expected it to not work, I suppose, due to current support being for nvidia and amd rather than Metal
Is there any reason it can't be used?

<img width="846" alt="Screen Shot 2022-05-10 at 9 25 42" src="https://user-images.githubusercontent.com/101025179/167677090-f6eecbc0-2773-4bb8-8f73-468215bcaae0.png">


**Required data**

OSX ARM64 M1 , Big Sur 11.6.5

 * ABOUT        XMRig/6.17.0 clang/12.0.5
 * LIBS         libuv/1.43.0 OpenSSL/1.1.1m hwloc/2.7.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       5.5/8.0 GB (69%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10001 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Sep  5 2021 22:39:06)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
 * CUDA         disabled
[2022-05-10 09:19:23.887]  net      use pool gulf.moneroocean.stream:10001  149.28.115.221
[2022-05-10 09:19:23.888]  net      new job from gulf.moneroocean.stream:10001 diff 1000 algo rx/0 height 2620504 (12 tx)
[2022-05-10 09:19:23.888]  cpu      use argon2 implementation default
[2022-05-10 09:19:23.888]  randomx  init dataset algo rx/0 (8 threads) seed e3da49220880d859...
[2022-05-10 09:19:23.888]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2022-05-10 09:19:28.799]  randomx  dataset ready (4910 ms)
[2022-05-10 09:19:28.799]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2022-05-10 09:19:28.799]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
[2022-05-10 09:19:28.800]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       128 |     8 |    256 | Apple M1
[2022-05-10 09:19:28.801]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[2022-05-10 09:19:29.045]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
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
program_source:1815:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,get_byte(is_fp?registerReadCycleFP:registerReadCycle,dst)*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1399:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                              [2022-05-10 09:19:29.046]  opencl   thread #0 self-test failed
[2022-05-10 09:19:29.046]  opencl   disabled (failed to start threads)


**Additional context**
Add any other context about the problem here.


# Discussion History
## ghost | 2022-05-17T18:06:21+00:00
Metal is its own API and development ecosystem made by Apple for their custom silicon, similar to OpenGL/CL, Vulkan, etc - as you said yourself, it doesn't work because it's not supported and probably won't be any time soon.

## Spudz76 | 2022-05-17T22:30:15+00:00
It worked sometime, but maybe not RandomX.

## iamhumanipromise | 2022-05-20T07:33:13+00:00
Just to provide data for the devs re:this issue, it seems that KAWPOW works fine.... **However**: I did have to build using the "Ubuntu Instructions" of running the build_deps script, then doing cmake ... -DXMRIG with the path to the scripts folder. Didn't work when referencing brew-installed hwloc. 

<img width="1080" alt="Screen Shot 2022-05-20 at 12 30 08 AM" src="https://user-images.githubusercontent.com/105223045/169477131-8ed5e363-ad80-4b29-9417-5bc0c177fc81.png">





## Spudz76 | 2022-05-20T16:40:20+00:00
I always build with the bundled deps everywhere to avoid untested territory, so that may be why I never saw problems.

## Amy-Ames | 2022-05-20T23:59:28+00:00
Thanks for the additional information. I’m by-the-book using for development / compilation tools and various video drivers on Linux . It’s the Mac part where I went “well this isn’t expected “ and wasn’t sure how to proceed. I’m effectively cpu mining with an m1 compiled ethminer, that does not make the cpu or laptop get hot. At all.

whereas xmrig makes it get hot. I appreciate you even bothered to offer the binary. I just could not (and can’t) figure out why ethminer can do 2mh/s and stay cool while it burns up doing 2000h/s on xmrig, it is using the system ram to calculate a job, as though it were basically video ram , and does so very quickly. From there it’s comparable to a 12 year old i5 I have. Would anyone know the general direction I might want to look in, for rolling or solving this on my own?

## Spudz76 | 2022-05-21T02:09:29+00:00
Well different algorithms are... different.  And 2MH/s is kinda slow for ethash.  And RandomX (where I assume you are seeing the 2000H/s) is a lot more difficult and hits the memory really hard (as part of being anti-GPU and anti-ASIC).  It's pretty terrible on everything other than a Ryzen since they have the best integrated memory controller.  Except the Ryzens with iGPU then the memory controller is wasting time handling the GPU... similar to the M1.  DDR5 is also worse than DDR4 for purposes of low latency.

Also there is nothing special in the M1 support it's just generic ARM64 compilation, with polyfills that convert the x86_64 intrinsics (AVX2, AES-NI) into ARM64 versions (NEON, crypto-extensions, etc), which can't be an optimal way of making an M1 kernel.  But, Apple wants people to use Obj-C or Swift to get into any of their proprietary CPU (or GPU for that matter) features so it's probably almost as good as it can be for C++ code.  Unless of course someone that knows how to write a mining kernel and also knows ARM64 assembly tricks shows up, maybe they could find some optimizations and shortcuts.  Then again they could work on it and make it perfect and the memory controller could still be the bottleneck after all that effort.  Or the memory you can't change or tweak at all.

## Amy-Ames | 2022-05-21T17:14:12+00:00
thats actually a pretty fantastic answer , thank you for summarizing it.

call me an old dog, trying to learn new tricks on a new architecture that for now is just a black box to me. (ive had to cope with 8088 -> x86 -> ppc -> modern intel, to this for other reasons than "muh coins"). even if this is a non-issue for xmrig, thank you for this answer

## Amy-Ames | 2022-05-21T17:15:17+00:00
that ALSO answers why the ryzen boxes generate the most tangible coinage for me at the same time!!! 

## chendind | 2023-01-22T08:10:43+00:00
Same problem with me. Is there any resolution?

## Spudz76 | 2023-01-22T14:48:14+00:00
Apple could better support OpenCL (they won't), or you could run antiques like HighSierra with an nvidia card which was the last CUDA that worked (bypass OpenCL and Metal completely).  And still rx/0 will be slow because it's designed explicitly to be bad on GPUs (support exists only to prove that it's slow).  So rx/0 not working on Apple is not really a loss so nobody is going to expend much effort to fix it.  Other algorithms tend to work somewhat, at least until Apple drops OpenCL in an upcoming OS (another reason to not put much effort into it, Apple has said it will be killed off).  They have not updated it in a long time, it is abandoned and unsupported but still included.  Or, someone could write mining kernels in Metal which I assume is not possible or some would exist by now, or maybe since it is not cross-platform at all and Apple hardware is generally more expensive nobody would build a mining farm with Apple products.  Also since x86-64 macs can just dualboot Linux and then work fine, the target audience for Metal mining would be AppleSilicon chips which is an even smaller amount of people that would be helped by all the effort (hobby miners that happen to already have an M1 unit for other uses, etc).  Not sure any mining devs have Apple stuff so dev and testing would be difficult.  I had remote access to an M1 unit graciously via another user here, which was how what does work works.  But I'm also not a mining kernel expert as far as the guts of how they work, I only fiddled with the OpenCL support so that it would stop trying to use AMD extensions when unavailable (many places in the code would see card name containing "AMD" and then assume it was 2.0+extensions, but that's a bad assumption on Apple), or OpenCL 2.0 features (Apple OpenCL only supports 1.2, and pretty tight to spec while other "1.2" stacks allow some slop or had partial 2.0 features) and then some algorithms worked okay.  RandomX was written and tested when most other OpenCL implementations were well beyond 1.2 and might have internal logic that depends on it, or at least the things it uses confuse CL2Metal, therefore the realtime-compilation crashes.  Again since I do not understand what the kernel is doing I can not identify where things are not strictly 1.2 base-spec compliant, and never got any RandomX family algo to work.

(LP)DDR5 memory is also slower overall latency than DDR4 (even at higher clock rates) so to some degree that holds the hashrate back pretty bad unless the algorithm is not as memory latency sensitive (older cryptonight?).  The only good thing about the AppleSilicon design is the low-power which gives a pretty good hash-per-watt although then also a low overall hashrate per unit, and the hash-per-rig is low (you spend what you'd save by the low-power to increase parallelism, still better off building Ryzens, which are also not terrible at hash-per-watt compared to Intel although worse than AppleSilicon -- one $600 Ryzen rig does the hashrate of about five $600 M1 units, at not much more watts).

## minisat0shi | 2023-11-26T07:30:09+00:00
> Just to provide data for the devs re:this issue, it seems that KAWPOW works fine.... **However**: I did have to build using the "Ubuntu Instructions" of running the build_deps script, then doing cmake ... -DXMRIG with the path to the scripts folder. Didn't work when referencing brew-installed hwloc.
> 
> <img alt="Screen Shot 2022-05-20 at 12 30 08 AM" width="1080" src="https://user-images.githubusercontent.com/105223045/169477131-8ed5e363-ad80-4b29-9417-5bc0c177fc81.png">

Would you mind posting slightly more detailed instructions for this? Very curious to try CPU and OpenCL mining concurrently (kawpow and randomx).

## CarlJHarris3141 | 2024-12-22T19:39:23+00:00
Am wondering if progress was ever made incorporating Metal support into XMRig. Am XMRig now on an M3 MacBook Pro, and absent Metal support am wondering how much potential 'performance upside' is being left on the table. (On XMRig version 6.22.2 I note that both OpenCL and CUDA show as 'disabled' in the ARMv 8 64-bit, OS X version. Can't see any mention of Metal in the support documentation either)

## Spudz76 | 2024-12-23T03:02:48+00:00
I sort of looked for similar functions for a while and then gave up, I also don't have any actual Apple hardware to fiddle with anyway.

# Action History
- Created by: Amy-Ames | 2022-05-10T16:26:44+00:00
- Closed at: 2025-06-28T10:37:07+00:00
