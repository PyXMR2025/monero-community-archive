---
title: daemon rpc `relay_tx` returns before all txids relayed
source_url: https://github.com/monero-project/monero/issues/8523
author: woodser
assignees: []
labels: []
created_at: '2022-08-20T14:06:46+00:00'
updated_at: '2022-08-20T17:24:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Calling daemon rpc `relay_tx` with a list of `txids` returns before all txs have been relayed. In my test, only the first txid is relayed on response. All txids are relayed after after a second or two, as indicated by `get_transaction_pool`.

This issue requests fixing `relay_tx` to return only after all txs have been relayed.

Steps to reproduce:

1. Call daemon rpc `relay_tx` with multiple txids.
2. Immediately get the txs in the pool with `get_transaction_pool`.
3. Observe txsids[1+] are not marked as relayed.



# Discussion History
## iamamyth | 2022-08-20T17:24:50+00:00
This issue appears to reflect some TODOs in the code:

https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server.cpp#L3154
https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server.cpp#L1302
https://github.com/monero-project/monero/blob/master/src/rpc/daemon_handler.cpp#L445

# Action History
- Created by: woodser | 2022-08-20T14:06:46+00:00
