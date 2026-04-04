---
title: Can't create wallet from hardware wallet
source_url: https://github.com/monero-project/monero-gui/issues/3114
author: lochuan
assignees: []
labels: []
created_at: '2020-09-26T10:31:19+00:00'
updated_at: '2023-01-17T05:09:20+00:00'
type: issue
status: closed
closed_at: '2023-01-17T05:09:19+00:00'
---

# Original Description
2020-09-26 10:24:49.512	     0x116840dc0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-09-26 10:24:49.512	     0x116840dc0	WARNING	frontend	src/wallet/api/wallet.cpp:412	app startd (log: /Users/lochuan/Library/Logs/monero-wallet-gui.log)
2020-09-26 10:24:49.514	     0x116840dc0	WARNING	frontend	src/wallet/api/wallet.cpp:412	Qt:5.12.8 GUI:- | screen: 1440x900 - dpi: 72 - ratio:0.998047
2020-09-26 10:25:11.561	     0x116840dc0	WARNING	frontend	src/wallet/api/wallet.cpp:412	file:///Applications/monero-wallet-gui.app/Contents/Resources/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2020-09-26 10:25:11.573	  0x700008907000	ERROR	device.io	src/device/device_io_hid.cpp:167	Unable to open device 4:11415
2020-09-26 10:25:14.210	  0x700008907000	ERROR	device.io	src/device/device_io_hid.cpp:167	Unable to open device 4:11415
2020-09-26 10:25:14.708	  0x700008907000	ERROR	device.io	src/device/device_io_hid.cpp:167	Unable to open device 4:11415

# Discussion History
## selsta | 2020-09-27T01:51:08+00:00
Please try to make sure Ledger Live is closed, also try to restart your computer, different USB port, etc. Also make sure the Monero app is open.

## lochuan | 2020-09-29T15:26:57+00:00
> Please try to make sure Ledger Live is closed, also try to restart your computer, different USB port, etc. Also make sure the Monero app is open.

Have tried all the methods, even tried on multiple computer with different OS, doesn't work.

## mateMathieu | 2021-10-20T15:40:19+00:00
Same thing here.
Do you know that Ledger have published some udev rules here?
https://github.com/LedgerHQ/udev-rules
Best regards

## mateMathieu | 2021-10-20T16:44:43+00:00
OK I fixed it by applying the aforementioned udev rules.
If you include t hem in the gui, it should work out.
Best

## selsta | 2023-01-17T05:09:19+00:00
Closing due to inactivity. There are currently no known Ledger issues with the latest version.

# Action History
- Created by: lochuan | 2020-09-26T10:31:19+00:00
- Closed at: 2023-01-17T05:09:19+00:00
