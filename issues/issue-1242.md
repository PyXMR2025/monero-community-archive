---
title: Can't launch v0.12.0.0 on Ubuntu
source_url: https://github.com/monero-project/monero-gui/issues/1242
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2018-04-02T22:24:43+00:00'
updated_at: '2018-04-19T19:27:20+00:00'
type: issue
status: closed
closed_at: '2018-04-19T19:27:20+00:00'
---

# Original Description
GUI_VERSION = "v0.12.0.0"
Ubunutu - 17.10

When opening monero-wallet-gui, this **error occurs** (and the GUI is ofc not launched)
"
_QQmlApplicationEngine failed to load component
qrc:///main.qml:1043 Type StandardDialog unavailable
qrc:///components/StandardDialog.qml:30 module "QtQuick.Controls" version 2.0 is not installed
Error: no root objects_
"
Could be that this #1240 is causing it, after some [research](https://stackoverflow.com/questions/22389605/module-qtquick-controls-is-not-installed-error-on-ubuntu-14-04) (aka quick duckduckgo search) - the issue can be that Ubuntu has also a older version of QT(5.0.2) which is first found when the program is launched - and it fails (even when the correct version is present in the system)

Don't know a easy way to fix this, probably there is a workaround, but I assume we don't really want people to remove some parts of ubuntu for installing a monero-gui build


# Discussion History
## pazos | 2018-04-02T22:35:01+00:00
From [reddit/r/monero](https://www.reddit.com/r/Monero/comments/892vlr/lithium_luna_gui_released/dwordse/)

`sudo apt qml-module-qtquick-controls2`

For ubuntu 17.10

## sanderfoobar | 2018-04-02T22:48:08+00:00
Must also be Qt 5.7+

## 1337tester | 2018-04-03T18:09:57+00:00
thanks alot, worked, the command is btw:

sudo apt install qml-module-qtquick-controls2

Creating a PR for updating this new dependency in README.md

## ghost | 2018-04-13T16:05:08+00:00
For Ubuntu 16.04LTS, this doesn't work:

> sudo apt-get install qml-module-qtquick-controls2

As @skftn commented, the version must be higher, but that one is not available. You have to manually install it.

## 1337tester | 2018-04-19T16:38:53+00:00
can be closed

## sanderfoobar | 2018-04-19T19:24:53+00:00
+resolved

# Action History
- Created by: 1337tester | 2018-04-02T22:24:43+00:00
- Closed at: 2018-04-19T19:27:20+00:00
