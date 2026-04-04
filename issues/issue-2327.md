---
title: viewonly wallet showing different balance to spend wallet
source_url: https://github.com/monero-project/monero/issues/2327
author: 4Reallive
assignees: []
labels:
- invalid
created_at: '2017-08-22T12:59:28+00:00'
updated_at: '2017-08-22T17:48:14+00:00'
type: issue
status: closed
closed_at: '2017-08-22T17:48:14+00:00'
---

# Original Description
I have a view only wallet showing a different balance to the spend wallet.

I have rescan_bc and refreshed the wallet.
Both wallets are syncing on the same node.
I suspect that the view-only wallet is not detecting the spends as on the rescan i only see purple (spends) on the spend wallet and only green (received) on the view only.

I thought that i had a surprise payday and people may freak out when they see their wallet in credit when it is not.

What are the best diagnostics i can provide so that you can see the failure, I am technically very capable and see myself contributing in future.

Thanks for all your hard work on this so far, this is an amazing project.

# Discussion History
## expez | 2017-08-22T14:09:15+00:00
> I suspect that the view-only wallet is not detecting the spends as on the rescan i only see purple (spends) on the spend wallet and only green (received) on the view only.

This is true and it's working as intended.  You need to read about key images and how to export and import them into your view only wallet so you can keep it up to date with spending.

## moneromooo-monero | 2017-08-22T17:44:16+00:00
Closing, please reopen if it's still wrong after importing key images.

+invalid

# Action History
- Created by: 4Reallive | 2017-08-22T12:59:28+00:00
- Closed at: 2017-08-22T17:48:14+00:00
