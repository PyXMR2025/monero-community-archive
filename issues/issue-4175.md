---
title: 'wallet_rpc: invalid jsonrpc value of error response'
source_url: https://github.com/monero-project/monero/issues/4175
author: artyomsol
assignees: []
labels: []
created_at: '2018-07-24T17:19:06+00:00'
updated_at: '2018-08-16T18:56:52+00:00'
type: issue
status: closed
closed_at: '2018-08-16T18:56:52+00:00'
---

# Original Description
Wallet _RPC response contains empty string in `jsonrpc` member of error response. 

Build version affected: `0.12.3.0`

#### Steps to reproduce
1. Post improper JSON query to RPC 
```
{"jsonrpc":"2.0","id":"0",
	"method":"transfer",
	"params":{
		"destinations": [
				{
					"amount": 1000000000000000000000000,
					"address": "SOME VALID ADDRESS"
				}
			]
	}
}
```
2. Get the error response
```
{
  "error": {
    "code": -32700,
    "message": "Parse error"
  },
  "id": 0,
  "jsonrpc": ""
}
```
See the `"jsonrpc": ""` which [MUST](https://www.jsonrpc.org/specification#response_object) be `"2.0"`

# Discussion History
## moneromooo-monero | 2018-07-25T22:01:33+00:00
https://github.com/monero-project/monero/pull/4177

## moneromooo-monero | 2018-08-16T18:53:47+00:00
+resolved

# Action History
- Created by: artyomsol | 2018-07-24T17:19:06+00:00
- Closed at: 2018-08-16T18:56:52+00:00
