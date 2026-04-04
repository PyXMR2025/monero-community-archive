---
title: 'Outgoing transfer counting change as incoming payment '
source_url: https://github.com/monero-project/monero/issues/8167
author: mrtestyboy781
assignees: []
labels: []
created_at: '2022-02-02T10:23:45+00:00'
updated_at: '2022-05-25T10:14:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Issue
On two rare occasions (less than .01% of all payments) we have seen the wallet create a `transfer` where the change is counted as an incoming payment and is visible in `get_bulk_payments`, `get_transfers`, and `get_transfer_by_txid` as `type="in"`

The change itself is using a payment id we haven't issued before, so it looks like an erroneous deposit to our wallet, when instead it's just change, and would normally not show up as an incoming payment.  

The payment itself constructed in a view-only / offline setup, where `transfer` is used to create the unsigned tx, its send to offline wallet to `sign_transfer` and broadcast later with `submit_transfer` 

Monerod Version : v0.17.1.9

# Details

### Expected output
In a normal outgoing transfer, you would see `get_transfer_by_txid` return
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "OUTGOING_ADDRESS",
      "amount": 1171780000000,
      "confirmations": 11,
      "destinations": [{
        "address": "OUTGOING_ADDRESS",
        "amount": 1171780000000
      }],
      "double_spend_seen": false,
      "fee": 6930000,
      "height": 2550596,
      "locked": false,
      "note": "",
      "payment_id": "XXXXXXXXXXX",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 2,
      "timestamp": 1643794568,
      "txid": "XXXXXXXXXXXX",
      "type": "out",
      "unlock_time": 0
    },
    "transfers": [{
      "address": "OUTGOING_ADDRESS",
      "amount": 1171780000000,
      "confirmations": 11,
      "destinations": [{
        "address": "OUTGOING_ADDRESS",
        "amount": 1171780000000
      }],
      "double_spend_seen": false,
      "fee": 6930000,
      "height": 2550596,
      "locked": false,
      "note": "",
      "payment_id": "XXXXXX",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 2,
      "timestamp": 1643794568,
      "txid": "XXXXXXX",
      "type": "out",
      "unlock_time": 0
    }]
  }
}
``` 
**Note** `type=out`, and `get_bulk_payments` would return nothing matching the txid, since change is ignored. 

### Actual output
Now, for these transfers where change is counted as an incoming payment we see
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "MAIN_ADDRESS",
      "amount": 42448162320000,
      "amounts": [42448162320000],
      "confirmations": 53354,
      "double_spend_seen": false,
      "fee": 7680000,
      "height": 2497242,
      "locked": false,
      "note": "",
      "payment_id": "YYYYYYYYYYYY",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 60,
      "timestamp": 1637390686,
      "txid": "XXXXXXXXXXXXXX",
      "type": "in",
      "unlock_time": 0
    },
    "transfers": [{
      "address": "MAIN_ADDRESS",
      "amount": 42448162320000,
      "amounts": [42448162320000],
      "confirmations": 53354,
      "double_spend_seen": false,
      "fee": 7680000,
      "height": 2497242,
      "locked": false,
      "note": "",
      "payment_id": "YYYYYYYYYYYY",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 60,
      "timestamp": 1637390686,
      "txid": "XXXXXXXXXXXXXX",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "OUTGOING_ADDRESS",
      "amount": 2551830000000,
      "confirmations": 53354,
      "destinations": [{
        "address": "OUTGOING_ADDRESS,
        "amount": 2551830000000
      }],
      "double_spend_seen": false,
      "fee": 7680000,
      "height": 2497242,
      "locked": false,
      "note": "",
      "payment_id": "XXXXXXXXXXXXXX",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 61807
      }],
      "suggested_confirmations_threshold": 4,
      "timestamp": 1637390678,
      "txid": "XXXXXXXXXXXXXX",
      "type": "out",
      "unlock_time": 0
    }]
  }
}
```
**Note** `type=in` and in `get_bulk_payments` we see an incoming transfer of `42448162320000` listed 

# Discussion History
## moneromooo-monero | 2022-03-05T17:40:53+00:00
Is is possible that you might have imported key images while the hot wallet was connected to an untrusted daemon (that is, a daemon that was not on 127.0.0.1 and where --trusted-daemon was not specified, OR any daemon with --untrusted-daemon specified) ? If that it the case, then I understand why this would happen (first step to fixing it).


## moneromooo-monero | 2022-03-06T08:36:09+00:00
After looking some more, this only applies to hardware wallets, so this doens't appear to be your case.

## mrtestyboy781 | 2022-04-22T11:45:54+00:00
It is possibly related to key image import, its something we have done in the past to re-sync watchonly wallet with offline signer 

## j-berman | 2022-04-23T20:38:36+00:00
@mrtestyboy781 are these transfers with the issue self-spends back to your own subaddress by chance?

## mrtestyboy781 | 2022-05-24T09:22:53+00:00
In this case they were not self-spends, it was...

main wallet -> 2 outputs
1 external output 
1 change output

but it seems like your fix may solve the issue?


## j-berman | 2022-05-24T23:36:02+00:00
I don't believe that fix would solve this issue unfortunately then. Sounds like this may be something else

# Action History
- Created by: mrtestyboy781 | 2022-02-02T10:23:45+00:00
