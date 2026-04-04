---
title: monero-wallet-rpc and tx confirmations
source_url: https://github.com/monero-project/monero/issues/3453
author: marcelo2442
assignees: []
labels: []
created_at: '2018-03-20T16:37:47+00:00'
updated_at: '2018-03-20T18:31:35+00:00'
type: issue
status: closed
closed_at: '2018-03-20T18:31:35+00:00'
---

# Original Description
Hi there, as I see it, there is no monero-wallet-rpc method that returns the confirmations of a transaction directly. How can we get or calculate them safely?

Let's say we call get_transfer_by_txid, want to make sure the transaction is still valid and calcuate the confirmations afterwards. We can check the value of "transfer.type" which is "pool" if the transaction is not included in a block yet and "in" after the transaction was included into a block. But what happens if a transaction is is affected by a reorg? Does the type change again? If yes which value does it get?


# Discussion History
## moneromooo-monero | 2018-03-20T16:48:39+00:00
It gets whatever value makes sense for its state (unless bug): pool if it's in the pool, and in if it's mined. If you're seeing differently, describe symptoms and circumstances precisely.

## marcelo2442 | 2018-03-20T17:30:37+00:00
Yes, that is what I found out. But what happens if there's a transaction that's mined and then affected by a reorg and thus no longer in the blockchain? What does get_transfer_by_txid return then? Does it return "nothing" or the same data as before with a different "transfer.type"?

## moneromooo-monero | 2018-03-20T18:06:17+00:00
If it's not in the blockchain anymore, nor in the pool, then it would turn to the failed state. If it's been mined once, it's pretty likely to be mined again though, but might not due to an input becoming invalid (it can happen when double spending for example). If it's in the pool, the state will be pool. If mined, in.

## marcelo2442 | 2018-03-20T18:31:26+00:00
I get it, thanks for the explanation. I was unsure if type "in" is a reliable value :)

# Action History
- Created by: marcelo2442 | 2018-03-20T16:37:47+00:00
- Closed at: 2018-03-20T18:31:35+00:00
