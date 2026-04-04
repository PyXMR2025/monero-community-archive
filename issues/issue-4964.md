---
title: MDB_PAGE_FULL
source_url: https://github.com/monero-project/monero/issues/4964
author: twake34
assignees: []
labels: []
created_at: '2018-12-09T22:53:25+00:00'
updated_at: '2019-03-05T14:25:47+00:00'
type: issue
status: closed
closed_at: '2019-03-05T14:25:47+00:00'
---

# Original Description
Hello,

For reason some, this error i get.

```
2018-12-09 22:47:22.276 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3728 Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_PAGE_FULL: Internal error - page has no more space
```

daemon will not start.

What i do?

# Discussion History
## hyc | 2018-12-10T13:05:25+00:00
Try starting the daemon with the --db-salvage flag.

## moneromooo-monero | 2019-02-01T21:56:26+00:00
https://github.com/monero-project/monero/pull/5112

## moneromooo-monero | 2019-03-05T13:36:51+00:00
Merged.

+resolved

# Action History
- Created by: twake34 | 2018-12-09T22:53:25+00:00
- Closed at: 2019-03-05T14:25:47+00:00
