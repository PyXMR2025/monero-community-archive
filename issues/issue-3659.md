---
title: 'History: parcially synced wallet displaying sent transaction with wrong amount'
source_url: https://github.com/monero-project/monero-gui/issues/3659
author: rating89us
assignees: []
labels: []
created_at: '2021-08-06T12:19:51+00:00'
updated_at: '2021-08-06T13:30:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I synced a wallet with a restore height that is too late (there were transactions before the wallet restore height), and its sync resulted in a single sent transaction with a completely wrong amount: 
![image](https://user-images.githubusercontent.com/45968869/128507933-02de0f56-9f51-4755-97d3-42a73f743a70.png)

This should be "Unknown amount" since it's a recovered wallet.

# Discussion History
## selsta | 2021-08-06T13:23:30+00:00
Don't think this is anything we can "fix" on GUI side.

## rating89us | 2021-08-06T13:26:32+00:00
At least we can change transactions with extremely high amounts (18 million XMR) to an "Unknown amount"

## selsta | 2021-08-06T13:30:10+00:00
It's theoretically possible to have 18 million XMR so I would be against this. 

# Action History
- Created by: rating89us | 2021-08-06T12:19:51+00:00
