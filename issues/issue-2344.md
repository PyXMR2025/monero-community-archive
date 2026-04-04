---
title: Store prunable and non prunable transaction data separately
source_url: https://github.com/monero-project/monero/issues/2344
author: moneromooo-monero
assignees: []
labels:
- proposal
created_at: '2017-08-25T14:52:05+00:00'
updated_at: '2018-06-21T16:09:04+00:00'
type: issue
status: closed
closed_at: '2018-06-21T16:09:04+00:00'
---

# Original Description
This will be a fairly large win for daemon memory usage when a wallet refreshes, as most data will not be needed (it is currenly read, and discarded via a parse/reserialize step, which would then become unnecessary).
This will require a DB schema change.

# Discussion History
## dEBRUYNE-1 | 2017-08-25T15:52:36+00:00
-feature
+proposal

## moneromooo-monero | 2018-06-21T16:05:23+00:00
+resolved

# Action History
- Created by: moneromooo-monero | 2017-08-25T14:52:05+00:00
- Closed at: 2018-06-21T16:09:04+00:00
