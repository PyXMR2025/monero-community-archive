---
title: Limit CPU use
source_url: https://github.com/xmrig/xmrig/issues/1863
author: AhmedAwadallah257
assignees: []
labels: []
created_at: '2020-10-03T23:03:40+00:00'
updated_at: '2021-04-12T14:47:36+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:47:36+00:00'
---

# Original Description
How I can use only 80% of the below virtual CPU:

Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          1
On-line CPU(s) list:             0
Thread(s) per core:              1
Core(s) per socket:              1
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           13
Model name:                      QEMU Virtual CPU version 2.5+
Stepping:                        3
CPU MHz:                         2199.998
BogoMIPS:                        4399.99
Hypervisor vendor:               KVM
Virtualization type:             full
L1d cache:                       32 KiB
L1i cache:                       32 KiB
L2 cache:                        4 MiB
L3 cache:                        16 MiB
NUMA node0 CPU(s):               0
Vulnerability Itlb multihit:     KVM: Vulnerable
Vulnerability L1tf:              Mitigation; PTE Inversion
Vulnerability Mds:               Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown
Vulnerability Meltdown:          Mitigation; PTI
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Full generic retpoline, STIBP disabled, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pse36 clf
                                 lush mmx fxsr sse sse2 syscall nx lm rep_good nopl xtopology cpuid
                                 tsc_known_freq pni cx16 x2apic hypervisor lahf_lm pti

# Discussion History
## DeadManWalkingTO | 2020-10-08T20:35:56+00:00
`How I can use only 80% of the below virtual CPU?`

You can't!
```
CPU(s): 1
On-line CPU(s) list: 0
Thread(s) per core: 1
Core(s) per socket: 1
Socket(s): 1
NUMA node(s): 1
```
You can use only the 100% from that CPU.

## Lonnegan | 2020-10-12T13:48:27+00:00
In older versions of xmrig there was an option  "max-cpu-usage": 100, in the config file, in newer versions I can't find it anymore. I don't know if that function is deprecated or still functional. Just try :)

## Henriquelay | 2021-04-07T22:06:53+00:00
@Lonnegan [CPU_MAX_USAGE](https://github.com/xmrig/xmrig/blob/master/doc/CPU_MAX_USAGE.md) , It is essentially renamed to max threads

## Spudz76 | 2021-04-09T06:18:47+00:00
And threads would be minimum 1, equal number of cores, so you get 100% no matter what.

It's not a governor/throttle but more like max-cores-usage.

You can use other tools like renice (or config option priority) to set it to always take a back seat to other tasks, which helps smoothness but it will still try to use 100% as much as it can (but the Linux kernel will preempt it for other tasks, the less priority the miner has).  Not as smooth maybe as hard limit but about the best supported solution.

I had wondered previously if a bsleep sort of idle/sleep of settable ms similar to CUDA miner backend could make CPU partial usage more possible.

# Action History
- Created by: AhmedAwadallah257 | 2020-10-03T23:03:40+00:00
- Closed at: 2021-04-12T14:47:36+00:00
