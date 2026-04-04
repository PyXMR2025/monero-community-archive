---
title: Failed to parse transaction from blob
source_url: https://github.com/monero-project/monero/issues/4649
author: BKdilse
assignees: []
labels: []
created_at: '2018-10-18T15:30:08+00:00'
updated_at: '2018-10-18T15:54:22+00:00'
type: issue
status: closed
closed_at: '2018-10-18T15:54:22+00:00'
---

# Original Description
Hi,

I've started seeing these errors while running the `monerod`  `v0.13.0.0`

This only started today as far as I am aware, well before the fork.
I've tried the `--db-salvage`, but it made no difference.  I then tried restoring the `.bitmonero` folder from another working node, but still seeing the errors.

```
2018-10-18 15:24:21.511  [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:185    Failed to parse transaction from blob
2018-10-18 15:24:41.796  [RPC1]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:185    Failed to parse transaction from blob
2018-10-18 15:25:02.085  [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:185    Failed to parse transaction from blob

```

Any ideas what is going on please?

# Discussion History
## BKdilse | 2018-10-18T15:34:39+00:00
Wallet RPC is causing this, but not sure why?

## moneromooo-monero | 2018-10-18T15:45:11+00:00
Fixed in https://github.com/monero-project/monero/pull/4636

## BKdilse | 2018-10-18T15:54:22+00:00
Dam, I only compiled last night.  Thanks, I'll compile again tonight.

# Action History
- Created by: BKdilse | 2018-10-18T15:30:08+00:00
- Closed at: 2018-10-18T15:54:22+00:00
