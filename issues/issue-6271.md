---
title: Build broken if ALLOW_DEBUG_COMMANDS is undefined
source_url: https://github.com/monero-project/monero/issues/6271
author: ahook
assignees: []
labels: []
created_at: '2019-12-30T20:05:43+00:00'
updated_at: '2020-05-16T16:02:31+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:02:31+00:00'
---

# Original Description
The ALLOW_DEBUG_COMMANDS macro is meant to hide/expose a few p2p commands meant only for debugging: COMMAND_REQUEST_STAT_INFO, COMMAND_REQUEST_NETWORK_STATE, and COMMAND_REQUEST_PEER_ID.

As of about 5 years ago (https://github.com/monero-project/monero/commit/1829966fe#diff-75dbb84a608233b878963350f63597e1R102), this macro was defaulted to be defined.

Since then, code has been added/modified which breaks the build if the macro is undefined. Specifically:
- the net_node::check_trust header should be wrapped in an ifdef
- initializing net_node::m_last_stat_request_time should be in an ifdef
- p2p_protocol_defs::get_proof_of_trust_hash should be in an ifdef
- p2p_protocol_defs::COMMAND_REQUEST_SUPPORT_FLAGS should NOT be in an ifdef
- a couple places are relying on a transitive include that is in an ifdef, these files should explicitly include crypto/crypto.h

I have a patch ready to fix these issues: https://github.com/ahook/monero/commit/c8ba8456ef3953c99497e38c707c8607201a708b

However, it also raises a couple questions about this code. That patch gets everything into working order, but:
- Should we just do away with the macro altogether? Seems not to have been a problem having it defined all these years, and the two important functions are guarded by check_trust()
- Do we even need/want these commands any more? Seems like this admin-level access might be better as an rpc?

# Discussion History
## moneromooo-monero | 2019-12-31T09:08:39+00:00
I'm fine removing them since they're unusable due to the key being zeroed.

## moneromooo-monero | 2020-05-16T16:02:30+00:00
Fixed

# Action History
- Created by: ahook | 2019-12-30T20:05:43+00:00
- Closed at: 2020-05-16T16:02:31+00:00
