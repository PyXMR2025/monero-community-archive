---
title: Can't change wallet restore height after restoring a wallet
source_url: https://github.com/monero-project/monero-gui/issues/2463
author: rating89us
assignees: []
labels: []
created_at: '2019-11-23T22:03:21+00:00'
updated_at: '2021-06-16T19:53:27+00:00'
type: issue
status: closed
closed_at: '2021-06-16T19:53:27+00:00'
---

# Original Description
I was recovering a wallet from seed and forgot to add my wallet restore height.

So I tried to change it in Settings > Info during the sync, but it didn't work, because the wallet kept returning its value to 0.

I'm using GUI 0.15.0.1 in Windows.

Steps to reproduce:
1. Import a wallet from seed
2. Don't set a restore height
3. Select remote node
4. Wallet will start sync from block 0
5. Go to Settings > Info and change _Wallet restore height_ to a higher height (I set 1819000)
6. Confirm the prompt about the wallet cache
7. Wallet automatically returns to restore height = 0 and start sync from the block 0 again.

# Discussion History
## selsta | 2020-02-25T23:01:55+00:00
Does this happen latest master version?

## rating89us | 2021-06-14T19:23:16+00:00
Yes, it's still present and it's probably the same bug of this user: 
- https://www.reddit.com/r/monerosupport/comments/nuny84/restoring_hardware_wallet_monerowallet_gui/
- https://www.reddit.com/r/monerosupport/comments/nuny84/restoring_hardware_wallet_monerowallet_gui/h1238qi

PR #3563 fixes this bug.

# Action History
- Created by: rating89us | 2019-11-23T22:03:21+00:00
- Closed at: 2021-06-16T19:53:27+00:00
