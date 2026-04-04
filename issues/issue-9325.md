---
title: Build unsigned transaction does not return "tx_blob" and "unsigned_txset"
source_url: https://github.com/monero-project/monero/issues/9325
author: dev-warrior777
assignees: []
labels: []
created_at: '2024-05-13T10:59:37+00:00'
updated_at: '2024-05-15T09:58:59+00:00'
type: issue
status: closed
closed_at: '2024-05-15T09:58:59+00:00'
---

# Original Description
Hi, I am building a shell script which uses many of the monero `wallet-rpc` api calls using curl. 

Here I am trying to build an **unsigned tx** and call the `transfer` api with the `do_not_relay` field set to **true** as per the example in sign_transfer in https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#sign_transfer

The example states: "In the example below, we first generate an unsigned_txset on a read only wallet before signing it:"

_I expected to see `tx_blob` and `unsigned_txset` populated. Is there something else I should specify?_

```bash

./wallet_transfer_norelay.sh 28084 1000011110000 453w1dEoNE1HjKzKVpAU14Honzenqs5VKKQWHb7RuNHLa4ekXhXnGhR6RuttNpvjbtDjzy8pTgz5j4ZSsWQqyxSDBVQ4WCk
{"destinations":[{"amount":1000011110000,"address":"453w1dEoNE1HjKzKVpAU14Honzenqs5VKKQWHb7RuNHLa4ekXhXnGhR6RuttNpvjbtDjzy8pTgz5j4ZSsWQqyxSDBVQ4WCk"}], "account_index":0,"subaddr_indices":[0],"priority":0,"do_not_relay":true,"get_tx_key": true }

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "amount": 1000011110000,
    "amounts_by_dest": {
      "amounts": [1000011110000]
    },
    "fee": 1808400000,
    "multisig_txset": "",
    "spent_key_images": {
      "key_images": ["351020242e1970c8ea11e63cd4ff709902ebdd68fcdd0f4c913b633d85dc1515"]
    },
    "tx_blob": "",
    "tx_hash": "cd11977fbe65a700ffed5fa3a54f8dc3031f8c4267fe79cdef3c4ac523cc6da3",
    "tx_key": "7b721d9c63813018edcc0e42a5dc60ff27adfd021660f4f0a6e83cb3e0f9650b",
    "tx_metadata": "",
    "unsigned_txset": "",
    "weight": 1507
  }
}

```

the official rpc documentation example shows:

```bash
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":1000000000000,"address":"7BnERTpvL5MbCLtj5n9No7J5oE5hHiB3tVCK5cjSvCsYWD2WRJLFuWeKTLiXo5QJqt2ZwUaLy2Vh1Ad51K7FNgqcHgjW85o"}],"account_index":0,"subaddr_indices":[0],"priority":0,"do_not_relay":true,"get_tx_hex":true}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "amount": 1000000000000,
    "fee": 15202740000,
    "multisig_txset": "",
    "tx_blob": "...long_hex...",
    "tx_hash": "c648ba0a049e5ce4ec21361dbf6e4b21eac0f828eea9090215de86c76b31d0a4",
    "tx_key": "",
    "tx_metadata": "",
    "unsigned_txset": "...long_hex..."
  }
}

```

Would be grateful for your help


# Discussion History
## dev-warrior777 | 2024-05-13T20:32:47+00:00
Ok .. I got as far as getting an 'unsigned_txset'  blob from a view_only wallet. It is huge ;-) 

Then when I try to sign with the parent non--view_only wallet I get:

   `"Failed to sign unsigned tx: Hot wallets cannot import outputs"

What I was looking for was something like bitcoin ``signrawtransaction`

## dev-warrior777 | 2024-05-14T14:11:56+00:00
What is in the txset blob?

## dev-warrior777 | 2024-05-15T09:58:59+00:00
Solved with https://monero.stackexchange.com/questions/2868/is-there-any-way-to-construct-a-transaction-manually

Sorry of inconvenience

Closed

# Action History
- Created by: dev-warrior777 | 2024-05-13T10:59:37+00:00
- Closed at: 2024-05-15T09:58:59+00:00
