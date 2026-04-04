---
title: Strange characters in Daemon log
source_url: https://github.com/monero-project/monero-gui/issues/2388
author: juazki
assignees: []
labels:
- bug
created_at: '2019-09-12T13:32:06+00:00'
updated_at: '2019-09-24T15:48:55+00:00'
type: issue
status: closed
closed_at: '2019-09-24T15:48:55+00:00'
---

# Original Description
Every output in the Daemon log shows strange characters:

[12/9/19 11:33] [36m2019-09-12 09:33:44.412 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 09:33:44.413 I Generating SSL certificate
[0mError: Couldn't connect to daemon: 127.0.0.1:18081
[12/9/19 11:34] [36m2019-09-12 09:34:00.429 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 09:34:00.431 I Generating SSL certificate
[0mError: Couldn't connect to daemon: 127.0.0.1:18081
[12/9/19 11:34] [36m2019-09-12 09:34:06.936 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 09:34:06.938 I Generating SSL certificate
[0mError: Couldn't connect to daemon: 127.0.0.1:18081
[12/9/19 11:34] [36m2019-09-12 09:34:11.600 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 09:34:11.601 I Generating SSL certificate
[0mError: Couldn't connect to daemon: 127.0.0.1:18081
[12/9/19 11:34] [36m2019-09-12 09:34:20.134 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 09:34:20.135 I Generating SSL certificate
[0mHeight: 1921409/1921409 (100.0%) on mainnet, not mining, net hash 344.76 MH/s, v11, update needed, 2(out)+0(in) connections, uptime 0d 0h 0m 7s
>>> status
[12/9/19 11:34] [36m2019-09-12 09:34:42.965 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 09:34:42.966 I Generating SSL certificate
[0mHeight: 1921409/1921409 (100.0%) on mainnet, not mining, net hash 344.76 MH/s, v11, update needed, 8(out)+0(in) connections, uptime 0d 0h 0m 29s
>>> status
[12/9/19 15:30] [36m2019-09-12 13:30:08.920 I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
[0m[36m2019-09-12 13:30:08.922 I Generating SSL certificate
[0mHeight: 1921519/1921519 (100.0%) on mainnet, not mining, net hash 344.34 MH/s, v11, update needed, 8(out)+0(in) connections, uptime 0d 3h 55m 52s

Any idea what is the problem?

Monero GUI v0.14.1.2-8f0aedfa1 built from code.


# Discussion History
## erciccione | 2019-09-14T13:07:15+00:00
This looks more like a problem related to your local configuration. Make sure you have no issues with your local fonts and the encoding settings of your terminal.

## selsta | 2019-09-14T20:21:08+00:00
Thanks for reporting this. These are escape codes for colored output, we should strip them.

+bug

## juazki | 2019-09-15T10:58:06+00:00
Terminal messages look fine.

There are some warnings in the terminal output when calling the GUI, maybe they are related to this?

> xxx@xxx:~/monero-gui/build/release/bin$ ./monero-wallet-gui 
> 2019-09-12 09:33:28.077	W app startd (log: /home/xxx/.bitmonero/monero-wallet-gui.log)
> 2019-09-12 09:33:28.082	W Qt:5.12.2 GUI:- | screen: 1600x1200 - dpi: 96 - ratio:0.778186
> 2019-09-12 09:33:29.971	W Failed to determine whether address '' is local, assuming not
> 2019-09-12 09:33:29.971	W Failed to determine whether address '' is local, assuming not
> 2019-09-12 09:33:30.910	W qrc:/pages/merchant/MerchantCheckbox.qml:14:5: QML Rectangle: Detected anchors on an item that is managed by a layout. This is undefined behavior; use Layout.alignment instead.
> 2019-09-12 09:33:30.911	W qrc:/pages/merchant/MerchantCheckbox.qml:39:5: QML MouseArea: Detected anchors on an item that is managed by a layout. This is undefined behavior; use Layout.alignment instead.
> 2019-09-12 09:33:30.911	W qrc:/pages/merchant/MerchantCheckbox.qml:50:5: QML DropShadow: Detected anchors on an item that is managed by a layout. This is undefined behavior; use Layout.alignment instead.
> 2019-09-12 09:33:30.936	W libpng warning: iCCP: known incorrect sRGB profile
> 2019-09-12 09:33:31.531	W qrc:/pages/Keys.qml:248:13: QML StandardButton: Detected anchors on an item that is managed by a layout. This is undefined behavior; use Layout.alignment instead.
> 2019-09-12 09:33:31.991	W file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
> 2019-09-12 09:33:36.787	I Generating SSL certificate
> 2019-09-12 09:33:40.901	W Loaded wallet keys file, with public address: xxxxxxxxxxxxxxxx
> 2019-09-12 09:33:42.077	E No message store file found: /home/xxx/Monero/wallets/xxx/xxx.mms
> 2019-09-12 09:33:42.090	I Generating SSL certificate
> 2019-09-12 09:33:58.392	I Monero 'Boron Butterfly' (v0.14.1.2-8f0aedfa1)
> Forking to background...

All colored messages look fine here.

## selsta | 2019-09-15T13:31:10+00:00
> Terminal messages look fine.

Yes, because your Terminal knows how to deal with escape codes. The GUI displays the daemon log in a textbox that doesn’t know about escape codes so it will display these strange characters.

# Action History
- Created by: juazki | 2019-09-12T13:32:06+00:00
- Closed at: 2019-09-24T15:48:55+00:00
