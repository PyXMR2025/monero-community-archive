---
title: Optimization on the latest Xeon with HT?
source_url: https://github.com/xmrig/xmrig/issues/1485
author: buzaiq
assignees: []
labels: []
created_at: '2020-01-05T08:11:44+00:00'
updated_at: '2021-04-12T15:04:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:04:26+00:00'
---

# Original Description
9242 is the new Xeon platinum from Intel - with up to 56 core per processor - from what I understand, it is actually Multiple Chip Package (MCP).

Running XMRig 5.5.0 on 2x 9242 (48C, 2.3GHz), with HT enabled - lscpu says 192 logical cores, but XMRig only uses 96 cores.

I know that RandomX requires 256kb of L2 per thread, 9242 does have enough amount of L2, any chance to improve the performance there by fully utilizing the additional logical cores?

9242 is Cascade Lake generation, and cache sizes as below:
**Level 1 cache size  | 48 x 32 KB instruction caches & 48 x 32 KB data caches
Level 2 cache size  | 48 x 1 MB caches**

Looks like the dataset was on 192 threads, but - cpu only uses the 96 threads profile from the miner log:
    _rx   init datasets algo rx/0 (192 threads) seed f5f03b8c0e01930c..._
    ...
    _cpu  use profile  rx  (96 threads) scratchpad 2048 KB_


```
[root@localhost xmrig-5.5.0]# lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                192
On-line CPU(s) list:   0-191
Thread(s) per core:    2
Core(s) per socket:    24
Socket(s):             4
NUMA node(s):          4
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 85
Model name:            Genuine Intel(R) CPU 0000%@
Stepping:              6
CPU MHz:               999.963
CPU max MHz:           3800.0000
CPU min MHz:           1000.0000
BogoMIPS:              4400.00
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              1024K
L3 cache:              36608K
NUMA node0 CPU(s):     0-23,96-119
NUMA node1 CPU(s):     24-47,120-143
NUMA node2 CPU(s):     48-71,144-167
NUMA node3 CPU(s):     72-95,168-191
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch epb cat_l3 cdp_l3 intel_pt ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm mpx rdt_a avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req pku ospke avx512_vnni spec_ctrl intel_stibp flush_l1d arch_capabilities

``` 
**Required data** - Miner log:
```
[root@localhost]# ./xmrig
 * ABOUT        XMRig/5.5.0 gcc/5.4.0
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Genuine Intel(R) CPU 0000%@ (4) x64 AES
                L2:96.0 MB L3:143.0 MB 96C/192T NUMA:4
 * MEMORY       11.8/187.3 GB (6%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xxx.xxx.com:00000 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-01-05 15:39:50.116]  net  use pool xxx.xxx.com:00000  203.107.32.162
[2020-01-05 15:39:50.117]  net  new job from xxx.xxx.com:00000 diff 32768 algo rx/0 height 2004439
[2020-01-05 15:39:50.136]  msr  register values for "intel" preset has been set successfully (20 ms)
[2020-01-05 15:39:50.136]  rx   init datasets algo rx/0 (192 threads) seed f5f03b8c0e01930c...
[2020-01-05 15:39:51.252]  rx   #0 allocated 2080 MB huge pages 100% (1115 ms)
[2020-01-05 15:39:51.688]  rx   #1 allocated 2080 MB huge pages 100% (1551 ms)
[2020-01-05 15:39:52.126]  rx   #3 allocated 2080 MB huge pages 100% (1989 ms)
[2020-01-05 15:39:52.128]  rx   #2 allocated 2080 MB huge pages 100% (1991 ms)
[2020-01-05 15:39:52.193]  rx   #0 allocated  256 MB huge pages 100% +JIT (65 ms)
[2020-01-05 15:39:52.194]  rx   -- allocated 8576 MB huge pages 100% 4288/4288 (2057 ms)
[2020-01-05 15:39:53.486]  rx   #0 dataset ready (1293 ms)
[2020-01-05 15:39:53.852]  rx   #1 dataset ready (366 ms)
[2020-01-05 15:39:54.173]  rx   #3 dataset ready (686 ms)
[2020-01-05 15:39:54.173]  rx   #2 dataset ready (686 ms)
[2020-01-05 15:39:54.173]  cpu  use profile  rx  (96 threads) scratchpad 2048 KB
[2020-01-05 15:39:56.105]  cpu  READY threads 96/96 (96) huge pages 100% 96/96 memory 196608 KB (1932 ms)
[2020-01-05 15:39:56.156]  cpu  accepted (1/0) diff 32768 (24 ms)

```

# Discussion History
## SChernykh | 2020-01-05T12:47:38+00:00
This CPU doesn't have enough L3 cache for more threads, so 1 thread per physical core might be optimal. You can try to decrease or increase the number of threads to see if hashrate gets better.

## buzaiq | 2020-01-05T18:48:39+00:00
`One 9242 has 71.5MB L3 cache.
`


Trying with command line:

`[root@a1 xmrig-5.4.0]# ./xmrig --donate-level 1 --threads=192 -o xmr.f2pool.com:13531 -u xxxxxxxxxxx -p x -k...
`
Hash rate dropped 70%. to a very low #..

Is this the right way to set up additional threads?

However:

`[root@a1 xmrig-5.4.0]# ./xmrig --donate-level 1 --threads=96 -o xmr.f2pool.com:13531 -u xxxxxxxxxxx -p x -k...
`
Setting back to 96 threads with command line... hash rate dropped 30% as well... guess the command line I used is not optimal...

## GjBrutello | 2020-01-06T08:16:27+00:00
1 processor - 35 threads is optimal for the proc, so set 70 threads  for your "2x 9242".

## srwx666 | 2020-01-11T23:40:24+00:00
by usnig --threads (not depending on hwloc) you have to use also affinity as far as i remember.


# Action History
- Created by: buzaiq | 2020-01-05T08:11:44+00:00
- Closed at: 2021-04-12T15:04:26+00:00
