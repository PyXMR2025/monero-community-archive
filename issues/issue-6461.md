---
title: RPC omits default/dummy payment ID
source_url: https://github.com/monero-project/monero/issues/6461
author: Mitchellpkt
assignees: []
labels: []
created_at: '2020-04-18T20:22:51+00:00'
updated_at: '2020-04-19T00:10:47+00:00'
type: issue
status: closed
closed_at: '2020-04-19T00:10:47+00:00'
---

# Original Description
### Description

Transactions that are created through the RPC interface do not include a payment ID by default, but I think that other core software does. It would be ideal if transactions always included a dummy PID (unless a real one is present) to prevent software fingerprinting and transaction linkability.

### INPUT: 
```
curl -X POST http://127.0.0.1:18082/json_rpc -d 
'{"jsonrpc":"2.0","id":"0","method":"transfer","params":{
"destinations":[{"amount":500000000,"address":"44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A"}],
"account_index":0,
"subaddr_indices":[0],
"priority":0,
"ring_size":11,
"get_tx_key": true}}' 
-H 'Content-Type: application/json'
```

### OUTPUT:
Transaction [b47775450b3e86b128f4d1be1b501cbf9f1cc74918488b557ea21c238cea12db](https://xmrchain.net/search?value=b47775450b3e86b128f4d1be1b501cbf9f1cc74918488b557ea21c238cea12db), with tx_extra containing only:
`010650bdc4d3da7cc962ccfcd7cfd84b704057729096419a090cc92d6d65e2c0360209018d240af750cc7893`

# Discussion History
## xiphon | 2020-04-18T23:09:33+00:00
> tx_extra containing only:
> `010650bdc4d3da7cc962ccfcd7cfd84b704057729096419a090cc92d6d65e2c0360209018d240af750cc7893`

`0209018d240af750cc7893` is encrypted payment id, the dummy one.

## Mitchellpkt | 2020-04-18T23:13:16+00:00
Oh good, I glanced at it wrong and mistook that for the txn pubkey.

## Mitchellpkt | 2020-04-19T00:10:25+00:00
Yea this looks fine. Closing issue.

# Action History
- Created by: Mitchellpkt | 2020-04-18T20:22:51+00:00
- Closed at: 2020-04-19T00:10:47+00:00
