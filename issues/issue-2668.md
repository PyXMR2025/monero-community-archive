---
title: 'Open wallet: wallet icons are folders'
source_url: https://github.com/monero-project/monero-gui/issues/2668
author: rating89us
assignees: []
labels: []
created_at: '2019-12-20T20:07:02+00:00'
updated_at: '2021-12-02T06:08:29+00:00'
type: issue
status: closed
closed_at: '2021-12-02T06:08:29+00:00'
---

# Original Description
Wallet file icons should be wallets or hardware wallets.

There are 4 types of wallet files, and we should use different icons for each type:
- Normal wallet (spend wallet)
- View-only wallet
- Ledger wallet
- Trezor wallet
![image](https://user-images.githubusercontent.com/45968869/71289005-bc2f7400-234a-11ea-9d0f-2dbca618563f.png)

Currently all wallets use a folder icon:
![image](https://user-images.githubusercontent.com/45968869/71289055-e123e700-234a-11ea-93b2-11428229e763.png)

# Discussion History
## xiphon | 2019-12-20T20:11:18+00:00
No way to determine the wallet type looking at the file.

## rating89us | 2019-12-20T20:32:09+00:00
> No way to determine the wallet type looking at the file.

You mean you must open the file to know the wallet type?

## xiphon | 2019-12-20T20:33:23+00:00
> You mean you must open the file to know the wallet type?

Yes, open and decrypt it.

## rating89us | 2019-12-20T20:35:55+00:00
Usually the wallet files presented in this page have already been opened before in the GUI wallet, unless the user is importing wallet files from other computer or that have been used in CLI wallet.

The GUI wallet could cache the type of the wallet when its opened.

If the wallet doesn't have a cache for the wallet file, we could display a general wallet icon or a wallet icon with a "?" inside.

## xiphon | 2019-12-20T22:39:24+00:00
Won't fix. Introduces a privacy leak.

## rating89us | 2019-12-24T08:41:21+00:00
Ok. But we should at least change icons from folder icons to wallet icons (https://fontawesome.com/icons/wallet?style=solid)

# Action History
- Created by: rating89us | 2019-12-20T20:07:02+00:00
- Closed at: 2021-12-02T06:08:29+00:00
