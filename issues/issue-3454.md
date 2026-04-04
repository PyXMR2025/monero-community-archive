---
title: Save tx to file does not work
source_url: https://github.com/monero-project/monero-gui/issues/3454
author: selsta
assignees: []
labels: []
created_at: '2021-05-04T21:05:59+00:00'
updated_at: '2021-05-04T21:38:05+00:00'
type: issue
status: closed
closed_at: '2021-05-04T21:38:05+00:00'
---

# Original Description
There appears to be code for view only wallets to save transactions to a file: https://github.com/monero-project/monero-gui/blob/master/main.qml#L933

But it is not possible to click on the send button in "view only" mode: https://github.com/monero-project/monero-gui/blob/master/pages/Transfer.qml#L806

ping @rating89us, I think you have used this in the past

# Discussion History
## rating89us | 2021-05-04T21:35:55+00:00
To save tx to file on view-only wallet, you should fill Address + Amount and then click on Create button on Advanced options > Offline transaction signing > Create

## selsta | 2021-05-04T21:38:05+00:00
Thanks!

# Action History
- Created by: selsta | 2021-05-04T21:05:59+00:00
- Closed at: 2021-05-04T21:38:05+00:00
