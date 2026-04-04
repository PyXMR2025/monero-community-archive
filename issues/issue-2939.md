---
title: 'Deploy MSYS2 Unable to find the platform plugin '
source_url: https://github.com/monero-project/monero-gui/issues/2939
author: bymagnum
assignees: []
labels: []
created_at: '2020-06-09T16:33:34+00:00'
updated_at: '2020-06-10T18:19:52+00:00'
type: issue
status: closed
closed_at: '2020-06-10T18:18:29+00:00'
---

# Original Description
Assembly:
Windows 10
MSYS2
MinGW-w64-x86_64 compiler with-qt5 5.15.0-1 (using MinGW-w64-x86_64-Qt architecture using MinGW-w64-x86_64-qt5 architecture)
QMake version 3.1


MINGW64 ~/monero-gui/build
$ make deploy
windeployqt C:/msys64/home/pavel/monero-gui/build/release/bin/monero-wallet-gui.exe -release -no-translations -qmldir=C:/msys64/home/pavel/monero-gui
C:\msys64\home\pavel\monero-gui\build\release\bin\monero-wallet-gui.exe 64 bit, release executable [QML]
Scanning C:\msys64\home\pavel\monero-gui:
QML imports:
'QtQuick' C:\msys64\mingw64\share\qt5\qml\QtQuick.2
'QtQuick.Layouts' C:\msys64\mingw64\share\qt5\qml\QtQuick\Layouts
'QtGraphicalEffects' C:\msys64\mingw64\share\qt5\qml\QtGraphicalEffects
'QtGraphicalEffects/private' C:\msys64\mingw64\share\qt5\qml\QtGraphicalEffects\private
'QtQuick.Window' C:\msys64\mingw64\share\qt5\qml\QtQuick\Window.2
'QtQuick.Controls' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls
'QtQuick.Controls.Styles' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls\Styles
'QtQuick.Dialogs' C:\msys64\mingw64\share\qt5\qml\QtQuick\Dialogs
'QtQml' C:\msys64\mingw64\share\qt5\qml\QtQml
'Qt.labs.folderlistmodel' C:\msys64\mingw64\share\qt5\qml\Qt\labs\folderlistmodel
'Qt.labs.settings' C:\msys64\mingw64\share\qt5\qml\Qt\labs\settings
'QtQuick.Dialogs.Private' C:\msys64\mingw64\share\qt5\qml\QtQuick\Dialogs\Private
'QtQuick.PrivateWidgets' C:\msys64\mingw64\share\qt5\qml\QtQuick\PrivateWidgets
'QtQuick.Controls' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2
'QtQuick.Templates' C:\msys64\mingw64\share\qt5\qml\QtQuick\Templates.2
'QtQuick.XmlListModel' C:\msys64\mingw64\share\qt5\qml\QtQuick\XmlListModel
'QtMultimedia' C:\msys64\mingw64\share\qt5\qml\QtMultimedia
'QtQuick.Controls.Private' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls\Private
'QtQml.Models' C:\msys64\mingw64\share\qt5\qml\QtQml\Models.2
'QtQuick.Extras.Private' C:\msys64\mingw64\share\qt5\qml\QtQuick\Extras\Private
'QtQuick.Extras' C:\msys64\mingw64\share\qt5\qml\QtQuick\Extras
'QtQuick.Controls.Fusion' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Fusion
'QtQuick.Controls.Imagine' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Imagine
'QtQuick.Controls.Material' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Material
'QtQuick.Controls.Universal' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Universal
Direct dependencies: Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5Widgets
All dependencies : Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5Widgets
To be deployed : Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5Widgets
Unable to find the platform plugin.
make: *** [Makefile:507: deploy] Error 1


What could be the error?

# Discussion History
## bymagnum | 2020-06-09T20:37:57+00:00
1. qt >5.14.0 no longer needs to specify --release and --debug

https://bugreports.qt.io/browse/QTBUG-84567?focusedCommentId=514306&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-514306

monero-wallet-gui.pro delete -release 

https://github.com/monero-project/monero-gui/blob/c8f4355e15e6574c7139bfb5f6ea195ad4199644/monero-wallet-gui.pro#L537

2. MSYS2 installs the ICU *67.dll

fix windeploy_helper.sh all DLLs 65 - > 67 

https://github.com/monero-project/monero-gui/blob/c8f4355e15e6574c7139bfb5f6ea195ad4199644/windeploy_helper.sh#L20

https://github.com/monero-project/monero-gui/blob/c8f4355e15e6574c7139bfb5f6ea195ad4199644/windeploy_helper.sh#L23

## selsta | 2020-06-10T18:19:52+00:00
@bymagnum Thank you, I PRed the 65 -> 67 change. The release flag can be removed later, didn’t look into it yet.

# Action History
- Created by: bymagnum | 2020-06-09T16:33:34+00:00
- Closed at: 2020-06-10T18:18:29+00:00
