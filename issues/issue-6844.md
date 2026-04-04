---
title: IPv6 only node
source_url: https://github.com/monero-project/monero/issues/6844
author: ser
assignees: []
labels: []
created_at: '2020-09-25T11:55:04+00:00'
updated_at: '2025-12-29T17:10:31+00:00'
type: issue
status: closed
closed_at: '2025-12-29T17:10:31+00:00'
---

# Original Description
Apparently it's impossible to have an IPv6 only node as there is no single IPv6 seed available. As IPv4 addresses are nearly out, monero should be able to work in IPv6 only environment. 

# Discussion History
## moneromooo-monero | 2020-09-25T14:32:43+00:00
You do not need a seed. These only serve to get a set of peer addresses.

## ser | 2020-09-25T15:49:36+00:00
OK, so why an IPV6 only node does not work?
```
status
Height: 1/1 (100.0%) on mainnet, not mining, net hash 0 H/s, v1, 0(out)+0(in) connections, uptime 0d 4h 6m 43s
```

## moneromooo-monero | 2020-09-25T16:05:30+00:00
This shows it knows no peers, so it can't sync. If you give it at least one valid IPv6 peer (--add-peer), it should find others.
There is a DNS based system which should get you peers without needing to connect to a seed, maybe it's broken. I don't know exactly how it works, I'll ask someone who does.

## boldsuck | 2020-10-18T20:28:28+00:00
My node is dualstack http://cloud.boldsuck.org:18081/get_info
Try `add-peer=[2a01:4f8:bc:a09::2]:18080`


## ser | 2020-10-19T03:46:57+00:00
Dual stack works, no doubts, single stack - not. Bitcoin works single stack without issues.

## boldsuck | 2020-10-19T12:48:28+00:00
OK, too bad. I was hoping it will work if one IPv6 P2P node is entered.

## hhartzer | 2025-12-29T17:08:01+00:00
Should this be closed in favor of #8818? It's newer, but has gotten more traction.

# Action History
- Created by: ser | 2020-09-25T11:55:04+00:00
- Closed at: 2025-12-29T17:10:31+00:00
