---
title: Churn transactions don't display as Received on Transactions tab
source_url: https://github.com/monero-project/monero-gui/issues/2185
author: rating89us
assignees: []
labels:
- invalid
created_at: '2019-05-30T14:09:09+00:00'
updated_at: '2019-05-31T23:09:38+00:00'
type: issue
status: closed
closed_at: '2019-05-31T23:09:38+00:00'
---

# Original Description
When I send a transaction to an address/subaddress of the same account/wallet, a single "Sent" transaction is created on Transactions tab. No "Received" transaction is created. 

It is a strange behavior, because if you export your transactions history to an excel spreadsheet, your balance won't be correct (because excel doesn't know it was a churn).

If the transaction is sent to an address owned by the same account/wallet, there should be an indication. Instead of "Sent", it could be displayed as "Sent to own address" or "Sent (churn)", maybe an special icon could be used.

A "Received" transaction should always be created on Transactions tab. Maybe call it "Received (churn)".

# Discussion History
## selsta | 2019-05-30T15:05:57+00:00
Can you test this with the CLI? Is it the same behavior?

## rating89us | 2019-05-31T20:23:30+00:00
Yes, CLI has the same behavior. It displays a single OUT transaction for each churn transaction that I made:
```
1 (FUNDING)  	  in unlocked        0.099335109436   0.000000000000 (my primary address):0.099335109436 0 - 
2 (MINKO)    	  out                0.010000000000   0.000032390000 (minko subaddress)  :0.010000000000 0 -
3 (MINKO PRIZE)   in unlocked        0.011000000000   0.000000000000 (my primary address):0.011000000000 0 - 
4 (CHURN)    	  out                0.000000000000   0.000047390000 (my subaddress)     :0.100255329436 0 - 
5 (CHURN)     	  out                0.000000000000   0.000032320000 (my primary address):0.100223009436 1 - 
6 (CHURN)    	  out                0.000000000000   0.000032300000 (my primary address):0.100190709436 0 - 
```
![image](https://user-images.githubusercontent.com/45968869/58732726-a67c5080-83f2-11e9-8afe-6e78345859f7.png)





## selsta | 2019-05-31T23:05:37+00:00
+invalid

Ok, this isn’t anything we can fix on the GUI side. I think there’s a technical reason behind it (you are sending your whole change back to yourself in a single out transaction). This probably won’t get changed or “fixed”. You can try opening an issue here though:

https://github.com/monero-project/monero/issues/

# Action History
- Created by: rating89us | 2019-05-30T14:09:09+00:00
- Closed at: 2019-05-31T23:09:38+00:00
