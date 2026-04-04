---
title: GUI Not Clearing Password After Wallet Creation
source_url: https://github.com/monero-project/monero-gui/issues/3794
author: spackle-xmr
assignees: []
labels: []
created_at: '2021-12-11T17:58:00+00:00'
updated_at: '2022-01-01T17:49:54+00:00'
type: issue
status: closed
closed_at: '2022-01-01T17:49:54+00:00'
---

# Original Description
When using the GUI to create a set of wallets, the password used for the initial wallet was still filled in on the 'Give your wallet a password' screen when creating a second wallet. This is repeatable, in that if a second wallet is created it's password will still be entered when creating a third.
This was observed using the latest release (0.17.3.0) on Windows.

# Discussion History
## selsta | 2021-12-11T18:00:35+00:00
@rating89us Can you check this? IIRC there were some changes to this recently.

## rating89us | 2021-12-11T18:47:43+00:00
I can't reproduce this issue on Windows (tried creating two new wallets and restoring two wallets).

## selsta | 2021-12-11T18:48:48+00:00
At first I also couldn't reproduce but after trying a couple times I was able to reproduce, don't know why exactly or what I did differently.

## rating89us | 2021-12-11T18:50:59+00:00
I could reproduce now, will investigate what is causing this.

# Action History
- Created by: spackle-xmr | 2021-12-11T17:58:00+00:00
- Closed at: 2022-01-01T17:49:54+00:00
