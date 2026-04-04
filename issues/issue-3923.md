---
title: '[Gentoo] - Build succeeds but program launch fails with missing module'
source_url: https://github.com/monero-project/monero-gui/issues/3923
author: Slips-PC
assignees: []
labels: []
created_at: '2022-05-15T00:45:17+00:00'
updated_at: '2022-05-15T00:59:38+00:00'
type: issue
status: closed
closed_at: '2022-05-15T00:59:38+00:00'
---

# Original Description
As the title states, I'm building on a gentoo system and the compilation seems to go okay, but trying to run monero-wallet-gui leaves me with the following error:
```
2022-05-15 00:42:15.652	W libunbound was not built with threads enabled - crashes may occur
2022-05-15 00:42:15.652	W Qt:5.15.3 GUI:- | screen: 1920x1080 - available: QSize(1920, 1080) - dpi: 96.316 - ratio:0.637479
2022-05-15 00:42:15.786	W QQmlApplicationEngine failed to load component
2022-05-15 00:42:15.786	W qrc:/main.qml:2387:5: Type MoneroComponents.LanguageSidebar unavailable
2022-05-15 00:42:15.786	W qrc:/components/LanguageSidebar.qml:32:1: module "QtQuick.XmlListModel" is not installed
2022-05-15 00:42:15.786	E Error: no root objects
```
Unsure where to go from here. 

# Discussion History
## Slips-PC | 2022-05-15T00:59:38+00:00
UPDATE: so, i did some searching about the name of the missing module in question, and i discovered a similar issue people had with other software, which led me to the package `dev-qt/qtxmlpatterns`. Sure enough, installing it fixed my error.

Tl;Dr for people looking for the answer to this question: emerge `dev-qt/qtxmlpatterns`

# Action History
- Created by: Slips-PC | 2022-05-15T00:45:17+00:00
- Closed at: 2022-05-15T00:59:38+00:00
