---
title: xmrig vs xmr-stak-(latest)
source_url: https://github.com/xmrig/xmrig/issues/422
author: jg5xd
assignees: []
labels: []
created_at: '2018-03-01T16:15:31+00:00'
updated_at: '2018-11-05T07:12:55+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:12:55+00:00'
---

# Original Description
xmrig is alot slower than xmrstak.  750 Hps vs 150 Hps.  Cpu affinity on xmrstak is simple.  It's a mystery with no documentation on xmrig.  Xmrig states that it is using all available cores with my dual opteron 6376 as it does when I run xmrstak, but the hash rates are dratically different.  
Even compiled with gcc 7.1.

Ubuntu 16.04 LTS
 * VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          AMD Opteron(tm) Processor 6376                  (2) x64 AES-NI
 * CPU L2/L3:    64.0 MB/24.0 MB
 * THREADS:      30, cryptonight, av=1, donate=1%
 * POOL #1:      45.32.171.89:4444
 * COMMANDS:     hashrate, pause, resume


# Discussion History
## kimats | 2018-03-01T16:18:54+00:00
do you have case to show this,,,logs???

## jg5xd | 2018-03-01T16:35:58+00:00
would that be a particular log file?  which folder?

## kimats | 2018-03-01T17:18:10+00:00
750 vs 150 looks too strange.
what is your config file? 

## jg5xd | 2018-03-01T17:35:25+00:00
{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "retries": 5,
    "retry-pause": 5,
    "donate-level": 1,
    "syslog": false,
    "log-file": null,
    "print-time": 60,
    "av": 1,
    "safe": false,
    "max-cpu-usage": 75,
    "cpu-priority": 4,
    "threads": 30,
    "pools": [
        {
            "url": "45.32.171.89:4444",
            "user": "iz5TJtrotzzcnpkqQc8bhQ4zoMd8PWnx3RHS3BkrtrYyKXXYEzAsNwmMj8XyaSjZoBZy3vwJ9BEmBVrYivWfCdDo2fH3aXAEu",
            "pass": "workerd",
            "keepalive": true,
            "nicehash": false
        }
    ],
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null
    }
}

## DrStein99 | 2018-03-01T23:50:07+00:00
Seriously something wrong with 600khs difference (if I am reading this right).  Try to set CPU affinity to match setup used in XMR-STAK.  Open windows calculator set for "PROGRAMMER" and select "BINARY" (BIN).   Start left-to-right, press 1 or 0 for all cpu processor cores.  Switch calculator say "HEX"  Copy hexidicamal number to "cpu-affinity"	: "0x________", (where _____ is the calculator hexidecimal output).  Start xmRig - check CPU affinities.  If it's in the reverse order, then restart procedure instead go from right to left.  THEN re-test & compare both applications.

## jg5xd | 2018-03-02T01:15:13+00:00
Forard hex or backward... didnt make a diff.

31 cores.

0x7fffffff
Or
0xfffffffe

Not sure if im supposed to delete the priority or max usage, but i left
them alone.


## kimats | 2018-03-02T05:02:38+00:00
@jg5xd I read the issues, once you set cpu affinity, the cpu max usage is skipped by the programme.

## CthulhuVRN | 2018-03-03T06:56:55+00:00
@jg5xd as I can see in specs Opteron 6376 has 16MB L3 Cache, thus your max use is 8 cores per 1 CPU. BUT! xmrig detects only 24MB L3 Cache total (12MB per CPU I guess), so try at first to use only 6 cores per CPU.

Provide me your cat /proc/cpuinfo to figure out your exact system configuration, so I can try to help you with xmrig conf.

## g5-freemen | 2018-03-03T12:40:17+00:00
why "max-cpu-usage": 75 not 100 ?

## jg5xd | 2018-03-03T14:41:04+00:00
 Better...  12 cores total.

* VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          AMD Opteron(tm) Processor 6376                  (2) x64 AES-NI
 * CPU L2/L3:    64.0 MB/24.0 MB
 * THREADS:      32, cryptonight, av=1, donate=1%, affinity=0xAAA0AAA0
 * POOL #1:      45.32.171.89:7777
 * COMMANDS:     hashrate, pause, resume
