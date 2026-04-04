---
title: Wonky behaviour when switching wallets
source_url: https://github.com/monero-project/monero-gui/issues/1157
author: dEBRUYNE-1
assignees: []
labels:
- resolved
created_at: '2018-03-05T15:14:53+00:00'
updated_at: '2018-03-30T00:09:18+00:00'
type: issue
status: closed
closed_at: '2018-03-30T00:09:18+00:00'
---

# Original Description
Switching wallets is somewhat borked. I switched from testwallet 3 to testwallet 1, but it would display testwallet 3 as Wallet name and have no balance. After restarting the GUI it showed the correct balance and Wallet name. I should also note that this bug was hard to reproduce and was quite inconsistent. 

# Discussion History
## sanderfoobar | 2018-03-28T23:48:32+00:00
Possibly related: #1194

## sanderfoobar | 2018-03-29T23:59:14+00:00
Closing this, in favor of issue #1194, which `ui-dark-theme` has a fix for. Please re-open or create a new issue when it occurs (+reproducible steps) and verify it is not #1194.

## sanderfoobar | 2018-03-29T23:59:26+00:00
+resolved

# Action History
- Created by: dEBRUYNE-1 | 2018-03-05T15:14:53+00:00
- Closed at: 2018-03-30T00:09:18+00:00
