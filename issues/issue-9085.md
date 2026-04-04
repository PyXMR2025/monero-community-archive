---
title: Slow synchronization for 'today'-created wallet.
source_url: https://github.com/monero-project/monero/issues/9085
author: developergames2d
assignees: []
labels:
- question
- wallet
- more info needed
created_at: '2023-12-15T15:51:00+00:00'
updated_at: '2023-12-16T02:18:53+00:00'
type: issue
status: closed
closed_at: '2023-12-16T02:18:52+00:00'
---

# Original Description
I created today new wallet and sent to it some moneros. After I created onlyview-wallet on monero-gui for today date and now try to synchronize via remote daemon (node in Switzerland; I am in Siberia, Russia). But it needs 2 hours! I repeat, the first transaction of wallet was today. Other wallets on Android worked much faster.
The synchronization was fast, but the passage through the blocks is very slow.
![image](https://github.com/monero-project/monero/assets/106807841/686eaffb-3251-4732-af08-691d572d41ae)


# Discussion History
## selsta | 2023-12-15T15:55:09+00:00
can you go to Settings -> Info and share what value your wallet restore height has?

## developergames2d | 2023-12-15T16:09:26+00:00
> can you go to Settings -> Info and share what value your wallet restore height has?

1514158
I updated day to 2023-12-15, it changed to 1524238

## selsta | 2023-12-15T16:15:18+00:00
Is this a mainnet wallet? The block height should be around 3000000 if you entered the current date correctly.

## developergames2d | 2023-12-15T16:38:21+00:00
> Is this a mainnet wallet? The block height should be around 3000000 if you entered the current date correctly.

I entered 2023-12-15 (ГГГГ-ММ-ДД).
I changed to 3040000, but passage through the blocks is still slow (1-2 thousands per minute for 41000).

## selsta | 2023-12-15T16:40:26+00:00
Can you share which remote node you use? Then I can check the speed I have with it.

## developergames2d | 2023-12-15T16:43:52+00:00
> Can you share which remote node you use? Then I can check the speed I have with it.

178.22.107.109:18081

## selsta | 2023-12-15T19:08:54+00:00
I can sync around 500 blocks / second with this remote node.

## selsta | 2023-12-16T02:18:52+00:00
I don't think there is a bug here, maybe a node closer to you will result in faster sync.

# Action History
- Created by: developergames2d | 2023-12-15T15:51:00+00:00
- Closed at: 2023-12-16T02:18:52+00:00
