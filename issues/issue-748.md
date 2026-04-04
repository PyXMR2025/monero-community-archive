---
title: GUI Beta 2, Windows, Menu glitch
source_url: https://github.com/monero-project/monero-gui/issues/748
author: tschauner-s
assignees: []
labels:
- bug
- enhancement
- resolved
created_at: '2017-05-25T21:39:17+00:00'
updated_at: '2018-11-18T16:36:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T16:36:32+00:00'
---

# Original Description
**This issue is only reproducible in low graphics mode.**

When clicking on "Advanced" in the menu, the sub-menu opens correctly:
![guiglitch1](https://cloud.githubusercontent.com/assets/1774712/26471633/b170e134-41a2-11e7-9ba3-1ae648ce0e29.jpg)

When switching to any other menu option afterwards, some small amount of text is glitching just below the letters of "Advanced":
![guiglitch2](https://cloud.githubusercontent.com/assets/1774712/26471632/b16d5046-41a2-11e7-9882-012cbf82bfe6.jpg)
The text fragments look like the lower portions of the sub-menu items.


# Discussion History
## romenoo | 2017-06-01T14:23:14+00:00
not the same issue but unless I go full screen, Settings and Network status overlaps when on the Advanced menu

screen size: 1366x768

![monero](https://cloud.githubusercontent.com/assets/29124329/26684021/57fc93c2-46d5-11e7-88ee-a973977466dd.png)

## romenoo | 2017-06-01T17:43:14+00:00
Similarly the buttons under the advanced options when sending monero is not visible and not scrollable unless I maximize the window

![monero](https://cloud.githubusercontent.com/assets/29124329/26692871/c3c713e0-46f1-11e7-8070-e981d3c05140.PNG)


## medusadigital | 2017-08-07T19:46:56+00:00
can confirm on windows.

+enhancement  

## basjoe | 2017-10-27T08:58:16+00:00
Issue has overlap with https://github.com/monero-project/monero-core/issues/349

## sanderfoobar | 2018-03-30T01:57:35+00:00
+bug

## erciccione | 2018-11-18T13:40:28+00:00
+resolved

# Action History
- Created by: tschauner-s | 2017-05-25T21:39:17+00:00
- Closed at: 2018-11-18T16:36:32+00:00
