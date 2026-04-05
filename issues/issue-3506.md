---
title: Closing XMRig on Linux doesn't free the allocated memory
source_url: https://github.com/xmrig/xmrig/issues/3506
author: PANCHO7532
assignees: []
labels: []
created_at: '2024-07-03T19:30:19+00:00'
updated_at: '2025-06-16T19:39:48+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:39:48+00:00'
---

# Original Description
**Describe the bug**
XMRig doesn't free the allocated memory when closing the window or by hitting CTRL+C

**To Reproduce**
0. Start a System Monitor and note how much memory do you have before running XMRig
1. Start XMRig
2. After it allocates the huge pages required for the RandomX JIT compiler, hit CTRL+C to exit XMRig or close the terminal
3. If you check on the System Monitor, the allocated memory is still there despite XMRig being closed

**Expected behavior**
The allocated memory by XMRig being freed upon closing the app

**Required data**
 - XMRig version
https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-linux-static-x64.tar.gz
 - Miner log as text or screenshot
```
 * ABOUT        XMRig/6.21.3 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i3-3220 CPU @ 3.30GHz (1) 64-bit -AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       1.3/7.7 GB (16%)
                DIMM_A0: 8 GB DDR3 @ 1600 MHz KHX1600C10D3/8G   
                DIMM_B0: <empty>
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - P8H61-M LX3 R2.0
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      us-va.moneroocean.stream:10128 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2024-07-03 12:01:29.611]  net      use pool us-va.moneroocean.stream:10128  38.175.197.61
[2024-07-03 12:01:29.612]  net      new job from us-va.moneroocean.stream:10128 diff 1121K algo rx/0 height xxxxxx
[2024-07-03 12:01:29.612]  cpu      use argon2 implementation SSSE3
[2024-07-03 12:01:30.812]  randomx  init dataset algo rx/0 (4 threads) seed xxxxxxxxxx...
[2024-07-03 12:01:31.355]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (543 ms)
[2024-07-03 12:01:39.420]  net      new job from us-va.moneroocean.stream:10128 diff 1121K algo rx/0 height xxxxxx
[2024-07-03 12:01:41.377]  randomx  dataset ready (10022 ms)
[2024-07-03 12:01:41.377]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2024-07-03 12:01:41.381]  cpu      READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (4 ms)
[2024-07-03 12:02:37.552]  net      new job from us-va.moneroocean.stream:10128 diff 1280K algo rx/0 height xxxxxxx (124 tx)
[2024-07-03 12:02:37.552]  randomx  init dataset algo rx/0 (4 threads) seed xxxxxxxxxxx...
[2024-07-03 12:02:41.419]  miner    speed 10s/60s/15m 313.0 n/a n/a H/s max 526.6 H/s
[2024-07-03 12:02:46.630]  randomx  dataset ready (9078 ms)
```
 - Config file or command line (without wallets)
 [config.json](https://github.com/user-attachments/files/16089800/config.json)
Command line is just `sudo /opt/xmrig/xmrig`
 - OS: [e.g. Windows]
LMDE 6 Faye x64
 - For GPU related issues: information about GPUs and driver version.
No GPU being used.

**Additional context**
Kinda related to #3430, except that I was experiencing this issue since I've first used XMRig on 6.21.0
I thought it was something temporary that could be fixed by future versions but I've noticed this happening on every Linux machine I've tried running XMRig into and even though 6.21.3 was released with a few changes on how JIT is allocated it isn't.
On Windows it works as intended and frees the memory correctly upon closing the application

# Discussion History
## SChernykh | 2024-07-25T10:57:33+00:00
The OS frees all memory allocated by user-level processes, and it has been like this since forever. What you observe is 100% some misunderstanding of the system monitor.

> If you check on the System Monitor, the allocated memory is still there despite XMRig being closed

Huge pages are not available for normal memory allocation, so they don't count as "free memory" in system monitor. They are however still available for huge page allocation, and next time XMRig starts, it will re-use them. Or it can be any other program that wants to use huge pages - they are actually free and available after XMRig exits.

## d4f5409d | 2024-12-01T18:49:57+00:00
> The OS frees all memory allocated by user-level processes, and it has been like this since forever. What you observe is 100% some misunderstanding of the system monitor.
> 
> > If you check on the System Monitor, the allocated memory is still there despite XMRig being closed
> 
> Huge pages are not available for normal memory allocation, so they don't count as "free memory" in system monitor. They are however still available for huge page allocation, and next time XMRig starts, it will re-use them. Or it can be any other program that wants to use huge pages - they are actually free and available after XMRig exits.

Tell that to me, while my OS crashes because of unavailable allocated huge pages RAM. I've noticed after terminating xmrig the first time in a sudo (huge pages) powered session, it indeed is getting free, however after the second or third time it won't anymore. (Yes it still happens to me to this day)

## SChernykh | 2024-12-01T19:03:08+00:00
Huge pages allocated on Linux remain as free huge pages after xmrig closes. They're not available for "regular" memory allocation, only for huge page memory allocation. If you want to "free" it (make it normal size pages again), try reducing `vm.nr_hugepages` number.

# Action History
- Created by: PANCHO7532 | 2024-07-03T19:30:19+00:00
- Closed at: 2025-06-16T19:39:48+00:00
