---
title: relay a confirmed tx to wallet produced dirty data
source_url: https://github.com/monero-project/monero/issues/8793
author: wangsai-silence
assignees: []
labels: []
created_at: '2023-03-21T08:36:09+00:00'
updated_at: '2023-04-25T15:24:31+00:00'
type: issue
status: closed
closed_at: '2023-04-25T15:24:31+00:00'
---

# Original Description
- First, I create a tx with wallet `transfer` RPC 
```
curl http://localhost:18082/json_rpc \
-u admin:123 --digest \
-H 'Content-Type: application/json' \
-d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":60,"address":"7BWQGPqwy3TAbykGqDoD9fXq6GS84121XRRKJvcb2y6Md2Bed42mvSwF5LqeVAqtrQVo1T9D3WsqP3THyLW4cZWTFjY8p2g"}],"account_index":0,"get_tx_key":false,"get_tx_hex":false, "do_not_relay": true, "get_tx_metadata":true}}' 
```

- Then, I relay it to chain
```
curl http://localhost:18082/json_rpc  \
-u admin:123 --digest \
-H 'Content-Type: application/json' \
-d '{"jsonrpc":"2.0","id":"0","method":"relay_tx","params":{"hex":"metadata..."}}'  \

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "tx_hash": "3850e52507f5a9b7038417d758bb1c12e93bb57187d562c614be81844735024e"
  }
}

```

- After tx is confirmed. I check the wallet balance

```
curl http://127.0.0.1:18082/json_rpc \
-u admin:123 --digest \
-H 'Content-Type: application/json' \
-d '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0,"address_indices":[]}}' \

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 61085212629330,
    "blocks_to_unlock": 5,
    "multisig_import_needed": false,
    "per_subaddress": [...],
    "time_to_unlock": 0,
    "unlocked_balance": 60906659842570
  }
}
```

- It seems all good, until I relay it again. The wallet accepts it and returns a tx_id as step 2
```
curl http://localhost:18082/json_rpc  \
-u admin:123 --digest \
-H 'Content-Type: application/json' \
-d '{"jsonrpc":"2.0","id":"0","method":"relay_tx","params":{"hex":"metadata..."}}'  \

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "tx_hash": "3850e52507f5a9b7038417d758bb1c12e93bb57187d562c614be81844735024e"
  }
}

```

- Obviously, this tx won't on chain again. So after 500s, it was marked as failed. But when I checked balance again, balance increased.

```
curl http://127.0.0.1:18082/json_rpc \
-u admin:123 --digest \
-H 'Content-Type: application/json' \
-d '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0,"address_indices":[]}}' \

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 61085364099330,
    "blocks_to_unlock": 0,
    "multisig_import_needed": false,
    "per_subaddress": [...],
    "time_to_unlock": 0,
    "unlocked_balance": 61085364099330
  }
}
```

**I'd have to run `rescan_spent` to fix balance and unspent info.  Relay tx should be a idempotent function.**

# Discussion History
## moneromooo-monero | 2023-03-21T14:02:58+00:00
What makes you think the balance change is due to this transaction ?

## moneromooo-monero | 2023-03-21T14:24:39+00:00
Nevermind, I can repro.

## moneromooo-monero | 2023-03-21T15:15:44+00:00
https://github.com/monero-project/monero/pull/8796

# Action History
- Created by: wangsai-silence | 2023-03-21T08:36:09+00:00
- Closed at: 2023-04-25T15:24:31+00:00
