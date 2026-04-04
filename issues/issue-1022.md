---
title: Bug with payment ID
source_url: https://github.com/monero-project/monero-gui/issues/1022
author: ghost
assignees: []
labels:
- bug
- resolved
created_at: '2017-12-13T20:29:32+00:00'
updated_at: '2018-03-30T02:32:16+00:00'
type: issue
status: closed
closed_at: '2018-03-30T01:27:22+00:00'
---

# Original Description
When jumping between wallets on Mac OS GUI a small bug.
If you randomly generate payment ID, and the payment ID field fills. Then proceed to close that wallet and open up a new wallet (without exiting the program), the same payment ID field is still filled in new wallet but with the previous payment ID.
The field doesn't clear when opening new wallet unless you manually clear it. It's a like cache that doesn't clear.

When jumping between wallets, need the payment ID field to be empty and not carry over payment ID field.


# Discussion History
## dEBRUYNE-1 | 2017-12-14T14:56:57+00:00
This wouldn't cause any issues for what it's worth, but it should still generate a new one. 

+bug

## sanderfoobar | 2018-03-30T01:16:22+00:00
Since #952, the receive page has switched to subadresses.

## sanderfoobar | 2018-03-30T01:16:26+00:00
+wontfix

# Action History
- Created by: ghost | 2017-12-13T20:29:32+00:00
- Closed at: 2018-03-30T01:27:22+00:00
