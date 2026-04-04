---
title: Funds are blocked every time I send them with RPC Wallet
source_url: https://github.com/monero-project/monero/issues/9283
author: maksemen2
assignees: []
labels:
- question
created_at: '2024-04-06T16:16:08+00:00'
updated_at: '2024-04-06T19:21:57+00:00'
type: issue
status: closed
closed_at: '2024-04-06T19:21:57+00:00'
---

# Original Description
```
>> wallet.balance(unlocked=True) # 0.49
>> wallet.transfer(<address>, 0.03)
>> wallet.balance(unlocked=True) # 0
>> wallet.balance(unlocked=False) # 0.46
```

Why does it happen and how to deal with it?

# Discussion History
## selsta | 2024-04-06T19:21:57+00:00
Please see https://monero.stackexchange.com/a/12781 and https://monero.stackexchange.com/questions/2783/what-is-the-purpose-of-locked-balance

# Action History
- Created by: maksemen2 | 2024-04-06T16:16:08+00:00
- Closed at: 2024-04-06T19:21:57+00:00
