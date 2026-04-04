---
title: Information leak in logs and on console.
source_url: https://github.com/monero-project/monero-gui/issues/3022
author: ronohara
assignees: []
labels: []
created_at: '2020-07-23T11:17:48+00:00'
updated_at: '2020-07-23T11:47:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This log and console message (I have changed the values) leaks sensitive financial information.

2020-07-23 11:10:12.062     7f4c6d2b2700        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3515     Refresh done, blocks received: 5095, balance (all accounts): 12.99956956117, unlocked: 12.99956956117

EDIT

I suggest it simply says something like:

2020-07-23 11:10:12.062     7f4c6d2b2700        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3515     Refresh done, blocks received: 5095, log in to the wallet to check your balance(s)

# Discussion History
# Action History
- Created by: ronohara | 2020-07-23T11:17:48+00:00
