---
title: '[MONERO GUI] Transactions are only displayed for a short moment and then disappear'
source_url: https://github.com/monero-project/meta/issues/571
author: mozzartg
assignees: []
labels: []
created_at: '2021-05-07T07:42:30+00:00'
updated_at: '2021-05-09T19:41:19+00:00'
type: issue
status: closed
closed_at: '2021-05-09T19:41:18+00:00'
---

# Original Description
Hello together
I have noticed a problem. 
I'm currently waiting for two transactions from 8 April that just won't arrive in my wallet. Meanwhile, each transaction has over 20000 confirmations and is still not showing up in my Ledger Wallet Monero GUI Wallet.

Therefore, I test sent 1$ to my wallet and selected higher transaction costs. Now I watched the transaction history in my wallet, indeed the transaction was displayed briefly, a few seconds later it disappeared again. The transaction history is now supposedly empty again.
Coins are also not displayed in the wallet total.

Does anyone know what happened here? Could the same problem have happened with my previous transactions?

Thanks in advance
![pic1](https://user-images.githubusercontent.com/83808387/117415322-79a71100-af18-11eb-8c7b-945a62b81981.jpg)
![pic2](https://user-images.githubusercontent.com/83808387/117415330-7ad83e00-af18-11eb-8f2d-e137b6d39460.png)



# Discussion History
## selsta | 2021-05-07T08:06:06+00:00
Can you click on the two arrows in the bottom left corner to connect to a new node and then go to Settings -> Info, click on (Change) next to wallet restore height and then on okay twice. Wait for it to sync (can take multiple minutes) and then report back if your funds showed up.

## mozzartg | 2021-05-07T08:10:14+00:00
> Can you click on the two arrows in the bottom left corner to connect to a new node and then go to Settings -> Info, click on (Change) next to wallet restore height and then on okay twice. Wait for it to sync (can take multiple minutes) and then report back if your funds showed up.

Thanks for your reply, I will try that later.

## selsta | 2021-05-07T08:36:12+00:00
Before doing what I wrote please report what "wallet restore height" is currently set inside Settings -> Info. I suspect that it is from the future and that's why transactions are getting skipped.

## mozzartg | 2021-05-09T19:22:52+00:00
> Before doing what I wrote please report what "wallet restore height" is currently set inside Settings -> Info. I suspect that it is from the future and that's why transactions are getting skipped.

Okay, Wallet restore height is 20210408.

How can you see that it is from the future?

Kind Regards

## selsta | 2021-05-09T19:24:19+00:00
You have to enter `2021-04-08` into the restore height field, not `20210408`, else it gets interpreted as a number.

## mozzartg | 2021-05-09T19:37:51+00:00
> You have to enter `2021-04-08` into the restore height field, not `20210408`, else it gets interpreted as a number.

It worked.. thanks you so much, all my coins are back! Waited so long for have them back. <3

## selsta | 2021-05-09T19:41:18+00:00
Closing as the issue seems resolved. I will try to remove the UI for the restore height field in a future update to avoid confusion.

# Action History
- Created by: mozzartg | 2021-05-07T07:42:30+00:00
- Closed at: 2021-05-09T19:41:18+00:00
