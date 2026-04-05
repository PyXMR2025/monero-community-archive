---
title: ESXi Host and Ubuntu VM - H/s not available?
source_url: https://github.com/xmrig/xmrig/issues/336
author: johnydo
assignees: []
labels: []
created_at: '2018-01-14T11:04:49+00:00'
updated_at: '2018-11-05T12:37:55+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:37:55+00:00'
---

# Original Description
Hi everybody,

I use a Ubuntu VMWare on a ESXi host. After I start the xmrig I can not see the H/s rate. I get the message H/s not available?

# Discussion History
## johnydo | 2018-01-14T13:16:43+00:00
My xmrig config:
` 
* VERSIONS:     XMRig/2.4.4 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Core(TM) i5-6500 CPU @ 3.20GHz (1) x64 AES-NI
 * CPU L2/L3:    0.2 MB/6.0 MB
 * THREADS:      3, cryptonight, av=1, donate=1%
 * POOL #1:      xmr.pool.minergate.com:45560
 * COMMANDS:     hashrate, pause, resume
[2018-01-14 14:14:32] speed 2.5s/60s/15m n/a n/a n/a H/s max: 7.4 H/s
[2018-01-14 14:14:39] speed 2.5s/60s/15m n/a n/a n/a H/s max: 7.4 H/s
`

# Action History
- Created by: johnydo | 2018-01-14T11:04:49+00:00
- Closed at: 2018-11-05T12:37:55+00:00
