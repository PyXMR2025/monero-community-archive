---
title: Documentation | Installation for ubuntu 18.04 x64
source_url: https://github.com/monero-project/monero-gui/issues/1405
author: SamueLacmene
assignees: []
labels: []
created_at: '2018-05-12T18:45:30+00:00'
updated_at: '2018-05-25T18:09:20+00:00'
type: issue
status: closed
closed_at: '2018-05-25T18:09:20+00:00'
---

# Original Description
In order to build the monero-gui under Ubuntu 18.04, following UI dependencies are needed:

sudo apt install qtbase5-dev qt5-default qtdeclarative5-dev qml-module-qtquick-controls qml-module-qtquick-xmllistmodel qttools5-dev-tools qml-module-qtquick-dialogs qml-module-qt-labs-settings **qml-module-qtquick-controls2 qml-module-qt-labs-settings qml-module-qt-labs-folderlistmodel**


# Discussion History
## pazos | 2018-05-12T21:10:00+00:00
Thanks. The same dependencies are required for Ubuntu 17.10.

We should update instructions for debian distros since we require Qt5.7 and Ubuntu 16.04 & distros based on it (like linux mint 18.x) doesn't have that version.  

# Action History
- Created by: SamueLacmene | 2018-05-12T18:45:30+00:00
- Closed at: 2018-05-25T18:09:20+00:00
