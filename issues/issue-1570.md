---
title: 'Wallet: some commands time out after #1474 was merged'
source_url: https://github.com/monero-project/monero/issues/1570
author: iDunk5400
assignees: []
labels: []
created_at: '2017-01-14T10:32:17+00:00'
updated_at: '2017-01-15T19:55:19+00:00'
type: issue
status: closed
closed_at: '2017-01-15T19:55:19+00:00'
---

# Original Description
After #1474 was merged, my monero-wallet-cli times out after starting foregroud refresh with the message `Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0`.

Also, sweep_all times out with the message `Error: no connection to daemon. Please make sure daemon is running.`

Reverting #1474 fixes the issue for me.
The issue was observed on Ubuntu 14.04 with the blockchain on a HDD.

# Discussion History
## iDunk5400 | 2017-01-14T14:15:18+00:00
#1573 fixes wallet timeout issues for me.

# Action History
- Created by: iDunk5400 | 2017-01-14T10:32:17+00:00
- Closed at: 2017-01-15T19:55:19+00:00
