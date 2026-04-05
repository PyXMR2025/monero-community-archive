---
title: Whether 32-bit operating system is supported
source_url: https://github.com/xmrig/xmrig/issues/1453
author: ainy0293
assignees: []
labels:
- bug
created_at: '2019-12-21T16:54:59+00:00'
updated_at: '2020-08-19T01:27:37+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:27:37+00:00'
---

# Original Description
I use a 32-bit system and can't run it.

I compiled with this method:  https://github.com/xmrig/xmrig/wiki/windows-build


Then run it with the following command, but the program will exit automatically.

```
xmrig.exe --donate-level=1  --url=pool.supportxmr.com:3333 --user=WalletAddress.MinerName  --pass=x -k
```

 The console logs are as follows: 
 ```
 * ABOUT        XMRig/5.3.0 gcc/9.2.0
 * LIBS         libuv/1.15.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz (2) -x64 AES
                L2:0.5 MB L3:16.0 MB 4C/8T NUMA:1
 * MEMORY       0.5/3.0 GB (18%)
 * DONATE       1%
 * POOL #1      pool.supportxmr.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-22 00:40:45.834]  net  use pool pool.supportxmr.com:3333  94.23.247.226

[2019-12-22 00:40:45.849]  net  new job from pool.supportxmr.com:3333 diff 50000
 algo rx/0 height 1993854
[2019-12-22 00:40:45.865]  rx   init dataset algo rx/0 (4 threads) seed bf19fddf
dae001f8...
[2019-12-22 00:40:45.958]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/116
8 -JIT (41 ms)

```


# Discussion History
## xmrig | 2019-12-21T17:24:16+00:00
Can you provide little more information about your 32 bit OS, because miner successfully allocated full dataset, it not possible without modifying boot parameters.
Thank you.

## ainy0293 | 2019-12-22T02:54:16+00:00
I used Windows 7 ultimate 32, with SP1 patch.
Memory is 3GB, In fact, the 32 bit system only supports 3GB's memory capacity.
Compiling with msys2 32bit, Xmrig-deps is version 4.0.

To execute xmrig.exe directly is to use config.json configuration file. If I don't make any changes to this file, I can mine and the program will not exit automatically.

When I change the <code>pools</code> in the config.json configuration file to <code>pool.supportxmr.com:3333</code>, the program will exit automatically, and the last line will show the red <code>-JIT</code> .

The pools in the config.json configuration file are <code>donate.v2.xmrig.com:3333</code> .

From the current phenomenon, is it related to the ore pool?

Do you need any more information? 

## xmrig | 2019-12-24T22:02:05+00:00
Fixed in dev branch.
Thank you.

# Action History
- Created by: ainy0293 | 2019-12-21T16:54:59+00:00
- Closed at: 2020-08-19T01:27:37+00:00
