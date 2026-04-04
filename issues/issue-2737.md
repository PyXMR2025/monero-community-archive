---
title: 'Send page: fee isn''t calculated before send button is clicked'
source_url: https://github.com/monero-project/monero-gui/issues/2737
author: rating89us
assignees: []
labels: []
created_at: '2020-01-19T21:33:56+00:00'
updated_at: '2020-04-16T17:18:08+00:00'
type: issue
status: closed
closed_at: '2020-04-16T17:18:08+00:00'
---

# Original Description
Send page should display the fee before the send button is clicked.

In order to calculate a fee, a transaction must first be created. 

Address + amount + fee priority are required to create a transaction.

Some thoughts:
- Address should be the first field of this page.
- Since fee priority is auto-selected, after the amount is typed, a transaction should be created in the background and the fee should be displayed for the user in Send page (no splash screen should appear).
- Every time fee priority, amount or address changes, a new transaction should be created in order to display the fee.
- This feature (displaying fee in send page) should probably be disabled in hardware wallets.

# Discussion History
## selsta | 2020-01-19T22:06:28+00:00
> Since fee priority is auto-selected, after the amount is typed, a transaction should be created in the background and the fee should be displayed for the user in Send page (no splash screen should appear).

AFAIK the fee also changes over time, e.g. 2 minutes later the fees can be different.

-------------------

MyMonero does the following:

<img width="225" alt="Screenshot 2020-01-19 at 23 05 37" src="https://user-images.githubusercontent.com/7697454/72689289-36047a00-3b10-11ea-80e8-d769e1d86e3e.png">

They also only estimate the amount and fee.

## ghost | 2020-04-04T13:25:45+00:00
Your ideas are very good. Some guy already had the same ideas (#2405):

![image](https://user-images.githubusercontent.com/46682965/78451873-4ac0ca80-7688-11ea-8d6b-6032a4cc936c.png)


## rating89us | 2020-04-16T17:18:08+00:00
Closed with PR #2739

# Action History
- Created by: rating89us | 2020-01-19T21:33:56+00:00
- Closed at: 2020-04-16T17:18:08+00:00
