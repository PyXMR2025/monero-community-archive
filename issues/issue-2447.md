---
title: Dual E5-2680v4() only doing 11kh/s
source_url: https://github.com/xmrig/xmrig/issues/2447
author: SuperFreeMan-CXM
assignees: []
labels: []
created_at: '2021-06-17T17:11:58+00:00'
updated_at: '2024-09-08T15:28:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,
I am running 2x Intel E5-2680 v4  (28 Cores total) , and get  CPU #XX warning: "can't bind memory".
I want to figure out whether this warning will hurt hashrate？And how can I fix it?
Can anyone point me to the right direction to maximize the hash rates?


`CPU          Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (2) 64-bit AES
                L2:7.0 MB L3:70.0 MB 28C/56T NUMA:2
 * MEMORY       61.4/62.7 GB (98%)
                DIMM_A1: 16 GB DDR4 @ 2133 MHz M393A2G40DB0-CPB    
                DIMM_B1: 16 GB DDR4 @ 2133 MHz M393A2G40DB0-CPB    
                DIMM_C1: 16 GB DDR4 @ 2133 MHz M393A2G40DB0-CPB    
                DIMM_D1: 16 GB DDR4 @ 2133 MHz M393A2G40DB0-CPB    
 * MOTHERBOARD  HUANANZHI - X99 F8D
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-06-18 00:10:37.620]  net      use pool pool.supportxmr.com:443 TLSv1.2 139.99.125.38
[2021-06-18 00:10:37.620]  net      fingerprint (SHA-256): "d7b39698f68a15b35b6b8a00324a0075873a100ead7f75a10c6e6a7be710d4cc"
[2021-06-18 00:10:37.620]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2385297
[2021-06-18 00:10:37.620]  cpu      use argon2 implementation AVX2
[2021-06-18 00:10:37.627]  msr      register values for "intel" preset have been set successfully (6 ms)
[2021-06-18 00:10:37.627]  randomx  init dataset algo rx/0 (56 threads) seed 8eedbfcfd60676c5...
[2021-06-18 00:10:38.064]  randomx  #0 allocated 2080 MB huge pages 100% (437 ms)
[2021-06-18 00:10:38.115]  randomx  #0 allocated  256 MB huge pages 100% +JIT (50 ms)
[2021-06-18 00:10:38.115]  randomx  -- allocated 2336 MB huge pages 100% 1168/1168 (488 ms)
[2021-06-18 00:10:39.753]  randomx  #0 dataset ready (1637 ms)
[2021-06-18 00:10:39.753]  cpu      use profile  rx  (28 threads) scratchpad 2048 KB
[2021-06-18 00:10:39.756] CPU #14 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #15 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #16 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #17 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #18 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #19 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #22 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #21 warning: "can't bind memory"
[2021-06-18 00:10:39.756] CPU #20 warning: "can't bind memory"
[2021-06-18 00:10:39.757] CPU #24 warning: "can't bind memory"
[2021-06-18 00:10:39.757] CPU #23 warning: "can't bind memory"
[2021-06-18 00:10:39.757] CPU #25 warning: "can't bind memory"
[2021-06-18 00:10:39.762] CPU #26 warning: "can't bind memory"
[2021-06-18 00:10:39.764] CPU #27 warning: "can't bind memory"
[2021-06-18 00:10:39.827]  cpu      READY threads 28/28 (28) huge pages 100% 28/28 memory 57344 KB (73 ms)
`

# Discussion History
## Spudz76 | 2021-06-17T19:32:11+00:00
Using hwloc?  It's required for proper dual CPU memory assignment.  You also cut off the most important top few lines of output (where all the libs and versions are...)

Ensure evenly half the sticks are in each CPU's slots (refer to motherboard manual).

Also `hwloc-ls` should show stuff like this:
```
root@dualrig:~# hwloc-ls  | grep NUMANode
    NUMANode L#0 (P#0 24GB)
    NUMANode L#1 (P#1 24GB)
```

See how I have 48GB total, while 24GB is on each Node (processor)?

## Spudz76 | 2021-06-17T19:49:40+00:00
NUMA should be enabled in BIOS some boards default it off for some reason.

Also in the [normal range of speed](https://xmrig.com/benchmark/59XkAS) (click the Memory header) for something with empty slots (sometimes means not the full available buswidth) and/or 2400MHz slow RDIMMs.

And yours are 2133 across two sticks per CPU (if they were in the right slots) so yeah you're probably getting what that setup should.  Figure out from motherboard manual how to ensure full widths and run maximum speed DDR4 (probably won't be RDIMM so see what rules the board has for using normal desktop UDIMMs) and readjust the memory accordingly for minimum latency.

Although top result did use 2133 with packed slots for max width, so maybe that's all that is holding you back.  I'm not sure how your output didn't list a bunch more empty slots (server board with four slots would be super odd).

This is mainly why server boards rarely are any improvement over single processor cheap desktop boards (many times you need a lot more sticks of memory / minimum as many as you would need for two separate boards anyway / sometimes even more sticks -- and then the minimum size you can find being 4GB if you need 16 sticks you have to buy 64GB when you only actually needed ~8GB for RandomX mining).

## Ultrafreak2103 | 2024-09-08T09:39:28+00:00
Hallo zusammen,

ich habe das selbe Problem. Habe einen Huawei Server mit Dual CPU 2680v4. Mit 6x 16gb RAM sauber verteilt auf beide CPU,s dazu ist Numa an .L2:7.0 MB L3:70.0 MB 28C/56T NUMA:2

Nun habe ich das Problem das er immer nur 28 Threads nutzt. Und wenn ich Manuel die core oder Thred Zuweisung mache sinkt meine Hash rate massiv . Aktuell liege ich mit 28 Threads von 56 Threads bei 12 Kh's. Wie muss ich die Cores sauber zuweisen das es funktioniert? 

Grüße Alex

## Spudz76 | 2024-09-08T15:28:45+00:00
https://xmrig.com/benchmark?cpu=Intel%28R%29+Xeon%28R%29+CPU+E5-2680+v4+%40+2.40GHz

~14KH/s is maximum, 28 threads is correct.

# Action History
- Created by: SuperFreeMan-CXM | 2021-06-17T17:11:58+00:00
