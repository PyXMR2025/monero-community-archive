---
title: xmrig-6.12.1-msvc-win64 randomx mode light always rejected Low difficulty share
source_url: https://github.com/xmrig/xmrig/issues/2377
author: KirkSuD
assignees: []
labels:
- bug
- randomx
created_at: '2021-05-15T19:01:53+00:00'
updated_at: '2025-06-16T18:50:14+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:50:13+00:00'
---

# Original Description
**Describe the bug**
When I run xmrig-6.12.1-msvc-win64 with randomx's mode set to light, I always get rejected "Low difficulty share".
I tried 2 Windows, both always rejected.
I tested 1 Windows without randomx's mode set to light, always accepted.
I tried to build on my Android armv8 phone and run, always accepted.

**To Reproduce**
My `config.json`:
```
{
    "autosave": false,
    "background": false,
    "randomx": {
        "mode": "light"
    },
    "cpu": {
        "max-threads-hint": 25
    },
    "opencl": true,
    "cuda": false,
    "pools": [
        {
            "url": "mine.c3pool.com:13333",
            "user": "my address",
            "pass": "my worker name",
            "keepalive": true,
            "enabled": true,
            "tls": false
        }
    ]
}
```

**Expected behavior**
Get accepted.

**Required data**
 - Miner output:
