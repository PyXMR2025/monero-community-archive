---
title: Ringsize / mixin still mixed up here and there
source_url: https://github.com/monero-project/monero/issues/4040
author: Gingeropolous
assignees: []
labels:
- invalid
created_at: '2018-06-23T03:24:18+00:00'
updated_at: '2018-07-12T23:01:04+00:00'
type: issue
status: closed
closed_at: '2018-07-12T23:01:04+00:00'
---

# Original Description
Is there a reason for this? I don't know exactly where, but according to 

https://www.reddit.com/r/Monero/comments/8sz02k/update_monerujo_159_maximum_nacho/e1402ag/

and from what i've seen on the block explorers, there must be some cases in the code where they are still referring to mixin and not ringsize, because there are some ringsize 8 transactions that are frequently pumped out. 

so someone is clearly feeding 7 into a parameter that is mixin, so the total ringsize is 8. 

is there a reason its not unified / standardized?

# Discussion History
## moneromooo-monero | 2018-06-23T08:24:19+00:00
RPC accepts both, ring size takes priority.


## shopglobal | 2018-06-23T08:54:39+00:00
wallet_rpc_server is using ring_size from request as default, but some pool software is using req.mixin and so we should just add some logic to accept both. As long as that's been handled it won't be a major concern.

I think it's good the way it is 
https://github.com/monero-project/monero/blob/4e7897e57ca9b580e7ad132bfdc0e9ba097b04e0/src/wallet/wallet_rpc_server.cpp#L797

The pools that don't have the correct configurations will be sending with the wrong mixins if we don't allow both

## moneromooo-monero | 2018-07-12T22:13:14+00:00
Reopen if you have some tangible information about something being wrong. I know of nothing missing.

+invalid


# Action History
- Created by: Gingeropolous | 2018-06-23T03:24:18+00:00
- Closed at: 2018-07-12T23:01:04+00:00
