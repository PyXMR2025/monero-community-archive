---
title: Not an issue - Affinity mappings
source_url: https://github.com/xmrig/xmrig/issues/620
author: dirtydavemcgee
assignees: []
labels:
- META
created_at: '2018-05-08T23:33:54+00:00'
updated_at: '2018-11-05T13:39:21+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:39:21+00:00'
---

# Original Description
I see many many people stuck with affinity
I made a chart ran out to 16 cores
Both Linux and Windows, due to different core enumerations between physical and virtual
Please correct if wrong
Also consider #563 - Advanced threads mode

Linux affinity, Physical cores (Ryzen users see windows affinities)
Good for 16 cores
Cores 0,1
0x3
Cores 0,1,2
0x7
Cores 0,1,2,3
0xF
Cores 0,1,2,3,4
0x1F
Cores 0,1,2,3,4,5
0x3F
Cores 0,1,2,3,4,5,6
0x7F
Cores 0,1,2,3,4,5,6,7
0xFF
Cores 0,1,2,3,4,5,6,7,8
0x1FF
Cores 0,1,2,3,4,5,6,7,8,9
0x3FF
Cores 0,1,2,3,4,5,6,7,8,9,10
0x7FF
Cores 0,1,2,3,4,5,6,7,8,9,10,11
0xFFF
Cores 0,1,2,3,4,5,6,7,8,9,10,11,12
0x1FFF
Cores 0,1,2,3,4,5,6,7,8,9,10,11,12,13
0x3FFF
Cores 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
0x7FFF
Cores 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
0xFFFF

Windows affinity, Physical cores
Windows enumerates cores differently than linux.
Cores 0,2
0x5
Cores 0,2,4
0x15
Cores 0,2,4,6
0x55
Cores 0,2,4,6,8
0x155
Cores 0,2,4,6,8,10
0x555
Cores 0,2,4,6,8,10,12
0x1555
Cores 0,2,4,6,8,10,12,14
0x5555
Cores 0,2,4,6,8,10,12,14,16
0x15555
Cores 0,2,4,6,8,10,12,14,16,18
0x55555
Cores 0,2,4,6,8,10,12,14,16,18,20
0x155555
Cores 0,2,4,6,8,10,12,14,16,18,20,22
0x555555
Cores 0,2,4,6,8,10,12,14,16,18,20,22,24
0x1555555
Cores 0,2,4,6,8,10,12,14,16,18,20,22,24,26
0x5555555
Cores 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28
0x15555555
Cores 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
0x55555555


# Discussion History
## xmrig | 2018-05-08T23:54:59+00:00
Nice, for Linux not always true, AMD Ryzen use same enumerations as Windows.
Also in v2.6 added more human friendly method to set affinity #563
Thank you.

## dirtydavemcgee | 2018-05-09T00:19:33+00:00
Yeah saw #563 only after I made this lol. Thanks for the work.
Updated the first post.

## Gizzywhop | 2018-05-16T06:13:19+00:00
Ok so I have been playing with this affinity settings and such for hours. My cpu sits at 60% any suggestions would be much appreciated

Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                96
On-line CPU(s) list:   0-95
Thread(s) per core:    2
Core(s) per socket:    24
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 85
Model name:            Intel(R) Xeon(R) CPU
Stepping:              3
CPU MHz:               2000.170
BogoMIPS:              4000.34
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              56320K
NUMA node0 CPU(s):     0-23,48-71
NUMA node1 CPU(s):     24-47,72-95
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1

Cpu text seems to only have numa 0 cpu's and I can't seem to get it to pick up the others 

## dirtydavemcgee | 2018-05-21T03:57:09+00:00
I only ran this out to 16 cores, you may benefit from advanced thread config as in #563 

## Adamandinos | 2018-06-18T13:30:24+00:00
Hello mate my CPU affinity is set to null but when i check task manager i can see all 4 cores at 50% as set.
shall i set it to 0x55 for  Cores 0,2,4,6 in WINDOWS?

Im using a low end laptop just testing the miner and pools as im new.

Also is there any other configurations that will increase the hashrate  ?

# Action History
- Created by: dirtydavemcgee | 2018-05-08T23:33:54+00:00
- Closed at: 2018-11-05T13:39:21+00:00
