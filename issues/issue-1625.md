---
title: monero-wallet-cli get_tx_key not working when sending from monero-wallet-rpc
source_url: https://github.com/monero-project/monero/issues/1625
author: ocminer
assignees: []
labels:
- invalid
created_at: '2017-01-23T23:43:42+00:00'
updated_at: '2017-10-15T18:42:21+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:42:21+00:00'
---

# Original Description
i'm sending payments through monero-wallet-rpc with get_tx_key set..

When looking through show_transfers out ... I see the corresponding txids in show_transfers but I cannot get the tx key for that txid .. get_tx_key reports "no tx keys found for this txid".

In my rpc.log the txid is sucessfully saved, no crashes whatsoever

show_transfers also doesn't return any receiving addresses for me 

i'm on 0.10.1.0 release 

# Discussion History
## moneromooo-monero | 2017-01-28T14:35:23+00:00
I've tested this, and it works: run monero-wallet-rpc, call transfer_split with get_tx_keys=true, and I get back the txid and tx key, and get_tx_key works with that tx id when I load monero-wallet-cli after that.

You did exit monero-wallet-rpc before trying in monero-wallet-cli, right ? If not, monero-wallet-cli would have loaded the state at the time monero-wallet-rpc was loaded.

## moneromooo-monero | 2017-08-08T11:35:08+00:00
Is this still happening ?

## moneromooo-monero | 2017-09-20T21:07:38+00:00
ping ?

## moneromooo-monero | 2017-10-03T09:57:14+00:00
I'll close this as invalid if no reply soon since it works for me.

## moneromooo-monero | 2017-10-15T18:32:28+00:00
+invalid

# Action History
- Created by: ocminer | 2017-01-23T23:43:42+00:00
- Closed at: 2017-10-15T18:42:21+00:00