[2018-03-03 08:19:09] use pool 45.32.171.89:7777 45.32.171.89
[2018-03-03 08:19:09] new job from 45.32.171.89:7777 diff 80000
[2018-03-03 08:20:03] new job from 45.32.171.89:7777 diff 44444
[2018-03-03 08:20:13] speed 2.5s/60s/15m 133.1 285.1 n/a H/s max: 255.0 H/s
[2018-03-03 08:21:03] new job from 45.32.171.89:7777 diff 22222
[2018-03-03 08:21:09] new job from 45.32.171.89:7777 diff 22222
[2018-03-03 08:21:13] speed 2.5s/60s/15m 108.0 288.1 n/a H/s max: 255.0 H/s
[2018-03-03 08:21:58] accepted (1/0) diff 22222 (121 ms)
[2018-03-03 08:22:04] new job from 45.32.171.89:7777 diff 12121
[2018-03-03 08:22:13] speed 2.5s/60s/15m 229.0 306.2 n/a H/s max: 299.4 H/s
[2018-03-03 08:22:19] accepted (2/0) diff 12121 (131 ms)
[2018-03-03 08:22:28] accepted (3/0) diff 12121 (136 ms)
[2018-03-03 08:23:04] new job from 45.32.171.89:7777 diff 24242
[2018-03-03 08:23:13] speed 2.5s/60s/15m 193.7 304.8 n/a H/s max: 299.4 H/s
[2018-03-03 08:24:04] new job from 45.32.171.89:7777 diff 7576
[2018-03-03 08:24:13] speed 2.5s/60s/15m 205.3 297.6 n/a H/s max: 299.4 H/s
[2018-03-03 08:25:04] new job from 45.32.171.89:7777 diff 3788
[2018-03-03 08:25:09] accepted (4/0) diff 3788 (123 ms)
[2018-03-03 08:25:13] speed 2.5s/60s/15m 160.5 298.7 n/a H/s max: 299.4 H/s
[2018-03-03 08:25:20] accepted (5/0) diff 3788 (132 ms)
[2018-03-03 08:25:22] accepted (6/0) diff 3788 (108 ms)
[2018-03-03 08:25:32] accepted (7/0) diff 3788 (124 ms)
[2018-03-03 08:25:36] accepted (8/0) diff 3788 (114 ms)
[2018-03-03 08:25:43] accepted (9/0) diff 3788 (158 ms)
[2018-03-03 08:25:54] accepted (10/0) diff 3788 (116 ms)
[2018-03-03 08:26:03] accepted (11/0) diff 3788 (118 ms)
[2018-03-03 08:26:04] new job from 45.32.171.89:7777 diff 7576
[2018-03-03 08:26:05] accepted (12/0) diff 7576 (161 ms)
[2018-03-03 08:26:13] speed 2.5s/60s/15m 150.1 293.9 n/a H/s max: 299.4 H/s
[2018-03-03 08:26:29] accepted (13/0) diff 7576 (125 ms)
[2018-03-03 08:26:49] accepted (14/0) diff 7576 (110 ms)
[2018-03-03 08:27:04] new job from 45.32.171.89:7777 diff 14823
[2018-03-03 08:27:13] speed 2.5s/60s/15m 395.7 357.7 n/a H/s max: 398.2 H/s
[2018-03-03 08:27:23] new job from 45.32.171.89:7777 diff 14823
[2018-03-03 08:27:27] accepted (15/0) diff 14823 (132 ms)
[2018-03-03 08:28:13] speed 2.5s/60s/15m 147.3 304.8 n/a H/s max: 398.2 H/s
[2018-03-03 08:28:22] accepted (16/0) diff 14823 (60 ms)
[2018-03-03 08:28:40] accepted (17/0) diff 14823 (123 ms)
[2018-03-03 08:29:13] speed 2.5s/60s/15m 345.6 339.6 n/a H/s max: 398.2 H/s
[2018-03-03 08:29:23] accepted (18/0) diff 14823 (125 ms)
[2018-03-03 08:30:13] speed 2.5s/60s/15m 225.9 403.4 n/a H/s max: 439.3 H/s
[2018-03-03 08:31:04] new job from 45.32.171.89:7777 diff 8719
[2018-03-03 08:31:13] speed 2.5s/60s/15m 268.0 373.6 n/a H/s max: 439.3 H/s
[2018-03-03 08:31:20] accepted (19/0) diff 8719 (57 ms)
[2018-03-03 08:31:21] accepted (20/0) diff 8719 (60 ms)
[2018-03-03 08:32:04] new job from 45.32.171.89:7777 diff 13079
[2018-03-03 08:32:13] speed 2.5s/60s/15m 209.2 314.1 n/a H/s max: 439.3 H/s
[2018-03-03 08:32:24] accepted (21/0) diff 13079 (66 ms)
[2018-03-03 08:32:30] new job from 45.32.171.89:7777 diff 13079
[2018-03-03 08:32:39] accepted (22/0) diff 13079 (60 ms)
[2018-03-03 08:33:02] accepted (23/0) diff 13079 (78 ms)
[2018-03-03 08:33:04] new job from 45.32.171.89:7777 diff 20295
[2018-03-03 08:33:13] speed 2.5s/60s/15m 389.1 386.7 n/a H/s max: 439.3 H/s
[2018-03-03 08:34:04] new job from 45.32.171.89:7777 diff 9820
[2018-03-03 08:34:13] speed 2.5s/60s/15m 432.8 456.1 326.6 H/s max: 474.2 H/s
[2018-03-03 08:34:35] accepted (24/0) diff 9820 (113 ms)
[2018-03-03 08:34:43] accepted (25/0) diff 9820 (129 ms)
[2018-03-03 08:35:05] new job from 45.32.171.89:7777 diff 15108
[2018-03-03 08:35:13] speed 2.5s/60s/15m 378.1 404.9 333.5 H/s max: 474.2 H/s
[2018-03-03 08:35:14] accepted (26/0) diff 15108 (73 ms)
[2018-03-03 08:35:19] accepted (27/0) diff 15108 (123 ms)
[2018-03-03 08:36:00] accepted (28/0) diff 15108 (62 ms)
[2018-03-03 08:36:12] accepted (29/0) diff 15108 (74 ms)
[2018-03-03 08:36:13] speed 2.5s/60s/15m 346.9 410.8 341.0 H/s max: 474.2 H/s
[2018-03-03 08:36:18] accepted (30/0) diff 15108 (81 ms)
[2018-03-03 08:36:18] accepted (31/0) diff 15108 (67 ms)
[2018-03-03 08:36:37] accepted (32/0) diff 15108 (81 ms)
[2018-03-03 08:37:05] new job from 45.32.171.89:7777 diff 27831
[2018-03-03 08:37:13] speed 2.5s/60s/15m 312.3 397.6 347.6 H/s max: 474.2 H/s
[2018-03-03 08:37:26] accepted (33/0) diff 27831 (65 ms)
[2018-03-03 08:38:05] new job from 45.32.171.89:7777 diff 17039
[2018-03-03 08:38:13] speed 2.5s/60s/15m 353.4 409.1 353.7 H/s max: 474.2 H/s
[2018-03-03 08:38:35] accepted (34/0) diff 17039 (60 ms)
[2018-03-03 08:39:03] Ctrl+C received, exiting
[2018-03-03 08:39:03] no active pools, stop mining


