---
title: '[Bug] Can''t Use Wallet in Stagenet or Testnet on Windows'
source_url: https://github.com/monero-project/monero-gui/issues/3816
author: elibroftw
assignees: []
labels: []
created_at: '2022-01-12T23:06:02+00:00'
updated_at: '2022-01-24T20:25:04+00:00'
type: issue
status: closed
closed_at: '2022-01-24T20:25:04+00:00'
---

# Original Description
There's no way to open a wallet in Stagenet on Windows

Reproduction steps:
From the advanced wallet menu, select stagenet under network
![image](https://user-images.githubusercontent.com/21298211/149237013-f8f3b03a-0023-48df-aaa0-ec98955e9250.png)
Click "Create new wallet"
Use remote node monero-stagenet.exan.tech:38081
![image](https://user-images.githubusercontent.com/21298211/149237144-7c9558c7-3d32-46fe-9be8-c3af087b7ba4.png)
Network type is Mainnet now???

Opening from file:
![image](https://user-images.githubusercontent.com/21298211/149237221-cdeb1cd5-4223-4400-b017-8f4739e62284.png)


# Discussion History
## rating89us | 2022-01-13T06:05:57+00:00
I can't reproduce your issue. Which GUI version are you using?

## elibroftw | 2022-01-13T06:10:28+00:00
I'm using the second latest version. It doesn't matter now because it decided to work. It might have something to do with opening a stagenet wallet already and then creating a stagenet wallet.

Anyways the workaround is just using the CLI. 

## elibroftw | 2022-01-13T06:10:57+00:00
I'm closing because the bug is hard to reproduce. 

## rating89us | 2022-01-13T06:30:44+00:00
I could reproduce your bug now, please reopen the issue.

## rating89us | 2022-01-13T06:33:24+00:00
1. Select stagenet in advanced options
2. Open a mainnet wallet
3. Close the wallet and return to the main menu (stagenet will still be selected in advanced options/Network dropdown)
4. Click on create a new wallet. A stagenet wallet should be created, but wizard is creating a mainnet wallet instead.

# Action History
- Created by: elibroftw | 2022-01-12T23:06:02+00:00
- Closed at: 2022-01-24T20:25:04+00:00
