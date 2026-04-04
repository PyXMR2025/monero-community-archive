---
title: '[Bug Report] Windows, database_size field from get_info is 0'
source_url: https://github.com/monero-project/monero/issues/9513
author: Cyrix126
assignees: []
labels:
- bug
created_at: '2024-10-10T13:21:12+00:00'
updated_at: '2025-01-05T08:30:20+00:00'
type: issue
status: closed
closed_at: '2024-12-29T09:13:35+00:00'
---

# Original Description
On Windows at least 10 & 11, the method "get_info" of the endpoint /json_rpc will always have a value of 0 on field "database_size".

To reproduce:

1. Start monerod without any args on a Windows system.
2. execute in cmd:
 `curl -d "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"method\":\"get_info\"}" http://127.0.0.1:18081/json_rpc`
3.  See the field "database_size"
`"database_size": 0,`

# Discussion History
## jeffro256 | 2024-10-10T17:47:20+00:00
I don't have a windows machine on me, but could you try compiling PR #9514 please and see if it fixes the issue?

## Cyrix126 | 2024-10-11T16:59:27+00:00
@jeffro256 Now it shows this value without changing: 18446744072227688448, so 18.446EB

## iamamyth | 2024-12-28T02:10:35+00:00
@Cyrix126 Can you compile https://github.com/iamamyth/monero/commit/dcf5e3ec7634b2f7055103dbed3e1499fcb0f202 and see if it fixes your issue?

## Cyrix126 | 2024-12-29T09:13:35+00:00
It's now returning the correct size with https://github.com/iamamyth/monero/commit/dcf5e3ec7634b2f7055103dbed3e1499fcb0f202
Thanks !

# Action History
- Created by: Cyrix126 | 2024-10-10T13:21:12+00:00
- Closed at: 2024-12-29T09:13:35+00:00
