---
title: GUI window keeps jumping into focus when it logs out automatically
source_url: https://github.com/monero-project/monero-gui/issues/2054
author: apertamono
assignees: []
labels: []
created_at: '2019-04-05T11:13:23+00:00'
updated_at: '2019-04-16T20:49:37+00:00'
type: issue
status: closed
closed_at: '2019-04-16T20:49:37+00:00'
---

# Original Description
There's a weird issue with the GUI which makes it annoying to keep it opened: when it logs me out of the wallet, it jumps into focus and asks me to enter my password. When I try to minimize it, it jumps back into view immediately.

The only way to minimize it is using Windows+M to minimize all windows. But then it returns in the same way after the period set for logging out.

GUI version: 14.0.0 x64 binaries. I use an old wallet, but I removed all files from C:\ProgramData\Monero and did a clean install of the client software.
OS: 64-bits Windows 10.
Expected behavior: log out of the wallet silently and keep the window minimized.

Video: https://imgur.com/0H3zVvt

# Discussion History
## sanderfoobar | 2019-04-08T01:51:06+00:00
Possibly need to use `focus()` instead of `forceActiveFocus()`:

https://github.com/monero-project/monero-gui/blob/19c2208dc447ccb5ba9ff990cbdd6ecf6b96f23d/components/PasswordDialog.qml#L62

https://doc.qt.io/qt-5/qml-qtquick-item.html#focus-prop

# Action History
- Created by: apertamono | 2019-04-05T11:13:23+00:00
- Closed at: 2019-04-16T20:49:37+00:00
