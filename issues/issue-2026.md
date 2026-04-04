---
title: generateblocks is missing in daemon RPC documentation
source_url: https://github.com/monero-project/monero-site/issues/2026
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-08-16T02:10:54+00:00'
updated_at: '2022-12-01T07:14:22+00:00'
type: issue
status: closed
closed_at: '2022-12-01T07:14:22+00:00'
---

# Original Description
Developers need to test their code and `generateblocks` is quite handy. I've used it a lot, but still could use the guide entry so I could finally learn what the `prev_block` and `starting_nonce` input values are used for.

Where it is missing:
https://github.com/monero-project/monero-site/blob/master/resources/developer-guides/daemon-rpc.md

C++ reference:
https://github.com/monero-project/monero/blob/v0.18.1.0/src/rpc/core_rpc_server_commands_defs.h#L1076-L1107

#### Example Use:

Start `monerod` in test mode:
```
monerod --detach --regtest --offline --fixed-difficulty=1 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081
```

Request:
```
curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"generateblocks","params":{
"amount_of_blocks":1,
"wallet_address":"42eTJxqsYwsSpFCRUp19vPAXNruqAUqnFMY2XN198643Ukrera958dY4qbRdoaoCVffhbC7ro4nzVBMw1E8ip7LAKG3SrsU"}' -H 'Content-Type: application/json'
```

Response:
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "blocks": ["49b712db7760e3728586f8434ee8bc8d7b3d410dac6bb6e98bf5845c83b917e4"],
    "height": 9783,
    "status": "OK",
    "untrusted": false
  }
}
```



# Discussion History
# Action History
- Created by: dimalinux | 2022-08-16T02:10:54+00:00
- Closed at: 2022-12-01T07:14:22+00:00
