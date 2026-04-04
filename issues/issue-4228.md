---
title: REDACTED FOR PRIVACY
source_url: https://github.com/monero-project/monero-gui/issues/4228
author: ghost
assignees: []
labels: []
created_at: '2023-10-14T09:07:50+00:00'
updated_at: '2023-11-16T08:09:51+00:00'
type: issue
status: closed
closed_at: '2023-11-16T08:09:51+00:00'
---

# Original Description
REDACTED FOR PRIVACY

# Discussion History
## selsta | 2023-10-14T13:37:57+00:00
Can you share the output of

```
brew info qt
```

and

```
brew info qt@5
```

and also which macOS version you use, which command you are using to build monero-gui and any other information that might be useful.

## selsta | 2023-10-14T14:16:47+00:00
@tobtoht found the issue, you have to uninstall qt6 for compilation to work. Easiest solution for now:

```
brew uninstall qt6
```

## Mike-Bou | 2023-10-15T07:40:18+00:00
It did compile, but app quit unexpectedly. Im using Monero Org new ARM version instead.

## selsta | 2023-10-15T09:04:36+00:00
You have to share a crash log, see Console.app

## Mike-Bou | 2023-10-15T09:33:14+00:00
￼

> On Oct 15, 2023, at 5:04 PM, selsta ***@***.***> wrote:
> 
> 
> You have to share a crash log, see Console.app
> 
> —
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/4228#issuecomment-1763328053>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AV4O6OJWIHOFUQKRV4FZGSDX7ORK7ANCNFSM6AAAAAA6AD2Z5I>.
> You are receiving this because you commented.
> 



## selsta | 2023-10-15T12:16:14+00:00
@Mike-Bou your comment is empty, it's best to share the log on paste.debian.net or similar site

## Mike-Bou | 2023-10-15T23:14:46+00:00
Posting 1295169 from @Mike-Bou for 24 hrs on paste.Debian.netSent from my iPhoneOn 15 Oct 2023, at 20:16, selsta ***@***.***> wrote:﻿
@Mike-Bou your comment is empty, it's best to share the log on paste.debian.net or similar site

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you were mentioned.Message ID: ***@***.***>

## selsta | 2023-10-15T23:17:23+00:00
@Mike-Bou It's trying to load libraries it doesn't find. Try to compile your own Qt instead of relying on the homebrew one

```
git clone https://github.com/qt/qt5.git
cd qt5
git checkout v5.15.9-lts-lgpl
./init-repository
mkdir build
cd build
../configure -prefix /Users/selsta/dev/qt-test/ -opensource -confirm-license -release -nomake examples -nomake tests -no-rpath -skip qtwebengine -skip qt3d -skip qtandroidextras -skip qtcanvas3d -skip qtcharts -skip qtconnectivity -skip qtdatavis3d -skip qtdoc -skip qtgamepad -skip qtlocation -skip qtnetworkauth -skip qtpurchasing -skip qtscript -skip qtscxml -skip qtsensors -skip qtserialbus -skip qtserialport -skip qtspeech -skip qttools -skip qtvirtualkeyboard -skip qtwayland -skip qtwebchannel -skip qtwebsockets -skip qtwebview -skip qtwinextras -skip qtx11extras -skip gamepad -skip serialbus -skip location -skip webengine
make
make install
cd ../qttools/src/linguist/lrelease
../../../../build/qtbase/bin/qmake
make
make install
cd ../../../../qttools/src/macdeployqt/macdeployqt/
../../../../build/qtbase/bin/qmake
make
make install
```

## Mike-Bou | 2023-10-17T04:23:25+00:00
the output of ../confgure was:
Info: creating super cache file /Users/mike/qt5/build/.qmake.super
Info: creating cache file /Users/mike/qt5/build/.qmake.cache
Info: creating stash file /Users/mike/qt5/build/.qmake.stash
Project ERROR: failed to parse default search paths from compiler output

> On Oct 16, 2023, at 7:17 AM, selsta ***@***.***> wrote:
> 
> ../configure -prefix /Users/selsta/dev/qt-test/ -opensource -confirm-license -release -nomake examples -nomake tests -no-rpath -skip qtwebengine -skip qt3d -skip qtandroidextras -skip qtcanvas3d -skip qtcharts -skip qtconnectivity -skip qtdatavis3d -skip qtdoc -skip qtgamepad -skip qtlocation -skip qtnetworkauth -skip qtpurchasing -skip qtscript -skip qtscxml -skip qtsensors -skip qtserialbus -skip qtserialport -skip qtspeech -skip qttools -skip qtvirtualkeyboard -skip qtwayland -skip qtwebchannel -skip qtwebsockets -skip qtwebview -skip qtwinextras -skip qtx11extras -skip gamepad -skip serialbus -skip location -skip webengine



## selsta | 2023-10-17T09:43:45+00:00
That's a Qt bug, you can apply this diff: https://raw.githubusercontent.com/Homebrew/formula-patches/086e8cf/qt5/qt5-qmake-xcode15.patch

# Action History
- Created by: ghost | 2023-10-14T09:07:50+00:00
- Closed at: 2023-11-16T08:09:51+00:00
