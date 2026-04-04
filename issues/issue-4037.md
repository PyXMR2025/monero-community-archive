---
title: XMR did not come to my wallet
source_url: https://github.com/monero-project/monero-gui/issues/4037
author: 1Maestro
assignees: []
labels: []
created_at: '2022-09-22T09:29:53+00:00'
updated_at: '2022-09-23T02:04:48+00:00'
type: issue
status: closed
closed_at: '2022-09-23T02:04:48+00:00'
---

# Original Description
I bought some XMR with bitcoin via ChangeNow.io and they claim everything went succesfull and the funds should have arrived in my wallet but i cant see any funds or transactions have been made and i am still a beginner in the crypto space so i dont really understand how this would happen when the adress and everything was correct

# Discussion History
## selsta | 2022-09-22T09:49:52+00:00
Can you go to Settings -> Info and post:

- Version
- Wallet mode
- Wallet restore height

Do you also have a transaction id?

## 1Maestro | 2022-09-22T10:04:30+00:00
Wallet mode is: Simple mode (bootstrap)
Version is: 0.17.3.1-release (Qt 5.15.2)
Wallet restore height :2716307 this one i changed becuase i thought thats what they meant with "resynchronize the blocks from [2716307]"
i dont know what the transaction id would be but i asked the support to send me one so ill post it shortly!

## selsta | 2022-09-22T10:06:42+00:00
As a first step you have to update to v0.18, there was a network upgrade.

Afterwards I would recommend to set a custom remote node.

## 1Maestro | 2022-09-22T10:24:19+00:00
https://changenow.io/exchange/txs/3ae8382e41ca2f here is the transaction ID i think? and i updated the wallet to 0.18 but i dont now how to change to a custom remote node

## selsta | 2022-09-22T10:25:06+00:00
You can follow the steps here to change to a custom remote node: https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781

## 1Maestro | 2022-09-22T10:31:39+00:00
wow it fixed it! Thanks alot!!!!!<3333

# Action History
- Created by: 1Maestro | 2022-09-22T09:29:53+00:00
- Closed at: 2022-09-23T02:04:48+00:00
