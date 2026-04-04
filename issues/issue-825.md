---
title: GUI doesn't load translations
source_url: https://github.com/monero-project/monero-gui/issues/825
author: daker
assignees: []
labels:
- bug
- duplicate
created_at: '2017-08-19T21:05:53+00:00'
updated_at: '2017-08-21T06:30:07+00:00'
type: issue
status: closed
closed_at: '2017-08-21T06:30:07+00:00'
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

![capture du 2017-08-19 21-29-37](https://user-images.githubusercontent.com/878518/29490112-85a8b22c-852a-11e7-9c3d-972ae28e78c3.png)

Version: monero-gui-0.10.3.1-beta2
OS: Ubuntu 16.04.2 LTS

# Discussion History
## daker | 2017-08-19T21:22:32+00:00
it appears that the GUI doesn't load translations at all.

## Jaqueeee | 2017-08-20T09:53:27+00:00
Is this the 32 or 64-bit Linux build? This is a known issue with the 32-bit build. 
+bug

## daker | 2017-08-20T17:10:52+00:00
32-bit

## Jaqueeee | 2017-08-21T06:29:56+00:00
see #768
This build should work https://build.getmonero.org/downloads/monero-core-3adb29b-linux-i686.tar.gz

source: https://build.getmonero.org/builders/monero-core-ubuntu-i686/builds/856

+duplicate


# Action History
- Created by: daker | 2017-08-19T21:05:53+00:00
- Closed at: 2017-08-21T06:30:07+00:00
