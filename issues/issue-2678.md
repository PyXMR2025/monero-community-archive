---
title: Daemon failed to start OS X 10.13
source_url: https://github.com/monero-project/monero/issues/2678
author: xxdetourxx
assignees: []
labels: []
created_at: '2017-10-18T19:34:50+00:00'
updated_at: '2017-10-18T23:18:29+00:00'
type: issue
status: closed
closed_at: '2017-10-18T23:18:29+00:00'
---

# Original Description
I'm running the latest release from the website 0.11.0,0, and after the latest update to OS X 10.13 Supplemental the daemon will no longer start.

Changed logging to level 4 and got the following errors, I was not sure how/if I could resolve it myself, a search for the error message did not provide and workaround.

from monero-wallet-gui.log:
2017-10-18 19:31:24.464	  0x70000398b000	TRACE	WalletAPI	src/wallet/api/wallet.cpp:1332	doRefresh: skipping refresh - daemon is not synced
2017-10-18 19:31:24.464	  0x70000398b000	TRACE	WalletAPI	src/wallet/api/wallet.cpp:1292	refreshThreadFunc: waiting for refresh...
2017-10-18 19:31:25.512	  0x700003ea9000	WARN 	net	contrib/epee/include/net/net_helper.h:177	Some problems at connect, message: Connection refused

from bitmonero.log:
2017-10-18 19:31:00.057	  0x7fffb7893340	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-18 19:31:07.655	  0x7fffb7893340	FATAL	daemon	src/daemon/daemon.cpp:150	Uncaught exception! Error adding spent key image to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2017-10-18 19:31:07.666	  0x7fffb7893340	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...

I haven't done anything in the app yet, I installed it, ran it, and was waiting for the blockchain to sync. Computer updated, and when it ran the wallet GUI after boot, daemon would not start any more.

I also tried to do a build from master with docker, failed at that as well.

# Discussion History
## moneromooo-monero | 2017-10-18T20:15:40+00:00
Usually I thought you'd get a different error before that one. Anyway, try running monerod with --db-salvage and see if that helps.

## xxdetourxx | 2017-10-18T23:18:29+00:00
Same error as before:

2017-10-18 22:44:48.927	  0x7fffb7893340	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /Users/Ben/.bitmonero/lmdb ...
2017-10-18 22:45:00.263	  0x7fffb7893340	FATAL	daemon	src/daemon/daemon.cpp:150	Uncaught exception! Error adding spent key image to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid

However, this time I took a second to read the line before it, where it started reading the blockchain, and I thought "Hmm, I wonder if the chain got messed up somehow." So I went to the appropriate folder and deleted the two databases.

Viola, issue resolved! Hope this might help someone else in the future.

# Action History
- Created by: xxdetourxx | 2017-10-18T19:34:50+00:00
- Closed at: 2017-10-18T23:18:29+00:00
