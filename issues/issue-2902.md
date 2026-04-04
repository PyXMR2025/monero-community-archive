---
title: '[security] Disable networking from QML?'
source_url: https://github.com/monero-project/monero-gui/issues/2902
author: jonathancross
assignees: []
labels: []
created_at: '2020-05-12T22:01:22+00:00'
updated_at: '2020-06-26T04:09:30+00:00'
type: issue
status: closed
closed_at: '2020-06-24T18:07:17+00:00'
---

# Original Description
We should consider disabling network access from QML (eg via [setNetworkAccessible](https://doc.qt.io/qt-5/qnetworkaccessmanager.html#setNetworkAccessible)) if possible.

RE: https://twitter.com/SarahJamieLewis/status/1260323514130694145

![qml-remote](https://user-images.githubusercontent.com/5115470/81749712-736c8900-94ac-11ea-9a4c-47bab9fbf2b1.jpg)

Although I have no indication this could be _remotely_ exploited, it's a defense-in-depth ("belt and suspenders") opportunity.

# Discussion History
## jonathancross | 2020-06-26T04:09:29+00:00
Thanks for fix @selsta !

# Action History
- Created by: jonathancross | 2020-05-12T22:01:22+00:00
- Closed at: 2020-06-24T18:07:17+00:00
