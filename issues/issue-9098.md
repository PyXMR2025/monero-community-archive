---
title: Incorrect getting block height from date
source_url: https://github.com/monero-project/monero/issues/9098
author: developergames2d
assignees: []
labels: []
created_at: '2023-12-24T16:13:02+00:00'
updated_at: '2023-12-25T00:27:17+00:00'
type: issue
status: closed
closed_at: '2023-12-25T00:27:17+00:00'
---

# Original Description
I restored my wallet from date 2023-12-01, but monero-gui sets height ~1'500'000, while real height is ~3'032'307.
I used formula:
1'009'827 + get_difference_days(2016.03.23, 2023.12.01) * 720.

# Discussion History
## selsta | 2023-12-24T16:20:13+00:00
Do you have the GUI set to stagenet?

## developergames2d | 2023-12-24T16:20:43+00:00
> Do you have the GUI set to stagenet?

I use usual monero-wallet-gui.exe

## developergames2d | 2023-12-24T16:21:40+00:00
> Do you have the GUI set to stagenet?

I restored from SEED and date.

## selsta | 2023-12-24T16:22:13+00:00
Yes, but do you have monero-wallet-gui set to Stagenet mode?

## developergames2d | 2023-12-24T16:22:47+00:00
> Yes, but do you have monero-wallet-gui set to Stagenet mode?

How can I check it? I just run monero-wallet-gui.exe

## selsta | 2023-12-24T16:23:48+00:00
When you open the GUI click on Advanced settings in the main menu and then there's a selection for Mainnet, Stagenet and Testnet.

## developergames2d | 2023-12-24T16:28:39+00:00
> When you open the GUI click on Advanced settings in the main menu and then there's a selection for Mainnet, Stagenet and Testnet.

When I use Stagenet, I show not my wallet, with other addresses.

## developergames2d | 2023-12-24T16:33:47+00:00
When I try to restore from height 3030000 (Mainnet), all is OK.

# Action History
- Created by: developergames2d | 2023-12-24T16:13:02+00:00
- Closed at: 2023-12-25T00:27:17+00:00
