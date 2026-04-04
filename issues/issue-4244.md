---
title: RPC Transfer Error -> No destinations for this transfer
source_url: https://github.com/monero-project/monero/issues/4244
author: i3bitcoin
assignees: []
labels: []
created_at: '2018-08-10T09:27:17+00:00'
updated_at: '2018-08-12T17:34:36+00:00'
type: issue
status: closed
closed_at: '2018-08-12T17:34:36+00:00'
---

# Original Description
Hello, after the last update v0.12.3.0 I cannot send XMR to another addresses via Wallet RPC.

Inputs:

Array
(
    [destinations] => Array
        (
            [amount] => 210000000000
            [address] => Address
        )

    [payment_id] => Payment ID
    [mixin] => 0
    [unlock_time] => 0
)

Outputs:

Array
(
    [code] => -20
    [message] => No destinations for this transfer
)

# Discussion History
## moneromooo-monero | 2018-08-10T15:35:33+00:00
Please post the JSON you're sending.

## i3bitcoin | 2018-08-10T18:20:36+00:00
I've tried both, but got same error

{"id":1,"method":"transfer","params":{"destinations":{"amount":210000000000,"address":"address"},"payment_id":"payment_id","mixin":0,"unlock_time":0}}

{"id":1,"method":"transfer","params":[{"destinations":{"amount":210000000000,"address":"address"},"payment_id":"payment_id","mixin":0,"unlock_time":0}]}

## moneromooo-monero | 2018-08-11T17:34:21+00:00
transfer does not have a destinations parameter. transfer_split does.
If you want to use transfer, use the destination parameter, but transfer_split is probably what you want.

## i3bitcoin | 2018-08-12T09:39:01+00:00
The docs should be fixed then
https://github.com/monero-project/monero/wiki/Wallet-RPC-Documentation#transfer

Thanks for you help

Edit.
I've just tested destination instead of destinations and it doesn't work as well.
This function worked well in the previous release.

## moneromooo-monero | 2018-08-12T11:03:46+00:00
Actually, I was wrong. It's destinations. I must be confusing with something else.

## stoffu | 2018-08-12T11:08:15+00:00
@i3bitcoin Your JSON is in a wrong format. `destinations` is supposed to be an array of object consisting of `address` and `amount`, so instead of 

```json
{"id":1,"method":"transfer","params":[{"destinations":{"amount":210000000000,"address":"address"},"payment_id":"payment_id","mixin":0,"unlock_time":0}]}
```

it should be

```json
{"id":1,"method":"transfer","params":{"destinations":[{"amount":210000000000,"address":"address"}],"payment_id":"payment_id","mixin":0,"unlock_time":0}}
```


## i3bitcoin | 2018-08-12T17:34:31+00:00
@stoffu okay, now it works great!
Thank you guys!

# Action History
- Created by: i3bitcoin | 2018-08-10T09:27:17+00:00
- Closed at: 2018-08-12T17:34:36+00:00
