---
title: after rebuilding wallet cache from seed, show_transfers sows amounts wrong
source_url: https://github.com/monero-project/monero/issues/1290
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-02T16:09:45+00:00'
updated_at: '2016-11-05T09:22:57+00:00'
type: issue
status: closed
closed_at: '2016-11-05T09:22:57+00:00'
---

# Original Description
This seems only to affect new (v0.10.0.0-b06c1ab), outgoing transactions when rebuilding caches.

When restoring a wallet from seed that contains such newly made transactions, the transaction change gets sumed up with the real transaction amount. this leaves an inconsistency between balance and transaction history. 

Logs from CLI: 

```
[wallet 48X2Pi]: show_transfers
 1170748     in      09:23:36 AM       5.000000000000 adbe4fc36c1e286e9892b79653c8f4d89f1266e7918d75fae70ce52b92e5b7c5 b73e638674488bf5 - 
 1170762    out      09:47:45 AM       4.998000000000 807ded753ed765e504306c1797c7030f80840f94a160d6ff8c66d8ce1c1fe680 0000000000000000 18446742.07770  
 1170780    out      10:22:47 AM       1.994000000000 89f19d7b6cb14a21939422b285107360d3a7a96cff79ae14026d6a14d8a362cd 0000000000000000 0.004000000000  
[wallet 48X2Pi]: refresh
Starting refresh...
Refresh done, blocks received: 0                                
Balance: 0.000000000000, unlocked balance: 0.000000000000
[wallet 48X2Pi]: 

```

Same wallet in GUI:

![moofeeandsumbughistory](https://cloud.githubusercontent.com/assets/17108301/19936729/d6b14d50-a11e-11e6-8dc0-3aa66c440eab.png)


How to Reproduce:

- Create new wallet
- deposit xmr
- make outgoing transactions with at least _v0.10.0.0-b06c1ab_ 
- delete wallet and restore again from seed with at least _v0.10.0.0-b06c1ab_


# Discussion History
## moneromooo-monero | 2016-11-02T23:32:59+00:00
https://github.com/moneromooo-monero/bitmonero/tree/amount_out

This should fix all the similar problems, whether rebuilt from seed or not.
Also the payment id one.
Please report whether there are remaining wrong numbers. Any in existing transactions in an existing cache might still exist (hopefully not, but I can't be sure), but there should be none when recreating from seed, nor for new transactions.


## medusadigital | 2016-11-03T18:14:40+00:00
tested your branch, seems to resolve all known cache rebuilding issues, great job. waiting for PR :-)


## moneromooo-monero | 2016-11-03T23:50:38+00:00
https://github.com/monero-project/monero/pull/1295

Thanks for testing.


## medusadigital | 2016-11-05T09:22:57+00:00
fixed --> closed


# Action History
- Created by: medusadigital | 2016-11-02T16:09:45+00:00
- Closed at: 2016-11-05T09:22:57+00:00
