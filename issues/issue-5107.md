---
title: Issue creating then relaying transaction with wallet RPC
source_url: https://github.com/monero-project/monero/issues/5107
author: woodser
assignees: []
labels: []
created_at: '2019-01-30T14:19:14+00:00'
updated_at: '2019-03-19T14:49:54+00:00'
type: issue
status: closed
closed_at: '2019-03-19T14:49:54+00:00'
---

# Original Description
Steps to reproduce:

1. Use wallet RPC to create a non-relayed transaction (e.g. invoke `transfer` with the `do_not_relay` flag)
2. Use wallet RPC `relay_tx` to relay the hex

Since accepting changes from master committed between 1/21 and 1/28, wallet RPC consistently returns “-4: Failed to commit tx” and the daemon logs “tx verification failed: invalid input”.

Environment: Mac OSX.

# Discussion History
## moneromooo-monero | 2019-02-03T10:35:19+00:00
https://github.com/monero-project/monero/pull/5122

## moneromooo-monero | 2019-03-19T14:17:07+00:00
+resolved

# Action History
- Created by: woodser | 2019-01-30T14:19:14+00:00
- Closed at: 2019-03-19T14:49:54+00:00
