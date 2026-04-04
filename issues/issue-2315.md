---
title: File Chooser appears without a text
source_url: https://github.com/monero-project/monero/issues/2315
author: daker
assignees: []
labels: []
created_at: '2017-08-19T20:39:32+00:00'
updated_at: '2017-08-19T21:06:26+00:00'
type: issue
status: closed
closed_at: '2017-08-19T21:06:26+00:00'
---

# Original Description
Start Monero GUI using:

```
$ ./start-gui.sh 
High DPI auto scaling - enabled
2017-08-19 21:37:13.606	        XYZ	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-08-19 21:37:14.269	        XYZ	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
```

Choose a language -> Choose USB -> File Chooser appears without a text


![capture du 2017-08-19 21-29-37](https://user-images.githubusercontent.com/878518/29489971-1b8e8e42-8526-11e7-9962-d810a07265e7.png)

Version: monero-gui-0.10.3.1-beta2
OS: Ubuntu 16.04.2 LTS

# Discussion History
## daker | 2017-08-19T21:06:26+00:00
Reported against monero-core

# Action History
- Created by: daker | 2017-08-19T20:39:32+00:00
- Closed at: 2017-08-19T21:06:26+00:00
