---
title: Dandelion with no outbound connections will freeze.
source_url: https://github.com/Cuprate/cuprate/issues/177
author: Boog900
assignees: []
labels:
- A-p2p
- C-bug
- P-medium
created_at: '2024-06-19T18:56:23+00:00'
updated_at: '2024-07-01T19:23:42+00:00'
type: issue
status: closed
closed_at: '2024-07-01T19:23:41+00:00'
---

# Original Description
We should provide a way for the `outbound_peer_discover` to tell us there are currently not enough peers.

relevant code: 

https://github.com/Cuprate/cuprate/blob/b76042a4e4f364aa2c3b53235f30382ac632d2e8/p2p/dandelion/src/router.rs#L164-L179

# Discussion History
# Action History
- Created by: Boog900 | 2024-06-19T18:56:23+00:00
- Closed at: 2024-07-01T19:23:41+00:00
