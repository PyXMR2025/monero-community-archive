---
title: monero not appearing in monero GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/4296
author: fentyman
assignees: []
labels: []
created_at: '2024-03-20T17:40:35+00:00'
updated_at: '2024-03-20T18:14:14+00:00'
type: issue
status: closed
closed_at: '2024-03-20T18:14:14+00:00'
---

# Original Description
i just just installed monero GUI wallet and purchased monero on localmonero.com from a high reputation seller using paypal. its been 2 days and localmonero says the transaction is complete and the monero should be in my wallet, but when i open my wallet it shows nothing has been added. i have just installed the app and the daemon still has blocks remaing. is there a fix to this or have i been scammed.

# Discussion History
## selsta | 2024-03-20T17:43:31+00:00
Please go to Settings -> Info and share

- Version
- Wallet mode
- Wallet restore height

> i have just installed the app and the daemon still has blocks remaing

You have to connect to a fully synced up daemon for your funds to show up. If there are blocks remaining it means you are still syncing the blockchain.

## fentyman | 2024-03-20T17:45:55+00:00
GUI version: 0.18.3.2-unknown (Qt 5.15.12)
Embedded Monero version: 0.18.3.2-unknown
Wallet restore height: 3089362
Wallet mode: Advanced mode (Local node)

how long does it usally take to sync i have 1786897 blocks left

## selsta | 2024-03-20T17:47:47+00:00
Syncing will take between 24h and a couple days depending on your hardware and if your blockchain is stored on SSD.

## fentyman | 2024-03-20T17:54:05+00:00
ok thanks for your help :)

# Action History
- Created by: fentyman | 2024-03-20T17:40:35+00:00
- Closed at: 2024-03-20T18:14:14+00:00
