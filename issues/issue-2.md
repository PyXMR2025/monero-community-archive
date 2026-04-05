---
title: The new software AES algo 4 is slower than the old one
source_url: https://github.com/xmrig/xmrig/issues/2
author: sfrode
assignees: []
labels: []
created_at: '2017-04-19T19:43:31+00:00'
updated_at: '2019-08-02T12:33:41+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:33:41+00:00'
---

# Original Description
Hello,
with the old software AES implementation, I used to get approximately 140 H/s on my dual E5520 with kernel 4.4.0 (VMware VM, 8 cores allocated). With the new one committed in 21c243ed8f5e67a08170cef1b1fbcf7a2167190b, I'm getting around 110-115 H/s. Is there any way you can keep the old algo around as well?

Btw, good work on the miner!

# Discussion History
## xmrig | 2017-04-21T16:01:18+00:00
Interesting result, old software AES is not so good, sometimes was broken due compiler optimization and was slower on i7 6700. I will check it again.

Anyway E5520 supports AES-NI. Sometimes virtual cpus is not contains for all available cpuid flags. If you manually select `--av=1` it may work. I already had a similar case.

## sfrode | 2017-04-21T17:22:02+00:00
Unfortunately for me who has loads of the Xeon 5500 series CPUs, AES-NI wasn't introduced until the Xeon 5600 series.

I pulled master again and recompiled with gcc 6.2.0 (ubuntu use 5.4.0 as default on 16.04); but that didn't change anything.

## esfomeado | 2017-04-21T20:20:03+00:00
With the latest commit i have about 5% drop on algo 3 (BMI2).

# Action History
- Created by: sfrode | 2017-04-19T19:43:31+00:00
- Closed at: 2019-08-02T12:33:41+00:00
