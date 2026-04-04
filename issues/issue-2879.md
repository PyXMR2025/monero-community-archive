---
title: fee == 0 in get_transfer_by_txid rpc method
source_url: https://github.com/monero-project/monero/issues/2879
author: prudnitskiy
assignees: []
labels:
- enhancement
created_at: '2017-11-30T17:42:33+00:00'
updated_at: '2018-01-30T10:24:35+00:00'
type: issue
status: closed
closed_at: '2018-01-30T10:24:35+00:00'
---

# Original Description
As I can see, RPC method `get_transfer_by_txid` shows me zero fee (0). But [moneroblocks](https://moneroblocks.info/search/) shows me real fee and amount? Is it a bug, or deserved behavior? Is there a way to get transaction fee via RPC?

# Discussion History
## moneromooo-monero | 2017-11-30T19:52:16+00:00
You've got to give more information, other this is not very useful. Like in or out tx, the JSON you're sending and receiving.

## prudnitskiy | 2017-12-01T10:12:59+00:00
TXID: be83fc780d7d53a1e7cab27b4f0a6f19b22db4a5952166c6ac370a0b59d18f23

request:
```curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"be83fc780d7d53a1e7cab27b4f0a6f19b22db4a5952166c6ac370a0b59d18f23"}}' -H 'Content-Type: application/json' -u ********:******** --digest```

response:
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "amount": 10000000000,
      "fee": 0,
      "height": 1452909,
      "note": "",
      "payment_id": "d40d84a85101579c",
      "timestamp": 1511877503,
      "txid": "be83fc780d7d53a1e7cab27b4f0a6f19b22db4a5952166c6ac370a0b59d18f23",
      "type": "in",
      "unlock_time": 0
    }
  }
}
```

## moneromooo-monero | 2017-12-01T10:33:23+00:00
In this case, it looks like it's just "not implemented yet". Since this is an incoming tx, the fee is not tracked. Should be easy to add.

## dEBRUYNE-1 | 2018-01-08T12:45:45+00:00
+enhancement

## CamilleScholtz | 2018-01-13T19:14:46+00:00
The same happens (a fee of `0`) with get_transfers (on incoming transfers). If I understand correctly this will possibly be added in the future?

## stoffu | 2018-01-14T04:43:07+00:00
#3113

## moneromooo-monero | 2018-01-30T09:49:02+00:00
+resolved

# Action History
- Created by: prudnitskiy | 2017-11-30T17:42:33+00:00
- Closed at: 2018-01-30T10:24:35+00:00
