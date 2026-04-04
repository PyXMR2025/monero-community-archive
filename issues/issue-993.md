---
title: Change "Wallet creation height" -> "Wallet scan height" + add info
source_url: https://github.com/monero-project/monero-gui/issues/993
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2017-12-05T14:24:06+00:00'
updated_at: '2019-07-17T21:18:42+00:00'
type: issue
status: closed
closed_at: '2019-07-17T21:18:42+00:00'
---

# Original Description
**Problem**:
I think this scanning from particular block height is confusing for some users and this naming does not help it much 
![image](https://user-images.githubusercontent.com/6553766/33611778-e301f2d6-d9cf-11e7-9aa0-b738c13f2967.png)
The naming is correct till the point the user changes this setting, then it is not really the creation height?

**Solution**:
More appropriate would be the name "Wallet scan height" or "Wallet minimal scan height" with some added information/help button - "This is the number of the first block from which the wallet scans the blockchain, transactions before this block will be ignored, best set it to the block from which you did the first transaction from/to this wallet"


# Discussion History
## damiangreen | 2018-01-06T17:52:20+00:00
So I set the wallet creation height to 1481260 (today), yet the sync tab says blocks remaining 1375528 rather than the couple of hundred I thought it would download. 

And my balance remains at 0. Do I misunderstand this, I thought setting this would allow you to just get the most recent blocks so you dont need to download the entire blockchain to be able to see your transactions.

## 1337tester | 2018-03-25T23:27:49+00:00
I think you have a slight misconception here, this value sets the first block to scan (and take into history and balance consideration) for your wallet.
I might be wrong but I think sync and loading the balance/history are separate processes, this one should not affect the sync

## selsta | 2019-07-17T21:16:34+00:00
We changed the label to `Wallet restore height` some time ago. For other wordings please propose to https://github.com/monero-project/monero/

+resolved

# Action History
- Created by: 1337tester | 2017-12-05T14:24:06+00:00
- Closed at: 2019-07-17T21:18:42+00:00
