---
title: amd_bfe ++ amd_bitalign break non-AMD OpenCL Implementations
source_url: https://github.com/xmrig/xmrig/issues/2934
author: hilga007
assignees: []
labels: []
created_at: '2022-02-20T09:27:14+00:00'
updated_at: '2022-02-21T08:29:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Unable to utilize OpenCL on Intel due to amd-specific amd_bfe and amd_bitalign (Intel is releasing the dedicated GPUs soon, so wanted to start prepping on iGPUs)

**To Reproduce**
Compile, Execute. 

**Expected behavior**
Expect OpenCL to execute correctly even though the platform is not AMD. 

**DATA**

[2022-02-20 01:23:58.971]  net      use pool us.uplexa.herominers.com:1177  116.202.226.168
[2022-02-20 01:23:58.971]  net      new job from us.uplexa.herominers.com:1177 diff 100001 algo cn/upx2 height 901941 (1 tx)
[2022-02-20 01:23:58.971]  cpu      use profile  cn/upx2  (4 threads) scratchpad 128 KB
[2022-02-20 01:23:58.981]  opencl   use profile  cn/upx2  (1 thread) scratchpad 128 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       256 |     8 |     32 | Intel(R) HD Graphics IvyBridge M GT2
[2022-02-20 01:23:58.986]  opencl   GPU #0 compiling...
[2022-02-20 01:23:58.995]  cpu      READY threads 4/4 (8) huge pages 100% 4/4 memory 1024 KB (24 ms)
[2022-02-20 01:23:59.977]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
stringInput.cl:155:16: error: implicit declaration of function 'amd_bfe' is invalid in OpenCL
stringInput.cl:138:21: note: expanded from macro 'BYTE'
stringInput.cl:163:16: warning: use of out-of-scope declaration of 'amd_bfe'
stringInput.cl:138:21: note: expanded from macro 'BYTE'
stringInput.cl:155:16: note: previous declaration is here
stringInput.cl:138:21: note: expanded from macro 'BYTE'
stringInput.cl:193:31: warning: use of out-of-scope declaration of 'amd_bfe'
stringInput.cl:189:29: note: expanded from macro 'SubWord'
stringInput.cl:138:21: note: expanded from macro 'BYTE'
stringInput.cl:155:16: note: previous declaration is here
stringInput.cl:138:21: note: expanded from macro 'BYTE'
stringInput.cl:240:17: error: implicit declaration of function 'amd_bitalign' is invalid in OpenCL
stringInput.cl:240:8: error: call to 'as_ulong' is ambiguous
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:132:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:259:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:159:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:172:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:185:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:197:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:209:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:221:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:233:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:246:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:272:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:285:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:297:20: note: candidate function
stringInput.cl:243:17: warning: use of out-of-scope declaration of 'amd_bitalign'
stringInput.cl:240:17: note: previous declaration is here
stringInput.cl:243:8: error: call to 'as_ulong' is ambiguous
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:132:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:259:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:159:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:172:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:185:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:197:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:209:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:221:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:233:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:246:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:272:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:285:20: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:297:20: note: candidate function
stringInput.cl:826:30: error: call to 'as_uint' is ambiguous
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:46:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:115:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:65:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:74:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:83:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:91:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:99:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:107:19: note: candidate function
/usr/lib/x86_64-linux-gnu/beignet/include/ocl_as.h:124:19: note: candidate function
stringInput.cl:1101:14: warning: use of out-of-scope declaration of 'amd_bfe'
stringInput.cl:138:21: note: expanded from macro 'BYTE'
stringInput.cl:155:16: note: previous declaration is here
stringInput.cl:138:21: note: expanded from macro 'BYTE'

[2022-02-20 01:23:59.987]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-02-20 01:23:59.987]  opencl   thread #0 self-test failed
[2022-02-20 01:23:59.987]  opencl   disabled (failed to start threads)




# Discussion History
## Spudz76 | 2022-02-20T14:24:26+00:00
Interesting, I was reasonably sure all this was fixed.

Try with `-DWITH_OPENCL_VERSION=120`

## Spudz76 | 2022-02-20T14:33:42+00:00
Beignet may never work, I only tested with Intel OpenCL (proprietary stack) on 6th gen or newer.

## hilga007 | 2022-02-21T06:01:36+00:00
> Beignet may never work, I only tested with Intel OpenCL (proprietary stack) on 6th gen or newer.

