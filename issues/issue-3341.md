---
title: wallet with a respend shows spent 18.4 million monero
source_url: https://github.com/monero-project/monero/issues/3341
author: williams-r
assignees: []
labels: []
created_at: '2018-03-03T22:13:58+00:00'
updated_at: '2018-03-04T01:48:05+00:00'
type: issue
status: closed
closed_at: '2018-03-04T01:48:05+00:00'
---

# Original Description
GUI wallet with a respend (both transactions were to the same wallet as sent it) shows spent 18.4 million monero when restoring from a specific block height.
spendable amount is normal.
the same mnemonic restored from genesis block in a new wallet file shows unconfirmed extra balance from the respend, but no 18.4 million spent coins.

# Discussion History
## moneromooo-monero | 2018-03-03T22:54:04+00:00
Was it restored from a block after it started being used ? If so, that's why, it's missing data.

## williams-r | 2018-03-04T01:15:12+00:00
yes. thanks.

## williams-r | 2018-03-04T01:45:52+00:00
i close this now?

# Action History
- Created by: williams-r | 2018-03-03T22:13:58+00:00
- Closed at: 2018-03-04T01:48:05+00:00
