---
title: Missing payment ID for outgoing transfer after cache deleted
source_url: https://github.com/monero-project/monero/issues/8378
author: woodser
assignees: []
labels: []
created_at: '2022-06-05T16:07:26+00:00'
updated_at: '2022-07-22T11:26:42+00:00'
type: issue
status: closed
closed_at: '2022-07-22T11:26:18+00:00'
---

# Original Description
monero-wallet-rpc does not return payment ids for outgoing transfers after the cache is deleted.

Steps to reproduce:

1. transfer to integrated address
2. delete wallet cache
3. get transfer by hash id
4. observe that transfer does not have payment id

# Discussion History
## Cactii1 | 2022-07-20T21:23:39+00:00
By design, this transfer information is only stored in the wallet cache, once deleted it is irrecoverable.

## woodser | 2022-07-20T21:57:07+00:00
The payment ID is public on the blockchain.

## Cactii1 | 2022-07-20T22:38:53+00:00
An encrypted version if it.

## woodser | 2022-07-20T22:40:59+00:00
Ah, so it's intentional that the payment ID not be decryptable without the wallet cache and not the private key?

## Cactii1 | 2022-07-20T22:53:42+00:00
It's not stored as plain text on the blockchain. If the private key is known you can, however I don't think any wallet currently has the capability of restoring this information from the blockchain.

You might want to have a look at https://xmr.llcoins.net/addresstests.html

## woodser | 2022-07-22T00:19:17+00:00
> If the private key is known you can, however I don't think any wallet currently has the capability of restoring this information from the blockchain.

Right, this issue requests restoring the payment id from private key when the cache is deleted.

## Cactii1 | 2022-07-22T00:29:19+00:00
So it's a feature request. Can we get this tagged as a feature request then?

## selsta | 2022-07-22T11:26:18+00:00
```
13:23 <moneromooo> It can't, as it doesn't have the secret key for it.
```

# Action History
- Created by: woodser | 2022-06-05T16:07:26+00:00
- Closed at: 2022-07-22T11:26:18+00:00
