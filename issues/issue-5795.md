---
title: Dear Developer monero can not Continuous transfer
source_url: https://github.com/monero-project/monero/issues/5795
author: vae520283995
assignees: []
labels: []
created_at: '2019-08-05T06:59:34+00:00'
updated_at: '2022-02-19T04:51:23+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:51:23+00:00'
---

# Original Description
I am an exchange platform and need to integrate monero Wallet,When I transfer once, I have to wait for 10 confirmations to transfer the next one.
Can you help me

# Discussion History
## thomasvaughan | 2019-08-07T19:11:43+00:00
@vae520283995  There's a discussion on reddit that you may find helpful:
 [https://www.reddit.com/r/Monero/comments/bel9w1/question_regarding_locked_balance_per_transaction/](https://www.reddit.com/r/Monero/comments/bel9w1/question_regarding_locked_balance_per_transaction/)

## vae520283995 | 2019-08-08T01:27:54+00:00
> @vae520283995 There's a discussion on reddit that you may find helpful:
> https://www.reddit.com/r/Monero/comments/bel9w1/question_regarding_locked_balance_per_transaction/

thank you

## moneromooo-monero | 2019-08-19T15:22:13+00:00
You can use min-outputs-* settings to avoid consolidating your outputs needlessly.
Values of, eg, 10 for count and 1 for value means the wallet will try to keep at least 10 outputs of value >= 1 monero. You only have to wait when you've spent the last of your outputs.

# Action History
- Created by: vae520283995 | 2019-08-05T06:59:34+00:00
- Closed at: 2022-02-19T04:51:23+00:00
