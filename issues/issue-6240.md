---
title: can not connect 127.0.0.1:18081
source_url: https://github.com/monero-project/monero/issues/6240
author: deepwebhacker
assignees: []
labels: []
created_at: '2019-12-15T11:43:06+00:00'
updated_at: '2020-10-15T22:48:34+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:48:34+00:00'
---

# Original Description
[2019-12-15 19:40] 2019-12-15 11:39:58.749 I Monero 'Carbon Chamaeleon' (v0.15.0.1-release) 
2019-12-15 11:39:58.990 I Generating SSL certificate 
Error: Couldn't connect to daemon: 127.0.0.1:18081

# Discussion History
## moneromooo-monero | 2019-12-15T11:52:35+00:00
I assume you have checked you have a daemon running on that port, right ?

## deepwebhacker | 2019-12-15T11:57:08+00:00
I click the option named “Boot guard”，then,It tells me that starting the process failed

## deepwebhacker | 2019-12-15T11:58:15+00:00
Im from China,My English is so poor

## deepwebhacker | 2019-12-15T11:59:37+00:00
Handsome boy, can you tell me your telegram number？

## deepwebhacker | 2019-12-15T12:02:33+00:00
It allows me to manually start monerod.exe, but I don't want to store the data in disk C

## moneromooo-monero | 2019-12-15T12:06:24+00:00
You can use: --data-dir put-some-directory-here
This will store the blockchain somewhere else of your choosing.
I have no idea what "Boot guard" means. Is this some back translated option from the GUI ?

## deepwebhacker | 2019-12-15T12:09:29+00:00
yes,it is back translated option from the GUI ,I have set the data storage path in GUI interface, but it doesn't work

## deepwebhacker | 2019-12-15T12:09:57+00:00
I use win10

## deepwebhacker | 2019-12-15T12:10:49+00:00
now ，my C disk is small and small

## moneromooo-monero | 2019-12-15T12:21:05+00:00
Find a file called bitmonero.log on your disk, and paste the last 100 lines from it.

## deepwebhacker | 2019-12-15T12:30:36+00:00
It download data on C:\ProgramData\bitmonero\lmdb\

## deepwebhacker | 2019-12-15T12:32:03+00:00
2019-12-15 12:25:51.572	404	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-15 12:25:51.573	404	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2019-12-15 12:25:51.573	404	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-12-15 12:25:51.573	404	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-12-15 12:25:51.574	404	INFO	global	src/daemon/core.h:63	Initializing core...
2019-12-15 12:25:51.576	404	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder F:\XMR-Local-Wallet\lmdb ...
2019-12-15 12:25:51.579	404	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-12-15 12:25:51.579	404	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2019-12-15 12:25:51.580	404	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2019-12-15 12:25:51.582	404	ERROR	daemon	src/daemon/main.cpp:339	Exception in main! Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-12-15 12:26:41.726	5916	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-15 12:26:41.727	5916	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2019-12-15 12:26:41.728	5916	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-12-15 12:26:41.728	5916	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-12-15 12:26:41.729	5916	INFO	global	src/daemon/core.h:63	Initializing core...
2019-12-15 12:26:41.731	5916	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder F:\XMR-Local-Wallet\lmdb ...
2019-12-15 12:26:41.734	5916	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-12-15 12:26:41.735	5916	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2019-12-15 12:26:41.735	5916	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2019-12-15 12:26:41.737	5916	ERROR	daemon	src/daemon/main.cpp:339	Exception in main! Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-12-15 12:28:02.877	9416	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-15 12:28:02.878	9416	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2019-12-15 12:28:02.879	9416	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-12-15 12:28:02.880	9416	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-12-15 12:28:02.881	9416	INFO	global	src/daemon/core.h:63	Initializing core...
2019-12-15 12:28:02.882	9416	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder F:\XMR-Local-Wallet\lmdb ...
2019-12-15 12:28:02.884	9416	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-12-15 12:28:02.885	9416	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2019-12-15 12:28:02.885	9416	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2019-12-15 12:28:02.887	9416	ERROR	daemon	src/daemon/main.cpp:339	Exception in main! Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage


## moneromooo-monero | 2019-12-15T12:42:38+00:00
Then your blockchain is corrupted. There is a known bug which does that, but we've not found a fix yet. The only thing you can do now is resync the blockchain from scratch and hope it doesn't happen again, sorry.

