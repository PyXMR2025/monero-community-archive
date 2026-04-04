---
title: '[Trezor] Device doesn''t return transaction fee to the GUI wallet'
source_url: https://github.com/monero-project/monero-gui/issues/2768
author: rating89us
assignees: []
labels:
- bug
created_at: '2020-02-05T13:20:54+00:00'
updated_at: '2020-05-08T17:37:37+00:00'
type: issue
status: closed
closed_at: '2020-05-08T17:37:36+00:00'
---

# Original Description
Steps to reproduce:
1. Send transaction
2. Proceed to device screen appears
3. See transaction amount and fee on the device's screen
4. Confirm transaction in device
5. GUI displays a transaction confirmation dialog, with correct Amount and Address, but with "Fee: 0.000000000000":

![image](https://user-images.githubusercontent.com/45968869/73845635-55dfb180-4823-11ea-8460-577956b0d16a.png)

# Discussion History
## rating89us | 2020-05-08T17:37:36+00:00
Closed in #2829 and monero-project/monero#6446

# Action History
- Created by: rating89us | 2020-02-05T13:20:54+00:00
- Closed at: 2020-05-08T17:37:36+00:00
