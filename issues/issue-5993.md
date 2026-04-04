---
title: Add output_idx to transfer information in the wallet
source_url: https://github.com/monero-project/monero/issues/5993
author: tmoravec
assignees: []
labels: []
created_at: '2019-10-16T14:17:49+00:00'
updated_at: '2019-11-27T10:09:58+00:00'
type: issue
status: closed
closed_at: '2019-11-27T10:09:57+00:00'
---

# Original Description
Methods like `incoming_transfers` and `get_transfer_by_txid` contain (or should: https://github.com/monero-project/monero/issues/5992) information about individual outputs in transactions. The information currently provided by the wallet does not provide the indices of individual outputs within the transactions (`output_idx`). For some use cases, it is useful to have this information. Similarly to information that the Monero Blockchain Explorer provides:

```json
{
   "data":{
      "address":"9156360164d0d44e95db3f44c554311a3039aff26c5cc57c1388bd42111c54502b9111dda4b39e4b54fd2ae70958b56b20181f345deb4271cb1992ee897cc43d",
      "outputs":[
         {
            "amount":0,
            "match":false,
            "output_idx":0,
            "output_pubkey":"f7d5e3f8bc7661396fd8689dc9b471367d3c26eb0a45960ff27a80ebcf596570"
         },
         {
            "amount":100000000000,
            "match":true,
            "output_idx":1,
            "output_pubkey":"ab475f5b78d4017f8c79e2f37ad6f67347bb216981f67c3f5ea89db59fd1f27a"
         }
      ],
      "tx_hash":"90c96deb689e373ae046107b6ae68f592827e57c23d21b5c9788fef4a321bdd3",
      "tx_prove":false,
      "viewkey":"84f5c3465fd81dbca65bcec9729d66012727790812f8d606f63c9210e45c4b01"
   },
   "status":"success"
}
```

I don't want to include the outputs with `"match": false`; just add the field to outputs belonging to this wallet.

AFAIK, the output indices are not available in the wallet currently. So this change requires changing the daemon RPC interface, and related data structures, too. I propose to attempt to implement this change, but first I'm interested in what others think about this?

EDIT: clarity.

# Discussion History
## tmoravec | 2019-11-27T10:09:57+00:00
Superseded by https://github.com/monero-project/monero/issues/6163. Instead of adding all output indices, we can break down the amount into individual payments. Closing this issue.

# Action History
- Created by: tmoravec | 2019-10-16T14:17:49+00:00
- Closed at: 2019-11-27T10:09:57+00:00
