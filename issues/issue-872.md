---
title: speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
source_url: https://github.com/xmrig/xmrig/issues/872
author: zaferweb
assignees: []
labels: []
created_at: '2018-11-08T05:03:29+00:00'
updated_at: '2018-12-17T07:31:56+00:00'
type: issue
status: closed
closed_at: '2018-12-17T07:31:56+00:00'
---

# Original Description
I have problem The following results are available on my 2 PCs. I've changed the settings in the config.json file many times, but the result is still unchanged. How can I solve this?

CPU : Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz (1) x64 AES
[2018-xx-xx xx:xx:xx] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s

CPU : Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz (2) x64 AES
[2018-xx-xx xx:xx:xx] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s

# Discussion History
## 2010phenix | 2018-11-08T11:45:37+00:00
and where is problem?
not receive from pool shares and no H/s stat )

## zaferweb | 2018-11-12T07:40:01+00:00
2010phenix Thank you for reply.

I have 2 computers which are same CPU Xeon. Although the options in the config.json file of the 2 computers are the same, there are two different results. Computer-1 is connected to the pool and working properly. Computer-2 cannot connect to the pool. The screen shot is below. Why is this problem caused?

![xeon-1](https://user-images.githubusercontent.com/25661901/48333198-8ad47700-e667-11e8-9402-0aa34ecb84f9.jpg)


## snipeTR | 2018-11-12T08:15:26+00:00
Firewall ?

## zaferweb | 2018-11-14T08:29:32+00:00
Hi snipeTR,
If you're asking for the firewall I'm using. I am using Cyberoam as firewall. There is open all web sites and services  on the firewall for Computer-1 like Computer-2 too. So there is no any blocking in the firewall.

## snipeTR | 2018-11-14T11:08:24+00:00
setup a proxy on a local machine. its connected to the pool. I'm sure the problem is related to the security system.

## zaferweb | 2018-12-17T07:31:55+00:00
I found the solution. Symantec is blocking the virus program. When i change some setting in Symantec it is working.

# Action History
- Created by: zaferweb | 2018-11-08T05:03:29+00:00
- Closed at: 2018-12-17T07:31:56+00:00
