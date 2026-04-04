---
title: Timeout too low
source_url: https://github.com/monero-project/monero/issues/4050
author: keffnet
assignees: []
labels: []
created_at: '2018-06-25T14:01:15+00:00'
updated_at: '2018-06-25T17:25:04+00:00'
type: issue
status: closed
closed_at: '2018-06-25T17:25:04+00:00'
---

# Original Description
Fluffer said this was fixed but I still have the problem in master so i'm opening an issue for it. Go ahead and close if duplicate.

When having a remote monerod and maybe even a local one and trying to do a transfer with alot of inputs the rpc session to the monerod will timeout making a transfer impossible. Changing DEFAULT_TIMEOUT_MS_REMOTE from 10s to 60s fixed it for me. But i'm not saying 60s is the optimal :D

# Discussion History
## moneromooo-monero | 2018-06-25T15:39:12+00:00
Fixed in https://github.com/monero-project/monero/pull/3962
Let us know if that works for you.

## keffnet | 2018-06-25T16:59:35+00:00
Works. Thanks. Thought the patch was commited to master already. Sorry for opening this issue.

## moneromooo-monero | 2018-06-25T17:18:47+00:00
No worries

+resolved

# Action History
- Created by: keffnet | 2018-06-25T14:01:15+00:00
- Closed at: 2018-06-25T17:25:04+00:00
