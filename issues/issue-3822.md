---
title: 'Can''t submit benchmark: benchmark failed: "Unknown CPU."'
source_url: https://github.com/xmrig/xmrig/issues/3822
author: adapt-L
assignees: []
labels: []
created_at: '2026-06-11T00:12:24+00:00'
updated_at: '2026-06-11T00:26:40+00:00'
type: issue
status: closed
closed_at: '2026-06-11T00:26:40+00:00'
---

# Original Description
**Describe the bug**
I've got a weird CPU, it is an EPYC engineering sample CPU. It doesn't let me submit a bench.

**To Reproduce**
Just run xmrig benchmark on my computer.

**Expected behavior**
It should run and upload the benchmark

 - XMRig version
  6.22.2 
 - Miner log as text or screenshot
 xmrig -t 192 -c /etc/xmrig/config.json --bench=10M --submit 
 * ABOUT        XMRig/6.22.2 gcc/15.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.5.6 
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Eng Sample: 100-000000475-15 (1) 64-bit AES
                threads:192
 * MEMORY       12.3/62.4 GB (20%)
                DIMMA1: 16 GB DDR5 @ 3600 MHz HMCG78MEBRA107N     
                DIMMC1: 16 GB DDR5 @ 3600 MHz M321R2GA3BB6-CQKMS  
                DIMMG1: 16 GB DDR5 @ 3600 MHz HMCG78MEBRA107N     
                DIMMI1: 16 GB DDR5 @ 3600 MHz HMCG78AEBRA168N     
 * MOTHERBOARD  Supermicro - H13SSL-N
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
[2026-06-10 20:08:13.447]  bench    start benchmark hashes 10M algo rx/0
[2026-06-10 20:08:13.447]  cpu      use argon2 implementation AVX-512F
[2026-06-10 20:08:13.457]  msr      register values for "ryzen_19h" preset have been set successfully (10 ms)
[2026-06-10 20:08:13.457]  randomx  init dataset algo rx/0 (192 threads) seed 0000000000000000...
[2026-06-10 20:08:13.788]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (332 ms)
[2026-06-10 20:08:14.395]  randomx  dataset ready (606 ms)
[2026-06-10 20:08:14.395]  cpu      use profile  *  (192 threads) scratchpad 2048 KB
[2026-06-10 20:08:14.814]  cpu      READY threads 192/192 (192) huge pages 100% 192/192 memory 393216 KB (419 ms)
[2026-06-10 20:08:14.961]  bench    benchmark failed: "Unknown CPU."
[2026-06-10 20:08:14.961]  bench    press Ctrl+C to exit
[2026-06-10 20:08:15.407]  cpu      stopped (11 ms)
 - Config file or command line (without wallets)
xmrig -t 192 -c /etc/xmrig/config.json --bench=10M --submit 

the config file just enables 1gb and huge pages.
 - OS: [e.g. Windows]
Gentoo Linux

# Discussion History
## adapt-L | 2026-06-11T00:26:36+00:00
My bad, the hwloc USE flag is disabled by default on gentoo for some reason

# Action History
- Created by: adapt-L | 2026-06-11T00:12:24+00:00
- Closed at: 2026-06-11T00:26:40+00:00
