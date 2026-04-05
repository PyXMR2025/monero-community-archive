---
title: XMRig 6.19.0 segmentation fault Apple M1 Ventura 13.2
source_url: https://github.com/xmrig/xmrig/issues/3209
author: giffeler
assignees: []
labels:
- bug
- arm
- randomx
created_at: '2023-02-09T16:27:40+00:00'
updated_at: '2023-11-23T15:26:45+00:00'
type: issue
status: closed
closed_at: '2023-11-23T15:26:45+00:00'
---

# Original Description
**Describe the bug**
Regardless of the selected compiler (Xcode or gcc in the current version), a segmentation fault occurs after starting the mining process. The error is reproducible on different machines (all Apple with M1 pro or M1 max CPU).

**To Reproduce**
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake .. -GXcode 

Alternatively according to the instructions at https://xmrig.com/docs/miner/build/macos

**Expected behavior**
The program should not produce a segfault under Mac OS.

**Required data**
Here is an example of a program run with stress test:

Debug git:(master) ✗ ./xmrig --stress
 * ABOUT        XMRig/6.19.0 clang/14.0.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.8 hwloc/2.9.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       14.7/16.0 GB (92%)
 * DONATE       1%
 * POOL #1      stratum+ssl://randomx.xmrig.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-02-09 16:52:43.140]  net      use pool randomx.xmrig.com:443 TLSv1.3 199.247.27.41
[2023-02-09 16:52:43.140]  net      fingerprint (SHA-256): "xxx"
[2023-02-09 16:52:43.140]  net      new job from randomx.xmrig.com:443 diff 1000K algo rx/0 height 2818204 (14 tx)
[2023-02-09 16:52:43.140]  cpu      use argon2 implementation default
[2023-02-09 16:52:43.140]  randomx  init dataset algo rx/0 (8 threads) seed 340ecc75cb98be9b...
[2023-02-09 16:52:43.141]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2023-02-09 16:52:43.677]  net      new job from randomx.xmrig.com:443 diff 1000K algo rx/0 height 2818204 (15 tx)
[2023-02-09 16:52:49.414]  randomx  dataset ready (6273 ms)
[2023-02-09 16:52:49.414]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2023-02-09 16:52:49.415]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
[1]    75701 segmentation fault  ./xmrig --stress

**Additional context**
The necessary programs under Homebrew are maintained. There are no problems with other applications in this configuration.

# Discussion History
## Spudz76 | 2023-02-09T20:29:18+00:00
Duplicate #3183 

## SChernykh | 2023-10-19T15:55:16+00:00
Fixed in #3346

# Action History
- Created by: giffeler | 2023-02-09T16:27:40+00:00
- Closed at: 2023-11-23T15:26:45+00:00
