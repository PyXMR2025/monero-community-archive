---
title: monero-wallet-cli seems to append ".keys" to wallet input, and fails to find
  the wallet
source_url: https://github.com/monero-project/monero/issues/3363
author: grubles
assignees: []
labels: []
created_at: '2018-03-06T23:22:35+00:00'
updated_at: '2018-03-07T17:06:04+00:00'
type: issue
status: closed
closed_at: '2018-03-07T17:06:04+00:00'
---

# Original Description
v0.11.1.0-master-c7ace5fa

Example:
```
Error: failed to load wallet: file not found "yourwallet.keys-watchonly.keys"
```
When the wallet is actually named `yourwallet.keys-watchonly`

# Discussion History
## grubles | 2018-03-06T23:34:10+00:00
Actually, the issue is that `monero-wallet-cli` saves watch-only wallets in that naming format (`wallet.keys-watchonly`), but apparently does not recognize it if specified with `--wallet-file`.

## moneromooo-monero | 2018-03-06T23:55:06+00:00
That file is a keys file. You have to rename it to something.keys, which admittedly is a bit naff and will be changed when I get to it.

## moneromooo-monero | 2018-03-07T13:56:27+00:00
https://github.com/monero-project/monero/pull/3369

# Action History
- Created by: grubles | 2018-03-06T23:22:35+00:00
- Closed at: 2018-03-07T17:06:04+00:00
