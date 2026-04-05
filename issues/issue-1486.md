---
title: The hashrate become more and more low
source_url: https://github.com/xmrig/xmrig/issues/1486
author: momettang
assignees: []
labels:
- stability
created_at: '2020-01-05T10:17:29+00:00'
updated_at: '2020-08-31T05:48:24+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:48:24+00:00'
---

# Original Description
I use a VM. It has 39 Core. The OS is Ubuntu 16.04. The miner version is XMRig 5.5.0.
When I start a new miner,the hashrate will be closed the max hashrate. But with the time pasted,
the hashrate will be more and more low. please refer the the log.

[2020-01-03 22:32:42.846] speed 10s/60s/15m 17406.0 17423.2 n/a H/s max 17669.7 H/s
[2020-01-03 22:32:53.002]  cpu  accepted (17/0) diff 175004 (339 ms)
[2020-01-03 22:32:58.058]  cpu  accepted (18/0) diff 175004 (318 ms)
[2020-01-03 22:33:42.895] speed 10s/60s/15m 17315.3 17351.0 n/a H/s max 17669.7 H/s
[2020-01-03 22:34:29.587]  cpu  accepted (19/0) diff 1251082 (321 ms)
[2020-01-03 22:34:42.935] speed 10s/60s/15m 17298.0 17300.4 n/a H/s max 17669.7 H/s
[2020-01-03 22:35:42.971] speed 10s/60s/15m 17283.8 17282.5 n/a H/s max 17669.7 H/s
[2020-01-03 22:36:01.817]  cpu  accepted (20/0) diff 1251082 (321 ms)
[2020-01-03 22:36:22.773]  cpu  accepted (21/0) diff 1251082 (321 ms)
[2020-01-03 22:36:32.727]  cpu  accepted (22/0) diff 1251082 (322 ms)
[2020-01-03 22:36:43.001] speed 10s/60s/15m 17307.8 17292.2 n/a H/s max 17669.7 H/s


[2020-01-05 17:56:59.331]  cpu  accepted (183/0) diff 959126 (327 ms)
[2020-01-05 17:57:23.072] speed 10s/60s/15m 16690.4 16676.3 16594.5 H/s max 17788.9 H/s
[2020-01-05 17:58:23.112] speed 10s/60s/15m 16680.3 16681.4 16591.7 H/s max 17788.9 H/s
[2020-01-05 17:58:44.012]  cpu  accepted (184/0) diff 959126 (334 ms)
[2020-01-05 17:59:23.150] speed 10s/60s/15m 16696.5 16682.7 16588.4 H/s max 17788.9 H/s
[2020-01-05 17:59:57.551]  cpu  accepted (185/0) diff 1136535 (364 ms)
[2020-01-05 17:59:59.146]  cpu  accepted (186/0) diff 1136535 (324 ms)
[2020-01-05 18:00:23.186] speed 10s/60s/15m 16666.8 16678.7 16584.8 H/s max 17788.9 H/s

The average hash rate change from 17292.2 to 16584.8. 
Does anybody meet this kinds of issue?


# Discussion History
## buzaiq | 2020-01-05T10:36:12+00:00
Which processor you are leveraging? lscpu info?

## momettang | 2020-01-05T10:52:13+00:00
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                39
On-line CPU(s) list:   0-38
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             39
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 85
Model name:            Intel(R) Xeon(R) Gold 6138 CPU @ 2.00GHz
Stepping:              4
CPU MHz:               1995.312
BogoMIPS:              3990.62
Hypervisor vendor:     VMware
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              1024K
L3 cache:              28160K
NUMA node0 CPU(s):     0-19
NUMA node1 CPU(s):     20-38
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp kaiser fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 invpcid rtm mpx avx512f rdseed adx smap clflushopt clwb avx512cd xsaveopt xsavec arat pku flush_l1d arch_capabilities


## SChernykh | 2020-01-05T12:49:36+00:00
CPU is running at higher clock speed when you start mining. It heats up and reduces clock speed later. You need to monitor it to see if it's really the issue.

## xmrig | 2020-08-31T05:48:24+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: momettang | 2020-01-05T10:17:29+00:00
- Closed at: 2020-08-31T05:48:24+00:00
