---
title: Synchronization optimization - parallel block queu pre-calculation
source_url: https://github.com/monero-project/monero/issues/3769
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-05-07T04:31:52+00:00'
updated_at: '2018-08-15T11:27:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So, unfortunately I can't tell if [the block quue](https://github.com/monero-project/monero/blob/36241552b56b156c08319935baf7afda12deb3c5/src/cryptonote_protocol/block_queue.cpp) already has this in it, but basically, when monerod has downloaded a bunch of different spans, it can begin processing them out of order and thus in a parallel fashion.

So, I presume the block queue is simply downloading spans of blocks and then storing them in a manner that they are readily accessible for their linear inclusion into the blockchain as they are linearly verified. 

Could we instead perform validations on the spans before they are linear?

so, here X's are the fully verified blocks. A's represent span 1, B's represent span 2, etc. For ease of diagramming the first block of each span is noted with the prime ' notation

XXXXXXA'AAAAAB'BBBBBBBBBC'CCCCD'DDD

The A span can begin validation immediately, because it is directly upstream of the fully validated blockchain (X's). The B span, however, would have to wait until the A span is validated to begin validation. 

Instead, the B span can treat B' as ground truth pending the validation of A span. Transactions in B that reference transactions in A will just have to wait, but otherwise the rest of B span can be validated. If there are references from B to A then the queue program can just treat A and B as a single span. Otherwise, the spanning can be programmed to work within the locktime of monero transactions (i.e., you have to wait n blocks until you can spend an output). 

@moneromooo-monero  , if this is indeed what your span thing has done, then ... i guess there just needs to be better documentation so I don't go reinventing the wheel. 

# Discussion History
## iamsmooth | 2018-06-15T22:40:47+00:00
> the B span can treat B' as ground truth pending the validation of A span

I believe this would be quite difficult (even impossible) as much of the structure necessary to validate signatures, such as output indexes, is only created when blocks are actually added to the main chain.

However some aspects can be validated without waiting to be added to the chain, such as PoW, range proofs, etc. Some of this might already be done now though.

## moneromooo-monero | 2018-08-15T11:27:26+00:00
There is no out of order validation now, beyond sanity checking.
PoW is usually disabled for historical block due to the embedded HoH data.
It might be that range proof and similar things may be better off checked even if the data the blocks depend on is not yet there, but typically the queue fills faster than it gets checked, and holes aren't that common (though I suppose it might depend on your internet connection, if some links break).
Not something I want to spend time on now, it seems high work and low reward at first glance.

# Action History
- Created by: Gingeropolous | 2018-05-07T04:31:52+00:00
