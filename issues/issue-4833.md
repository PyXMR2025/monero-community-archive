---
title: Failed to parse transaction from blob
source_url: https://github.com/monero-project/monero/issues/4833
author: alextrezvy
assignees: []
labels: []
created_at: '2018-11-09T17:23:40+00:00'
updated_at: '2025-03-16T08:24:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The same issue as [#4649](https://github.com/monero-project/monero/issues/4649), but on version 0.13.0.4 (Ubuntu, 64bit), which seems to be fixed. Is there a way to avoid of downloading of 60+GB DB?

# Discussion History
## moneromooo-monero | 2018-11-09T17:43:16+00:00
Bump logs  (--log-level 2), see if you can see where it errors out.
If you can't tell from the logs, add the following patch, which will dump the stack trace and the faulty transaction data in the logs:

<pre>
diff --git a/src/cryptonote_basic/cryptonote_format_utils.cpp b/src/cryptonote_basic/cryptonote_format_utils.cpp
index a51c2496b..04d90dc86 100644
--- a/src/cryptonote_basic/cryptonote_format_utils.cpp
+++ b/src/cryptonote_basic/cryptonote_format_utils.cpp
@@ -41,6 +41,7 @@ using namespace epee;
 #include "crypto/crypto.h"
 #include "crypto/hash.h"
 #include "ringct/rctSigs.h"
+#include "common/stack_trace.h"
 
 #undef MONERO_DEFAULT_LOG_CATEGORY
 #define MONERO_DEFAULT_LOG_CATEGORY "cn"
@@ -182,6 +183,11 @@ namespace cryptonote
     ss << tx_blob;
     binary_archive<false> ba(ss);
     bool r = ::serialization::serialize(ba, tx);
+if (!r)
+{
+  MGINFO("Failed to parse tx from blob: " << epee::string_tools::buff_to_hex_nodelimer(tx_blob));
+  tools::log_stack_trace("");
+}
     CHECK_AND_ASSERT_MES(r, false, "Failed to parse transaction from blob");
     CHECK_AND_ASSERT_MES(expand_transaction_1(tx, false), false, "Failed to expand transaction data");
     tx.invalidate_hashes();
@@ -194,6 +200,11 @@ namespace cryptonote
     ss << tx_blob;
     binary_archive<false> ba(ss);
     bool r = tx.serialize_base(ba);
+if (!r)
+{
+  MGINFO("Failed to parse tx base from blob: " << epee::string_tools::buff_to_hex_nodelimer(tx_blob));
+  tools::log_stack_trace("");
+}
     CHECK_AND_ASSERT_MES(r, false, "Failed to parse transaction from blob");
     CHECK_AND_ASSERT_MES(expand_transaction_1(tx, true), false, "Failed to expand transaction data");
     tx.invalidate_hashes();
</pre>


## alextrezvy | 2018-11-09T18:50:10+00:00
2018-11-09 18:46:45.795	    7f4005796780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:4072	updating txs_pruned and txs_prunable tables...
2018-11-09 18:46:45.795	    7f4005796780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:4100	updating txs tables:
2018-11-09 18:46:46.024	    7f4005796780	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:185	Failed to parse transaction from blob
2018-11-09 18:46:46.024	    7f4005796780	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to parse tx from blob retrieved from the db

## moneromooo-monero | 2018-11-09T18:52:24+00:00
OK that does look like corrupt db.

## alextrezvy | 2018-11-09T19:39:05+00:00
What the reason made it corrupt? Previously it worked OK with 0.12.3.0. Hard disk has no errors.

## iDunk5400 | 2018-11-09T21:18:44+00:00
Maybe you kept using v0.12.3.0 past block 1685554.

## alextrezvy | 2018-11-10T08:33:57+00:00
> Maybe you kept using v0.12.3.0 past block 1685554.

