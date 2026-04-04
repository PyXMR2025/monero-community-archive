---
title: '[Discussion] make QT quick 2D renderer the default renderer on all platforms. '
source_url: https://github.com/monero-project/monero-gui/issues/813
author: medusadigital
assignees: []
labels:
- proposal
created_at: '2017-08-08T01:28:14+00:00'
updated_at: '2020-04-22T20:58:20+00:00'
type: issue
status: closed
closed_at: '2020-04-22T20:58:10+00:00'
---

# Original Description
Right now we offer this option only via environment variable on Linux and OS-X.
On windows there is a .bat script, named _start-low-graphichs-mode.bat._

duscussion needs to happen if this should be made the default setting. this would highly benefit old machines, and depending on settings machines via RDP or VNC, which often support 2D. on future(?) ARM builds it might have an effect too. 

on the other side, we dont know if the 2D renderer really runs everywhere. the current state is kind of ballte proofed allready, therefore the discussion Label (yet to come)

# Discussion History
## danrmiller | 2017-08-09T02:34:43+00:00
I can add the "discussion" label but I would think the existing "proposal" label should suffice.

## medusadigital | 2018-01-11T14:26:08+00:00
+proposal 

## selsta | 2020-04-22T20:58:10+00:00
Closing as I don’t think this proposal makes sense. The 2D renderer has worse quality, less features and is less supported by Qt overall.

# Action History
- Created by: medusadigital | 2017-08-08T01:28:14+00:00
- Closed at: 2020-04-22T20:58:10+00:00
