---
title: missing 'destination' field when call 'get_transfer_by_id' rpc
source_url: https://github.com/monero-project/monero/issues/7974
author: past2017
assignees: []
labels: []
created_at: '2021-09-25T13:56:20+00:00'
updated_at: '2021-10-06T02:26:54+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:26:54+00:00'
---

# Original Description

```
 ~# monero-wallet-rpc --version
 Monero 'Oxygen Orion' (v0.17.2.3-release)
 ~# monerod --version
 Monero 'Oxygen Orion' (v0.17.2.3-release)
```

```
curl --digest -k -u 'xxxxxxxx:yyyyyyyy' -X POST http://127.0.0.1:12345/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"d10f37f14d6c62909b531a689ac002bae2d41f21a5a4af25b607e20ac85c2b3a"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "45nRCwkKRfJP1Mumn9neNydSRpv9xgjiWjC81v4efRvVabFMi67D7PPj6tAUc6cvSDJTwmEmXHQ6fR1LXauwam5tGGTZ3FH",
      "amount": 79990000000000,
      "confirmations": 1119,
      "double_spend_seen": false,
      "fee": 11240000,
      "height": 2456042,
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
      "suggested_confirmations_threshold": 94,
      "timestamp": 1632444853,
      "txid": "d10f37f14d6c62909b531a689ac002bae2d41f21a5a4af25b607e20ac85c2b3a",
      "type": "out",
      "unlock_time": 0
    },
    "transfers": [{
      "address": "45nRCwkKRfJP1Mumn9neNydSRpv9xgjiWjC81v4efRvVabFMi67D7PPj6tAUc6cvSDJTwmEmXHQ6fR1LXauwam5tGGTZ3FH",
      "amount": 79990000000000,
      "confirmations": 1119,
      "double_spend_seen": false,
      "fee": 11240000,
      "height": 2456042,
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
      "suggested_confirmations_threshold": 94,
      "timestamp": 1632444853,
      "txid": "d10f37f14d6c62909b531a689ac002bae2d41f21a5a4af25b607e20ac85c2b3a",
      "type": "out",
      "unlock_time": 0
    }]
  }
}
```



# Discussion History
## selsta | 2021-09-26T14:30:43+00:00
Is this an incoming transaction? Is this a restored wallet?

## past2017 | 2021-09-27T01:57:01+00:00
> Is this an incoming transaction? Is this a restored wallet?

type is out
yes this is a restored wallet

## selsta | 2021-09-30T22:08:22+00:00
The destination is not visible if you restore a wallet. You can confirm that by restoring a wallet into CLI / GUI.

# Action History
- Created by: past2017 | 2021-09-25T13:56:20+00:00
- Closed at: 2021-10-06T02:26:54+00:00
