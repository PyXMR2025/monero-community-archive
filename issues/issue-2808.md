---
title: Daemon fail to start through GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/2808
author: Lafudoci
assignees: []
labels: []
created_at: '2020-03-15T03:12:27+00:00'
updated_at: '2023-01-18T06:16:54+00:00'
type: issue
status: closed
closed_at: '2023-01-18T06:16:54+00:00'
---

# Original Description
Wallet version: 0.15.0.4
OS version: Windows 10 x64

GUI wallet works well with manually started monerod. But if I try to start daemon by clicking "wallet setting/node/start daemon", it shows 120s timeout error.

ps. I'm forwarding this issue from a memeber in my local community.
Here is some wallet log he provided that I found might help:
```
2020-03-15 02:21:42.563	6652	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2185	pauseRefresh: refresh paused...
2020-03-15 02:21:42.563	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Displaying processing splash
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [monerod.exe] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [--db-sync-mode] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [safe] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [--block-sync-size] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [20] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [--data-dir] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [E:\\XMR\\bitmonero] "
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"starting monerod C:/Program Files/Monero GUI Wallet/monerod.exe"
2020-03-15 02:21:42.567	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	With command line arguments  ("monerod.exe", "--db-sync-mode", "safe", "--block-sync-size", "20", "--data-dir", "E:\\XMR\\bitmonero", "--data-dir", "E:\\XMR\\bitmonero", "--bootstrap-daemon-address", "node1.xmr-tw.org:18081", "--check-updates", "disabled", "--max-concurrency", "2")
2020-03-15 02:21:44.678	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 02:21:47.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 02:21:47.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 02:21:47.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-03-15 02:21:47.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 02:21:47.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 02:21:49.975	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 02:21:45.901\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 02:21:45.903\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 02:21:49.975	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 02:21:51.976	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 02:21:57.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 02:21:57.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 02:21:57.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-03-15 02:21:57.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 02:21:57.347	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 02:21:58.312	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 02:21:53.136\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 02:21:53.138\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 02:21:58.312	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 02:22:00.313	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 02:22:04.842	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 02:22:01.484\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 02:22:01.486\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 02:22:04.842	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 02:22:06.843	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 02:22:07.348	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 02:22:07.348	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 02:22:07.348	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-03-15 02:22:07.348	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 02:22:07.348	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 02:22:11.401	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 02:22:07.992\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 02:22:07.994\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 02:22:11.401	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 02:22:13.402	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 02:22:17.350	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 02:22:17.350	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 02:22:17.350	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-03-15 02:22:17.350	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 02:22:17.350	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
```
```
2020-03-15 02:23:49.367	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 02:23:45.177\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 02:23:45.178\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 02:23:49.367	9800	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 02:23:49.412	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon start failed
2020-03-15 02:23:49.412	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Hiding processing splash
2020-03-15 02:23:49.415	6652	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2165	startRefresh: refresh started/resumed...
2020-03-15 02:23:49.415	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 02:23:49.416	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 02:23:49.416	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-03-15 02:23:49.416	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 02:23:49.416	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 02:23:49.416	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 02:23:51.420	11920	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 02:23:51.420	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 02:23:51.420	11920	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 02:23:51.421	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 02:23:51.425	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 02:23:51.425	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 02:23:51.431	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 02:23:51.440	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 02:23:53.430	9800	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 02:23:53.431	6652	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 02:24:01.422	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 02:24:01.422	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 02:24:01.422	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-03-15 02:24:01.422	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 02:24:01.422	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 02:24:01.422	11920	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
```

# Discussion History
## selsta | 2020-03-15T09:14:33+00:00
Do you use simple mode or advanced mode? 

When you go to Settings -> Node, is the bootstrap-daemon and bootstrap-port textbox empty?

## xiphon | 2020-03-15T09:20:51+00:00
Drop `--data-dir` argument from `Daemon startup flags`. Use `Blockchain location` field instead.

## Lafudoci | 2020-03-15T12:46:02+00:00
> Do you use simple mode or advanced mode?
> 
> When you go to Settings -> Node, is the bootstrap-daemon and bootstrap-port textbox empty?

