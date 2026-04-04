---
title: v0.12.3.0 does not recognize ledger
source_url: https://github.com/monero-project/monero-gui/issues/1524
author: M5M400
assignees: []
labels:
- resolved
created_at: '2018-07-27T12:10:38+00:00'
updated_at: '2019-03-13T07:36:38+00:00'
type: issue
status: closed
closed_at: '2019-03-13T07:36:38+00:00'
---

# Original Description
just built v0.12.3.0 (6206e3d) on ubuntu 18.04 server x64; won't recognize ledger hardware wallet.

```
2018-07-27 12:04:44.259	    7f753943f780	WARN 	frontend	src/wallet/api/wallet.cpp:327	app startd (log: /home/blah/monero-wallet-gui.log)
2018-07-27 12:04:44.259	    7f753943f780	WARN 	frontend	src/wallet/api/wallet.cpp:327	Qt:5.9.5 | screen: 2560x1440 - dpi: 96 - ratio:0.849972
2018-07-27 12:04:44.914	    7f753943f780	WARN 	frontend	src/wallet/api/wallet.cpp:327	qrc:///components/TitleBar.qml:70:9: QML Image: Cannot anchor to an item that isn't a parent or sibling.
2018-07-27 12:04:44.989	    7f753943f780	WARN 	net.http	src/common/util.cpp:683	Failed to determine whether address '' is local, assuming not
2018-07-27 12:04:44.989	    7f753943f780	WARN 	net.http	src/common/util.cpp:683	Failed to determine whether address '' is local, assuming not
2018-07-27 12:04:45.385	    7f753943f780	WARN 	frontend	src/wallet/api/wallet.cpp:327	file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2018-07-27 12:04:45.386	    7f753943f780	WARN 	frontend	src/wallet/api/wallet.cpp:327	qrc:///components/InputDialog.qml:68: ReferenceError: bg is not defined
2018-07-27 12:04:45.497	    7f74fffff700	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-07-27 12:05:07.008	    7f74fffff700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2865	Account on device. Initing device...
2018-07-27 12:05:07.009	    7f74fffff700	ERROR	default	src/device/device.cpp:60	device not found in registry: 'Ledger'
known devices:
2018-07-27 12:05:07.009	    7f74fffff700	ERROR	default	src/device/device.cpp:63	 - default
2018-07-27 12:05:07.009	    7f74fffff700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:627	Error opening wallet: device not found: Ledger
2018-07-27 12:05:07.013	    7f753943f780	ERROR	frontend	src/wallet/api/wallet.cpp:331	Error opening wallet with password:  device not found: Ledger
2018-07-27 12:05:34.417	    7f753943f780	ERROR	default	src/device/device.cpp:60	device not found in registry: 'Ledger'
known devices:
2018-07-27 12:05:34.417	    7f753943f780	ERROR	default	src/device/device.cpp:63	 - default
2018-07-27 12:05:37.739	    7f753943f780	ERROR	frontend	src/wallet/api/wallet.cpp:331	Trying to close non existing wallet  QObject(0x0)
```
works fine with public precompiled version

# Discussion History
## mmbyday | 2019-03-13T02:23:01+00:00
+invalid 
obsolete. Reopen if issue still persists.

## dEBRUYNE-1 | 2019-03-13T07:26:02+00:00
+resolved

# Action History
- Created by: M5M400 | 2018-07-27T12:10:38+00:00
- Closed at: 2019-03-13T07:36:38+00:00