## deepwebhacker | 2019-12-15T12:45:37+00:00
C:/Users/PYBZXF/AppData/Roaming/monero-wallet-gui/monero-wallet-gui.log
↓      ↓      ↓
2019-12-15 12:18:43.894	3260	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:44.407	4788	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:45.594	7848	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:49.081	4268	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:49.761	3344	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:50.986	3344	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:54.738	3344	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:18:54.993	12000	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:19:03.021	4268	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:19:05.078	11768	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:19:07.163	11768	WARNING	util	src/common/util.cpp:893	Failed to determine whether address '' is local, assuming not
2019-12-15 12:19:07.164	3344	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:21:29.641	3344	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:21:29.642	4268	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:21:30.890	4788	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:21:32.084	3260	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:21:32.869	12040	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:21:34.078	12040	WARNING	util	src/common/util.cpp:893	Failed to determine whether address '' is local, assuming not
2019-12-15 12:21:34.078	11768	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:24:13.595	3464	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-15 12:24:13.595	3464	WARNING	frontend	src/wallet/api/wallet.cpp:410	app startd (log: C:/Users/PYBZXF/AppData/Roaming/monero-wallet-gui/monero-wallet-gui.log)
2019-12-15 12:24:13.597	3464	WARNING	frontend	src/wallet/api/wallet.cpp:410	Qt:5.9.7 GUI:v0.15.0.2 | screen: 1920x1080 - dpi: 120 - ratio:1.10613
2019-12-15 12:24:23.463	3464	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2019-12-15 12:25:08.977	3464	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-15 12:25:09.364	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:09.468	5728	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5434	Loaded wallet keys file, with public address: 44mknptWyF2E7tRH6PW9Tbd8chpHAe4ii4Vtvsby6DqwAaDEJqJmStzbBJtFvveSUaETswyybiQx9U2Bbr8SQhY468eGD9U
2019-12-15 12:25:09.503	5728	ERROR	wallet.mms	src/wallet/message_store.cpp:727	No message store file found: G:\XMR\XMR-Local-Wallet/pyb_xmr_wallet/pyb_xmr_wallet.mms
2019-12-15 12:25:09.568	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:19.777	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:19.777	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:47.933	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:47.933	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:49.973	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:50.715	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:50.781	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:25:57.759	1196	WARNING	util	src/common/util.cpp:893	Failed to determine whether address '' is local, assuming not
2019-12-15 12:25:57.759	9100	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:26:35.044	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:26:35.044	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:26:38.411	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:26:38.411	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:26:39.970	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:26:45.241	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:53.187	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:53.187	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:56.159	9100	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:56.159	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:57.835	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:59.116	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:27:59.609	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:00.878	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:02.395	9100	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:03.179	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:04.014	13112	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:05.694	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:06.709	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:07.023	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:08.899	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:10.256	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:10.271	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:10.652	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:11.280	13112	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:12.738	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:13.738	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:14.155	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:14.561	13112	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:15.127	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:15.976	9220	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:16.606	1196	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:19.668	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:21.306	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:21.783	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:28:26.081	13112	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:29:15.949	2416	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:29:15.949	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:31:21.344	2084	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1031	daemonBlockChainHeight: Failed to connect to daemon
2019-12-15 12:31:23.351	2084	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1050	daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-15 12:31:25.356	2084	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1031	daemonBlockChainHeight: Failed to connect to daemon
2019-12-15 12:31:29.373	5728	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1031	daemonBlockChainHeight: Failed to connect to daemon
2019-12-15 12:31:31.375	2416	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1050	daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-15 12:33:33.914	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:33:33.914	2024	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:33:57.413	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:33:57.413	4912	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:35:39.459	13112	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:35:40.897	9100	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:10.631	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:10.632	12852	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:13.887	12852	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:13.887	7580	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:15.955	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:17.115	7580	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:17.849	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:18.303	12568	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:43.917	12568	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:43.917	7580	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:47.135	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:47.357	5728	WARNING	util	src/common/util.cpp:893	Failed to determine whether address '' is local, assuming not
2019-12-15 12:38:47.826	12852	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:52.203	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:52.203	7580	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:54.793	12852	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:56.952	12568	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:58.633	2584	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:59.149	3684	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:38:59.927	5728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:39:01.206	10728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:39:02.616	12852	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:39:04.626	10728	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:39:07.407	12568	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-12-15 12:39:11.252	3684	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate

## streetgrid | 2020-05-14T22:30:12+00:00
I keep getting the same issue and have since I first tried running the full Monero node.  I have been doing lots of research and it seems to come down to one little line of code when running the monerod:

dyld: lazy symbol binding failed: Symbol not found: _clock_gettime
  Referenced from: /Applications/monero-wallet-gui.app/Contents/MacOS/monerod (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib

dyld: Symbol not found: _clock_gettime
  Referenced from: /Applications/monero-wallet-gui.app/Contents/MacOS/monerod (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib

From [what I have read](https://github.com/gambit/gambit/issues/293), the issue seems to be with the _clock_gettime command.  It may need to reference what to do with a need to "export MACOSX_DEPLOYMENT_TARGET=10.11" before "make" to disable use of clock_gettime) or something similar. 

Anybody else have issues not running the latest version of OSX?

## selsta | 2020-05-14T22:32:06+00:00
@StreetGrid Which OS are you running? macOS 10.11?

## streetgrid | 2020-05-14T23:29:54+00:00
@selsta It's macOS 10.10.5

## selsta | 2020-05-14T23:35:18+00:00
Looks like you are using the GUI. Does the CLI version from getmonero.org work?

## streetgrid | 2020-05-14T23:52:08+00:00
I haven't tried it.  Perhaps I'll download it and give it a shot

## streetgrid | 2020-05-15T00:06:40+00:00
Similar issue -- 
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.

## selsta | 2020-05-15T00:07:29+00:00
You have to start the daemon (monerod) first.

## streetgrid | 2020-05-15T00:14:29+00:00
Cool.  It's running in the CLI version.  I wonder if there is some way to use the daemon from this for the GUI ... 


## selsta | 2020-05-15T00:15:52+00:00
Yes. Open the finder, right click on monero-wallet-gui.app and then `Show package contents -> Contents -> macOS` and then replace the monerod with the working one. 

We will make sure that the next version does not requires this file replacing workaround.

## streetgrid | 2020-05-15T00:19:07+00:00
Excellent!  I'll give that a shot once it syncs.  If I have the same issues, I'll just use the CLI.  I appreciate your help.

## streetgrid | 2020-05-15T00:32:22+00:00
FYI ... I replaced monerod within the Package Contents for the GUI and it's syncing! 

Sending you some BAT for a tip ;)  I've been working at this for a while. 


# Action History
- Created by: deepwebhacker | 2019-12-15T11:43:06+00:00
- Closed at: 2020-10-15T22:48:34+00:00
