---
title: show_transfers history doersn't restore if view only wallet cache is deleted
source_url: https://github.com/monero-project/monero/issues/1427
author: rndbr
assignees: []
labels:
- enhancement
created_at: '2016-12-10T20:06:08+00:00'
updated_at: '2018-01-08T12:48:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
creating this off of #1406 (I closed that because it was a bit jumbled, and one of the two issues was fixed... this ticket documents the remaining, lower priority issue):

if you have a view wallet, perform a transaction on it, with the new code things work well, and the outgoing tx shows in `show_transfers`, no problem. if you then call `rescan_bc`, and then re-import the key images from the cold wallet, it appears that `show_transfers` doesn’t show outgoing transactions. balance output is correct, though....

# Discussion History
## moneromooo-monero | 2016-12-11T14:07:41+00:00
A view only wallet only sees incoming transfers. You need to spend key to see outgoing transfers.

There will be a "hybrid" rescan-with-key-images-set function at some point, that will solve this, but not right now.

## dEBRUYNE-1 | 2018-01-08T12:44:45+00:00
+enhancement

# Action History
- Created by: rndbr | 2016-12-10T20:06:08+00:00
