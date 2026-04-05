---
title: '[SOLVED] Mining server not accepting jobs'
source_url: https://github.com/xmrig/xmrig/issues/2170
author: EricDriussi
assignees: []
labels: []
created_at: '2021-03-10T19:49:46+00:00'
updated_at: '2021-03-12T16:34:16+00:00'
type: issue
status: closed
closed_at: '2021-03-12T16:33:41+00:00'
---

# Original Description
Hi there! I'm struggling to get a mining server going. It seems to not be accepting jobs (I think, not an expert). 

I'm using Nanopool and have chacked that my run command actually works by mining on my laptop with the same setup (apart from hardware and distro, of course).

It seems to get stuck showing these two messages, showing (a slightly different version of them) on loop:
```
[2021-03-10 19:31:48.253]  miner    speed 10s/60s/15m 57.43 56.41 n/a H/s max 59.00 H/s
[2021-03-10 19:31:55.052]  net      new job from xmr-eu1.nanopool.org:14444 diff 480045 algo rx/0 height 2314107
```

pressing h returns
```
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   56.58 |   56.64 |     n/a |
|        - |        - |   56.58 |   56.64 |     n/a |
```

pressing s returns
```
[2021-03-10 19:30:36.367] no results yet
```
Again, if I run the 'same' setup on my machine it works no problem and my wallet shows up on the pools website. All good.

Might be kind of a noob question but I can't quite find the cause of the issue. Let me know if I can provide any further info!

# Discussion History
## SChernykh | 2021-03-10T19:54:52+00:00
With difficulty 480045 and hashrate of 56.64 h/s it'll take you ~2.35 hours to find a single share (`accepted` message in the log), you have to mine at another pool which allows lower difficulty.

## Lonnegan | 2021-03-11T08:19:21+00:00
Yes, as @SChernykh said.

In addition with such a slow hardware you should consider to mine at a pool, which has low payout limit to get paid before the year 2025 ;) and if the diff is still too high to find a result about each minute, it would be cool if the pool has a PPS payment scheme. When you return a valid result, you get your bucks, regardless if the pool has found a block in that round (PROP) or was within the PPLNS window. E.g. hashcity or hellominer

## Spudz76 | 2021-03-11T16:25:14+00:00
Some pools offer "autodiff", or fixed-diff but smaller, on some other port(s).

Sometimes they have "autodiff" but it doesn't react very fast (will take a while to drop smaller).

Sometimes they have none of the above and then you should find a better pool, like MoneroOcean, where you can also mine other coins and be paid XMR for them all (and get profitability back on GPUs).

## EricDriussi | 2021-03-12T16:33:15+00:00
Thanks a lot you guys! That was both helpful and very instructive 😁

# Action History
- Created by: EricDriussi | 2021-03-10T19:49:46+00:00
- Closed at: 2021-03-12T16:33:41+00:00
