---
title: Cannot run gui builded from source code on windows
source_url: https://github.com/monero-project/monero-gui/issues/3021
author: CharikovAI
assignees: []
labels: []
created_at: '2020-07-23T08:36:06+00:00'
updated_at: '2020-08-26T23:19:52+00:00'
type: issue
status: closed
closed_at: '2020-08-26T23:09:34+00:00'
---

# Original Description
I built the project from the source code using the instructions. I've installed 
`pacman -S mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake mingw-w64-x86_64-boost mingw-w64-x86_64-openssl mingw-w64-x86_64-zeromq mingw-w64-x86_64-libsodium mingw-w64-x86_64-hidapi mingw-w64-x86_64-protobuf-c mingw-w64-x86_64-libusb mingw-w64-x86_64-libgcrypt`

I've tried both `source ./build.sh release-static` and just `./build.sh`.

Still the `monero-gui` doesn't start. I got the system error that some libraries (libprotobuf.dll, libhidapi-0.dll, Qt5Core.dll, Qt5Gui.dll) are missing. The `monerod` starts well.

Qt version is 5.15.0-1

Any help?

# Discussion History
## xiphon | 2020-07-23T13:04:51+00:00
Did you stop on `build.sh` step? If so, there is some additional step required afterwards, have a look at the manual.

## CharikovAI | 2020-07-23T13:48:30+00:00
In the case of question - yes, I stopped on `build.sh` step

If I tried 
`cd build && make deploy`
I faced that:
`windeployqt C:/msys64/home/asus/monero-gui/build/release/bin/monero-wallet-gui.exe -release -no-translations -qmldir=C:/msys64/home/asus/monero-gui
C:\msys64\home\asus\monero-gui\build\release\bin\monero-wallet-gui.exe 64 bit, release executable [QML]
Scanning C:\msys64\home\asus\monero-gui:
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
  'QtQuick.Extras.Private' C:\msys64\mingw64\share\qt5\qml\QtQuick\Extras\Private
  'QtQuick.Extras' C:\msys64\mingw64\share\qt5\qml\QtQuick\Extras
  'QtQuick.Controls.Fusion' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Fusion
  'QtQuick.Controls.Imagine' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Imagine
  'QtQuick.Controls.Material' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Material
  'QtQuick.Controls.Universal' C:\msys64\mingw64\share\qt5\qml\QtQuick\Controls.2\Universal
  'QtQml.Models' C:\msys64\mingw64\share\qt5\qml\QtQml\Models.2
Direct dependencies: Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5Widgets
All dependencies   : Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5Widgets
To be deployed     : Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5Widgets
Unable to find the platform plugin.
make: *** [Makefile:507: deploy] Error 1
`

## selsta | 2020-08-26T23:09:34+00:00
Will be fixed with #3047

Edit: Sorry for closing early, should be merged in the next days.

# Action History
- Created by: CharikovAI | 2020-07-23T08:36:06+00:00
- Closed at: 2020-08-26T23:09:34+00:00
