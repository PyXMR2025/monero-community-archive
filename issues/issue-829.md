---
title: MacOS GUI turn on dedicated graphics card
source_url: https://github.com/monero-project/monero-gui/issues/829
author: Axam
assignees: []
labels:
- resolved
created_at: '2017-08-22T01:33:16+00:00'
updated_at: '2018-07-17T14:09:30+00:00'
type: issue
status: closed
closed_at: '2018-07-17T14:09:30+00:00'
---

# Original Description
MacOS GUI Beta 2 always turn on dedicated graphics card on MacBooks with switchable graphics.
Such behavior isn't power efficient. Is it possible to remove dGPU dependency? 

# Discussion History
## johnalanwoods | 2017-09-17T21:01:38+00:00
Is this issue still occurring on the release GUI? I'd guess so, but don't have a Mac with dual cards to test.

This issue can be solved by including 'NSSupportsAutomaticGraphicsSwitching' in the info.plist appropriately, and is compatible with all Mac OS releases since 10.7 (2011)

Further considerations here: https://developer.apple.com/library/content/technotes/tn2229/_index.html


## pebroz | 2018-01-17T22:24:10+00:00
Still an issue with 0.11.1.0 the monero-wallet-gui.app is still listed as "Requires High Perf GPU" in the Activity Monitor under Energy.

## sanderfoobar | 2018-07-17T13:53:13+00:00
Was previously fixed via #1367. Thanks for the heads-up.

+resolved

# Action History
- Created by: Axam | 2017-08-22T01:33:16+00:00
- Closed at: 2018-07-17T14:09:30+00:00
