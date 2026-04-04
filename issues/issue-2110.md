---
title: '[Trezor] - Entering passphrase hint in wallet'
source_url: https://github.com/monero-project/monero-gui/issues/2110
author: vir-satoshi
assignees: []
labels:
- enhancement
- invalid
created_at: '2019-04-24T12:12:30+00:00'
updated_at: '2019-04-30T11:27:38+00:00'
type: issue
status: closed
closed_at: '2019-04-30T11:27:38+00:00'
---

# Original Description
During the process of entering the passphrase in the Monero wallet, the T2 (Trezor T) device asks "Where to enter your passphrase?" question on the T2 display. During that process, the Monero wallet has only the "Opening wallet" dialog loading. 

![image](https://user-images.githubusercontent.com/37402655/56658140-2566c680-669a-11e9-8a41-66ec3bf7f8d4.png)

It would be really user-friendly if during this process the wallet could show a message to complete an action on the Trezor device, letting know the user to check the device display. 

I have attached a Trezor wallet solution for reference.

![image](https://user-images.githubusercontent.com/37402655/56658470-f7ce4d00-669a-11e9-8749-5166b6137b91.png)
@ph4r05 
 

# Discussion History
## selsta | 2019-04-24T12:19:42+00:00
@ph4r05 

+enhancement

## ph4r05 | 2019-04-24T12:41:40+00:00
This should be already implemented with the current monero.git master and monero-gui.git master. All PRs are merged, pls rebuild and try again and let us know. Thanks! :)

Related PRs:
- https://github.com/monero-project/monero/pull/5355
- https://github.com/monero-project/monero-gui/pull/2037

## dEBRUYNE-1 | 2019-04-25T19:38:13+00:00
@vir-satoshi - Can you confirm it works properly with monero master & monero-gui master? 

## selsta | 2019-04-30T11:26:17+00:00
I can confirm that this is working.

<img width="1026" alt="Screenshot 2019-04-30 at 13 25 21" src="https://user-images.githubusercontent.com/7697454/56958737-70298800-6b4b-11e9-854a-dba3be176de6.png">

+invalid

# Action History
- Created by: vir-satoshi | 2019-04-24T12:12:30+00:00
- Closed at: 2019-04-30T11:27:38+00:00
