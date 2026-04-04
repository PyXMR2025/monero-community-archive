---
title: 'Send page: transaction details persist when another wallet is opened'
source_url: https://github.com/monero-project/monero-gui/issues/2611
author: rating89us
assignees: []
labels: []
created_at: '2019-12-16T01:12:43+00:00'
updated_at: '2019-12-21T23:11:08+00:00'
type: issue
status: closed
closed_at: '2019-12-21T23:11:08+00:00'
---

# Original Description
This issue compromises privacy when the GUI wallet is in a computer that is shared by more than one user (each user owns a different wallet file). 

User B will be able to see the details (amount, address and description) of a transaction that User A wanted to do, but didn't finish.

Steps to reproduce:
1) Open a wallet (wallet A).
2) Go to Send page, and fill amount, address and Description. Don't send the transaction.
3) Close the wallet. Don't close the GUI wallet.
4) Open a different wallet (wallet B).
5) Go to Send page. Amount, address and Description persist from the Send page of wallet A.

# Discussion History
# Action History
- Created by: rating89us | 2019-12-16T01:12:43+00:00
- Closed at: 2019-12-21T23:11:08+00:00
