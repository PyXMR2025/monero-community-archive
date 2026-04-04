---
title: Invalid address format in CLI output on launch
source_url: https://github.com/monero-project/monero-gui/issues/211
author: sammy007
assignees: []
labels: []
created_at: '2016-11-26T16:14:17+00:00'
updated_at: '2017-03-29T21:21:49+00:00'
type: issue
status: closed
closed_at: '2017-03-29T21:21:49+00:00'
---

# Original Description
Version: `26abdee5c47017a80117b1bed5ee36586a240c62`
OS: OSX, qt5: stable 5.7.0 (bottled), HEAD [keg-only]

```
app startd
qrc:///MiddlePanel.qml:259:9: QML StackView: Cannot anchor to an item that isn't a parent or sibling.
2016-Nov-26 18:09:50.460876 Invalid address format
2016-Nov-26 18:09:50.460996 Invalid address format
2016-Nov-26 18:09:50.465505 Invalid address format
```

Starting with empty `~/Monero` directory.
I believe something is wrong with it.

# Discussion History
## moneromooo-monero | 2016-11-26T18:34:38+00:00
It starts on the "send" page, so looks whether the send widget has a valid address (and it doesn't, it's empty). That message could be removed though.

## ghost | 2017-03-29T03:56:39+00:00
@sammy007 Can this issue be closed?

# Action History
- Created by: sammy007 | 2016-11-26T16:14:17+00:00
- Closed at: 2017-03-29T21:21:49+00:00
