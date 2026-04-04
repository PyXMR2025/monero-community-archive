---
title: win64 Buildbot builds - "QtQuick" version 2.9 is not installed
source_url: https://github.com/monero-project/monero-gui/issues/2151
author: mmbyday
assignees: []
labels: []
created_at: '2019-05-02T19:38:38+00:00'
updated_at: '2019-05-24T20:53:52+00:00'
type: issue
status: closed
closed_at: '2019-05-24T20:53:52+00:00'
---

# Original Description
```
WARNING	frontend	src/wallet/api/wallet.cpp:410	QQmlApplicationEngine failed to load component
WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///main.qml:29 module "QtQuick" version 2.9 is not installed
```

# Discussion History
## sanderfoobar | 2019-05-03T02:05:53+00:00
Win64 buildbot not migrated to 5.9.7 yet.

## mmbyday | 2019-05-24T20:53:52+00:00
Buildbot appears to have been upgraded to 5.9.7.

# Action History
- Created by: mmbyday | 2019-05-02T19:38:38+00:00
- Closed at: 2019-05-24T20:53:52+00:00
