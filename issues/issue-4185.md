---
title: running ./monerod issue
source_url: https://github.com/monero-project/monero/issues/4185
author: madman-genchie
assignees: []
labels: []
created_at: '2018-07-28T14:27:20+00:00'
updated_at: '2018-08-15T11:25:01+00:00'
type: issue
status: closed
closed_at: '2018-08-15T11:25:01+00:00'
---

# Original Description
running ~/monero/build/release/bin# ./monerod

this is what i get !!!!!
2018-07-28 14:23:37.487	    7efc76670bc0	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-e2c39f6)
2018-07-28 14:23:37.487	    7efc76670bc0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-07-28 14:23:37.487	    7efc76670bc0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-07-28 14:23:37.487	    7efc76670bc0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-07-28 14:23:42.151	    7efc76670bc0	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-07-28 14:23:42.151	    7efc76670bc0	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-07-28 14:23:42.151	    7efc76670bc0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-07-28 14:23:42.152	    7efc76670bc0	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-07-28 14:23:42.152	    7efc76670bc0	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-07-28 14:23:42.152	    7efc76670bc0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /root/.bitmonero/lmdb ...
2018-07-28 14:23:43.074	    7efc76670bc0	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Error attempting to retrieve a hard fork version at height 1601485 from the db: MDB_NOTFOUND: No matching key/data pair found
2018-07-28 14:23:43.078	    7efc76670bc0	FATAL	daemon	src/daemon/daemon.cpp:194	Uncaught exception! Error attempting to retrieve a hard fork version at height 1601485 from the db: MDB_NOTFOUND: No matching key/data pair found
2018-07-28 14:23:43.078	    7efc76670bc0	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-07-28 14:23:43.078	    7efc76670bc0	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-07-28 14:23:47.083	    7efc76670bc0	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-07-28 14:23:47.166	    7efc76670bc0	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-07-28 14:23:47.166	    7efc76670bc0	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully

Highly frustrating please help

# Discussion History
## moneromooo-monero | 2018-07-28T15:27:16+00:00
Looks corrupted. Try with --db-salvage, and if it doesn't help, remove blockchain.

## madman-genchie | 2018-07-28T16:05:52+00:00
i tried --db-salvage with no luck so i deleted the ./bitmonero and restarted it, it is now syncing the blockchain hopefully this has working will keep this thread updated



## MicahZoltu | 2018-08-14T18:34:42+00:00
Hmm, actually I think I have a different issue, will create a new one.

## madman-genchie | 2018-08-15T06:52:16+00:00
I deleted the .blockchain/dB dir then re synced successfully 

## moneromooo-monero | 2018-08-15T11:10:52+00:00
Fixed in 740da1b

+resolved

# Action History
- Created by: madman-genchie | 2018-07-28T14:27:20+00:00
- Closed at: 2018-08-15T11:25:01+00:00