It was in advanced mode with miscofigured bootstrap setting. I have told him to remove bootstrap setting. But the issue persists without bootstrap setting.

> Drop `--data-dir` argument from `Daemon startup flags`. Use `Blockchain location` field instead.

We have moved this arg to GUI field. But it's still uable to start daemon.

Here is the last log
```
2020-03-15 12:36:51.547	4484	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 12:36:51.547	4484	WARNING	frontend	src/wallet/api/wallet.cpp:410	app startd (log: C:/Users/john/AppData/Roaming/monero-wallet-gui/monero-wallet-gui.log)
2020-03-15 12:36:51.549	4484	WARNING	frontend	src/wallet/api/wallet.cpp:410	Qt:5.12.2 GUI:- | screen: 1440x900 - dpi: 96 - ratio:0.60374
2020-03-15 12:36:53.919	4484	WARNING	frontend	src/wallet/api/wallet.cpp:410	DirectWrite: CreateFontFaceFromHDC() failed (指示輸入檔案 (例如，字型檔案) 中的錯誤。) for QFontDef(Family="Fixedsys", stylename=Solid, pointsize=13.5, pixelsize=16, styleHint=5, weight=50, stretch=100, hintingPreference=0) LOGFONT("Fixedsys", lfWidth=0, lfHeight=-16) dpi=96
2020-03-15 12:36:55.899	4484	WARNING	frontend	src/wallet/api/wallet.cpp:410	DirectWrite: CreateFontFaceFromHDC() failed (指示輸入檔案 (例如，字型檔案) 中的錯誤。) for QFontDef(Family="Fixedsys", pointsize=9, pixelsize=16, styleHint=5, weight=75, stretch=100, hintingPreference=0) LOGFONT("Fixedsys", lfWidth=0, lfHeight=-16) dpi=96
2020-03-15 12:36:57.436	4484	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2020-03-15 12:36:57.926	7060	WARNING	frontend	src/wallet/api/wallet.cpp:410	DirectWrite: CreateFontFaceFromHDC() failed (指示輸入檔案 (例如，字型檔案) 中的錯誤。) for QFontDef(Family="Fixedsys", stylename=Solid, pointsize=13.5, pixelsize=16, styleHint=5, weight=50, stretch=100, hintingPreference=0) LOGFONT("Fixedsys", lfWidth=0, lfHeight=-16) dpi=96
2020-03-15 12:37:09.546	4484	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:TRACE
2020-03-15 12:37:09.546	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	setLanguage   "zh-tw"
2020-03-15 12:37:09.547	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	setLanguage: loading translation file 'monero-core_zh-tw' from 'C:/Program Files/Monero GUI Wallet/translations'
2020-03-15 12:37:09.547	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	setLanguage: couldn't load translation file 'monero-core_zh-tw' from 'C:/Program Files/Monero GUI Wallet/translations'
2020-03-15 12:37:09.547	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	setLanguage: loading embedded translation file 'monero-core_zh-tw'
2020-03-15 12:37:09.547	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	setLanguage: embedded translation for language 'zh-tw' loaded successfully
2020-03-15 12:37:10.487	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	transfer page loaded
2020-03-15 12:37:10.492	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	opening wallet at:  C:/Users/john/Documents/Monero/wallets/local/local , network type:  mainnet
2020-03-15 12:37:10.492	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Displaying processing splash
2020-03-15 12:37:10.493	7648	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2020-03-15 12:37:10.494	7648	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 12:37:10.495	5232	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type, quint64): opening wallet at C:/Users/john/Documents/Monero/wallets/local/local, nettype = 0 
2020-03-15 12:37:10.496	5232	DEBUG	device.ledger	src/device/device_ledger.cpp:246	Device 0 Created
2020-03-15 12:37:10.497	5232	DEBUG	frontend	src/wallet/api/wallet.cpp:402	onSetWallet
2020-03-15 12:37:10.497	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2096	refreshThreadFunc: starting refresh thread
2020-03-15 12:37:10.498	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:37:10.498	5232	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7302	ringdb path set to C:\ProgramData\.shared-ringdb
2020-03-15 12:37:10.918	5232	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7326	caching ringdb key
2020-03-15 12:37:11.016	5232	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5434	Loaded wallet keys file, with public address: 45r4zJQySfjXTuirD28rvodr94XZAb2TTBAniqvDzUvhVK1MsMdb2VdHfArQTFHharjivt3VFc2eJ9YrAWdLb4ZfFfQypmp
2020-03-15 12:37:11.028	5232	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5456	Trying to decrypt cache data
2020-03-15 12:37:11.261	5232	ERROR	wallet.mms	src/wallet/message_store.cpp:727	No message store file found: C:/Users/john/Documents/Monero/wallets/local/local.mms
2020-03-15 12:37:11.261	5232	DEBUG	wallet.wallet2	src/wallet/api/address_book.cpp:98	Refreshing addressbook
2020-03-15 12:37:11.261	5232	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type, quint64): opened wallet: 45r4zJQySfjXTuirD28rvodr94XZAb2TTBAniqvDzUvhVK1MsMdb2VdHfArQTFHharjivt3VFc2eJ9YrAWdLb4ZfFfQypmp, status: 0
2020-03-15 12:37:11.280	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Hiding processing splash
2020-03-15 12:37:11.282	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet opened: Wallet(0xb537f00)
2020-03-15 12:37:11.289	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Recovering from seed:  false
2020-03-15 12:37:11.289	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	restore Height 0
2020-03-15 12:37:11.289	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	initializing with daemon address:  localhost:18081
2020-03-15 12:37:11.289	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"initAsync: localhost:18081"
2020-03-15 12:37:11.289	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:37:11.290	7648	DEBUG	frontend	src/wallet/api/wallet.cpp:402	init non async
2020-03-15 12:37:11.290	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:37:11.290	7648	INFO	wallet.wallet2	src/wallet/wallet2.cpp:1297	setting daemon to localhost:18081
2020-03-15 12:37:11.290	7648	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2020-03-15 12:37:11.290	7648	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 12:37:11.292	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:37:11.293	9596	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:37:11.296	1792	DEBUG	net.http	contrib/epee/include/net/http_client.h:382	Reconnecting...
2020-03-15 12:37:11.624	4484	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:5611	trimming to 1957999, offset 1958000
2020-03-15 12:37:12.346	7648	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2020-03-15 12:37:12.347	7648	DEBUG	util	src/common/util.cpp:907	Address 'localhost:18081' is local
2020-03-15 12:37:12.347	7648	DEBUG	frontend	src/wallet/api/wallet.cpp:402	init async finished - starting refresh
2020-03-15 12:37:12.347	7648	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:37:12.347	7648	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2165	startRefresh: refresh started/resumed...
2020-03-15 12:37:12.347	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:37:12.348	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 12:37:12.348	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:37:12.348	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:37:12.348	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 12:37:12.348	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 12:37:13.305	1792	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:13.305	1792	DEBUG	net.http	contrib/epee/include/net/http_client.h:385	Failed to connect to localhost:18081
2020-03-15 12:37:13.305	1792	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /mining_status
2020-03-15 12:37:14.356	5232	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:14.364	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:37:16.359	7648	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:17.360	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Settings page loaded
2020-03-15 12:37:17.832	9596	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:37:12.497\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:37:12.499\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:37:18.362	2756	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:18.362	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 12:37:18.362	2756	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 12:37:18.362	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:37:18.362	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 12:37:18.363	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:37:18.364	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:37:18.365	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 12:37:20.365	1792	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:20.365	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:37:22.370	5232	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:28.363	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:37:28.363	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 12:37:28.363	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:37:28.363	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:37:28.363	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 12:37:28.363	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 12:37:30.369	2756	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:30.369	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 12:37:30.369	2756	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 12:37:30.370	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:37:30.370	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 12:37:30.370	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:37:30.372	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:37:30.373	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 12:37:30.774	4484	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2185	pauseRefresh: refresh paused...
2020-03-15 12:37:30.774	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Displaying processing splash
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [monerod.exe] "
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [--db-sync-mode] "
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [safe] "
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [--block-sync-size] "
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	" [20] "
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"starting monerod C:/Program Files/Monero GUI Wallet/monerod.exe"
2020-03-15 12:37:30.787	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	With command line arguments  ("monerod.exe", "--db-sync-mode", "safe", "--block-sync-size", "20", "--data-dir", "E:\\XMR\\bitmonero", "--check-updates", "disabled", "--max-concurrency", "2")
2020-03-15 12:37:32.379	9596	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:37:32.392	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:37:32.816	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:37:36.282	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:37:33.987\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:37:33.989\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:37:36.282	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:37:38.283	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:37:40.372	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:37:40.372	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:37:40.372	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:37:40.372	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:37:40.372	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:37:44.629	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:37:39.434\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:37:39.436\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:37:44.629	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:37:46.630	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:37:50.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:37:50.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:37:50.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:37:50.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:37:50.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:37:50.934	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:37:47.857\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:37:47.859\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:37:50.934	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:37:52.935	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:37:58.086	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:37:54.129\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:37:54.165\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:37:58.086	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:00.087	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:00.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:38:00.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:38:00.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:38:00.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:38:00.375	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:38:06.111	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:01.235\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:01.237\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:06.111	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:08.112	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:10.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:38:10.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:38:10.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:38:10.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:38:10.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:38:12.837	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:09.264\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:09.266\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:12.837	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:14.839	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:20.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:38:20.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:38:20.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:38:20.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:38:20.378	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:38:21.561	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:15.973\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:15.976\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:21.561	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:23.562	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:27.515	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:24.705\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:24.707\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:27.515	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:29.516	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:30.379	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:38:30.379	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:38:30.379	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:38:30.379	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:38:30.379	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:38:33.157	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:30.654\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:30.656\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:33.157	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:35.158	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:39.848	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:36.319\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:36.321\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:39.848	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:40.380	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:38:40.380	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:38:40.380	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:38:40.380	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:38:40.380	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:38:41.849	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:46.653	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:43.021\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:43.029\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:46.653	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:48.654	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:50.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:38:50.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:38:50.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:38:50.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:38:50.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:38:53.083	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:49.803\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:49.806\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:53.083	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:38:55.084	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:38:59.264	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:38:56.298\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:38:56.300\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:38:59.264	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:39:00.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:00.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:39:00.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:00.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:00.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:01.265	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:39:05.479	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:39:02.436\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:39:02.438\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:39:05.479	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:39:07.480	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:39:10.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:10.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:39:10.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:10.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:10.381	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:11.816	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:39:08.675\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:39:08.677\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:39:11.816	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:39:13.817	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:39:20.383	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:20.383	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:39:20.383	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:20.383	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:20.383	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:21.375	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:39:14.973\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:39:14.974\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:39:21.375	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:39:23.376	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:39:26.899	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:39:24.549\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:39:24.551\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:39:26.899	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:39:28.900	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	sending external cmd:  ("sync_info")
2020-03-15 12:39:30.386	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:30.386	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:39:30.386	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:30.386	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:30.386	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:33.342	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	"2020-03-15 12:39:30.039\tI Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)\r\n2020-03-15 12:39:30.041\tI Generating SSL certificate\r\nError: Couldn't connect to daemon: 127.0.0.1:18081\r\n"
2020-03-15 12:39:33.342	1792	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon not running. checking again in 2 seconds.
2020-03-15 12:39:33.413	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	daemon start failed
2020-03-15 12:39:33.413	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Hiding processing splash
2020-03-15 12:39:33.415	4484	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2165	startRefresh: refresh started/resumed...
2020-03-15 12:39:33.415	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:33.415	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 12:39:33.415	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:33.415	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:33.416	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 12:39:33.416	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 12:39:35.420	2756	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:39:35.420	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 12:39:35.420	2756	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 12:39:35.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:35.421	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 12:39:35.422	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:39:35.441	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:39:35.444	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 12:39:37.424	1792	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:39:37.438	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:39:45.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:45.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 12:39:45.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:45.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:45.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 12:39:45.421	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 12:39:47.428	2756	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:39:47.428	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 12:39:47.428	2756	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 12:39:47.428	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:47.432	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 12:39:47.432	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:39:47.433	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:39:47.434	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 12:39:49.436	10360	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:39:49.442	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:39:57.429	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:39:57.429	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 12:39:57.429	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:39:57.429	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:39:57.429	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 12:39:57.429	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 12:39:59.432	2756	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:39:59.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 12:39:59.432	2756	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 12:39:59.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:39:59.433	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 12:39:59.433	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:39:59.433	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:39:59.435	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 12:40:01.437	10984	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:40:01.442	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:40:09.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:40:09.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-03-15 12:40:09.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:40:09.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:40:09.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-03-15 12:40:09.432	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-03-15 12:40:11.441	2756	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:40:11.441	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2149	doRefresh: skipping refresh - daemon is not synced
2020-03-15 12:40:11.441	2756	DEBUG	frontend	src/wallet/api/wallet.cpp:402	refreshed
2020-03-15 12:40:11.441	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2103	refreshThreadFunc: waiting for refresh...
2020-03-15 12:40:11.441	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet refreshed
2020-03-15 12:40:11.441	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Checking connection status
2020-03-15 12:40:11.442	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 3
2020-03-15 12:40:11.443	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	>>> wallet updated
2020-03-15 12:40:13.446	1792	DEBUG	net	contrib/epee/include/net/net_helper.h:238	Some problems at connect, message: �L�k�s�u�A�]���ؼйq���ڵ��s�u�C
2020-03-15 12:40:13.446	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet connection status changed 0
2020-03-15 12:40:20.979	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	blocking close event
2020-03-15 12:40:20.980	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	close accepted
2020-03-15 12:40:20.980	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	DaemonManager: exit()
2020-03-15 12:40:20.983	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Displaying processing splash
2020-03-15 12:40:20.997	10944	DEBUG	frontend	src/wallet/api/wallet.cpp:402	~Wallet: Closing wallet
2020-03-15 12:40:20.997	10944	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:5611	trimming to 1957999, offset 1958000
2020-03-15 12:40:21.133	10944	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Wallet cache stored successfully
2020-03-15 12:40:21.133	10944	INFO	WalletAPI	src/wallet/api/wallet.cpp:451	~WalletImpl
2020-03-15 12:40:21.133	10944	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2185	pauseRefresh: refresh paused...
2020-03-15 12:40:21.133	10944	INFO	WalletAPI	src/wallet/api/wallet.cpp:764	closing wallet...
2020-03-15 12:40:21.133	10944	INFO	WalletAPI	src/wallet/api/wallet.cpp:775	Calling wallet::stop...
2020-03-15 12:40:21.133	10944	INFO	WalletAPI	src/wallet/api/wallet.cpp:777	wallet::stop done
2020-03-15 12:40:21.133	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-03-15 12:40:21.133	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 0
2020-03-15 12:40:21.133	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 0
2020-03-15 12:40:21.133	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-03-15 12:40:21.133	2756	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2122	refreshThreadFunc: refresh thread stopped
2020-03-15 12:40:21.134	10944	INFO	WalletAPI	src/wallet/api/wallet.cpp:464	~WalletImpl finished
2020-03-15 12:40:21.134	10944	DEBUG	net	contrib/epee/include/net/net_helper.h:647	Problems at ssl shutdown: uninitialized
2020-03-15 12:40:21.134	10944	DEBUG	net	contrib/epee/include/net/net_helper.h:571	Problems at cancel: ���Ѫ��ɮױ����N�X�L�ġC
2020-03-15 12:40:21.134	10944	DEBUG	net	contrib/epee/include/net/net_helper.h:574	Problems at shutdown: ���Ѫ��ɮױ����N�X�L�ġC
2020-03-15 12:40:21.137	10944	DEBUG	net	contrib/epee/include/net/net_helper.h:647	Problems at ssl shutdown: uninitialized
2020-03-15 12:40:21.137	10944	DEBUG	net	contrib/epee/include/net/net_helper.h:571	Problems at cancel: ���Ѫ��ɮױ����N�X�L�ġC
2020-03-15 12:40:21.137	10944	DEBUG	net	contrib/epee/include/net/net_helper.h:574	Problems at shutdown: ���Ѫ��ɮױ����N�X�L�ġC
2020-03-15 12:40:21.138	10944	DEBUG	frontend	src/wallet/api/wallet.cpp:402	m_walletImpl deleted
2020-03-15 12:40:21.141	4484	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Hiding processing splash
2020-03-15 12:40:21.708	4484	DEBUG	device.ledger	src/device/device_ledger.cpp:251	Device 0 Destroyed
```


