---
title: GUI 0.14.1 - laggy and unresponsive when trying to close
source_url: https://github.com/monero-project/monero-gui/issues/2333
author: dginovker
assignees: []
labels:
- resolved
created_at: '2019-07-31T17:23:24+00:00'
updated_at: '2019-07-31T17:36:48+00:00'
type: issue
status: closed
closed_at: '2019-07-31T17:28:39+00:00'
---

# Original Description
I've got my wallet fully synced, and I click the "X" on the top right to close the wallet. It takes quite a while (still running), and I can't click anywhere else on the GUI either while this is happening.

Some specs:

Manjaro Linux, Kernel 5.2.4-1, KDE Plasma 5.16.3, neither CPU nor RAM are near limits, internet is connected.

*****

Edit: Can't reproduce. Trying to narrow down now. It was after a long sync, while another wallet was also open, however.

# Discussion History
## selsta | 2019-07-31T17:27:46+00:00
v0.14.1.2 addresses this, which will be out really soon.

+resolved

# Action History
- Created by: dginovker | 2019-07-31T17:23:24+00:00
- Closed at: 2019-07-31T17:28:39+00:00
