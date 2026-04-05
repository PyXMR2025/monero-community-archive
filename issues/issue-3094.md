---
title: 'KAWPOW: AMD R9 290/390 OpenCL Failure "thread #0 failed with error CL_INVALID_BUFFER_SIZE"'
source_url: https://github.com/xmrig/xmrig/issues/3094
author: iamhumanipromise
assignees: []
labels: []
created_at: '2022-07-24T01:36:24+00:00'
updated_at: '2025-06-28T10:42:32+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:42:32+00:00'
---

# Original Description
**Describe the bug**
The executable fails to create a KAWPOW buffer. Using latest Manjaro Linux: All "Sea Islands" and "Southern Islands" AMD GPU fixes enabled to ensure amdgpu kernel driver is loaded. Using AMDGPU-PRO 20.45 OpenCL bundle (Seemingly the last to support the Sea Islands/Southern Islands for OpenCL) 

**To Reproduce**
1) Compile with strict cache enabled and strict cache disabled. Try targeting 120 with 100 110 120 cache references. Try targeting 120 with 120 cache. Try targeting 210 with 120 200 210 caches. Try targeting 210 with 100 110 120 caches. (AMD-APP spec is CL 1.2). I compiled using GCC as well as clang. I also tried the pre-compiled xmrig binary in the manjaro repos. Basically, I tried 6+ combinations of "change a setting, try to compile with GCC. Fails to create buffer? Try OpenCL" (I also tried intel-llvm) 

**Expected behavior**
The expected outcome is for this to successfully compile an OpenCL buffer and begin to compute. Please note: Benchmarking via phoronix openbenchmarking and via geekbench indicates OpenCL is otherwise working as expected, so it does not appear to be a platform error. 

