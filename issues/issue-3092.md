---
title: 'Ghostrider fork: Mike, Vkax mining'
source_url: https://github.com/xmrig/xmrig/issues/3092
author: Alphafox992
assignees: []
labels: []
created_at: '2022-07-21T18:54:03+00:00'
updated_at: '2025-06-28T10:42:38+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:42:38+00:00'
---

# Original Description
There is a rapidly increasing popularity for Mike, or Vkax mining, and currently the only miner is rplant opt.

Xmrig supports ghostrider already, and Mike is a subset of ghostrider; shouldn't take any brand New code.

My attempts to add and compile from source however have been fruitless. Ends up losing sync after a few blocks... 

Thank you for the wonderful software.

# Discussion History
## Spudz76 | 2022-07-22T00:24:14+00:00
If it scrambles the chosen set of sub-algos more often than regular Ghostrider that might be why you had trouble, the count of blocks until re-selection is fairly hard-coded several places in the current implementation (I think).

## Alphafox992 | 2022-07-22T19:15:23+00:00
Restarting work with each job seems to work much better, but still getting desync.... Any other help?

I'm WELL outside my depth.
Happy to pay for Mike algo integration.

# Action History
- Created by: Alphafox992 | 2022-07-21T18:54:03+00:00
- Closed at: 2025-06-28T10:42:38+00:00
