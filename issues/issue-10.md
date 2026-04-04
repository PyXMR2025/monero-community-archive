---
title: qmake - error
source_url: https://github.com/monero-project/monero-gui/issues/10
author: thewurx
assignees: []
labels: []
created_at: '2016-09-02T11:32:02+00:00'
updated_at: '2016-11-01T08:25:18+00:00'
type: issue
status: closed
closed_at: '2016-11-01T08:25:18+00:00'
---

# Original Description
Hi Guys,

Firstly. Thanks for the great work. 

Error I get is with qmake:

**qmake: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/qmake': No such file or directory**

Followed instructions for the Linux Mint 18 64bit package. Running on Asus X554L machine. Core i3 4GB Ram. (Same issue on my tower Core i3 8GB Ram Linux Mint 18)

edit: the folder /usr/lib/x86_64-linux-gnu/qt4/bin/ exists. No qmake file in the directory. Only a qdbus file in the said directory.

Tired: sudo apt-get install qt4-qmake libqt4-dev

New error:

**qmake
/home/######/monero-core/monero-core.pro:146: Unknown replace function: shell_path
Project MESSAGE: Warning: unknown QT: qml**

Also tried:apt-get update && upgrade     no luck


# Discussion History
## mbg033 | 2016-09-05T10:57:38+00:00
Hi, seems you installed qt4 but it needs to be qt5.  If you followed README already, you probably need to setup default Qt version. On Ubuntu (same for Mint I guess)  it can be done with qtchooser package


## medusadigital | 2016-11-01T06:18:53+00:00
can be closed


# Action History
- Created by: thewurx | 2016-09-02T11:32:02+00:00
- Closed at: 2016-11-01T08:25:18+00:00
