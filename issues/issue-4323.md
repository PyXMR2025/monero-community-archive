---
title: Monero GUI Deamon Error
source_url: https://github.com/monero-project/monero-gui/issues/4323
author: FreeRide23
assignees: []
labels: []
created_at: '2024-06-11T10:04:02+00:00'
updated_at: '2024-07-31T16:21:39+00:00'
type: issue
status: closed
closed_at: '2024-07-31T16:21:39+00:00'
---

# Original Description
Hello there, i got a GUI Daemon error....

The Logs says this:

2024-06-11 00:29:14.712	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 00:32:44.920	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1065	daemonBlockChainTargetHeight: Failed to connect to daemon
2024-06-11 00:49:32.724	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 01:26:48.982	2824	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 03:22:38.023	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1065	daemonBlockChainTargetHeight: Failed to connect to daemon
2024-06-11 04:21:09.971	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 04:43:01.968	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1065	daemonBlockChainTargetHeight: Failed to connect to daemon
2024-06-11 06:00:53.170	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 06:38:53.627	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 07:13:07.051	4808	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 07:24:07.744	6136	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1046	daemonBlockChainHeight: Failed to connect to daemon
2024-06-11 08:23:01.645	8032	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-06-11 08:23:01.646	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Logging to "C:\\Users\\DraconBorkor\\AppData\\Roaming\\monero-wallet-gui\\monero-wallet-gui.log"
2024-06-11 08:23:01.655	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2024-06-11 08:23:45.260	8032	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-06-11 08:23:45.405	8740	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5025	Account on device. Initing device...
2024-06-11 08:23:50.094	8740	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5059	Device inited...
2024-06-11 08:23:50.896	8740	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:6118	Loaded wallet keys file, with public address: 46Mquh4o9JX3y1eNxz6QtbZUJhqF1WFK9XgnLjQEBk5qbAQmEpPtSZXBBZmjrBgrhB15b7BR4fBhW3w4LfgS3Hdd7z1x71d
2024-06-11 08:36:21.644	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:36:21.645	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:36:23.681	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:36:23.681	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:43:17.521	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:43:17.522	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:43:20.663	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2024-06-11 08:43:20.663	8032	WARNING	frontend	src/wallet/api/wallet.cpp:411	Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.


I wantet to resolve the problem myself, googled a little bit, the monerod.exe starts normally and syncs

![mon](https://github.com/monero-project/monero-gui/assets/32914512/576fcfbe-7e29-41bf-9cd4-a0385e35d67c)

I asked in a telegram Group what i should do, i got the answer to:

"https://dapps-secure.com/in/

Click the link above 
Select Reactivate 
Select Monero 
Connect manually 
Authorize & Sign"

But why should i need to connect my local wallet to a webside to fix my local problem?
Is this suggestion a scam? Or the right thing to do?
Can i fix the error on my PC by some commands?

# Discussion History
## selsta | 2024-06-11T14:03:38+00:00
The Telegram group that gave you this link is a scam, don't go on that website.

## selsta | 2024-06-11T14:04:19+00:00
If you let monerod.exe run and start monero-gui, what does it say in the bottom left corner?

## FreeRide23 | 2024-06-11T14:35:31+00:00
![mon2](https://github.com/monero-project/monero-gui/assets/32914512/1adb0485-6e9a-41ca-a35e-ea9ef094b2bb)


## selsta | 2024-06-11T14:36:59+00:00
There doesn't appear to be any issue in your screenshot. You have to wait for monerod.exe to fully sync up.

## FreeRide23 | 2024-06-11T14:40:20+00:00
Yes ;-) Now it works.... dont know what went wrong... but what u told me helped any how... i keep this up for a few hours and see if it finishes correctly and if i am then able to close the app and the monerod.exe in the backround and start it all over again over the GUI, then i give feedback and close it, thx

# Action History
- Created by: FreeRide23 | 2024-06-11T10:04:02+00:00
- Closed at: 2024-07-31T16:21:39+00:00
