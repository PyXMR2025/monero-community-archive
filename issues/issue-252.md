---
title: GUI styling is broken in compact mode
source_url: https://github.com/monero-project/monero-gui/issues/252
author: ghost
assignees: []
labels: []
created_at: '2016-12-09T02:37:52+00:00'
updated_at: '2016-12-14T21:32:24+00:00'
type: issue
status: closed
closed_at: '2016-12-14T21:32:24+00:00'
---

# Original Description
Tool may work fine, but I think messing with the title bar messed up some stuff. 

See: https://i.imgur.com/ht6LEif.png

# Discussion History
## ghost | 2016-12-09T06:50:04+00:00
This is on OSX 10.12.1

## M5M400 | 2016-12-09T14:17:07+00:00
confirmed on ubuntu 16.04 x64 on ff998ba

Also I have standard window decorations now *sigh*

![screenshot from 2016-12-09 15-15-57](https://cloud.githubusercontent.com/assets/22886679/21051856/669307f4-be22-11e6-963b-01b8e1e9ed8b.png)

![screenshot from 2016-12-09 15-15-44](https://cloud.githubusercontent.com/assets/22886679/21051862/6a8d9720-be22-11e6-8157-d4c29a124ab3.png)


## moneromooo-monero | 2016-12-09T19:50:58+00:00
Broken by https://github.com/monero-project/monero-core/pull/238/commits/17add2d75e36b5f9f224d2234db55dc9c68f7fee, but I don't know what this fixed in the first place, so I don't want to revert this right now.

## M5M400 | 2016-12-14T08:57:48+00:00
how is this closed if it's not merged to master yet?

## ghost | 2016-12-14T17:17:52+00:00
Good point. I'll keep it open for now.

# Action History
- Created by: ghost | 2016-12-09T02:37:52+00:00
- Closed at: 2016-12-14T21:32:24+00:00
