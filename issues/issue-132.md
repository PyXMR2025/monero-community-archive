---
title: double spend issue when txs not relayed
source_url: https://github.com/seraphis-migration/monero/issues/132
author: plowsof
assignees: []
labels: []
created_at: '2025-10-03T14:39:16+00:00'
updated_at: '2025-10-04T17:57:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
*after my node began broadcasting transactions, the problem has gone.

```
0 double spends, 10 not relayed, 0 failing, 0 older than 10 minutes (oldest 4 minutes ago), estimated 2 block (4 minutes) backlog
```
my node is was not relaying tx's as `tx-proxy` had no peers at that time (if relevant) 

subsequent transfer attempts result in a double spend error regardless of amounts 

# Discussion History
## j-berman | 2025-10-04T17:57:45+00:00
Possibly helped by #135, though this exact issue should be reproducible

# Action History
- Created by: plowsof | 2025-10-03T14:39:16+00:00
