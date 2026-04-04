---
title: Resync Required?
source_url: https://github.com/monero-project/monero/issues/8782
author: devatgo
assignees: []
labels: []
created_at: '2023-03-18T09:34:20+00:00'
updated_at: '2023-03-24T04:35:43+00:00'
type: issue
status: closed
closed_at: '2023-03-19T06:25:06+00:00'
---

# Original Description
We were syncing a node on a VPS the other day (we're running a few tests on one of our wimpy VPS's before migrating to one of our beefy dedi servers) and when checking the sync progress we noticed that the monero daemon shutdown and output the message "Killed" (no other error messages indicating a corrupt db was ever displayed in output upon resuming syncing), We're guessing this probably occurred due to OOM. We've since created a swap file on the server and have resumed syncing. Is it safe to continue syncing (safe in regards to assuming no data corruption)? Or should we resync?

# Discussion History
## selsta | 2023-03-18T11:38:22+00:00
Yes, it means OOM. You can safely continue syncing.

# Action History
- Created by: devatgo | 2023-03-18T09:34:20+00:00
- Closed at: 2023-03-19T06:25:06+00:00
