---
title: Rejected shares with GhostRider
source_url: https://github.com/xmrig/xmrig/issues/2730
author: Lonnegan
assignees: []
labels: []
created_at: '2021-11-27T15:32:22+00:00'
updated_at: '2021-11-28T01:48:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

I've been mining Raptoreum with the cpu miner avx2 for weeks. In that time I had a few stale shares 0,2% but not a single rejected one.

Yesterday I switched from the cpu miner to xmrig 6.16 and despite of the short period of running there have already been 6 rejected shares. 6 is not much, indeed, but there must be something wrong. Rejected means, the share was not correct, defective, broken, somehow not right. Here I could find two:

[2021-11-27 14:38:04.649]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2021-11-27 14:38:04.649]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-11-27 14:38:04.649]  cpu      GhostRider algo 3: cn/dark (512 KB)
[2021-11-27 14:38:25.354]  cpu      rejected (26/1) diff 55008 "high-hash" (44 ms)

[2021-11-27 16:17:36.169]  cpu      GhostRider algo 1: cn/dark-lite (256 KB)
[2021-11-27 16:17:36.169]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2021-11-27 16:17:36.169]  cpu      GhostRider algo 3: cn/dark (512 KB)
[2021-11-27 16:17:37.542]  cpu      rejected (1713/5) diff 95559 "high-hash" (363 ms)

CPUs are AMD Ryzen 9 3900X, OS Windows, MSVC binary.

# Discussion History
## SChernykh | 2021-11-27T15:42:55+00:00
If you get a rejected share immediately after receiving new job from the pool, it's just an old share that was tested against a new job, i.e. stale share. Or, if you overclock your CPU and it was stable with cpuminer, it might not be stable with xmrig because the load on CPU is different.

## Lonnegan | 2021-11-27T15:47:26+00:00
There are ones which are not immediately after a new job, too. I just chose those after algo change to help you finding a possible problem (if there is one) in one of the new cn-variants which were not part of xmrig up to 6.16.

The shares, which are late, are rejected with "stale-job", not with "high-hash":

[2021-11-27 15:31:46.033]  cpu      rejected (115/2) diff 85713 "stale-job" (166 ms)

The machines are not overclocked. These are fileservers with ECC ram running @stock 24/7.

## SChernykh | 2021-11-27T16:38:28+00:00
Which pool was that?

## Lonnegan | 2021-11-27T16:44:58+00:00
The same one as before, because I wanted to have the possibility to compare directly since that's not so simple with the permanently changing hashrate of GR: flockpool on the TLS port.

## SChernykh | 2021-11-27T16:49:19+00:00
Can you check if you get these rejected shares soon after pool adjusts difficulty up or down? Because I don't think it's the problem with algorithm, more likely it's incorrect Stratum implementation in xmrig.

## Lonnegan | 2021-11-27T17:11:13+00:00
Well, I don't have logging enabled, I just can page up a bit, so I cannot see all errors anymore.

Regarding the rejeceted "stale-jobs" you are right. These occur milliseconds after the pool sent a new job and xmrig tried to return shares of the old one. Here for example:

[2021-11-27 17:26:07.128]  cpu      accepted (2488/30) diff 94104 (47 ms)
[2021-11-27 17:26:09.029]  net      new job from eu.flockpool.com:5555 diff
[2021-11-27 17:26:09.030]  cpu      rejected (2488/31) diff 94104 "stale-job
[2021-11-27 17:26:09.031]  cpu      GhostRider algo 1: cn/dark-lite (256 KB)
[2021-11-27 17:26:09.031]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-11-27 17:26:09.031]  cpu      GhostRider algo 3: cn/turtle (256 KB)

You can see that the pool sent a new job at 17:26:09.029, so it rejects the simultaneously returned old one at 17:26:09.030 as "stale". I think that's normal.

The shares that pool rejected as "high-hash" I don't see noticeable timings. Here for example:

[2021-11-27 14:38:01.914]  cpu      accepted (26/0) diff 57457 (37 ms)
[2021-11-27 14:38:04.644]  net      new job from eu.flockpool.com:5555 diff 55008 algo ghostrider height 193486
[2021-11-27 14:38:04.649]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2021-11-27 14:38:04.649]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-11-27 14:38:04.649]  cpu      GhostRider algo 3: cn/dark (512 KB)
[2021-11-27 14:38:25.354]  cpu      rejected (26/1) diff 55008 "high-hash" (44 ms)
[2021-11-27 14:38:39.514]  cpu      accepted (27/1) diff 55008 (39 ms)

The pool accepts a share of the old block height and difficulty 57457 at 14:38:01.914. Then the pool sends a new job with difficulty 55008 and new algo mix at 14:38:04.644. And then, at 14:38:25.354 the miner tries to return a result of that job, which you can recognize at the difficulty 55008. The pool rejects it not as stale but as "high-hash". That's 19 seconds (!) after the miner got the job. Further 14 seconds later at 14:38:39.514, xmrig returns a further result of the same job (diff 55008) and these were accepted.

To me, this looks more like a problem with one of the algos than a protocol problem. But of course I'm not the dev 8-)

## qanatozp | 2021-11-27T19:14:43+00:00
Lonnegan, try to run it with rtm.suprnova.cc pool.
This pool spam with low difficulty task so you will fail shares more frequently.

## RussianE39 | 2021-11-27T23:53:08+00:00
I have exactly same results, 100% is rejected. In my case on ClearLinux, but when I tried precompiled static binary - everything works as expected. So I suspect its either gcc 11.2 bug or cmake configuration

## Lonnegan | 2021-11-28T01:02:59+00:00
> Lonnegan, try to run it with rtm.suprnova.cc pool. This pool spam with low difficulty task so you will fail shares more frequently.

xmrig on suprnova:

[2021-11-28 01:50:31.511]  cpu      accepted (68/0) diff 31441 (92 ms)
[2021-11-28 01:50:38.893]  net      new job from rtm.suprnova.cc:4273 diff 31441 algo ghostrider height 193814
[2021-11-28 01:50:38.903]  cpu      GhostRider algo 1: cn/turtle-lite (128 KB)
[2021-11-28 01:50:38.903]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-11-28 01:50:38.905]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)
[2021-11-28 01:50:38.962]  cpu      rejected (68/1) diff 31441 "job not found" (50 ms)

But a new reason, I've not seen on flockpool before: "job not found"

## Lonnegan | 2021-11-28T01:33:01+00:00
> I have exactly same results

I don't think so! I do not have 100% rejected results. There are a few, meanwhile 12 within a day, that's around 0,2%. But before I had 0% rejected shares at flockpool, as I had before with xmrig and Haven. I had mined Haven with xmrig for 15 month on Hashvault.pro and never had a single rejected share; a few stale shares of course, that's normal, but not a single invalid one.

## RussianE39 | 2021-11-28T01:35:01+00:00
From my experience, if you have only little bit of rejected shares, it could be RAM errors. Xmrig uses more memory than cpuminer-gr. 

## Lonnegan | 2021-11-28T01:47:04+00:00
I've never had rejected shares with xmrig in other, more traditional implementations like rx (Monero) or cn/xhv (Haven). GR support in xmrig is status alpha 0.1 ;-) So please don't be angry with me if I'm currently looking for bugs in xmrig rather than in pools or the hardware. Btw: my RAMs are not OC and are ECC, so RAM errors are currently the least likely source of errors.

## RussianE39 | 2021-11-28T01:48:04+00:00
You tried gcc built xmrig for windows? 

# Action History
- Created by: Lonnegan | 2021-11-27T15:32:22+00:00