## jg5xd | 2018-03-03T14:42:33+00:00
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1800.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 0
cpu cores	: 8
apicid		: 32
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 1
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 1
cpu cores	: 8
apicid		: 33
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 2
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 2
cpu cores	: 8
apicid		: 34
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 3
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 3
cpu cores	: 8
apicid		: 35
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 4
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 4
cpu cores	: 8
apicid		: 36
initial apicid	: 4
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 5
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 5
cpu cores	: 8
apicid		: 37
initial apicid	: 5
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 6
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 6
cpu cores	: 8
apicid		: 38
initial apicid	: 6
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 7
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 39
initial apicid	: 7
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 8
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1800.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 0
cpu cores	: 8
apicid		: 40
initial apicid	: 8
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 9
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 1
cpu cores	: 8
apicid		: 41
initial apicid	: 9
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 10
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 2
cpu cores	: 8
apicid		: 42
initial apicid	: 10
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 11
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 3
cpu cores	: 8
apicid		: 43
initial apicid	: 11
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 12
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 4
cpu cores	: 8
apicid		: 44
initial apicid	: 12
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 13
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 5
cpu cores	: 8
apicid		: 45
initial apicid	: 13
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 14
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 2300.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 6
cpu cores	: 8
apicid		: 46
initial apicid	: 14
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 15
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 0
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 47
initial apicid	: 15
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 16
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 0
cpu cores	: 8
apicid		: 64
initial apicid	: 32
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 17
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 1
cpu cores	: 8
apicid		: 65
initial apicid	: 33
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 18
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 2300.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 2
cpu cores	: 8
apicid		: 66
initial apicid	: 34
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 19
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 3
cpu cores	: 8
apicid		: 67
initial apicid	: 35
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 20
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 2300.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 4
cpu cores	: 8
apicid		: 68
initial apicid	: 36
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 21
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 5
cpu cores	: 8
apicid		: 69
initial apicid	: 37
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 22
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1800.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 6
cpu cores	: 8
apicid		: 70
initial apicid	: 38
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 23
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 71
initial apicid	: 39
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 24
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 0
cpu cores	: 8
apicid		: 72
initial apicid	: 40
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 25
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 1
cpu cores	: 8
apicid		: 73
initial apicid	: 41
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 26
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 2
cpu cores	: 8
apicid		: 74
initial apicid	: 42
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 27
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 3
cpu cores	: 8
apicid		: 75
initial apicid	: 43
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 28
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 4
cpu cores	: 8
apicid		: 76
initial apicid	: 44
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 29
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 5
cpu cores	: 8
apicid		: 77
initial apicid	: 45
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 30
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 6
cpu cores	: 8
apicid		: 78
initial apicid	: 46
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro

