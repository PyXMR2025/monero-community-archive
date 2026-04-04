---
title: '[Suggestion] Daemon RPC: submit_block improvements'
source_url: https://github.com/monero-project/monero/issues/8874
author: duggavo
assignees: []
labels: []
created_at: '2023-05-24T16:11:41+00:00'
updated_at: '2023-08-17T15:17:59+00:00'
type: issue
status: closed
closed_at: '2023-08-17T15:17:59+00:00'
---

# Original Description
I think submit_block should return the submitted block's fast hash, if successful.
This would allow to keep track of mined blocks more easily, as knowing the height might be not enough if there are reorgs.

# Discussion History
## jeffro256 | 2023-06-03T03:17:33+00:00
I opened a PR (#8890) to add this feature. Now the `submit_block` RPC call will respond with a `block_id` field containing the block fast hash. Is this what you were imagining? Try compiling with that commit and test it out for yourself

# Action History
- Created by: duggavo | 2023-05-24T16:11:41+00:00
- Closed at: 2023-08-17T15:17:59+00:00
