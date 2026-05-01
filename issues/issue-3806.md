---
title: EPYC 7742 (64C128T) 8x4GB 2400 MT/s Ram ~ 25% hashrate regression with rx/2
source_url: https://github.com/xmrig/xmrig/issues/3806
author: Motophan
assignees: []
labels: []
created_at: '2026-04-28T08:55:54+00:00'
updated_at: '2026-05-01T09:41:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I understand the rx/2 was made to slow down the JBOC (just a bunch of CPUs) bitmain hashboards, and they are expected to lose 30% of their hashrate, but when I did a bench for rx/2 I lost about 25%

Windows 11

rx/0 -> 45KH/s
rx/2 -> 34KH/s



# Discussion History
## SChernykh | 2026-04-28T09:11:27+00:00
This is a Zen 2 CPU. Other Zen 2 CPUs we tested didn't slow down that much: https://github.com/tevador/RandomX/blob/master/doc/design_v2.md#ryzen-9-3950x-zen-2--131w

Maybe your EPYC's power limit kicks in, because rx/2 does more than 1.5x computations per hash. Reminder that rx/2 is much heavier, so you can't compare hashrates directly. With 34 kh/s vs 45 kh/s, your CPU still does ~15% more RandomX and AES instructions per second.

Another reminder is that rx/2 was tuned for more modern CPUs: https://github.com/tevador/RandomX/blob/master/doc/design_v2.md#3-program-size-increase-from-256-to-384 so your result is expected.

## Motophan | 2026-04-29T06:15:39+00:00
Fair, but hear me out... I use 4 numa nodes to keep as much free bandwidth on the cores as possible. 

The regression is much more than a dual ccd zen2. Could the algo be getting stalled on something traversing the cpu interconnect? I tried single numa but regression is still there much more than a 3950x. btop would tell me I was hitting 220w on both v1 and v2, so I assume I was power limited. I used cpufreq to set govener to powersave so it wouldnt go above 1.5GHz all cores but still have huge differences in hashrate. 


I get what you are saying that this cpu is ~ 10 years old, so regression is expected. I am just saying maybe there is more regression being amplified because I have effectively 4 zen2 cpu's glued together. Like (I am not a programmer) could the HW AES part of the cpu have trouble dumping AES hashes through the cpu interconnect? Could it try to do AES ondie on each numa and see if its faster? 

If operating as designed and amplification of regression is expected (because its compounding limits due to duplicated cores) you can close the issue. 

I can compile and run a dev version if it helps. I have no confidential data on the epyc, I can just strait up give you ssh if you want acsess to a box. Its a dedicated mining rig. Can do windows instead of linux but I cant expose rdp over the internet easily. 

## SChernykh | 2026-04-29T07:17:59+00:00
No, it's not AES. Zen2 handles AES instructions just fine. Maybe your CPU clocks drop down a lot on v2 because it's power limited? Can you check it?

## Motophan | 2026-04-29T07:50:56+00:00
Yes, give me a day. Thanks man. 

## Motophan | 2026-04-30T08:13:08+00:00
Using a wattmeter at the wall 
```
sudo cpupower frequency-info
analyzing CPU 3:
  driver: acpi-cpufreq
  CPUs which run at the same hardware frequency: 3
  CPUs which need to have their frequency coordinated by software: 3
  maximum transition latency:  Cannot determine or is not supported.
  hardware limits: 1.50 GHz - 3.42 GHz
  available frequency steps:  2.25 GHz, 2.00 GHz, 1.50 GHz
  available cpufreq governors: conservative ondemand userspace powersave performance schedutil
  current policy: frequency should be within 1.50 GHz and 2.25 GHz.
                  The governor "schedutil" may decide which speed to use
                  within this range.
  current CPU frequency: 2.25 GHz (asserted by call to hardware)
  boost state support:
    Supported: yes
    Active: yes
    Boost States: 0
    Total States: 3
    Pstate-P0:  2250MHz
    Pstate-P1:  2000MHz
    Pstate-P2:  1500MHz
```

Forcing 1500MHz

