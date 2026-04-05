---
title: xmrig-6.16.1-linux-static-x64 Segmentation fault
source_url: https://github.com/xmrig/xmrig/issues/2750
author: Csordi
assignees: []
labels:
- bug
created_at: '2021-11-29T16:46:43+00:00'
updated_at: '2021-12-19T15:05:46+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:05:46+00:00'
---

# Original Description
```
 * ABOUT        XMRig/6.16.1 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       1.4/15.6 GB (9%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
 * MOTHERBOARD  Micro-Star International Co., Ltd. - X570-A PRO (MS-7C37)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://r-pool.net:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:8080
[2021-11-29 16:31:46.466]  net      use pool r-pool.net:3008  167.86.115.224
[2021-11-29 16:31:46.466]  net      new job from r-pool.net:3008 diff 16384 algo ghostrider height 194979
[2021-11-29 16:31:46.469]  msr      register values for "ryzen_19h" preset have been set successfully (3 ms)
Segmentation fault
```




Additional info:
Linux version 5.4.0-90-generic (buildd@lgw01-amd64-054) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021

Kernel Log:
Nov 29 16:31:46 miner-1 kernel: [93091.795060] traps: xmrig[4869] general protection fault ip:7f67112fdd96 sp:7f670f0285e0 error:0 in xmrig[7f6711118000+4c0000]


# Discussion History
## KaruroChori | 2021-11-29T16:56:13+00:00
The problem persists after compiling it manually. The architecture on which it has been tested does support the extended instruction set as well.

## SChernykh | 2021-11-29T17:25:17+00:00
I've tested this exact binary on two machines (Ryzen 5 5600X and Ryzen 5 3600, both Ubuntu 20.04) and it works for me. I'm not sure what's different with your setup. Maybe AVX2 was somehow disabled programmatically in your Ubuntu installation?

## Csordi | 2021-11-29T17:31:13+00:00
```
 cat /proc/cpuinfo
processor       : 0
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 33
model name      : AMD Ryzen 9 5950X 16-Core Processor
stepping        : 0
microcode       : 0xa201009
cpu MHz         : 3900.136
cache size      : 512 KB
physical id     : 0
siblings        : 32
core id         : 0
cpu cores       : 16
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 16
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca
bugs            : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
bogomips        : 7800.27
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]
```


## SChernykh | 2021-11-29T17:36:17+00:00
I don't see anything wrong with CPU flags. Does v6.16.0 work for you?

## Csordi | 2021-11-29T17:38:38+00:00
xmrig-6.16.0-linux-x64 works great on this machine

## KaruroChori | 2021-11-29T17:39:20+00:00
In my case the most recent not-static version is working. The one I compiled or the one tagged as static do not and result in a segmentation faul like shown.

## SChernykh | 2021-11-29T17:44:10+00:00
@Csordi can you try other v6.16.1 Linux builds on your machine?

## Csordi | 2021-11-29T17:44:47+00:00
Yup I can try it

## Csordi | 2021-11-29T17:49:15+00:00
The non static 6.16.1 works fine.

```
 * ABOUT        XMRig/6.16.1 gcc/5.4.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       1.4/15.6 GB (9%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
 * MOTHERBOARD  Micro-Star International Co., Ltd. - X570-A PRO (MS-7C37)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://r-pool.net:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:8080
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-29 17:47:13.595]  net      use pool r-pool.net:3008  75.119.130.196
[2021-11-29 17:47:13.595]  net      new job from r-pool.net:3008 diff 16384 algo ghostrider height 195014
[2021-11-29 17:47:13.598]  msr      register values for "ryzen_19h" preset have been set successfully (3 ms)
[2021-11-29 17:47:14.820]  cpu      use profile  ghostrider  (16 threads) scratchpad 2048 KB
[2021-11-29 17:47:14.820]  net      new job from r-pool.net:3008 diff 16384 algo ghostrider height 195015
[2021-11-29 17:47:14.926]  cpu      GhostRider algo 1: cn/lite (1 MB)
```

## SChernykh | 2021-11-29T17:54:50+00:00
This one was compiled with GCC 5.4 which doesn't support VAES instructions. Can you try xmrig-6.16.1-focal-x64.tar.gz instead?

## Csordi | 2021-11-29T18:01:51+00:00
The xmrig-6.16.1-focal-x64 has the same Segmentation fault problem at least on this PC

