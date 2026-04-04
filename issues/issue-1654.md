---
title: Report monero-gui version to stdout
source_url: https://github.com/monero-project/monero-gui/issues/1654
author: sanderfoobar
assignees: []
labels:
- Hacktoberfest
created_at: '2018-10-15T11:10:45+00:00'
updated_at: '2018-11-18T05:58:49+00:00'
type: issue
status: closed
closed_at: '2018-11-18T05:58:49+00:00'
---

# Original Description
Upon startup, the application could output the monero-gui version to stdout as `WARN`. People often post logs to debug problems and to be able to see their version would be beneficial.

In QML the variable is exposed as `Version.GUI_VERSION`:
https://github.com/monero-project/monero-gui/blob/a9fa808dd136f6e95b81badb76dfcee5c18d7a1f/pages/settings/SettingsInfo.qml#L275

Should probably output somewhere around here:

https://github.com/monero-project/monero-gui/blob/7adeb694c17511ffcb1d3d0c0038f5f8b8684a5f/main.cpp#L143-L145

# Discussion History
## sanderfoobar | 2018-10-15T13:33:58+00:00
+hacktoberfest

## pazos | 2018-10-15T16:08:48+00:00
Somewhat related to #1578. We need to define a version in qmake and export that to qml. An automated version would be better than a manual one.

## sanderfoobar | 2018-10-16T00:16:49+00:00
@pazos I thought perhaps it would be best to read the version file the same way QML does it; via the resource system. Let me know what you think of the PR (probably some C++ style issues).

# Action History
- Created by: sanderfoobar | 2018-10-15T11:10:45+00:00
- Closed at: 2018-11-18T05:58:49+00:00
