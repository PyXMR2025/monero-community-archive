---
title: 5.5.2 crashes
source_url: https://github.com/xmrig/xmrig/issues/1527
author: vegaminer
assignees: []
labels:
- bug
created_at: '2020-02-02T14:33:41+00:00'
updated_at: '2020-02-03T06:59:05+00:00'
type: issue
status: closed
closed_at: '2020-02-03T06:59:05+00:00'
---

# Original Description
Note: 5.5.1 works just fine

Both gcc and msvc verisons are crashing
This is GCC log
```
 * ABOUT        XMRig/5.5.2 gcc/9.2.0
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD FX(tm)-8350 Eight-Core Processor (1) x64 AES
                L2:8.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       2.5/7.9 GB (32%)
 * DONATE       5%
 * ASSEMBLY     auto:bulldozer
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-02-02 17:27:27.762]  net  use pool pool.supportxmr.com:443 TLSv1.2 95.216.46.125
[2020-02-02 17:27:27.764]  net  fingerprint (SHA-256): "efe8e986720f4631571b03936da48deff25aad8d58168c3403c48150978db2e6"
[2020-02-02 17:27:27.764]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2024815
[2020-02-02 17:27:27.764]  rx   init dataset algo rx/0 (8 threads) seed 4301c262ef34ec54...
[2020-02-02 17:27:27.795]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (30 ms)
[2020-02-02 17:27:34.558]  rx   dataset ready (6762 ms)
[2020-02-02 17:27:34.559]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2020-02-02 17:27:34.568] [THREAD 2252] Access violation at 0x00000000004af93f: read at address 0xffffffffffffffff
``` 

And this is MSVC log

```
* ABOUT        XMRig/5.5.2 MSVC/2019
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD FX(tm)-8350 Eight-Core Processor (1) x64 AES
                L2:8.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       2.6/7.9 GB (32%)
 * DONATE       5%
 * ASSEMBLY     auto:bulldozer
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-02-02 17:29:31.943]  net  use pool pool.supportxmr.com:443 TLSv1.2 149.202.83.171
[2020-02-02 17:29:31.945]  net  fingerprint (SHA-256): "f5725c18577243b1a5bbff1bdad26b56cc13b5e96150ca6897330f015852b954"
[2020-02-02 17:29:31.945]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2024820
[2020-02-02 17:29:31.945]  rx   init dataset algo rx/0 (8 threads) seed 4301c262ef34ec54...
[2020-02-02 17:29:31.976]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (31 ms)
[2020-02-02 17:29:38.843]  rx   dataset ready (6866 ms)
[2020-02-02 17:29:38.843]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2020-02-02 17:29:38.846] [THREAD 2944] Access violation at 0x000002A3CD431AF8: read at address 0xFFFFFFFFFFFFFFFF
[2020-02-02 17:29:38.846] [THREAD 2944] Access violation at 0x000002A3CD431A5C: read at address 0xFFFFFFFFFFFFFFFF
[2020-02-02 17:29:38.846] [THREAD 2944] Access violation at 0x000002A3CD431990: read at address 0xFFFFFFFFFFFFFFFF
[2020-02-02 17:29:38.846] [THREAD 2944] Access violation at 0x000002A3CD4319EE: read at address 0xFFFFFFFFFFFFFFFF
[2020-02-02 17:29:38.846] [THREAD 2944] Access violation at 0x000002A3CD4319FA: read at address 0xFFFFFFFFFFFFFFFF
[2020-02-02 17:29:38.846] [THREAD 2944] Access violation at 0x000002A3CD4319C1: read at address 0xFFFFFFFFFFFFFFFF
[2020-02-02 17:29:38.846] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD431648
[2020-02-02 17:29:38.846] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310CD
[2020-02-02 17:29:38.847] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4318BF
[2020-02-02 17:29:38.847] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310B0
[2020-02-02 17:29:38.848] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310C0
[2020-02-02 17:29:38.848] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310B6
[2020-02-02 17:29:38.848] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310C4
[2020-02-02 17:29:38.849] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310B0
[2020-02-02 17:29:38.849] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310B8
[2020-02-02 17:29:38.850] [THREAD 2944] Exception 0xC0000090 at 0x000002A3CD4310B0
...
[2020-02-02 17:29:42.473]  cpu  stopped (22 ms)

```

# Discussion History
## xmrig | 2020-02-02T16:21:21+00:00
Please check fix #1529
Thank you.

## xmrig | 2020-02-02T17:09:06+00:00
Fixed in v5.5.3.

## vegaminer | 2020-02-03T05:16:41+00:00
Fixed. Thank you!

# Action History
- Created by: vegaminer | 2020-02-02T14:33:41+00:00
- Closed at: 2020-02-03T06:59:05+00:00
