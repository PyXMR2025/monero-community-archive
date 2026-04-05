---
title: eypc9654 lower hashrate
source_url: https://github.com/xmrig/xmrig/issues/3597
author: duguguang
assignees: []
labels:
- question
created_at: '2024-12-12T03:46:58+00:00'
updated_at: '2025-06-16T19:32:02+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:32:02+00:00'
---

# Original Description
**Describe the bug**
eypc9654 hashrate is only 6kh/s

**To Reproduce**
run benchmark_10M with admin.

**Expected behavior**
hashrate same with the benchmark with  webpage

**Required data**
 - XMRig version: 6.22
 - Miner log 
   -  * ABOUT        XMRig/6.22.2 MSVC/2019 (built for Windows x86-64, 64 bit)
   * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
   * HUGE PAGES   permission granted
   * 1GB PAGES    unavailable
   * CPU          AMD Eng Sample: 100-000000475-15 (1) 64-bit AES
                  L2:96.0 MB L3:384.0 MB 96C/192T NUMA:1
   * MEMORY       3.7/31.8 GB (12%)
                  DIMMC1: 16 GB DDR5 @ 3600 MHz HMCG78AEBRA107N
                  DIMME1: 16 GB DDR5 @ 3600 MHz HMCG78AEBRA107N
   * MOTHERBOARD  Supermicro - H13SSL-N
   * DONATE       0%
   * ASSEMBLY     auto:ryzen
   * POOL #1      benchmark algo auto
   * COMMANDS     hashrate, pause, resume, results, connection
   * OPENCL       disabled
   * CUDA         disabled
  [2024-12-12 11:35:56.017]  bench    start benchmark hashes 10M algo rx/0
  [2024-12-12 11:35:56.018]  cpu      use argon2 implementation AVX-512F
  [2024-12-12 11:35:56.019]  msr      service WinRing0_1_2_0 already exists
  [2024-12-12 11:35:56.019]  msr      service path: "\??\C:\WC\xmrig-6.22.2-gcc-win64\xmrig-6.22.2\WinRing0x64.sys"
  [2024-12-12 11:35:56.020]  msr      service WinRing0_1_2_0 already exists, but with a different service name
  [2024-12-12 11:35:56.416]  msr      register values for "ryzen_19h" preset have been set successfully (398 ms)
  [2024-12-12 11:35:56.416]  randomx  init dataset algo rx/0 (192 threads) seed 0000000000000000...
  [2024-12-12 11:35:56.417]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
  [2024-12-12 11:35:58.033]  randomx  dataset ready (1616 ms)
  [2024-12-12 11:35:58.033]  cpu      use profile  rx  (192 threads) scratchpad 2048 KB
  [2024-12-12 11:35:58.088]  cpu      READY threads 192/192 (192) huge pages 100% 192/192 memory 393216 KB (54 ms)
  [2024-12-12 11:35:59.034]  bench    seed 2a04f27c3611a4c9282208af1291469f7d27ae1d3cc5505ba71bf5cfcb054f32
  [2024-12-12 11:36:58.188]  miner    speed 10s/60s/15m 5668.3 n/a n/a H/s max 5803.0 H/s
  [2024-12-12 11:36:58.263]  bench     3.35% 335344/10000000 (60.208s)

![2022资源占用](https://github.com/user-attachments/assets/7ea8236b-4193-49b5-8f55-38955c341dfb)

 - Config file: Keep dafault
 - OS: [Windows Server2022]

**Additional context**
Windows Server 2022Standard 21H2 OSVersion:20348.2700
CPU-Z multiprocessor Score: 47000



# Discussion History
## SChernykh | 2024-12-12T08:42:58+00:00
This CPU has 12 memory channels, and you use only 2 channels (2 memory sticks). You should also check that nothing else is using CPU when you run the benchmark.

## duguguang | 2024-12-12T09:29:51+00:00
> This CPU has 12 memory channels, and you use only 2 channels (2 memory sticks). You should also check that nothing else is using CPU when you run the benchmark.

When i decrease the thread to 48 by the param '-t 48', the hashrate increase to the maxium about 17k,  if i add the thread num again, hashrate will down, next i will increase the ram nums , thanks!

# Action History
- Created by: duguguang | 2024-12-12T03:46:58+00:00
- Closed at: 2025-06-16T19:32:02+00:00