**Required data**
[CLANG14_Compiler-Succeed-w-Warnings-Executable-Fail.txt](https://github.com/xmrig/xmrig/files/9174940/CLANG14_Compiler-Succeed-w-Warnings-Executable-Fail.txt)
[Compile-Fail-Intel-LLVM.txt](https://github.com/xmrig/xmrig/files/9174941/Compile-Fail-Intel-LLVM.txt)
[GCC1211_Compiler-Succeed-w-Warnings-Executable-Fail.txt](https://github.com/xmrig/xmrig/files/9174942/GCC1211_Compiler-Succeed-w-Warnings-Executable-Fail.txt)
[Manjaro Binary.txt](https://github.com/xmrig/xmrig/files/9174943/Manjaro.Binary.txt)
[config-json.txt](https://github.com/xmrig/xmrig/files/9174949/config-json.txt)
 - Manjaro (Arch-based, rolling: kernels 5.15 stock and 5.18-xanmod)
 - AMD R9 290 4GB (HAWAII) -- AMDGPU open-source kernel driver, fixes enabled, OpenCL from 20.45 driver release package 

**Additional context**
I have thought about trying Ubuntu - but given that I will be using the same hardware with the same software packages, I am inquiring about potential software fixes. 

All of the 4GB, 6GB and 8GB cards are super cheap right now and I picked up 10 of these cards for $25 each to start a basic RVN mining farm. Getting these older cards working with OpenCL means that they can be mining for many years to come (especially the 6GB and 8GB cards) 


# Discussion History
## Spudz76 | 2022-07-24T03:56:51+00:00
My recipe for Hawaii cards is as follows:
* Ubuntu 20.04 and amdgpu-pro `20.30-1109583`
* Install only `amdgpu-pro-pin` and `opencl-amdgpu-pro` (do not use the dumb installer, unpack the debs and `dpkg -i` them)
* Once the dkms build completes, `dkms remove` it

This stack works great, using the normal `amdgpu` driver that comes with the kernel (`5.4.0-122`) with the proprietary OpenCL on top of it.  I also use this for Ellesmeres and FuryNanos which also don't work right.

I have tried almost every version of packages and 20.30 is the only reliable one for this sort of "hybrid" stack.

Also I have in `/etc/modprobe.d/amdgpu.conf`:
```
options amdgpu cik_support=1 si_support=1 pcie_gen2=0 pcie_lane_cap=1 vm_fragment_size=9 audio=0 dc=0 aspm=0 ppfeaturemask=0xffffffff
```
Unsure if any of that is "required" and I'm running them in x1 risers anyway so forcing lanes/gen seemed to be helpful.

## iamhumanipromise | 2022-07-26T07:49:57+00:00
Greetings! Thank you for that... _I embarked down a journey of Ubuntu 18.04 and 20.04. I have spent nearly 24+sleep+tinkering from bed over SSH + more hours downgrading packages and pinning the HWE stack once I was at 5.4.122 -- then using aptitude to fix broken things._  

(### Perhaps I don't know how to extract and install a deb file on Ubuntu/Debian/Mint.... On Arch I can install the files fine using a deb tool that extracts, repackages, and reinstalls.) 
(Tried the 20.30 package on Arch also, with 5.4LTS UUR kernel install -- clinfo will then load and freeze but rocminfo shows the GPUs)

..... 
_any tips for the Ubuntu piece? just sudo dpkg -i opencl-amdgpu-pro.deb amdgpu-pro-pin.deb and let them install their associated packages? Then OpenCL works for you?_ 

--------------
**\\Issue Also Occurs on Windows with pre-compiled binary, using 22.6.1 drivers and 22.x Pro Drivers//**

```
* ABOUT        XMRig/6.18.0 gcc/11.2.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz (1) 64-bit AES
                L2:2.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       3.2/30.9 GB (10%)
                DIMM_A0: <empty>
                DIMM_A1: 16 GB DDR4 @ 2667 MHz CMK32GX4M2A2666C16
                DIMM_B0: <empty>
                DIMM_B1: 16 GB DDR4 @ 2667 MHz CMK32GX4M2A2666C16
 * MOTHERBOARD  ASRock - Z390 Pro4
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      us.ravenminer.com:3838 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3224.5)
 * OPENCL GPU   #0 03:00.0 AMD FirePro W5100 (Bonaire) 930 MHz cu:12 mem:3264/4096 MB
 * OPENCL GPU   #1 01:00.0 AMD Radeon R9 200 Series (Hawaii) 1500 MHz cu:40 mem:3264/4096 MB
 * CUDA         disabled
[2022-07-26 07:41:25.851]  net      use pool us.ravenminer.com:3838  54.189.245.235
[2022-07-26 07:41:25.852]  net      new job from us.ravenminer.com:3838 diff 431M algo kawpow height 2379920
[2022-07-26 07:41:25.852]  opencl   use profile  kawpow  (2 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 |   3145728 |   256 |   3615 | AMD FirePro W5100 (Bonaire)
|  1 |   1 | 01:00.0 |  10485760 |   256 |   3615 | AMD Radeon R9 200 Series (Hawaii)
[2022-07-26 07:41:26.306]  opencl   READY threads 2/2 (452 ms)
[2022-07-26 07:41:26.624]  opencl   KawPow program for period 793306 compiled (318ms)
[2022-07-26 07:41:26.624]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 3741319168[2022-07-26 07:41:26.629]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE
[2022-07-26 07:41:26.909]  opencl   KawPow program for period 793307 compiled (285ms)
[2022-07-26 07:41:27.201]  opencl   KawPow program for period 793306 compiled (293ms)
[2022-07-26 07:41:27.202]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 3741319168[2022-07-26 07:41:27.203]  opencl   thread #1 failed with error CL_INVALID_BUFFER_SIZE
[2022-07-26 07:41:27.490]  opencl   KawPow program for period 793307 compiled (288ms)
[2022-07-26 07:41:37.347]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2022-07-26 07:41:37.349]  opencl   #1 01:00.0   0W 51C 1605RPM 1030/1300MHz
```

## Spudz76 | 2022-07-27T16:16:04+00:00
Well it's allocating 3568MB when the cards only have 3615MB free which will probably fail (needs to have a bit of headroom), so the KawPow DAG has gotten too large for those -- unless the available memory can be increased, are they 4GB cards?  Do you also run video out of them wasting space with framebuffers or such?  The module arg `dc` set to zero disables video output and stops automatic framebuffer allocation.

You could have rocm opencl installed simultaneous to the amdgpu-pro opencl which may cause confusion, I always purge any other opencl implementation (rocm or mesa) to force there to be only one cl-platform available, the amdgpu-pro one.  You can also just edit some files in `/etc/OpenCL/` so it no longer locates any other libraries besides the amdgpu-pro one.

## Spudz76 | 2022-07-27T16:25:27+00:00
As far as the Ubuntu package question, I have put all the amdgpu-pro files on a webserver so I just set it as a regular add-on repo and then add the amdgpu-pro gpg key and it all "just works" by names with apt, I don't use the installer script nor dpkg just `apt install`.

If you do use the dpkg route it should complain about missing deps and then you just keep adding each deb until it's happy with the prerequisites.

My list of installed packages with either opencl or amdgpu in the name ends up as:
```
amdgpu-core amdgpu-dkms amdgpu-dkms-firmware amdgpu-pro-core amdgpu-pro-pin clinfo-amdgpu-pro libdrm2-amdgpu libdrm-amdgpu1 libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common ocl-icd-libopencl1-amdgpu-pro opencl-amdgpu-pro opencl-amdgpu-pro-comgr opencl-amdgpu-pro-icd opencl-orca-amdgpu-pro-icd
```
But `apt-mark showmanual` has just the previously mentioned pin and opencl packages which pull the rest of those in.  And then manually remove the dkms result to force the vanilla kernel amdgpu driver since the pro one doesn't work well on older chip families.  I even use this hybrid stack on Vega64's but it does not work for Vega2 (aka VegaVII) or newer.

## Spudz76 | 2022-07-28T16:02:49+00:00
As a side note most of my 4GB cards end up running autolykos2 which does not have a forever-expanding DAG to worry about.  I am unsure if KawPow even works on them anymore, although it did when the DAG wasn't so huge yet (similar to Ethash when it deprecated itself on 4GB cards a while back).  There was a "zombie mode" for Ethash which allowed 4GB to still work somehow (with subset of the DAG) at reduced speeds -- I don't know of any KawPow Zombie-mode miner apps or if a similar workaround would even be possible or worthwhile.

# Action History
- Created by: iamhumanipromise | 2022-07-24T01:36:24+00:00
- Closed at: 2025-06-28T10:42:32+00:00