<details>
<summary>30225.2 h/s @ 193.7w rx/0</summary>
```
sudo xmrig --benchmark=1M -a rx/0
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       1.6/31.2 GB (5%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:08:27.424]  bench    start benchmark hashes 1M algo rx/0
[2026-04-30 00:08:27.424]  cpu      use argon2 implementation AVX2
[2026-04-30 00:08:27.435]  msr      register values for "ryzen_17h" preset have been set successfully (11 ms)
[2026-04-30 00:08:27.435]  randomx  init datasets algo rx/0 (128 threads) seed 0000000000000000...
[2026-04-30 00:08:27.987]  randomx  #2 allocated 2080 MB huge pages 100% (551 ms)
[2026-04-30 00:08:28.265]  randomx  #0 allocated 2080 MB huge pages 100% (829 ms)
[2026-04-30 00:08:28.542]  randomx  #1 allocated 2080 MB huge pages 100% (1106 ms)
[2026-04-30 00:08:28.821]  randomx  #3 allocated 2080 MB huge pages 100% (1385 ms)
[2026-04-30 00:08:28.891]  randomx  #0 allocated  256 MB huge pages 100% +JIT (70 ms)
[2026-04-30 00:08:28.891]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (1456 ms)
[2026-04-30 00:08:30.543]  randomx  #0 dataset ready (1652 ms)
[2026-04-30 00:08:30.821]  randomx  #1 dataset ready (277 ms)
[2026-04-30 00:08:30.826]  randomx  #3 dataset ready (282 ms)
[2026-04-30 00:08:30.829]  randomx  #2 dataset ready (285 ms)
[2026-04-30 00:08:30.830]  cpu      use profile  rx  (128 threads) scratchpad 2048 KB
[2026-04-30 00:08:30.952]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (122 ms)
[2026-04-30 00:09:04.112]  bench    benchmark finished in 33.244 seconds (30080.6 h/s) hash sum = 898B6E0431C28A6B
[2026-04-30 00:09:04.112]  bench    press Ctrl+C to exit
[2026-04-30 00:09:04.415]  cpu      stopped (10 ms)
[2026-04-30 00:09:33.305]  signal   Ctrl+C received, exiting
```
</details>

<details>
<summary>23676.5 h/s @ 194w rx/2</summary>
```
sudo xmrig --benchmark=1M -a rx/2
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       10.2/31.2 GB (33%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:09:45.912]  bench    start benchmark hashes 1M algo rx/2
[2026-04-30 00:09:45.912]  cpu      use argon2 implementation AVX2
[2026-04-30 00:09:45.922]  msr      register values for "ryzen_17h" preset have been set successfully (10 ms)
[2026-04-30 00:09:45.922]  randomx  init datasets algo rx/2 (128 threads) seed 0000000000000000...
[2026-04-30 00:09:46.201]  randomx  #0 allocated 2080 MB huge pages 100% (279 ms)
[2026-04-30 00:09:47.036]  randomx  #3 allocated 2080 MB huge pages 100% (1113 ms)
[2026-04-30 00:09:47.037]  randomx  #2 allocated 2080 MB huge pages 100% (1114 ms)
[2026-04-30 00:09:47.037]  randomx  #1 allocated 2080 MB huge pages 100% (1114 ms)
[2026-04-30 00:09:47.073]  randomx  #0 allocated  256 MB huge pages 100% +JIT (36 ms)
[2026-04-30 00:09:47.073]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (1151 ms)
[2026-04-30 00:09:48.723]  randomx  #0 dataset ready (1650 ms)
[2026-04-30 00:09:48.993]  randomx  #2 dataset ready (270 ms)
[2026-04-30 00:09:48.996]  randomx  #1 dataset ready (273 ms)
[2026-04-30 00:09:48.999]  randomx  #3 dataset ready (275 ms)
[2026-04-30 00:09:49.000]  cpu      use profile  rx  (128 threads) scratchpad 2048 KB
[2026-04-30 00:09:49.123]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (123 ms)
[2026-04-30 00:10:31.306]  bench    benchmark finished in 42.236 seconds (23676.5 h/s) hash sum = 88D6B8FB70CD479D
[2026-04-30 00:10:31.306]  bench    press Ctrl+C to exit
[2026-04-30 00:10:31.603]  cpu      stopped (10 ms)
```
</details>

