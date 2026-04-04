---
title: Readme Qt installation doesn't list Debian dependencies
source_url: https://github.com/monero-project/monero-gui/issues/4053
author: 2l47
assignees: []
labels: []
created_at: '2022-10-24T17:21:59+00:00'
updated_at: '2022-12-02T05:44:51+00:00'
type: issue
status: closed
closed_at: '2022-12-02T05:44:51+00:00'
---

# Original Description
I had no errors building, but couldn't start the GUI until I installed `qml-module-qt-labs-platform`:
```
W QQmlApplicationEngine failed to load component
W qrc:/main.qml:2378:5: Type MoneroComponents.MenuBar unavailable
W qrc:/components/MenuBar.qml:29:1: module "Qt.labs.platform" is not installed
E Error: no root objects
```

Debian 11.5 does not offer the `qt5-default` package, but all others listed under the Ubuntu dependencies in the "Install Qt" section are available, and on my machine were already installed (with the exception of `qml-module-qt-labs-platform`).

`qt5-default` is an Ubuntu-specific metapackage: https://packages.ubuntu.com/focal/qt5-default
Thus, I would suggest replacing it with `qtbase5-dev qtchooser` (both of which are available on Debian) and changing the section header to "For Debian distributions (Debian, Ubuntu, Mint, Tails...)" as in the "Install Monero dependencies" section.

# Discussion History
# Action History
- Created by: 2l47 | 2022-10-24T17:21:59+00:00
- Closed at: 2022-12-02T05:44:51+00:00