processor	: 31
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD Opteron(tm) Processor 6376
stepping	: 0
microcode	: 0x6000822
cpu MHz		: 1600.000
cache size	: 2048 KB
physical id	: 1
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 79
initial apicid	: 47
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate retpoline retpoline_amd rsb_ctxsw vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2
bogomips	: 4599.89
TLB size	: 1536 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management: ts ttp tm 100mhzsteps hwpstate cpb eff_freq_ro


## jg5xd | 2018-03-03T15:00:12+00:00
Doesn't seem to like 16 cores as much.  By the way, the last run and this one I had cpu usage set at 100 and priority set to 5.  XMR-STAK is still 772 H/s. 

* VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          AMD Opteron(tm) Processor 6376                  (2) x64 AES-NI
 * CPU L2/L3:    64.0 MB/24.0 MB
 * THREADS:      32, cryptonight, av=1, donate=1%, affinity=0xAAAAAAAA
 * POOL #1:      45.32.171.89:7777
 * COMMANDS:     hashrate, pause, resume
[2018-03-03 08:44:16] use pool 45.32.171.89:7777 45.32.171.89
[2018-03-03 08:44:16] new job from 45.32.171.89:7777 diff 80000
[2018-03-03 08:45:05] new job from 45.32.171.89:7777 diff 48980
[2018-03-03 08:45:19] accepted (1/0) diff 48980 (138 ms)
[2018-03-03 08:45:19] speed 2.5s/60s/15m 210.4 310.7 n/a H/s max: 294.2 H/s
[2018-03-03 08:46:19] speed 2.5s/60s/15m 161.3 298.4 n/a H/s max: 294.2 H/s
[2018-03-03 08:47:05] new job from 45.32.171.89:7777 diff 24490
[2018-03-03 08:47:19] speed 2.5s/60s/15m 184.3 315.2 n/a H/s max: 294.2 H/s
[2018-03-03 08:47:33] new job from 45.32.171.89:7777 diff 24490
[2018-03-03 08:48:05] new job from 45.32.171.89:7777 diff 12245
[2018-03-03 08:48:19] speed 2.5s/60s/15m 238.6 318.6 n/a H/s max: 294.2 H/s
[2018-03-03 08:49:05] accepted (2/0) diff 12245 (117 ms)
[2018-03-03 08:49:06] new job from 45.32.171.89:7777 diff 6123
[2018-03-03 08:49:19] speed 2.5s/60s/15m 281.5 326.5 n/a H/s max: 294.2 H/s
[2018-03-03 08:49:32] accepted (3/0) diff 6123 (101 ms)
[2018-03-03 08:50:01] accepted (4/0) diff 6123 (198 ms)
[2018-03-03 08:50:18] accepted (5/0) diff 6123 (121 ms)
[2018-03-03 08:50:19] speed 2.5s/60s/15m 282.6 290.8 n/a H/s max: 306.3 H/s
[2018-03-03 08:50:31] accepted (6/0) diff 6123 (124 ms)
[2018-03-03 08:50:49] accepted (7/0) diff 6123 (112 ms)
[2018-03-03 08:51:01] accepted (8/0) diff 6123 (108 ms)
[2018-03-03 08:51:04] accepted (9/0) diff 6123 (117 ms)
[2018-03-03 08:51:06] new job from 45.32.171.89:7777 diff 10805
[2018-03-03 08:51:18] accepted (10/0) diff 10805 (140 ms)
[2018-03-03 08:51:19] speed 2.5s/60s/15m 230.7 334.8 n/a H/s max: 306.3 H/s
[2018-03-03 08:51:55] new job from 45.32.171.89:7777 diff 10805
[2018-03-03 08:52:10] new job from 45.32.171.89:7777 diff 10805
[2018-03-03 08:52:19] speed 2.5s/60s/15m 180.3 314.1 n/a H/s max: 306.3 H/s


## CthulhuVRN | 2018-03-03T15:14:08+00:00
@jg5xd, your hash rate looks weird. It jumps like a crazy kangaroo. Any active side processes? Don't you start xmrig and xmr-stak simultaneously? Check htop for core usages by processes.

Btw, try this CPU affinity: 0x7F807F80.

## jg5xd | 2018-03-03T16:31:37+00:00
I don't run xmrstak and xmrig at the same time.  Weird thing about xmrstak is if I run all cores or 8 cores per cpu, i get the same rate.  Anything in between is slower.  Below is a run using CPU affinity: 0x7F807F80.  Got upto 358 H/s.

* VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          AMD Opteron(tm) Processor 6376                  (2) x64 AES-NI
 * CPU L2/L3:    64.0 MB/24.0 MB
 * THREADS:      32, cryptonight, av=1, donate=1%, affinity=0x7F807F80
 * POOL #1:      45.32.171.89:7777
 * COMMANDS:     hashrate, pause, resume
[2018-03-03 09:48:02] use pool 45.32.171.89:7777 45.32.171.89
[2018-03-03 09:48:02] new job from 45.32.171.89:7777 diff 80000
[2018-03-03 09:48:46] speed 2.5s/60s/15m 213.1 n/a n/a H/s max: 219.3 H/s
[2018-03-03 09:48:48] speed 2.5s/60s/15m 213.3 n/a n/a H/s max: 219.3 H/s
[2018-03-03 09:48:54] new job from 45.32.171.89:7777 diff 47059
[2018-03-03 09:49:06] speed 2.5s/60s/15m 223.5 276.1 n/a H/s max: 247.9 H/s
[2018-03-03 09:49:54] new job from 45.32.171.89:7777 diff 23144
[2018-03-03 09:50:06] speed 2.5s/60s/15m 146.1 272.0 n/a H/s max: 259.9 H/s
[2018-03-03 09:50:41] speed 2.5s/60s/15m 249.3 271.6 n/a H/s max: 259.9 H/s
[2018-03-03 09:50:54] new job from 45.32.171.89:7777 diff 11572
[2018-03-03 09:51:06] speed 2.5s/60s/15m 106.4 280.0 n/a H/s max: 259.9 H/s
[2018-03-03 09:51:29] accepted (1/0) diff 11572 (120 ms)
[2018-03-03 09:52:06] speed 2.5s/60s/15m 211.6 279.8 n/a H/s max: 291.3 H/s
[2018-03-03 09:52:25] accepted (2/0) diff 11572 (109 ms)
[2018-03-03 09:52:49] accepted (3/0) diff 11572 (111 ms)
[2018-03-03 09:52:57] accepted (4/0) diff 11572 (185 ms)
[2018-03-03 09:53:06] speed 2.5s/60s/15m 189.3 277.0 n/a H/s max: 291.3 H/s
[2018-03-03 09:53:29] accepted (5/0) diff 11572 (117 ms)
[2018-03-03 09:53:49] accepted (6/0) diff 11572 (150 ms)
[2018-03-03 09:54:06] speed 2.5s/60s/15m 217.7 286.3 n/a H/s max: 291.3 H/s
[2018-03-03 09:54:37] accepted (7/0) diff 11572 (137 ms)
[2018-03-03 09:54:38] accepted (8/0) diff 11572 (124 ms)
[2018-03-03 09:55:06] speed 2.5s/60s/15m 178.2 291.4 n/a H/s max: 291.3 H/s
[2018-03-03 09:55:29] accepted (9/0) diff 11572 (123 ms)
[2018-03-03 09:55:42] accepted (10/0) diff 11572 (116 ms)
[2018-03-03 09:56:02] accepted (11/0) diff 11572 (170 ms)
[2018-03-03 09:56:06] speed 2.5s/60s/15m 219.6 293.9 n/a H/s max: 291.3 H/s
[2018-03-03 09:56:38] accepted (12/0) diff 11572 (184 ms)
[2018-03-03 09:56:57] accepted (13/0) diff 11572 (115 ms)
[2018-03-03 09:57:06] speed 2.5s/60s/15m 99.4 305.4 n/a H/s max: 291.3 H/s
[2018-03-03 09:57:32] accepted (14/0) diff 11572 (117 ms)
[2018-03-03 09:57:38] accepted (15/0) diff 11572 (116 ms)
[2018-03-03 09:57:45] accepted (16/0) diff 11572 (56 ms)
[2018-03-03 09:57:54] new job from 45.32.171.89:7777 diff 11572
[2018-03-03 09:58:06] speed 2.5s/60s/15m 278.6 309.1 n/a H/s max: 298.2 H/s
[2018-03-03 09:58:54] accepted (17/0) diff 11572 (155 ms)
[2018-03-03 09:59:06] speed 2.5s/60s/15m 289.5 328.1 n/a H/s max: 324.1 H/s
[2018-03-03 09:59:11] accepted (18/0) diff 11572 (119 ms)
[2018-03-03 09:59:41] accepted (19/0) diff 11572 (94 ms)
[2018-03-03 10:00:06] speed 2.5s/60s/15m 319.3 323.5 n/a H/s max: 324.1 H/s
[2018-03-03 10:01:06] speed 2.5s/60s/15m 264.6 309.8 n/a H/s max: 324.1 H/s
[2018-03-03 10:01:31] accepted (20/0) diff 11572 (111 ms)
[2018-03-03 10:02:06] speed 2.5s/60s/15m 271.1 314.4 n/a H/s max: 324.1 H/s
[2018-03-03 10:02:15] accepted (21/0) diff 11572 (115 ms)
[2018-03-03 10:03:06] speed 2.5s/60s/15m 283.0 323.8 289.6 H/s max: 324.1 H/s
[2018-03-03 10:03:32] accepted (22/0) diff 11572 (126 ms)
[2018-03-03 10:04:06] speed 2.5s/60s/15m 277.6 318.9 291.5 H/s max: 324.1 H/s
[2018-03-03 10:04:39] accepted (23/0) diff 11572 (59 ms)
[2018-03-03 10:05:06] speed 2.5s/60s/15m 222.4 297.5 291.9 H/s max: 324.1 H/s
[2018-03-03 10:05:08] new job from 45.32.171.89:7777 diff 11572
[2018-03-03 10:05:18] accepted (24/0) diff 11572 (57 ms)
[2018-03-03 10:05:55] new job from 45.32.171.89:7777 diff 8679
[2018-03-03 10:06:06] speed 2.5s/60s/15m 281.7 299.3 293.1 H/s max: 324.1 H/s
[2018-03-03 10:06:26] new job from 45.32.171.89:7777 diff 8679
[2018-03-03 10:06:44] accepted (25/0) diff 8679 (108 ms)
[2018-03-03 10:06:55] new job from 45.32.171.89:7777 diff 3028
[2018-03-03 10:07:01] accepted (26/0) diff 3028 (135 ms)
[2018-03-03 10:07:04] accepted (27/0) diff 3028 (58 ms)
[2018-03-03 10:07:04] accepted (28/0) diff 3028 (58 ms)
[2018-03-03 10:07:06] speed 2.5s/60s/15m 224.4 268.2 292.1 H/s max: 324.1 H/s
[2018-03-03 10:07:19] accepted (29/0) diff 3028 (56 ms)
[2018-03-03 10:07:21] accepted (30/0) diff 3028 (117 ms)
[2018-03-03 10:07:28] accepted (31/0) diff 3028 (57 ms)
[2018-03-03 10:07:38] accepted (32/0) diff 3028 (57 ms)
[2018-03-03 10:07:54] accepted (33/0) diff 3028 (58 ms)
[2018-03-03 10:07:55] new job from 45.32.171.89:7777 diff 6056
[2018-03-03 10:08:06] speed 2.5s/60s/15m 251.2 312.0 294.1 H/s max: 324.1 H/s
[2018-03-03 10:08:17] new job from 45.32.171.89:7777 diff 6056
[2018-03-03 10:08:17] accepted (34/0) diff 6056 (60 ms)
[2018-03-03 10:08:27] accepted (35/0) diff 6056 (59 ms)
[2018-03-03 10:08:34] accepted (36/0) diff 6056 (58 ms)
[2018-03-03 10:08:38] accepted (37/0) diff 6056 (82 ms)
[2018-03-03 10:08:39] accepted (38/0) diff 6056 (59 ms)
[2018-03-03 10:08:55] new job from 45.32.171.89:7777 diff 12112
[2018-03-03 10:08:57] accepted (39/0) diff 12112 (108 ms)
[2018-03-03 10:09:02] accepted (40/0) diff 12112 (57 ms)
[2018-03-03 10:09:06] speed 2.5s/60s/15m 291.4 331.1 296.9 H/s max: 324.1 H/s
[2018-03-03 10:10:06] speed 2.5s/60s/15m 270.4 316.6 298.2 H/s max: 324.1 H/s
[2018-03-03 10:10:55] new job from 45.32.171.89:7777 diff 8015
[2018-03-03 10:11:03] accepted (41/0) diff 8015 (57 ms)
[2018-03-03 10:11:06] speed 2.5s/60s/15m 292.2 324.6 299.7 H/s max: 325.6 H/s
[2018-03-03 10:11:07] accepted (42/0) diff 8015 (57 ms)
[2018-03-03 10:11:09] accepted (43/0) diff 8015 (56 ms)
[2018-03-03 10:11:12] accepted (44/0) diff 8015 (56 ms)
[2018-03-03 10:11:52] accepted (45/0) diff 8015 (60 ms)
[2018-03-03 10:11:55] new job from 45.32.171.89:7777 diff 16030
[2018-03-03 10:12:00] accepted (46/0) diff 16030 (57 ms)
[2018-03-03 10:12:06] speed 2.5s/60s/15m 290.5 338.9 300.6 H/s max: 325.6 H/s
[2018-03-03 10:12:22] accepted (47/0) diff 16030 (59 ms)
[2018-03-03 10:12:55] new job from 45.32.171.89:7777 diff 32060
[2018-03-03 10:13:06] speed 2.5s/60s/15m 321.0 328.9 301.5 H/s max: 325.6 H/s
[2018-03-03 10:13:43] accepted (48/0) diff 32060 (121 ms)
[2018-03-03 10:13:55] new job from 45.32.171.89:7777 diff 11874
[2018-03-03 10:14:06] speed 2.5s/60s/15m 311.5 325.6 302.3 H/s max: 325.6 H/s
[2018-03-03 10:14:17] accepted (49/0) diff 11874 (57 ms)
[2018-03-03 10:15:06] speed 2.5s/60s/15m 302.4 321.5 301.5 H/s max: 325.6 H/s
[2018-03-03 10:15:20] accepted (50/0) diff 11874 (57 ms)
[2018-03-03 10:15:55] new job from 45.32.171.89:7777 diff 7345
[2018-03-03 10:16:06] speed 2.5s/60s/15m 320.8 333.7 302.4 H/s max: 325.6 H/s
[2018-03-03 10:16:09] accepted (51/0) diff 7345 (57 ms)
[2018-03-03 10:16:10] accepted (52/0) diff 7345 (116 ms)
[2018-03-03 10:16:17] accepted (53/0) diff 7345 (57 ms)
[2018-03-03 10:16:28] accepted (54/0) diff 7345 (58 ms)
[2018-03-03 10:16:44] accepted (55/0) diff 7345 (118 ms)
[2018-03-03 10:16:54] accepted (56/0) diff 7345 (56 ms)
[2018-03-03 10:16:56] new job from 45.32.171.89:7777 diff 14065
[2018-03-03 10:17:06] speed 2.5s/60s/15m 302.0 336.1 304.3 H/s max: 325.6 H/s
[2018-03-03 10:17:08] accepted (57/0) diff 14065 (58 ms)
[2018-03-03 10:17:11] accepted (58/0) diff 14065 (88 ms)
[2018-03-03 10:17:56] new job from 45.32.171.89:7777 diff 20417
[2018-03-03 10:18:06] speed 2.5s/60s/15m 276.2 329.7 305.0 H/s max: 325.6 H/s
[2018-03-03 10:18:56] new job from 45.32.171.89:7777 diff 20417
[2018-03-03 10:18:56] new job from 45.32.171.89:7777 diff 10209
[2018-03-03 10:18:59] accepted (59/0) diff 10209 (56 ms)
[2018-03-03 10:19:06] speed 2.5s/60s/15m 289.0 332.1 307.1 H/s max: 326.9 H/s
[2018-03-03 10:19:43] accepted (60/0) diff 10209 (58 ms)
[2018-03-03 10:20:06] speed 2.5s/60s/15m 293.4 344.2 310.3 H/s max: 341.6 H/s
[2018-03-03 10:20:21] accepted (61/0) diff 10209 (57 ms)
[2018-03-03 10:20:21] accepted (62/0) diff 10209 (66 ms)
[2018-03-03 10:20:51] accepted (63/0) diff 10209 (91 ms)
[2018-03-03 10:21:01] accepted (64/0) diff 10209 (57 ms)
[2018-03-03 10:21:06] speed 2.5s/60s/15m 300.4 323.0 312.0 H/s max: 341.6 H/s
[2018-03-03 10:21:21] accepted (65/0) diff 10209 (116 ms)
[2018-03-03 10:21:33] accepted (66/0) diff 10209 (58 ms)
[2018-03-03 10:21:56] new job from 45.32.171.89:7777 diff 15606
[2018-03-03 10:22:06] speed 2.5s/60s/15m 300.7 334.0 315.0 H/s max: 341.6 H/s
[2018-03-03 10:22:23] accepted (67/0) diff 15606 (117 ms)
[2018-03-03 10:22:45] accepted (68/0) diff 15606 (62 ms)
[2018-03-03 10:23:06] speed 2.5s/60s/15m 316.9 356.4 317.6 H/s max: 350.4 H/s
[2018-03-03 10:23:25] accepted (69/0) diff 15606 (58 ms)
[2018-03-03 10:24:06] speed 2.5s/60s/15m 306.1 338.8 318.3 H/s max: 350.4 H/s
[2018-03-03 10:24:56] new job from 45.32.171.89:7777 diff 9225
[2018-03-03 10:25:06] speed 2.5s/60s/15m 276.6 346.9 319.4 H/s max: 350.4 H/s
[2018-03-03 10:25:34] new job from 45.32.171.89:7777 diff 9225
[2018-03-03 10:25:46] accepted (70/0) diff 9225 (114 ms)
[2018-03-03 10:25:56] new job from 45.32.171.89:7777 diff 5535
[2018-03-03 10:25:59] accepted (71/0) diff 5535 (70 ms)
[2018-03-03 10:26:06] speed 2.5s/60s/15m 191.1 286.7 316.9 H/s max: 350.4 H/s
[2018-03-03 10:26:12] accepted (72/0) diff 5535 (57 ms)
[2018-03-03 10:26:34] accepted (73/0) diff 5535 (58 ms)
[2018-03-03 10:26:37] accepted (74/0) diff 5535 (57 ms)
[2018-03-03 10:26:43] accepted (75/0) diff 5535 (60 ms)
[2018-03-03 10:26:56] new job from 45.32.171.89:7777 diff 11070
[2018-03-03 10:27:06] speed 2.5s/60s/15m 278.6 286.8 314.2 H/s max: 350.4 H/s
[2018-03-03 10:27:21] accepted (76/0) diff 11070 (57 ms)
[2018-03-03 10:27:39] accepted (77/0) diff 11070 (57 ms)
[2018-03-03 10:28:06] speed 2.5s/60s/15m 335.2 361.0 316.7 H/s max: 358.3 H/s


