---
title: Crash under WSL v1
source_url: https://github.com/xmrig/xmrig/issues/2802
author: red-scorp
assignees: []
labels: []
created_at: '2021-12-07T19:20:29+00:00'
updated_at: '2022-07-24T22:07:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I've built xmrig in WSL/Ubuntu under Windows 10. When I'm staring the miner it crashes nearly immediately.

**To Reproduce**
1. sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. cmake ..
5. make -j$(nproc)
6. /home/xxx/xmrig/build/xmrig -o gulf.moneroocean.stream:10128 -u 481xf...Ta3yz -p xxx

**Expected behavior**
I would like it to start digging

**Required data**
` * ABOUT        XMRig/6.16.2 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i9-7900X CPU @ 3.30GHz (1) 64-bit AES
                L2:0.0 MB L3:0.0 MB 10C/20T NUMA:1
 * MEMORY       7.2/63.7 GB (11%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-12-07 20:14:36.273]  net      use pool gulf.moneroocean.stream:10128  195.201.124.214
[2021-12-07 20:14:36.274]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2509799 (28 tx)
[2021-12-07 20:14:36.275]  cpu      use argon2 implementation AVX-512F
[2021-12-07 20:14:36.285]  msr      msr kernel module is not available
[2021-12-07 20:14:36.285]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-12-07 20:14:36.286]  randomx  init dataset algo rx/0 (20 threads) seed 72e85eed124de1b5...
[2021-12-07 20:14:36.286]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2021-12-07 20:14:38.762]  randomx  dataset ready (2476 ms)
[2021-12-07 20:14:38.763]  cpu      use profile  rx  (10 threads) scratchpad 2048 KB
Aborted (core dumped)
`

**Additional context**
Sucks. I understand WSL v1 is not a real linux, but it's sucks anyway.
Works under WSL v2

# Discussion History
## Zitt | 2022-07-24T22:07:42+00:00
Doesn't work of me under WSL2.
Running with Ubuntu binaries and also tried using a compiled binary with same result.
I also can't get a core dump.

# Action History
- Created by: red-scorp | 2021-12-07T19:20:29+00:00
