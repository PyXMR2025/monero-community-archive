---
title: Old CPU Optimization
source_url: https://github.com/xmrig/xmrig/issues/3133
author: ghost
assignees: []
labels: []
created_at: '2022-10-06T12:48:06+00:00'
updated_at: '2025-06-18T22:51:59+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:51:59+00:00'
---

# Original Description
I am doing some experimenting with old computers I have lying around and need some help optimizing the configs for two ancient processors. I know they aren't profitable, just curious how far I can push them (within reason). Any advice is appreciated!

**Computer #1 ( Dell SN:CXLP741)**

Currently getting 0.21-0.32H/s

_#cat /proc/cpuinfo_
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 15
model		: 2
model name	: Intel(R) Pentium(R) 4 CPU 2.66GHz
stepping	: 9
microcode	: 0x17
cpu MHz		: 2659.812
cache size	: 512 KB
physical id	: 0
siblings	: 1
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fdiv_bug	: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 2
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe pebs bts cpuid cid xtpr
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit mmio_unknown
bogomips	: 5321.27
clflush size	: 64
cache_alignment	: 128
address sizes	: 36 bits physical, 32 bits virtual
power management:

_#config.json_
"randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "slow",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": false,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "argon2-impl": null,
        "argon2": [-1],
        "cn": [-1],
        "cn-heavy": [-1],
        "cn-lite": [-1],
        "cn-pico": [-1],
        "cn/upx2": [-1],
        "ghostrider": [-1],
        "rx": [-1],
        "rx/wow": [-1],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },

_#xmrig startup output_
* ABOUT        XMRig/6.18.0 gcc/11.2.1
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1q hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU           (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 1C/1T NUMA:1
 * MEMORY       0.2/1.5 GB (16%)
                DIMM_1: 1 GB SDRAM @ 333 MHz (null)
                DIMM_2: 0 GB SDRAM @ 333 MHz (null)
 * MOTHERBOARD  Dell Computer Corp. - 0X1105
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
cpu      use argon2 implementation default
randomx  init dataset algo rx/0 (1 threads) seed xxx...
randomx  not enough memory for RandomX dataset
randomx  failed to allocate RandomX dataset, switching to slow mode


**Computer #2 (HP SN:5CB132362P)**

Currently getting 11.88-11.99H/s

_#cat /proc/cpuinfo_
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 20
model		: 1
model name	: AMD E-350 Processor
stepping	: 0
microcode	: 0x5000029
cpu MHz		: 1596.544
cache size	: 512 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 6
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni monitor ssse3 cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch ibs skinit wdt hw_pstate vmmcall arat npt lbrv svm_lock nrip_save pausefilter
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 3193.09
TLB size	: 1024 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management: ts ttp tm stc 100mhzsteps hwpstate

processor	: 1
vendor_id	: AuthenticAMD
cpu family	: 20
model		: 1
model name	: AMD E-350 Processor
stepping	: 0
microcode	: 0x5000029
cpu MHz		: 799.939
cache size	: 512 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 6
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni monitor ssse3 cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch ibs skinit wdt hw_pstate vmmcall arat npt lbrv svm_lock nrip_save pausefilter
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 3193.09
TLB size	: 1024 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management: ts ttp tm stc 100mhzsteps hwpstate

_#config.json_
"randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "light",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": null,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1],
        "cn": [
            [1, -1]
        ],
        "cn-heavy": [
            [1, -1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1]
        ],
        "ghostrider": [
            [8, -1]
        ],
        "rx": [-1],
        "rx/wow": [0, 1],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },

_#xmrig startup output_
* ABOUT        XMRig/6.18.0 gcc/11.2.0
 * LIBS         libuv/1.43.0 OpenSSL/3.0.2 hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD E-350 Processor (1) 64-bit -AES
                L2:1.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       0.6/2.5 GB (23%)
                Top-Slot 1(top): 1 GB DDR3 @ 533 MHz AD73I1A0873EU     
                Top-Slot 2(under): 2 GB DDR3 @ 533 MHz M471B5773DH0-CH9  
 * MOTHERBOARD  Hewlett-Packard - 3577
 * ASSEMBLY     auto:none
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
cpu      use argon2 implementation SSSE3
randomx  init dataset algo rx/0 (2 threads) seed xxx...
randomx  fast RandomX mode disabled by config
randomx  failed to allocate RandomX dataset, switching to slow mode

