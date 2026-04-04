---
title: Settings > Info has wallet items that should be moved to Settings > Wallet
source_url: https://github.com/monero-project/monero-gui/issues/2663
author: rating89us
assignees: []
labels: []
created_at: '2019-12-20T19:07:54+00:00'
updated_at: '2019-12-21T10:02:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This items are wallet file properties and should be moved to Settings > Wallet (see issue #2475):
- Wallet path
- Wallet restore height

Settings > Info should include only items related to GUI wallet software:
- GUI version
- Embedded monero version
- GUI wallet log path
- Wallet mode
- Graphics mode

Current:
![image](https://user-images.githubusercontent.com/45968869/71284869-8c7c6e00-2342-11ea-88d7-a0b3af81bd50.png)


# Discussion History
## erciccione | 2019-12-21T10:02:22+00:00
I think this depends. When debugging an issue we need the users to give all the info we need. Asking them to go look in two different places could make the process much more long and clunky. But i understand the reason of this change, so if others think it's fine, cool for me.

# Action History
- Created by: rating89us | 2019-12-20T19:07:54+00:00
