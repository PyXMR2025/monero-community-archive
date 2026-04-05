---
title: 1 GB pages lowers the hashrate, doesnt't increase it
source_url: https://github.com/xmrig/xmrig/issues/1904
author: bkmy625
assignees: []
labels: []
created_at: '2020-10-18T18:04:40+00:00'
updated_at: '2021-04-12T14:45:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:45:15+00:00'
---

# Original Description
```
* ABOUT        XMRig/6.3.5 gcc/9.3.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2673 v3 @ 2.40GHz (1) x64 AES
                L2:1.0 MB L3:30.0 MB 4C/4T NUMA:1
 * MEMORY       6.7/13.7 GB (49%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xxxxx algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[  cpu      use argon2 implementation AVX2
[  msr      register values for "intel" preset has been set successfully (11 ms)
[  randomx  init dataset algo rx/0 (4 threads) seed 326af4e7e2321620...
[  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (829 ms)
[  randomx  dataset ready (8732 ms)
[  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (66 ms)
[  miner    speed 10s/60s/15m 1468.7 n/a n/a H/s max 1477.1 H/s
[  net      new job from pool diff 1000K algo rx/0 height 
[  miner    speed 10s/60s/15m 1436.1 1419.1 n/a H/s max 1477.1 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   383.1 |   368.9 |     n/a |
|        1 |        1 |   354.4 |   347.9 |     n/a |
|        2 |        2 |   367.6 |   370.0 |     n/a |
|        3 |        3 |   358.6 |   346.0 |     n/a |
```


After disabling 1GB Pages here is the following

```
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   383.6 |   375.8 |   376.3 |
|        1 |        1 |   368.9 |   367.4 |   369.8 |
|        2 |        2 |   372.4 |   384.6 |   390.9 |
|        3 |        3 |   370.6 |   371.0 |   366.7 |
  miner    speed 10s/60s/15m 1495.5 1498.7 1503.7 H/s max 1553.8 H/s
```



Thats like 80 h/s difference with DISABLED 1 GB pages. Why is this?

# Discussion History
## Lonnegan | 2020-10-19T12:24:57+00:00
Since Intel Xeon E5-2673 v3 natively has 12C/24T and not 4C/4T as detected by xmrig, I assume you are running xmrig in a virtual machine? In this case there are other regularities than bare metal.

## bkmy625 | 2020-10-19T16:39:02+00:00
Yes, so what can be the problem. there are enough resources

## Lonnegan | 2020-10-19T17:25:17+00:00
May be there are enough ressources, but can you be sure what is happening outside the VM? The machine is not in idle on the rest of the cores, is it? So you can't measure the hashrate in the VM in a proper way, because even low activity on the cores/caches influence the hashrate. The fluctuations are too large to be able to say "this is faster than that". You'd have to run for hours to be sure or being 100 percent sure, that there is really nothing outside the VM putting load on the cores while you are measuring.

# Action History
- Created by: bkmy625 | 2020-10-18T18:04:40+00:00
- Closed at: 2021-04-12T14:45:15+00:00
