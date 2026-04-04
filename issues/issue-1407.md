---
title: some qml warnings
source_url: https://github.com/monero-project/monero-gui/issues/1407
author: pazos
assignees: []
labels:
- resolved
created_at: '2018-05-12T21:04:54+00:00'
updated_at: '2018-10-06T16:18:19+00:00'
type: issue
status: closed
closed_at: '2018-10-06T16:18:19+00:00'
---

# Original Description
These are warnings that don't break the gui. They should be fixed in the long run, but seems easy. Pinging @skftn 

Self-explanatory:
qrc:///main.qml:1317: ReferenceError: mainFlickable is not defined
qrc:///components/InputDialog.qml:68: ReferenceError: bg is not defined
qrc:///components/TitleBar.qml:70:9: QML Image: Cannot anchor to an item that isn't a parent or sibling.

Other:
file:///opt/qt/5.10.1/gcc_64/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth" **in components/DatePicker.qml**

qrc:///pages/Receive.qml:392: Error: Insufficient arguments (adding a new subaddress with o without a valid label)


# Discussion History
## sanderfoobar | 2018-07-15T23:36:12+00:00
Will fix them in #1511

## erciccione | 2018-10-06T16:01:24+00:00
+resolved

# Action History
- Created by: pazos | 2018-05-12T21:04:54+00:00
- Closed at: 2018-10-06T16:18:19+00:00
