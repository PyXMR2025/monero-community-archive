---
title: Optimal config for 4 sockets 8 NUMA nodes
source_url: https://github.com/xmrig/xmrig/issues/78
author: ghost
assignees: []
labels:
- NUMA
created_at: '2017-08-30T10:47:59+00:00'
updated_at: '2017-11-27T00:24:24+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:14:35+00:00'
---

# Original Description
I know that the issue of multiple sockets was discussed before but I am struggling to find the optimal configuration (i.e. maximum hashrate). here is the output of lscpu

Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                48
On-line CPU(s) list:   0-47
Thread(s) per core:    1
Core(s) per socket:    12
CPU socket(s):         4
NUMA node(s):          8
Vendor ID:             AuthenticAMD
CPU family:            16
Model:                 9
Stepping:              1
CPU MHz:               800.000
BogoMIPS:              4400.05
Virtualization:        AMD-V
L1d cache:             64K
L1i cache:             64K
L2 cache:              512K
L3 cache:              5118K
NUMA node0 CPU(s):     0-5
NUMA node1 CPU(s):     6-11
NUMA node2 CPU(s):     12-17
NUMA node3 CPU(s):     18-23
NUMA node4 CPU(s):     24-29
NUMA node5 CPU(s):     30-35
NUMA node6 CPU(s):     36-41
NUMA node7 CPU(s):     42-47


When I start xmrig with default (undefined settings), I get the following:

`* VERSIONS:     XMRig/2.3.1 libuv/1.14.0 gcc/7.1.0
 * HUGE PAGES:   available, disabled
 * CPU:          AMD Opteron(tm) Processor 6174 (4) x64 -AES-NI
 * CPU L2/L3:    96.0 MB/40.0 MB
 * THREADS:      20, cryptonight , av=4, donate=5%

I tried to run multiple xmrig instances as described before but the combined hashrate decreased substantially.

Could you please give me some suggestions on how to run with multiple NUMA nodes and what kind of cpu-affinity should I use. 

Thanks a lot in advance.
 

# Discussion History
## hoangcao243 | 2017-08-30T15:01:23+00:00
What kind of hs are you getting if you don't mind me asking?

## xmrig | 2017-08-30T21:28:30+00:00
Not sure about these CPUs. probably 6 threads per socket. Anyway you don't get much all 61* lacks support for AES-NI instructions, it can work with software AES, but very slow.

## ghost | 2017-08-30T21:39:44+00:00
Thanks for your reply. Yes I know, the machine is about 7 years old and lacks support for AES-NI. I am trying to get the most out of it. So you say I should run 4 instances of xmrig? Is NUMA configuration relative here? or cpu-affinity?

## xmrig | 2017-08-30T21:43:22+00:00
Here a huge field for experiments, I think better strategy first get maximum from single CPU then try scale it to all.

## ghost | 2017-08-30T21:48:47+00:00
OK I will try. 

Amazing software(s) and amazing support. Can't thank you enough.
Keep up the good work.

## xmrig | 2017-09-03T03:14:35+00:00
Move all NUMA related issues to #86

# Action History
- Created by: ghost | 2017-08-30T10:47:59+00:00
- Closed at: 2017-09-03T03:14:35+00:00
