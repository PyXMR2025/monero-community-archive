---
title: Successful transaction box remains visible after wallet auto lock through inactivity
source_url: https://github.com/monero-project/monero-gui/issues/3340
author: tficharmers
assignees: []
labels: []
created_at: '2021-02-20T17:19:28+00:00'
updated_at: '2021-06-09T19:03:54+00:00'
type: issue
status: closed
closed_at: '2021-06-09T19:03:54+00:00'
---

# Original Description
After sending a transaction, if the GUI auto locks through inactivity and the success message hasn't been dismissed, it will remain visible. See attached image. I have obscured the transaction ID with a red rectangle.

MacOS Catalina
GUI: 0.17.1.9-3ca5f10

<img width="980" alt="gui" src="https://user-images.githubusercontent.com/23356013/108603489-00c7fc80-73a0-11eb-8385-e6cfda8bb2d1.png">



# Discussion History
## rating89us | 2021-06-09T18:57:51+00:00
This issue can be closed (fixed by #3512) @selsta

# Action History
- Created by: tficharmers | 2021-02-20T17:19:28+00:00
- Closed at: 2021-06-09T19:03:54+00:00
