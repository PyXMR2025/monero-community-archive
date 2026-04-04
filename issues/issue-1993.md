---
title: Know total amount  in waiting on pending TX ( change address)
source_url: https://github.com/monero-project/monero/issues/1993
author: perl5577
assignees: []
labels: []
created_at: '2017-04-19T06:07:41+00:00'
updated_at: '2017-08-07T18:12:16+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:12:16+00:00'
---

# Original Description
Exemple simple for understand, I have only one TXNO for 100XMR.
Balance 100 Unlocked 100

I payout 70XMR to another addresse ( not already include on block).
Balance 0 Unlocked 0

Is impossible know amount 30XMR is waiting spend 

Is very difficults follow amount in wallet when make many payout.






# Discussion History
## moneromooo-monero | 2017-04-22T11:02:15+00:00
This is probably caused by the bug fixed by https://github.com/monero-project/monero/pull/1989

## perl5577 | 2017-04-22T20:17:20+00:00
No,
I want juste method for know amount in my wallet after payout.

Other exemple :
sweep_all  MYADDRESS 
balance
Balance:  0.000000000000, unlocked balance: 0.000000000000













## jonathancross | 2017-06-03T12:49:38+00:00
@perl5577 Can you test the latest version now that #1989 is merged?

## moneromooo-monero | 2017-08-07T17:49:49+00:00
+resolved

# Action History
- Created by: perl5577 | 2017-04-19T06:07:41+00:00
- Closed at: 2017-08-07T18:12:16+00:00
