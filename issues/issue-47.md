---
title: Wallet Curl RPC Demonstration Needed
source_url: https://github.com/monero-project/monero/issues/47
author: CoinDev
assignees: []
labels: []
created_at: '2014-06-17T22:49:24+00:00'
updated_at: '2014-06-18T00:15:52+00:00'
type: issue
status: closed
closed_at: '2014-06-18T00:15:52+00:00'
---

# Original Description
Could someone demonstrate wallet rpc using curl please?

Thanks.


# Discussion History
## CoinDev | 2014-06-18T00:15:52+00:00
curl -X POST http://127.0.0.1:8080/json_rpc -d '{"jsonrpc":"2.0","id":"test","method":"getbalance","params":{}}' -H "Content-Type: application/json" 


# Action History
- Created by: CoinDev | 2014-06-17T22:49:24+00:00
- Closed at: 2014-06-18T00:15:52+00:00
