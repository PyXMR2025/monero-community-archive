---
title: CPU usage not maxing 100%
source_url: https://github.com/xmrig/xmrig/issues/1490
author: Helmeboi
assignees: []
labels: []
created_at: '2020-01-06T14:57:31+00:00'
updated_at: '2021-04-12T15:04:14+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:04:14+00:00'
---

# Original Description
I used to get 100% cpu usage with 4 cores before but all of a sudden I'm getting half the hashrate. I tried different affinity settings, got 100% again but it got lowered just like the first time, lastly I didn't set affinity and I'm getting 80% at best.

My config file:

    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": 5,
        "yield": false,
        "memory-pool": false,
        "argon2-impl": null,
        "argon2": [0],
        "rx": [-1,-1,-1,-1],

lscpu:

```
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                16
On-line CPU(s) list:   0-15
Thread(s) per core:    2
Core(s) per socket:    8
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 79
Model name:            Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Stepping:              1
CPU MHz:               2300.220
BogoMIPS:              4600.10
Hypervisor vendor:     Xen
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              46080K
NUMA node0 CPU(s):     0-15
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat p                                                           se36 clflush mmx fxsr sse sse2 ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl                                                            xtopology cpuid pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_de                                                           adline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm cpuid_fault invpcid_single p                                                           ti fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt
```


# Discussion History
## GjBrutello | 2020-01-06T21:58:35+00:00
it's normal because of 2.30GHz. And set "yield": true,

## Helmeboi | 2020-01-08T02:18:15+00:00
> try "rx": [1,2,3,4],

I tried different options always not getting 100% as I used to.



> it's normal because of 2.30GHz. And set "yield": true,

Tried both true and false, no signification difference in hashrate. And what do you mean "normal because of 2.30GHz" if I may ask? It used to use 100%.

## TheCherry | 2020-03-10T12:47:29+00:00
@Helmeboi set threads to your cores. And you reach the 100%

## Spudz76 | 2020-03-21T21:04:01+00:00
I see hypervisor junk, is this a VM, and do you know that other VMs aren't getting in the way now, as opposed to previously the server had less customers?

# Action History
- Created by: Helmeboi | 2020-01-06T14:57:31+00:00
- Closed at: 2021-04-12T15:04:14+00:00
