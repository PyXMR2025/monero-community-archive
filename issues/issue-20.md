---
title: cpu affinity setting bug
source_url: https://github.com/xmrig/xmrig/issues/20
author: nightbowl
assignees: []
labels: []
created_at: '2017-06-26T07:22:53+00:00'
updated_at: '2017-06-29T22:41:39+00:00'
type: issue
status: closed
closed_at: '2017-06-29T22:41:39+00:00'
---

# Original Description
Hi,
A big cpu-affinity value cannot be set.
Fof example:
Dual  Intel® Xeon® E5-2680 v3 (12 cores 24 threads) requires sample mask 0xAAAAAAAAAAAA which however cannot be seen on the start console window. The same is for dual Intel® Xeon® E5-2650 (8 cores 16 threads) / 0xAAAAAAAA
Thanks

# Discussion History
## esfomeado | 2017-06-26T08:42:49+00:00
For 12 cores should be: 0xFFF
For 8 cores should be: 0xFF

## nightbowl | 2017-06-26T09:09:02+00:00
12 physical cores + HT = 24 logical cores, so mask should be 0xFFFFFF. Then you should take the mask two times for two physical processors, As a result mask should be 0xFFFFFFFFFFFF

## nightbowl | 2017-06-26T10:31:05+00:00
![pic](https://user-images.githubusercontent.com/29701149/27535462-bf19bb78-5a8c-11e7-8507-3bb4709d1130.jpg)
Added proof picture

## xmrig | 2017-06-26T16:14:07+00:00
What version do you use? old C or new C++ (1.0.0+) According mask 0xAAAAAAAAAAAA you try use 24 threads. But for 60 MB L3 cache optimal 30 or 15 threads (--av 2). I will look later today what happened with mask. Thank you.

## nightbowl | 2017-06-26T18:03:54+00:00
I have mentioned the mask 0xAAAAAAAAAAAA just for example.
It doesn't matter which mask I choose, xmrig ignores such big values of mask. Both versions of binaries - gcc and msvc behave the same way.

**Command line:**
xmrig -u WALLET -p x --cpu-affinity 0xFEAAAAFEAAAA --algo=cryptonight -o stratum+tcp://cryptonight.eu.nicehash.com:3355

**Console output (used mask is absent):**
 * VERSIONS:     XMRig/1.0.1 libuv/1.12.0 MSVC/2017
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz (2) x64 AES-NI
 * CPU L2/L3:    12.0 MB/60.0 MB
 * THREADS:      30, cryptonight, av=1, donate=5%, nicehash
 * POOL #1:      cryptonight.eu.nicehash.com:3355



## xmrig | 2017-06-26T20:31:45+00:00
I fix it, can you compile from source to confirm? If not I will compile it later.

## nightbowl | 2017-06-27T02:17:09+00:00
I'll better wait for your binaries.
Thanks

## xmrig | 2017-06-27T02:42:26+00:00
[xmrig-1.1.0-dev-msvc-win64.zip](https://github.com/xmrig/xmrig/files/1104030/xmrig-1.1.0-dev-msvc-win64.zip)

## nightbowl | 2017-06-27T05:00:15+00:00
Hi, thanks for the fast fix, but the problem is not solved yet. The first CPU takes the mask as it should, but the second mask is taken wrong.

**Log of start seems Ok:**
 * VERSIONS:     XMRig/1.1.0-dev libuv/1.12.0 MSVC/2017
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz (2) x64 AES-NI
 * CPU L2/L3:    12.0 MB/60.0 MB
 * THREADS:      30, cryptonight, av=1, donate=5%, nicehash, affinity=0xFEAAAAFEAAAA
 * POOL #1:      cryptonight.eu.nicehash.com:3355

**But CPU diagram shows wrong resuls:**
Picture in the next comment

## nightbowl | 2017-06-27T05:02:00+00:00
![pic](https://user-images.githubusercontent.com/29701149/27571500-06ad312c-5b28-11e7-98da-921b2fde7663.jpg)


## xmrig | 2017-06-27T14:58:12+00:00
I think I will make calculator for this, these masks very confused. Currently I use Windows Calculator http://i.imgur.com/0FupoXX.png so mask for 30 threads should be `0xFEAAAAFEAAAA`.
If you want move 4 threads on second CPU to end `0xAA0000FEAAAA` http://i.imgur.com/rt0uuMJ.png

## nightbowl | 2017-06-27T15:29:38+00:00
Of course, I agree with you, that mask for 30 threads should be 0xFEAAAAFEAAAA. Moreover, I have tried to put it in the command line of xmrig, but alas, instead of it, the new xmrig wrongly uses mask 0x0000AAFEAAAA as I have showed on the screenshot above.

## nightbowl | 2017-06-27T15:36:33+00:00
It seems like some variable cannot be bigger than 32 bits

## xmrig | 2017-06-27T15:54:35+00:00
[xmrig-1.1.0-dev-msvc-win64.zip](https://github.com/xmrig/xmrig/files/1105915/xmrig-1.1.0-dev-msvc-win64.zip)
You are right, I forgot in other place it limited to 32 bits, now should be ok.

## nightbowl | 2017-06-27T16:19:09+00:00
Thanks a lot!! Now all the cores are working as they have set in the command line. Again, thanks!
Good luck! I wish you success.


# Action History
- Created by: nightbowl | 2017-06-26T07:22:53+00:00
- Closed at: 2017-06-29T22:41:39+00:00
