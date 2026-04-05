---
title: 32-bit potential panics
source_url: https://github.com/Cuprate/cuprate/issues/429
author: Boog900
assignees: []
labels: []
created_at: '2025-04-08T16:00:05+00:00'
updated_at: '2025-05-13T18:48:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The issue for `wasm32-unknown-unknown` builds was:
- `cuprate_rpc_types` depends on `cuprate_types` with `json` feature
- `json` feature requires `cuprate_helper::cast`

To fix this, I am making `cuprate_helper::cast` work on 32-bit targets, yet panic when the cast is lossy. I don't think this is the correct long-term solution but it does work for now.

_Originally posted by @hinto-janai in https://github.com/Cuprate/cuprate/pull/355#discussion_r2015230356_
            

# Discussion History
# Action History
- Created by: Boog900 | 2025-04-08T16:00:05+00:00