## CthulhuVRN | 2018-03-03T21:04:00+00:00
@jg5xd 358 H/s is your max, but not stable average. Don't look at these numbers. Only average matter. The same is for xmr-stak.

I just realized you'd set the threads parameter. Set it to null and try again.

I don't know about AMD CPUs, but on Intel I have +/- same hash rates on xmrig and xmr-stak. Sometimes xmrig shows me a little bit higher hash rates on same CPUs.
Also it's really weird that's 10s-average jumps between 190 and 335 H/s. It tells me there are some processes use CPU actively and cause such hash rate drop or maybe your CPU is throttling. Check for temperature and governor.

Btw, here is my conf for 6-core 12-threads Intel CPU, L3 12MB so only 6 threads are active:

```
{
        "algo": "cryptonight",
        "api": {
                "port": 0,
                "access-token": null,
                "worker-id": null
        },
        "av": 0,
        "background": false,
        "colors": true,
        "cpu-affinity": "0xFC0",
        "cpu-priority": 5,
        "donate-level": 5,
        "log-file": null,
        "max-cpu-usage": 100,
        "pools": [
                {
                        "url": "/* your pool here */",
                        "user": "/* your wallet address here */",
                        "pass": "/* your pass here */",
                        "keepalive": true,
                        "nicehash": false
                }
        ],
        "print-time": 60,
        "retries": 3,
        "retry-pause": 60,
        "safe": false,
        "syslog": false,
        "threads": null
}
```

