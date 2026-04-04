---
title: Receive error code 0 on flush_txpool
source_url: https://github.com/monero-project/monero/issues/7383
author: euri10
assignees: []
labels: []
created_at: '2021-02-15T11:04:26+00:00'
updated_at: '2022-02-19T00:29:22+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:29:22+00:00'
---

# Original Description
If I send 
`b'{"method": "flush_txpool", "jsonrpc": "2.0", "id": 0, "params": {"txids": ["faketxid"]}}'` or any invalid txid inside the txids array I receive an error code 0 which is not defined in [here](https://github.com/monero-project/monero/blob/8286f07b265d16a87b3fe3bb53e8d7bf37b5265a/src/rpc/core_rpc_server_error_codes.h)
`b'{\r\n  "error": {\r\n    "code": 0,\r\n    "message": ""\r\n  },\r\n  "id": 0,\r\n  "jsonrpc": "2.0"\r\n}'`

Wouldn't a error code -1 (CORE_RPC_ERROR_CODE_WRONG_PARAM) be more appropriate ?

# Discussion History
## moneromooo-monero | 2021-02-15T12:29:06+00:00
https://github.com/monero-project/monero/pull/7384

# Action History
- Created by: euri10 | 2021-02-15T11:04:26+00:00
- Closed at: 2022-02-19T00:29:22+00:00