Maybe but how do I know when I must turn off the daemon? I'm not reading announcements 24/7.
I suppose the software must stop running by itself before it makes a damage to the user's data.
Now there is the case where I can't make a transaction before sync is finished. It might take a day or two. Is that a good motivation to run a node?

## moneromooo-monero | 2019-01-16T20:32:27+00:00
Thankfully, there is a release at most a few days before the fork, so just looking every couple days should be enough. If you still fail to update and end up on the wrong chain, the current code will automatically get rid of the bad blocks once you update, and should then find the correct chain again.


## Retia-Adolf | 2019-01-16T21:12:34+00:00
That sounds good. I have similar problem, it seems be caused by previous one error occurred in last year, now using current release `v0.13.0.4-release` but still can't resolve. Any idea? Thanks very much


```

**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************[0m
2018-07-01 05:51:42.241	[P2P4]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-07-01 05:51:42.459	[P2P4]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 66436MiB, New: 67460MiB
2018-07-01 05:51:42.459	[P2P4]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-07-01 05:51:42.459	[P2P4]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 67460MiB, New: 68484MiB
2018-07-01 06:55:35.430	[P2P7]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-01 06:55:39.623	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[83.43.150.180:18080 OUT] Sync data returned a new top block candidate: 1606930 -> 1606932 [Your node is 2 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-07-01 06:55:40.661	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 07:58:38.277	[P2P1]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-01 07:58:52.512	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[208.102.3.17:18080 OUT] Sync data returned a new top block candidate: 1606968 -> 1606969 [Your node is 1 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-07-01 07:58:54.786	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[208.102.3.17:18080 OUT]  Synced 1606969/1606969[0m
2018-07-01 07:58:54.787	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 08:39:26.197	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 09:01:03.524	[P2P3]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-01 09:01:10.589	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[158.69.25.71:18080 OUT] Sync data returned a new top block candidate: 1607005 -> 1607006 [Your node is 1 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-07-01 09:01:13.756	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[159.69.35.201:18080 OUT]  Synced 1607006/1607006[0m
2018-07-01 09:01:13.756	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 09:01:13.954	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 10:05:57.564	[P2P3]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-01 11:08:40.590	[P2P6]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-01 11:08:43.755	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[95.84.156.154:18080 OUT] Sync data returned a new top block candidate: 1607085 -> 1607086 [Your node is 1 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-07-01 11:08:47.081	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[81.107.114.253:18080 OUT]  Synced 1607086/1607086[0m
2018-07-01 11:08:47.081	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 11:08:59.230	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	[1;32mSYNCHRONIZED OK[0m
2018-07-01 12:14:07.420	[P2P0]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-01 12:22:02.697	[P2P3]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1599986
id:	<7e79c99dd378cd2e7830170a6b0928234f0a0f2b704599f5216ee6c29888efdf>
PoW:	<0d386fa4c7a4907d2166f9caa1d27eaaf3a5862fd655332fec930b0000000000>
difficulty:	47575247869[0m
2018-07-01 13:20:45.031	[P2P2]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
```
```
2018-07-01 13:34:30.606	11568	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-07-01 13:34:30.628	11568	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-07-01 13:34:30.629	11568	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-07-01 13:34:30.629	11568	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-07-01 13:34:30.631	11568	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-07-01 13:34:51.769	11568	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-07-01 13:34:52.071	11568	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-07-01 13:34:52.072	11568	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-07-01 13:34:52.072	11568	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-07-01 13:34:52.072	11568	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-07-01 13:34:52.075	11568	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder E:\Blockchain\Monero\lmdb ...
2018-07-01 13:34:52.811	11568	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2018-07-01 13:56:10.697	11568	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Error attempting to retrieve a block from the db
2018-07-01 13:56:10.701	11568	FATAL	daemon	src/daemon/daemon.cpp:194	Uncaught exception! Error attempting to retrieve a block from the db
2018-07-01 13:56:10.702	11568	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-07-01 13:56:10.711	11568	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-07-01 13:56:11.859	11568	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-07-01 13:56:12.178	11568	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-07-01 13:56:12.178	11568	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
```
```
2019-01-16 20:40:40.691	2136	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2019-01-16 20:40:40.695	2136	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-01-16 20:40:40.697	2136	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-01-16 20:40:40.697	2136	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2019-01-16 20:41:01.757	2136	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2019-01-16 20:41:01.762	2136	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2019-01-16 20:41:01.763	2136	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2019-01-16 20:41:01.764	2136	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2019-01-16 20:41:01.764	2136	INFO 	global	src/daemon/core.h:86	Initializing core...
2019-01-16 20:41:01.766	2136	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder C:\Users\Retia\Monero\lmdb ...
2019-01-16 20:41:01.810	2136	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:4071	[1;33mMigrating blockchain from DB version 1 to 2 - this may take a while:[0m
2019-01-16 20:41:02.345	2136	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:185	Failed to parse transaction from blob
2019-01-16 20:41:02.346	2136	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to parse tx from blob retrieved from the db
2019-01-16 20:41:02.346	2136	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:548	Error opening database: Failed to parse tx from blob retrieved from the db
2019-01-16 20:41:02.385	2136	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2019-01-16 20:41:02.387	2136	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2019-01-16 20:41:03.520	2136	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2019-01-16 20:41:03.566	2136	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2019-01-16 20:41:03.571	2136	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2019-01-16 20:41:03.572	2136	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
```

