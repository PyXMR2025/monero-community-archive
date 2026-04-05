---
title: OpenCL Disabled yet still sending error msg
source_url: https://github.com/xmrig/xmrig/issues/3026
author: bitmastercoin
assignees: []
labels: []
created_at: '2022-04-17T03:37:19+00:00'
updated_at: '2025-06-28T10:38:36+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:38:36+00:00'
---

# Original Description
originally i was using kali linux and had my RAM all mixed up . so i alligned my ram up and am using a MX Linux live boot off a usb  to try this out with the RAM alligned. Now i am getting open cl error... although i believe i am mining some now, albeit not much.
$ ./xmrig
 * ABOUT        XMRig/6.17.0 gcc/5.4.0
 * LIBS         libuv/1.43.0 OpenSSL/1.1.1m hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU X5550 @ 2.67GHz (1) 64-bit -AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       3.3/8.7 GB (38%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
[2022-04-16 22:35:42.878]  net      use pool rx.unmineable.com:3333  159.65.30.104
[2022-04-16 22:35:42.878]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603635 (6 tx)
[2022-04-16 22:35:42.878]  cpu      use argon2 implementation SSSE3
[2022-04-16 22:35:44.080]  randomx  init dataset algo rx/0 (8 threads) seed ea068db639e0385a...
[2022-04-16 22:35:44.080]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603635 (6 tx)
[2022-04-16 22:35:44.080]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2022-04-16 22:35:51.629]  randomx  dataset ready (7548 ms)
[2022-04-16 22:35:51.629]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:35:51.633]  cpu      READY threads 3/3 (3) huge pages 0% 0/3 memory 6144 KB (4 ms)



 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:32:28.342]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603633 (30 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:32:29.188]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603634 (20 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:32:29.925]  miner    speed 10s/60s/15m 554.7 553.9 610.3 H/s max 636.3 H/s
[2022-04-16 22:32:41.147]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603634 (20 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:32:56.265]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603634 (20 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:33:11.192]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603634 (20 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:33:29.968]  miner    speed 10s/60s/15m 618.5 578.5 607.4 H/s max 636.3 H/s
[2022-04-16 22:33:35.859]  net      no active pools, stop mining
[2022-04-16 22:33:42.311]  net      use pool rx.unmineable.com:3333  159.65.25.23
[2022-04-16 22:33:42.312]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603634 (20 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)
[2022-04-16 22:33:54.831]  cpu      accepted (70/0) diff 100001 (551 ms)
[2022-04-16 22:33:56.399]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2603634 (20 tx)
 * OPENCL       disabled (failed to load OpenCL runtime)


# Discussion History
# Action History
- Created by: bitmastercoin | 2022-04-17T03:37:19+00:00
- Closed at: 2025-06-28T10:38:36+00:00
