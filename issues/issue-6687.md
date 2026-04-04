---
title: Error in the deamon
source_url: https://github.com/monero-project/monero/issues/6687
author: Cideg
assignees: []
labels: []
created_at: '2020-06-24T14:00:13+00:00'
updated_at: '2020-09-02T08:43:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Does any of you know what that means ???

```
2020-06-24 12:30:20.761	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2301	SYNCHRONIZED OK
2020-06-24 13:03:47.446	[P2P8]	ERROR	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:546	Unable to send transaction(s) via Dandelion++ stem
2020-06-24 13:03:49.258	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:19.275	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:29.291	[P2P0]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:44.309	[P2P4]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:53.699	[P2P3]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:53.785	[RPC1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:54.324	[P2P9]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:04:54.392	[RPC1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-06-24 13:37:40.794	    7f2d37020700	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2127700/2127700 (100.0%) on mainnet, smart mining at 0 H/s, net hash 1.44 GH/s, v12, 0(out)+67(in) connections, uptime 0d 22h 43m 12s
2020-06-24 13:44:02.819	    7f2d37020700	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2127702, target: 2127702 (100%)
2020-06-24 13:44:02.819	    7f2d37020700	INFO	msgwriter	src/common/scoped_message_writer.h:102	Downloading at 4 kB/s
2020-06-24 13:44:02.819	    7f2d37020700	INFO	msgwriter	src/common/scoped_message_writer.h:102	60 peers
```

# Discussion History
## moneromooo-monero | 2020-06-24T16:01:51+00:00
You're mining and some transactions were not found when making a block template to mine on.
It can be ignored.


## vtnerd | 2020-08-17T19:17:17+00:00
Was this with i2p or tor enabled?

## jtgrassie | 2020-09-02T08:43:48+00:00
I have a few different daemons running behind pools and on one, this "failed to find tx meta" happens _a lot_. That one's not a pruned node or on i2p/tor. It has identical conf (other than a couple are pruned) to the other daemons that never show the error.

# Action History
- Created by: Cideg | 2020-06-24T14:00:13+00:00
