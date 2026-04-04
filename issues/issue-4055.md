---
title: payment_id not work
source_url: https://github.com/monero-project/monero/issues/4055
author: DogLi
assignees: []
labels:
- invalid
created_at: '2018-06-26T02:55:59+00:00'
updated_at: '2018-09-14T11:48:58+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:48:58+00:00'
---

# Original Description
I use the `transfer` method in monero-wallet-rpc, and I set a 64-character hex string as the `payment_id` in params like:

```
curl -X POST http://127.0.0.1:28082/json_rpc  \
   -H 'Content-Type: application/json' \
   -u user:password --digest \
    -d '{"jsonrpc":"2.0","method":"transfer","params":{"destinations":[{"address":"9vwHdk4vYpn3P6oVngQDWGAYKKHbvLxjjYnDv2a3GnrP5g559af1J6HXXkF3kfGq89KVmE4yZHCLJJDwEbnyCuH83NE8ALh","amount":199999950000}],"mixin":4,"unlock_time":0,"payment_id":"4279257e0a20608e25dba8744949c9e1caff4fcdafc7d5362ecf14225f3d9031","get_tx_key":true,"priority":0,"get_tx_hex":true}}'
```
But I can not get payment infomation base on `payment_id` in [get_payments](https://getmonero.org/resources/developer-guides/wallet-rpc.html#get_payments) or [get_bulk_payments ](https://getmonero.org/resources/developer-guides/wallet-rpc.html#get_bulk_payments) , which result is empty! 

If I set the `payment_ids` empty and set the `min_block_height`, I can get all the payments info, but as we see, all the `payment_id` is `0000000000000000000000000000000000000000000000000000000000000000`:

```
curl -X POST http://127.0.0.1:28082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_bulk_payments","params":{"payment_ids":[],"min_block_height":1131777}}' -H 'Co│Type "help", "copyright", "credits" or "license" for more information.
ntent-Type: application/json
```


# Discussion History
## moneromooo-monero | 2018-07-13T09:29:16+00:00
Worked for me:

```
$ curl -X POST http://127.0.0.1:8989/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_bulk_payments","params":{"payment_ids":[],"min_block_height":1131777}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "payments": [{
      "address": "xxx",
      "amount": 199999950000,
      "block_height": 1137382,
      "payment_id": "4279257e0a20608e25dba8744949c9e1caff4fcdafc7d5362ecf14225f3d9031",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "tx_hash": "8b6888b5ff84b74b20f9b6edb16939bd8bf00b9a99ae4a4e939431d236e61c4a",
      "unlock_time": 0
    },{
      "address": "xxx",
      "amount": 7294520223378,
      "block_height": 1137381,
      "payment_id": "0000000000000000000000000000000000000000000000000000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "tx_hash": "85126fb41a2418f70547942d855c407548908b10a506c86c0af0492d84637513",
      "unlock_time": 1137441
    }]
  }
}
```

The first one is the one I sent using your command, the second one's a coinbase.

Try with a more recent version ?

## moneromooo-monero | 2018-08-15T11:15:51+00:00
If you don't comment with more info, I'll close ince it works for me.

## moneromooo-monero | 2018-09-14T11:30:51+00:00
Works for me. Please reopen if you try it with a current master and it still does not work.

+invalid


# Action History
- Created by: DogLi | 2018-06-26T02:55:59+00:00
- Closed at: 2018-09-14T11:48:58+00:00
