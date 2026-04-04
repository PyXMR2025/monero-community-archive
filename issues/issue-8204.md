---
title: How to simulate a TXID for multiple UTXO transaction
source_url: https://github.com/monero-project/monero/issues/8204
author: EWIT521
assignees: []
labels: []
created_at: '2022-03-04T07:47:07+00:00'
updated_at: '2022-03-16T08:07:42+00:00'
type: issue
status: closed
closed_at: '2022-03-16T08:07:42+00:00'
---

# Original Description
How to simulate a TXID for multiple UTXO transaction，Thank you very much

# Discussion History
## selsta | 2022-03-08T04:28:47+00:00
Can you explain in more detail what you want to do?

## EWIT521 | 2022-03-16T07:21:52+00:00
Account A  has   2 xmr
Account B  has   3 xmr
two UTXOs under different accounts 
want to spent In a transfer transaction

## selsta | 2022-03-16T07:23:19+00:00
You will have to do two separate transactions.

## EWIT521 | 2022-03-16T07:26:18+00:00
The wallet is under account 0 by default, I can't see another UTXO, do I have to change the account?


## selsta | 2022-03-16T07:27:38+00:00
Yes, see `help account`.

Also you can use subaddressses instead of accounts so that you can spend them in a single transaction. See `help address`.

## EWIT521 | 2022-03-16T07:30:23+00:00
Thank you very much

# Action History
- Created by: EWIT521 | 2022-03-04T07:47:07+00:00
- Closed at: 2022-03-16T08:07:42+00:00
