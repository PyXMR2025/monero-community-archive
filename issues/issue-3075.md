---
title: 'Transfer: advanced options are enabled in view-only wallet of hardware wallet'
source_url: https://github.com/monero-project/monero-gui/issues/3075
author: rating89us
assignees: []
labels: []
created_at: '2020-09-07T20:32:56+00:00'
updated_at: '2020-09-13T06:14:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It is possible to create a view-only wallet file for a hardware wallet. The main advantage is that user can monitor incoming transactions without having to plug in the device. However there are some problems:
- Balance of view-only wallet is wrong (can't refresh key images) (see #2952)
- User can't create a transaction for offline tx signing (see https://www.reddit.com/r/monerosupport/comments/io67bw/offline_signing_with_trezor_t_hardware_wallet/)

Since offline tx signing isn't supported with hardware wallet view-only wallets, we should disable all advanced options buttons for this type of wallet.

# Discussion History
# Action History
- Created by: rating89us | 2020-09-07T20:32:56+00:00
