---
title: Can't create wallet from hardware device
source_url: https://github.com/monero-project/monero-gui/issues/3190
author: gmcintyre-conga
assignees: []
labels: []
created_at: '2020-10-24T00:46:20+00:00'
updated_at: '2020-11-10T22:22:22+00:00'
type: issue
status: closed
closed_at: '2020-11-10T22:22:22+00:00'
---

# Original Description
using gui wallet 0.171.1, when I try to create wallet from hardware (NanoX), I receive this error:

failed to generate new wallet: Wrong Device Status 0x6e00 (SW_CLA_NOT_SUPPORTED), EXPECTED 0x9000 (SW_OK), Mask 0xffff

I've tried on Mac Mojave & Windows 10. Tried re-installing Monero app on NanoX. Nothing works.

# Discussion History
## selsta | 2020-10-24T00:52:30+00:00
You need the latest version of Ledger Live, Ledger firmware 1.6.1 and Ledger Monero app 1.7.4

## gmcintyre-conga | 2020-11-10T02:42:41+00:00
I don't see a version 1.6.1 available for the Nano X, only for Nano S. The support page only shows me 1.2.4-4, which is already on my device. 
To be clear, this is the url I'm looking at --> https://support.ledger.com/hc/en-us/articles/360013349800-Update-Ledger-Nano-X-firmware

Also, I do have another new Nano X that I could try if you think it might be specific to my device, but both were purchased at the same time.

Thanks for your help.

## selsta | 2020-11-10T06:00:08+00:00
Yes, Ledger Nano X has a different firmware. Do you have Ledger Monero app 1.7.4 installed?

## gmcintyre-conga | 2020-11-10T14:28:31+00:00
on the device itself, yes. It says Spec 1.0, App 1.7.4

## xiphon | 2020-11-10T14:37:05+00:00
`SW_CLA_NOT_SUPPORTED` means Ledger Monero app rejects Monero GUI version.

Make sure you are using the latest Monero GUI (v0.17.1.4) and Ledger Monero app (1.7.4 is okay).


## gmcintyre-conga | 2020-11-10T22:22:22+00:00
got it. v0.17.1.4 did the trick. thanks again.

# Action History
- Created by: gmcintyre-conga | 2020-10-24T00:46:20+00:00
- Closed at: 2020-11-10T22:22:22+00:00
