---
title: 'Feature request: differentiate view-only wallet types (from hardware wallet
  x normal)'
source_url: https://github.com/monero-project/monero-gui/issues/3086
author: rating89us
assignees: []
labels: []
created_at: '2020-09-13T06:12:34+00:00'
updated_at: '2020-09-13T06:29:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Many users are creating view-only wallets of hardware wallets to monitor incoming transactions without having to plug in the device. However, our code doesn't differentiate a view-only wallet of a hardware wallet from a normal view-only wallet. Both return false for `appWindow.currentWallet.isHwBacked()`.

This is a problem because some functionality (like import of key images and offline transaction signing) is available only for normal view-only wallets, and should be disabled for view-only wallets of hardware wallets. Also, the instruction messages in send page should be different for each type.

# Discussion History
# Action History
- Created by: rating89us | 2020-09-13T06:12:34+00:00
