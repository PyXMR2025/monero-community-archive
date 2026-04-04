---
title: Window does not render on MacOS
source_url: https://github.com/monero-project/monero-gui/issues/3457
author: mwthink
assignees: []
labels: []
created_at: '2021-05-06T17:07:16+00:00'
updated_at: '2021-05-06T17:20:14+00:00'
type: issue
status: closed
closed_at: '2021-05-06T17:20:14+00:00'
---

# Original Description
Encountering a strange issue on MacOS (v11.2.3 - Big Sur) where the wallet GUI does not open. The process "starts" and sits in my taskbar, but that is the only evidence of life. It will sit in this state indefinitely until I quit (command + Q) the process.

This issue seems to only happen when I am plugged into my external GPU. If I launch the GUI while I am use the laptop standalone, it works as expected. 

Here are the logs of `bitmonero.log` during this process.
```
2021-05-06 14:57:13.427	     0x10be9fe00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.0-release)
2021-05-06 14:57:14.466	     0x10be9fe00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2021-05-06 15:24:14.162	     0x110a04e00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO

2021-05-06 15:24:14.163	     0x110a04e00	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.0-release)
2021-05-06 15:24:14.425	     0x110a04e00	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2021-05-06 15:26:00.394	     0x1175a0e00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
```

This shows 2 attempts to launch the GUI (with me killing the process in-between). You'll notice there is no additional log output after `New log categories`. When launching successfully, we get these same exact log lines followed by the normal stuff.

There's also the logs from `monero-wallet-gui.log`.
When it fails to start:
```
2021-05-06 16:57:33.822	     0x11008ce00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-05-06 16:57:33.824	     0x11008ce00	WARNING	frontend	src/wallet/api/wallet.cpp:412	Logging to "/Users/mwthink/Library/Logs/monero-wallet-gui.log"
2021-05-06 16:57:33.826	     0x11008ce00	WARNING	frontend	src/wallet/api/wallet.cpp:412	file:///Applications/monero-wallet-gui.app/Contents/Resources/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
```

When we have a successful start:
```
2021-05-06 06:05:07.350	     0x10cd34e00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-05-06 06:05:07.351	     0x10cd34e00	WARNING	frontend	src/wallet/api/wallet.cpp:412	Logging to "/Users/mwthink/Library/Logs/monero-wallet-gui.log"
2021-05-06 06:05:07.353	     0x10cd34e00	WARNING	frontend	src/wallet/api/wallet.cpp:412	file:///Applications/monero-wallet-gui.app/Contents/Resources/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2021-05-06 06:05:07.388	  0x7000113be000	WARNING	frontend	src/wallet/api/wallet.cpp:412	Display non non-main thread! Deferring to main thread
2021-05-06 06:05:53.273	     0x10cd34e00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-05-06 06:05:53.398	  0x70000c373000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5602	Loaded wallet keys file, with public address: <REDACTED>
2021-05-06 06:05:55.655	  0x700011b6b000	WARNING	frontend	src/wallet/api/wallet.cpp:412	Display non non-main thread! Deferring to main thread
```

I've poked and prodded at this a few ways before making this ticket and got nothing. Any insight would be great! 

# Discussion History
## selsta | 2021-05-06T17:17:37+00:00
The issue is with 2 monitors. Try to unplug one and it will work. We are working on a new release that fixes this.

## mwthink | 2021-05-06T17:19:10+00:00
Awesome to hear. I hope that patch supports 3 monitors and not just 2 or else I'll be back 😉

## selsta | 2021-05-06T17:20:14+00:00
You can also compile GUI master if you don't want to wait in the meantime :)

Closing as the reported issue is resolved in repository.

# Action History
- Created by: mwthink | 2021-05-06T17:07:16+00:00
- Closed at: 2021-05-06T17:20:14+00:00
