---
title: Monero GUI Crashes When Exporting Seed Using Ledger
source_url: https://github.com/monero-project/monero-gui/issues/4413
author: jostpay
assignees: []
labels: []
created_at: '2025-02-21T04:02:44+00:00'
updated_at: '2025-02-23T06:41:32+00:00'
type: issue
status: closed
closed_at: '2025-02-23T06:41:31+00:00'
---

# Original Description
I am experiencing a crash in Monero GUI when I attempt to export my seed using my Ledger device. The application immediately terminates and generates a crash report. My Ledger firmware is up to date, and I have verified that Monero GUI is the latest version. I need help, what can i do, see the crash report attached


[crash-report.pdf](https://github.com/user-attachments/files/18900256/crash-report.pdf)

# Discussion History
## selsta | 2025-02-21T12:06:55+00:00
Did this suddenly start happening or were you never able to get monero-gui + Ledger working?

## jostpay | 2025-02-21T12:13:14+00:00
It started happening suddenly. In fact, I accessed my Monero account just a few hours before it began crashing.

## selsta | 2025-02-21T17:00:38+00:00
Can you try re-creating the Ledger wallet with a different file name and check if the issue is still happening? You don't have to delete the existing wallet.

## jostpay | 2025-02-21T19:08:05+00:00
I created a new wallet under a different name and encountered the same crash. After setting up the wallet, when I enter my password and tap on "Export Wallet" on the Ledger device, it crashes immediately. I have attached the crash report for reference.  

However, when I create a standard wallet on the Monero GUI without using the hardware, it functions properly.

[new_wallet_crash_report.pdf](https://github.com/user-attachments/files/18914142/new_wallet_crash_report.pdf)

## selsta | 2025-02-21T19:12:50+00:00
Do you remember doing anything Ledger related before this started happening? Like use a new program together with Ledger, update firmware, etc?

## jostpay | 2025-02-21T19:19:20+00:00
I think i updated the ledger live. 

## selsta | 2025-02-21T19:36:22+00:00
Just updating Ledger Live should not be relevant. Can you try to restart your Mac and only start monero-wallet-gui and see if it works?

## jostpay | 2025-02-23T06:41:31+00:00
The issue persisted, so I downloaded the Monero GUI on another computer. I imported my key from the original computer, synced it from the beginning, and it worked fine. Thank you for your help!

# Action History
- Created by: jostpay | 2025-02-21T04:02:44+00:00
- Closed at: 2025-02-23T06:41:31+00:00
