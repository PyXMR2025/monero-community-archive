---
title: running two monerod
source_url: https://github.com/monero-project/monero/issues/4910
author: AndrVdov
assignees: []
labels:
- invalid
created_at: '2018-11-27T15:24:18+00:00'
updated_at: '2018-11-27T16:17:18+00:00'
type: issue
status: closed
closed_at: '2018-11-27T16:17:18+00:00'
---

# Original Description
Now there is a working monerod.
It is necessary to run another one, but with a block chain from another directory.
run:
./monerod --data-dir /home/user/MoneroBlockchain --p2p-bind-port 18500 --rpc-bind-port 18550

get err:
**Error creating ZMQ Socket: Address already in use
Failed to add TCP Socket (127.0.0.1:18082) to ZMQ RPC Server**

How start two demons so that they do not interfere with each other?

# Discussion History
## moneromooo-monero | 2018-11-27T15:55:59+00:00
This is not a bug. It is telling you the zmq port is already used. Did you try to tell it to use another one ?
--help shows:
--zmq-rpc-bind-port arg (=18082, 28082 if 'testnet', 38082 if 'stagenet')


## AndrVdov | 2018-11-27T16:05:07+00:00
it helped, thanks

## moneromooo-monero | 2018-11-27T16:11:11+00:00
+invalid

# Action History
- Created by: AndrVdov | 2018-11-27T15:24:18+00:00
- Closed at: 2018-11-27T16:17:18+00:00
