---
title: Window does not drag consistently when using Custom Decorations (Monero Wallet
  Gui)
source_url: https://github.com/monero-project/monero/issues/8436
author: ethereal-gaze
assignees: []
labels: []
created_at: '2022-07-14T23:27:54+00:00'
updated_at: '2022-07-15T09:28:20+00:00'
type: issue
status: closed
closed_at: '2022-07-15T02:08:36+00:00'
---

# Original Description
When dragging the window on Linux based systems (Xorg, if that matters) it does not stay bound to the cursor. 

# Discussion History
## hyc | 2022-07-15T02:08:36+00:00
Wrong repo, should report it there https://github.com/monero-project/monero-gui/

## selsta | 2022-07-15T09:28:13+00:00
Since using custom decorations is kinda a hack with Qt, we had to write our own resize code which isn't performance efficient. There are some solutions to this but it's quite a bit of work (would require custom code for every OS) which isn't high priority currently.

If it bothers you I would recommend to disable custom decorations.

# Action History
- Created by: ethereal-gaze | 2022-07-14T23:27:54+00:00
- Closed at: 2022-07-15T02:08:36+00:00
