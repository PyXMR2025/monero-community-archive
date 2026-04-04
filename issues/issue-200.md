---
title: wrong info about height for alternative chain?
source_url: https://github.com/monero-project/monero-docs/issues/200
author: jermanuts
assignees: []
labels: []
created_at: '2025-08-06T22:47:19+00:00'
updated_at: '2025-09-12T00:45:24+00:00'
type: issue
status: closed
closed_at: '2025-09-12T00:45:24+00:00'
---

# Original Description
from Ruck in MRL:

>The docs seem wrong https://docs.getmonero.org/rpc-library/monerod-rpc/#get_alternate_chains
height - unsigned int; the block height of the first diverging block of this alternative chain

>I think `height` here is the block height of the _last_ diverging block of the alternative chain.

if it is indeed not correct, then need to update info in https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_alternate_chains too.

# Discussion History
## nahuhh | 2025-08-06T23:02:36+00:00
> if it is indeed not correct, then need to update info in https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_alternate_chains too.


the above page is deprecated. won't be updating it.
will confirm rucks finding and update monero-docs



# Action History
- Created by: jermanuts | 2025-08-06T22:47:19+00:00
- Closed at: 2025-09-12T00:45:24+00:00
