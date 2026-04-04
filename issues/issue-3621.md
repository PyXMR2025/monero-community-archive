---
title: Someone know what this Error means?
source_url: https://github.com/monero-project/monero/issues/3621
author: dmgmaker
assignees: []
labels:
- invalid
created_at: '2018-04-12T14:44:06+00:00'
updated_at: '2018-05-16T11:08:57+00:00'
type: issue
status: closed
closed_at: '2018-05-16T11:08:57+00:00'
---

# Original Description
It happens when i try to get into my wallet with my password.
![unbenannt](https://user-images.githubusercontent.com/38203374/38684770-b2d3e118-3e70-11e8-8211-09b3dbbb433a.jpg)


# Discussion History
## dmgmaker | 2018-04-12T14:48:37+00:00
Or can someone explain to me why remote node isnt working? I got rid of the first error by restoring my wallet. 
![unbenannt](https://user-images.githubusercontent.com/38203374/38685051-54e4c206-3e71-11e8-8617-bdaf9ca5d342.jpg)


## dmgmaker | 2018-04-12T14:49:04+00:00
There should be a balance on my account

## stoffu | 2018-04-13T03:57:16+00:00
The red text at the top right of the balance section means that you unintentionally chose stagenet when restoring the wallet, which is why you can't connect to node.moneroworld.com:18089 and your balance is zero. Do the wallet restoration process again, and make sure that neither of the "testnet" or "stagenet" checkboxes is checked at the very first "Welcome to Monero" screen.


## dmgmaker | 2018-04-13T14:43:30+00:00
What is the Mode stagenet and testnet for? But thank you very much this helped me to get my wallet to work. I have one little more question i thought that when i use remote node that it will be ready instantly but it needed like one hour to finish (it was no problem because i try to get it working since 5 days)

## stoffu | 2018-04-13T15:36:40+00:00
The testnet and stagenet are for testing the software without having to spend real money.

Regarding remote node: if your wallet’s restore height is sometime back in the past, the wallet still needs to download and scan those blocks which can take a while.

## moneromooo-monero | 2018-05-16T10:28:34+00:00
+invalid

# Action History
- Created by: dmgmaker | 2018-04-12T14:44:06+00:00
- Closed at: 2018-05-16T11:08:57+00:00