Forcing max cpu max power 
<details>
<summary>42627.6 h/s 301w rx/0</summary>
```
sudo xmrig --benchmark=1M -a rx/0
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       10.7/31.2 GB (34%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:26:18.981]  bench    start benchmark hashes 1M algo rx/0
[2026-04-30 00:26:18.981]  cpu      use argon2 implementation AVX2
[2026-04-30 00:26:18.988]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2026-04-30 00:26:18.988]  randomx  init datasets algo rx/0 (128 threads) seed 0000000000000000...
[2026-04-30 00:26:19.227]  randomx  #2 allocated 2080 MB huge pages 100% (238 ms)
[2026-04-30 00:26:19.933]  randomx  #3 allocated 2080 MB huge pages 100% (945 ms)
[2026-04-30 00:26:19.933]  randomx  #0 allocated 2080 MB huge pages 100% (945 ms)
[2026-04-30 00:26:19.933]  randomx  #1 allocated 2080 MB huge pages 100% (945 ms)
[2026-04-30 00:26:19.964]  randomx  #0 allocated  256 MB huge pages 100% +JIT (31 ms)
[2026-04-30 00:26:19.964]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (976 ms)
[2026-04-30 00:26:21.355]  randomx  #0 dataset ready (1391 ms)
[2026-04-30 00:26:21.588]  randomx  #2 dataset ready (232 ms)
[2026-04-30 00:26:21.589]  randomx  #1 dataset ready (234 ms)
[2026-04-30 00:26:21.603]  randomx  #3 dataset ready (247 ms)
[2026-04-30 00:26:21.603]  cpu      use profile  rx  (128 threads) scratchpad 2048 KB
[2026-04-30 00:26:21.709]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (105 ms)
[2026-04-30 00:26:45.102]  bench    benchmark finished in 23.459 seconds (42627.6 h/s) hash sum = 898B6E0431C28A6B
[2026-04-30 00:26:45.102]  bench    press Ctrl+C to exit
[2026-04-30 00:26:45.158]  cpu      stopped (6 ms)
```

</details>

<details>
<summary>35685.0 h/s 299w rx/2</summary>
```
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       10.3/31.2 GB (33%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:27:20.754]  bench    start benchmark hashes 1M algo rx/2
[2026-04-30 00:27:20.754]  cpu      use argon2 implementation AVX2
[2026-04-30 00:27:20.761]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2026-04-30 00:27:20.761]  randomx  init datasets algo rx/2 (128 threads) seed 0000000000000000...
[2026-04-30 00:27:21.000]  randomx  #3 allocated 2080 MB huge pages 100% (238 ms)
[2026-04-30 00:27:21.710]  randomx  #1 allocated 2080 MB huge pages 100% (949 ms)
[2026-04-30 00:27:21.710]  randomx  #0 allocated 2080 MB huge pages 100% (949 ms)
[2026-04-30 00:27:21.710]  randomx  #2 allocated 2080 MB huge pages 100% (949 ms)
[2026-04-30 00:27:21.741]  randomx  #0 allocated  256 MB huge pages 100% +JIT (31 ms)
[2026-04-30 00:27:21.741]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (980 ms)
[2026-04-30 00:27:23.123]  randomx  #0 dataset ready (1381 ms)
[2026-04-30 00:27:23.348]  randomx  #3 dataset ready (224 ms)
[2026-04-30 00:27:23.458]  randomx  #1 dataset ready (335 ms)
[2026-04-30 00:27:23.458]  randomx  #2 dataset ready (334 ms)
[2026-04-30 00:27:23.458]  cpu      use profile  rx  (128 threads) scratchpad 2048 KB
[2026-04-30 00:27:23.566]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (108 ms)
[2026-04-30 00:27:51.522]  bench    benchmark finished in 28.023 seconds (35685.0 h/s) hash sum = 88D6B8FB70CD479D
[2026-04-30 00:27:51.522]  bench    press Ctrl+C to exit
[2026-04-30 00:27:52.024]  cpu      stopped (6 ms)
```
</details>

The only way I know how to check cpu freq is using sudo cpupower frequency-info and it shows either 1.5Ghz (powersave) or 2.25Ghz (performance)

Its def not hitting powerlimit when I limit freq to 1.5, since btop says 161w cpu, but it is hitting powerlimit on performance (expected) and btop says 210w both rx/0 and rx/2