## jg5xd | 2018-03-03T23:30:50+00:00
Aight, don't bother.  I'm done messing with it.

## CthulhuVRN | 2018-03-05T14:25:48+00:00
@jg5xd check #86 if still interested.
Long story short, your CPUs has 2 NUMA nodes per CPU so I guess xmrig must be started 2 times with 2 different cpu affinity (lscpu must help you with it).

## elescondite | 2018-03-13T17:19:36+00:00
You can only run 8 cores on these cpus. The cache size is 16MB per cpu, not 24MB as xmrig reports (it's not xmrig's fault, but that's another matter). The reason the hash rate jumps around so much is there are too many processes vying for the same cache memory.

Add a **-t 16** parameter to the command line, or **"threads":16** to config.json and you will get in the 940 H/s range. You don't need to worry about affinity -- the OS does a fine job of that.

You can run 1 xmrig process with 16 threads, or 8 processes with 2 threads each or any other combination. They all work well. Here's a snippet from xmrig's log on a dual 6376 machine running under Ubuntu 16.04:

`
xmrig.log:[2018-02-14 15:35:32] speed 2.5s/60s/15m 944.0 943.7 943.5 H/s max: 944.1 H/s
xmrig.log:[2018-02-14 15:36:32] speed 2.5s/60s/15m 943.5 943.7 943.5 H/s max: 944.1 H/s
xmrig.log:[2018-02-14 15:37:32] speed 2.5s/60s/15m 943.3 943.1 943.5 H/s max: 944.1 H/s
xmrig.log:[2018-02-14 15:38:32] speed 2.5s/60s/15m 943.6 943.3 943.5 H/s max: 944.1 H/s
`

Occasionally, you may get lower rates initially if the cpu is/has been running other things, but restarting xmrig a couple of times usually fixes it. Having xmrig start on boot is the cleanest way to ensure maximum performance. This will run for days on end with hardly a blip in the hash rate.

## mohammad4u | 2018-04-06T07:09:58+00:00
Hi, if you use ubuntu. Set the cache to 13. Then use -t 12. If you are using v 2.5.0 or above set cache to 14 and check -t 13 or 14. Cheers.

# Action History
- Created by: jg5xd | 2018-03-01T16:15:31+00:00
- Closed at: 2018-11-05T07:12:55+00:00
