---
title: 'AES / AVX Optimizations: any way to improve performance'
source_url: https://github.com/xmrig/xmrig/issues/137
author: erotavlasme
assignees: []
labels: []
created_at: '2017-10-03T21:40:58+00:00'
updated_at: '2017-10-05T19:25:03+00:00'
type: issue
status: closed
closed_at: '2017-10-05T19:25:03+00:00'
---

# Original Description
Hi,
at the moment xmrig is the fastest CPU mining for monero. It uses AES instructions that are 128 bit registers, what about using AVX 2 instructions that are 256 bit registers?
Some miners for other cryptocurrencies use them [link](https://github.com/elmad/darkcoin-cpuminer-1.3-avx-aes).
Thank you

# Discussion History
## xmrig | 2017-10-04T12:53:05+00:00
AVX won't help, other people try use AVX2, but it slower.
SSE2 for renaming parts of the loop won't help too.
128 bit registers used only for AES related parts, because there no choice.

Bottleneck for Monero is memory/cache latency.
Thank you. 

## erotavlasme | 2017-10-04T16:38:13+00:00
Ok I see, so it seems that we cannot get any further improvement.
Did you try to compile with Profile-Guide Optimization (pogo)?
Thank you

## xmrig | 2017-10-05T11:17:55+00:00
I was use in first releases, I stop do it long time ago, there is no noticeable difference.

## erotavlasme | 2017-10-05T19:25:03+00:00
Ok thank you.

# Action History
- Created by: erotavlasme | 2017-10-03T21:40:58+00:00
- Closed at: 2017-10-05T19:25:03+00:00
