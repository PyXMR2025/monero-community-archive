---
title: monero-wallet-rpc callback subscription
source_url: https://github.com/monero-project/monero/issues/4284
author: Revinand
assignees: []
labels: []
created_at: '2018-08-20T11:08:15+00:00'
updated_at: '2018-08-20T12:46:15+00:00'
type: issue
status: closed
closed_at: '2018-08-20T12:46:15+00:00'
---

# Original Description
Hello, I found that some callback is called on a payment received or a new block in the wallet

https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1416
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1717

but I can't find how to subscribe to these notifications. Is it possible somehow? And if yes, how can I do this?

# Discussion History
## moneromooo-monero | 2018-08-20T11:39:53+00:00
You override those functions on your derived class, like simplewallet does.


## Revinand | 2018-08-20T12:08:15+00:00
so, to listen for a wallet events in a node.js app I should use https://github.com/exantech/monero-nodejs-libwallet for example? There is no zeromq implementation or some kind of bitcoin `walletnotify` option out of the box, right?

## moneromooo-monero | 2018-08-20T12:21:05+00:00
There are no external notifications.
I believe vtnerd is planning on doing this in the near future though, using 0MQ.
Ask him in #monero-dev on Freenode if you want details.

## Revinand | 2018-08-20T12:46:15+00:00
ok, I got it. Thank you for the info

# Action History
- Created by: Revinand | 2018-08-20T11:08:15+00:00
- Closed at: 2018-08-20T12:46:15+00:00
