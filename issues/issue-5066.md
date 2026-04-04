---
title: Transaction notifications comes too often
source_url: https://github.com/monero-project/monero/issues/5066
author: KraxCZ
assignees: []
labels: []
created_at: '2019-01-12T21:11:27+00:00'
updated_at: '2019-01-29T00:57:17+00:00'
type: issue
status: closed
closed_at: '2019-01-29T00:57:17+00:00'
---

# Original Description
I'm using new notification system (via tx_notify). It seems to me that notifications about the same transaction comes too often (every about 20 seconds) until the transaction is mined. 
I have the experience with bitcoind where transaction is reported once when it arrives to mempool and for the second time when it is mined.
What's worse, it seems that the notifications are triggered every time get_transfer_by_txid RPC method is invoked.
Are both of the described cases intended? At least the second one seems to me as a bug.

# Discussion History
## moneromooo-monero | 2019-01-13T14:49:34+00:00
https://github.com/monero-project/monero/pull/5069 should fix it.

## moneromooo-monero | 2019-01-29T00:55:48+00:00
+resolved

## moneromooo-monero | 2019-01-29T00:57:15+00:00
+resolved

# Action History
- Created by: KraxCZ | 2019-01-12T21:11:27+00:00
- Closed at: 2019-01-29T00:57:17+00:00
