---
title: bootstrap - `get_coinbase_tx_sum` returns `height or count is too large` instead
  of `method not found`
source_url: https://github.com/monero-project/monero/issues/9208
author: SyntheticBird45
assignees: []
labels:
- question
- low priority
- more info needed
created_at: '2024-02-27T19:13:01+00:00'
updated_at: '2024-02-28T18:46:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**v0.18.3.1**

Using a fresh node that only synced 5973 blocks in database, `--no-sync` and `--bootstrap-daemon-address <ANY NODE URL>`

**Behavior**

```
$ curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_coinbase_tx_sum","params":{"height":5973,"count":100}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "credits": 0,
    "emission_amount": 17492292945292,
    "emission_amount_top64": 0,
    "fee_amount": 0,
    "fee_amount_top64": 0,
    "status": "OK",
    "top_hash": "",
    "untrusted": false,
    "wide_emission_amount": "0xfe8bde8458c",
    "wide_fee_amount": "0x0"
  }
}
```
```
$ curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_coinbase_tx_sum","params":{"height":5974,"count":100}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "credits": 0,
    "emission_amount": 0,
    "emission_amount_top64": 0,
    "fee_amount": 0,
    "fee_amount_top64": 0,
    "status": "height or count is too large",
    "top_hash": "",
    "untrusted": false,
    "wide_emission_amount": "",
    "wide_fee_amount": ""
  }
}
```

**Expected Behavior**

Node shouldn't tell client that `height or count is too large`, by solely relying on the database.

# Discussion History
## selsta | 2024-02-27T22:19:38+00:00
I might be missing something but why should it return `method not found`?

## SyntheticBird45 | 2024-02-27T22:21:22+00:00
because the bootstrap daemon have `--restricted-rpc`. But I'm realizing it's maybe out of scope for `get_coinbase_tx_sum` to fetch the response to the bootstrap daemon

## selsta | 2024-02-28T18:46:48+00:00
The bootstrap-daemon feature was created so that someone can scan a wallet and create a transaction while the local node is still syncing. Endpoints like `get_coinbase_tx_sum` that require an unrestricted bootstrap node do seem out of scope.

The existing code could be improved for such edge cases but it doesn't seem like high priority.

# Action History
- Created by: SyntheticBird45 | 2024-02-27T19:13:01+00:00
