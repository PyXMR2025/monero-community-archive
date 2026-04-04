---
title: long payment id is truncated
source_url: https://github.com/monero-project/monero/issues/5593
author: xinyijun
assignees: []
labels: []
created_at: '2019-05-31T08:38:35+00:00'
updated_at: '2019-06-03T01:49:13+00:00'
type: issue
status: closed
closed_at: '2019-06-03T01:49:13+00:00'
---

# Original Description
I created a transfer using RPC "transfer" with payment id "223ef04ab3eb525b000000000000000000000000000000000000000000000000", and then call RPC "get_transfers", the payment id returned was truncated to the first 16 non-zero characters. It seem that the payment id will be truncated if the it ends with 48 '0'.

# Discussion History
## moneromooo-monero | 2019-05-31T09:05:32+00:00
Yes. It is intended. Is this annoying ?

## xinyijun | 2019-05-31T09:27:38+00:00
Thanks for the quick reply, it seems to be strange, is there any reason to do this? Our audit failed in this case because the payment id is inconsistent.

## moneromooo-monero | 2019-05-31T10:27:23+00:00
The reason is that short payment ids were added after long ones, and use the same system, but they're shorter, so they're padded with zeroes internally.

You should not use long payment IDs anyway. they're obsolete, and support for them may be removed soon. Subaddresses is the best thing to use, and integrated addresses (short encrypted payment IDs) a second choice.


## xinyijun | 2019-06-03T01:49:13+00:00
Ok, thanks.

# Action History
- Created by: xinyijun | 2019-05-31T08:38:35+00:00
- Closed at: 2019-06-03T01:49:13+00:00
