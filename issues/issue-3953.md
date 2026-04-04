---
title: daemon rpc getblockheaderbyhash can't get block by hash.
source_url: https://github.com/monero-project/monero/issues/3953
author: apufvqsp
assignees: []
labels: []
created_at: '2018-06-07T08:13:26+00:00'
updated_at: '2018-06-07T08:49:05+00:00'
type: issue
status: closed
closed_at: '2018-06-07T08:38:16+00:00'
---

# Original Description
$ curl -X POST http://127.0.0.1:28081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getblockheaderbyhash","params":{"hash":"2480a2e6996d01d2e899a002abd2b01ccbeab37c418951e4704701ac313684e8"}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -5,
    "message": "Internal error: can't get block by hash. Hash = 2480a2e6996d01d2e899a002abd2b01ccbeab37c418951e4704701ac313684e8."
  },
  "id": "0",
  "jsonrpc": "2.0"
}

why i get this error！！！

# Discussion History
## stoffu | 2018-06-07T08:23:54+00:00
That's a tx hash on testnet: https://testnet.xmrchain.com/search?value=2480a2e6996d01d2e899a002abd2b01ccbeab37c418951e4704701ac313684e8

You request it with `gettransactions`.

## apufvqsp | 2018-06-07T08:49:05+00:00
@stoffu thank you

# Action History
- Created by: apufvqsp | 2018-06-07T08:13:26+00:00
- Closed at: 2018-06-07T08:38:16+00:00
