---
title: Amount of transactions sent to the same wallet appear as 0 XMR when tx details
  are recovered from blockchain
source_url: https://github.com/monero-project/monero-gui/issues/2763
author: rating89us
assignees: []
labels: []
created_at: '2020-02-04T13:30:23+00:00'
updated_at: '2020-12-04T19:38:29+00:00'
type: issue
status: closed
closed_at: '2020-12-04T19:38:28+00:00'
---

# Original Description

In Monero GUI:
![image](https://user-images.githubusercontent.com/45968869/73748811-80b20300-475a-11ea-99cc-5e2261b5e528.png)

![image](https://user-images.githubusercontent.com/45968869/73748997-c8388f00-475a-11ea-9d4d-3ec15fa39678.png)

Same wallet in MyMonero:
![image](https://user-images.githubusercontent.com/45968869/73748865-99bab400-475a-11ea-8f3a-0377f08e9fed.png)


# Discussion History
## xiphon | 2020-02-04T14:25:37+00:00
Looks correct according to the screenshot. What is the actual amount and fee?

## rating89us | 2020-02-04T19:04:01+00:00
Transactions were with amounts of 0.0001 XMR and 0.00001 XMR.

I investigated it, and it is related to #2185. All these transactions were done to my own wallet as testing.

When the Monero GUI doesn't hold the transaction history (and must read it from the blockchain), it can't calculate the amount of transactions that were sent to the same wallet. That occurs because since it doesn't hold the key images of used outputs anymore, it can't know the transaction inputs amounts, missing a value in the equation transaction fee = transaction inputs - outputs.

Without importing key images of already spent outputs, I believe it's not possible to recover from the blockchain data the amount of the transaction sent to myself. 

If there is no way for the GUI to recover the amount, at least it should detect that the transaction was sent to the same wallet, and display something like "-0.0003371 XMR (transaction to the same wallet, displaying fee as amount). MyMonero seems to do this, but it doesn't inform that the displayed amount is actually the fee of the transaction.

We could also display the fee as the amount of the transaction when the user is sending a transaction to his/her own wallet.

## selsta | 2020-02-04T20:31:24+00:00
What does monero-wallet-cli display?

## rating89us | 2020-12-04T19:38:28+00:00
Fixed in #2992

# Action History
- Created by: rating89us | 2020-02-04T13:30:23+00:00
- Closed at: 2020-12-04T19:38:28+00:00
