---
title: xmrig crash on ryzen 5 1600X
source_url: https://github.com/xmrig/xmrig/issues/1832
author: oliverlj
assignees: []
labels: []
created_at: '2020-09-14T18:03:57+00:00'
updated_at: '2021-04-12T14:49:10+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:49:10+00:00'
---

# Original Description
 * ABOUT        XMRig/6.3.3 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * 1GB PAGES    disabled
 * HUGE PAGES   supported
 * CPU          AMD Ryzen 5 1600X Six-Core Processor (1) x64 AES
                L2:3.0 MB L3:16.0 MB 6C/12T NUMA:1
 * MEMORY       10.0/23.5 GB (42%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-09-14 19:30:58.506]  net      use pool pool.supportxmr.com:443 TLSv1.2 37.187.95.110
[2020-09-14 19:30:58.506]  net      fingerprint (SHA-256): "b20cea27ba8012ad17fb6f2b8f4c57f3c154f3069277aa67ec010ea8e873023f"
[2020-09-14 19:30:58.506]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2186657
[2020-09-14 19:30:58.506]  cpu      use argon2 implementation AVX2
[2020-09-14 19:30:58.512]  msr      register values for "ryzen" preset has been set successfully (6 ms)
[2020-09-14 19:30:58.512]  randomx  init dataset algo rx/0 (12 threads) seed 4c5e9967f21d94ac...
[2020-09-14 19:30:58.859]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (347 ms)
[2020-09-14 19:31:01.986]  randomx  dataset ready (3127 ms)
[2020-09-14 19:31:01.986]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2020-09-14 19:31:02.129]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (143 ms)
[2020-09-14 19:31:09.441]  cpu      accepted (1/0) diff 50000 (64 ms)

Xmrig is crashing randomly without no log, I don't know why

# Discussion History
## SChernykh | 2020-09-15T18:09:19+00:00
Read https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide - **Faulty first gen Zen CPUs** section.

## oliverlj | 2020-10-07T19:30:02+00:00
wrmsr config seems to work, no restart since 24h of the miner !

# Action History
- Created by: oliverlj | 2020-09-14T18:03:57+00:00
- Closed at: 2021-04-12T14:49:10+00:00
