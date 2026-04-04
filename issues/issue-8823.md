---
title: Issue with monero-cli-wallet and daemon
source_url: https://github.com/monero-project/monero/issues/8823
author: Dinamitrii
assignees: []
labels: []
created_at: '2023-04-15T12:40:16+00:00'
updated_at: '2023-04-15T16:49:33+00:00'
type: issue
status: closed
closed_at: '2023-04-15T16:49:33+00:00'
---

# Original Description
Wanna inform for this bug.
When in monero-cli-wallet option 'persistent-rpc-client-id' is set to 1 (on),then payments from the daemon getting to 'Stale' status and never received.
All of this is when payments for rpc are set to on.
Is there any solution?

# Discussion History
## selsta | 2023-04-15T14:31:49+00:00
We will drop the rpc payment system: https://github.com/monero-project/monero/pull/8724

See here for reasons to remove: https://github.com/monero-project/monero/issues/8722

## Dinamitrii | 2023-04-15T16:49:33+00:00
Thanks i'll remove it right now

# Action History
- Created by: Dinamitrii | 2023-04-15T12:40:16+00:00
- Closed at: 2023-04-15T16:49:33+00:00
