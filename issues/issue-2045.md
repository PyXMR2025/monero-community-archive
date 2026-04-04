---
title: 500%+ Speedup Hack for Transaction Creation on Slow Nodes (Time Critical Deposits)
source_url: https://github.com/monero-project/monero-gui/issues/2045
author: MoneroChan
assignees: []
labels: []
created_at: '2019-03-30T10:43:30+00:00'
updated_at: '2019-07-04T13:57:48+00:00'
type: issue
status: closed
closed_at: '2019-07-04T13:57:48+00:00'
---

# Original Description
Hi, I’ve been using a bootstrap trick to speed up transaction creation times on Old PCs running a monero node (turned on only to send a transactions)

This has also been successfully used to resolve other github issues, e.g;
https://github.com/monero-project/monero-gui/issues/1995#event-2235518223

**Why use this hack:** Creating a transaction quickly is Critical for deposits to fixed rate exchanges ( LRoS , XMR.TO etc..), as you only have a short timeframe to make a deposit to qualify for that exchange rate once you get the payment information.


**Speed Comparison (Core2 Duo, 160GB Spinning HDD) Create a transaction time:**
- Normal: 50+ seconds
- Bootstrap hack: 10 seconds (500%+ Speedup)


**Here's How to perform this Hack on the Monero GUI Wallet (v14) (internet connected):**

- Step 1: Power on your node, Sync the blockchain and start the Monero GUI.

- Step 2: Create a dummy transaction (prepare to send 0.00000001 XMR to Yourself)

- Step 3: Click SEND ONCE (this should NOT send the funds, but will cause the GUI to bootstrap the wallet, and the 'preparing transaction'/'creating transaction' screen should now appear. This is the bootstrap phase.

- Step 4: After a long wait, The Enter Password Screen finally appears. DO NOT ENTER YOUR PASSWORD. Click "CANCEL/BACK" and you will return to the Send screen.

- Step 5: The hack is now complete. Your wallet is now bootstrapped for rapid transaction creation. Your wallet transaction generator is Now in sync with the more recent blocks and can now prepare Transactions much faster from this point (at least for the next 10 minutes or so). Do Not close the GUI / wallet.

- Step 6: Go to your exchange (XMR.TO/ LROS etc) and book/arrange a time sensitive order now.

- Step 7: Go back to your wallet and send the payment from the screen where you left off.

- Step 8: Enter the payment details and click send. the Create transaction screen should only take a few seconds now (500%+ Speedup).

- Step 9: Enter your password and click Send again, to actually send the funds.


**How to perform this Hack on GUI View only wallet (Cold sign wallet):**

- Step 1: Power on your node, Sync the blockchain and start the Monero GUI.

- Step 2: Create a Dummy transaction (prepare to send 0.00000001 XMR to Yourself).

- Step 3: Click 'Create TX file.' (advanced options if it doesn't appear) the 'preparing transaction'/'creating transaction' screen now appears. This is the bootstrap phase.

- Step 4: After a long wait, you will be asked to save the transaction file, Just cancel or save the file anywhere and delete it.

- Step 5 to 7 is the same as above.

..........
This trick has already helped a lot of people, so maybe the Devs can insert a 'bootstrap' button to perform this bootstrap hack instead?

Cheers
MC

# Discussion History
## sanderfoobar | 2019-04-08T01:46:53+00:00
CLI should yield the same transaction creation times. As mentioned in #1995, this probably ought to be reported in https://github.com/monero-project/monero

## dEBRUYNE-1 | 2019-07-03T17:29:13+00:00
Can you check whether GUI v0.14.1.0 is an improvement in this regard? 

## MoneroChan | 2019-07-04T13:57:21+00:00
I'm glad to report a major improvement is noticable in GUI v0.14.1.0
The Time taken to create transaction is now reduced to 18 seconds on the first attempt :)


# Action History
- Created by: MoneroChan | 2019-03-30T10:43:30+00:00
- Closed at: 2019-07-04T13:57:48+00:00
