---
title: failed to start monerod.exe
source_url: https://github.com/monero-project/monero-gui/issues/1196
author: coolhty
assignees: []
labels:
- resolved
created_at: '2018-03-24T04:13:57+00:00'
updated_at: '2018-07-04T10:27:29+00:00'
type: issue
status: closed
closed_at: '2018-07-04T10:27:29+00:00'
---

# Original Description
2018-03-24 04:09:38.878	4808	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-03-24 04:09:38.878	4808	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-03-24 04:09:38.878	4808	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2018-03-24 04:09:38.878	4808	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2018-03-24 04:09:38.878	4808	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-03-24 04:09:43.554	4808	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2018-03-24 04:09:43.555	4808	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2018-03-24 04:09:43.555	4808	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2018-03-24 04:09:43.555	4808	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2018-03-24 04:09:43.555	4808	INFO 	global	src/daemon/core.h:73	Initializing core...
2018-03-24 04:09:43.555	4808	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder D:\blockchains\monero\lmdb ...
2018-03-24 04:09:43.555	4808	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2018-03-24 04:09:43.555	4808	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 6758MiB, New: 7782MiB
2018-03-24 04:09:43.555	4808	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-03-24 04:09:43.571	4808	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:399	Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-03-24 04:09:43.572	4808	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2018-03-24 04:09:43.573	4808	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-03-24 04:09:43.595	4808	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2018-03-24 04:09:43.597	4808	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2018-03-24 04:09:43.598	4808	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2018-03-24 04:09:43.598	4808	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully

# Discussion History
## dEBRUYNE-1 | 2018-03-25T14:38:01+00:00
Is this the first time you're starting `monerod.exe`?

## dEBRUYNE-1 | 2018-07-04T08:31:12+00:00
Given the inactivity of this issue, I am going to close it.

+resolved

## dEBRUYNE-1 | 2018-07-04T08:37:44+00:00
+resolved

# Action History
- Created by: coolhty | 2018-03-24T04:13:57+00:00
- Closed at: 2018-07-04T10:27:29+00:00
