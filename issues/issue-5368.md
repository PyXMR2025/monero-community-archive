---
title: BUG sign_transfer throws "failed to connect to deamon" when offline signing
source_url: https://github.com/monero-project/monero/issues/5368
author: dnaleor
assignees: []
labels:
- duplicate
created_at: '2019-03-29T16:45:17+00:00'
updated_at: '2019-03-29T16:57:41+00:00'
type: issue
status: closed
closed_at: '2019-03-29T16:57:41+00:00'
---

# Original Description
It's just a small annoyance, but when I recently (CLI 14.0.2) tried to sign a transaction offline, it failed and I got the message "failed to connect to deamon".

The workaround was starting monerod (even though it was unsynced) and then signing the raw transaction.

As far as I remember, this wasn't the behaviour of the CLI before.

# Discussion History
## moneromooo-monero | 2019-03-29T16:50:20+00:00
Fixed in 5277.

+duplicate

# Action History
- Created by: dnaleor | 2019-03-29T16:45:17+00:00
- Closed at: 2019-03-29T16:57:41+00:00
