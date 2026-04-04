---
title: Monero transaction missing from GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/4305
author: SidelinedGazelle
assignees: []
labels: []
created_at: '2024-04-09T14:51:04+00:00'
updated_at: '2024-04-09T15:16:57+00:00'
type: issue
status: closed
closed_at: '2024-04-09T15:15:48+00:00'
---

# Original Description
I bought some monero from localmonero.co and on the site it says the transaction is complete but i cant see the transaction or the monero in my wallet.
when i check the transaction on https://xmr.llcoins.net/checktx.html it says "Failed to get transaction data! Perhaps LocalMonero is down?"
i think my GUI wallet program hadn't been updated when i made the transaction but i have since updated it and still nothing.
i have tried to refresh the wallet and when it was syncing i saw the wallet balance go up briefly to the right amount but when it finished it was down again.
anyone have any idea what would cause this?
thanks in advance for any help anyone can provide


# Discussion History
## selsta | 2024-04-09T14:52:28+00:00
Please go to Settings -> Info and share

- Version
- Wallet mode
- Wallet restore height

## SidelinedGazelle | 2024-04-09T14:55:32+00:00
Hi,
Version: 0.18.3.3-unknown (Qt 5.15.13)
Wallet mode: Advanced mode (Remote node)
Wallet restore height: 3101668

## selsta | 2024-04-09T14:56:51+00:00
What does it say in the bottom left corner?

## SidelinedGazelle | 2024-04-09T14:59:36+00:00
Wallet is synchronized
Deamon is synchronized (3117947)
Network status
Remote node

## selsta | 2024-04-09T15:00:33+00:00
Can you go to Settings -> Wallet, click on Scan transaction and enter the tx_id that is missing from your wallet?

## SidelinedGazelle | 2024-04-09T15:02:40+00:00
it says "failed to scan transaction: failed to scan transaction: failed to get transaction from deamon"

## selsta | 2024-04-09T15:08:43+00:00
What remote node are you using?

## SidelinedGazelle | 2024-04-09T15:09:45+00:00
http://157.90.234.17
18089

## selsta | 2024-04-09T15:11:28+00:00
This node isn't even synced up, try a different one.

## SidelinedGazelle | 2024-04-09T15:12:23+00:00
is this one ok?
88.198.199.23
18081

## selsta | 2024-04-09T15:12:41+00:00
yes, try this one

## SidelinedGazelle | 2024-04-09T15:14:50+00:00
Yay!! that fixed it, thanks alot, i was really starting to panic

## selsta | 2024-04-09T15:16:09+00:00
it's a good idea to add a couple nodes from monero.fail so that you can switch if one is causing issues

## SidelinedGazelle | 2024-04-09T15:16:56+00:00
yeh i'll do that, thanks :]

# Action History
- Created by: SidelinedGazelle | 2024-04-09T14:51:04+00:00
- Closed at: 2024-04-09T15:15:48+00:00
