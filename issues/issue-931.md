---
title: New ALGO for Zelerius Network ZLS. Support Pleased
source_url: https://github.com/xmrig/xmrig/issues/931
author: pikomule
assignees: []
labels:
- enhancement
- algo
created_at: '2019-02-13T13:15:53+00:00'
updated_at: '2020-03-29T18:16:04+00:00'
type: issue
status: closed
closed_at: '2019-03-06T13:20:58+00:00'
---

# Original Description
https://github.com/fireice-uk/xmr-stak/pull/2234

itinerations: 0x60000

Thanks

# Discussion History
## xmrig | 2019-03-05T12:27:20+00:00
@zelerius What current status of fork? I found both know pools http://pool.zelerius.org and http://pool.zelerius.ru/ still accept `cn/2` and reject `cn/zls` (added recently).
Thank you.

## xmrig | 2019-03-05T16:40:01+00:00
@nilhcraiv Also test pool https://xyztest.zelerius.org still accept `cn/2`, coin is dead or something wrong.

## ghost | 2019-03-05T17:30:06+00:00
@xmrig Currently Zelerius is using CN variant 2 the fork will be probabily at the end of the week 12 but we will not announce the block number yet, we hope say it in a few days.
https://xyztest.zelerius.org is running a testnet with the new algorithm then it should work it's strange. @nilhcraiv will check it.

## xmrig | 2019-03-05T18:19:16+00:00
@zelerius Okay, fine, I was think network is already forked, so... I'm not late.

## ghost | 2019-03-05T18:43:18+00:00
@xmrig https://xyztest.zelerius.org is running the new algorithm i.e using 393216 ( **0x60000** ) iterations, I've checked it and works fine. The pool rejected CNv2 hashes and accepts CN zelerius, it was tested with` xmr-stak 2.8.3 e785ca1` using both ports:

Port | Starting Difficulty | TLS
-- | -- | --
9292 | 2 000 | false
6886 | 25 000 | true

The pool should not accept CNv2 hashes it's strange... but I try to check it running xmrig

## ghost | 2019-03-05T19:22:41+00:00
I've tested it using xmrig. It's working well, the pool reject cn/2.

Maybe it was a confusion using the mining ports because of we have testnet and mainet running in the same domain:

- pool.**zelerius.org**
- xyztest.**zelerius.org**

I see If you don't indicate the port xmrig uses 3333 in this case you will mine cn/2 in the mainnet as follows:

Port | Network | algorithm | TLS
-- | -- | -- | --
3333 | mainnet | cn/2 | false
5555 | mainnet | cn/2 | false
9999 | mainnet | cn/2 | true
9292 | testnet | cn/zelerius | false
6886 | testnet | cn/zelerius | true

### TESTNET

/xmrig -a **cryptonight/2** -o xyztest.zelerius.org:**9292** -u ZL38EUFVDYvCvrSexBuqgHMEKXZzR1TgR2XfuDtPikv1WpiifeLDqwfW7vXDUnv2zm7BFF6EVuve14j5iBNaCTyU2SHteq6M4.1400 --rig-id=xmrig 

```
 * ABOUT        XMRig/2.13.1 clang/10.0.0
 * LIBS         libuv/1.26.0 OpenSSL/1.0.2q microhttpd/0.9.59 
 * CPU          Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz (1) x64 AES AVX2
 * CPU L2/L3    0.5 MB/3.0 MB
 * THREADS      2, cryptonight/2, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      xyztest.zelerius.org:9292 variant 2
 * COMMANDS     hashrate, pause, resume
[2019-03-05 20:04:54] use pool xyztest.zelerius.org:9292  82.223.50.28 
[2019-03-05 20:04:54] new job from xyztest.zelerius.org:9292 diff 1400 algo cn/2
[2019-03-05 20:04:55] READY (CPU) threads 2(2) huge pages 0/2 0% memory 4096 KB
[2019-03-05 20:05:10] new job from xyztest.zelerius.org:9292 diff 1400 algo cn/2
[2019-03-05 20:05:21] rejected (0/1) diff 1400 "Rejected share: invalid result" (60 ms)
[2019-03-05 20:05:28] Ctrl+C received, exiting
[2019-03-05 20:05:28] no active pools, stop mining
```

### MAINNET 

but If I don't indicate any porty xmrig use the default port 3333 where there is a pool running the mainnet

