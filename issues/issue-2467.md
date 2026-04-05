---
title: Is it possible to start xmrig without a terminal session starting?
source_url: https://github.com/xmrig/xmrig/issues/2467
author: Joe23232
assignees: []
labels: []
created_at: '2021-07-01T10:22:08+00:00'
updated_at: '2021-08-23T08:26:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Is it possible to start xmrig without a terminal session starting and it continues to mine?

# Discussion History
## Lonnegan | 2021-07-01T12:36:14+00:00
change background: false to true in the config.json. So the window will disapear after starting xmrig.

## Joe23232 | 2021-07-01T13:07:07+00:00
Thanks mate :)

## Thepowa753 | 2021-08-23T08:25:21+00:00
I found this (will prevent also the startup terminal flash):
[https://stackoverflow.com/questions/1283721/disable-showing-console-window/1283823](https://stackoverflow.com/questions/1283721/disable-showing-console-window/1283823)
and this:
[https://stackoverflow.com/questions/2139637/hide-console-of-windows-application](https://stackoverflow.com/questions/2139637/hide-console-of-windows-application)

I'll try and edit this comment if it works

# Action History
- Created by: Joe23232 | 2021-07-01T10:22:08+00:00
