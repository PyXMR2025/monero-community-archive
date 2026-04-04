---
title: 'OpenSuSE 42.2: Need to manually export QT_SCALE_FACTOR=0.5 to fit GUI window
  on full HD display'
source_url: https://github.com/monero-project/monero-gui/issues/623
author: villabacho
assignees: []
labels:
- resolved
created_at: '2017-03-28T08:02:41+00:00'
updated_at: '2019-07-16T17:27:47+00:00'
type: issue
status: closed
closed_at: '2019-07-16T17:27:47+00:00'
---

# Original Description
The scaling should somehow be automatic depending on screen resolution.
Without setting QT_SCALE_FACTOR, fonts and other GUI elements are unnecessarily large.

# Discussion History
## sanderfoobar | 2018-03-30T02:18:00+00:00
Cool, I did not know of `QT_SCALE_FACTOR`. Works pretty good.

Side-note: GUI is releasing a new (black) theme soon. Might improve things on small resolutions, all tough more steps should def. be taken to combat this.

## erciccione | 2018-11-18T13:20:10+00:00
was this solved with new theme?

## sanderfoobar | 2018-11-18T14:51:10+00:00
Don't think so, perhaps @villabacho can verify.

## selsta | 2019-07-16T17:22:04+00:00
Full HD doesn’t sound like any high DPI scaling, the GUI should fit on a full HD display fine.

Please open a new issue if this problem still persists.

+resolved

# Action History
- Created by: villabacho | 2017-03-28T08:02:41+00:00
- Closed at: 2019-07-16T17:27:47+00:00
