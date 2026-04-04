---
title: getblocktemplate RPC returns wrong reserved_offset
source_url: https://github.com/monero-project/monero/issues/2348
author: glv2
assignees: []
labels:
- bug
created_at: '2017-08-25T22:02:09+00:00'
updated_at: '2017-09-25T20:42:22+00:00'
type: issue
status: closed
closed_at: '2017-09-25T20:42:22+00:00'
---

# Original Description
For example, calling the *getblocktemplate* RPC with a *reserve_size* parameter of 8 returns:

``` json
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "blockhashing_blob": "0506c09e82cd05f45e9c170188824df0ad30b466ef47ed3674ec0f3ec37cec5e80ed5d01964918000000007b0c2102210fa7ed43eb520c4403f8e3d6e8206be67148227137a663280d172c0a",
    "blocktemplate_blob": "0506c09e82cd05f45e9c170188824df0ad30b466ef47ed3674ec0f3ec37cec5e80ed5d019649180000000002dec15401ffa2c15401c293e896ecc501023072de4f37bf43a5d62f8c2148acf9f0329d8468df81557cf00bd66a195224ed2b013b6506bb208a11d91cddee6f8e156b1535681846cd388cf45c169c7e6796a612020800000000000000000009dac84eb863193e1cea52f32c1a0c0f0b25490fed26aebb7e97df3e696c92a8f679be8cdf9adaf3dbb5893dd21cac2cda29f6017f641954feff221f0bfb189674aaf791c8878ce968704b9b73876f1c6d316923807d7c37d9d1b584e8320f49495ad3938738635b770f7702b153a271369ff70f9ae7cb9ceb88468f4fba2dabf1a075239d90c21e0d67b45f5f032ef9c2949464b473b2c1e98c6b89dc925aa61de90eb722c0ed777e683c0feb70f52638b0f0bb6b5b0c5ff2226b7b653dd7fca9e67504894fa3462470fb45c6aecff44dee474b5fa4a1425df8c84dba7b6d72692a2168248d206ac6b9b2e2fa785d8b71f2409f8197d0da37a28c8c1f43faf82c82f36ce9831de404cf9705c4bb847da3b9c862bb0085928f011ae8cf5cbdfc7c",
    "difficulty": 18092100340,
    "expected_reward": 6797907331522,
    "height": 1384610,
    "prev_hash": "f45e9c170188824df0ad30b466ef47ed3674ec0f3ec37cec5e80ed5d01964918",
    "reserved_offset": 130,
    "status": "OK"
  }
}
```

Looking at the block header more closely:

```
0506    (block version, 2 bytes)
c09e82cd05   (timestamp, 5 bytes)
f45e9c170188824df0ad30b466ef47ed3674ec0f3ec37cec5e80ed5d01964918   (previous block hash, 32 bytes)
00000000   (nonce, 4 bytes)

02   (miner transaction version, 1 byte)
dec154   (unlock time, 3 bytes)
01 ff a2c154   (1 coin generation input, 5 bytes)
01   (1 output, 1 byte)
c293e896ecc501   (amount, 7 bytes)
02 3072de4f37bf43a5d62f8c2148acf9f0329d8468df81557cf00bd66a195224ed   (output to key, 33 bytes)
2b 01 3b6506bb208a11d91cddee6f8e156b1535681846cd388cf45c169c7e6796a612   (extra, tx pubkey, 34 bytes)
02 08 0000000000000000   (extra nonce of 8 bytes, 2 + 8 bytes)
00   (ringct signature type)
09   (transaction count)
dac84eb863193e1cea52f...   (transaction hashes)
```

The reserved extra nonce (```0000000000000000```) starts at offset ```2 + 5 + 32 + 4 + 1 + 3 + 5 + 1 + 7 + 33 + 34 + 2 = 129```, which is 1 less than the *reserved_offset* of 130 returned by the RPC.

I tried with different *reserve_size* values, on monerod version 0.10.3.1 and master:335681896a8ea6142a4331aa203ce728d507265c, and the *reserved_offset* returned by the *getblocktemplate* RPC was always 1 too much.


# Discussion History
## moneromooo-monero | 2017-08-26T15:54:15+00:00
The code adds 3 bytes after the tx key:
    res.reserved_offset += sizeof(tx_pub_key) + 3; //3 bytes: tag for TX_EXTRA_TAG_PUBKEY(1 byte), tag for TX_EXTRA_NONCE(1 byte), counter in TX_EXTRA_NONCE(1 byte)

I don't see why it needs to add one byte for the TX_EXTRA_TAG_PUBKEY, since that is before the pubkey already. That's the bug AFAICT.


## glv2 | 2017-08-26T16:23:44+00:00
I think you're right.

The offset returned by ```res.reserved_offset = slow_memmem((void*)block_blob.data(), block_blob.size(), &tx_pub_key, sizeof(tx_pub_key))``` already includes the byte for TX_EXTRA_TAG_PUBKEY.


## glv2 | 2017-08-26T16:28:01+00:00
@moneromooo-monero  do you already have a PR ready to fix this bug, or should I do one ?

## moneromooo-monero | 2017-08-26T18:17:35+00:00
I don't have one. I was wondering why such a bug was there, and second guessing whether I was wrong, since it seems fairly obvious :) Please make it to master only, in case it somehow upsets something in the pool software.

## dEBRUYNE-1 | 2017-08-27T13:56:16+00:00
+bug

## moneromooo-monero | 2017-09-25T20:30:05+00:00
+resolved

# Action History
- Created by: glv2 | 2017-08-25T22:02:09+00:00
- Closed at: 2017-09-25T20:42:22+00:00
