---
title: monerod bc_dyn_stats not behaving as expected
source_url: https://github.com/monero-project/monero/issues/1807
author: ghost
assignees: []
labels: []
created_at: '2017-02-26T17:10:12+00:00'
updated_at: '2017-02-28T21:06:42+00:00'
type: issue
status: closed
closed_at: '2017-02-28T21:06:42+00:00'
---

# Original Description
Node up and running 0.10.2.1, Ubuntu 16.04

```
nodey@odroidc2:~$ monerod status
Height: 1254694/1254694 (100.0%) on mainnet, not mining, net hash 58.55 MH/s, v4, up to date, 34(out)+1(in) connections, uptime 0d 0h 5m 13s
nodey@odroidc2:~$ monerod bc_dyn_stats 5
2017-02-26 17:07:48.308	      7f9fd3c000	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon
```

# Discussion History
## moneromooo-monero | 2017-02-26T23:13:52+00:00
https://github.com/monero-project/monero/pull/1814

## ghost | 2017-02-28T21:06:42+00:00
Closing due to @moneromooo-monero's PR

# Action History
- Created by: ghost | 2017-02-26T17:10:12+00:00
- Closed at: 2017-02-28T21:06:42+00:00
