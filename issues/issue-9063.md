---
title: Incorrect amounts for wallet transaction after key image sync
source_url: https://github.com/monero-project/monero/issues/9063
author: mmbbee
assignees: []
labels:
- important
- reproduction needed
- more info needed
created_at: '2023-11-09T13:18:47+00:00'
updated_at: '2025-09-16T02:00:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Environment 

Monero v0.18.1.2 using view-only wallet and offline signing wallet on linux

## Issue

After our view-only wallet recently OOM'd, on reboot it had lost some history of recent withdrawals, so we had to do a key image sync with the offline signing node. The sync completed successfully and we were able to do transfers again, however after the import the history of some transactions is now incorrect, with amounts that cant be possible

For instance, calling `get_transfer_by_txid` on a prior transfer that was for < 0.2 XMR, we see the following payload
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "ANON",
      "amount": 18446744073654775634,
      "confirmations": 37119,
      "double_spend_seen": false,
      "fee": 44400000,
      "height": 2975787,
      "locked": false,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 67064
      }],
      "timestamp": 1694912775,
      "txid": "ANON",
      "type": "out",
      "unlock_time": 0
    },
    "transfers": [{
      "address": "ANON",
      "amount": 18446744073654775634,
      "confirmations": 37119,
      "double_spend_seen": false,                                                                                                                                                                                                                                                     "fee": 44400000,                                                                                                                                                                                                                                                                "height": 2975787,                                                                                                                                                                                                                                                              "locked": false,
      "note": "",                                                                                                                                                                                                                                                                     "payment_id": "0000000000000000",
      "subaddr_index": {                                                                                                                                                                                                                                                                "major": 0,
        "minor": 0                                                                                                                                                                                                                                                                    },
      "subaddr_indices": [{                                                                                                                                                                                                                                                             "major": 0,
        "minor": 67064                                                                                                                                                                                                                                                                }],
      "timestamp": 1694912775,
      "txid": "ANON",
      "type": "out",
      "unlock_time": 0
    }]
  }
```

The amount shown is 18, 446, 744.073654776 XMR, which is around the entire circulating supply, which clearly isn't possible. Curious how this is possible and if there is a way to correct this in the wallet

# Discussion History
## selsta | 2023-11-09T14:29:12+00:00
Can you try re-importing with --log-level 2 and see if it gives any clues?

Do you have a backup of the wallet cache from before it OOMd?

## mmbbee | 2023-12-13T10:49:10+00:00
@selsta - sorry for late response. We unfortunately do not have a cache from before OOM. Also cannot run re-import at will as this wallet is massive, 1m+ transactions (its an exchange wallet), so full re-import takes 12+ hours and we would have to schedule some downtime

## selsta | 2023-12-25T02:19:37+00:00
I understand that this is an exchange wallet so it's difficult to do testing, but is it possible to setup this view only wallet from scratch on a separate machine? We need more information here to debug this issue.

## mmbbee | 2023-12-27T08:44:22+00:00
Yes, will report back if when we can hopefully reproduce this issue 

## j-berman | 2025-09-16T02:00:40+00:00
One way this looks possible is if the wallet knows *some* key images but not *all* for the given tx.

A simple way to see if the wallet is missing some key images from the tx is by locating the tx in a block explorer, and then passing each key image used in the tx to the [`/frozen` wallet RPC endpoint](https://docs.getmonero.org/rpc-library/wallet-rpc/#frozen). A failure response indicates the key image is not known to the wallet. To be clear, a failure response in this context is not a response that returns frozen set to false, but a failed response.

If the wallet is missing key images for this tx, that could help narrow down where the issue is.

# Action History
- Created by: mmbbee | 2023-11-09T13:18:47+00:00
