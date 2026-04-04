---
title: 'Send page: no invalid address error'
source_url: https://github.com/monero-project/monero-gui/issues/2620
author: rating89us
assignees: []
labels: []
created_at: '2019-12-16T19:27:55+00:00'
updated_at: '2019-12-20T00:45:49+00:00'
type: issue
status: closed
closed_at: '2019-12-20T00:45:49+00:00'
---

# Original Description
If an invalid address is entered, the address field changes its border color to red, but no error message is displayed:
![image](https://user-images.githubusercontent.com/45968869/70935961-1e713780-2020-11ea-9416-d4d376e28d7a.png)

An error message appears only when an amount is entered:
![image](https://user-images.githubusercontent.com/45968869/70936053-56787a80-2020-11ea-8aef-771607606072.png)

Also, what else could cause an "Incorrect transaction information" error? I can't imagine anything else other than an invalid address. Therefore, I suggest changing the message error to: "Destination address is not a valid Monero address"

# Discussion History
# Action History
- Created by: rating89us | 2019-12-16T19:27:55+00:00
- Closed at: 2019-12-20T00:45:49+00:00
