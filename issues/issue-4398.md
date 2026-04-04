---
title: Offline new wallet has restore height 0 with simplewallet
source_url: https://github.com/monero-project/monero/issues/4398
author: m2049r
assignees: []
labels: []
created_at: '2018-09-17T17:26:28+00:00'
updated_at: '2018-09-21T18:56:57+00:00'
type: issue
status: closed
closed_at: '2018-09-21T18:56:57+00:00'
---

# Original Description
Creating a new wallet with simplewallet without connecting to a daemon seems to set the restore height to 0 (exit & reopen with daemon does a full scan from genesis).

AFAICR it used to guess the height when there was no daemon connected.

# Discussion History
## moneromooo-monero | 2018-09-17T17:40:33+00:00
#4394

## moneromooo-monero | 2018-09-21T18:52:49+00:00
+resolved

# Action History
- Created by: m2049r | 2018-09-17T17:26:28+00:00
- Closed at: 2018-09-21T18:56:57+00:00
