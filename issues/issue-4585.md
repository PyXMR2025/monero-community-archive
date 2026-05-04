---
title: '[Bug] MacOS App crashes when restoring Monero wallet from Ledger hardware
  device'
source_url: https://github.com/monero-project/monero-gui/issues/4585
author: RamsDark
assignees: []
labels: []
created_at: '2026-05-03T21:09:01+00:00'
updated_at: '2026-05-03T21:36:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When attempting to restore a Monero wallet using a Ledger physical device, the application crashes unexpectedly.

Steps to Reproduce :

Open the application
Select "Restore wallet from device"
Connect and unlock the Ledger device
→ App crashes with provided logs in the attached file 

OS: MacOS M1 15.7.4
App version: 0.18.4.7-release (Qt 5.15.13)
Ledger model: Ledger Nano X

Logs in the attached file

[scratch_10.txt](https://github.com/user-attachments/files/27324724/scratch_10.txt)

# Discussion History
## selsta | 2026-05-03T21:15:47+00:00
Do you have all other applications closed that might connect to Ledger? Do you have to monero Ledger app open? Did it work in the past?

## RamsDark | 2026-05-03T21:17:56+00:00
I only have Ledger live open along side, first time use it with hardware wallet

## selsta | 2026-05-03T21:18:47+00:00
Can you try having Ledger Live closed

## RamsDark | 2026-05-03T21:36:49+00:00
Still same, have to relaunch the app to access the wallet, but always fails on first restoring -> click on relaunch the app on the error report window it restart the app with access to the wallet

# Action History
- Created by: RamsDark | 2026-05-03T21:09:01+00:00
