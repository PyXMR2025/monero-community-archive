---
title: 'Pending forever transaction '
source_url: https://github.com/monero-project/monero-gui/issues/1027
author: theguy62
assignees: []
labels: []
created_at: '2017-12-17T09:16:09+00:00'
updated_at: '2017-12-27T20:34:30+00:00'
type: issue
status: closed
closed_at: '2017-12-27T20:34:30+00:00'
---

# Original Description
Hi,

I have a problem with a pending transaction using monero-gui that does not execute but stays in pending seemingly forever. This is the second time now and I used this guide https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui
 and executed all steps in there and finally created a new database as described in the guide to get rid of the pending transaction. After this I tried again with the same result - a pending transaction. 
The blockchain is fully synced and the block height in the status dialog matches the block height in MoneroBase.

Here is an extract of the log file:
2017-12-19 20:00:34.650	13812	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-19 20:00:36.062	13812	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-19 20:00:36.405	13812	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-19 20:00:36.542	13812	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-19 20:00:36.617	4120	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-12-19 20:00:36.617	4120	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-12-19 20:00:36.617	4120	WARN 	net.http	src/wallet/wallet_errors.h:707	C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-12-19 20:00:36.618	4120	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-12-19 20:00:36.812	4120	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-12-19 20:02:35.487	13812	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
...
2017-12-19 20:02:37.238	18088	WARN 	net	contrib/epee/include/net/net_helper.h:177	Some problems at connect, message: No connection could be made because the target machine actively refused it
2017-12-19 20:02:38.240	12264	WARN 	net	contrib/epee/include/net/net_helper.h:177	Some problems at connect, message: No connection could be made because the target machine actively refused it
2017-12-19 20:05:22.882	12264	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-12-19 20:05:22.882	12264	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2017-12-19 20:05:24.046	12264	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:660	Transaction extra has unsupported format: <
2017-12-19 20:09:18.301	13812	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-12-19 20:09:18.301	13812	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2017-12-19 20:10:24.383	12264	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:660	Transaction extra has unsupported format: <

Your help is greatly appreciated.

Thx Bob

# Discussion History
# Action History
- Created by: theguy62 | 2017-12-17T09:16:09+00:00
- Closed at: 2017-12-27T20:34:30+00:00
