---
title: 'wallet-rpc: how make transfer on view-only wallet and sign it on cold-wallet?'
source_url: https://github.com/monero-project/monero/issues/4176
author: frankegoesdown
assignees: []
labels:
- invalid
created_at: '2018-07-25T15:26:55+00:00'
updated_at: '2018-07-25T16:08:59+00:00'
type: issue
status: closed
closed_at: '2018-07-25T16:08:59+00:00'
---

# Original Description
Hello
I need to make a transfer on hot-wallet (view-only) and sign it on my offline wallet(cold-wallet) via wallet-rpc

And then send it to blockchain

It possible?
I know how it can be done through a wallet-cli and unsigned_tx file

```
curl -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":1000,"address":"9uUr8urCW73Hf1S2PxDkmKBk8wRujbSNuVgusyUDGv5seSjbKwDATafCXAmbWd8cWHghhzF2J4hpGLXEkUkxHCT35A4VaU3"}],"mixin":1,"get_tx_key": true}}' -H 'Content-Type:application/json'
{
  "error": {
    "code": -4,
    "message": "transaction was rejected by daemon"
  },
  "id": "0",
  "jsonrpc": "2.0"
```

with `do_not_relay` parameter it returns:
```
curl -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destiations":[{"amount":1000,"address":"9uUr8urCW73Hf1S2PxDkmKBk8wRujbSNuVgusyUDGv5seSjbKwDATafCXAmbWd8cWHghhzF2J4hpGLXEkUkxHCT35A4VaU3"}],"mixin":1,"get_tx_key": true, "do_not_relay":true}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "amount": 1000,
    "fee": 851850000,
    "multisig_txset": "",
    "tx_blob": "",
    "tx_hash": "f7afba7ccb8e859a7600927053759d51f3904add1ba5217329a4a402d48fa6c5",
    "tx_key": "f9a932f872f28b1c1be19342c84e59fbe244b6e902430daf22dbd8b2f0eb4100",
    "tx_metadata": ""
  }
```

# Discussion History
## hyc | 2018-07-25T16:03:18+00:00
+invalid

Look on monero.stackexchange.com. This issue tracker is for bug reports, not help requests.


# Action History
- Created by: frankegoesdown | 2018-07-25T15:26:55+00:00
- Closed at: 2018-07-25T16:08:59+00:00
