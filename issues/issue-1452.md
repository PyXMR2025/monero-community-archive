---
title: Low hashrate when memory installed only on one NUMA node
source_url: https://github.com/xmrig/xmrig/issues/1452
author: Tualua
assignees: []
labels: []
created_at: '2019-12-21T14:22:50+00:00'
updated_at: '2021-04-12T15:07:35+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:07:35+00:00'
---

# Original Description
Hi! I have a problem with hashrate on server with 2 NUMA nodes and 1 memory module installed on 1st node (4Gb or 8Gb)

    xmrig[1737]:  rx   init datasets algo rx/0 (40 threads) seed bf19fddfdae001f8...
    xmrig[1737]:  rx   #1 skipped (can't bind memory)
    xmrig[1737]:  rx   failed to allocate RandomX dataset using 1GB pages
    xmrig[1737]:  rx   #0 allocated 2080 MB huge pages 100% (485 ms)
    xmrig[1737]:  rx   #0 allocated  256 MB huge pages 100% +JIT (55 ms)
    xmrig[1737]:  rx   -- allocated 2336 MB huge pages 100% 1168/1168 (540 ms)
    xmrig[1737]:  rx   #0 dataset ready (4304 ms)
    xmrig[1737]:  cpu  use profile  rx  (18 threads) scratchpad 2048 KB
    xmrig[1737]: CPU #10 warning: "can't bind memory"
    xmrig[1737]: CPU #11 warning: "can't bind memory"
    xmrig[1737]: CPU #12 warning: "can't bind memory"
    xmrig[1737]: CPU #13 warning: "can't bind memory"
    xmrig[1737]: CPU #14 warning: "can't bind memory"
    xmrig[1737]: CPU #15 warning: "can't bind memory"
    xmrig[1737]: CPU #16 warning: "can't bind memory"
    xmrig[1737]: CPU #17 warning: "can't bind memory"
    xmrig[1737]: CPU #18 warning: "can't bind memory"
    xmrig[1737]:  cpu  READY threads 18/18 (18) huge pages 100% 18/18 memory 36864 KB (347 ms)
    xmrig[1737]: speed 10s/60s/15m 4002.2 3942.9 n/a H/s max 4009.5 H/s

As you can see, hashrate is 4k only, but on same server xmr-stak-rx can do 5.5k without any problem. Disabling NUMA has no effect. 

I understand that thos memory setup is far from optimal but may be there is any way to increase hashrate on xmrig?




# Discussion History
## xmrig | 2019-12-21T15:19:24+00:00
Please show full output from begin, and `cpu.txt` from xmr-stak.
Thank you.

## Tualua | 2019-12-22T03:48:43+00:00
I reduced number of threads of xmrig to 16 - better result

Output of xmrig: 

    systemd[1]: Started xmrig daemon.
    xmrig[3323]:  * ABOUT        XMRig/5.4.0 gcc/9.2.1
    xmrig[3323]:  * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
    xmrig[3323]:  * HUGE PAGES   supported
    xmrig[3323]:  * 1GB PAGES    supported
    xmrig[3323]:  * CPU          Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz (2) x64 AES
    xmrig[3323]:                 L2:5.0 MB L3:50.0 MB 20C/40T NUMA:2
    xmrig[3323]:  * MEMORY       5.3/7.8 GB (68%)
    xmrig[3323]:  * DONATE       1%
    xmrig[3323]:  * ASSEMBLY     auto:intel
    xmrig[3323]:  * POOL #1      fin01.supportxmr.com:443 coin monero
    xmrig[3323]:  * POOL #2      fr06.supportxmr.com:443 coin monero
    xmrig[3323]:  * POOL #3      de01.supportxmr.com:443 coin monero
    xmrig[3323]:  * COMMANDS     hashrate, pause, resume
    xmrig[3323]:  * HTTP API     0.0.0.0:1478
    xmrig[3323]:  * OPENCL       disabled
    xmrig[3323]:  * CUDA         disabled
    xmrig[3323]:  net  use pool fin01.supportxmr.com:443 TLSv1.2 95.216.46.125
    xmrig[3323]:  net  fingerprint (SHA-256): "efe8e986720f4631571b03936da48deff25aad8d58168c3403c48150978db2e6"
    xmrig[3323]:  net  new job from fin01.supportxmr.com:443 diff 80000 algo rx/0 height 1994182
    xmrig[3323]:  msr  register values for "custom" preset has been set successfully (3 ms)
    xmrig[3323]:  rx   init datasets algo rx/0 (40 threads) seed bf19fddfdae001f8...
    xmrig[3323]:  rx   #1 skipped (can't bind memory)
    xmrig[3323]:  rx   failed to allocate RandomX dataset using 1GB pages
    xmrig[3323]:  rx   #0 allocated 2080 MB huge pages 100% (495 ms)
    xmrig[3323]:  rx   #0 allocated  256 MB huge pages 100% +JIT (60 ms)
    xmrig[3323]:  rx   -- allocated 2336 MB huge pages 100% 1168/1168 (555 ms)
    xmrig[3323]:  rx   #0 dataset ready (4106 ms)
    xmrig[3323]:  cpu  use profile  rx  (16 threads) scratchpad 2048 KB
    xmrig[3323]: CPU #10 warning: "can't bind memory"
    xmrig[3323]: CPU #11 warning: "can't bind memory"
    xmrig[3323]: CPU #12 warning: "can't bind memory"
    xmrig[3323]: CPU #13 warning: "can't bind memory"
    xmrig[3323]: CPU #14 warning: "can't bind memory"
    xmrig[3323]: CPU #15 warning: "can't bind memory"
    xmrig[3323]: CPU #16 warning: "can't bind memory"
    xmrig[3323]: CPU #17 warning: "can't bind memory"
    xmrig[3323]:  cpu  READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (306 ms)
    xmrig[3323]:  cpu  accepted (1/0) diff 80000 (97 ms)
    xmrig[3323]:  cpu  accepted (2/0) diff 80000 (102 ms)
    xmrig[3323]:  cpu  accepted (3/0) diff 80000 (101 ms)
    xmrig[3323]:  cpu  accepted (4/0) diff 80000 (97 ms)
    xmrig[3323]: speed 10s/60s/15m 4822.8 n/a n/a H/s max 4823.6 H/s
    xmrig[3323]:  cpu  accepted (5/0) diff 80000 (85 ms)
    xmrig[3323]:  cpu  accepted (6/0) diff 80000 (105 ms)
    xmrig[3323]:  cpu  accepted (7/0) diff 80000 (83 ms)

cpu.txt from xmr-stak

    "cpu_threads_conf": [
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 0
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 1
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 2
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 3
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 4
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 5
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 6
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 7
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 10
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 11
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 12
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 13
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 14
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 15
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 16
       },
       {
         "low_power_mode": false,
         "no_prefetch": true,
         "asm": "auto",
         "affine_to_cpu": 17
       }
     ]

# Action History
- Created by: Tualua | 2019-12-21T14:22:50+00:00
- Closed at: 2021-04-12T15:07:35+00:00
