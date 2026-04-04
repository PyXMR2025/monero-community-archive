---
title: ··
source_url: https://github.com/monero-project/monero-gui/issues/2239
author: maogo
assignees: []
labels: []
created_at: '2019-06-30T06:37:10+00:00'
updated_at: '2019-07-24T03:59:28+00:00'
type: issue
status: closed
closed_at: '2019-07-01T06:16:51+00:00'
---

# Original Description
 

# Discussion History
## selsta | 2019-06-30T06:37:57+00:00
When is the 4-5 seconds delay happening?

## selsta | 2019-06-30T06:50:27+00:00
It takes ~4.5 seconds on a 2014 MacBook Pro from double clicking the .app until the GUI is fully loaded.

Should be faster with your specs.

## selsta | 2019-06-30T07:27:17+00:00
Can you compare it to v0.14.0.0? Did it get slower?

## selsta | 2019-07-01T05:58:23+00:00
We are using Qt/QML, which is slow on startup compared to pure C++ programs. Not a lot we can do about this. https://blog.qt.io/blog/2019/01/11/qt-5-12-lts-road-faster-qml-application-startup/ has some suggestions.

# Action History
- Created by: maogo | 2019-06-30T06:37:10+00:00
- Closed at: 2019-07-01T06:16:51+00:00
