---
title: Since commit 4a9db89 xmrig crashes instantly on Core2 6600 (and possibly other
  CPUs without SSE4.1)
source_url: https://github.com/xmrig/xmrig/issues/1853
author: BugerDread
assignees: []
labels:
- bug
- randomx
- kawpow
created_at: '2020-09-26T18:10:16+00:00'
updated_at: '2020-10-03T05:22:45+00:00'
type: issue
status: closed
closed_at: '2020-10-03T05:22:45+00:00'
---

# Original Description
**Describe the bug**
Since commit 4a9db89527dfac4e0c66892190fd3d642408d459 xmrig crashes instantly on all my rigs.
Im using quite old CPUs (Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz according to /proc/cpuinfo) to mine kawpow on AMD GPUs (opencl). I was asked to try the dev branch to check that #1836 was fixed, but the xmrig crashed instantly as launched with:
```
$ ./xmrig 
Illegal instruction (core dumped)
```
Then I went trough trial and error over previos commits to find out which one starts to cause this, and I found its "4a9db89527dfac4e0c66892190fd3d642408d459 - RandomX: added SSE4.1-optimized Blake2b".

Xmrig build from previous commits starts normally so it seems that SSE4.1 optimisation is breaking xmrig for older CPUs (without SSE4.1 support, such as mentioned Core2 6600).

I found a way how to buid later commits to be able to mine kawpow over opencl on my old CPUs:

- remove all "-msse4.1" occurrences from cmake/flags.cmake
- add "-DWITH_RANDOMX=OFF" to the cmake command (eg. cmake .. -DWITH_RANDOMX=OFF -DXMRIG_DEPS=scripts/deps)

**To Reproduce**
Run xmrig build from source after commit 4a9db89527dfac4e0c66892190fd3d642408d459 on Core2 6600 (which lacks SSE4.1) and try to launch it.

**Expected behaviour**
Xmrig should detect older CPUs and run on them as before 4a9db89527dfac4e0c66892190fd3d642408d459 (at least to be able to mine algos which does not require SSE4.1)

**Required data**
 - Miner log as text or screenshot
```
$ ./xmrig 
Illegal instruction (core dumped)
```
 - Config file or command line (without wallets)
```
config independent, crashes even without config in the same way
```
 - OS: [e.g. Windows]
```
Ubuntu 18.04.5 LTS
4GB RAM + 2GB swap
Linux m04 5.4.0-48-lowlatency #52~18.04.1-Ubuntu SMP PREEMPT Thu Sep 10 13:34:23 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
amdgpu-pro 20.10-1048554
```



# Discussion History
## xmrig | 2020-09-27T07:02:19+00:00
Fixed in dev branch.
Thank you.

## SChernykh | 2020-09-27T07:10:05+00:00
Can you also test that RandomX still works on this CPU in the dev branch?

## BugerDread | 2020-09-27T09:12:08+00:00
> Fixed in dev branch.
> Thank you.

Yes, now I can run xmrig compiled from dev branch on my old CPUs to mine kawpow on AMD GPUs.

> Can you also test that RandomX still works on this CPU in the dev branch?

Of course. Unfortunately it seems that I cant mine RandomX (Monero) on my old CPUs with latest dev - xmrig crashes:
```
$ ./xmrig --donate-level 5 -o randomxmonero.eu.nicehash.com:3380 -u WALLET-REMOVED.m04 -p x -k --nicehash --coin monero
 * ABOUT        XMRig/6.3.5-dev gcc/7.5.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.4/3.8 GB (36%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      randomxmonero.eu.nicehash.com:3380 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-09-27 11:05:35.626]  net      use pool randomxmonero.eu.nicehash.com:3380  172.65.200.133
[2020-09-27 11:05:35.626]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195712
[2020-09-27 11:05:35.627]  cpu      use argon2 implementation SSSE3
[2020-09-27 11:05:36.227]  randomx  init dataset algo rx/0 (2 threads) seed 03ff5130b4c62713...
[2020-09-27 11:05:36.227]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
Aborted (core dumped)
```

... but I can mine RandomX with the same config using older xmrig on this CPU:
```
$ ./xmrig --donate-level 5 -o randomxmonero.eu.nicehash.com:3380 -u WALLET-REMOVED.m04 -p x -k --nicehash --coin monero
 * ABOUT        XMRig/6.3.2 gcc/7.4.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.4/3.8 GB (36%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      randomxmonero.eu.nicehash.com:3380 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-09-27 11:09:17.207]  net      use pool randomxmonero.eu.nicehash.com:3380  172.65.200.133
[2020-09-27 11:09:17.207]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195714
[2020-09-27 11:09:17.207]  cpu      use argon2 implementation SSSE3
[2020-09-27 11:09:17.207]  randomx  init dataset algo rx/0 (2 threads) seed 03ff5130b4c62713...
[2020-09-27 11:09:17.208]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2020-09-27 11:09:42.227]  randomx  dataset ready (25020 ms)
[2020-09-27 11:09:42.228]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2020-09-27 11:09:42.249]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (21 ms)
[2020-09-27 11:09:56.566]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195714
[2020-09-27 11:09:59.812]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195714
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   83.82 |     n/a |     n/a |
|        1 |        1 |   83.50 |     n/a |     n/a |
|        - |        - |   167.3 |     n/a |     n/a |
[2020-09-27 11:10:10.028]  miner    speed 10s/60s/15m 167.3 n/a n/a H/s max 169.3 H/s
```
 

## SChernykh | 2020-09-27T09:51:18+00:00
> Unfortunately it seems that I cant mine RandomX (Monero) on my old CPUs with latest dev - xmrig crashes

Can you try again with the latest dev?

## BugerDread | 2020-09-27T10:38:18+00:00
Of course - yes, it works with latest dev (dfab81e):
```
$ ./xmrig --donate-level 5 -o randomxmonero.eu.nicehash.com:3380 -u wallet.m04 -p x -k --nicehash --coin monero
 * ABOUT        XMRig/6.3.5-dev gcc/7.5.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.4/3.8 GB (36%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      randomxmonero.eu.nicehash.com:3380 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-09-27 12:31:57.754]  net      use pool randomxmonero.eu.nicehash.com:3380  172.65.200.133
[2020-09-27 12:31:57.754]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195753
[2020-09-27 12:31:57.754]  cpu      use argon2 implementation SSSE3
[2020-09-27 12:31:58.354]  randomx  init dataset algo rx/0 (2 threads) seed 03ff5130b4c62713...
[2020-09-27 12:31:58.354]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2020-09-27 12:32:16.546]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195754
[2020-09-27 12:32:19.953]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195755
[2020-09-27 12:32:23.438]  randomx  dataset ready (25084 ms)
[2020-09-27 12:32:23.438]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2020-09-27 12:32:23.460]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (22 ms)
[2020-09-27 12:32:43.891]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 167804 algo rx/0 height 2195755
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   100.8 |     n/a |     n/a |
|        1 |        1 |   100.7 |     n/a |     n/a |
|        - |        - |   201.5 |     n/a |     n/a |
[2020-09-27 12:32:47.930]  miner    speed 10s/60s/15m 201.5 n/a n/a H/s max 201.5 H/s
```
Im happy to help to make xmrig better.

## berlusconi500 | 2020-09-30T01:59:54+00:00
I confirm, with the dev branch my e4600 now works. Thank you <3

## xmrig | 2020-10-03T05:22:44+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.3.5

# Action History
- Created by: BugerDread | 2020-09-26T18:10:16+00:00
- Closed at: 2020-10-03T05:22:45+00:00
