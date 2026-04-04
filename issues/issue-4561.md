---
title: Transactions keep failing on Moneiro GUI Wallet
source_url: https://github.com/monero-project/monero-gui/issues/4561
author: SabriMercimek
assignees: []
labels: []
created_at: '2026-01-23T14:19:44+00:00'
updated_at: '2026-01-24T09:12:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello everybody

Last Sunday I have successfully transferred a small amount (0.3) XMR from my Monero GUI wallet. Last Tuesday I then tried to send some more XMR however the transaction failed. What is even stranger is that the amount of XMR in my account doubled! I have tried multiple times sending XMR out of my Monero Gui wallet however without succes (they all fail). Please see below:

<img width="1226" height="830" alt="Image" src="https://github.com/user-attachments/assets/3263cc98-050b-41ac-a633-db9c280c525d" />

I have not connected my wallet to a Ledger. The wallet is synchronized and the deamon is synchronized and connected. I have tried switching public note, and updating the wallet to the latest version. Anyone knows how I can fix this issue?

Help is much appreciated,

Kind regards,

Sabri

Extra info: 

GUI version: 0.18.4.5-unknown (Qt 5.15.17)

>>> status
[23/01/2026 15:17] 2026-01-23 14:17:12.312 I Monero 'Fluorine Fermi' (v0.18.4.5-release) 
Height: 3594152/3594152 (100.0%) on mainnet, bootstrapping from 99.26.189.25:18081, local height: 1 (0.0%), not mining, net hash 6.70 GH/s, v16, 0(out)+0(in) connections

# Discussion History
## selsta | 2026-01-23T14:21:46+00:00
Could you try restoring your wallet from seed and see if you can transact again?

## SabriMercimek | 2026-01-24T09:12:17+00:00
Thank you that solved the issue!

# Action History
- Created by: SabriMercimek | 2026-01-23T14:19:44+00:00
