---
title: Bad performance on AMD Ryzen Threadripper 2950X
source_url: https://github.com/xmrig/xmrig/issues/1101
author: lexansoft
assignees: []
labels: []
created_at: '2019-08-05T17:38:54+00:00'
updated_at: '2019-08-07T02:21:43+00:00'
type: issue
status: closed
closed_at: '2019-08-07T02:21:30+00:00'
---

# Original Description
I see only 3300 H/s on this top of line CPU...

 * ABOUT        XMRig/2.99.4-beta gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * CPU          AMD Ryzen Threadripper 2950X 16-Core Processor (1) x64 AES AVX2
                L2:8.0 MB L3:32.0 MB 16C/32T NUMA:2
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      donate.v2.xmrig.com:3333 algo rx/loki
 * COMMANDS     hashrate, pause, resume
[2019-08-05 10:30:48.722] use pool donate.v2.xmrig.com:3333  185.92.222.223
[2019-08-05 10:30:48.722] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 330074
[2019-08-05 10:30:48.722]  rx   init datasets algo rx/loki (32 threads) seed 4465c1c55f3944b7...
[2019-08-05 10:30:48.722]  cpu  use profile  rx  (16 threads) scratchpad 2048 KB
[2019-08-05 10:30:48.913]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-05 10:30:48.914]  rx   #0 allocate done huge pages 0/1168 0% +JIT (191 ms)
[2019-08-05 10:30:48.915]  cpu  READY threads 16(16) huge pages 0/16 0% memory 32768 KB (192 ms)
[2019-08-05 10:30:52.858]  rx   #0 init done (4135 ms)
[2019-08-05 10:30:52.889]  rx   #1 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-05 10:30:52.889]  rx   #1 allocate done huge pages 0/1168 0% +JIT (32 ms)
[2019-08-05 10:30:56.788]  rx   #1 init done (3930 ms)
[2019-08-05 10:31:48.785] speed 10s/60s/15m 3310.8 n/a n/a H/s max 3312.1 H/s
[2019-08-05 10:32:48.852] speed 10s/60s/15m 3309.8 3310.9 n/a H/s max 3314.2 H/s
[2019-08-05 10:32:59.627] accepted (1/0) diff 1000225 (169 ms)
[2019-08-05 10:33:48.926] speed 10s/60s/15m 3309.8 3309.4 n/a H/s max 3314.2 H/s
[2019-08-05 10:33:58.726] accepted (2/0) diff 1000225 (164 ms)
[2019-08-05 10:34:23.449] Ctrl+C received, exiting
[2019-08-05 10:34:23.455]  cpu  stopped (5 ms)


[xmrig-config.json.zip](https://github.com/xmrig/xmrig/files/3468720/xmrig-config.json.zip)

[topology.xml.zip](https://github.com/xmrig/xmrig/files/3468722/topology.xml.zip)



# Discussion History
## xmrig | 2019-08-05T18:01:23+00:00
https://github.com/xmrig/xmrig/issues/1077#issuecomment-515836516 you need hugepages, absolute minimum in your case is 2368, but better reserve little more as mentioned in the comment.

`allocate done huge pages 0/1168 0%`
`cpu READY threads 16(16) huge pages 0/16 0%`
there should be 100%, make sure CPU is idle, no other heavy tasks, CPU configuration from your config looks perfect.

## xmrig | 2019-08-05T18:03:14+00:00
If press `h` you can view hashrate per thread, all threads should have about same hashrate.

## lexansoft | 2019-08-05T19:02:48+00:00
Yes!

sysctl -w vm.nr_hugepages=2368

helped to get it to 8170 H/s

Thank you. 

Any other tips I can use?

## lexansoft | 2019-08-05T19:05:14+00:00
Why it only uses 16 threads? Should it be 32?

[2019-08-05 21:24:26.626]  rx   init datasets algo rx/loki (32 threads) seed 4465c1c55f3944b7...
[2019-08-05 21:24:26.627]  cpu  use profile  rx  (16 threads) scratchpad 2048 KB

It says it is 32 for rx, but then only starts 16...

## xmrig | 2019-08-06T05:01:11+00:00
For dataset initialization better use all threads (it configurable in `randomx` object in config).
For mining each thread required 2 MB of cache, so 32 / 2 = **16**.
Also please note rx/loki slower that reference RandomX, not to much, but slower.

Next step is memory, for example https://www.reddit.com/r/MoneroMining/comments/clvtc0/randomx_ryzen_7_3700x_and_memory_speed_dependency/ (this CPU also has 32 MB of cache).

## lexansoft | 2019-08-07T02:21:43+00:00
Thank you. Good job!

# Action History
- Created by: lexansoft | 2019-08-05T17:38:54+00:00
- Closed at: 2019-08-07T02:21:30+00:00
