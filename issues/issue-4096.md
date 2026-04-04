---
title: GUI wallet Crashes on MAC
source_url: https://github.com/monero-project/monero/issues/4096
author: italocoin-project
assignees: []
labels:
- invalid
created_at: '2018-07-04T13:18:12+00:00'
updated_at: '2018-07-12T22:25:05+00:00'
type: issue
status: closed
closed_at: '2018-07-12T22:25:05+00:00'
---

# Original Description
**SORRY i now noticed i'm not on GUI repo**

GUI wallet crashes on MAC and i can't seem to solve it, any advices?

here is the error
```
2018-07-04 12:15:58.740      0x7fffa0fa8380    WARN     frontend    src/wallet/api/wallet.cpp:361    app startd (log: /Users/xxxx/Library/Logs/monero-wallet-gui.log)
2018-07-04 12:15:58.744      0x7fffa0fa8380    WARN     frontend    src/wallet/api/wallet.cpp:361    Qt:5.10.0 | screen: 1280x800 - dpi: 72 - ratio:0.890625
2018-07-04 12:16:00.647      0x7fffa0fa8380    WARN     frontend    src/wallet/api/wallet.cpp:361    QQmlApplicationEngine failed to load component
2018-07-04 12:16:00.647      0x7fffa0fa8380    WARN     frontend    src/wallet/api/wallet.cpp:361    qrc:///main.qml:1542 Type WizardMain unavailable
qrc:///wizard/WizardMain.qml:252 Type WizardWelcome unavailable
qrc:///wizard/WizardWelcome.qml:30 module "QtQuick.XmlListModel" is not installed

2018-07-04 12:16:00.647      0x7fffa0fa8380    ERROR    frontend    src/wallet/api/wallet.cpp:365    Error: no root objects
```

# Discussion History
## moneromooo-monero | 2018-07-04T13:40:46+00:00
That's not a crash. And you're missing some Qt widget package.

## italocoin-project | 2018-07-04T14:35:29+00:00
I don;t think i miss them here they are:

```
 ls -l /usr/local/Cellar/qt/5.10.0/qml/
total 112
drwxr-xr-x   4 xxxx  admin    128 Dec  2  2017 Qt
drwxr-xr-x   8 xxxx  admin    256 Dec  2  2017 Qt3D
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtAudioEngine
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtBluetooth
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtCanvas3D
drwxr-xr-x   6 xxxx  admin    192 Dec  2  2017 QtCharts
drwxr-xr-x   6 xxxx  admin    192 Dec  2  2017 QtDataVisualization
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtGamepad
drwxr-xr-x  31 xxxx  admin    992 Dec  2  2017 QtGraphicalEffects
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtLocation
drwxr-xr-x   6 xxxx  admin    192 Dec  2  2017 QtMultimedia
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtNfc
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtPositioning
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtPurchasing
drwxr-xr-x   7 xxxx  admin    224 Dec  2  2017 QtQml
drwxr-xr-x  17 xxxx  admin    544 Dec  2  2017 QtQuick
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtQuick.2
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtScxml
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtSensors
drwxr-xr-x   8 xxxx  admin    256 Dec  2  2017 QtTest
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtWebChannel
drwxr-xr-x   7 xxxx  admin    224 Dec  2  2017 QtWebEngine
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtWebSockets
drwxr-xr-x   5 xxxx  admin    160 Dec  2  2017 QtWebView
-rw-r--r--   1 xxxx  admin  56367 Dec  2  2017 builtins.qmltypes

 ls -l /usr/local/Cellar/qt/5.10.0/qml/QtQuick
total 0
drwxr-xr-x  56 xxxx  admin  1792 May 28 18:14 Controls
drwxr-xr-x  64 xxxx  admin  2048 Dec  2  2017 Controls.2
drwxr-xr-x  19 xxxx  admin   608 May 28 18:14 Dialogs
drwxr-xr-x  16 xxxx  admin   512 Dec  2  2017 Extras
drwxr-xr-x   5 xxxx  admin   160 Dec  2  2017 Layouts
drwxr-xr-x   5 xxxx  admin   160 Dec  2  2017 LocalStorage
drwxr-xr-x   5 xxxx  admin   160 Dec  2  2017 Particles.2
drwxr-xr-x   5 xxxx  admin   160 Dec  2  2017 PrivateWidgets
drwxr-xr-x   5 xxxx  admin   160 Dec  2  2017 Scene2D
drwxr-xr-x   5 xxxx  admin   160 Dec  2  2017 Scene3D
drwxr-xr-x   5 xxx admin   160 Dec  2  2017 Shapes
drwxr-xr-x   5 xxx admin   160 Dec  2  2017 Templates.2
drwxr-xr-x   5 xxx admin   160 Dec  2  2017 VirtualKeyboard
drwxr-xr-x   5 xxx admin   160 Dec  2  2017 Window.2
drwxr-xr-x   5 xxx admin   160 Dec  2  2017 XmlListModel
```

and this is the crash 

`2018-07-04 12:16:00.647      0x7fffa0fa8380    ERROR    frontend    src/wallet/api/wallet.cpp:365    Error: no root objects`

I'm not a MAC guy so any suggestion how to fix this would be apreciated! Thanks

## dEBRUYNE-1 | 2018-07-04T19:45:34+00:00
Is this a binary you built yourself or are you using the GUI v0.12.2.0 release binary? 

## italocoin-project | 2018-07-04T20:08:22+00:00
Its GUI v0.12.2.0 and i build it from source

## dEBRUYNE-1 | 2018-07-05T11:04:01+00:00
Does the error also occur when you use the GUI v0.12.2.0 release binaries? 

## moneromooo-monero | 2018-07-12T22:13:48+00:00
Let this be dealt with on the GUI repo.

+invalid


# Action History
- Created by: italocoin-project | 2018-07-04T13:18:12+00:00
- Closed at: 2018-07-12T22:25:05+00:00
