---
title: get_transactions RPC fails if transactions aren't found
source_url: https://github.com/monero-project/monero/issues/7956
author: ndorf
assignees: []
labels: []
created_at: '2021-09-19T02:25:24+00:00'
updated_at: '2021-10-11T19:05:52+00:00'
type: issue
status: closed
closed_at: '2021-10-11T19:05:52+00:00'
---

# Original Description
Instead of returning a response with the hashes that couldn't be found in the `missed_tx` field, the entire request fails with HTTP 500 due to an exception thrown [here](https://github.com/monero-project/monero/blob/665bd8933a7a00d21f983a9e89c1706692dc3015/src/rpc/core_rpc_server.cpp#L1033).

The real problem is [here](https://github.com/monero-project/monero/blob/665bd8933a7a00d21f983a9e89c1706692dc3015/src/rpc/core_rpc_server.cpp#L949). We are iterating over `txs`, which contains only the txs that have been found. But on these two lines, we're reading from `req.tx_hashes` and `vh`, which both contain *all* of the requested hashes, both found and not. So, if any weren't found, then `tx_hash` and `e.tx_hash` will be set to the wrong hash -- one of the not-found ones, instead of the one corresponding to the current `tx`.

The bug isn't triggered if all the not-found hashes happen to be at the end of the request array. 

# Discussion History
## ndorf | 2021-09-20T21:15:12+00:00
Maybe [this](https://github.com/ndorf/monero/commit/27b002c718ae62ea6e246676f42eb80d98173442) will fix it, but I don't yet know if it's correct.

## ndorf | 2021-09-20T22:08:56+00:00
[This](https://github.com/ndorf/monero/commit/7c276cc5f2983d1086f4c125b392591cad4c6954) seems to work, still need to verify that the ordering of `txs` and `missed_txs` is consistent in all cases, though.

## ndorf | 2021-10-11T19:05:52+00:00
Fixed.

# Action History
- Created by: ndorf | 2021-09-19T02:25:24+00:00
- Closed at: 2021-10-11T19:05:52+00:00
