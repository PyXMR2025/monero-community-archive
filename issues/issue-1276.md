---
title: Compilation went fine, but GUI v0.12.0.0 crashes on Ubuntu 18.04 beta
source_url: https://github.com/monero-project/monero-gui/issues/1276
author: cialu
assignees: []
labels: []
created_at: '2018-04-05T16:44:43+00:00'
updated_at: '2018-04-05T16:50:33+00:00'
type: issue
status: closed
closed_at: '2018-04-05T16:50:33+00:00'
---

# Original Description
Hi,
I have compiled **monero** and **monero-gui** without issues on **Ubuntu 18.04** beta. The _monerod_ daemon and the _monero-wallet-cli_ worked fine, but the _monero-wallet-gui_ crashed on launch.

This is the _monero-wallet-gui.log_:

```
2018-04-05 16:27:07.726	    7fb5bf98c780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-05 16:29:46.772	    7fb510e2e780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-05 16:32:37.226	    7fd2158d2780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
```


I solved the issue installing the missing dependencies _qml-module-qtquick-controls2_ and _qml-module-qt-labs-folderlistmodel_ as explained [here](https://www.reddit.com/r/Monero/comments/892vlr/lithium_luna_gui_released/dwordse/) for Ubuntu 17.10.

# Discussion History
## dEBRUYNE-1 | 2018-04-05T16:48:49+00:00
See #1258.

## cialu | 2018-04-05T16:50:33+00:00
Perfect, I can close the issue.

# Action History
- Created by: cialu | 2018-04-05T16:44:43+00:00
- Closed at: 2018-04-05T16:50:33+00:00
