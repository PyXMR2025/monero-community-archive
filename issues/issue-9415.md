---
title: Expose Expected Block Size to get_block_template RPC
source_url: https://github.com/monero-project/monero/issues/9415
author: HardenedSteel
assignees: []
labels:
- low priority
- daemon
- request
created_at: '2024-07-31T19:31:01+00:00'
updated_at: '2024-08-14T18:19:26+00:00'
type: issue
status: closed
closed_at: '2024-08-14T18:19:26+00:00'
---

# Original Description
With ``get_block_template`` RPC call we should able get expected block sizes like the ``expected_reward``.

Currently its internally calculated but its not exposed to RPC 

I believe its needed because it would be very useful blockchain explorers (for an example:  https://github.com/txstreet/processor/issues/2)

Related code: https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.h

# Discussion History
# Action History
- Created by: HardenedSteel | 2024-07-31T19:31:01+00:00
- Closed at: 2024-08-14T18:19:26+00:00