## Lafudoci | 2020-03-15T13:02:29+00:00
Here is the bitmonero.log
```
2020-03-15 12:53:54.159	10932	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 12:53:54.160	10932	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-03-15 12:53:54.162	10932	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
```

## xiphon | 2020-03-15T13:34:07+00:00
Does running the following command in command prompt successfully start monerod?

`"C:\Program Files\Monero GUI Wallet\monerod.exe" --db-sync-mode safe --block-sync-size 20 --data-dir E:\XMR\bitmonero --check-updates disabled --max-concurrency 2`

## Lafudoci | 2020-03-15T13:40:53+00:00
> Does running the following command in command prompt successfully start monerod?
> 
> `"C:\Program Files\Monero GUI Wallet\monerod.exe" --db-sync-mode safe --block-sync-size 20 --data-dir E:\XMR\bitmonero --check-updates disabled --max-concurrency 2`

Yes, it does through the CMD.

## xiphon | 2020-03-15T13:57:39+00:00
> Here is the bitmonero.log

Are you sure is the correct one? 

If GUI fails to start monerod process, it logs appropriate error message. Given that there is no such message in the logs, it successfully started monerod process. But then there should be startup log messages in `bitmonero.log`.

## Lafudoci | 2020-03-15T14:11:36+00:00
> > Here is the bitmonero.log
> 
> Are you sure is the correct one?
> 
> If GUI fails to start monerod process, it logs appropriate error message. Given that there is no such message in the logs, it successfully started monerod process. But then there should be startup log messages in `bitmonero.log`.

