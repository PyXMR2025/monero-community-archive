---
title: Enabling tracking checkbox in 0.13.0.3 GUI causes UI to be unresponsive
source_url: https://github.com/monero-project/monero-gui/issues/1663
author: Engelberg
assignees: []
labels:
- bug
- resolved
created_at: '2018-10-16T10:56:05+00:00'
updated_at: '2018-10-25T17:36:26+00:00'
type: issue
status: closed
closed_at: '2018-10-25T17:36:26+00:00'
---

# Original Description
After checking the tracking checkbox, the interface slows down where clicking and typing a character takes several seconds to respond.

Only way I've found to regain responsiveness is to switch the receive view to an unused subaddress, and then the UI becomes sufficiently responsive to disable tracking again, at which point the UI returns to normal.

This is the Windows 64-bit GUI version.

# Discussion History
## erciccione | 2018-10-16T13:36:14+00:00
+bug

## dEBRUYNE-1 | 2018-10-25T17:29:58+00:00
+resolved

# Action History
- Created by: Engelberg | 2018-10-16T10:56:05+00:00
- Closed at: 2018-10-25T17:36:26+00:00