## moneromooo-monero | 2019-01-16T22:24:38+00:00
Ah, it looks like it's trying to convert before popping, this is annoying.
What you'd do in this case is revert to using the monerod you were using originally, then run:
monero-blockchain-import --pop-blocks 61086
Then, with some luck, you'll be at height 1546000. If you're still above, pop some more blocks. If you're below, it's fine.
Then update to current monerod again, and it should hopefully sync. If not, your db was probably corrupt to start with.


## Retia-Adolf | 2019-01-17T05:19:09+00:00
@moneromooo-monero emmm... not try yet, I found I forgot to mention that it had converted for a while at a few days ago, my first using of this release.

```
2019-01-10 14:25:10.897	10384	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-01-10 14:25:10.899	10384	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2019-01-10 14:25:10.901	10384	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-01-10 14:25:10.901	10384	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-01-10 14:25:10.902	10384	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2019-01-10 14:25:31.938	10384	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2019-01-10 14:25:31.939	10384	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2019-01-10 14:25:31.940	10384	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2019-01-10 14:25:31.941	10384	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2019-01-10 14:25:31.941	10384	INFO 	global	src/daemon/core.h:86	Initializing core...
2019-01-10 14:25:31.942	10384	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder C:\Users\Retia\Monero\lmdb ...
2019-01-10 14:25:31.981	10384	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:4071	[1;33mMigrating blockchain from DB version 1 to 2 - this may take a while:[0m
2019-01-10 14:55:27.000	10384	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:185	Failed to parse transaction from blob
2019-01-10 14:55:27.003	10384	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to parse tx from blob retrieved from the db
2019-01-10 14:55:27.022	10384	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:548	Error opening database: Failed to parse tx from blob retrieved from the db
```

