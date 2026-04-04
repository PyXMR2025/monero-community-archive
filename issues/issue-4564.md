---
title: 'Cannot open Ledger-backed wallet: Wrong Device Status: 0x6985'
source_url: https://github.com/monero-project/monero-gui/issues/4564
author: haplo
assignees: []
labels: []
created_at: '2026-01-30T17:00:37+00:00'
updated_at: '2026-01-30T18:29:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have a password-protected Ledger-backed Monero wallet, created years ago, that fails to open with Monero GUI.

Monero installed from Arch Linux AUR, version 0.18.4.5-1.

Full steps:

1. Connect Ledger, enter PIN, set up passphrase, open Monero app
2. Start Monero GUI
3. Open wallet file, enter password
4. Ledger Monero app prompts to export view keys
5. On accept, the app closes on Ledger, it goes back to the app list, instead of going back to the Monero app main screen as usual.
6. Monero GUI displays an error and the wallet doesn't open. The full error on console:

```
Wrong Device Status: 0x6985 (SW_WRONG_DATA_RANGE), EXPECTED 0x9000 (UNKNOWN), MASK 0xffff
Error opening wallet: Wrong Device Status: 0x6985 (SW_WRONG_DATA_RANGE), EXPECTED 0x9000 (UNKNOWN), MASK 0xffff
Error opening wallet with password:  Wrong Device Status: 0x6985 (SW_WRONG_DATA_RANGE), EXPECTED 0x9000 (UNKNOWN), MASK 0xffff
```

Ledger firmware and Monero app are up to date to latest versions. I tried reinstalling the Monero app.

Other Ledger-backed wallet created at the same time, also password protected, opens and transacts just fine. The only difference I can see is that the broken wallet uses a passphrase in the Ledger device.

# Discussion History
## selsta | 2026-01-30T17:03:09+00:00
Please share which Ledger device you use and which monero-gui version you use.

## haplo | 2026-01-30T17:05:04+00:00
> Please share which Ledger device you use and which monero-gui version you use.

Monero installed from Arch Linux AUR, version 0.18.4.5-1, Ledger Nano S Plus.

Thanks @selsta.

## selsta | 2026-01-30T17:10:00+00:00
Unfortunately Ledger did changes to their app, it's possible that they did not do any testing with passphrase.

I would recommend opening an issue here and contacting Ledger support.

https://github.com/LedgerHQ/app-monero

Alternatively you can use python software to convert your Ledger passphrase and seed to a monero seed.

https://github.com/LedgerHQ/app-monero/tree/develop/tools/python

## haplo | 2026-01-30T17:11:58+00:00
> Unfortunately Ledger did changes to their app, it's possible that they did not do any testing with passphrase.
> 
> I would recommend opening an issue here and contacting Ledger support.
> 
> https://github.com/LedgerHQ/app-monero

It seems likely that its a bug on their end, I will open an issue there. Thanks!

## haplo | 2026-01-30T18:04:58+00:00
I think the problem might be with the Monero wallet itself, as creating a new wallet restoring from the Ledger worked fine. The wallet was created in 2022, so maybe some incompatible change was introduced at some point after that?

## selsta | 2026-01-30T18:29:59+00:00
Wallet cache incompatibility looks different. The fact that the Ledger monero app itself crashes indicates a bug in their code. I'm not aware of any changes recently made on monero's side that would explain this.

# Action History
- Created by: haplo | 2026-01-30T17:00:37+00:00
