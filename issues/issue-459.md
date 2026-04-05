---
title: 'duplicated job receiveed '
source_url: https://github.com/xmrig/xmrig/issues/459
author: zhouzuoji
assignees:
- xmrig
labels:
- bug
created_at: '2018-03-17T07:30:12+00:00'
updated_at: '2018-03-17T11:09:44+00:00'
type: issue
status: closed
closed_at: '2018-03-17T11:09:44+00:00'
---

# Original Description
when using xmr.f2pool.com:13531, miner report "duplicated job receiveed, reconnect...", it can't work 

# Discussion History
## xmrig | 2018-03-17T08:14:14+00:00
I confirm issue, pool really send duplicated jobs, first one in login response, second as regular notification, no one other pool do it in that way, but I little confused, previous versions should no work too, but works.
Thank you.

## xmrig | 2018-03-17T09:35:37+00:00
Fixed, it will be included to next bugfix release v2.5.1.
Thank you.

# Action History
- Created by: zhouzuoji | 2018-03-17T07:30:12+00:00
- Closed at: 2018-03-17T11:09:44+00:00
