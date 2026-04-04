---
title: Locked amount message from previous wallet gets show in new wallet when syncing.
source_url: https://github.com/monero-project/monero-gui/issues/2889
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2020-05-06T12:47:02+00:00'
updated_at: '2020-05-08T17:26:47+00:00'
type: issue
status: closed
closed_at: '2020-05-08T17:26:47+00:00'
---

# Original Description
Using monero-wallet-gui 0.15.0.4 on macOS.

**Scenario:**
Suppose you have 2 wallets: A and B.
With the GUI, I sent some XMR from wallet A to wallet X.
Next, I close wallet A, and open wallet B.
Wallet B is not up to date, and needs to sync for a while. The GUI will show the message from wallet A that the "available balance will be unavailable for 20 minutes", until it is done syncing. This is not correct as **that information has nothing to do with wallet B**, and ideally, **it should not even remember that anymore to avoid information leaks via memory!**


# Discussion History
# Action History
- Created by: peanutsformonkeys | 2020-05-06T12:47:02+00:00
- Closed at: 2020-05-08T17:26:47+00:00
