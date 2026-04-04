---
title: make_integrated_address from arbitrary standard_address returns integrated
  address from loaded wallet
source_url: https://github.com/monero-project/monero/issues/5003
author: ztnark
assignees: []
labels: []
created_at: '2018-12-20T21:01:45+00:00'
updated_at: '2018-12-20T21:26:01+00:00'
type: issue
status: closed
closed_at: '2018-12-20T21:26:01+00:00'
---

# Original Description
I am trying to create an integrated address from an arbitrary standard address not related to the loaded address in the monero-wallet-rpc process.

However, running the example RPC call:

`{"jsonrpc":"2.0","id":"0","method":"make_integrated_address","params":{"standard_address":"55LTR8KniP4LQGJSPtbYDacR7dz8RBFnsfAKMaMuwUNYX6aQbBcovzDPyrQF9KXF9tVU6Xk3K8no1BywnJX6GvZX8yJsXvt"}}`

returns an integrated address that points back to the loaded wallet, not the provided standard_address:

`{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "integrated_address": "4DKZNCZKW2MguWaxD3AnycfqJAdRMMy17iyAVunUBKVNAKgn41PZrNkSWQybGjkpXvfL553pN5aMdWn5Bq1DkupXi6ZpztXrKwM2CjYgTq",
        "payment_id": "b25c7c52e869000a"
    }
}`

Proven by running:

`{"jsonrpc": "2.0","i": "0","method": "split_integrated_address","params": {"integrated_address": "4DKZNCZKW2MguWaxD3AnycfqJAdRMMy17iyAVunUBKVNAKgn41PZrNkSWQybGjkpXvfL553pN5aMdWn5Bq1DkupXi6ZpztXrKwM2CjYgTq"}}`

Which returns the loaded standard address on the process:

`{
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "is_subaddress": false,
        "payment_id": "b25c7c52e869000a",
        "standard_address": "43ctMPjptkqguWaxD3AnycfqJAdRMMy17iyAVunUBKVNAKgn41PZrNkSWQybGjkpXvfL553pN5aMdWn5Bq1DkupXUfpSmcn"
    }
}`

# Discussion History
## ztnark | 2018-12-20T21:05:46+00:00
Ah, I think this is a version issue... Please hold...

## ztnark | 2018-12-20T21:26:01+00:00
Yep, version issue. Upgrading to 0.13.0.4 helped.

# Action History
- Created by: ztnark | 2018-12-20T21:01:45+00:00
- Closed at: 2018-12-20T21:26:01+00:00
