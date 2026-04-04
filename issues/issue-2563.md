---
title: Wallet lock is unlocked without password
source_url: https://github.com/monero-project/monero-gui/issues/2563
author: rating89us
assignees: []
labels: []
created_at: '2019-12-07T11:49:31+00:00'
updated_at: '2019-12-23T14:28:34+00:00'
type: issue
status: closed
closed_at: '2019-12-23T14:28:34+00:00'
---

# Original Description
This happens when the wallet is automatically locked for inactivity while the `Set description` dialog is open in Transactions page. 

![image](https://user-images.githubusercontent.com/45968869/70374016-920f9800-18ee-11ea-8e0e-085996376410.png)

When the `Please enter wallet password` dialog appears, both dialogs get mixed, and the `Set description` dialog can be canceled, which removes the black screen in the layer below thus bypassing the wallet lock without entering a password. 

![image](https://user-images.githubusercontent.com/45968869/70374018-963bb580-18ee-11ea-8fea-0490e51f565c.png)

![image](https://user-images.githubusercontent.com/45968869/70374020-9a67d300-18ee-11ea-8ff5-8c997b9a64a0.png)

![lock2](https://user-images.githubusercontent.com/45968869/70374101-9c7e6180-18ef-11ea-91da-0230ec801596.gif)

This allows the user to see all wallet's transactions, accounts and balances. Funds can't be sent because the password is asked again.

# Discussion History
# Action History
- Created by: rating89us | 2019-12-07T11:49:31+00:00
- Closed at: 2019-12-23T14:28:34+00:00
