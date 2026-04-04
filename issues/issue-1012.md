---
title: Misc Tabbing Related Hotkey Bugs
source_url: https://github.com/monero-project/monero-gui/issues/1012
author: Timo614
assignees: []
labels:
- resolved
created_at: '2017-12-11T15:48:41+00:00'
updated_at: '2018-11-18T14:36:31+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:36:31+00:00'
---

# Original Description
The hotkeys are a bit bugged with how they are currently setup.

1. On Mac OS X if I click the `alt` key while I'm on the "Advanced" tab I'm sent to the previous tab I was on but no other tabs have this behavior (guessing since the hotkeys logic sets the leftPanel to the current main state but the advanced tab has no content / mainstate by itself so it reverts to the last tab)
2. The `ctrl+tab` or `alt+tab` behavior seems random "Send" -> "Receive" -> "Prove/check"(under advanced) -> "History" -> "Address book"(under send) -> "Sign/verify"(under advanced) -> "Settings"
3. The "alt+shift+backspace" logic doesn't appear to do anything on a mac (perhaps since it's the delete key on macs?)

# Discussion History
## erciccione | 2018-11-18T14:16:50+00:00
+resolved

# Action History
- Created by: Timo614 | 2017-12-11T15:48:41+00:00
- Closed at: 2018-11-18T14:36:31+00:00
