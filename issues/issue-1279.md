---
title: GUI v0.12.0.0 cannot be upgraded.
source_url: https://github.com/monero-project/monero-gui/issues/1279
author: liukaixin007
assignees: []
labels:
- resolved
created_at: '2018-04-06T03:37:51+00:00'
updated_at: '2018-05-23T18:54:24+00:00'
type: issue
status: closed
closed_at: '2018-05-23T18:54:24+00:00'
---

# Original Description
GUI v0.12.0.0 cannot be upgraded.Open the monero-wallet- GUI. Exe prompt has stopped working.
Log display:

2018-04-06 03:19:57.889 3192 INFO  logging contrib/epee/src/mlog.cpp:185 New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-06 03:19:59.402 3192 WARN  net.http src/common/util.cpp:627 Failed to determine whether address '' is local, assuming not
2018-04-06 03:31:48.565 3772 INFO  logging contrib/epee/src/mlog.cpp:185 New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-06 03:31:49.688 3772 WARN  net.http src/common/util.cpp:627 Failed to determine whether address '' is local, assuming not


# Discussion History
## dEBRUYNE-1 | 2018-04-06T08:41:09+00:00
Could you try launching GUI v0.12 via the `start-low-graphics-mode.bat` batch file that is included?

## liukaixin007 | 2018-04-06T09:12:59+00:00
It's open. Why?

## dEBRUYNE-1 | 2018-04-06T13:30:51+00:00
Good to hear. 

>Why?

It ensures the GUI uses the Qt Quick 2D Renderer instead of relying on OpenGL

## dEBRUYNE-1 | 2018-05-23T18:47:42+00:00
+resolved

# Action History
- Created by: liukaixin007 | 2018-04-06T03:37:51+00:00
- Closed at: 2018-05-23T18:54:24+00:00
