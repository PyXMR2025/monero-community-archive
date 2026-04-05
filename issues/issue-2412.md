---
title: Hashrate
source_url: https://github.com/xmrig/xmrig/issues/2412
author: japrozs
assignees: []
labels: []
created_at: '2021-05-27T10:09:07+00:00'
updated_at: '2021-05-27T10:31:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
OS : MacOS
Pool : [UnMineable](https://unmineable.com)

I have 16 GB ram on my Intel MacBook Pro. The Miner is saying that it is using `15.6Gb/16Gb` but still I am getting a speed of only `131.7H/s` . Please advice me on how to increase this rate as currently it takes a lot of time to mine cryptocurrency with this `hash rate`.

This is what my output looks like when I'm mining `Dogecoin`:
```shell
[2021-05-27 15:28:38.461]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
[2021-05-27 15:28:45.422]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
[2021-05-27 15:28:49.973]  miner    speed 10s/60s/15m 97.52 104.4 n/a H/s max 131.7 H/s
[2021-05-27 15:29:00.416]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
[2021-05-27 15:29:15.441]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
[2021-05-27 15:29:30.479]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
[2021-05-27 15:29:45.412]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
[2021-05-27 15:29:50.307]  miner    speed 10s/60s/15m 100.2 104.6 n/a H/s max 131.7 H/s
[2021-05-27 15:30:00.418]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370004
```

# Discussion History
## SChernykh | 2021-05-27T10:24:59+00:00
Show console output when xmrig starts up, from the first line until it starts mining.

## japrozs | 2021-05-27T10:27:45+00:00
Here it is :
```bash
 * ABOUT        XMRig/6.12.1 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz (1) 64-bit AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       15.6/16.0 GB (97%)
                DIMM0: 8 GB DDR3 @ 1600 MHz 0x202020202020202020202020202020202020
                DIMM0: 8 GB DDR3 @ 1600 MHz 0x202020202020202020202020202020202020
 * MOTHERBOARD  Apple Inc. - Mac-6F01561E16C75D06
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rx.unmineable.com:3333 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-05-27 15:20:42.658]  net      use pool rx.unmineable.com:3333  139.59.102.100
[2021-05-27 15:20:42.698]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370000
[2021-05-27 15:20:42.698]  cpu      use argon2 implementation SSSE3
[2021-05-27 15:20:42.698]  randomx  init dataset algo rx/0 (4 threads) seed 9df7eacc3696fd98...
[2021-05-27 15:20:44.991]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (2293 ms)
[2021-05-27 15:20:45.064]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370000
[2021-05-27 15:20:59.938]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370000
[2021-05-27 15:21:15.081]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370000
[2021-05-27 15:21:16.545]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:21:30.034]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:21:45.006]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:21:47.471]  randomx  dataset ready (62481 ms)
[2021-05-27 15:21:47.471]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-05-27 15:21:50.623]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (3152 ms)
[2021-05-27 15:22:00.016]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:22:15.035]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:22:17.343]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:22:30.062]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:22:45.281]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2370001
[2021-05-27 15:22:48.011]  miner    speed 10s/60s/15m 125.8 93.86 n/a H/s max 125.9 H/s
```

## SChernykh | 2021-05-27T10:31:44+00:00
i5-3210M should mine at 800 h/s. Your problem is 0% huge pages and also something else is using CPU most likely. Rebooting and closing all other programs might help.

# Action History
- Created by: japrozs | 2021-05-27T10:09:07+00:00
