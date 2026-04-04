---
title: ' List of all transactions against wallet with payment id..'
source_url: https://github.com/monero-project/monero/issues/3781
author: zeshanvirk
assignees: []
labels:
- invalid
created_at: '2018-05-08T05:22:13+00:00'
updated_at: '2018-05-18T08:33:01+00:00'
type: issue
status: closed
closed_at: '2018-05-18T08:33:01+00:00'
---

# Original Description
I've integrated monero wallet in a web, i ran monero full node but i'm unable to get list of all transactions against my wallet address with payment_id too in responce. i'm using incoming_transfers method and passing transfers type: all to get list of all with payment id, but i receive response without payment id like this
```

"transfers": [
 { 
"amount": 1230000000000, 
"global_index": 384388, "key_image": "", 
"spent": false, "subaddr_index": 0, "tx_hash": "2bb0696950bb8039aff68cc7b4972fbc67b4bf0ef3db5a1db9c75ad3bb878ade", 
"tx_size": 160 
}
 ]
```

# Discussion History
## moneromooo-monero | 2018-05-09T08:26:18+00:00
That's because you're using the wrong RPC. Use get_transfers, not incoming_transfers. Where did you find this reference to incoming_transfers to use with type:all ?

## zeshanvirk | 2018-05-14T17:38:20+00:00
https://getmonero.org/resources/developer-guides/wallet-rpc.html here in incoming_transfers method.


## moneromooo-monero | 2018-05-15T08:41:10+00:00
Ah, yes, this is also valid, but "all" here refers to spent and unspent. I got confused.
So you want get_transfers, and set booleans to true for whatever type of tx you want: in. out, pool, pending...

## zeshanvirk | 2018-05-15T10:14:30+00:00
which transactions are pool transactions?

## cryptochangements34 | 2018-05-15T12:38:42+00:00
Pool transactions are unconfirmed transactions in the mempool

## zeshanvirk | 2018-05-15T13:21:43+00:00
then whats the difference b/w pool & pending?

## stoffu | 2018-05-15T14:31:58+00:00
Pool is incoming, pending is outgoing.

## moneromooo-monero | 2018-05-18T08:31:16+00:00
+invalid

# Action History
- Created by: zeshanvirk | 2018-05-08T05:22:13+00:00
- Closed at: 2018-05-18T08:33:01+00:00
