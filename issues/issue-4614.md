---
title: Enabling tracking checkbox in 0.13.0.3 GUI causes UI to be unresponsive
source_url: https://github.com/monero-project/monero/issues/4614
author: Engelberg
assignees: []
labels:
- invalid
created_at: '2018-10-16T10:34:08+00:00'
updated_at: '2018-10-16T11:01:07+00:00'
type: issue
status: closed
closed_at: '2018-10-16T10:56:08+00:00'
---

# Original Description
After checking the tracking checkbox, the interface slows down where clicking and typing a character takes several seconds to respond.

Only way I've found to regain responsiveness is to switch the receive view to an unused subaddress, and then the UI becomes sufficiently responsive to disable tracking again, at which point the UI returns to normal.

This is the Windows 64-bit GUI version.

# Discussion History
## moneromooo-monero | 2018-10-16T10:40:56+00:00
Please file GUI bugs on https://github.com/monero-project/monero-core

+invalid


# Action History
- Created by: Engelberg | 2018-10-16T10:34:08+00:00
- Closed at: 2018-10-16T10:56:08+00:00
