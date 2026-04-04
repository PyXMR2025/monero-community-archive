---
title: It is a out transfer, but I get a in transfer from 'get_transfers' api
source_url: https://github.com/monero-project/monero/issues/9398
author: chenxiange
assignees: []
labels:
- reproduction needed
- more info needed
created_at: '2024-07-15T07:12:11+00:00'
updated_at: '2024-08-03T23:11:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
version: v0.18.3.3 - monero-wallet-rpc

tx_hash: 70f39ea6e6cbfa70519897e510897511a746409576a04e99282ade2809d621b6

<img width="975" alt="截屏2024-07-12 11 10 48" src="https://github.com/user-attachments/assets/611f6149-a851-42b6-8f77-4a12b742f145">


It is a out transfer, but I get a in type transfer from rpc 'get_transfers', and the balance is wrong!


```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "in": [{
      "address": "49uPzR1BdjDepK8FvBrzCzLNwwCexMiuBZUyEhyZztbZK1x1tFpRHDEfRUCjg1jF7oQQbSDX5kHAD8yiFWPZk5utC5ULoo1",
      "amount": 31855520000,
      "amounts": [31855520000],
      "confirmations": 8505,
      "double_spend_seen": false,
      "fee": 44480000,
      "height": 3184682,
      "locked": false,
      "note": "",
      "payment_id": "01620eed8c5b5326",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1719996295,
      "txid": "8aa4320dbb20c3703ce300cd0170439c7e0dedd0c188fb6f4c2e789a9fc40fa9",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "49uPzR1BdjDepK8FvBrzCzLNwwCexMiuBZUyEhyZztbZK1x1tFpRHDEfRUCjg1jF7oQQbSDX5kHAD8yiFWPZk5utC5ULoo1",
      "amount": 18794060000,
      "amounts": [18794060000],
      "confirmations": 2299,
      "double_spend_seen": false,
      "fee": 30680000,
      "height": 3190888,
      "locked": false,
      "note": "",
      "payment_id": "9647ddb237173184",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1720751902,
      "txid": "70f39ea6e6cbfa70519897e510897511a746409576a04e99282ade2809d621b6",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "49uPzR1BdjDepK8FvBrzCzLNwwCexMiuBZUyEhyZztbZK1x1tFpRHDEfRUCjg1jF7oQQbSDX5kHAD8yiFWPZk5utC5ULoo1",
      "amount": 30824740000,
      "amounts": [30824740000],
      "confirmations": 2309,
      "double_spend_seen": false,
      "fee": 30780000,
      "height": 3190878,
      "locked": false,
      "note": "",
      "payment_id": "0a3256bf98512ab8",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1720750862,
      "txid": "54e0f2deb8761cdb6abfc83db2d55d9719e93aaecb7e750d5d7f5162a229e247",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "49uPzR1BdjDepK8FvBrzCzLNwwCexMiuBZUyEhyZztbZK1x1tFpRHDEfRUCjg1jF7oQQbSDX5kHAD8yiFWPZk5utC5ULoo1",
      "amount": 1000000000,
      "amounts": [1000000000],
      "confirmations": 12099,
      "double_spend_seen": false,
      "fee": 44400000,
      "height": 3181088,
      "locked": false,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1719572388,
      "txid": "67e0321833dadb7507816656c904f50d4bc9a0caf2b71737f0a6fccf56f69a50",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "49uPzR1BdjDepK8FvBrzCzLNwwCexMiuBZUyEhyZztbZK1x1tFpRHDEfRUCjg1jF7oQQbSDX5kHAD8yiFWPZk5utC5ULoo1",
      "amount": 39900000000,
      "amounts": [39900000000],
      "confirmations": 63786,
      "double_spend_seen": false,
      "fee": 30680000,
      "height": 3129401,
      "locked": false,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1713366963,
      "txid": "d39e5b2774f89246eaf4944ffc62df712c397dba862d22a307469d1dfd9ff4f0",
      "type": "in",
      "unlock_time": 0
    }]
  }
}
```


# Discussion History
## selsta | 2024-07-16T22:18:03+00:00
Are these the same two wallets?

## chenxiange | 2024-07-17T10:08:40+00:00
> Are these the same two wallets?

A GUI wallet, and a read only wallet generate by the view key!

## selsta | 2024-08-03T23:11:37+00:00
Did you import key images to the view only wallet?

# Action History
- Created by: chenxiange | 2024-07-15T07:12:11+00:00
