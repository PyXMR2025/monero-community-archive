---
title: 'monero-wallet-rpc is not stable providing rpc feature '
source_url: https://github.com/monero-project/monero/issues/2401
author: martinpeterbauer
assignees: []
labels:
- invalid
created_at: '2017-09-05T09:30:27+00:00'
updated_at: '2018-01-08T13:40:33+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:40:33+00:00'
---

# Original Description
(Environment: ubuntu 16, 64Bit, latest official downloadable version of monero)

i am tring to use the monero-wallet-rpc by doing calls from my own (java) client. The deamon is currently running and is updating/syncing the blockchain.

If i start the monero-wallet-rpc the program will 'provide' the rpc-feature only 2 times out of 10 times of trying. It rpc connect directly to the daemon work always like a charm - but not to the wallet rpc.

What to do if i need a stable 'rpc feature' of the wallet functions? Is this issue known? Is there any workaround? Happens this because the wallet-rpc tries to reconnect to the deamon which is busy while syncing? Will it work after the deamon is fully synced?

Please help. Using this rpc without stability makes no sense in my environment.


# Discussion History
## moneromooo-monero | 2017-09-06T10:38:31+00:00
Blockchain sync takes the blockchain lock for a long time, and you get timeouts. Wait till sync's finished before doing any RPC. 

## dEBRUYNE-1 | 2018-01-08T13:11:34+00:00
+invalid

# Action History
- Created by: martinpeterbauer | 2017-09-05T09:30:27+00:00
- Closed at: 2018-01-08T13:40:33+00:00
