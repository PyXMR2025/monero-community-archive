---
title: Gui crashing on start - Failed to determine whether address '' is local, assuming
  not
source_url: https://github.com/monero-project/monero-gui/issues/1302
author: pedro-reis
assignees: []
labels:
- resolved
created_at: '2018-04-09T09:18:58+00:00'
updated_at: '2018-07-04T10:00:35+00:00'
type: issue
status: closed
closed_at: '2018-07-04T10:00:35+00:00'
---

# Original Description
Windows 10 64Bits with 64Bits Wallet v0.12

2018-04-09 09:15:22.631	9812	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-09 09:15:23.892	9812	WARN 	net.http	src/common/util.cpp:627	Failed to determine whether address '' is local, assuming not

# Discussion History
## stoffu | 2018-04-09T09:35:26+00:00
That warning message is normal and can be ignored. Perhaps the issue is due to the graphics card. Please refer to https://monero.stackexchange.com/questions/7997/windows-gui-v0-12-does-not-launch-start and try running the GUI with `start-low-graphics-mode.bat`.

## dEBRUYNE-1 | 2018-07-04T08:38:17+00:00
This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-04T08:38:22+00:00
+resolved

# Action History
- Created by: pedro-reis | 2018-04-09T09:18:58+00:00
- Closed at: 2018-07-04T10:00:35+00:00
