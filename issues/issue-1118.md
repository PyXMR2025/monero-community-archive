---
title: 'Duplicate/collision of symbol: qsTr("D") in LeftPanel.qml'
source_url: https://github.com/monero-project/monero-gui/issues/1118
author: ordtrogen
assignees: []
labels:
- resolved
created_at: '2018-02-14T21:12:01+00:00'
updated_at: '2018-12-17T11:27:29+00:00'
type: issue
status: closed
closed_at: '2018-12-17T11:27:29+00:00'
---

# Original Description
Problem: String "Dashboard" does not appear for localization in monero-core.ts

This may be the cause:

LeftPanel.qml rows 268+269:

                text: qsTr("Dashboard") + translationManager.emptyString
                symbol: qsTr("D") + translationManager.emptyString

LeftPanel.qml rows 392+393:

                text: qsTr("Advanced") + translationManager.emptyString
                symbol: qsTr("D") + translationManager.emptyString

Only the second pair "Advanced"/"D" appears for localization in monero-core.ts.  I'm guessing the second pair "overrides" the first when localizable strings files are generated.





# Discussion History
## mmbyday | 2018-12-17T08:52:34+00:00
Dashboard was not active since June 2016. It's commented out. Nothing to worry about here. Thanks.
https://github.com/monero-project/monero-gui/commit/17f38a930e33c25392dd565f484009e5eddba56a

+resolved 

## erciccione | 2018-12-17T11:16:28+00:00
+resolved

# Action History
- Created by: ordtrogen | 2018-02-14T21:12:01+00:00
- Closed at: 2018-12-17T11:27:29+00:00
