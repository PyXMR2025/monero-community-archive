---
title: MoneroComponents.StandardDropdown should include labelText
source_url: https://github.com/monero-project/monero-gui/issues/2205
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-06-08T21:38:57+00:00'
updated_at: '2021-06-21T18:39:17+00:00'
type: issue
status: closed
closed_at: '2021-06-21T18:39:17+00:00'
---

# Original Description
QML API for the following 2 components: `lineEdit` and `lineEditMulti` both have a `labelText` property that functions as the label text, displayed above the aforementioned components.

`MoneroComponents.StandardDropdown` however, does not have a `labelText` property. If you want text above a `StandardDropdown`, it is necessary to include it within a `Layout.ColumnLayout` and use a `Text {}` field there.

Which results in PRs like this: https://github.com/monero-project/monero-gui/pull/2198

On-going effort for me is 'standardization' of our existing components in order to create an uniform API.

In addition, I believe our current dropdown component has some layout issues as observed here: https://github.com/monero-project/monero-gui/blob/68c7cf7276b8192ef800e3ab8fcc51815fb9c1cc/pages/settings/SettingsLayout.qml#L193

The layout of the language picker dropdown box is wrong.

Another example below.

https://github.com/monero-project/monero-gui/blob/68c7cf7276b8192ef800e3ab8fcc51815fb9c1cc/pages/Transfer.qml#L184-L220

Which, ideally, would be rewritten to:

```QML
         MoneroComponents.StandardDropdown { 
             Layout.fillWidth: true 
             labelText: qsTr("Transaction priority") + translationManager.emptyString
             id: priorityDropdown 
             Layout.topMargin: 5 
             currentIndex: 0 
         } 
```

# Discussion History
## selsta | 2019-06-14T21:40:10+00:00
> In addition, I believe our current dropdown component has some layout issues as observed here:

Can you make a screenshot of the layout issue?

# Action History
- Created by: sanderfoobar | 2019-06-08T21:38:57+00:00
- Closed at: 2021-06-21T18:39:17+00:00
