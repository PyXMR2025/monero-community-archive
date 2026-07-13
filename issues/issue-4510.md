---
title: Wallet creation fails when wallet directory is a link to another drive (Windows)
source_url: https://github.com/monero-project/monero-gui/issues/4510
author: mesvam
assignees: []
labels: []
created_at: '2025-10-16T05:02:10+00:00'
updated_at: '2026-07-11T13:58:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Platform: Windows

To reproduce:

- Create a link to another drive. e.g. `mklink /J C:\link D:\` for hardlink/junction, `mklink /J C:\link D:\` for symlink (may require admin privileges)
- Create wallet in a directory through the link, e.g. at `C:\link\wallets` (for symlinks, need to manually enter the path rather than use directory selection GUI, since the GUI resolves the symlink)

Symptoms

- At the final step, when you click "Create wallet", get an error message "Failed to store the wallet"
- in `monero-wallet-gui.log` see `ERROR	WalletAPI	src/wallet/api/wallet.cpp:972	Error saving wallet: boost::filesystem::weakly_canonical: The request is not supported`

Opening a wallet within a link still works

# Discussion History
## mialily1222-del | 2026-06-16T20:38:50+00:00
@mesvam have you been able to resolve this issue?

## mesvam | 2026-07-03T20:48:19+00:00
Workaround is to create wallet somewhere else, then move it to desired location

## Noisetteer | 2026-07-11T12:55:15+00:00
i got the same error at the end but i only have 1 drive so does i just make a other files and tries on it? cuz its still on same the drive (windows)

edit : works on the same drive so you just need to make the wallet somewhere else and then it works

# Action History
- Created by: mesvam | 2025-10-16T05:02:10+00:00
