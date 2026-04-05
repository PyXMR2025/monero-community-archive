---
title: xmrig vs Ryzen 3600
source_url: https://github.com/xmrig/xmrig/issues/1782
author: andrexTI
assignees: []
labels:
- stability
created_at: '2020-07-17T19:23:38+00:00'
updated_at: '2020-08-31T05:46:47+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:46:47+00:00'
---

# Original Description
Hello everyone, my xmrig is stuck on this screen. What can I do to make it work?

![error](https://user-images.githubusercontent.com/60714578/87823386-95d2a800-c849-11ea-96cc-a43536c19559.png)


# Discussion History
## Lonnegan | 2020-07-18T22:11:54+00:00
Hi,

I see you are using xmrig compiled with gcc. Have you counter-tested with xmrig in the MS version?

## andrexTI | 2020-07-19T00:24:47+00:00
Yes, I tested both. I think I found the solution, disable "opcache" in BIOS. So far it's working. It seems that this is a problem for the ryzens.

look this https://github.com/xmrig/xmrig/issues/1384

## xmrig | 2020-08-31T05:46:47+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: andrexTI | 2020-07-17T19:23:38+00:00
- Closed at: 2020-08-31T05:46:47+00:00
