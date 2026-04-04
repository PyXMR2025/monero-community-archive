---
title: RPC call get_coinbase_tx_sum returns 0 fees and 0 emission for some (all?)
  blocks
source_url: https://github.com/monero-project/monero/issues/2476
author: whateverpal
assignees: []
labels: []
created_at: '2017-09-19T12:40:05+00:00'
updated_at: '2017-09-22T10:00:24+00:00'
type: issue
status: closed
closed_at: '2017-09-22T10:00:24+00:00'
---

# Original Description
monerod (v0.11.0.0) RPC call get_coinbase_tx_sum returns

{u'status': u'OK', u'fee_amount': 0, u'emission_amount': 0}

for blocks 800000, 1200000, 1400000

monerod is run with --block-sync-size=20 and --detach flags



# Discussion History
## moneromooo-monero | 2017-09-19T13:13:51+00:00
Thanks, fixed in https://github.com/monero-project/monero/pull/2477

## moneromooo-monero | 2017-09-22T09:48:21+00:00
+resolved

# Action History
- Created by: whateverpal | 2017-09-19T12:40:05+00:00
- Closed at: 2017-09-22T10:00:24+00:00
