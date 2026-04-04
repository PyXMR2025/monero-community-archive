---
title: Wallet gui doesn work
source_url: https://github.com/monero-project/monero-gui/issues/1506
author: leaenbinario
assignees: []
labels: []
created_at: '2018-07-11T00:04:00+00:00'
updated_at: '2018-07-11T00:11:09+00:00'
type: issue
status: closed
closed_at: '2018-07-11T00:11:09+00:00'
---

# Original Description
I have ubuntu 16.04.02 and i can use my wallet. I didn't have problems with v12.0.0 and lhe last week my v12.2.0 was fine, but now i have this error

....:~/wallets/monero-gui-v0.12.2.0$ ./monero-wallet-gui
2018-07-11 00:01:30.053	    7f5035ac1780	WARN 	frontend	src/wallet/api/wallet.cpp:327	app startd (log: /home/lea/monero-wallet-gui.log)
2018-07-11 00:01:30.054	    7f5035ac1780	WARN 	frontend	src/wallet/api/wallet.cpp:327	Qt:5.7.0 | screen: 1920x1080 - dpi: 96 - ratio:0.238125
2018-07-11 00:01:31.638	    7f5035ac1780	WARN 	frontend	src/wallet/api/wallet.cpp:327	qrc:///components/TitleBar.qml:70:9: QML Image: Cannot anchor to an item that isn't a parent or sibling.
2018-07-11 00:01:31.728	    7f5035ac1780	WARN 	net.http	src/common/util.cpp:669	Failed to determine whether address '' is local, assuming not
2018-07-11 00:01:31.729	    7f5035ac1780	WARN 	net.http	src/common/util.cpp:669	Failed to determine whether address '' is local, assuming not
2018-07-11 00:01:32.080	    7f5035ac1780	WARN 	frontend	src/wallet/api/wallet.cpp:327	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:241:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2018-07-11 00:01:32.082	    7f5035ac1780	WARN 	frontend	src/wallet/api/wallet.cpp:327	qrc:///components/InputDialog.qml:68: ReferenceError: bg is not defined
2018-07-11 00:01:32.170	    7f5035ac1780	ERROR	frontend	src/wallet/api/wallet.cpp:331	Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior 2, swapInterval 1, profile  0) 
Aborted (core dumped)


# Discussion History
## leaenbinario | 2018-07-11T00:11:09+00:00
ooohhhhhh. My ubuntu was updating in background. I restarted my pc and started again the wallet and now is fine.
Please ignore this issue 

# Action History
- Created by: leaenbinario | 2018-07-11T00:04:00+00:00
- Closed at: 2018-07-11T00:11:09+00:00
