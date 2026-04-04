---
title: '[Ledger] Changing restore height in settings doesn’t work.'
source_url: https://github.com/monero-project/monero-gui/issues/1992
author: selsta
assignees: []
labels: []
created_at: '2019-03-01T13:25:55+00:00'
updated_at: '2019-04-23T20:28:28+00:00'
type: issue
status: closed
closed_at: '2019-04-23T20:28:28+00:00'
---

# Original Description
I briefly looked into it but I don’t understand how all our restore height variables (appWindow, persistentSettings, wallet api) work together. Could be a monero API bug.

# Discussion History
## mmbyday | 2019-03-13T02:15:22+00:00
Confirmed +bug. Changing from settings does not work. If you wait long enough, the GUI just resets to the original wallet creation height.

# Action History
- Created by: selsta | 2019-03-01T13:25:55+00:00
- Closed at: 2019-04-23T20:28:28+00:00