# Discussion History
## Spudz76 | 2022-10-06T18:22:25+00:00
Needs ~2.6GB of memory free to avoid slow-mode which is... very very slow.

Needs 2MB of cache per thread, you have 512K and 1M.  32-bit will always be terrible, if the P4 will run in a 64-bit mode that might be an improvement.

Otherwise the CPU and its memory controller will be constantly wasting time shifting data in and out of the workspace, more than doing any real mining work.

## ghost | 2022-10-07T05:06:58+00:00
> Needs ~2.6GB of memory free to avoid slow-mode which is... very very slow.
> 
> Needs 2MB of cache per thread, you have 512K and 1M. 32-bit will always be terrible, if the P4 will run in a 64-bit mode that might be an improvement.
> 
> Otherwise the CPU and its memory controller will be constantly wasting time shifting data in and out of the workspace, more than doing any real mining work.

I can likely add more memory, given I can find it for these ancient machines. Sadly the Intel Pentium 4 is 32 bit.

Are there any changes I can make to the config that might improve the performance? I have been unable to get the AMD E-350 to run unless it is in slow mode. Any ideas?

## Spudz76 | 2022-10-07T17:46:37+00:00
4GB (stripped console linux, not GUI) or 8GB would fix the slow mode problem. Not sure how much faster it would go though considering the lack of cache.

## 2008dmx | 2023-01-25T07:04:15+00:00
> > Needs ~2.6GB of memory free to avoid slow-mode which is... very very slow.
> > Needs 2MB of cache per thread, you have 512K and 1M. 32-bit will always be terrible, if the P4 will run in a 64-bit mode that might be an improvement.
> > Otherwise the CPU and its memory controller will be constantly wasting time shifting data in and out of the workspace, more than doing any real mining work.
> 
> I can likely add more memory, given I can find it for these ancient machines. Sadly the Intel Pentium 4 is 32 bit.
> 
> Are there any changes I can make to the config that might improve the performance? I have been unable to get the AMD E-350 to run unless it is in slow mode. Any ideas?

1) Take this junk to the trash!
2) Buy at least ryzen9 (minimum 5900X) with 32GB micron e-die (or more expensive samsung b-die)
3) Learn popular compilers (eg Intel IoTKit, mvc, gcc)
Decide what suits you best!!
4) For linux, clang is the most optimal IMHO
5) Remember that the smaller the code size, the faster it works, ideally you need an executable for each algorithm or coin
6) Do useful work for each owner of the zen3, share the result!!

P.S. I have ryzen9 5950X and it is slow, only 20kh on RandomX

## MrHyplex9511 | 2025-01-12T17:54:05+00:00
> > > Needs ~2.6GB of memory free to avoid slow-mode which is... very very slow.
> > > Needs 2MB of cache per thread, you have 512K and 1M. 32-bit will always be terrible, if the P4 will run in a 64-bit mode that might be an improvement.
> > > Otherwise the CPU and its memory controller will be constantly wasting time shifting data in and out of the workspace, more than doing any real mining work.
> > 
> > 
> > I can likely add more memory, given I can find it for these ancient machines. Sadly the Intel Pentium 4 is 32 bit.
> > Are there any changes I can make to the config that might improve the performance? I have been unable to get the AMD E-350 to run unless it is in slow mode. Any ideas?
> 
> 1. Take this junk to the trash!
> 2. Buy at least ryzen9 (minimum 5900X) with 32GB micron e-die (or more expensive samsung b-die)
> 3. Learn popular compilers (eg Intel IoTKit, mvc, gcc)
>    Decide what suits you best!!
> 4. For linux, clang is the most optimal IMHO
> 5. Remember that the smaller the code size, the faster it works, ideally you need an executable for each algorithm or coin
> 6. Do useful work for each owner of the zen3, share the result!!
> 
> P.S. I have ryzen9 5950X and it is slow, only 20kh on RandomX

dude let blud do his thing. we want to fix his problem not to make it so that the problem had never existed creating a branch in the sacred timeline which will cause more issues

# Action History
- Created by: ghost | 2022-10-06T12:48:06+00:00
- Closed at: 2025-06-18T22:51:59+00:00