Is there a way to disable "relaxed fast math" while compiling to see if that resolves the issues related to these AMD kernels/extensions (as is needed apparently with Radeon HD 5000/6000/7000 GPUs as well) 

## Spudz76 | 2022-02-21T06:16:03+00:00
amd_bfe is polyfilled whenever it's [not an AMD platform here](https://github.com/xmrig/xmrig/blob/master/src/backend/opencl/cl/cn/wolf-aes.cl#L7)

If beignet erroneously lies about having `cl_amd_media_ops2` extension then it might use the AMD-only code thus ending up with a missing polyfill.

## hilga007 | 2022-02-21T06:32:09+00:00
> amd_bfe is polyfilled whenever it's [not an AMD platform here](https://github.com/xmrig/xmrig/blob/master/src/backend/opencl/cl/cn/wolf-aes.cl#L7)
> 
> If beignet erroneously lies about having `cl_amd_media_ops2` extension then it might use the AMD-only code thus ending up with a missing polyfill.

That makes sense - I'll open an issue on the beignet Gitlab (however, it seems to be a dead project at this point). 

## hilga007 | 2022-02-21T07:56:31+00:00
> Interesting, I was reasonably sure all this was fixed.
> 
> Try with `-DWITH_OPENCL_VERSION=120`

I forgot to mention that I tried this and the issue persisted. I think tried with 110... made the necessary changes in the runners and wrappers for execution and the program simply ended with "illegal instruction" -- obviously wasn't designed for 110 and I am too dumb to know what I am doing other than playing around. 

I guess now its time to play with clspv to see if OpenCL 1.2 on Vulkan in combination with the -DWITH_OPENCL_VERSION=120 will be fruitful for these GPUs.

I have like 25 of these NUCs and get such a low hashrate due to lack of AES so have been motivated to *try* to find an alternative solution before chucking them all in the eWaste bin and buying something new. It seems like OpenCL in this particular use case (Intel 3rd/4th gen CPUs w/their iGPUs) would yield a faster hashrate using graphics instead of cpu. 

The issue: My lack of knowledge. 

 

## Spudz76 | 2022-02-21T08:21:03+00:00
When I tested various pre 6th-gen Intel iGPUs the performance was less than the CPU anyway even missing AES.

Best use case for oddball CPUs is to run MoneroOcean so it can use better fitting algorithms (astrobwt probably) and earn ~1KH/s equivalence XMR which is probably 3x what they do in raw rx/0.

The weak bit is the memory controller which both CPU and iGPU have to use to get to memory.  If the iGPU had its own VRAM (HBM something) then it might go faster.  I think newer gens some of them use cache as VRAM which might go faster but again not at rx/0.

And running both CPU and iGPU at the same time just clogs the memory controller and both go slower than just CPU (high wait states / contention)

## Spudz76 | 2022-02-21T08:22:20+00:00
And again I never tested beignet or mesa or anything opensource, only the proprietary Intel OpenCL stack (which works).

Possibly only on Linux also, not sure I ever got the right combination of things to work on Windows.

## hilga007 | 2022-02-21T08:29:20+00:00
> And again I never tested beignet or mesa or anything opensource, only the proprietary Intel OpenCL stack (which works).

Makes sense. Sadly proprietary Intel OpenCL is Skylake and newer, I believe and then new Intel OpenSource OneAPI/NEO OpenCL drivers are again for Skylake (6th Gen Core???) and newer. 

Oddly enough when I install the proprietary Intel OpenCL ICD, I notice that beignet shows more kernels and more extensions -- even though the prop. installation won't work. Maybe I'll mess around again with that and see if I can force OCL for fun. 

I also have some engineering sample i9 9th gen CPUs that I was hoping to mine Raven with thanks to sharing more VRAM but I imagine that unless I can tighten the RAM timings to something ridiculous I'll get 1MH/s to 2MH/s with that. 

These are more of "novelty projects" than anything else, but I have this danged urge to try to keep old hardware out of landfills by mining instead and putting it to use (or using BOINC, etc) but again -- the age of the hardware and lack of interest by Intel to ensure their drivers work with it seems to be the issue. 

(I think Mesa's Clover OpenCL implementation is only 1.1 anyway, which probably wouldn't work with XMRig if my experiments today are an indicator) 

If for any reason you want to mess around with one of these I'm more than happy to send one to you with 8GB DDR3 and a 30GB mSATA SSD so long as you are like... not in a war zone where a package would be lost. 

# Action History
- Created by: hilga007 | 2022-02-20T09:27:14+00:00
