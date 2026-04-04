---
title: Getting “Error retrieving blocks, missed (#) transactions for block with hash”
  while running pruned node
source_url: https://github.com/monero-project/monero/issues/5654
author: dginovker
assignees: []
labels: []
created_at: '2019-06-16T17:21:04+00:00'
updated_at: '2019-08-27T15:18:07+00:00'
type: issue
status: closed
closed_at: '2019-08-27T15:18:07+00:00'
---

# Original Description
I'm getting a lot of lines that look like these while running a pruned node on a very low end server (1 core CPU, 3.75GB RAM): 

```
2019-06-16 16:57:47.824 E Error retrieving blocks, missed 70 transactions for block with hash: <6689c1252116921b0b17a7fbcc6b93d0026593c93689f82679341af3878301fb>
2019-06-16 16:00:26.551 E Error retrieving blocks, missed 6 transactions for block with hash: <b5e57c909ef0a98786959cb230294fb6ca4032734ce498cfeff05e126bd92acd>
```

May be relevant, opening a wallet with the RPC throws this warning: `WARNING: You may not have a high enough lockable memory limit, see ulimit -l` as well.

# Discussion History
## moneromooo-monero | 2019-06-16T17:34:28+00:00
That's from nodes that don't understand pruning are asking you for data that you pruned. It's OK.

For the lockable memory issue, you can increase the amount of lockable memory using the command the message is giving you.

## moneromooo-monero | 2019-06-17T09:21:35+00:00
https://github.com/monero-project/monero/pull/5651 silences the message when we're in this case.

## moneromooo-monero | 2019-08-27T15:09:20+00:00
+resolved

# Action History
- Created by: dginovker | 2019-06-16T17:21:04+00:00
- Closed at: 2019-08-27T15:18:07+00:00