./xmrig -a **cryptonight/2** -o **xyztest.zelerius.org** -u ZL38EUFVDYvCvrSexBuqgHMEKXZzR1TgR2XfuDtPikv1WpiifeLDqwfW7vXDUnv2zm7BFF6EVuve14j5iBNaCTyU2SHteq6M4.1400 --rig-id=xmrig 
```
 * ABOUT        XMRig/2.13.1 clang/10.0.0
 * LIBS         libuv/1.26.0 OpenSSL/1.0.2q microhttpd/0.9.59 
 * CPU          Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz (1) x64 AES AVX2
 * CPU L2/L3    0.5 MB/3.0 MB
 * THREADS      2, cryptonight/2, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      xyztest.zelerius.org variant 2
 * COMMANDS     hashrate, pause, resume
[2019-03-05 20:04:11] use pool xyztest.zelerius.org:3333  82.223.50.28 
[2019-03-05 20:04:11] new job from xyztest.zelerius.org:3333 diff 1400 algo cn/2
[2019-03-05 20:04:12] READY (CPU) threads 2(2) huge pages 0/2 0% memory 4096 KB
[2019-03-05 20:04:15] accepted (1/0) diff 1400 (73 ms)
[2019-03-05 20:04:34] accepted (2/0) diff 1400 (66 ms)
[2019-03-05 20:04:39] Ctrl+C received, exiting
[2019-03-05 20:04:39] no active pools, stop mining
```

## xmrig | 2019-03-05T19:50:29+00:00
@nilhcraiv Sorry, my bad, I was use `xyztest.zelerius.org:3333`, with `:9292` new algorithm work fine.

This algorithm added as `cryptonight/zls` in dev branches for CPU and AMD miner (NVIDIA miner will be updated tomorrow) and will be included into next release.
Thank you.

```
 * ABOUT        XMRig/2.13.2-dev gcc/7.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1a microhttpd/0.9.59
 * HUGE PAGES   available
 * CPU          AMD Ryzen 7 2700X Eight-Core Processor          (1) x64 AES AVX2
 * CPU L2/L3    4.0 MB/16.0 MB
 * THREADS      8, cryptonight/zls, av=0, donate=5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xyztest.zelerius.org:9292 variant zls
 * COMMANDS     hashrate, pause, resume
[2019-03-06 02:42:26] use pool xyztest.zelerius.org:9292  82.223.50.28
[2019-03-06 02:42:26] new job from xyztest.zelerius.org:9292 diff 1400 algo cn/zls
[2019-03-06 02:42:26] READY (CPU) threads 8(8) huge pages 8/8 100% memory 16384 KB
[2019-03-06 02:42:29] accepted (1/0) diff 1400 (265 ms)
[2019-03-06 02:42:33] accepted (2/0) diff 1400 (257 ms)
[2019-03-06 02:42:36] accepted (3/0) diff 1400 (258 ms)
[2019-03-06 02:42:36] accepted (4/0) diff 1400 (514 ms)
[2019-03-06 02:42:39] accepted (5/0) diff 1400 (267 ms)
[2019-03-06 02:42:41] Ctrl+C received, exiting
```

## ghost | 2019-03-05T20:21:28+00:00
Amazing!! Thank you @xmrig

## xmrig | 2019-03-06T13:20:58+00:00
v2.14.0 released https://github.com/xmrig/xmrig/releases/tag/v2.14.0

## Pilott73 | 2019-03-24T19:18:13+00:00
Hello, XMRig alas does not work with the new algorithm. I tested on AMD GPU and Nvidia. Under option "ZLS" is enabled option "CN/2" It happens all the miners as well.

## pikomule | 2019-03-24T19:21:26+00:00
cn/zls

## Pilott73 | 2019-03-24T19:23:06+00:00
Yes of course cn / zls. It's not working. on CPU, too, not works.

## xmrig | 2019-03-24T20:18:00+00:00
Looks like I use wrong block version for algorithm detection, so `"variant": "!zls"` should help, also it can be done on pool side by adding field `"algo":"cn/zls"` to each job https://github.com/xmrig/xmrig-proxy/blob/master/doc/STRATUM_EXT.md
Thank you.

## ghost | 2019-03-24T21:06:10+00:00
Yes, Zelerius uses the new algorithm ZLS in block version 7. I think xmrig uses version 8 instead of 7 https://github.com/xmrig/xmrig/blob/08ef94486b1f5e24b25e4609621929a7efd72732/src/common/net/Job.cpp#L143

Thank you!!

## Pilott73 | 2019-03-24T21:08:19+00:00
option"!zls " works.

## ghost | 2019-03-24T21:11:57+00:00
Here the details about each version https://github.com/zelerius/Zelerius-Network/issues/8

Thanks!

## singh86harjinder | 2020-03-29T18:16:04+00:00
Hi, mining script is using half of the cores of my system. Any idea? what change do I need to make to fix it?

Thanks

# Action History
- Created by: pikomule | 2019-02-13T13:15:53+00:00
- Closed at: 2019-03-06T13:20:58+00:00
