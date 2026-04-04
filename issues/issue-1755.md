---
title: full portable
source_url: https://github.com/monero-project/monero-gui/issues/1755
author: snipeTR
assignees: []
labels: []
created_at: '2018-11-28T01:08:40+00:00'
updated_at: '2021-04-13T23:43:02+00:00'
type: issue
status: closed
closed_at: '2021-04-13T23:43:02+00:00'
---

# Original Description
Please do not use the gui application registry.
Designed to be completely portable.
all settings can be stored in a settings.ini file.
Please take this proposal seriously.

# Discussion History
## sanderfoobar | 2018-11-28T01:26:13+00:00
I agree and AFAIK. is related to how `QSettings` is initialized with default configuration, which on Windows means [it uses the registry](http://doc.qt.io/qt-5/qsettings.html#details).

## selsta | 2021-04-13T23:43:01+00:00
GUI now has a portable mode.

# Action History
- Created by: snipeTR | 2018-11-28T01:08:40+00:00
- Closed at: 2021-04-13T23:43:02+00:00
