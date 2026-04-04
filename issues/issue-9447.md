---
title: Offline wallet RPC "incoming_transfers" method reports tx_hash as 0000...
source_url: https://github.com/monero-project/monero/issues/9447
author: yagop
assignees: []
labels:
- low priority
- reproduction needed
created_at: '2024-08-22T07:02:28+00:00'
updated_at: '2026-02-18T21:51:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When querying an offline wallet the  RPC "incoming_transfers" method replies with `"tx_hash": "0000000000000000000000000000000000000000000000000000000000000000"`


```bash
$ curl http://localhost:18083/json_rpc \
  -d '{"jsonrpc":"2.0","id":"0","method":"incoming_transfers", "params":{ "transfer_type": "all" } }' -H 'Content-Type: application/json'
```

```json
 "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfers": [{
      "amount": 35164211634107,
      "block_height": 0,
      "frozen": false,
      "global_index": 302,
      "key_image": "2e05e81c716340d9e99cce5c228c61250a1a6b4bd70a1c546db4ce9372ab74cf",
      "pubkey": "5e2ece3fa6ee78f21670b133ffeac463a6b18f15111e5fda33496491bc04f2d1",
      "spent": true,
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "tx_hash": "0000000000000000000000000000000000000000000000000000000000000000",
      "unlocked": false
    },{
      "amount": 35164144563696,
      "block_height": 0,
      "frozen": false,
      "global_index": 303,
      "key_image": "1231bb43f3672247104a6bcc60a2a2bfbe692deba010b0cf9df590f66e20270c",
      "pubkey": "2c92e406e0a017ef73770b32b5118b8e179e5a4e93c7c4c2810e4aabf8cf572a",
      "spent": true,
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "tx_hash": "0000000000000000000000000000000000000000000000000000000000000000",
      "unlocked": false
    },{
      "amount": 35164077493412,
      "block_height": 0,
      "frozen": false,
      "global_index": 304,
      "key_image": "c5002670d788dd3b993dd78eaf410456b30b861484b7fd92e47c6a50853489d3",
      "pubkey": "34c050ff1070d097c0298165dcd862ad4aacaf4a158f398d17349da9ec51c918",
      "spent": true,
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "tx_hash": "0000000000000000000000000000000000000000000000000000000000000000",
      "unlocked": false
    }...
```

# Discussion History
# Action History
- Created by: yagop | 2024-08-22T07:02:28+00:00
