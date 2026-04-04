---
title: Monero stops before syncing
source_url: https://github.com/monero-project/monero/issues/2037
author: californiaburritos
assignees: []
labels:
- invalid
created_at: '2017-05-18T22:18:53+00:00'
updated_at: '2017-10-03T21:06:23+00:00'
type: issue
status: closed
closed_at: '2017-10-03T21:06:23+00:00'
---

# Original Description
When I try to run monerod I get this response:

017-05-18 15:12:15.454		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-18 15:12:15.455		INFO 	global	src/daemon/main.cpp:282	Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-05-18 15:12:15.455		INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-05-18 15:12:15.455		INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-05-18 15:12:15.455		INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-05-18 15:12:16.663		INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-05-18 15:12:16.664		INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-05-18 15:12:16.664		INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-05-18 15:12:16.664		INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-05-18 15:12:16.664		INFO 	global	src/daemon/core.h:73	Initializing core...
2017-05-18 15:12:16.665		INFO 	global	src/cryptonote_core/cryptonote_core.cpp:326	Loading blockchain from folder /Users/FrankHome/.bitmonero/lmdb ...
2017-05-18 15:12:16.673		WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	Failed to add output pubkey to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-05-18 15:12:16.674		ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:395	Error opening database: Failed to add output pubkey to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-05-18 15:12:16.674		INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-05-18 15:12:16.674		INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-05-18 15:12:16.674		INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-05-18 15:12:16.675		ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-05-18 15:12:16.675		INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-05-18 15:12:16.675		INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
logout
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Process completed]

I don't understand what this means but I cannot run the daemon in the GUI 2 or CLI. I've tried solutions in other issue threads but I haven't seen this response.

# Discussion History
## moneromooo-monero | 2017-05-22T07:36:18+00:00
This indicates db corruption:
 2017-05-18 15:12:16.673 WARN blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:71 Failed to add output pubkey to db transaction: MDB_KEYEXIST: Key/data pair already exists

Delete the db (in ~/.bitmonero/lmdb), and restart the daemon, making sure you're running 0.10.3.1.

## californiaburritos | 2017-05-22T23:56:53+00:00
Thank you, it appears to be synchronizing now.

## relliott2474 | 2017-07-24T19:08:17+00:00
Rod-Home-Main:local relliottmullens$ ./bin/monerod
2017-07-24 12:04:47.567		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-07-24 12:04:47.568		INFO 	global	src/daemon/main.cpp:282	Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-07-24 12:04:47.568		INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-07-24 12:04:47.568		INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-07-24 12:04:47.569		INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-07-24 12:04:47.685		INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-07-24 12:04:47.685		ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-07-24 12:04:47.685		INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-07-24 12:04:47.685		INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2017-07-24 12:04:47.685		ERROR	daemon	src/daemon/main.cpp:290	Exception in main! Failed to initialize p2p server.

seems I have a new core Error. This is new was working earlier. Any thoughts?????


## moneromooo-monero | 2017-07-25T22:52:40+00:00
There's no useful info on that log, run with --log-level 1

## moneromooo-monero | 2017-08-08T10:27:42+00:00
That last one looks like a bind error though. This was hidden in the default logs recently, and would cause a silent exit on start like this.

## moneromooo-monero | 2017-10-03T21:01:50+00:00
Original error was a corrupt db, the other one looks like there was another daemon running.

+invalid

# Action History
- Created by: californiaburritos | 2017-05-18T22:18:53+00:00
- Closed at: 2017-10-03T21:06:23+00:00
