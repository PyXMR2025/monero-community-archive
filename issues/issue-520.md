---
title: Slow Hash Rate for Cryptonight-Heavy
source_url: https://github.com/xmrig/xmrig/issues/520
author: codeorcode
assignees: []
labels:
- question
created_at: '2018-04-08T11:55:06+00:00'
updated_at: '2018-10-10T22:17:05+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:17:05+00:00'
---

# Original Description
I try to mine Sumokoin using 2.6.0-beta1 version.
I got hashrate of **80 Hh/s** on an AMD FX 6300 CPU where on the same suokoin but old fork that used cryptonight I got **270 Hs/s**.

So it's a drop from **270** to **80** Hs/s when using **cryptonight heavy** instead of **cryptonight**.


# Discussion History
## farmer-1 | 2018-04-08T12:17:13+00:00
I'm afraid that's by design of cryptonight-heavy, a 60% drop on hashrate on CPU is unfortunately normal.

## xmrig | 2018-04-08T12:54:17+00:00
@codeorcode don't forget, threads count should be reduced twice if you set it manually before.
Thank you.

## codeorcode | 2018-04-08T23:50:16+00:00
I've set it to three (instead of 6 but then only 3 cores are used).

The interesting part is that now I get 149 Hh/s but see the image:

https://i.imgur.com/mLKheuj.png


# Action History
- Created by: codeorcode | 2018-04-08T11:55:06+00:00
- Closed at: 2018-10-10T22:17:05+00:00
