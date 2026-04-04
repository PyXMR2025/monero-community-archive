---
title: CLI wallet - 'set ask-password' command reacts to invalid input
source_url: https://github.com/monero-project/monero/issues/2648
author: 1337tester
assignees: []
labels: []
created_at: '2017-10-13T21:20:12+00:00'
updated_at: '2017-11-14T20:08:28+00:00'
type: issue
status: closed
closed_at: '2017-11-14T20:08:28+00:00'
---

# Original Description
'set ask-password' command should accept only 0 or 1, as per help - 'ask-password <1|0>'

However when there is an invalid (nor 0 or 1) parameter provided, the value is set to 0, see screenshot (works also with non numeric values)
![ask_password](https://user-images.githubusercontent.com/6553766/31566906-08d7be8c-b06d-11e7-91ca-097f7ac02d8d.jpg)


# Discussion History
## selsta | 2017-10-19T11:54:10+00:00
What be defaulting to 1 better?

## stoffu | 2017-10-19T12:59:56+00:00
#2683 

## moneromooo-monero | 2017-11-14T19:43:02+00:00
+resolved

# Action History
- Created by: 1337tester | 2017-10-13T21:20:12+00:00
- Closed at: 2017-11-14T20:08:28+00:00
