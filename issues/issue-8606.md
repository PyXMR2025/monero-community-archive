---
title: usage of tx-notify beside get_transfer_by_txid
source_url: https://github.com/monero-project/monero/issues/8606
author: MedGaSToN
assignees: []
labels: []
created_at: '2022-10-08T13:54:31+00:00'
updated_at: '2022-10-14T04:16:31+00:00'
type: issue
status: closed
closed_at: '2022-10-14T04:16:31+00:00'
---

# Original Description
Hello 
I run my own node and i use this on my own wallet
my problem is when trying to fetch a transaction info (pool|in|out) from my wallet using **get_transfer_by_txid** rpc method without adding the params **account_index** always the rpc call return transaction not found error. 
I know that using the params account_index will return the information but imagine looping throw 500+ account to fetch the result this cost a lot of time.
Q1 : how can i point directly the txid information without using account index?
Q2 : does tx-notify have an arg that tell the account index?
i realy take a lot of time to make it work but no success please i need help.
Thanks 

# Discussion History
## selsta | 2022-10-14T01:18:01+00:00
Maybe using different accounts isn't the best for your use case? Why not use subaddresses instead?

## MedGaSToN | 2022-10-14T01:35:54+00:00
yes i can use sub-addresses but in my case it the same logic.
I'm trying different logic to make the process more fast.
but it not possible to get the txid information without given the account index when meany account are present in the wallet ?
Thanks


## selsta | 2022-10-14T01:38:18+00:00
> yes i can use sub-addresses but in my case it the same logic.

Can you rephrase?

> I'm trying different logic to make the process more fast.

Why would it be slower with subaddresses?

## MedGaSToN | 2022-10-14T01:51:37+00:00
let say i have 5 account when a new transaction is detected (type pool or in) how can i get the txid information without knowing to witch account that txid is sent ?

# Action History
- Created by: MedGaSToN | 2022-10-08T13:54:31+00:00
- Closed at: 2022-10-14T04:16:31+00:00
