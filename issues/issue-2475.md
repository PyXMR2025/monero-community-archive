---
title: 'Settings > Wallet: missing wallet information'
source_url: https://github.com/monero-project/monero-gui/issues/2475
author: rating89us
assignees: []
labels: []
created_at: '2019-11-24T02:02:21+00:00'
updated_at: '2020-01-26T20:38:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The `Settings > Wallet page` should display an overview of all important details about the wallet, including: 
- Name
- Type
  - Normal
  - View-only with all key images imported (balance is right)
  - View-only with missing key images (balance may not be right)
  - Hardware wallet (Ledger)
  - Hardware wallet (Trezor)
- Creation date & Restore height
- File location
- Statistics
  - Total balance
  - Number of accounts
  - Number of transactions
  - Number of contacts in address book

Currently some important details of the wallet (wallet path, restore height) are inside the `Settings > Info page`. 

![image](https://user-images.githubusercontent.com/45968869/71284509-a8cbdb00-2341-11ea-9386-781ce889dc6b.png)


# Discussion History
## SamsungGalaxyPlayer | 2019-12-20T19:42:42+00:00
I like this idea but I'm also open to other designs. Good list of requirements.

## selsta | 2019-12-20T19:43:39+00:00
Yep, idea ok, not a fan of the design yet.

## rating89us | 2019-12-20T20:02:06+00:00
We could use different icons for wallet types:
* Normal wallet
* View-only wallet
* Hardware wallet (Ledger)
* Hardware wallet (Trezor)
![image](https://user-images.githubusercontent.com/45968869/71288859-6bb81680-234a-11ea-8a20-fef06da4c42d.png)





## erciccione | 2019-12-21T10:00:03+00:00
I'm ok with it if it's only for the advanced mode. Simple mode should be as close as possible to send/receive functonalities only. All these details aren't of any use for a simple user IMO (block height, type, transactions, etc)

# Action History
- Created by: rating89us | 2019-11-24T02:02:21+00:00
