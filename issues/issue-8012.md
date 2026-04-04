---
title: Monero GUI crashes when over-filling description of payment request
source_url: https://github.com/monero-project/monero/issues/8012
author: the-lightstack
assignees: []
labels: []
created_at: '2021-10-19T16:55:14+00:00'
updated_at: '2021-10-21T00:30:08+00:00'
type: issue
status: closed
closed_at: '2021-10-21T00:30:08+00:00'
---

# Original Description
Version of pre-build binary GUI:
0.17.2.3-113efbf (Qt 5.15.2)

OS:
Linux, 64bit

Crash message in terminal:
`
terminate called after throwing an instance of 'qrcodegen::data_too_long'
  what():  Data length = 20604 bits, Max capacity = 18672 bits
fish: “./monero-wallet-gui” terminated by signal SIGABRT (Abort)
`
Solution:
Cap the UI input field after MAX_CAPACITY bytes entered

# Discussion History
## selsta | 2021-10-21T00:30:08+00:00
Thank you, I created a PR for it on the GUI repo. Closing this as this issue tracker is for monero itself, not the GUI.

# Action History
- Created by: the-lightstack | 2021-10-19T16:55:14+00:00
- Closed at: 2021-10-21T00:30:08+00:00
