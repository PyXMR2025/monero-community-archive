---
title: The problem with Monero transactions
source_url: https://github.com/monero-project/meta/issues/523
author: Evgenii272
assignees: []
labels: []
created_at: '2020-10-28T13:36:18+00:00'
updated_at: '2020-12-24T16:31:39+00:00'
type: issue
status: closed
closed_at: '2020-12-24T16:31:39+00:00'
---

# Original Description
I am the owner of a Monero wallet. I use the desktop version of the Monero GUI to manage my funds. After updating "Oxygen Orion" (0.17), I have an expense transaction in my wallet for the entire balance of the wallet, which I did not make. Further it was failed. And the balance is still showing my funds.The details of this transaction do not include the wallet address, and the transaction does not have a transaction key, but there are network confirmations. How is this possible? Now I am trying to send these funds to another wallet, but there is an error occurs saying about an error and double spending. Why I cannot make a transaction for any amount with the balance positive?

# Discussion History
## selsta | 2020-10-28T16:10:54+00:00
Please update to v0.17.1.1 first.

Are you using simple mode or advanced mode? You can check on Settings -> Info.

If advanced mode: Local or remote node?

## Evgenii272 | 2020-10-29T11:02:13+00:00
> Please update to v0.17.1.1 first.
> 
> Are you using simple mode or advanced mode? You can check on Settings -> Info.
> 
> If advanced mode: Local or remote node?

The program has been updated to version v0.17.1.1
Advanced mode in use, remote node

## selsta | 2020-10-29T13:28:21+00:00
Okay, if the remote node you are connected to is a trusted remote node (you can set this in Settings -> Node menu) you can click on "Rescan wallet balance" on Settings -> Wallet screen. Afterwards this issue should be resolved.


If your remote node is not a trusted remote node you have to go to Settings -> Info, click on "(Change)" next to wallet restore height and then okay twice.

## Evgenii272 | 2020-10-29T13:44:54+00:00
> Okay, if the remote node you are connected to is a trusted remote node (you can set this in Settings -> Node menu) you can click on "Rescan wallet balance" on Settings -> Wallet screen. Afterwards this issue should be resolved.
> 
> If your remote node is not a trusted remote node you have to go to Settings -> Info, click on "(Change)" next to wallet restore height and then okay twice.

Node is trusted
After re-scanning the wallet balance, the balance became 0.

There is an expense transaction. The details of this transaction do not include the wallet address and the transaction does not have a transaction key, but there is network confirmation. How is this possible?

## selsta | 2020-10-29T16:16:25+00:00
Go to Settings -> Info, click on "(Change)" next to wallet restore height and then okay twice. Then wait for the wallet to refresh. If you still have issues afterwards please formulate the exact problem.

## Evgenii272 | 2020-10-30T12:49:50+00:00
> Go to Settings -> Info, click on "(Change)" next to wallet restore height and then okay twice. Then wait for the wallet to refresh. If you still have issues afterwards please formulate the exact problem.

How does this help?

Can you please answer these questions?
There is an expense transaction. The details of this transaction do not include the wallet address and the transaction does not have a transaction key, but there is network confirmation. How is this possible?

## SamsungGalaxyPlayer | 2020-12-24T16:31:39+00:00
Please use another support channel like r/MoneroSupport. Meta is not the right place for these issues.

# Action History
- Created by: Evgenii272 | 2020-10-28T13:36:18+00:00
- Closed at: 2020-12-24T16:31:39+00:00
