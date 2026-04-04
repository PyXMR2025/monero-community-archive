---
title: crashed
source_url: https://github.com/monero-project/monero-gui/issues/1297
author: sx5486510
assignees: []
labels:
- resolved
created_at: '2018-04-09T03:00:54+00:00'
updated_at: '2018-04-28T17:36:18+00:00'
type: issue
status: closed
closed_at: '2018-04-28T17:36:18+00:00'
---

# Original Description
问题事件名称:	BEX64
  应用程序名:	monero-wallet-gui.exe
  应用程序版本:	0.0.0.0
  应用程序时间戳:	5ac38fb4
  故障模块名称:	StackHash_1dc2
  故障模块版本:	0.0.0.0
  故障模块时间戳:	00000000
  异常偏移:	0000000000000000
  异常代码:	c0000005
  异常数据:	0000000000000008
  OS 版本:	6.1.7601.2.1.0.256.1
  区域设置 ID:	2052
  其他信息 1:	1dc2
  其他信息 2:	1dc22fb1de37d348f27e54dbb5278e7d
  其他信息 3:	eae3
  其他信息 4:	eae36a4b5ffb27c9d33117f4125a75c2


# Discussion History
## sx5486510 | 2018-04-09T03:02:47+00:00
monero-wallet-gui.log

2018-04-09 03:01:56.049	7548	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-09 03:01:57.551	7548	WARN 	net.http	src/common/util.cpp:627	Failed to determine whether address '' is local, assuming not
2018-04-09 03:02:00.179	2300	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received


## sx5486510 | 2018-04-09T03:12:11+00:00
if run from start-low-graphics-mode.bat, it's worked

## sanderfoobar | 2018-04-09T08:21:36+00:00
Please post your OS/videocard details and the videocard drivers you're using (if any)

## sanderfoobar | 2018-04-28T17:04:30+00:00
If `start-low-graphics-mode.bat` works, I'm guessing this is related to the absence of fallback with angle/mesa on Windows. The next release `12.1` will have these fallbacks, and I suspect your issue will then be resolved. If not, re-create issue.

+resolved

# Action History
- Created by: sx5486510 | 2018-04-09T03:00:54+00:00
- Closed at: 2018-04-28T17:36:18+00:00
