---
title: monerod can't restart after power down
source_url: https://github.com/monero-project/monero/issues/3874
author: AlexVN74
assignees: []
labels: []
created_at: '2018-05-28T10:04:33+00:00'
updated_at: '2022-03-16T15:44:33+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:44:33+00:00'
---

# Original Description
I'm using monerod in docker container for several weeks, but after unexpected power down it can't start again without any errors in log.
Here is log with default log level: 
```docker run -it --rm --name monero -v /hdd/monero:/root/.bitmonero -p 18080:18080 -p 18081:18081 monero
+ NICE=nice -n 19
+ MONEROD=monerod  --rpc-bind-ip=0.0.0.0 --confirm-external-bind
+ [[  = - ]]
+ [[ -z ]]
+ set -- nice -n 19 monerod --rpc-bind-ip=0.0.0.0 --confirm-external-bind
+ exec nice -n 19 monerod --rpc-bind-ip=0.0.0.0 --confirm-external-bind
2018-05-28 10:01:58.954	    7f9728e37bc0	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-28 10:01:58.954	    7f9728e37bc0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-05-28 10:01:58.954	    7f9728e37bc0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-05-28 10:01:58.955	    7f9728e37bc0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-05-28 10:02:04.748	    7f9728e37bc0	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-05-28 10:02:04.749	    7f9728e37bc0	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-05-28 10:02:04.749	    7f9728e37bc0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 0.0.0.0:18081
2018-05-28 10:02:04.750	    7f9728e37bc0	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-05-28 10:02:04.750	    7f9728e37bc0	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-05-28 10:02:04.750	    7f9728e37bc0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /root/.bitmonero/lmdb ...
```
and last lines with log level 4:
```2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1868	BlockchainLMDB::get_block_size
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1868	BlockchainLMDB::get_block_size
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1868	BlockchainLMDB::get_block_size
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1868	BlockchainLMDB::get_block_size
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1868	BlockchainLMDB::get_block_size
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2874	BlockchainLMDB::block_txn_stop
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1683	BlockchainLMDB::for_all_txpool_txes
2018-05-28 09:24:33.829	    7fefc4ddfbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2820	BlockchainLMDB::block_rtxn_start
```

# Discussion History
## moneromooo-monero | 2018-05-28T10:06:59+00:00
Probably a DB corruption.
It *might* work with --db-salvage
The actual error isn't shown on that log fwiw.


## AlexVN74 | 2018-05-28T10:12:01+00:00
--db-salvage doesn't help :(
How can I get the reason of monerod stopped work?

## moneromooo-monero | 2018-05-28T10:29:40+00:00
The reason is most likely a corrupted DB.
What filesystem and OS variant are you using ?
Monero is now supposed to switch to a "safe" mode once the initial blockchain is synced. I guess this did not work :/


## AlexVN74 | 2018-05-28T10:45:33+00:00
I'm using docker image builded from official Dockerfile. Host server running on Ubuntu 16.04.4 LTS, file system for blockchain DB is ext4.

## moneromooo-monero | 2018-05-28T11:20:01+00:00
That might be the reason: https://github.com/monero-project/monero/pull/3876
It looks like safe mode was not being set.

## AlexVN74 | 2018-05-29T09:14:31+00:00
Is it possible to repair database? 
Or I have to start new node with empty DB?

## moneromooo-monero | 2018-05-29T11:30:30+00:00
If --db-salvage did not work, I don't think you can recover it without expert lmdb knowledge.

## AlexVN74 | 2018-05-29T19:53:51+00:00
Ok, thx. Will start from empty blockchain.
But it's strange that log has completely no information why monerod stoped working.
 Last lines with --log-level 4:
```
2018-05-29 19:48:08.443	    7f55ab68bbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2874	BlockchainLMDB::block_txn_stop
2018-05-29 19:48:08.443	    7f55ab68bbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1683	BlockchainLMDB::for_all_txpool_txes
2018-05-29 19:48:08.444	    7f55ab68bbc0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2820	BlockchainLMDB::block_rtxn_start
```
and no errors in log

## moneromooo-monero | 2018-05-29T22:30:19+00:00
Yes, that is odd. Are you sure it's the end of the log ? The logs rotate, so it might be the end of that particular file only.

## AlexVN74 | 2018-05-30T06:54:16+00:00
Yes, I'm sure it's the end of log. 
It seems monerod stoped when init mempool in line 512 of cryptonote_core.cpp: 
r = m_mempool.init(max_txpool_size);

## selsta | 2022-03-16T15:44:33+00:00
Closing due to inactivity and this looking like simple blockchain corruption.

# Action History
- Created by: AlexVN74 | 2018-05-28T10:04:33+00:00
- Closed at: 2022-03-16T15:44:33+00:00
