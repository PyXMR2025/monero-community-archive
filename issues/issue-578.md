---
title: Issue with GUI resizing/snapping on Windows
source_url: https://github.com/monero-project/monero-gui/issues/578
author: philkode
assignees: []
labels:
- enhancement
created_at: '2017-03-19T22:45:19+00:00'
updated_at: '2019-07-17T21:27:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The way the Windows QT borderless display works is a bit broken, in that it doesn't play nice with Windows compositor (can't be scaled to 1/2 screen by dragging to the edge of the screen or using Windows key+arrow keys as per most Windows apps). It's a shame because the flat GUI looks very much at home on Windows 10 and could easily be mistaken for a Metro app if it behaved like all other Windows programs.

I found a post on StackOverflow referring to a similar issue with QT & Windows Vista's Aero compositor. An example solution was recently posted here: https://github.com/dfct/TrueFramelessWindow , not sure if this will be an applicable route for the XMR GUI but seemed to work in that instance.

# Discussion History
## sanderfoobar | 2018-12-18T10:08:24+00:00
+enhancement

## selsta | 2019-07-16T17:20:07+00:00
Disable “Custom decorations” in Settings -> Interface.

+resolved

## selsta | 2019-07-17T21:26:14+00:00
Sorry I didn’t see that you linked a plugin. I’ll leave this open to add this for frameless windows.

-resolved

# Action History
- Created by: philkode | 2017-03-19T22:45:19+00:00
