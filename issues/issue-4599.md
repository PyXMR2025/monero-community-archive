---
title: DB conversion error
source_url: https://github.com/monero-project/monero/issues/4599
author: netxecute
assignees: []
labels: []
created_at: '2018-10-15T16:08:39+00:00'
updated_at: '2024-07-31T23:24:50+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:24:50+00:00'
---

# Original Description
My db was converting - it was about halfway (2630000) and then when I came home the cmd prompt window was gone. Tried starting again and get this error when it gets to the DB conversion



2018-10-12 03:47:15.525 5504 ERROR blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:4232 Output found claiming height >= blockchain height

2018-10-12 03:47:15.525 5504 WARN blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:75 Failed to build rct output distribution

2018-10-12 03:47:15.525 5504 ERROR cn src/cryptonote_core/cryptonote_core.cpp:548 Error opening database: Failed to build rct output distribution

# Discussion History
## moneromooo-monero | 2018-10-15T16:11:52+00:00
Are there interesting things from when it crashed in the log ? An exception maybe ?

## netxecute | 2018-10-15T16:22:58+00:00
Here's the log from that day.

2018-10-11 15:53:16.458	3620	INFO 	logging	contrib/epee/src/mlog.cpp:242	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 15:53:16.494	3620	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-11 15:53:16.512	3620	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-11 15:53:16.512	3620	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-11 15:53:16.546	3620	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-11 15:53:19.455	3620	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-10-11 15:53:19.714	3620	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-10-11 15:53:19.783	3620	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-10-11 15:53:19.795	3620	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-10-11 15:53:19.795	3620	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-10-11 15:53:19.831	3620	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder E:\Blockchain\XMR\lmdb ...
2018-10-11 15:53:20.421	3620	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:4071	[1;33mMigrating blockchain from DB version 1 to 2 - this may take a while:[0m
2018-10-11 22:13:44.228	3620	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:4213	[1;33mMigrating blockchain from DB version 2 to 3 - this may take a while:[0m
2018-10-11 22:52:01.662	3620	ERROR	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:4232	Output found claiming height >= blockchain height
2018-10-11 22:52:01.694	3620	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to build rct output distribution
2018-10-11 22:52:01.772	3620	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:548	Error opening database: Failed to build rct output distribution
2018-10-11 22:52:03.944	3620	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-10-11 22:52:04.522	3620	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-10-11 22:52:05.959	3620	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-10-11 22:52:05.991	3620	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-10-11 22:52:05.991	3620	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-10-11 22:52:05.991	3620	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-10-12 03:12:17.231	5504	INFO 	logging	contrib/epee/src/mlog.cpp:242	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-12 03:12:17.262	5504	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-12 03:12:17.262	5504	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-12 03:12:17.262	5504	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-12 03:12:17.262	5504	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-12 03:12:20.246	5504	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-10-12 03:12:20.246	5504	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-10-12 03:12:20.246	5504	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-10-12 03:12:20.246	5504	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-10-12 03:12:20.246	5504	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-10-12 03:12:20.246	5504	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder E:\Blockchain\XMR\lmdb ...
2018-10-12 03:12:20.340	5504	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:4213	[1;33mMigrating blockchain from DB version 2 to 3 - this may take a while:[0m
2018-10-12 03:47:15.525	5504	ERROR	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:4232	Output found claiming height >= blockchain height
2018-10-12 03:47:15.525	5504	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to build rct output distribution
2018-10-12 03:47:15.525	5504	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:548	Error opening database: Failed to build rct output distribution
2018-10-12 03:47:16.478	5504	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-10-12 03:47:16.478	5504	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-10-12 03:47:17.588	5504	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-10-12 03:47:17.588	5504	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-10-12 03:47:17.588	5504	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-10-12 03:47:17.588	5504	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully

## moneromooo-monero | 2018-10-15T16:23:44+00:00
Also, please log with the height and blockchain height just before that line (db_lmdb.cpp:4232):
MGINFO("height " << height << ", bc height " << blockchain_height);

## netxecute | 2018-10-15T16:39:44+00:00
Sorry not sure I follow - you want a different part of the log or is this some action you want me to take?

## moneromooo-monero | 2018-10-15T17:46:42+00:00
Add that line before the error (db_lmdb.cpp:4232), compile, run, post those logs again.

## netxecute | 2018-10-15T17:57:23+00:00
? I didn't compile
This is just the win 64bit binary cli trying to upgrade the blockchain db

## moneromooo-monero | 2018-10-15T18:15:25+00:00
I'm not saying you compiled it, I'm saying compile it now with that patch :)
If you can't/won't compile it now, then fair enough, but I can't help further.

## netxecute | 2018-10-15T18:47:20+00:00
Ah, I see.  No sorry can't compile this.  Could you expand on the error a bit?

Do I need to re-sync the blockchain from scratch?  Is it an issue with the CLI or with the db?

thanks

## moneromooo-monero | 2018-10-15T19:35:57+00:00
I don't know yet.

## trasherdk | 2018-10-16T05:22:58+00:00
I've got, not exactly an error, but extremely slow DB conversion 25 hours, using 14 of 16 GB RAM.
Windows 8.1 x64 16 GB RAM, 1 TB HDD.


	Monero 'Beryllium Bullet' (v0.13.0.2-release)
	2018-10-13 01:55:00.557 1780   INFO global  src/blockchain_db/lmdb/db_lmdb.cpp:4071 Migrating blockchain from DB version 1 to 2 - this may take a while:
	2018-10-14 02:05:55.318 1780   INFO global  src/blockchain_db/lmdb/db_lmdb.cpp:4213 Migrating blockchain from DB version 2 to 3 - this may take a while:
	2018-10-14 03:17:00.524 1780   INFO global  src/cryptonote_core/cryptonote_core.cpp:585  Loading checkpoints
	2018-10-14 03:17:02.799 1780   INFO global  src/daemon/core.h:92    Core initialized OK
	2018-10-14 03:27:25.400 [P2P7] INFO global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182 [x.x.x.x:18080 OUT]  Synced 1682456/1682456


## selsta | 2024-07-31T23:24:50+00:00
Closing due to lack of reports by others users and age of the issue.

# Action History
- Created by: netxecute | 2018-10-15T16:08:39+00:00
- Closed at: 2024-07-31T23:24:50+00:00
