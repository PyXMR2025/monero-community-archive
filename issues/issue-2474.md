---
title: Commandline argument parser bug
source_url: https://github.com/monero-project/monero/issues/2474
author: MaxXor
assignees: []
labels:
- invalid
created_at: '2017-09-19T06:13:55+00:00'
updated_at: '2017-09-20T19:12:33+00:00'
type: issue
status: closed
closed_at: '2017-09-20T19:12:33+00:00'
---

# Original Description
I think I noticed a small argument parser bug. Try to execute the command:
`./monerod limit -1` and you'll see:
> Failed to parse arguments: unrecognised option '-1'

While `./monerod limit 1` works fine.

# Discussion History
## moneromooo-monero | 2017-09-19T09:48:38+00:00
add -- at some point before -1. This is normal input parsing behaviour.

## hyc | 2017-09-20T19:10:39+00:00
+invalid

# Action History
- Created by: MaxXor | 2017-09-19T06:13:55+00:00
- Closed at: 2017-09-20T19:12:33+00:00
