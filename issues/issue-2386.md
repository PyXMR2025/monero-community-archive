---
title: Transactions page
source_url: https://github.com/monero-project/monero-gui/issues/2386
author: ghost
assignees: []
labels: []
created_at: '2019-09-10T18:52:22+00:00'
updated_at: '2019-11-12T09:34:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(Updated!)

![image](https://user-images.githubusercontent.com/46682965/66257830-12563780-e79e-11e9-9261-a11d8912d8c7.png)



# Discussion History
## selsta | 2019-09-10T18:55:05+00:00
Scroll lists can become a performance problem in wallets with more than 5000 transactions. That’s a reason why dsc added pages.

I think the current design is visually nicer, also we already show more than 5 items per page (will be included in next release):

https://user-images.githubusercontent.com/7697454/64641729-14321280-d40d-11e9-8a07-8b4348a66dc6.png

Combining sort and advanced options is something to think about.

## ghost | 2019-09-10T19:34:15+00:00
> Scroll lists can become a performance problem in wallets with more than 5000 transactions.

Only show ~500 transactions at max. To see older transactions, use filters. (Which you'd need either way, because clicking through hundreds of pages isn't an option either.)

## rating89us | 2019-10-06T13:52:05+00:00
I prefer a full date like MM/DD/YYYY.

Displaying blockheight in this page makes no sense (maybe useful in advanced mode).

I agree that we should display descriptions in this page.

I agree that we should remove "Received" and "Sent" texts, and instead use green and red colors and symbols + an -.






## ghost | 2019-10-06T16:02:28+00:00
> I prefer a full date like MM/DD/YYYY.

That's the default! What I've shown is optional. Go to the (current) GUI settings and see it for yourself :)

## rating89us | 2019-11-12T08:39:47+00:00
- If the wallet saves the transaction amount in fiat when the transaction is completed, it could display in Transactions page the respective amount in fiat (current amount and amount at the time of the transaction).
- Therefore, I would use "Amount" instead of "XMR" in second column, because amount value could be 1 XMR (62 USD).
- The Transaction page is the place you go when you want to check if your transaction was confirmed. Some tags according to confirmation and amount being locked would be nice:
1. Unconfirmed Tx: **UNCONFIRMED** (in red)
2. Confirmed Tx with <10 conf. (amount locked):
- Option 1:
   - All transactions: **5 of 10 CONFIRMATIONS (~10 min. left)** (in yellow)
- Option 2: 
   - Receiving transaction: **5 of 10 CONFIRMATIONS (spendable in ~10 min.)** (in yellow)
   - Spending transaction: **5 of 10 CONFIRMATIONS (change spendable in ~10 min.)** (in yellow)
- Option 3:
   - Receiving transaction: **CONFIRMED (spendable in ~10 min.)** (in yellow)
   - Spending transaction: **CONFIRMED (change spendable in ~10 min.)** (in yellow)
3. Confirmed Tx with ≥10 conf. (amount unlocked): no tag

# Action History
- Created by: ghost | 2019-09-10T18:52:22+00:00
