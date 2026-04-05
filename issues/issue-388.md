---
title: A new consistent API in addition to the existing RPC and "Daemon" APIs
source_url: https://github.com/Cuprate/cuprate/issues/388
author: Har01d
assignees: []
labels:
- C-proposal
created_at: '2025-03-01T11:45:26+00:00'
updated_at: '2025-03-25T18:54:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`monerod` has a somewhat inconsistent API. For example, getting block data is done using the `get_block` method of the RPC API, but to fetch transaction data we need to use the `/get_transactions` endpoint of another API (which doesn't adhere to the RPC API standard).

While maintaining compatibility with `monerod` is great, it'd be also nice to have something more consistent. Also, it'd be nice to include transaction data to `get_block`. This would add new use cases to `cuprate`.

Thanks for the great work!

# Discussion History
## spirobel | 2025-03-25T18:54:57+00:00
I agree with this sentiment 100%

just to add: getblocks.bin is the most used endpoint and it includes the transactions. Here is a recently happening change to this endpoint (worth a read to get context) https://github.com/monero-project/monero/pull/9381

# Action History
- Created by: Har01d | 2025-03-01T11:45:26+00:00
