---
title: 'job: mprotect failed'
source_url: https://github.com/monero-project/monero/issues/8106
author: ubback2
assignees: []
labels: []
created_at: '2021-12-06T20:36:39+00:00'
updated_at: '2022-02-18T23:12:44+00:00'
type: issue
status: closed
closed_at: '2022-02-18T23:12:43+00:00'
---

# Original Description
src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2429872/2509015 (96%, 79143 left)
2021-12-06 15:22:00.314	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2429892/2509015 (96%, 79123 left)
2021-12-06 15:22:00.968	[P2P0]	INFO	global	src/blockchain_db/lmdb/db_lmdb.cpp:664	[batch] DB resize needed
2021-12-06 15:22:01.424	[P2P0]	INFO	global	src/blockchain_db/lmdb/db_lmdb.cpp:584	LMDB Mapsize increased.  Old: 125280MiB, New: 126304MiB
2021-12-06 15:22:01.424	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2429912/2509015 (96%, 79103 left)
2021-12-06 15:22:41.247	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2429932/2509015 (96%, 79083 left)
2021-12-06 15:22:41.981	    7f8a075fd700	ERROR	default	src/common/threadpool.cpp:170	Exception in threadpool job: mprotect failed
2021-12-06 20:17:19.190	    7f25d2da8780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-06 20:17:19.190	    7f25d2da8780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-06 20:17:19.190	    7f25d2da8780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-12-06 20:18:38.713	    7f45711d2780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-06 20:18:38.713	    7f45711d2780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-06 20:18:38.713	    7f45711d2780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-12-06 20:21:35.510	    7f3d81ea9780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-06 20:21:35.510	    7f3d81ea9780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-12-06 20:21:35.510	    7f3d81ea9780	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.3-release)

# Discussion History
## notmike-5 | 2021-12-19T19:59:54+00:00
Can you give some more background on what it is you're trying to do exactly? Is this related to Monero + Tor?

## selsta | 2022-02-18T23:12:43+00:00
Closing as there was no reply from the issue creator. Also please see https://github.com/monero-project/monero/issues/6957 for a similar issue.

# Action History
- Created by: ubback2 | 2021-12-06T20:36:39+00:00
- Closed at: 2022-02-18T23:12:43+00:00
