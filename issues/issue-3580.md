---
title: Monerod error
source_url: https://github.com/monero-project/monero/issues/3580
author: rmbb
assignees: []
labels: []
created_at: '2018-04-07T16:07:58+00:00'
updated_at: '2018-06-20T09:33:05+00:00'
type: issue
status: closed
closed_at: '2018-06-20T09:33:05+00:00'
---

# Original Description
No description

# Discussion History
## rmbb | 2018-04-07T16:12:38+00:00
Got this error running monerod after 4 hours:

SYNCHRONIZATION started
2018-04-07 16:01:35.432 12156   ERROR   ringct  src/ringct/rctSigs.cpp:361
point conv failed
2018-04-07 16:01:35.441 12156   ERROR   ringct  src/ringct/rctSigs.cpp:361
point conv failed
2018-04-07 16:01:35.450 12156   ERROR   ringct  src/ringct/rctSigs.cpp:361
point conv failed

status
Height: 1546134/1546134 (100.0%) on mainnet, mining at 16 H/s, net hash 645.63 MH/s, v7, up to date, 7(out)+12(in) connections, uptime 0d 5h 17m 18s

## moneromooo-monero | 2018-04-07T17:15:22+00:00
Someone sent an invalid transaction, and some of the data in it is being rejected. This can be ignored.

## moneromooo-monero | 2018-06-20T08:58:21+00:00
Not a bug, just a noisy log, which was recently toned down.

+resolved

# Action History
- Created by: rmbb | 2018-04-07T16:07:58+00:00
- Closed at: 2018-06-20T09:33:05+00:00
