---
title: Daemon not starting after PC crash - FATAL
source_url: https://github.com/monero-project/monero/issues/3162
author: zexanana
assignees: []
labels: []
created_at: '2018-01-20T16:02:29+00:00'
updated_at: '2019-08-19T18:29:22+00:00'
type: issue
status: closed
closed_at: '2019-08-19T18:29:22+00:00'
---

# Original Description
Hello.
After a crash in my computer I cannot get daemon to start syncing again. After 2 seconds of initializing, it just crashes. The bitmonero.log from when it was running smoothly (and then PC crashed) until a few days later when I tried running it again, is posted below. There is a WARN entry followed by a FATAL entry:
```
2018-01-20 15:30:27.909	3016	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Failed to find txpool tx blob to match metadata
2018-01-20 15:30:27.911	3016	FATAL	daemon	src/daemon/daemon.cpp:150	Uncaught exception! Failed to find txpool tx blob to match metadata
```

bitmonero.log
```
2018-01-17 01:43:23.119 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  Height: 1488812, target: 1488812 (100%)
2018-01-17 01:43:23.120 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  Downloading at 14 kB/s
2018-01-17 01:43:23.121 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  11 peers
2018-01-17 01:43:23.122 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  134.228.12.2:60762        983a4732cd6de65c  1488802  0 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.123 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  51.15.208.97:51786        36c52ccbdbba4669  1488812  3 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.124 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  82.102.20.169:62673       ceb4d36c63fa2ac8  62313  0 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.125 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  94.55.32.92:60486         39d0c60bf0e9fa38  1466777  3 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.126 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  88.99.138.74:63218        a518c71d14a801f7  1488812  3 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.127 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  54.173.52.1:18080         7175f3bf83b46185  1488812  0 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.130 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  70.127.143.231:18080      69ad3a07724be807  1488812  0 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.131 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  172.248.65.15:18080       29045dc6a9f95d2c  1488812  3 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.132 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  213.152.161.219:60023     7618b0cc5756243a  1488812  0 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.133 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  68.42.67.72:18080         e0b2de7ff92fe9d4  1488812  2 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.134 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  153.228.190.230:18080     fd354709266808d1  1488812  0 kB/s, 0 blocks / 0 MB queued
2018-01-17 01:43:23.135 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  0 spans, 0 MB
2018-01-17 01:48:13.170 7596    INFO    msgwriter   src/common/scoped_message_writer.h:102  No update available
2018-01-17 02:26:39.879 8048    INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-17 02:26:39.879 8048    INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.1.0-release)
2018-01-17 02:26:39.879 8048    INFO    global  src/daemon/protocol.h:55    Initializing cryptonote protocol...
2018-01-17 02:26:39.879 8048    INFO    global  src/daemon/protocol.h:60    Cryptonote protocol initialized OK
2018-01-17 02:26:39.879 8048    INFO    global  src/daemon/p2p.h:63 Initializing p2p server...
2018-01-17 02:26:42.152 8048    INFO    global  src/daemon/p2p.h:68 P2p server initialized OK
2018-01-17 02:26:42.152 8048    INFO    global  src/daemon/rpc.h:58 Initializing core rpc server...
2018-01-17 02:26:42.152 8048    INFO    global  contrib/epee/include/net/http_server_impl_base.h:70 Binding on 127.0.0.1:18081
2018-01-17 02:26:42.168 8048    INFO    global  src/daemon/rpc.h:63 Core rpc server initialized OK on port: 18081
2018-01-17 02:26:42.168 8048    INFO    global  src/daemon/core.h:73    Initializing core...
2018-01-17 02:26:42.168 8048    INFO    global  src/cryptonote_core/cryptonote_core.cpp:323 Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-01-17 02:26:43.262 8048    INFO    global  src/cryptonote_core/cryptonote_core.cpp:421 Loading checkpoints
2018-01-17 02:26:43.433 8048    INFO    global  src/daemon/core.h:78    Core initialized OK
2018-01-17 02:26:43.433 8048    INFO    global  src/daemon/rpc.h:68 Starting core rpc server...
2018-01-17 02:26:43.433 [SRV_MAIN]  INFO    global  src/daemon/rpc.h:73 Core rpc server started ok
2018-01-17 02:26:43.433 [SRV_MAIN]  INFO    global  src/daemon/p2p.h:78 Starting p2p net loop...
2018-01-17 02:26:44.434 [P2P7]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1258    [1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.
 
You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)
 
Use the "help" command to see the list of available commands.
**********************************************************************
[0m
2018-01-17 02:26:44.684 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305 [90.66.140.71:36190 INC] Sync data returned a new top block candidate: 1488835 -> 1488838 [Your node is 3 blocks (0 days) behind]
SYNCHRONIZATION started
2018-01-17 02:26:45.231 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    [1;33m[90.66.140.71:36190 INC]  Synced 1488838/1488838[0m
2018-01-17 02:26:45.231 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    [1;32mSYNCHRONIZED OK[0m
2018-01-17 02:26:45.231 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1543    [1;33m
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.
 
Use the "help" command to see the list of available commands.
**********************************************************************[0m
2018-01-20 15:06:38.786 8752    INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-20 15:06:38.789 8752    INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.1.0-release)
2018-01-20 15:06:38.790 8752    INFO    global  src/daemon/protocol.h:55    Initializing cryptonote protocol...
2018-01-20 15:06:38.790 8752    INFO    global  src/daemon/protocol.h:60    Cryptonote protocol initialized OK
2018-01-20 15:06:38.793 8752    INFO    global  src/daemon/p2p.h:63 Initializing p2p server...
2018-01-20 15:06:40.914 8752    INFO    global  src/daemon/p2p.h:68 P2p server initialized OK
2018-01-20 15:06:40.916 8752    INFO    global  src/daemon/rpc.h:58 Initializing core rpc server...
2018-01-20 15:06:40.920 8752    INFO    global  contrib/epee/include/net/http_server_impl_base.h:70 Binding on 127.0.0.1:18081
2018-01-20 15:06:40.921 8752    INFO    global  src/daemon/rpc.h:63 Core rpc server initialized OK on port: 18081
2018-01-20 15:06:40.922 8752    INFO    global  src/daemon/core.h:73    Initializing core...
2018-01-20 15:06:40.926 8752    INFO    global  src/cryptonote_core/cryptonote_core.cpp:323 Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-01-20 15:06:43.158 8752    WARN    blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to find txpool tx blob to match metadata
2018-01-20 15:06:43.161 8752    FATAL   daemon  src/daemon/daemon.cpp:150   Uncaught exception! Failed to find txpool tx blob to match metadata
2018-01-20 15:06:43.161 8752    INFO    global  src/daemon/rpc.h:90 Deinitializing rpc server...
2018-01-20 15:06:43.162 8752    INFO    global  src/daemon/p2p.h:90 Deinitializing p2p...
2018-01-20 15:06:43.210 8752    INFO    global  src/daemon/core.h:89    Deinitializing core...
2018-01-20 15:06:44.002 8752    INFO    global  src/daemon/protocol.h:77    Stopping cryptonote protocol...
2018-01-20 15:06:44.002 8752    INFO    global  src/daemon/protocol.h:81    Cryptonote protocol stopped successfully

```

