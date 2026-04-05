---
title: Failover on IP ban?????
source_url: https://github.com/xmrig/xmrig/issues/518
author: ghost
assignees: []
labels:
- question
created_at: '2018-04-08T04:01:02+00:00'
updated_at: '2018-10-10T22:16:49+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:16:49+00:00'
---

# Original Description
Is there a way to failover on an IP ban/switch pools on any error? Such as "Low difficulty share" or "Ip Ban error"?


I do this because I'm awaiting a new coin's algorithm jump/fork and set multiple algorithm variations to make sure it will work when the node is updated.

# Discussion History
## xmrig | 2018-04-08T08:21:44+00:00
https://github.com/xmrig/xmrig/blob/master/src/net/Client.cpp#L237 here short list of critical errors, when miner receive it, connection will closed, it force failover. But some pool now add non widely used error messages.
Thank you.

# Action History
- Created by: ghost | 2018-04-08T04:01:02+00:00
- Closed at: 2018-10-10T22:16:49+00:00
