---
title: Not working on AMD Opteron
source_url: https://github.com/xmrig/xmrig/issues/165
author: solucaojp
assignees: []
labels:
- NUMA
created_at: '2017-10-22T11:58:52+00:00'
updated_at: '2019-08-02T12:37:53+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:37:53+00:00'
---

# Original Description
I configured iqual to another server with Xeon processor, but is not getting speed from H / s, could you help me?

# Discussion History
## solucaojp | 2017-10-22T11:59:47+00:00
I configured exactly as on another server with Xeon processor, but not getting speed from H / s, could they help me?

## ght3d | 2017-10-23T06:45:01+00:00
Same here, speed on old 6 core Opterons HE series doesnt display at the beginning , but after a while starts to mine with speed of max 20h/sec, 10 times slower compared to cpuminer-opt. 

## xmrig | 2017-10-23T08:06:43+00:00
Old Opterons without hardware AES? Might something wrong with software AES implementation.
Also huge pages enabled? If yes try disable it `--no-huge-pages`, otherwise enable it.
Thank you.

## ght3d | 2017-10-23T08:49:02+00:00
In my case the opterons are 2423 HE without hardware AES, only SSE, but the huge pages are available and enabled.

## xmrig | 2019-07-29T02:19:37+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: solucaojp | 2017-10-22T11:58:52+00:00
- Closed at: 2019-08-02T12:37:53+00:00
