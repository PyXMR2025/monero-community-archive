---
title: 'monero-wallet-rpc wach-only '
source_url: https://github.com/monero-project/monero/issues/4383
author: luoqeng
assignees: []
labels: []
created_at: '2018-09-15T03:29:14+00:00'
updated_at: '2018-09-27T12:33:58+00:00'
type: issue
status: closed
closed_at: '2018-09-27T12:33:58+00:00'
---

# Original Description
private-testnet

wallet2 transfer wallet1
```
curl -X POST http://127.0.0.1:8084/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":1000000000000,"address":"9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8"}],"mixin":4,"get_tx_key": true}}' -H 'Content-Type: application/json'

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "amount": 1000000000000,
    "fee": 4000000000,
    "multisig_txset": "",
    "tx_blob": "",
    "tx_hash": "1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433",
    "tx_key": "49c3b747e7fec1b8fe1a89ee2f7898edb279d93b53fb6336ae1ebc1ded483006",
    "tx_metadata": "",
    "unsigned_txset": ""
  }
}
```

wallet2 wach-only mode 
get_transfer_by_txid  "amount":6575000000000 "type":"in" ?
```
curl -X POST http://localhost:8085/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433"}}' -H 'Content-Type: application/json'

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "A2rgGdM78JEQcxEUsi761WbnJWsFRCwh1PkiGtGnUUcJTGenfCr5WEtdoXezutmPiQMsaM4zJbpdH5PMjkCt7QrXAhV8wDB",
      "amount": 6575000000000,
      "confirmations": 22,
      "double_spend_seen": false,
      "fee": 18446736498709551616,
      "height": 2943,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1536839423,
      "txid": "1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433",
      "type": "in",
      "unlock_time": 0
    }
  }
}
```
Why is the amount and type of wallet2 watch-noly wrong?

wallet2 get_transfer_by_txid
```
curl -X POST http://localhost:8084/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "A2rgGdM78JEQcxEUsi761WbnJWsFRCwh1PkiGtGnUUcJTGenfCr5WEtdoXezutmPiQMsaM4zJbpdH5PMjkCt7QrXAhV8wDB",
      "amount": 1000000000000,
      "confirmations": 47,
      "destinations": [{
        "address": "9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8",
        "amount": 1000000000000
      }],
      "double_spend_seen": false,
      "fee": 4000000000,
      "height": 2943,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1536839423,
      "txid": "1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433",
      "type": "out",
      "unlock_time": 0
    }
  }
}
```

wallet1 get_transfer_by_txid
```
curl -X POST http://localhost:8081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8",
      "amount": 1000000000000,
      "confirmations": 158,
      "double_spend_seen": false,
      "fee": 18446736498709551616,
      "height": 2943,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1536839423,
      "txid": "1675c0f6959b87c56183f74973d147e09672d95cfc18cbc09a74c7775715a433",
      "type": "in",
      "unlock_time": 0
    }
  }
}
```


# Discussion History
## moneromooo-monero | 2018-09-16T09:57:17+00:00
The watch wallet only sees incoming, so it only sees the change, it's indistinguishable from an incoming tx.

If it's got the key images for its outputs, then it should be able to see the outgoing outputs too, and so know it's an outgoing tx. If not, it can't.

Did your watch wallet have the key images for the sent outputs ?


## moneromooo-monero | 2018-09-16T10:07:09+00:00
To see that, load the wallet in monero-wallet-cli, and type "incoming_transfers verbose". If the key images aren't known, they'll show as ????

## luoqeng | 2018-09-27T12:33:23+00:00
> To see that, load the wallet in monero-wallet-cli, and type "incoming_transfers verbose". If the key images aren't known, they'll show as ????

I understand, thank you.

# Action History
- Created by: luoqeng | 2018-09-15T03:29:14+00:00
- Closed at: 2018-09-27T12:33:58+00:00