## Retia-Adolf | 2019-08-15T19:25:55+00:00
@moneromooo-monero  Forgot this again for a long time. emmm... what should I do next? ( I know that's enough for me to re-download it many times, but just ask for curious _(:з)∠)_)

```
~\..\..\..\0.12.0.0  .\monero-blockchain-import --data-dir E:\monero --pop-blocks 61086
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:688
        Starting...
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:723
        database: lmdb
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:724
        database flags: 0
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:725
        verify:  true
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:729
        batch:   true  batch size: 5000
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:735
        resume:  true
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:736
        nettype: mainnet
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:738
        bootstrap file path: E:\monero\export\blockchain.raw
2019-08-15 18:06:24.689 13528   INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:739
        database path:       E:\monero
2019-08-15 18:06:24.704 13528   INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder E:\monero\lmdb ...
2019-08-15 18:06:24.704 13528   WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1181
        LMDB memory map needs to be resized, doing that now.
2019-08-15 18:06:24.704 13528   INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:504  LMDB Mapsize increased.  Old: 68484MiB, New: 69508MiB
2019-08-15 18:06:24.736 13528   WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75
        Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2019-08-15 18:06:24.736 13528   INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:588  [batch] DB resize needed
2019-08-15 18:06:24.736 13528   INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:504  LMDB Mapsize increased.  Old: 69508MiB, New: 70532MiB
2019-08-15 18:20:28.881 13528   WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75
        Error attempting to retrieve a block from the db
Error loading blockchain db: Error attempting to retrieve a block from the db -- shutting down now
```

## moneromooo-monero | 2019-08-19T12:02:44+00:00
At this point your db is likely corrupt. Whether it got corrupted by the upgrade process I can't tell.

## MaxXor | 2025-03-16T08:14:46+00:00
Same issue here. Fresh node testing latest not-yet released v0.18.4.0-88a5d0768, can sync till fork version v11. Then it's stuck at Height: 1788724/3368917 (53.1%) on mainnet,

```
2025-03-16 08:09:27.988	I Synced 1787924/3368912 (53%, 1580988 left)
2025-03-16 08:09:28.059	I Synced 1787944/3368912 (53%, 1580968 left)
2025-03-16 08:09:28.135	I Synced 1787964/3368912 (53%, 1580948 left)
2025-03-16 08:09:28.234	I Synced 1787984/3368912 (53%, 1580928 left)
2025-03-16 08:09:28.408	I Validating txpool for v10
2025-03-16 08:09:28.570	I Synced 1788004/3368912 (53%, 1580908 left)
2025-03-16 08:09:28.878	I Synced 1788024/3368912 (53%, 1580888 left)
2025-03-16 08:09:29.049	I Synced 1788044/3368912 (53%, 1580868 left)
2025-03-16 08:09:29.331	I Synced 1788064/3368912 (53%, 1580848 left)
2025-03-16 08:09:29.633	I Synced 1788084/3368912 (53%, 1580828 left)
2025-03-16 08:09:30.001	I Synced 1788104/3368912 (53%, 1580808 left)
2025-03-16 08:09:30.209	I Synced 1788124/3368912 (53%, 1580788 left)
2025-03-16 08:09:30.434	I Synced 1788144/3368912 (53%, 1580768 left)
2025-03-16 08:09:30.597	I Synced 1788164/3368912 (53%, 1580748 left)
2025-03-16 08:09:30.822	I Synced 1788184/3368912 (53%, 1580728 left)
2025-03-16 08:09:31.099	I Synced 1788204/3368912 (53%, 1580708 left)
2025-03-16 08:09:31.282	I Synced 1788224/3368912 (53%, 1580688 left)
2025-03-16 08:09:31.470	I Synced 1788244/3368912 (53%, 1580668 left)
2025-03-16 08:09:31.637	I Synced 1788264/3368912 (53%, 1580648 left)
2025-03-16 08:09:31.812	I Synced 1788284/3368912 (53%, 1580628 left)
2025-03-16 08:09:32.079	I Synced 1788304/3368912 (53%, 1580608 left)
2025-03-16 08:09:32.271	I Synced 1788324/3368912 (53%, 1580588 left)
2025-03-16 08:09:32.435	I Synced 1788344/3368912 (53%, 1580568 left)
2025-03-16 08:09:32.654	I Synced 1788364/3368912 (53%, 1580548 left)
2025-03-16 08:09:32.862	I Synced 1788384/3368912 (53%, 1580528 left)
2025-03-16 08:09:32.998	I Synced 1788404/3368912 (53%, 1580508 left)
2025-03-16 08:09:33.179	I Synced 1788424/3368912 (53%, 1580488 left)
2025-03-16 08:09:33.330	I Synced 1788444/3368912 (53%, 1580468 left)
2025-03-16 08:09:33.469	I Synced 1788464/3368912 (53%, 1580448 left)
2025-03-16 08:09:33.592	I Synced 1788484/3368912 (53%, 1580428 left)
2025-03-16 08:09:33.710	I Synced 1788504/3368912 (53%, 1580408 left)
2025-03-16 08:09:33.852	I Synced 1788524/3368912 (53%, 1580388 left)
2025-03-16 08:09:33.934	I Synced 1788544/3368912 (53%, 1580368 left)
2025-03-16 08:09:34.004	I Synced 1788564/3368912 (53%, 1580348 left)
2025-03-16 08:09:34.110	I Synced 1788584/3368912 (53%, 1580328 left)
2025-03-16 08:09:34.207	I Synced 1788604/3368912 (53%, 1580308 left)
2025-03-16 08:09:34.286	I Synced 1788624/3368912 (53%, 1580288 left)
2025-03-16 08:09:34.320	I Synced 1788644/3368912 (53%, 1580268 left)
2025-03-16 08:09:34.419	I Synced 1788664/3368912 (53%, 1580248 left)
2025-03-16 08:09:34.461	I Synced 1788684/3368912 (53%, 1580228 left)
2025-03-16 08:09:34.524	I Synced 1788704/3368912 (53%, 1580208 left)
2025-03-16 08:09:34.577	I Validating txpool for v11
2025-03-16 08:09:34.596	I Synced 1788724/3368912 (53%, 1580188 left)
2025-03-16 08:09:34.596	E Failed to parse transaction from blob
2025-03-16 08:09:35.319	E Failed to parse transaction from blob
2025-03-16 08:09:36.549	E Failed to parse transaction from blob
2025-03-16 08:09:36.685	E Failed to parse transaction from blob
2025-03-16 08:09:37.265	E Failed to parse transaction from blob
2025-03-16 08:09:37.622	E Failed to parse transaction from blob
2025-03-16 08:09:37.868	E Failed to parse transaction from blob
2025-03-16 08:09:37.869	I Host 51.195.62.81 blocked.
2025-03-16 08:09:41.037	E Failed to parse transaction from blob
2025-03-16 08:09:42.146	E Failed to parse transaction from blob
2025-03-16 08:09:43.240	E Failed to parse transaction from blob
2025-03-16 08:09:43.241	I Host 139.99.125.38 blocked.
2025-03-16 08:09:43.427	E Failed to parse transaction from blob
2025-03-16 08:09:43.428	I Host 135.181.26.236 blocked.
2025-03-16 08:09:43.746	E Failed to parse transaction from blob
2025-03-16 08:09:47.563	E Failed to parse transaction from blob
2025-03-16 08:09:50.987	E Failed to parse transaction from blob
2025-03-16 08:09:52.799	E Failed to parse transaction from blob
2025-03-16 08:09:52.800	I Host 5.161.47.56 blocked.
2025-03-16 08:09:55.953	E Failed to parse transaction from blob
2025-03-16 08:09:57.974	E Failed to parse transaction from blob
2025-03-16 08:09:57.974	I Host 68.118.241.70 blocked.
2025-03-16 08:09:58.895	E Failed to parse transaction from blob
2025-03-16 08:09:59.001	E Failed to parse transaction from blob
2025-03-16 08:09:59.001	I Host 81.6.40.17 blocked.
2025-03-16 08:09:59.222	E Failed to parse transaction from blob
2025-03-16 08:10:00.761	E Failed to parse transaction from blob
2025-03-16 08:10:00.761	I Host 34.95.6.121 blocked.
2025-03-16 08:10:01.851	E Failed to parse transaction from blob
2025-03-16 08:10:01.851	I Host 91.218.20.4 blocked.
2025-03-16 08:10:02.113	E Failed to parse transaction from blob
2025-03-16 08:10:02.113	I Host 213.148.17.110 blocked.
2025-03-16 08:10:02.398	E Failed to parse transaction from blob
2025-03-16 08:10:02.398	I Host 47.248.133.92 blocked.
2025-03-16 08:10:02.987	E Failed to parse transaction from blob
2025-03-16 08:10:02.988	I Host 38.242.206.133 blocked.
2025-03-16 08:10:04.040	E Failed to parse transaction from blob
2025-03-16 08:10:04.041	I Host 73.145.170.84 blocked.
2025-03-16 08:10:04.252	E Failed to parse transaction from blob
2025-03-16 08:10:04.252	I Host 104.234.204.25 blocked.
2025-03-16 08:10:04.775	E Failed to parse transaction from blob
2025-03-16 08:10:09.218	E Failed to parse transaction from blob
2025-03-16 08:10:09.219	I Host 136.28.94.65 blocked.
2025-03-16 08:10:09.842	E Failed to parse transaction from blob
2025-03-16 08:10:15.301	E Failed to parse transaction from blob
2025-03-16 08:10:15.371	E Failed to parse transaction from blob
2025-03-16 08:10:15.572	E Failed to parse transaction from blob
2025-03-16 08:10:19.723	E Failed to parse transaction from blob
2025-03-16 08:10:19.737	E Failed to parse transaction from blob
2025-03-16 08:10:19.737	I Host 139.162.62.53 blocked.
2025-03-16 08:10:21.187	E Failed to parse transaction from blob
2025-03-16 08:10:21.188	I Host 100.42.27.96 blocked.
2025-03-16 08:10:21.892	E Failed to parse transaction from blob
2025-03-16 08:10:21.892	I Host 114.246.103.207 blocked.
2025-03-16 08:10:23.403	E Failed to parse transaction from blob
2025-03-16 08:10:30.110	E Failed to parse transaction from blob
2025-03-16 08:10:31.189	E Failed to parse transaction from blob
2025-03-16 08:10:31.988	E Failed to parse transaction from blob
2025-03-16 08:10:33.447	E Failed to parse transaction from blob
2025-03-16 08:10:33.448	I Host 104.228.83.236 blocked.
2025-03-16 08:10:33.556	E Failed to parse transaction from blob
2025-03-16 08:10:33.556	I Host 65.108.133.154 blocked.
2025-03-16 08:10:36.979	E Failed to parse transaction from blob
2025-03-16 08:10:39.042	E Failed to parse transaction from blob
2025-03-16 08:10:39.042	I Host 89.177.175.95 blocked.
2025-03-16 08:10:42.584	E Failed to parse transaction from blob
2025-03-16 08:10:47.054	E Failed to parse transaction from blob
2025-03-16 08:10:49.594	E Failed to parse transaction from blob
2025-03-16 08:10:52.848	E Failed to parse transaction from blob
2025-03-16 08:10:52.906	E Failed to parse transaction from blob
2025-03-16 08:10:53.718	E Failed to parse transaction from blob
2025-03-16 08:10:54.236	E Failed to parse transaction from blob
2025-03-16 08:10:55.753	E Failed to parse transaction from blob
2025-03-16 08:10:55.754	I Host 174.81.192.129 blocked.
2025-03-16 08:10:56.668	E Failed to parse transaction from blob
2025-03-16 08:10:57.732	E Failed to parse transaction from blob
2025-03-16 08:10:57.733	I Host 77.23.45.22 blocked.
2025-03-16 08:10:58.278	E Failed to parse transaction from blob
2025-03-16 08:10:59.030	E Failed to parse transaction from blob
2025-03-16 08:10:59.031	I Host 66.27.114.116 blocked.
2025-03-16 08:10:59.056	E Failed to parse transaction from blob
2025-03-16 08:10:59.056	I Host 187.49.210.42 blocked.
2025-03-16 08:11:00.807	I [100.42.27.223:18083 OUT] Sync data returned a new top block candidate: 1788724 -> 3368913 [Your node is 1580189 blocks (6.0 years) behind] 
2025-03-16 08:11:00.807	I SYNCHRONIZATION started
2025-03-16 08:11:14.036	E Failed to parse transaction from blob
2025-03-16 08:11:14.037	I Host 212.51.134.243 blocked.
2025-03-16 08:11:14.166	E Failed to parse transaction from blob
2025-03-16 08:11:14.166	I Host 62.194.111.116 blocked.
2025-03-16 08:11:19.681	E Failed to parse transaction from blob
2025-03-16 08:11:19.681	I Host 145.239.0.194 blocked.
2025-03-16 08:11:24.536	E Failed to parse transaction from blob
2025-03-16 08:11:24.749	E Failed to parse transaction from blob
2025-03-16 08:11:27.381	E Failed to parse transaction from blob
2025-03-16 08:11:27.381	I Host 135.181.79.230 blocked.
2025-03-16 08:11:27.621	E Failed to parse transaction from blob
2025-03-16 08:11:27.852	E Failed to parse transaction from blob
2025-03-16 08:11:30.436	E Failed to parse transaction from blob
2025-03-16 08:11:32.214	E Failed to parse transaction from blob
2025-03-16 08:11:32.266	E Failed to parse transaction from blob
2025-03-16 08:11:32.706	E Failed to parse transaction from blob
2025-03-16 08:11:33.873	E Failed to parse transaction from blob
2025-03-16 08:11:34.163	E Failed to parse transaction from blob
2025-03-16 08:11:34.788	E Failed to parse transaction from blob
2025-03-16 08:11:40.152	E Failed to parse transaction from blob
2025-03-16 08:11:45.400	E Failed to parse transaction from blob
2025-03-16 08:11:49.475	E Failed to parse transaction from blob
2025-03-16 08:11:50.767	E Failed to parse transaction from blob
2025-03-16 08:11:50.965	E Failed to parse transaction from blob
2025-03-16 08:11:51.022	E Failed to parse transaction from blob
2025-03-16 08:11:51.716	E Failed to parse transaction from blob
2025-03-16 08:11:52.573	E Failed to parse transaction from blob
2025-03-16 08:11:52.573	I Host 84.170.96.172 blocked.
2025-03-16 08:11:52.608	E Failed to parse transaction from blob
2025-03-16 08:11:52.609	I Host 95.216.28.106 blocked.
2025-03-16 08:11:52.672	E Failed to parse transaction from blob
2025-03-16 08:11:52.673	I Host 45.89.127.227 blocked.
2025-03-16 08:11:52.728	E Failed to parse transaction from blob
2025-03-16 08:11:52.729	I Host 137.184.68.172 blocked.
2025-03-16 08:11:53.954	E Failed to parse transaction from blob
2025-03-16 08:11:53.954	I Host 37.187.142.2 blocked.
2025-03-16 08:11:54.087	E Failed to parse transaction from blob
2025-03-16 08:11:54.087	I Host 147.135.129.32 blocked.
2025-03-16 08:11:54.323	E Failed to parse transaction from blob
2025-03-16 08:11:54.323	I Host 103.253.25.29 blocked.
2025-03-16 08:11:54.434	E Failed to parse transaction from blob
2025-03-16 08:11:54.434	I Host 142.56.48.225 blocked.
2025-03-16 08:11:55.808	E Failed to parse transaction from blob
2025-03-16 08:11:55.809	I Host 178.250.157.63 blocked.
```

# Action History
- Created by: alextrezvy | 2018-11-09T17:23:40+00:00
