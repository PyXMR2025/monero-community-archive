---
title: 'v0.12.2 fails to launch with "module "QtQuick" version 2.10 is not installed
  / Error: no root objects"'
source_url: https://github.com/monero-project/monero-gui/issues/1500
author: jwt27
assignees: []
labels:
- resolved
created_at: '2018-07-09T10:46:23+00:00'
updated_at: '2018-07-14T15:45:22+00:00'
type: issue
status: closed
closed_at: '2018-07-14T15:45:22+00:00'
---

# Original Description
After installing v0.12.2, overwriting v0.12.0, monero-gui no longer starts. The process briefly appears in task manager and immediately closes, writing no information to the log file.

Running in gdb yields the following error message:
```
Reading symbols from monero-wallet-gui.exe...(no debugging symbols found)...done.
(gdb) run
Starting program: D:\programs\Monero\monero-wallet-gui.exe
[New Thread 7580.0x235c]
warning: QCoreApplication::applicationDirPath: Please instantiate the QApplication object first
2018-07-08 19:25:20.122 9052    WARN    frontend        src/wallet/api/wallet.cpp:327   app startd (log: /monero-wallet-gui.log)
2018-07-08 19:25:20.122 9052    WARN    frontend        src/wallet/api/wallet.cpp:327   Qt:5.7.0 | screen: 2048x1536 - dpi: 96 - ratio:0.562621
[New Thread 7580.0x24e0]
[New Thread 7580.0x2798]
[New Thread 7580.0x20e0]
[New Thread 7580.0x1a00]
[New Thread 7580.0x18b0]
[New Thread 7580.0xb94]
[New Thread 7580.0x19a4]
[Thread 7580.0x19a4 exited with code 0]
2018-07-08 19:25:22.179 9052    WARN    frontend        src/wallet/api/wallet.cpp:327   QQmlApplicationEngine failed to load component
2018-07-08 19:25:22.179 9052    WARN    frontend        src/wallet/api/wallet.cpp:327   qrc:///main.qml:1432 Type MiddlePanel unavailable
qrc:///MiddlePanel.qml:41 Type Keys unavailable
qrc:///pages/Keys.qml:125 Type LineEditMulti unavailable
qrc:///components/LineEditMulti.qml:97 Type MoneroComponents.InputMulti unavailable
qrc:///components/InputMulti.qml:36 Type TextArea unavailable
file:///D:/programs/Monero/QtQuick/Controls.2/Fusion/TextArea.qml:37 module "QtQuick" version 2.10 is not installed

2018-07-08 19:25:22.179 9052    ERROR   frontend        src/wallet/api/wallet.cpp:331   Error: no root objects
[Thread 7580.0x24e0 exited with code 0]
[Thread 7580.0x18b0 exited with code 1]
[Thread 7580.0xb94 exited with code 1]
[Thread 7580.0x1a00 exited with code 1]
[Thread 7580.0x20e0 exited with code 1]
[Thread 7580.0x2798 exited with code 1]
[Inferior 1 (process 7580) exited with code 01]
```

OS: Windows 7 x86_64

# Discussion History
## cryptochangements34 | 2018-07-09T22:48:47+00:00
You need to use the latest version of Qt

## jwt27 | 2018-07-10T03:38:59+00:00
Shouldn't that be included with the full release?

## sanderfoobar | 2018-07-10T08:13:03+00:00
The previous release (0.12.0) ran on Qt 5.10. Some files are left behind when you overwrote it with the current release, which runs on Qt 5.7.1. My guess is that an attempt is made by the current release to include certain files from the previous release, which yielded some incompatibility.

Simple solution is to not overwrite the files but start from scratch. Doubt that we can properly fix it, post-release.

## dEBRUYNE-1 | 2018-07-10T08:48:04+00:00
Please see:

https://reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/e21xnyd/

## Doy-lee | 2018-07-10T10:55:49+00:00
For clarification does this mean that the minimum Qt version has been bumped up to 5.10? Seems building from source with 5.7 has similar runtime QML problems.

## sanderfoobar | 2018-07-10T11:30:51+00:00
@Doy-lee `5.7.1` should not yield these errors. The current official binaries for 0.12.3 are compiled with 5.7.1 (or 5.7.0). 

Please note that you should not overwrite a previous installation, rather run it as is.

## sanderfoobar | 2018-07-14T15:39:29+00:00
Should be fixed. In the future you may overwrite previous installations. This was a special situation :)

+resolved

# Action History
- Created by: jwt27 | 2018-07-09T10:46:23+00:00
- Closed at: 2018-07-14T15:45:22+00:00
