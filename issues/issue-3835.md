---
title: GUI Freezes upon canceling wallet password
source_url: https://github.com/monero-project/monero-gui/issues/3835
author: riverliway
assignees: []
labels: []
created_at: '2022-02-05T22:07:59+00:00'
updated_at: '2022-02-06T09:32:45+00:00'
type: issue
status: closed
closed_at: '2022-02-06T09:32:45+00:00'
---

# Original Description
The Monero GUI asks for the wallet password every so often. I accidentally clicked cancel and a screen popped up saying "closing wallet" with a little loading circle. The circle then stopped moving and I was unable to interact with the GUI at all. I could not use the minimization, fullscreen, nor close window buttons. I was forced to kill it with task manager. 

My wallet was in the middle of synchronizing, so it is possible that the GUI would have unfrozen when the synchronization completed, but I did not wait for it to complete.

OS: windows x64
GUI version: 0.17.3.1-release (Qt 5.15.2)
Embedded Monero Version: 0.17.3.0-release

# Discussion History
## selsta | 2022-02-06T09:32:45+00:00
Yes, it's most likely related to the wallet still syncing. It would close once it finished.

Closing this as there are similar reports about this open.

# Action History
- Created by: riverliway | 2022-02-05T22:07:59+00:00
- Closed at: 2022-02-06T09:32:45+00:00
