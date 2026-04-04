---
title: Balance does not show
source_url: https://github.com/monero-project/monero-gui/issues/3206
author: MrTrewar
assignees: []
labels: []
created_at: '2020-11-02T14:00:59+00:00'
updated_at: '2020-11-02T15:56:49+00:00'
type: issue
status: closed
closed_at: '2020-11-02T15:56:48+00:00'
---

# Original Description
Hi, sorry for the question i'm new to this.
But I send an amount of mxr to the gui wallet and the when i check the prove/check Verification it says

"This address received 1.200000000000 monero, with 555 confirmation(s)."

But it does not show the balance in my wallet.

Do i need to wait longer?

kind regards

# Discussion History
## xiphon | 2020-11-02T14:17:01+00:00
Make sure your wallet restore height is less than the transaction height (`Settings` -> `Info` tab).

You can rescan the blockchain: click on wallet restore height `(Change)` -> `Ok` (keep the same wallet restore height value).

## MrTrewar | 2020-11-02T14:21:36+00:00
transaction height is now less, but still no change 
i rescanned also
but when i send it, my wallet height was the same as the transaction height

## xiphon | 2020-11-02T14:47:48+00:00
Do you see a tx in the block explorer? Make sure your node is synced with the network.

## MrTrewar | 2020-11-02T15:55:56+00:00
hi there, problem solved
conclusion: i was stupid, i put the block height to YYYYMMDD  instead of YYYY-MM-DD, resulting in a very big block height
dumb solution: put the block height real low 13500 and waited

sorry and thank you
kind regards

## MrTrewar | 2020-11-02T15:56:48+00:00

:)

# Action History
- Created by: MrTrewar | 2020-11-02T14:00:59+00:00
- Closed at: 2020-11-02T15:56:48+00:00
