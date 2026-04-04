---
title: Move HTTP calls to C++
source_url: https://github.com/monero-project/monero-gui/issues/2254
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-07-03T15:30:10+00:00'
updated_at: '2020-04-22T21:08:55+00:00'
type: issue
status: closed
closed_at: '2020-04-22T21:08:55+00:00'
---

# Original Description
Currently [calling this](https://github.com/monero-project/monero-gui/blob/5f38dbb7dd3c25755427b103ae389ccc619b6c42/wizard/WizardController.qml#L566) from Javascript, should probably be done in C++ through our networkmanager for greater control over timeouts, not freeze the UI and also the ability to setup proxies.

https://github.com/monero-project/monero-gui/issues/2252

# Discussion History
## sanderfoobar | 2019-07-03T23:22:16+00:00
I'm actually not sure if Javascript HTTP calls freeze the UI. I would expect them to run async in their own interpreter.

## selsta | 2020-04-22T21:08:55+00:00
`src/qt/network.cpp`

# Action History
- Created by: sanderfoobar | 2019-07-03T15:30:10+00:00
- Closed at: 2020-04-22T21:08:55+00:00
