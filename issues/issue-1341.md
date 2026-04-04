---
title: 'Feature request: export/import all details of outputs'
source_url: https://github.com/monero-project/monero/issues/1341
author: glv2
assignees: []
labels:
- enhancement
created_at: '2016-11-15T10:25:59+00:00'
updated_at: '2018-01-08T12:48:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Would it be possible to improve the *export_outputs* command so that it also exports the extra info of outgoing transactions (recipients' addresses, etc.)?

This would allow getting back the fully detailed transaction history in a restored wallet using the *import_outputs* command.


# Discussion History
## moneromooo-monero | 2016-11-15T12:06:12+00:00
That file would be... pretty much a wallet cache file.
Without the block hashes.
So you could see that as expunging the block hashes from your cache file, and having to rescan them again in order to make it usable.
Why not backup your cache file in the first place ? Any other advantage in using such a separate file ?


## glv2 | 2016-11-15T13:29:24+00:00
When switching from version 0.9.4 to 0.10.0, I got the problem described in issue #1106. So I renamed the wallet cache file and refreshed to build a new cache file (using version 0.10.0).
But the new cache file didn't contain the recipients' addresses for outgoing transactions any more as they can't be recovered from the blockchain.

So now I have two cache files:
- The old one with the recipients' addresses of transactions that happened before block _n_
- The new one with the recipients' addresses of transactions that happened after block _n_

And I don't know of any way to merge the info of these two cache file to get a cache file with the recipients' addresses for all the payments I made.

This is why I thought it could be useful to have a way to export the payments' info from the old cache file, and import it to the new cache file to get all the details for all the payments.

But maybe the _export_outputs_ command is not the best one for this and a new _export_payment_info_ command would be more appropriate...


## moneromooo-monero | 2016-11-15T14:12:41+00:00
Since the outputs file uses the same serialization system as the cache file, it would likely have similar compatiblity problems.


## dEBRUYNE-1 | 2018-01-08T12:43:59+00:00
+enhancement

# Action History
- Created by: glv2 | 2016-11-15T10:25:59+00:00
