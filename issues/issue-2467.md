---
title: Transaction confirmation improvements
source_url: https://github.com/monero-project/monero-gui/issues/2467
author: rating89us
assignees: []
labels: []
created_at: '2019-11-23T22:38:11+00:00'
updated_at: '2020-10-28T07:39:52+00:00'
type: issue
status: closed
closed_at: '2020-10-28T07:39:52+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/45968869/70388059-60a9d180-19ad-11ea-8a74-6be021cb129c.png)

1) Simple mode shouldn't display `Ring size`, `Number of transactions` and `Spending address index`.

2) There should be an additional field `From:`, with the following format:
- From: "_Wallet_" / "_Account_"
- `From: John's wallet / Savings`

3) `Address:` should be renamed into `To:`

4) `Amount:` and `Fee:` should display XMR

5) Amount converted in fiat (USD) should also appear
- in a second line: `Amount (USD):` and `Amount (EUR):`
- or in the same line: `Amount: 1.0 XMR (54 USD)`

6) `Fee:` shouldn't display extra zeros at the end
- Currently: `Fee: 0.0000248200`
- Expected: `Fee: 0.00002482`

7) `Ok` button should be renamed into `Confirm transaction`

# Discussion History
# Action History
- Created by: rating89us | 2019-11-23T22:38:11+00:00
- Closed at: 2020-10-28T07:39:52+00:00
