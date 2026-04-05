---
title: Can't Bind memory
source_url: https://github.com/xmrig/xmrig/issues/1175
author: sloppycoffee
assignees: []
labels:
- bug
- NUMA
created_at: '2019-09-17T03:18:03+00:00'
updated_at: '2022-06-10T16:22:48+00:00'
type: issue
status: closed
closed_at: '2019-09-18T16:20:02+00:00'
---

# Original Description
Hate to open an issue but couldn't find any info about this message:

[2019-09-16 20:14:27.290] configuration saved to: "/home/randomx/Downloads/xmrig-3.1.2/config.json"
[2019-09-16 20:14:27.485] use pool donate.v2.xmrig.com:3333  159.89.38.204
[2019-09-16 20:14:27.486] new job from donate.v2.xmrig.com:3333 diff 100001 algo cn-lite/1 height 1132351
[2019-09-16 20:14:27.486]  cpu  use profile  cn-lite  (32 threads) scratchpad 1024 KB
[2019-09-16 20:14:28.351] CPU #00 warning: "can't bind memory"
[2019-09-16 20:14:28.355] CPU #02 warning: "can't bind memory"
[2019-09-16 20:14:28.359] CPU #18 warning: "can't bind memory"
[2019-09-16 20:14:28.359] CPU #28 warning: "can't bind memory"
[2019-09-16 20:14:28.359] CPU #31 warning: "can't bind memory"
[2019-09-16 20:14:28.360] CPU #16 warning: "can't bind memory"
[2019-09-16 20:14:28.360] CPU #12 warning: "can't bind memory"
[2019-09-16 20:14:28.361] CPU #29 warning: "can't bind memory"
[2019-09-16 20:14:28.362] CPU #03 warning: "can't bind memory"
[2019-09-16 20:14:28.362] CPU #14 warning: "can't bind memory"
[2019-09-16 20:14:28.366] CPU #30 warning: "can't bind memory"
[2019-09-16 20:14:28.366] CPU #13 warning: "can't bind memory"
[2019-09-16 20:14:28.366] CPU #01 warning: "can't bind memory"
[2019-09-16 20:14:28.366] CPU #19 warning: "can't bind memory"
[2019-09-16 20:14:28.369] CPU #15 warning: "can't bind memory"
[2019-09-16 20:14:28.370] CPU #17 warning: "can't bind memory"
[2019-09-16 20:14:28.543]  cpu  READY threads 32(32) huge pages 32/32 100% memory 32768 KB (1057 ms)


# Discussion History
## sloppycoffee | 2019-09-17T03:32:39+00:00
Hmm swapped to randomx and got this core dump:

[2019-09-16 20:31:46.196]  rx   init datasets algo rx/test (32 threads) seed 4ea280d70f6567ff...
[2019-09-16 20:31:46.196]  cpu  use profile  rx  (16 threads) scratchpad 2048 KB
[2019-09-16 20:31:46.641]  rx   #1 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-16 20:31:47.698]  rx   #1 allocate done huge pages 1168/1168 100% +JIT (1501 ms)
[2019-09-16 20:31:47.702] CPU #29 warning: "can't bind memory"
[2019-09-16 20:31:47.702] CPU #16 warning: "can't bind memory"
[2019-09-16 20:31:47.702] CPU #01 warning: "can't bind memory"
[2019-09-16 20:31:47.703] CPU #17 warning: "can't bind memory"
[2019-09-16 20:31:47.703] CPU #00 warning: "can't bind memory"
[2019-09-16 20:31:47.703] CPU #12 warning: "can't bind memory"
[2019-09-16 20:31:47.707] CPU #28 warning: "can't bind memory"
[2019-09-16 20:31:47.707] CPU #13 warning: "can't bind memory"
[2019-09-16 20:31:47.724]  cpu  READY threads 16(16) huge pages 16/16 100% memory 32768 KB (1528 ms)
[2019-09-16 20:31:53.075]  rx   #1 init done (6878 ms)
[2019-09-16 20:31:53.093]  rx   #2 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-16 20:31:53.094]  rx   #2 allocate done huge pages 0/1168 0% +JIT (19 ms)
[2019-09-16 20:31:58.139]  rx   #2 init done (5064 ms)
[2019-09-16 20:31:58.167]  rx   #5 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-16 20:31:58.167]  rx   #5 allocate done huge pages 0/1168 0% +JIT (28 ms)
[2019-09-16 20:32:04.072]  rx   #5 init done (5932 ms)
[2019-09-16 20:32:04.090]  rx   #6 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-16 20:32:04.090]  rx   #6 allocate done huge pages 0/1168 0% +JIT (18 ms)
[2019-09-16 20:32:10.102]  rx   #6 init done (6030 ms)
terminate called after throwing an instance of 'std::out_of_range'
  what():  map::at
