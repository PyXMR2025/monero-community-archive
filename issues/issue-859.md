---
title: Angle brackets in JSON API responses
source_url: https://github.com/monero-project/monero/issues/859
author: sheepman0
assignees: []
labels: []
created_at: '2016-06-08T12:20:16+00:00'
updated_at: '2016-07-07T20:00:28+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:00:28+00:00'
---

# Original Description
For some reason a few of the API calls return some of the results in angle brackets but other API calls don't.

For instance:

payment_id has angle brackets:

[ monero->~ ]$ curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"split_integrated_address","params":{"integrated_address": "4BpEv3WrufwXoyJAeEoBaNW56ScQaLXyyQWgxeRL9KgAUhVzkvfiELZV7fCPBuuB2CGuJiWFQjhnhhwiH1FsHYGQQ8H2RRJveAtUeiFs6J"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "payment_id": "<420fa29b2d9a49f5>",
    "standard_address": "427ZuEhNJQRXoyJAeEoBaNW56ScQaLXyyQWgxeRL9KgAUhVzkvfiELZV7fCPBuuB2CGuJiWFQjhnhhwiH1FsHYGQGaDsaBA"
  }
}

Then here the payment_id doesn't have angle brackets:

[ monero->~ ]$ curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_payments","params":{"payment_id":"4279257e0a20608e25dba8744949c9e1caff4fcdafc7d5362ecf14225f3d9030"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "payments": [{
      "amount": 10350000000000,
      "block_height": 994327,
      "payment_id": "4279257e0a20608e25dba8744949c9e1caff4fcdafc7d5362ecf14225f3d9030",
      "tx_hash": "c391089f5b1b02067acc15294e3629a463412af1f1ed0f354113dd4467e4f6c1",
      "unlock_time": 0
    }]
  }
}

They can also be found in the guide:

https://getmonero.org/knowledge-base/developer-guides/wallet-rpc

P.S Keep up the great work guys! 👍 


# Discussion History
## moneroexamples | 2016-06-08T21:55:10+00:00
This is caused by the way monero autputs hashes, keys etc. By default it often adds the brackets to it. But I think it should be modified for rpc and a unified approach used for rpc calls. 


## moneromooo-monero | 2016-06-09T19:41:10+00:00
https://github.com/monero-project/bitmonero/pull/862

If you nice any leftover, let me know.


## fluffypony | 2016-07-07T20:00:28+00:00
Fixed


# Action History
- Created by: sheepman0 | 2016-06-08T12:20:16+00:00
- Closed at: 2016-07-07T20:00:28+00:00