## Motophan | 2026-04-30T08:34:32+00:00
```
sudo xmrig --benchmark=1M --threads 64 -a rx/2
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       18.5/31.2 GB (59%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:31:13.725]  bench    start benchmark hashes 1M algo rx/2
[2026-04-30 00:31:13.725]  cpu      use argon2 implementation AVX2
[2026-04-30 00:31:13.732]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2026-04-30 00:31:13.732]  randomx  init datasets algo rx/2 (128 threads) seed 0000000000000000...
[2026-04-30 00:31:13.965]  randomx  #1 allocated 2080 MB huge pages 100% (233 ms)
[2026-04-30 00:31:14.673]  randomx  #3 allocated 2080 MB huge pages 100% (940 ms)
[2026-04-30 00:31:14.674]  randomx  #2 allocated 2080 MB huge pages 100% (941 ms)
[2026-04-30 00:31:14.674]  randomx  #0 allocated 2080 MB huge pages 100% (942 ms)
[2026-04-30 00:31:14.705]  randomx  #0 allocated  256 MB huge pages 100% +JIT (30 ms)
[2026-04-30 00:31:14.705]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (972 ms)
[2026-04-30 00:31:16.104]  randomx  #0 dataset ready (1399 ms)
[2026-04-30 00:31:16.353]  randomx  #1 dataset ready (248 ms)
[2026-04-30 00:31:16.355]  randomx  #2 dataset ready (251 ms)
[2026-04-30 00:31:16.358]  randomx  #3 dataset ready (254 ms)
[2026-04-30 00:31:16.358]  cpu      use profile  *  (64 threads) scratchpad 2048 KB
[2026-04-30 00:31:16.435]  cpu      READY threads 64/64 (64) huge pages 100% 64/64 memory 131072 KB (77 ms)
[2026-04-30 00:32:04.493]  bench    benchmark finished in 48.106 seconds (20787.4 h/s) hash sum = 88D6B8FB70CD479D
[2026-04-30 00:32:04.493]  bench    press Ctrl+C to exit
[2026-04-30 00:32:04.910]  cpu      stopped (3 ms)
[2026-04-30 00:32:31.747]  signal   Ctrl+C received, exiting
```

```
~ gentoo@epyc-cacheyos 1m 18s
❯ sudo xmrig --benchmark=1M --threads 64 -a rx/0
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       18.6/31.2 GB (59%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:32:37.920]  bench    start benchmark hashes 1M algo rx/0
[2026-04-30 00:32:37.920]  cpu      use argon2 implementation AVX2
[2026-04-30 00:32:37.927]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2026-04-30 00:32:37.927]  randomx  init datasets algo rx/0 (128 threads) seed 0000000000000000...
[2026-04-30 00:32:38.165]  randomx  #0 allocated 2080 MB huge pages 100% (238 ms)
[2026-04-30 00:32:38.880]  randomx  #3 allocated 2080 MB huge pages 100% (952 ms)
[2026-04-30 00:32:38.880]  randomx  #1 allocated 2080 MB huge pages 100% (953 ms)
[2026-04-30 00:32:38.880]  randomx  #2 allocated 2080 MB huge pages 100% (953 ms)
[2026-04-30 00:32:38.911]  randomx  #0 allocated  256 MB huge pages 100% +JIT (31 ms)
[2026-04-30 00:32:38.911]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (984 ms)
[2026-04-30 00:32:40.314]  randomx  #0 dataset ready (1402 ms)
[2026-04-30 00:32:40.529]  randomx  #3 dataset ready (214 ms)
[2026-04-30 00:32:40.561]  randomx  #1 dataset ready (248 ms)
[2026-04-30 00:32:40.564]  randomx  #2 dataset ready (249 ms)
[2026-04-30 00:32:40.564]  cpu      use profile  *  (64 threads) scratchpad 2048 KB
[2026-04-30 00:32:40.637]  cpu      READY threads 64/64 (64) huge pages 100% 64/64 memory 131072 KB (73 ms)
[2026-04-30 00:33:28.304]  bench    benchmark finished in 47.714 seconds (20958.2 h/s) hash sum = 898B6E0431C28A6B
[2026-04-30 00:33:28.304]  bench    press Ctrl+C to exit
[2026-04-30 00:33:28.603]  cpu      stopped (3 ms)

```

if I use half the threads though I get the same hashrate.... maybe i am power limited after all? 


weird, if I use --threads 128 I still get 20KH/s but if I dont touch threads it gets 35/43KH/s. 

