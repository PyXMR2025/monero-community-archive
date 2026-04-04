---
title: 'Wallet RPC get_balance returns an incorrect unlocked_balance value intermittently. '
source_url: https://github.com/monero-project/monero/issues/8744
author: suggalla
assignees: []
labels: []
created_at: '2023-02-17T19:31:23+00:00'
updated_at: '2023-02-17T19:54:06+00:00'
type: issue
status: closed
closed_at: '2023-02-17T19:54:05+00:00'
---

# Original Description
I'm using the monero-java library to call the method `wallet.getUnlockedBalance()` on a view-only wallet. I believe this is a proxy to the underlying `get_balance` wallet RPC. This method will intermittently return a very incorrect value for `unlocked_balance`. Something to the order of 55x my balance. This happens infrequently, about 2-3 times a month and persists for 3 hours at a time. Thanks for any help! 

# Discussion History
## selsta | 2023-02-17T19:41:51+00:00
Did you import key images? A view only wallet won't have the correct balance without key images imported.

> If your wallet has outgoing transactions, the balance displayed will not be correct. To get a correct balance in a view-only wallet, you have to import the accompanying key images of each output of the wallet.

https://www.getmonero.org/resources/user-guides/view_only.html



## suggalla | 2023-02-17T19:47:38+00:00
> Did you import key images? A view only wallet won't have the correct balance without key images imported.
> 
> > If your wallet has outgoing transactions, the balance displayed will not be correct. To get a correct balance in a view-only wallet, you have to import the accompanying key images of each output of the wallet.
> 
> https://www.getmonero.org/resources/user-guides/view_only.html

Yes, I import the key images to the view wallet right before creating a transaction.

## suggalla | 2023-02-17T19:54:05+00:00
This might be a timing issue of not importing the key images upon a restart. Will try that, thanks! 

# Action History
- Created by: suggalla | 2023-02-17T19:31:23+00:00
- Closed at: 2023-02-17T19:54:05+00:00