I was wondering this too. So I have already asked him to make sure the bitmonero.log is the last one from E: location.



## Lafudoci | 2020-03-15T14:29:38+00:00
We have tried turning off antivirus and firewall. But it was not helping either.

## xiphon | 2020-03-15T23:28:45+00:00
> We have tried turning off antivirus and firewall. But it was not helping either.

Does the system have third-party antivirus software installed?

## Lafudoci | 2020-03-16T01:38:06+00:00
> Does the system have third-party antivirus software installed?

It's only with built-in win10 antivirus. But I'll ask him to check again.

So it's more probable an external issue that something blocks the launch of daemon?

## xiphon | 2020-03-16T02:05:21+00:00
> So it's more probable an external issue that something blocks the launch of daemon?

Yep, at this point GUI logs doesn't comply with monerod logs. Either we should see specific error in GUI logs or startup messages in monerod logs.

## dEBRUYNE-1 | 2020-03-16T20:22:44+00:00
@Lafudoci - regarding the AV, you can refer him to this guide:

https://monero.stackexchange.com/questions/10798/my-antivirus-av-software-blocks-quarantines-the-monero-gui-wallet-is-there

## Lafudoci | 2020-03-18T10:35:04+00:00
> @Lafudoci - regarding the AV, you can refer him to this guide:
> 
> https://monero.stackexchange.com/questions/10798/my-antivirus-av-software-blocks-quarantines-the-monero-gui-wallet-is-there

Thanks for your information. I'll forward it. However, I can't reproduce this issue on my own Win10 1909 laptop. The buit-in AV seems not aggressive to monerod.exe.

## selsta | 2023-01-18T06:16:54+00:00
Closing due to inactivity and lack of logs to investigate the issue.

# Action History
- Created by: Lafudoci | 2020-03-15T03:12:27+00:00
- Closed at: 2023-01-18T06:16:54+00:00