```
 * ABOUT        XMRig/6.16.1 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       1.4/15.6 GB (9%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
 * MOTHERBOARD  Micro-Star International Co., Ltd. - X570-A PRO (MS-7C37)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://r-pool.net:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:8080
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-29 17:58:21.980]  net      use pool r-pool.net:3008  75.119.130.196
[2021-11-29 17:58:21.980]  net      new job from r-pool.net:3008 diff 16384 algo ghostrider height 195023
[2021-11-29 17:58:21.983]  msr      register values for "ryzen_19h" preset have been set successfully (3 ms)
Segmentation fault
```

## SChernykh | 2021-11-29T20:11:13+00:00
@Csordi @KaruroChori can you build with https://github.com/xmrig/xmrig/pull/2751 and check if it works?

## KaruroChori | 2021-11-29T20:40:59+00:00
I can confirm it is working now.

## Csordi | 2021-11-29T21:52:26+00:00
Yup... It's working!

```
 * ABOUT        XMRig/6.16.1-dev gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       2.2/15.6 GB (14%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2667 MHz KF2666C13D4/8GX
 * MOTHERBOARD  Micro-Star International Co., Ltd. - X570-A PRO (MS-7C37)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://r-pool.net:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:8080
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-29 21:50:26.733]  net      use pool r-pool.net:3008  75.119.130.196
[2021-11-29 21:50:26.733]  net      new job from r-pool.net:3008 diff 16384 algo ghostrider height 195145
[2021-11-29 21:50:26.735]  msr      register values for "ryzen_19h" preset have been set successfully (2 ms)
[2021-11-29 21:50:27.935]  cpu      use profile  ghostrider  (16 threads) scratchpad 2048 KB
[2021-11-29 21:50:28.041]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2021-11-29 21:50:28.041]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-11-29 21:50:28.041]  cpu      GhostRider algo 3: cn/lite (1 MB)
[2021-11-29 21:50:28.064]  cpu      READY threads 32/32 (128) huge pages 100% 128/128 memory 262144 KB (129 ms)
```

## acermez | 2021-11-29T22:27:12+00:00
@SChernykh Thank you so much for the fix, I can confirm that I had the same issue above explained by @Csordi , I'm using AMD Ryzen 5950X with Ubuntu 21.10, I tried everything 6.16.1 (even creating from source), didn't work, only building from your fix (dev branch) is working for me. I can also confirm that 6.16.0 was working fine too.

## MallevGit | 2021-11-30T06:12:15+00:00
I can confirm building from dev branch fixed segmentation fault for me too on Ubuntu 21.10. 
Many thanks!
 
 * ABOUT        XMRig/6.16.2-dev gcc/11.2.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1l hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       0.8/31.3 GB (3%)
                DIMM 0: <empty>
                DIMM_A1: 16 GB DDR4 @ 3200 MHz CMK32GX4M2E3200C16
                DIMM 0: <empty>
                DIMM_B1: 16 GB DDR4 @ 3200 MHz CMK32GX4M2E3200C16
 * MOTHERBOARD  Gigabyte Technology Co., Ltd. - B450 I AORUS PRO WIFI-CF
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      us.flockpool.com:5555 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled


## acermez | 2021-11-30T20:31:36+00:00
@Csordi, @MallevGit, @KaruroChori  Guys, since we have the same CPU (Ryzen 9 5950x) and the same Distro, can we share data about hashrates and CPU clock/overclocking? , I'm doing average 4.1kh at 4.5GHZ with 1.36 vols, the temps are between 62c-72c using a 360mm RAD (Cooler Master AIO), I was able to reach higher average (4.4kh) using another miner but the system was running hotter (reaching 82c sometimes), and I think xmrig is more stable and obviously less fees 👍 
(just to clarify, by average, I mean pool average not the miner reported average, I'm using flockpool...). Thanks again to the dev for the hard work, keep it up!

## KaruroChori | 2021-11-30T21:22:33+00:00
I do not believe this is the proper place for such discussion. This was an issue for a bug report.

## acermez | 2021-11-30T21:49:09+00:00
@KaruroChori  Yeah, you are right, happy to move the above to a discussion section if there is any under this repo.

# Action History
- Created by: Csordi | 2021-11-29T16:46:43+00:00
- Closed at: 2021-12-19T15:05:46+00:00