```
 * ABOUT        XMRig/6.12.1 MSVC/2019
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 7 4700U with Radeon Graphics (1) 64-bit AES VM
                L2:4.0 MB L3:8.0 MB 8C/8T NUMA:1
 * MEMORY       3.2/7.4 GB (43%)
                DIMM_A0: 4 GB LPDDR4 @ 3200 MHz Unknown
                DIMM_B0: 4 GB LPDDR4 @ 3200 MHz Unknown
 * MOTHERBOARD  my laptop model name
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      mine.c3pool.com:13333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3188.4)
 * OPENCL GPU   #0 03:00.0 AMD Radeon(TM) Graphics (gfx902) 1600 MHz cu:7 mem:2242/3150 MB
 * CUDA         disabled
[2021-05-16 02:26:48.532]  net      use pool mine.c3pool.com:13333  150.109.71.50
[2021-05-16 02:26:48.534]  net      new job from mine.c3pool.com:13333 diff 25000 algo rx/0 height 2361617
[2021-05-16 02:26:48.535]  cpu      use argon2 implementation AVX2
[2021-05-16 02:26:48.536]  msr      to access MSR registers Administrator privileges required.
[2021-05-16 02:26:48.537]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-05-16 02:26:48.537]  randomx  init dataset algo rx/0 (2 threads) seed df91a6d00a489596...
[2021-05-16 02:26:48.538]  randomx  fast RandomX mode disabled by config
[2021-05-16 02:26:48.538]  randomx  failed to allocate RandomX dataset, switching to slow mode (0 ms)
[2021-05-16 02:26:48.940]  randomx  dataset ready (400 ms)
[2021-05-16 02:26:48.940]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-05-16 02:26:48.942]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 |       256 |     8 |    512 | AMD Radeon(TM) Graphics (gfx902)
[2021-05-16 02:26:48.944]  opencl   error CL_INVALID_HOST_PTR when calling clCreateBuffer with buffer size 2181038080
[2021-05-16 02:26:48.948]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (7 ms)
[2021-05-16 02:26:49.216]  opencl   thread #0 failed with error RandomX dataset is not available
[2021-05-16 02:26:49.220]  opencl   thread #0 self-test failed
[2021-05-16 02:26:49.221]  opencl   disabled (failed to start threads)
[2021-05-16 02:27:49.865]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:27:49.866]  miner    speed 10s/60s/15m 80.22 79.86 n/a H/s max 80.41 H/s
[2021-05-16 02:28:31.991]  net      new job from mine.c3pool.com:13333 diff 25000 algo rx/0 height 2361618
[2021-05-16 02:28:51.177]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:28:51.177]  miner    speed 10s/60s/15m 80.14 80.19 n/a H/s max 80.41 H/s
[2021-05-16 02:29:24.643]  net      new job from mine.c3pool.com:13333 diff 25000 algo rx/0 height 2361619
[2021-05-16 02:29:32.028]  net      new job from mine.c3pool.com:13333 diff 18398 algo rx/0 height 2361619
[2021-05-16 02:29:52.373]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:29:52.373]  miner    speed 10s/60s/15m 79.88 78.69 n/a H/s max 80.41 H/s
[2021-05-16 02:30:31.210]  net      new job from mine.c3pool.com:13333 diff 18398 algo rx/0 height 2361620
[2021-05-16 02:30:31.742]  net      new job from mine.c3pool.com:13333 diff 9898 algo rx/0 height 2361620
[2021-05-16 02:30:53.536]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:30:53.536]  miner    speed 10s/60s/15m 78.55 78.73 n/a H/s max 80.63 H/s
[2021-05-16 02:31:11.780] no results yet
[2021-05-16 02:31:31.731]  net      new job from mine.c3pool.com:13333 diff 4196 algo rx/0 height 2361620
[2021-05-16 02:31:54.502]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:31:54.503]  miner    speed 10s/60s/15m 74.15 78.85 n/a H/s max 80.63 H/s
[2021-05-16 02:32:31.665]  net      new job from mine.c3pool.com:13333 diff 1467 algo rx/0 height 2361620
[2021-05-16 02:32:55.643]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:32:55.643]  miner    speed 10s/60s/15m 79.80 77.77 n/a H/s max 80.63 H/s
[2021-05-16 02:33:16.179]  cpu      rejected (0/1) diff 1467 "Low difficulty share" (89 ms)
[2021-05-16 02:33:37.682]  cpu      rejected (0/2) diff 1467 "Unauthenticated" (9079 ms)
[2021-05-16 02:33:37.683]  net      no active pools, stop mining
[2021-05-16 02:33:52.837]  net      mine.c3pool.com:13333 error: "New connections from this IP address are temporarily suspended from mining (10 minutes max)", code: -1
[2021-05-16 02:33:52.838]  net      mine.c3pool.com:13333 read error: "end of file"
[2021-05-16 02:33:56.692]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:33:56.693]  miner    speed 10s/60s/15m n/a 54.36 n/a H/s max 80.63 H/s
[2021-05-16 02:33:58.636]  net      use pool mine.c3pool.com:13333  206.119.80.236
[2021-05-16 02:33:58.637]  net      new job from mine.c3pool.com:13333 diff 25000 algo rx/0 height 2361621
[2021-05-16 02:34:44.197]  cpu      rejected (0/3) diff 25000 "Low difficulty share" (121 ms)
[2021-05-16 02:34:55.009]  cpu      rejected (0/4) diff 25000 "Unauthenticated" (9343 ms)
[2021-05-16 02:34:55.009]  net      no active pools, stop mining
[2021-05-16 02:34:57.815]  opencl   #0 03:00.0   0W  0C    0RPM 0/0MHz
[2021-05-16 02:34:57.815]  miner    speed 10s/60s/15m 55.67 72.94 n/a H/s max 80.63 H/s
[2021-05-16 02:35:00.374]  net      use pool mine.c3pool.com:13333  124.156.188.48
[2021-05-16 02:35:00.375]  net      new job from mine.c3pool.com:13333 diff 25000 algo rx/0 height 2361621
```
 - Config file: above.
 - OS: Windows 10
 - For GPU related issues: not a GPU-related problem.

**Additional context**
I'm a newbie in this field.
If this is a known issue, just close it and ignore me.
Also, I don't really care about it much because light mode can hardly be profitable.
Just playing around, found this problem, and want to share.
I suspect there's something wrong in light mode.
Thanks.


# Discussion History
## SChernykh | 2021-05-15T19:26:51+00:00
I confirm the bug. I'll look into it.

# Action History
- Created by: KirkSuD | 2021-05-15T19:01:53+00:00
- Closed at: 2025-06-16T18:50:13+00:00
