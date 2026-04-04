---
title: Can't prove payment was made - Payment proof check bad signature
source_url: https://github.com/monero-project/monero-gui/issues/1935
author: ghost
assignees: []
labels:
- resolved
created_at: '2019-02-11T18:26:00+00:00'
updated_at: '2019-02-25T11:00:41+00:00'
type: issue
status: closed
closed_at: '2019-02-25T11:00:41+00:00'
---

# Original Description
In the prove/check tab of the wallet I get "Bad signature" when I press "check" after filling the tx_id and SpendProof.
I can't seem to be able to verify the transaction on https://xmr.llcoins.net/checktx.html with tx_key either. 
I use ledger nano s to sign transactions.

Here's the log file:
```
2019-02-11 18:09:42.455	    7fcf9f5888c0	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-02-11 18:09:42.456	    7fcf9f5888c0	WARN 	frontend	src/wallet/api/wallet.cpp:367	app startd (log: /home/myusername/monero-wallet-gui.log)
2019-02-11 18:09:42.458	    7fcf9f5888c0	WARN 	frontend	src/wallet/api/wallet.cpp:367	Qt:5.7.0 | screen: 1920x1080 - dpi: 96 - ratio:0.716621
2019-02-11 18:09:43.725	    7fcf9f5888c0	WARN 	frontend	src/wallet/api/wallet.cpp:367	<Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredHeight"
2019-02-11 18:09:43.785	    7fcf9f5888c0	WARN 	frontend	src/wallet/api/wallet.cpp:367	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:241:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2019-02-11 18:09:47.642	    7fcf9f5888c0	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-02-11 18:09:47.728	    7fcf80fa1700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3411	Account on device. Initing device...
2019-02-11 18:09:58.252	    7fcf80fa1700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3417	Device inited...
2019-02-11 18:09:58.771	    7fcf80fa1700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:4590	Loaded wallet keys file, with public address: ///////redacted
2019-02-11 18:11:18.370	    7fcf9f5888c0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:9772	!received. THROW EXCEPTION: error::wallet_internal_error
```

The exception is thrown when I press the 'P' button to obtain a spend proof in the history of transactions.

# Discussion History
## dEBRUYNE-1 | 2019-02-18T15:42:34+00:00
I *think* Ledger in conjunction with Monero does not support the private transaction key yet (on which the payment proof is based as well). As a result, it yields a bad signature. 

In my opinion, it would be better to open a new feature request on the Ledger Monero blue app Github repository. 

https://github.com/LedgerHQ/ledger-app-monero

## dEBRUYNE-1 | 2019-02-25T10:54:28+00:00
Going to mark this as resolved, as it is more relevant on the Ledger Monero app repository. 

+resolved

# Action History
- Created by: ghost | 2019-02-11T18:26:00+00:00
- Closed at: 2019-02-25T11:00:41+00:00
