---
title: CryptoNight variant 2 migration guide
source_url: https://github.com/xmrig/xmrig/issues/753
author: xmrig
assignees: []
labels:
- enhancement
- META
created_at: '2018-09-13T09:06:56+00:00'
updated_at: '2018-11-05T14:17:11+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:17:11+00:00'
---

# Original Description
Monero will change PoW algorithm to [CryptoNight variant 2](https://github.com/monero-project/monero/pull/4218) on [October 18th](https://github.com/monero-project/monero/commit/7f590e72619e81b943af9ad48858472ea78c0918).

### Required steps
1. **Miners and proxy should be updated to v2.8 before October 18th.**
2. `variant` option on each Monero pool should be set to `-1` (automatic).

#### Notes
* If your pool support [mining algorithm negotiation](https://github.com/xmrig/xmrig-proxy/blob/dev/doc/STRATUM_EXT.md#1-mining-algorithm-negotiation), don't need change `variant` option, just update miners and proxy to v2.8.
* If you use [xmrig-proxy](https://github.com/xmrig/xmrig-proxy) change `variant` option only on proxy side.

### Test pool
http://killallasics.moneroworld.com/

### Checklist
* [x] CPU miner is ready in [dev](https://github.com/xmrig/xmrig/commits/dev) branch.
  * [x] v2.8 released.
* [x] Pure C CPU miner is ready in [classic](https://github.com/xmrig/xmrig/commits/classic) branch.
* [x] AMD miner ready in [dev](https://github.com/xmrig/xmrig-amd/commits/dev) branch.
  * [x] v2.8 released.
* [x] NVIDIA miner is ready in [dev](https://github.com/xmrig/xmrig-nvidia/commits/dev) branch.
  * [x] v2.8 released.
* [x] proxy is ready in [dev](https://github.com/xmrig/xmrig-proxy/commits/dev) branch.
  * [x] v2.8 released.

# Discussion History
## jetbird747 | 2018-09-19T00:08:28+00:00
I tested xmrig on killallasics.moneroworld.com. for cn/2. I'm seeing a 25% drop in hashrate vs cn/1. I'm using dual E5-2660 V2 cpus, is this drop in hashrate expected?

thanks

## xmrig | 2018-09-19T02:15:05+00:00
`cn/2` is slower by design, before release will be added ability to use highly optimized assembly code for Intel and AMD Ryzen CPUs, new option `asm` will be introduced, it will helps reduce difference in hashrate.
Thank you.

## xmrig | 2018-09-25T07:55:03+00:00
## CPU miner
CPU miner will use highly optimized Assembly code for  CryptoNight variant 2, author of this code is @SChernykh. Changes already in [dev branch](https://github.com/xmrig/xmrig/commits/dev) and ready for tests. Usually no additional configuration required for it, miner will load proper ASM code automatically if it available for your CPU, for fine tuning also added global and per thread option `"asm"`.

#### Possible values for `"asm"` option:
* `true` or `"auto"` automatic, miner will try use proper assembly by CPUID information. This is default value.
* `false` or `"none"` feature disabled.
* `"intel"` best for Intel CPUs starting from Ivy Bridge/Sandy Bridge.
* `"ryzen"` best for AMD Ryzen CPUs.

#### Limitations:
Only 64bit builds and single and double hash modes supported.

## NVIDIA/CUDA miner
Future of NVIDIA miner now unclear, we hope @psychocrypt can create fast CUDA code for it, if not for NVIDIA can be used AMD/OpenCL miner.

## AMD/OpenCL miner
* `"strided_index": 1,` should be not used for CryptoNight variant 2, you will see warning message about it.
* Added [extended `opencl-platform`](https://github.com/xmrig/xmrig-amd/issues/162) option, can be used for auto-configuration for NVIDIA GPUs.

## jetbird747 | 2018-09-25T13:07:05+00:00
It's my understanding that @SChernykh is still working on the double hash asm mode, hopefully this will be done and incorporated by the release date. Without it I'm seeing a 12% reduction in hashrate on my CPU system.

## SChernykh | 2018-09-25T13:50:53+00:00
@jetbird747 Double hash asm version is already integrated into xmrig.

## jetbird747 | 2018-09-25T20:19:29+00:00
@SChernykh 

Using double hash I'm seeing;
CNv7: 908H/S
CNv8 873H/s

Using single hash;
CNv7: 962H/S
CNv8 846H/s

~9% reduction in hashrate

6 of 10 cores enabled on a Dual E5-2660 v2 processor; 25MB L3; Fedora 27


    "threads": [
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 0 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 1 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 2 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 3 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 4 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 5 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 6 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 7 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 8 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 9 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 10 },
    { "low_power_mode" : 2, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 11 }
     ]

  "threads": [
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 0 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 1 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 2 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 3 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 4 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 5 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 12 },
	{ "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 13 },
	{ "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 14 },
	{ "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 15 },
	{ "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 16 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 17 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 6 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 7 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 8 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 9 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 10 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 11 },
	{ "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 18 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 19 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 20 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 21 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 22 },
    { "low_power_mode" : false, "no_prefetch" : true,  "asm" : "intel", "affine_to_cpu" : 23 }
 ]


## snipeTR | 2018-09-25T20:23:09+00:00
Hardware os and xmrig info

## SChernykh | 2018-09-25T20:39:09+00:00
@jetbird747 Try to enable all 10 cores. Run single thread on 8 cores and double thread on 2 remaining cores for each CPU. This should give you the best performance.

## Bathmat | 2018-09-26T13:05:34+00:00
OS: Win10 1803
CPU: Dual E5-2670v2 (10 cores, 20 threads, 25MB L3)

CNv7: 1090 h/s
CNv8: 1055 h/s (with asm)

Interestingly, using `"asm" : "intel"` or `"asm" : "ryzen"` results in about the same hashrate. `"asm" : false` is only 15 h/s slower.
```
"threads": [
            {                "low_power_mode": 1,                "affine_to_cpu": 0            },
            {                "low_power_mode": 1,                "affine_to_cpu": 2            },
            {                "low_power_mode": 1,                "affine_to_cpu": 4            },
            {                "low_power_mode": 2,                "affine_to_cpu": 6            },
            {                "low_power_mode": 1,                "affine_to_cpu": 8            },
            {                "low_power_mode": 1,                "affine_to_cpu": 10            },
            {                "low_power_mode": 1,                "affine_to_cpu": 12            },
            {                "low_power_mode": 1,                "affine_to_cpu": 14            },
            {                "low_power_mode": 1,                "affine_to_cpu": 16            },
            {                "low_power_mode": 1,                "affine_to_cpu": 18            },
            {                "low_power_mode": 1,                "affine_to_cpu": 20            },
            {                "low_power_mode": 1,                "affine_to_cpu": 22            },
            {                "low_power_mode": 1,                "affine_to_cpu": 24            },
            {                "low_power_mode": 2,                "affine_to_cpu": 26            },
            {                "low_power_mode": 1,                "affine_to_cpu": 28            },
            {                "low_power_mode": 1,                "affine_to_cpu": 30            },
            {                "low_power_mode": 1,                "affine_to_cpu": 32            },
            {                "low_power_mode": 1,                "affine_to_cpu": 34            },
            {                "low_power_mode": 1,                "affine_to_cpu": 36            },
            {                "low_power_mode": 1,                "affine_to_cpu": 38            }
        ],
```

## Bathmat | 2018-09-26T13:15:31+00:00
OS: Win10 1803
GPU: GTX1050 (+160 core, +98 mem)

CNv7 (CUDA) : 325 h/s
CNv7 (OpenCL) : 319.5 h/s
CNv8 (OpenCL) : **262 h/s** 👎 
```
{            "index": 0,
            "intensity": 448,
            "worksize": 8,
            "strided_index": 0,
            "mem_chunk": 2,
            "unroll_factor": 1,
            "comp_mode": true,
            "affine_to_cpu": false        }
```

## SChernykh | 2018-09-26T13:27:58+00:00
> CNv7 (OpenCL) : 319.5 h/s
CNv8 (OpenCL) : 262 h/

@xmrig I forgot to add my NVIDIA tuned OpenCL code for reading/writing scratchpad chunks: https://github.com/SChernykh/xmr-stak-amd/blob/master/opencl/cryptonight.cl#L728
On AMD cards it's fine to read/write to global memory directly, but on NVIDIA it's faster to first read 64 bytes to shared memory, process them and write them all back to global memory.

Can you add it? I can create a pull request in a couple of days if you don't have time right now.

## xmrig | 2018-09-26T13:54:34+00:00
@SChernykh Yes I can, I'll do it later today.
Thank you.

## xmrig | 2018-09-27T12:48:37+00:00
@Bathmat @SChernykh done https://github.com/xmrig/xmrig-amd/commit/27444452153019d56cbb0d309a4777da86b32fd7

## Bathmat | 2018-09-27T14:37:22+00:00
> @Bathmat @SChernykh done [xmrig/xmrig-amd@2744445](https://github.com/xmrig/xmrig-amd/commit/27444452153019d56cbb0d309a4777da86b32fd7)

Same GTX1050:

CNv7 (OpenCL) : 320 h/s
CNv8 (OpenCL) : **296 h/s** 👍 Still not quite as good as AMD or CPU, but much better.

## vitaliy1985 | 2018-09-28T12:18:34+00:00
how to download xmrig 2.8?


## xmrig | 2018-09-28T12:23:49+00:00
@vitaliy1985 Now it available only as source in [dev](https://github.com/xmrig/xmrig/tree/dev) branch.
Thank you.

## vitaliy1985 | 2018-09-28T12:36:28+00:00
"exe" will be?

## xmrig | 2018-09-28T12:41:57+00:00
Of course it will be, but later, we still have a lot of time before October 18th for release.
Thank you.

## Bathmat | 2018-09-28T13:02:17+00:00
OS: Win10
GPU: GTX-1060 6GB (+150 core, +500 mem = 2000 core, 4300 mem)

CNv7 (CUDA): 520 h/s
CNv7 (OpenCL): 497 h/s
CNv8 (OpenCL): **446 h/s** 
```
    "threads": [
        {
            "index": 0,
            "intensity": 640,
            "worksize": 8,
            "strided_index": 0,
            "mem_chunk": 2,
            "unroll": 2,
            "comp_mode": true,
            "affine_to_cpu": false
        }
    ],
```

## xmrig | 2018-09-30T13:58:27+00:00
v2.8.0-rc (release candidate) will be released on October 1 (about 24 hours from now) if no critical bugs will found, except NVIDIA miner.

https://config.xmrig.com/ is updated for v2.8 too.

Also I create Twitter account https://twitter.com/xmrig_dev it's **_dev** because just **xmrig** is already taken.

## xmrig | 2018-10-01T10:43:35+00:00
v2.8.0-rc released.
https://github.com/xmrig/xmrig/releases/tag/v2.8.0-rc
https://github.com/xmrig/xmrig-amd/releases/tag/v2.8.0-rc
https://github.com/xmrig/xmrig-proxy/releases/tag/v2.8.0-rc

## vitaliy1985 | 2018-10-01T12:41:26+00:00
My xmrig.exe normally works.
What is xmrig-notls.exe for?

## xmrig | 2018-10-01T12:50:59+00:00
`xmrig-notls.exe` build **without** SSL/TLS support, all versions before 2.8 was without it.
`xmrig.exe` build **with** SSL/TLS support, with this build you can use secure ports on your pool (if available).

## vitaliy1985 | 2018-10-01T13:10:29+00:00
"pools":[
{
"tls": true
}
]
if SSL/TLS support?

xmrig.exe "pools":[{"tls": false}] = xmrig-notls.exe ?

## xmrig | 2018-10-01T13:24:40+00:00
`"tls": true` and TLS port on pool.

* If you set `"tls": true` but try connect to regular/unsecure port, it won't work.
* Or if set `"tls": false` but try connect to TLS port it won't work too.

`tls` option should match with port on pool.
`xmrig-notls.exe` will ignore pools with `"tls": true`

For example https://monero.hashvault.pro/en/ports with `"tls": true` you can connect only to port `8080` and `9000`.

If any question renaming better use this issue: #758

## strawbs1 | 2018-10-01T14:01:09+00:00
Are there any extra build instructions ? I built it for windows and ASM is causing problems. 

## xmrig | 2018-10-01T14:10:26+00:00
@JungleCatSW please open new issue with full details, for recent CMake and MSVC 2017/MSYS2 no additional steps required.
Thank you.

## k0ste | 2018-10-02T07:39:26+00:00
@xmrig, stable releases (not rc) will be available before 18 oct?

## xmrig | 2018-10-02T10:10:27+00:00
@k0ste  yes it will, actually this rc is pretty stable, at least no major bugs was found.
Thank you.

## k0ste | 2018-10-02T12:18:14+00:00
@xmrig this is important not because of bugs. This important for packaging, only stable versions, not 'git/svn' or rc. So if "stable" is not will be released I as package maintainer should provide "rc" version as release version due hardfork of protocol.
Thanks.

## k0ste | 2018-10-03T08:05:54+00:00
@xmrig, also please document new options in code: `unroll`, `cache` and `autosave`.
Thanks.

## LearnMiner | 2018-10-03T14:24:52+00:00
test pool have pyment? or no mine?

## phillipsjk | 2018-10-04T15:25:48+00:00
I am using a G34 socket AMD CPU (Bulldozer 6200 series)

Should I use the Intel or Ryzen ASM flag?

Edit: https://en.wikipedia.org/wiki/List_of_AMD_Opteron_microprocessors#Bulldozer_based_Opterons

> All models support: MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, SSE4a, NX bit, AMD64, AMD-V, AES, CLMUL, AVX, XOP, FMA4.

I may be retiring the machine by spring though.

## Bathmat | 2018-10-04T15:35:29+00:00
> I am using a C34 socket AMD CPU (Bulldozer?)
> 
> Should I use the Intel or Ryzen ASM flag?

@phillipsjk I've tested on an FX-6350 (Piledriver?) and both give about the same performance, but "ryzen" is slightly faster.

## phillipsjk | 2018-10-04T15:39:48+00:00
@Bathmat I an not even sure I got the series right, I guess I should just test it.

I was worried the optimizations would use instructions one or the other does not have.

## xmrig | 2018-10-04T15:48:25+00:00
@Bathmat ASM code is faster than C++? If yes should enable ASM by default on this kind of CPUs too, currently `ryzen` only automatically loaded on real Ryzen.
@phillipsjk If ASM code use unsupported instructions it easy to known, miner just crash.

## SChernykh | 2018-10-04T15:50:02+00:00
ASM code is generally faster than C++ on any CPU. It only uses AES instructions, nothing exotic. All CPUs with AES support can run both asm versios.

## Bathmat | 2018-10-04T15:50:33+00:00
@xmrig sorry, should have said that yes, both asm versions are faster than "off"/false.

## Bathmat | 2018-10-04T15:53:27+00:00
OS: Win10
CPU: AMD FX-6350 @ 4.5Ghz (6 cores, 8MB L3)
v7: 290 h/s
v8 (asm : off): 240 h/s
v8 (asm : ryzen): 271 h/s
v8 (asm : intel): 268 h/s

Config: 5 threads, no affinity.

## xmrig | 2018-10-04T16:01:23+00:00
@SChernykh Current code to determinate what assembly should use https://github.com/xmrig/xmrig/blob/master/src/core/cpu/AdvancedCpuInfo.cpp#L75 so, I can safe remove `ext_family` and `ext_model` checks?

## SChernykh | 2018-10-04T16:03:39+00:00
@xmrig Yes, you don't need them. Only AES support check.

## xmrig | 2018-10-04T16:11:51+00:00
@SChernykh Done. Thank you.

## k0ste | 2018-10-05T01:46:23+00:00
@xmrig, answer on [this post](https://github.com/xmrig/xmrig/issues/753#issuecomment-426547493), please.

## k0ste | 2018-10-05T03:34:39+00:00
Ok, `cache` is a OpenCL cache, I'm also was find issue with this and create separate issue xmrig/xmrig-amd#165.

## 2010phenix | 2018-10-05T22:07:46+00:00
@xmrig First one with classic(test ~5 min each):

**Windows7 x64 build with MSYS2 x64** (i5-2500 CPU @ 3.30GHz - 4core)

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   available, enabled
 * CPU:                  Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      2, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-06 00:17:17] Pool set diff to 100
[2018-10-06 00:17:17] Stratum detected new block
[2018-10-06 00:17:18] accepted: 1/1 (100.00%), 127.03 H/s at diff 100
....
[2018-10-06 00:20:35] Pool set diff to 10000
[2018-10-06 00:20:35] Stratum detected new block
[2018-10-06 00:21:35] accepted: 84/84 (100.00%), 145.59 H/s at diff 10000
[2018-10-06 00:21:52] accepted: 85/85 (100.00%), 145.99 H/s at diff 10000


**asm ~146 H\s** (if use key --asm ryzen without Ryzen CPU **~142 H\s**)
+++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   available, enabled
 * CPU:                  Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      2, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-06 00:26:15] Pool set diff to 100
[2018-10-06 00:26:15] Stratum detected new block
[2018-10-06 00:26:18] accepted: 1/1 (100.00%), 112.05 H/s at diff 100
....
[2018-10-06 00:31:13] Pool set diff to 10000
[2018-10-06 00:31:13] Stratum detected new block
[2018-10-06 00:31:48] accepted: 70/70 (100.00%), 123.47 H/s at diff 10000
[2018-10-06 00:31:59] accepted: 71/71 (100.00%), 129.21 H/s at diff 10000


**noasm ~129 H\s** (if use key --asm ryzen without Ryzen CPU and ASM code no any crash ;) )
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   available, enabled
 * CPU:                  Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      2, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-06 00:46:58] Pool set diff to 5000
[2018-10-06 00:46:58] Stratum detected new block
[2018-10-06 00:47:08] accepted: 1/1 (100.00%), 159.29 H/s at diff 5000
....
[2018-10-06 00:50:19] Pool set diff to 8310
[2018-10-06 00:50:19] Stratum detected new block
[2018-10-06 00:51:10] accepted: 8/8 (100.00%), 158.38 H/s at diff 8310

++++++++++++++++++++++++++++++++++++++++++++++++++++
Monero **### v7 ~159 H\s**


## 2010phenix | 2018-10-05T22:58:05+00:00
Second one with classic(test ~5 min each):
**Windows Server 2012 R2 x64** (CPU E5-2620 0 @ 2.00GHz - 12core)

 * XMRig 9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      6, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-06 06:22:56] Pool set diff to 100
[2018-10-06 06:22:56] Stratum detected new block
[2018-10-06 06:22:57] accepted: 1/1 (100.00%), 115.54 H/s at diff 100
......
[2018-10-06 06:26:33] Pool set diff to 10000
[2018-10-06 06:26:33] Stratum detected new block
[2018-10-06 06:26:59] accepted: 57/57 (100.00%), 134.07 H/s at diff 10000


**V8 asm ~134 H\s**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      6, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-06 06:36:52] Pool set diff to 5000
[2018-10-06 06:36:52] Stratum detected new block
[2018-10-06 06:37:36] accepted: 1/1 (100.00%), 107.48 H/s at diff 5000
.....
[2018-10-06 06:41:46] accepted: 6/6 (100.00%), 154.11 H/s at diff 5000

**Monero v7 ~154 H\s**

## 2010phenix | 2018-10-05T23:31:17+00:00
another one OS with classic(test ~5 min each):

**Windows 10 x64** (CPU E5-2650 @ 2.00GHz - 16 core)

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   available, enabled
 * CPU:                 Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      8, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-06 07:06:04] Pool set diff to 100
[2018-10-06 07:06:04] Stratum detected new block
[2018-10-06 07:06:05] accepted: 1/1 (100.00%), 57.20 H/s at diff 100
......
[2018-10-06 07:10:28] Pool set diff to 10000
[2018-10-06 07:10:28] Stratum detected new block
[2018-10-06 07:10:33] accepted: 186/186 (100.00%), 324.98 H/s at diff 10000


**v8 asm ~325 H\s** (if use key --asm ryzen without Ryzen CPU)
**v8 asm ~333 H\s** (if use key --asm auto)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   available, enabled
 * CPU:                 Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      8, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-06 07:15:05] Pool set diff to 5000
[2018-10-06 07:15:05] Stratum detected new block
[2018-10-06 07:15:11] accepted: 1/1 (100.00%), 344.30 H/s at diff 5000
.....
[2018-10-06 07:19:17] Stratum detected new block
[2018-10-06 07:19:24] accepted: 9/9 (100.00%), 343.19 H/s at diff 6630

**Monero v7 ~344 H\s**

PS tomorrow check few other OS and VM if build stable

## k0ste | 2018-10-06T09:27:07+00:00
```
OS: Linux 4.16.12
Miner version: xmrig 2.8.0-rc
Backend: AMD OpenCL:

- Adapter 0: PCI 2:0:0: Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
  Core: 1050 MHz, Mem: 1500 MHz, Vddc: 1.188 V, Load: 99%, Temp: 66 C, Fan: 100%                                                                                                                                
- Adapter 1: PCI 3:0:0: Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
  Core: 1050 MHz, Mem: 1500 MHz, Vddc: 1.163 V, Load: 99%, Temp: 65 C, Fan: 100%                                                                                                                                     
- Adapter 2: PCI 6:0:0: Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
  Core: 1050 MHz, Mem: 1500 MHz, Vddc: 1.163 V, Load: 99%, Temp: 60 C, Fan: 100%                                                                                                                            
- Adapter 3: PCI 7:0:0: Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
  Core: 1050 MHz, Mem: 1500 MHz, Vddc: 1.163 V, Load: 99%, Temp: 55 C, Fan: 100%                                                                                                                                  
- Adapter 4: PCI 8:0:0: Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
  Core: 1000 MHz, Mem: 1500 MHz, Vddc: 1.188 V, Load: 99%, Temp: 56 C, Fan: 100%                                                                                                                                
- Adapter 5: PCI 9:0:0: Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
  Core: 1050 MHz, Mem: 1500 MHz, Vddc: 1.163 V, Load: 99%, Temp: 46 C, Fan: 100%                                                                     

speed:  
 - cryptonight_v7: 2670.2 H/S

| THREAD | GPU | 10s H/s | 60s H/s | 15m H/s |
|      0 |   0 |   215.9 |   215.6 |     n/a |
|      1 |   0 |   215.6 |   215.9 |     n/a |
|      2 |   1 |   227.1 |   227.0 |     n/a |
|      3 |   1 |   227.1 |   227.0 |     n/a |
|      4 |   2 |   226.2 |   225.9 |     n/a |
|      5 |   2 |   226.0 |   226.0 |     n/a |
|      6 |   3 |   227.0 |   226.8 |     n/a |
|      7 |   3 |   226.6 |   226.8 |     n/a |
|      8 |   4 |   212.8 |   212.0 |     n/a |
|      9 |   4 |   211.4 |   211.8 |     n/a |
|     10 |   5 |   226.7 |   226.8 |     n/a |
|     11 |   5 |   227.2 |   226.9 |     n/a |
[2018-10-06 15:52:07] speed 10s/60s/15m 2670.2 2669.2 n/a H/s max 2670.2 H/s

 - cryptonight_v8: 1925.0 H/S

| THREAD | GPU | 10s H/s | 60s H/s | 15m H/s |
|      0 |   0 |   163.7 |   163.9 |     n/a |
|      1 |   0 |   164.0 |   163.9 |     n/a |
|      2 |   1 |   160.8 |   159.9 |     n/a |
|      3 |   1 |   161.1 |   159.9 |     n/a |
|      4 |   2 |   161.0 |   159.8 |     n/a |
|      5 |   2 |   162.6 |   160.0 |     n/a |
|      6 |   3 |   160.9 |   160.0 |     n/a |
|      7 |   3 |   161.5 |   160.1 |     n/a |
|      8 |   4 |   154.6 |   154.0 |     n/a |
|      9 |   4 |   153.7 |   154.3 |     n/a |
|     10 |   5 |   160.2 |   160.6 |     n/a |
|     11 |   5 |   160.3 |   160.5 |     n/a |
[2018-10-06 16:03:14] speed 10s/60s/15m 1925.0 1917.5 n/a H/s max 1924.8 H/s

Miner config:
- cryptonight_v7:

    "threads": [
        {
            "index": 0,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 0,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 1,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 1,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 2,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 2,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 3,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 3,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 4,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 4,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 5,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 5,
            "intensity": 400,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        }

- cryptonight_v8:

    "threads": [
        {
            "index": 0,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 0,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 1,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 1,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 2,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 2,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 3,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 3,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 4,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 4,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 5,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        },
        {
            "index": 5,
            "intensity": 400,
            "worksize": 16,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 4,
            "comp_mode": true,
            "affine_to_cpu": false
        }
```

@SChernykh, -27% for Sea Islands cards, on 3% `xmrig-amd` better than `xmr-stak`.

## xmrig | 2018-10-06T10:49:54+00:00
@HostCrypto stable v2.8.1 release (not rc) around October 9-12, NVIDIA release 11-14.

## SChernykh | 2018-10-06T13:41:01+00:00
@questionman1992 The final tweak was done 2 weeks ago, 2.8 will work after the fork.

## xmrig | 2018-10-06T13:42:32+00:00
@questionman1992 Just don't forget set `variant` to `-1` and all will be good.

## bigstunta101 | 2018-10-06T15:19:06+00:00
> @questionman1992 Just don't forget set `variant` to `-1` and all will be good.

for AMD GPUs, are we also going to be expecting the significant hashrate drop or is there something that could help keep hashrate close to current rates?

## SChernykh | 2018-10-06T15:22:21+00:00
@bigstunta101 Less than 10% drop for RX and Vega with proper config: https://github.com/SChernykh/xmr-stak-cpu#performance

## bigstunta101 | 2018-10-06T15:26:32+00:00
> @bigstunta101 Less than 10% drop for RX and Vega with proper config: https://github.com/SChernykh/xmr-stak-cpu#performance

great news. thank you

## 2010phenix | 2018-10-06T20:54:40+00:00
classic(test ~5 min each):

**Windows Server 2012 R2 x64** (CPU E5-2640 v3 @ 2.60GHz - 16core)

 **double hash mode. --av=2**

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      8, av=2, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-07 04:36:37] Pool set diff to 5000
[2018-10-07 04:36:37] Stratum detected new block
[2018-10-07 04:38:01] accepted: 1/1 (100.00%), 216.12 H/s at diff 5000
.......
[2018-10-07 04:41:55] Pool set diff to 6510
[2018-10-07 04:41:55] Stratum detected new block
[2018-10-07 04:41:56] accepted: 12/12 (100.00%), 214.91 H/s at diff 6510


**Monero v7 ~216 H\s**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz (1)
 * CPU FEATURES: x86_64 AES-NI
 * THREADS:      8, av=2, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-07 04:42:42] Pool set diff to 100
[2018-10-07 04:42:42] Stratum detected new block
[2018-10-07 04:42:44] accepted: 1/1 (100.00%), 135.61 H/s at diff 100
........
[2018-10-07 04:47:50] Pool set diff to 10000
[2018-10-07 04:47:50] Stratum detected new block
[2018-10-07 04:47:57] accepted: 55/55 (100.00%), 142.69 H/s at diff 10000

**v8 asm ~142 H\s** (if use key --asm auto)


## 2010phenix | 2018-10-08T14:03:03+00:00
classic(test ~5 min each):
Last one test, strange and not detect AES and etc with VMware server:

**VMware - Windows server 2008 R2 X64**   (CPU E7- 4820  @ 2.00GHz - 64 core)

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E7- 4820  @ 2.00GHz (1)
 * CPU FEATURES: x86_64 -AES-NI
 * THREADS:      32, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-08 21:11:26] Pool set diff to 100
[2018-10-08 21:11:26] Stratum detected new block
[2018-10-08 21:11:31] accepted: 1/1 (100.00%), 281.77 H/s at diff 100
.....
[2018-10-08 21:14:23] Pool set diff to 10000
[2018-10-08 21:14:24] Stratum detected new block
[2018-10-08 21:15:26] accepted: 134/134 (100.00%), 410.57 H/s at diff 10000
[2018-10-08 21:15:55] accepted: 135/135 (100.00%), 410.31 H/s at diff 10000


**mode. --av=1** (in config av1)
**v8 asm ~414 H\s** (if use key --asm auto)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E7- 4820  @ 2.00GHz (1)
 * CPU FEATURES: x86_64 -AES-NI
 * THREADS:      32, av=1, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-08 21:19:30] Pool set diff to 5000
[2018-10-08 21:19:30] Stratum detected new block
[2018-10-08 21:19:36] accepted: 1/1 (100.00%), 545.26 H/s at diff 5000
....
[2018-10-08 21:23:24] Pool set diff to 10890
[2018-10-08 21:23:47] Stratum detected new block
[2018-10-08 21:23:54] accepted: 13/13 (100.00%), 584.24 H/s at diff 10890


**mode. --av=1** (in config av1)
**Monero v7 ~584 H\s**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E7- 4820  @ 2.00GHz (1)
 * CPU FEATURES: x86_64 -AES-NI
 * THREADS:      32, av=3, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-08 21:34:52] Pool set diff to 100
[2018-10-08 21:34:52] Stratum detected new block
[2018-10-08 21:34:57] accepted: 1/1 (100.00%), 226.13 H/s at diff 100
.......
[2018-10-08 21:39:11] Pool set diff to 10000
[2018-10-08 21:39:11] Stratum detected new block
[2018-10-08 21:39:31] accepted: 107/107 (100.00%), 261.39 H/s at diff 10000

**mode. --av=3** (in config av auto)
**v8 asm ~259 H\s** (if use key --asm auto)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E7- 4820  @ 2.00GHz (1)
 * CPU FEATURES: x86_64 -AES-NI
 * THREADS:      32, av=3, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-08 21:25:15] Pool set diff to 5000
[2018-10-08 21:25:15] Stratum detected new block
[2018-10-08 21:25:41] accepted: 1/1 (100.00%), 290.30 H/s at diff 5000
.....
[2018-10-08 21:30:01] Pool set diff to 11490
[2018-10-08 21:30:01] Stratum detected new block
[2018-10-08 21:30:31] accepted: 15/15 (100.00%), 277.88 H/s at diff 11490


**mode. --av=3** (in config auto)
**Monero v7 ~283 H\s**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


**very strange with AV2 double ASM**

 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E7- 4820  @ 2.00GHz (1)
 * CPU FEATURES: x86_64 -AES-NI
 * THREADS:      32, av=2, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://killallasics.moneroworld.com:3333
[2018-10-08 21:49:23] Pool set diff to 100
[2018-10-08 21:49:23] Stratum detected new block
[2018-10-08 21:49:29] accepted: 1/1 (100.00%), 155.06 H/s at diff 100
.............
[2018-10-08 21:54:00] Pool set diff to 10000
[2018-10-08 21:54:00] Stratum detected new block
[2018-10-08 21:54:07] accepted: 79/79 (100.00%), 154.58 H/s at diff 10000


**mode. --av=2** (in config av av2)
**v8 asm ~158 H\s** (if use key --asm auto)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * XMRig 0.9.0-dev   www.xmrig.com
 * HUGE PAGES:   unavailable, disabled
 * CPU:                 Intel(R) Xeon(R) CPU E7- 4820  @ 2.00GHz (1)
 * CPU FEATURES: x86_64 -AES-NI
 * THREADS:      32, av=2, cryptonight/auto, donate=0%
 * STRATUM URL:  stratum+tcp://pool.supportxmr.com:3333
[2018-10-08 21:43:07] Pool set diff to 5000
[2018-10-08 21:43:07] Stratum detected new block
[2018-10-08 21:43:42] accepted: 1/1 (100.00%), 226.45 H/s at diff 5000
........
[2018-10-08 21:47:58] Pool set diff to 5000
[2018-10-08 21:47:58] Stratum detected new block
[2018-10-08 21:48:01] accepted: 8/8 (100.00%), 202.32 H/s at diff 5000


 **double hash mode. --av=2
Monero v7 ~226 H\s**

## FBI962 | 2018-10-08T20:10:34+00:00
and how can i do that on Ubuntu 16.4 TLS???

## xmrig | 2018-10-09T00:50:48+00:00
Stable v2.8.1 release (CPU/AMD/Proxy) available. For miners only minor bugfixes since v2.8.0-rc, for proxy update highly recommended to install.

## xmrig | 2018-10-10T04:27:51+00:00
NVIDIA miner ready for `cn/2` tests in dev branch https://github.com/xmrig/xmrig-nvidia/commits/dev

## FBI962 | 2018-10-10T10:42:26+00:00
> Stable v2.8.1 release (CPU/AMD/Proxy) available. For miners only minor bugfixes since v2.8.0-rc, for proxy update highly recommended to install.

i didnt understand

is theres any update for ubuntu 16.4 TLS??

## k0ste | 2018-10-10T11:52:06+00:00
@FBI962, you should update miner at any distro.

## FBI962 | 2018-10-10T12:44:43+00:00
> @FBI962, you should update miner at any distro.

how can i update

what is teh command?

also is it working on ubuntu 18.4 TLS

## snipeTR | 2018-10-10T12:45:54+00:00
Read the doc

## SChernykh | 2018-10-10T13:17:11+00:00
@xmrig 
> NVIDIA miner ready for cn/2 tests in dev branch https://github.com/xmrig/xmrig-nvidia/commits/dev

I've optimized integer math for CUDA: https://github.com/SChernykh/fast_int_math_v2_cuda/commit/2ac043c097449f29ed0cec4a9100b68c1e4cf636
It works faster on NVIDIA cards. I'll test optimized OpenCL version this evening.

## xmrig | 2018-10-10T17:04:26+00:00
@SChernykh Added (you already saw it) about extra 1 H/s per card. Thank you.

## Bathmat | 2018-10-10T17:48:11+00:00
@SChernykh seeing the same as @xmrig. 1-5 h/s faster, depending on the GPU.

## SChernykh | 2018-10-10T17:51:56+00:00
@Bathmat Nice, can you post the latest numbers (CNv1 vs. CNv2) here, so I could update my performance table https://github.com/SChernykh/xmr-stak-cpu#performance ?

## Bathmat | 2018-10-10T18:07:51+00:00
@SChernykh 
OS: Win7
GPU(s): GTX970, 2x GTX1050 (CUDA10, 411.7 driver)
CN/1: 483 + (2 * 300) h/s = 1083 h/s
CN/2: 455 + (2 * 291) h/s = 1037 h/s, 95.75%

Of note, this computer was slightly faster using CUDA 9.1 and 391 drivers (1100 h/s); however, I cannot get xmrig-nvidia to compile with CUDA 9.1 🤷‍♂️ 

For my Win10 with GTX1050:
CN/1: 325 h/s
CN/2: 318 h/s, 97.8% (that's without your latest optimizations since I haven't updated the driver for that rig yet, still using CUDA 9.1 and 397 driver)

## xmrig | 2018-10-10T18:28:58+00:00
> I cannot get xmrig-nvidia to compile with CUDA 9.1

Compile error or? `-DCUDA_TOOLKIT_ROOT_DIR=` allow specify path to CUDA, I recently successfully compile with CUDA 9.2 and 8.0, so no issues with 9.1 should be.

## Bathmat | 2018-10-10T18:47:32+00:00
`set CUDA_PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.1`

```
Build FAILED.

"C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-nvidia.sln" (default target) (1) ->
"C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj.metaproj" (default target) (3) ->
"C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj" (default target) (4) ->
(CustomBuild target) ->
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(603): err
or : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(604): err
or : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(605): err
or : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(637): err
or : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(1148): er
ror : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(1594): er
ror : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(2433): er
ror : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(2433): er
ror : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(385): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xtr1common(59): error
 : class "std::enable_if<<error-constant>, int>" has no member "type" [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcx
proj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(647): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(654): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(698): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(705): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(777): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(786): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(787): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(796): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(797): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(862): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xmemory0(353): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xmemory0(943): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xmemory0(1217): error
 : expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xstring(1914): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xtr1common(59): error
 : class "std::enable_if<<error-constant>, void>" has no member "type" [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vc
xproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\xutility(264): error
: expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(1562): er
ror : expected a ">" [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\memory(1483): error :
 expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\memory(1490): error :
 expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\memory(2536): error :
 expression must have a constant value [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(1562): er
ror : expected a ">" [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(1562): er
ror : expected a ">" [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\include\type_traits(1562): er
ror : expected a ">" [C:\xmrig\xmrig-nvidia-dev\cuda9.1\xmrig-cuda.vcxproj]
  CUSTOMBUILD : nvcc error : 'cicc' died with status 0xC0000005 (ACCESS_VIOLATION) [C:\xmrig\xmrig-nvidia-dev\cuda9.1\x
mrig-cuda.vcxproj]

    0 Warning(s)
    34 Error(s)
```

## SChernykh | 2018-10-10T19:12:12+00:00
@Bathmat It looks like CUDA 9.1 and latest Visual Studio are not really compatible.

## Bathmat | 2018-10-10T20:11:40+00:00
@SChernykh yeah, I can get 9.1 to work with stak and `-vcvars_ver=14.11` and `-T v141,host=x64`, but that's not working with xmrig-nvidia, and I haven't had time to figure out what might work.

Also, I misspoke earlier: Drivers 391 work better than 411 on my Win7 rig. Even if I compile stak with CUDA 9.1, it's still slower with driver 411. 

Oh well, I should probably just upgrade to CUDA 10.

## xmrig | 2018-10-10T20:12:21+00:00
@Bathmat ok, then, you should use build instructions for CUDA 8 https://github.com/xmrig/xmrig-nvidia/wiki/Windows-Build-CUDA-8 but with path to CUDA 9.1.

`cmake .. -G "Visual Studio 15 2017 Win64" -T v140,host=x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2015\x64 -DCUDA_TOOLKIT_ROOT_DIR="c:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.1"`

## Bathmat | 2018-10-10T21:45:13+00:00
@xmrig thanks, that worked. Reloaded 391 drivers and speed is back up: 1100 h/s total for CNv1 and 1067 h/s for CNv2 (97%). The GTX970 stayed the same at 455 h/s for CNv2, but the 2 GTX1050s got a 15h/s boost each to 306 h/s

Also @SChernykh I tested my Win10 GTX1050 with your optimizations and CNv2 hashrate is the same; 318h/s

## Bathmat | 2018-10-11T02:24:31+00:00
Here's my last Nvidia:
OS: Win10
GPU: GTX1060 6GB (CUDA 9.1, 397 drivers), 2000 core clock, 4300 mem clock
CNv1: 520 h/s
CNv2: 512 h/s, 98.4% 🥇 

EDIT: Been running it for a few hours and hashrate is stable at 507 h/s (97.5%).

## xmrig | 2018-10-11T11:07:59+00:00
xmrig-nvidia v2.8.0-rc released https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.8.0-rc

## trasherdk | 2018-10-14T11:35:01+00:00
CPU....: Intel(R) Core(TM) i3-7100 CPU @ 3.90GHz
RAM....: 8 GB RAM DDR4.
OS.....: Windows 10 Pro x64 (Version 10.0.16299.611)
Driver.: Radeon Software Version Radeon Software Version Adrenalin 18.5.1

Version: xmr-stak 2.4.7 c5f0505d
Custom amt.txt config.
HashVault - CN/1

	HASHRATE REPORT - CPU
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |   29.5 |   30.1 |   29.1 |  1 |   31.0 |   31.7 |   30.9 |
	Totals (CPU):    60.5   61.8   60.0 H/s
	-----------------------------------------------------------------
	HASHRATE REPORT - AMD
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |  234.9 |  235.4 |  235.3 |  1 |  236.1 |  235.2 |  235.3 | MSI RX 550 2GB
	|  2 |  238.3 |  237.3 |  237.0 |  3 |  234.5 |  236.9 |  237.0 | MSI RX 550 2GB
	|  4 |  231.3 |  231.0 |  231.0 |  5 |  230.9 |  231.1 |  231.1 | GIGABYTE RX 560 4GB
	|  6 |  236.8 |  237.2 |  237.3 |  7 |  238.1 |  237.9 |  237.3 | MSI RX 550 2GB
	|  8 |  233.9 |  234.3 |  234.0 |  9 |  233.8 |  233.7 |  234.0 | MSI RX 550 2GB
	Totals (AMD):  2348.5 2350.0 2349.3 H/s
	-----------------------------------------------------------------
	Totals (ALL):   2409.0 2411.8 2409.3 H/s
	Highest:  2417.2 H/s
	-----------------------------------------------------------------

Version: xmr-stak 2.5.0 90125127
Default autodetected amd.txt settings.
HashVault - CN/1

	HASHRATE REPORT - CPU
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |   28.4 |   29.0 |   28.8 |  1 |   29.9 |   30.3 |   30.1 |
	Totals (CPU):    58.3   59.2   58.9 H/s
	-----------------------------------------------------------------
	HASHRATE REPORT - AMD
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |  377.1 |  376.6 |  376.0 |  1 |  380.6 |  380.6 |  380.6 |
	|  2 |  426.7 |  426.6 |  423.9 |  3 |  379.6 |  377.9 |  380.6 |
	|  4 |  377.5 |  378.8 |  378.8 |
	Totals (AMD):  1941.5 1940.5 1939.9 H/s
	-----------------------------------------------------------------
	Totals (ALL):   1999.8 1999.7 1998.9 H/s
	Highest:  2011.0 H/s
	-----------------------------------------------------------------

Version: xmr-stak 2.5.0 90125127
Custom amd.txt config. Same as ver. 2.4.7 + onroll: 8
HashVault - CN/1

	HASHRATE REPORT - CPU
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |   29.7 |   29.0 |   30.5 |  1 |   31.3 |   30.4 |   31.7 |
	Totals (CPU):    61.0   59.3   62.1 H/s
	-----------------------------------------------------------------
	HASHRATE REPORT - AMD
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |  234.5 |  235.4 |  235.2 |  1 |  236.8 |  234.9 |  235.2 | MSI RX 550 2GB
	|  2 |  236.9 |  237.2 |  237.2 |  3 |  237.6 |  237.2 |  237.2 | MSI RX 550 2GB
	|  4 |  230.9 |  231.1 |  231.1 |  5 |  231.3 |  231.0 |  231.0 | GIGABYTE RX 560 4GB
	|  6 |  235.6 |  237.2 |  237.4 |  7 |  238.8 |  237.5 |  237.5 | MSI RX 550 2GB
	|  8 |  231.4 |  233.8 |  233.9 |  9 |  235.3 |  233.6 |  233.9 | MSI RX 550 2GB
	Totals (AMD):  2349.0 2348.9 2349.5 H/s
	-----------------------------------------------------------------
	Totals (ALL):   2410.0 2408.3 2411.7 H/s
	Highest:  2417.4 H/s
	-----------------------------------------------------------------

Version: xmr-stak 2.5.0 90125127
Custom amd.txt config. Same as ver. 2.4.7 + onroll: 8
KILL ALL ASICS - CN/2-2

	HASHRATE REPORT - CPU
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |   29.1 |   26.2 |   28.3 |  1 |   30.5 |   27.9 |   29.7 |
	Totals (CPU):    59.6   54.1   58.0 H/s
	-----------------------------------------------------------------
	HASHRATE REPORT - AMD
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |  198.3 |  190.6 |  189.9 |  1 |  192.4 |  191.7 |  189.9 | MSI RX 550 2GB
	|  2 |  198.3 |  193.3 |  192.9 |  3 |  196.2 |  193.4 |  192.9 | MSI RX 550 2GB
	|  4 |  212.3 |  211.4 |  214.0 |  5 |  217.5 |  210.5 |  214.0 | GIGABYTE RX 560 4GB
	|  6 |  189.6 |  188.2 |  187.6 |  7 |  190.0 |  187.8 |  187.6 | MSI RX 550 2GB
	|  8 |  202.2 |  194.9 |  193.3 |  9 |  195.2 |  195.2 |  193.3 | MSI RX 550 2GB
	Totals (AMD):  1992.1 1957.1 1955.3 H/s
	-----------------------------------------------------------------
	Totals (ALL):   2051.7 2011.2 2013.3 H/s
	Highest:  2061.2 H/s
	-----------------------------------------------------------------

amd.txt

RX 550 - 2 x `{ "index" : 0, "intensity" : 432, "worksize" : 16, "affine_to_cpu" : false, "strided_index" : 1, "mem_chunk" : 2, "unroll" : 8, "comp_mode" : true }`,
RX 560 - 2 x `{ "index" : 2, "intensity" : 424, "worksize" : 8, "affine_to_cpu" : false, "strided_index" : 1, "mem_chunk" : 2, "unroll" : 8, "comp_mode" : true }`,


## trasherdk | 2018-10-14T11:55:37+00:00
Just before switching back to CN/1, I copied the report on CN/2, and noticed that "Highest" is close to what I'd expect on CN/1

	
	HASHRATE REPORT - CPU
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |   18.0 |   24.3 |   27.6 |  1 |   20.8 |   26.1 |   28.9 |
	Totals (CPU):    38.8   50.4   56.5 H/s
	-----------------------------------------------------------------
	HASHRATE REPORT - AMD
	| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
	|  0 |  179.3 |  190.6 |  191.6 |  1 |  192.4 |  190.0 |  191.7 |
	|  2 |  192.4 |  192.7 |  194.4 |  3 |  190.0 |  192.6 |  194.4 |
	|  4 |  214.9 |  215.3 |  212.3 |  5 |  222.8 |  216.4 |  212.2 |
	|  6 |  193.1 |  189.7 |  189.8 |  7 |  185.7 |  188.8 |  189.9 |
	|  8 |  199.0 |  195.3 |  194.8 |  9 |  200.5 |  195.0 |  194.8 |
	Totals (AMD):  1970.0 1966.5 1966.0 H/s
	-----------------------------------------------------------------
	Totals (ALL):   2008.8 2016.9 2022.5 H/s
	Highest:  2436.0 H/s
	-----------------------------------------------------------------
	


## psychocrypt | 2018-10-14T11:59:43+00:00
@trasherdk I think you reported your values to the wrong miner. This is a xmrig issue. Maybe you thought you are in https://github.com/fireice-uk/xmr-stak/issues/1851

## trasherdk | 2018-10-14T12:05:16+00:00
You are right. Sorry guys :)

BTW. xmrig is running just fine.

`Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz GenuineIntel GNU/Linux`

    [2018-10-14 13:57:41] accepted (12626/0) diff 7560 (37 ms)
    [2018-10-14 13:57:42] accepted (12627/0) diff 7560 (83 ms)
    [2018-10-14 13:57:49] accepted (12628/0) diff 7560 (37 ms)
    [2018-10-14 13:57:50] speed 10s/60s/15m 260.5 261.2 259.7 H/s max 263.4 H/s


## Bathmat | 2018-10-14T18:13:59+00:00
Has anyone tested cn/2 (cnv8) with Vega and Blockchain drivers? I'm getting 1975 with cn/1 easily, but the best I can get with cn/2 is 1200 h/s (600 per thread). It's a mixed rig, and when I tried adrenaline 18.5.1, my RXs didn't want to switch to compute mode. I'll have to try again later, but just wanted to see if anyone had gotten blockchain drivers to work successfully.

# Action History
- Created by: xmrig | 2018-09-13T09:06:56+00:00
- Closed at: 2018-11-05T14:17:11+00:00
