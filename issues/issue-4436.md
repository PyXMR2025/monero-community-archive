---
title: 'get_transfer_by_txid RPC method still returns single transfer when multiple
  are present '
source_url: https://github.com/monero-project/monero/issues/4436
author: magnoliafan
assignees: []
labels: []
created_at: '2018-09-25T10:25:13+00:00'
updated_at: '2018-10-02T21:01:07+00:00'
type: issue
status: closed
closed_at: '2018-10-02T21:01:07+00:00'
---

# Original Description
Monero transaction can contain multiple transfers to different subaddresses of one account. In this case not all transfers can be shown. Maybe, wallet rpc should have get_transfers_by_txid, that shows all transfers of a transaction related to wallet, or chosen account?

# Discussion History
## magnoliafan | 2018-09-25T10:52:26+00:00
Or add filter_by_txid flag and txid param to get_transfers

## moneromooo-monero | 2018-10-01T12:52:12+00:00
Works for me. Are you sure you passed the right account_index ?

## magnoliafan | 2018-10-01T13:39:03+00:00
Yes. But single transaction have two outputs, first to subaddress no1, and second to subaddress no2. Same account index 0.

## moneromooo-monero | 2018-10-01T14:05:24+00:00
Ah, I had misunderstood, I sent to different accounts from the same wallet. It does seem buggy now.

## magnoliafan | 2018-10-01T14:18:19+00:00
What do you think about get_transfers_by_txid i've descibed above?

## moneromooo-monero | 2018-10-01T14:49:28+00:00
https://github.com/monero-project/monero/pull/4484

## moneromooo-monero | 2018-10-02T20:50:17+00:00
+resolved

# Action History
- Created by: magnoliafan | 2018-09-25T10:25:13+00:00
- Closed at: 2018-10-02T21:01:07+00:00
