---
title: Issue with GUI resizing/snapping on Windows
source_url: https://github.com/monero-project/monero/issues/1891
author: philkode
assignees: []
labels: []
created_at: '2017-03-19T04:44:47+00:00'
updated_at: '2017-03-19T22:42:25+00:00'
type: issue
status: closed
closed_at: '2017-03-19T22:42:25+00:00'
---

# Original Description
The way the Windows QT borderless display works is a bit broken, in that it doesn't play nice with Windows compositor (can't be scaled to 1/2 screen by dragging to the edge of the screen or using Windows+arrow keys as per most Windows apps). It's a shame because the flat GUI looks very much at home on Windows 10 and could easily be mistaken for a Metro app if it behaved like all other Windows apps.

I found a post on StackOverflow referring to a similar issue with QT & Windows Vista's Aero compositor. An example solution was recently posted here: https://github.com/dfct/TrueFramelessWindow , not sure if this will be an applicable route for the XMR GUI but seemed to work in that instance.


# Discussion History
## iDunk5400 | 2017-03-19T11:37:22+00:00
Wrong repo. You probably wanted to post here: [https://github.com/monero-project/monero-core/issues](url)

## philkode | 2017-03-19T22:42:25+00:00
Yes, yes I did. Thanks.

# Action History
- Created by: philkode | 2017-03-19T04:44:47+00:00
- Closed at: 2017-03-19T22:42:25+00:00
