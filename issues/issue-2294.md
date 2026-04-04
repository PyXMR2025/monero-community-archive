---
title: Is transfer_split RPC supposed to return -4 (transaction too big)?
source_url: https://github.com/monero-project/monero/issues/2294
author: oliverw
assignees: []
labels:
- invalid
created_at: '2017-08-14T21:12:06+00:00'
updated_at: '2017-10-15T13:24:19+00:00'
type: issue
status: closed
closed_at: '2017-10-15T13:24:19+00:00'
---

# Original Description
My pool test-installation running against v0.10.3.1 daemons (connected to the testnet) is experiencing problems when performing payouts to test-miners.

Due to the extremely low difficulty of the testnet, workers manage to solve a block using a single share and thus accumulate funds that would otherwise be split between hundreds of workers (PPLNS). I now have a case where the pool has received several block rewards of 17.56 XMR each and attempts to payout 2097.49 XMR to my test miner. 

The initial 'transfer' RPC request (one destination) fails with -4. Unfortunately the automatic retry with 'transfer_split' also fails with -4. Is this supposed to happen?

# Discussion History
## moneromooo-monero | 2017-08-14T21:51:38+00:00
No, it should split the tx to pay that miner in several transasctions.
Run monero-wallet-rpc with --log-level wallet*:2 and put the resulting log on fpaste.org, then paste the URL here and I will take a look.

## oliverw | 2017-08-15T06:57:14+00:00
Here you go: https://paste.fedoraproject.org/paste/kqQVOD-wsDkmX4XewHS6TQ

RPC request for initial <code>transfer</code> attempt:

```
{
  "jsonrpc":"2.0",
  "method":"transfer",
  "params":{
    "destinations":[{
       "address":"9wq792k9sxVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4bh2tCh",
      "amount":2498356476812098
    }],
    "mixin":0,
    "payment_id":null,
    "get_tx_key":true,
    "unlock_time":0
  },
  "id":"1502780105"
}
```
And for the retry using <code>transfer_split</code>:

```
{
  "jsonrpc":"2.0",
  "method":"transfer_split",
  "params":{
    "destinations":[{
      "address":"9wq792k9sxVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4bh2tCh",
      "amount":2498356476812098
    }],
    "mixin":0,
    "payment_id":null,
    "get_tx_key":true,
    "unlock_time":0
  },
  "id":"1502780204"
}
```



## moneromooo-monero | 2017-08-15T09:39:05+00:00
This log is truncated, it seems to just have the rejection at the end.
Loads of small dusty outputs though, that's very odd. It looks like you're not synced at all. Current coinbase should be just one output.

## oliverw | 2017-08-15T10:20:50+00:00
@moneromooo-monero Well it's a private testnet running inside docker ([Source](https://github.com/oliverw/monero-private-testnet))

`
docker run -it -d -p 28081:28081 -p 28082:28082 -p 38081:38081 -p 38082:38082 oweichhold/monero-private-testnet`

Addresses
-  Pool: 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8
- Bob (Miner): 9wq792k9sxVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4bh2tCh

RPC using curl (Port Pool: 28081, Bob: 38081):

`
curl -u monerorpc:rpcpassword --digest --data-binary '{"jsonrpc": "2.0", "id":"1", "method": "get_info", "params": [] }' -H 'content-type: application/json' -X POST http://127.0.0.1:28081/json_rpc`

Wallet-RPC using curl (Port Pool: 28082, Bob: 38082)

`curl -u monerorpc:rpcpassword --digest --data-binary '{"jsonrpc": "2.0", "id":"1", "method": "getaddress", "params": [] }' -H 'content-type: application/json' -X POST http://127.0.0.1:28082/json_rpc`

## moneromooo-monero | 2017-10-03T11:07:39+00:00
I went back to this, and the log's timed out. Error -4 is a generic error, and there is no "transaction too big"  message in the source. There is a transaction too large, though. Can you post another log (level 2) please ?


## moneromooo-monero | 2017-10-15T13:20:54+00:00
Given this is a daemon mining on a reset network, new txes are generated for recent rules, and older rules are applied. So given there's no further info to make sure it's really that and not an actual bug (which we'd have most likely heard about from pool operators), I'll close.

+invalid


# Action History
- Created by: oliverw | 2017-08-14T21:12:06+00:00
- Closed at: 2017-10-15T13:24:19+00:00
