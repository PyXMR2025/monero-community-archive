---
title: StandardDropdown is not Scrollable
source_url: https://github.com/monero-project/monero-gui/issues/3864
author: elibroftw
assignees: []
labels: []
created_at: '2022-03-15T20:19:11+00:00'
updated_at: '2022-03-15T20:33:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If there are more items than the dropdown can fit in its popup,
the extra items simply get clipped and the user won't be able to scroll to those items.
![image](https://user-images.githubusercontent.com/21298211/158464265-fe7aa4ad-9841-43d7-8c79-84e3741a456e.png)
I spent an hour trying to fiddle with adding Flickable and Scrollviews before and after the Rectange in StandardDropdown.qml, but to no avail. Someone more experienced at QML can have a go.

This problem blocks #3852 

# Discussion History
# Action History
- Created by: elibroftw | 2022-03-15T20:19:11+00:00
