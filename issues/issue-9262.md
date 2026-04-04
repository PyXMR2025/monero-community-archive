---
title: monero-gui-mac-armv8 locking up at quit
source_url: https://github.com/monero-project/monero/issues/9262
author: AntlerDM
assignees: []
labels: []
created_at: '2024-03-25T16:51:29+00:00'
updated_at: '2024-03-25T16:53:17+00:00'
type: issue
status: closed
closed_at: '2024-03-25T16:53:17+00:00'
---

# Original Description
This has been happening to me for a few versions now including v0.18.3.2. The GUI seems to function correctly while running, but when I quit, the application locks up and requires a force quit.

Workaround has been to lock the wallet first and then click the "X" button. Locking and then selecting Quit menu causes lockup.

I have tried connecting to a remote daemon and local daemon. And it is the same if I click the X button or select Quit from the menu.

The issue has been happening with macOS versions 13 & 14. Hardware is Mac Studio M1 Ultra.

Lockup Log:
`2024-03-25 16:45:06.674	     0x1f721bac0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-03-25 16:45:06.674	     0x1f721bac0	WARNING	frontend	src/wallet/api/wallet.cpp:411	Logging to "/Users/<USER>/Library/Logs/monero-wallet-gui.log"
2024-03-25 16:45:06.675	     0x1f721bac0	WARNING	frontend	src/wallet/api/wallet.cpp:411	file:///Users/<USER>/Applications/Monero GUI/monero-wallet-gui.app/Contents/Resources/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2024-03-25 16:45:21.253	     0x1f721bac0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,perf.*:DEBUG
2024-03-25 16:45:21.254	     0x16dbff000	INFO	net	contrib/epee/src/net_parse_helpers.cpp:138	[PARSE URI] regex not matched for uri: ^(([^:]*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2024-03-25 16:45:21.255	     0x16dda3000	INFO	wallet.wallet2	src/wallet/wallet2.cpp:8279	ringdb path set to /Users/<USER>/.shared-ringdb
2024-03-25 16:45:21.260	     0x16dbff000	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:137	Generating SSL certificate
2024-03-25 16:45:21.328	     0x16dda3000	INFO	wallet.wallet2	src/wallet/wallet2.cpp:8303	caching ringdb key
2024-03-25 16:45:21.349	     0x16dda3000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:6118	Loaded wallet keys file, with public address: <WALLET ADDRESS>
2024-03-25 16:45:21.377	     0x16dda3000	INFO	wallet.wallet2	src/wallet/wallet2.cpp:6150	Trying to decrypt cache data
2024-03-25 16:45:21.451	     0x16dda3000	INFO	wallet.mms	src/wallet/message_store.cpp:778	No message store file found: /Users/<USER>/Monero/wallets/<USER>/<USER>.mms
2024-03-25 16:45:21.453	     0x16dda3000	INFO	wallet.wallet2	src/wallet/wallet2.cpp:1390	setting daemon to <LOCAL DAEMON>
2024-03-25 16:45:21.453	     0x16dda3000	INFO	net	contrib/epee/src/net_parse_helpers.cpp:138	[PARSE URI] regex not matched for uri: ^(([^:]*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2024-03-25 16:45:21.457	     0x16dda3000	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:137	Generating SSL certificate
2024-03-25 16:45:21.665	     0x16dda3000	INFO	net	contrib/epee/src/net_parse_helpers.cpp:138	[PARSE URI] regex not matched for uri: ^(([^:]*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2024-03-25 16:45:21.807	     0x16dda3000	WARNING	net.ssl	contrib/epee/src/net_ssl.cpp:539	SSL peer has not been verified
2024-03-25 16:45:21.807	     0x16dda3000	WARNING	net.ssl	contrib/epee/src/net_ssl.cpp:539	SSL peer has not been verified`

Lock Wallet successful quit log:
`2024-03-25 16:50:02.898	     0x16e927000	INFO	WalletAPI	src/wallet/api/wallet.cpp:452	~WalletImpl
2024-03-25 16:50:02.899	     0x16e927000	INFO	WalletAPI	src/wallet/api/wallet.cpp:769	closing wallet...
2024-03-25 16:50:02.899	     0x16e927000	INFO	WalletAPI	src/wallet/api/wallet.cpp:780	Calling wallet::stop...
2024-03-25 16:50:02.899	     0x16e927000	INFO	WalletAPI	src/wallet/api/wallet.cpp:782	wallet::stop done
2024-03-25 16:50:02.899	     0x16e927000	INFO	WalletAPI	src/wallet/api/wallet.cpp:465	~WalletImpl finished
`

# Discussion History
## selsta | 2024-03-25T16:53:17+00:00
Please add your comment here https://github.com/monero-project/monero-gui/issues/4286

# Action History
- Created by: AntlerDM | 2024-03-25T16:51:29+00:00
- Closed at: 2024-03-25T16:53:17+00:00