```
sudo xmrig --benchmark=1M  --threads 128 -a rx/0
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       18.5/31.2 GB (59%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:42:26.619]  bench    start benchmark hashes 1M algo rx/0
[2026-04-30 00:42:26.619]  cpu      use argon2 implementation AVX2
[2026-04-30 00:42:26.626]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2026-04-30 00:42:26.626]  randomx  init datasets algo rx/0 (128 threads) seed 0000000000000000...
[2026-04-30 00:42:26.861]  randomx  #3 allocated 2080 MB huge pages 100% (234 ms)
[2026-04-30 00:42:27.563]  randomx  #2 allocated 2080 MB huge pages 100% (936 ms)
[2026-04-30 00:42:27.564]  randomx  #0 allocated 2080 MB huge pages 100% (937 ms)
[2026-04-30 00:42:27.564]  randomx  #1 allocated 2080 MB huge pages 100% (937 ms)
[2026-04-30 00:42:27.595]  randomx  #0 allocated  256 MB huge pages 100% +JIT (30 ms)
[2026-04-30 00:42:27.595]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (968 ms)
[2026-04-30 00:42:28.961]  randomx  #0 dataset ready (1367 ms)
[2026-04-30 00:42:29.200]  randomx  #1 dataset ready (239 ms)
[2026-04-30 00:42:29.203]  randomx  #2 dataset ready (242 ms)
[2026-04-30 00:42:29.306]  randomx  #3 dataset ready (344 ms)
[2026-04-30 00:42:29.306]  cpu      use profile  *  (128 threads) scratchpad 2048 KB
[2026-04-30 00:42:29.750]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (443 ms)
[2026-04-30 00:43:21.576]  bench    benchmark finished in 52.211 seconds (19153.1 h/s) hash sum = 898B6E0431C28A6B
[2026-04-30 00:43:21.577]  bench    press Ctrl+C to exit
[2026-04-30 00:43:21.933]  cpu      stopped (5 ms)
```
 ```
sudo xmrig --benchmark=1M  --threads 128 -a rx/2
 * ABOUT        XMRig/6.26.0 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.6.1 hwloc/2.13.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES
                L2:32.0 MB L3:256.0 MB 64C/128T NUMA:4
 * MEMORY       18.5/31.2 GB (59%)
                DIMM_A0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_B0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_C0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_D0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_E0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_F0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_G0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
                DIMM_H0: 4 GB DDR4 @ 2933 MHz 9ASF51272PZ-2G3B1
 * MOTHERBOARD  HUANANZHI - H12D-8D
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-04-30 00:41:13.006]  bench    start benchmark hashes 1M algo rx/2
[2026-04-30 00:41:13.006]  cpu      use argon2 implementation AVX2
[2026-04-30 00:41:13.013]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2026-04-30 00:41:13.013]  randomx  init datasets algo rx/2 (128 threads) seed 0000000000000000...
[2026-04-30 00:41:13.248]  randomx  #3 allocated 2080 MB huge pages 100% (235 ms)
[2026-04-30 00:41:13.952]  randomx  #2 allocated 2080 MB huge pages 100% (939 ms)
[2026-04-30 00:41:13.952]  randomx  #1 allocated 2080 MB huge pages 100% (939 ms)
[2026-04-30 00:41:13.953]  randomx  #0 allocated 2080 MB huge pages 100% (939 ms)
[2026-04-30 00:41:13.983]  randomx  #0 allocated  256 MB huge pages 100% +JIT (30 ms)
[2026-04-30 00:41:13.984]  randomx  -- allocated 8576 MB huge pages 100% 4288/4288 (971 ms)
[2026-04-30 00:41:15.388]  randomx  #0 dataset ready (1404 ms)
[2026-04-30 00:41:15.597]  randomx  #3 dataset ready (209 ms)
[2026-04-30 00:41:15.665]  randomx  #1 dataset ready (278 ms)
[2026-04-30 00:41:15.669]  randomx  #2 dataset ready (281 ms)
[2026-04-30 00:41:15.669]  cpu      use profile  *  (128 threads) scratchpad 2048 KB
[2026-04-30 00:41:15.925]  cpu      READY threads 128/128 (128) huge pages 100% 128/128 memory 262144 KB (255 ms)
[2026-04-30 00:42:07.878]  bench    benchmark finished in 52.154 seconds (19174.0 h/s) hash sum = 88D6B8FB70CD479D
[2026-04-30 00:42:07.878]  bench    press Ctrl+C to exit
[2026-04-30 00:42:08.342]  cpu      stopped (7 ms)
[2026-04-30 00:42:23.587]  signal   Ctrl+C received, exiting



```

## SChernykh | 2026-05-01T09:41:11+00:00
> weird, if I use --threads 128 I still get 20KH/s but if I dont touch threads it gets 35/43KH/s.

XMRig doesn't set CPU affinity and NUMA nodes if you just use `--threads 128` without manually specifying affinity in command line. 

```
Forcing 1500MHz
30225.2 h/s @ 193.7w rx/0
23676.5 h/s @ 194w rx/2

Forcing max cpu max power
42627.6 h/s 301w rx/0
35685.0 h/s 299w rx/2
```
These numbers are in line with some other CPUs. 78-84% of rx/0 hashrate, but rx/2 hashes are 1.5x more heavy, so your CPU still gets efficiency boost on rx/2.

# Action History
- Created by: Motophan | 2026-04-28T08:55:54+00:00
