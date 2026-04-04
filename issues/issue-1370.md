---
title: '''Error: no root objects'' running monero-wallet-gui in Ubuntu 16.04 x64 on
  Asus UX410U'
source_url: https://github.com/monero-project/monero-gui/issues/1370
author: chrisfeigl
assignees: []
labels: []
created_at: '2018-05-04T00:55:22+00:00'
updated_at: '2018-05-22T17:26:38+00:00'
type: issue
status: closed
closed_at: '2018-05-22T17:26:38+00:00'
---

# Original Description
I installed Monero GUI as per the instructions on the [Monero github page](https://github.com/monero-project/monero-gui/blob/master/README.md)

These were the steps:

1. Install Monero dependencies

   For Ubuntu and Mint

`sudo apt install build-essential cmake libboost-all-dev miniupnpc libunbound-dev graphviz doxygen libunwind8-dev pkg-config libssl-dev libzmq3-dev`

2. Grab an up-to-date copy of the monero-gui repository

`git clone https://github.com/monero-project/monero-gui.git`

Go into the repository

`cd monero-gui`

Install the GUI dependencies

   For Ubuntu 16.04+ x64

`sudo apt install qtbase5-dev qt5-default qtdeclarative5-dev qml-module-qtquick-controls qml-module-qtquick-xmllistmodel qttools5-dev-tools qml-module-qtquick-dialogs qml-module-qt-labs-settings libqt5qml-graphicaleffects`

Build the GUI:

`./build.sh`

The build finished without error and as instructed I went to build/release/bin and ran the executable (monero-wallet-gui), resulting in the following error:

```
cd build/release/bin
./monero-wallet-gui
```

> app startd
> Qt:5.5.1 | screen: 1920x1080 - dpi: 96 - ratio:1.23591
> QQmlApplicationEngine failed to load component
> qrc:///main.qml:1811 Type DaemonConsole unavailable
> qrc:///components/DaemonConsole.qml:30 module "QtQuick.Controls" version 2.0 is not installed 
> 
> Error: no root objects

PS apols for formatting issues

# Discussion History
## pazos | 2018-05-04T08:04:58+00:00
you need to install qtquickcontrols2, but it shouldn't work because qt version < 5.7. Best option is install a newer qt and link against that version

## chrisfeigl | 2018-05-05T13:55:10+00:00
I had searched for Qt Quick Controls however I couldn't find anything on the [Qt Quick Controls 2 page](https://doc.qt.io/qt-5/qtquickcontrols2-index.html#prerequisites) which explained how to install it.

I installed qtquickcontrols2 using
`$sudo apt-get update`
`$sudo apt-get install qml-module-qtquick-controls`

No new packages were installed.

I ran a fresh build anyway and executed ./monero-wallet-gui with the following result:

```
app startd
Qt:5.5.1 | screen: 1920x1080 - dpi: 96 - ratio:1.23591
QQmlApplicationEngine failed to load component
qrc:///main.qml:1540 Type WizardMain unavailable
qrc:///wizard/WizardMain.qml:292 Type WizardDaemonSettings unavailable
qrc:///wizard/WizardDaemonSettings.qml:185 Type RemoteNodeEdit unavailable
qrc:///components/RemoteNodeEdit.qml:64 Type LineEdit unavailable
qrc:///components/LineEdit.qml:194 Type MoneroComponents.Input unavailable
qrc:///components/Input.qml:29 module "QtQuick.Controls" version 2.0 is not installed

Error: no root objects
```

## pazos | 2018-05-05T14:13:45+00:00
@chrisfeigl: I think my message should be more explicit.

Ubuntu 16.04 is not supported anymore. It doesn't have the minimum QT required by the application to run, which is QT 5.7.0. Official releases work because they ship qt bundled *inside* the application.

The are three things you can do: 
1) use official builds, don't try to build from source. 
2) upgrade your ubuntu box to -at least- ubuntu 17.10. 
3) download qt official releases for linux-x64 from [download.qt.io](http://download.qt.io/official_releases/qt/5.7/5.7.1/) and install it somewhere on your path. Use that qt version to link your program.

I don't suggest to try 3 if you don't understand what it means. The README should be updated to specify all those changes.


# Action History
- Created by: chrisfeigl | 2018-05-04T00:55:22+00:00
- Closed at: 2018-05-22T17:26:38+00:00
