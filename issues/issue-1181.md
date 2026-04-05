---
title: Exit without error
source_url: https://github.com/xmrig/xmrig/issues/1181
author: ivarsdzalbs
assignees: []
labels: []
created_at: '2019-09-19T21:55:40+00:00'
updated_at: '2019-12-22T19:26:44+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:26:44+00:00'
---

# Original Description
Having issues where xmrig will just terminate without any errors or anything. System spec: Windows 10 pro running from 32gb USB stick, 8GB ram. Any suggestions?

```
C:\Users\RandomX_1\Desktop\xmrig-4.0.0-beta>xmrig
 * ABOUT        XMRig/4.0.0-beta gcc/9.2.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          AMD Ryzen 7 1700 Eight-Core Processor (1) x64 AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      randomx-benchmark.xmrig.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled (no devices)
[2019-09-19 14:54:09.315] use pool randomx-benchmark.xmrig.com:7777  178.128.242.134
[2019-09-19 14:54:09.330] new job from randomx-benchmark.xmrig.com:7777 diff 1000225 algo rx/test height 362543
[2019-09-19 14:54:09.330]  rx   init dataset algo rx/test (16 threads) seed 4ea280d70f6567ff...
[2019-09-19 14:54:09.330]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-09-19 14:54:09.330]  rx   #0 allocate done huge pages 1168/1168 100% +JIT (6 ms)
[2019-09-19 14:54:12.220]  rx   #0 init done 1/1 (2900 ms)
[2019-09-19 14:54:12.233]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-09-19 14:54:12.236]  cpu  READY threads 8(8) huge pages 8/8 100% memory 16384 KB (1 ms)

C:\Users\RandomX_1\Desktop\xmrig-4.0.0-beta>
```

# Discussion History
## SChernykh | 2019-09-23T15:02:32+00:00
Ryzen 7 1700 CPUs are known to be unstable on RandomX, at least the very first revisions without BIOS updates. Try to update BIOS to the latest version and remove any overclock (if there is any).

## xmrig | 2019-11-25T16:37:23+00:00
https://github.com/xmrig/xmrig/issues/1297#issuecomment-558233482

# Action History
- Created by: ivarsdzalbs | 2019-09-19T21:55:40+00:00
- Closed at: 2019-12-22T19:26:44+00:00
