---
title: GUI will not start over RDP connection [v0.12.0.0]
source_url: https://github.com/monero-project/monero-gui/issues/1277
author: LesterCovax
assignees: []
labels:
- bug
- resolved
created_at: '2018-04-05T19:24:41+00:00'
updated_at: '2018-07-04T08:36:25+00:00'
type: issue
status: closed
closed_at: '2018-07-04T08:36:25+00:00'
---

# Original Description
`monero-wallet-gui.exe` in v0.12.0.0 will not start while RDP'ing via Remmina from Ubuntu to a Win10 box.  This issue does not occur in v0.11.1.0.

`start-low-graphics-mode.bat`, however, does start correctly with v0.12.0.0.  I suspect that it's a QT-based regression error, and related to [OpenGL rendering of QT over RDP](https://forum.qt.io/topic/79580/opening-qt-from-remote-desktop-connection/12).

# Discussion History
## medusadigital | 2018-04-05T19:35:36+00:00
issue seems to be that we have nuked ANGLE support by accident while upgrading to qt 5.10 on windows build environment.

it may also be possible that ANGLE ist still enabled, but needs some dll's. 

## dEBRUYNE-1 | 2018-04-05T19:45:46+00:00
+bug

## LesterCovax | 2018-04-05T20:26:22+00:00
@medusadigital Thanks for the info. TIL.

[Here's more information](https://wiki.qt.io/Qt_5_on_Windows_ANGLE_and_OpenGL) on the differences between OpenGL and ANGLE for others that are interested.  One of the key advantages listed for ANGLE is RDP support.

## dEBRUYNE-1 | 2018-07-04T08:33:42+00:00
This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-04T08:33:46+00:00
+resolved

# Action History
- Created by: LesterCovax | 2018-04-05T19:24:41+00:00
- Closed at: 2018-07-04T08:36:25+00:00