I tried running daemon with "--db-salvage" but problem persisted. I suppose lmdb is corrupted but maybe it would be possible to create a function to delete the last x entries in the DB and then try resyncing to see if the corruption was in the newer entries. I have a DB backup so this is not a huge problem for me but I saw other people in reddit with the same problem.

I also tried running mdb_stat but I couldn't figure out how to build it (I just downloaded GUI, didnt build from source). The problem is, even though I got Codeblocks and Mingw installed, I don't know where Mingw make.exe is. I just can't find it.

# Discussion History
## moneromooo-monero | 2018-01-20T17:01:41+00:00
LMDB would need a concept of checkpoints (further than the last two txns).
For this particular error, a recent monerod might help. Failing that, you can drop txpool_blob and txpool_meta, though there might be corruption elsewhere too.

## leonklingele | 2018-01-20T17:08:03+00:00
Would `--db-sync-mode safe` have helped in this particular case?

## zexanana | 2018-01-20T18:23:00+00:00
I tried redownloading monerod, the problem persisted. Using `--db-sync-mode safe` didn't help in my case also. I don't know how to go about "dropping txpool_blob and txpool_meta".
I am resyncing the blockchain from my backup startup point. If the checkpoints idea is simple, it may be worth implementation or a little testing as I see some people with these kinds of errors.

## moneromooo-monero | 2018-01-20T18:55:20+00:00
Safe mode should have helped. Maybe we have a db txn bug.
To drop those tables: mdb_drop -s txpool_blob ~/.bitmonero/lmdb (and same for txpool_meta).

## moneromooo-monero | 2018-08-15T11:44:42+00:00
Re-reading the comment above, it looks like "--db-sync-mode safe" was used on the bad db, in which case it's expected it won't fix anything.
In any case, #3884 fixed safe mode not being used after sync, which should fix a good number of those issues.

# Action History
- Created by: zexanana | 2018-01-20T16:02:29+00:00
- Closed at: 2019-08-19T18:29:22+00:00