Aborted (core dumped)


## xmrig | 2019-09-17T06:26:48+00:00
Please run `./xmrig --export-topology` and share resulting `topology.xml` also show output of `lscpu`.

You run miner on complex NUMA hardware, cores where `can't bind memory` error happen likely don't have physical memory also node with index 0 seems unavailable, miner should support this case but something wrong it reason of crash. topology.xml helps understand your hardware topology.
Thank you.

## sloppycoffee | 2019-09-17T17:25:13+00:00
[top.txt](https://github.com/xmrig/xmrig/files/3622705/top.txt)


## sloppycoffee | 2019-09-17T17:26:02+00:00
lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              32
On-line CPU(s) list: 0-31
Thread(s) per core:  1
Core(s) per socket:  8
Socket(s):           4
NUMA node(s):        8
Vendor ID:           AuthenticAMD
CPU family:          16
Model:               9
Model name:          AMD Opteron(tm) Processor 6128
Stepping:            1
CPU MHz:             800.000
CPU max MHz:         2000.0000
CPU min MHz:         800.0000
BogoMIPS:            4000.38
Virtualization:      AMD-V
L1d cache:           64K
L1i cache:           64K
L2 cache:            512K
L3 cache:            5118K
NUMA node0 CPU(s):   0-3
NUMA node1 CPU(s):   4-7
NUMA node2 CPU(s):   8-11
NUMA node3 CPU(s):   12-15
NUMA node4 CPU(s):   16-19
NUMA node5 CPU(s):   20-23
NUMA node6 CPU(s):   24-27
NUMA node7 CPU(s):   28-31
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm 3dnowext 3dnow constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm pni monitor cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt nodeid_msr hw_pstate vmmcall npt lbrv svm_lock nrip_save pausefilter


## sloppycoffee | 2019-09-17T17:27:10+00:00
> Please run `./xmrig --export-topology` and share resulting `topology.xml` also show output of `lscpu`.
> 
> You run miner on complex NUMA hardware, cores where `can't bind memory` error happen likely don't have physical memory also node with index 0 seems unavailable, miner should support this case but something wrong it reason of crash. topology.xml helps understand your hardware topology.
> Thank you.

Are you saying I need more RAM in the machine? That would solve the can't bind warnings?

## xmrig | 2019-09-18T07:02:33+00:00
`std::out_of_range'` error happen because hwloc 2.0.4 filter out NUMA nodes without memory and it makes miner think you have only 4 nodes (not 8), this case needs fix on miner side. You have 2 options, disable NUMA support `"numa": false` in `randomx` object in config file or rebuild miner with hwloc 1.11.x (this version should not filter out empty nodes).

About `can't bind memory` you can ignore this warning, each CPU (as physical package) contains 2 CPU (2 dies) each die support 2 memory channels, right now memory connected to only one die (hwloc don't provide information how many memory sticks you have), so in best case (utilize all memory channels) you should have 16 memory sticks, but anyway this CPU won't perform well on RandomX because it not support AES-NI instructions.

## sloppycoffee | 2019-09-18T16:19:57+00:00
> `std::out_of_range'` error happen because hwloc 2.0.4 filter out NUMA nodes without memory and it makes miner think you have only 4 nodes (not 8), this case needs fix on miner side. You have 2 options, disable NUMA support `"numa": false` in `randomx` object in config file or rebuild miner with hwloc 1.11.x (this version should not filter out empty nodes).
> 
> About `can't bind memory` you can ignore this warning, each CPU (as physical package) contains 2 CPU (2 dies) each die support 2 memory channels, right now memory connected to only one die (hwloc don't provide information how many memory sticks you have), so in best case (utilize all memory channels) you should have 16 memory sticks, but anyway this CPU won't perform well on RandomX because it not support AES-NI instructions.

Thanks for all the info. Ordered some different CPUs (6378). Should have AES-NI support. Sounds like these issues are all contained to how I built the server. Will close this issue for now but if the new cpu/build has the same issue, will reopen. Thank you for the help.

## sloppycoffee | 2019-09-18T16:57:08+00:00
When choosing ram, will hashrate be impacted by unbuffered sticks vs reg sticks? 

Also, can I get by with 16 4gb sticks or will I have more hashrate with 8gb sticks?

For reference, Looking at this item.

https://www.ebay.com/itm/96GB-12X8GB-PC3-12800R-DDR3-1600MHz-ECC-Reg-Server-Memory-RAM-DIMM-Upgrade-Kit/191856069743?hash=item2cab834c6f:g:susAAOSwcwhVKDz8


## xmrig | 2019-09-19T06:46:32+00:00
You can ask here or check recent posts, actually all of them about Ryzens and DDR4, please note DDR3 should be 2-3x slower than DDR4 according this information https://github.com/tevador/RandomX#which-cpu-is-best-for-mining-randomx

Also please take look to this issue #1099 

## sloppycoffee | 2019-10-02T05:25:28+00:00
So update from my side.

I got the 6378 opterons installed and added 16 sticks of ram.

I downloaded the latest 3.2.0 xmrig and changed one line in the config.json.

This line: "url": "randomx-benchmark.xmrig.com:7777"

I still get this error message:
[2019-10-01 22:23:27.158]  rx   #7 init done (4091 ms)
terminate called after throwing an instance of 'std::out_of_range'
  what():  map::at
Aborted (core dumped)


EDIT: Reading your reply above and testing now

EDIT2: disable NUMA support "numa": false in randomx --> Doing this caused this error:
2019-10-01 22:28:55.164]  rx   init dataset algo rx/0 (64 threads) seed 1fada2b0e5787146...
[2019-10-01 22:28:55.164]  cpu  use profile  rx  (56 threads) scratchpad 2048 KB
terminate called after throwing an instance of 'std::out_of_range'
  what():  map::at
Aborted (core dumped)


## sloppycoffee | 2019-10-02T05:29:32+00:00
lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              64
On-line CPU(s) list: 0-63
Thread(s) per core:  2
Core(s) per socket:  8
Socket(s):           4
NUMA node(s):        8
Vendor ID:           AuthenticAMD
CPU family:          21
Model:               2
Model name:          AMD Opteron(tm) Processor 6378
Stepping:            0
CPU MHz:             1398.653
CPU max MHz:         2400.0000
CPU min MHz:         1400.0000
BogoMIPS:            4800.06
Virtualization:      AMD-V
L1d cache:           16K
L1i cache:           64K
L2 cache:            2048K
L3 cache:            6144K
NUMA node0 CPU(s):   0-7
NUMA node1 CPU(s):   8-15
NUMA node2 CPU(s):   16-23
NUMA node3 CPU(s):   24-31
NUMA node4 CPU(s):   32-39
NUMA node5 CPU(s):   40-47
NUMA node6 CPU(s):   48-55
NUMA node7 CPU(s):   56-63
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 popcnt aes xsave avx f16c lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt lwp fma4 tce nodeid_msr tbm topoext perfctr_core perfctr_nb cpb hw_pstate vmmcall bmi1 arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold


## sloppycoffee | 2019-10-02T05:40:18+00:00
How do I downgrade hwloc? Tried multiple versions from: https://github.com/open-mpi/hwloc

All of the .zips don't have a configure file to run and not really sure how to build and install it. 

## xmrig | 2019-10-02T06:08:19+00:00
In version 4.2.1 this issue should be fixed.

## sloppycoffee | 2019-10-02T16:00:49+00:00
> In version 4.2.1 this issue should be fixed.

Perfect. Looking forward to testing it.

## sloppycoffee | 2019-10-03T23:30:45+00:00
Sweet! This version didn't core dump.
https://github.com/xmrig/xmrig/releases/tag/v4.2.1-beta



## Stuperfied | 2021-03-01T07:30:51+00:00
This issue is back

Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              16
On-line CPU(s) list: 0-15
Thread(s) per core:  2
Core(s) per socket:  4
Socket(s):           2
NUMA node(s):        2
Vendor ID:           GenuineIntel
CPU family:          6
Model:               26
Model name:          Intel(R) Xeon(R) CPU           X5550  @ 2.67GHz
Stepping:            5
CPU MHz:             2933.374
BogoMIPS:            5333.40
Virtualisation:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            8192K
NUMA node0 CPU(s):   0,2,4,6,8,10,12,14
NUMA node1 CPU(s):   1,3,5,7,9,11,13,15
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm dca sse4_1 sse4_2 popcnt lahf_lm pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid dtherm ida flush_l1d


## lexo-mfleuti | 2022-06-10T16:22:48+00:00
I fiddled with this now for several hours and the solution is most probably not software related. I documented it here:
https://www.lexo.ch/blog/2022/06/solved-xmrig-cpu-xx-warning-cant-bind-memory-xmrig-does-not-run-on-all-cpu-cores/

Hope this helps!

# Action History
- Created by: sloppycoffee | 2019-09-17T03:18:03+00:00
- Closed at: 2019-09-18T16:20:02+00:00
