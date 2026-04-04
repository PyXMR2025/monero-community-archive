---
title: Navigation menu horizontal artifacts
source_url: https://github.com/monero-project/monero-gui/issues/166
author: peronero
assignees: []
labels: []
created_at: '2016-11-15T00:50:17+00:00'
updated_at: '2016-11-26T04:36:37+00:00'
type: issue
status: closed
closed_at: '2016-11-26T04:36:37+00:00'
---

# Original Description
I'm seeing horizontal lines that appear below only the Transfer  after Verify Payment tabs after being on those those tabs and then moving onto another tab. They do not disappear afterwards.

Steps to reproduce:

1. Open monero-core (Transfer is selected by default)
2. Select another tab  - the horizontal line below Transfer will now appear

Also occurs after selecting the Verify Payments tab and moving to another tab - see screenshot.

![screenshot from 2016-11-14 19-45-08](https://cloud.githubusercontent.com/assets/22800288/20288669/eeb52c2c-aaa2-11e6-9bf6-527149813486.png)

Tumbleweed with GNOME.


# Discussion History
## ghost | 2016-11-15T17:26:34+00:00
I've noticed this too


## iDunk5400 | 2016-11-15T20:41:19+00:00
I suppose it is these two separators that bother you.

https://github.com/monero-project/monero-core/blob/master/LeftPanel.qml#L241-L247
https://github.com/monero-project/monero-core/blob/master/LeftPanel.qml#L279-L285


## ghost | 2016-11-16T18:53:42+00:00
@iDunk5400 I don't think it's the separators themselves that are the problem. Moreso that they come and go sporadically, or at least, that's my experience.


## Jaqueeee | 2016-11-23T19:08:30+00:00
Fixed in https://github.com/monero-project/monero-core/issues/195

## peronero | 2016-11-26T04:36:33+00:00
Confirmed fixed.

# Action History
- Created by: peronero | 2016-11-15T00:50:17+00:00
- Closed at: 2016-11-26T04:36:37+00:00
