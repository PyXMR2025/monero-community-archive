---
title: Segmentation fault argon2_core.c
source_url: https://github.com/xmrig/xmrig/issues/1459
author: zhangming965
assignees: []
labels:
- bug
created_at: '2019-12-23T12:29:36+00:00'
updated_at: '2020-06-02T14:33:23+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:33:23+00:00'
---

# Original Description
**Describe the bug**
Segmentation fault

**To Reproduce**
Just run?


**Required data**
xmrig 5.4.0
[New LWP 16070]
[New LWP 16072]
[New LWP 16071]
[New LWP 16069]
[New LWP 16074]
[New LWP 16073]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x00000000007aadf4 in load_block (dst=0x0, input=0x7f9a279245e0)
    at /root/xmrig/src/crypto/randomx/argon2_core.c:89
89                      dst->v[i] = load64((const uint8_t *)input + i * sizeof(dst->v[i]));
[Current thread is 1 (Thread 0x7f9a27925700 (LWP 16070))]

System info
Ubuntu 18.04.3 LTS
Linux abf27f708942 3.10.0-1062.4.3.el7.x86_64 #1 SMP Wed Nov 13 23:58:53 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 79
model name      : Intel(R) Xeon(R) CPU E5-26xx v4
stepping        : 1
microcode       : 0x1
cpu MHz         : 2394.454
cache size      : 4096 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx lm constant_tsc rep_good nopl eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch bmi1 avx2 bmi2 rdseed adx xsaveopt
bogomips        : 4788.90
clflush size    : 64
cache_alignment : 64
address sizes   : 40 bits physical, 48 bits virtual
power management:



# Discussion History
## xmrig | 2019-12-23T12:51:13+00:00
Can you provide more details than *Just run*, it first time when someone experienced issues with argon2.
Thank you.

## zhangming966 | 2019-12-24T11:42:34+00:00
what information do you need? it happens on 5.4.0 released build. and i make own debug build for getting debug symbols

## xmrig | 2019-12-24T12:17:40+00:00
Any information, config, miner output, etc, because I can't confirm crash, to fix this crash required:
1. I reproduce the crash.
2. Or you figure it out by self, as it stable in your environment.
Thank you.

## zhangming966 | 2019-12-24T13:01:57+00:00
same build work on some machines, and not working on other
used default config from repo (changed only url for minexmr/other pool with randomx (because donate pool used cn))
reproduced on another machine
first
 * LIBS         libuv/1.34.0 hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-26xx v4 (1) x64 AES
                L2:4.0 MB L3:0.0 MB 1C/1T NUMA:1
 * MEMORY       0.9/1.0 GB (93%)
 * DONATE       5%
 * COMMANDS     hashrate, pause, resume
[2019-12-24 12:55:52.843]  rx   init dataset algo rx/0 (1 threads) seed 8fd8d3ee74547743...
[2019-12-24 12:55:52.843]  rx   not enough memory for RandomX dataset
[2019-12-24 12:55:52.843]  rx   failed to allocate RandomX dataset, switching to slow mode (0 ms)
Segmentation fault (core dumped)

second
 * LIBS         libuv/1.34.0 hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz (1) x64 AES
                L2:4.0 MB L3:16.0 MB 1C/1T NUMA:1
 * MEMORY       3.3/3.7 GB (89%)
 * DONATE       5%
 * COMMANDS     hashrate, pause, resume

lscpu | grep "Byte Order"
Byte Order:          Little Endian

can i do something else?

## SChernykh | 2019-12-24T14:21:36+00:00
> MEMORY 0.9/1.0 GB (93%)
> MEMORY 3.3/3.7 GB (89%)

This is the issue. XMRig fails to allocate even 256 MB buffer for slow mining mode and crashes.

## xmrig | 2019-12-24T22:03:58+00:00
Crash fixed in dev branch, but you can't mine anyway if you have not enough memory.
Thank you.

# Action History
- Created by: zhangming965 | 2019-12-23T12:29:36+00:00
- Closed at: 2020-06-02T14:33:23+00:00
