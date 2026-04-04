---
title: '''get_outs'' daemon RPC method always contains zero txid'
source_url: https://github.com/monero-project/monero/issues/6721
author: knaccc
assignees: []
labels: []
created_at: '2020-07-25T13:06:40+00:00'
updated_at: '2020-07-26T03:36:39+00:00'
type: issue
status: closed
closed_at: '2020-07-26T03:36:39+00:00'
---

# Original Description
To reproduce:

`curl http://127.0.0.1:18081/get_outs -d '{"outputs":[{"amount":0,"index":"1234567"}]}' -H 'Content-Type: application/json'`

output:
``` json
{
  "credits": 0,
  "outs": [{
    "height": 1330759,
    "key": "3e62f1f9cf54d565b420bef33df6eb7df0b261f7d902c78007bf9c9ac6a1bd66",
    "mask": "572359f766952fb71dea8bce87927532a2216f219d94b3f2e8c36cdc1e2962d6",
    "txid": "0000000000000000000000000000000000000000000000000000000000000000",
    "unlocked": true
  }],
  "status": "OK",
  "top_hash": "",
  "untrusted": false
}
```

In this example, the correct txid is `8e856d6c63927abd8964871ab55763edb7a3551ddeba763d7006f1cf830c68a4 `

# Discussion History
## moneromooo-monero | 2020-07-25T15:59:12+00:00
You apparently did not ask for the txid (get_txid: true).

## moneromooo-monero | 2020-07-25T17:02:40+00:00
Also, https://github.com/monero-project/monero/pull/6722

## knaccc | 2020-07-26T03:36:10+00:00
Aha, thank you, it works perfectly when I do:
`curl http://127.0.0.1:18081/get_outs -d '{"get_txid":true,"outputs":[{"amount":0,"index":"1234567"}]}' -H 'Content-Type: application/json'`.

I just sent a pull request to update the documentation here: https://github.com/monero-project/monero-site/pull/1100/commits


# Action History
- Created by: knaccc | 2020-07-25T13:06:40+00:00
- Closed at: 2020-07-26T03:36:39+00:00
