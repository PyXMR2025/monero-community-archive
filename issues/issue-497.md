---
title: Code comment inconsistencies
source_url: https://github.com/Cuprate/cuprate/issues/497
author: YichiZhang0613
assignees: []
labels: []
created_at: '2025-06-02T14:52:47+00:00'
updated_at: '2025-06-13T23:29:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In p2p/p2p-core/src/handles.rs, as function's comment said, this function should panic when permit was not set, but check is missing
```rust
/// This will panic if a permit was not set [`HandleBuilder::with_permit`]
    pub fn build(self) -> (ConnectionGuard, ConnectionHandle) {
        let token = CancellationToken::new();

        (
            ConnectionGuard {
                token: token.clone(),
                _permit: self.permit,
            },
            ConnectionHandle {
                token,
                ban: Arc::new(OnceLock::new()),
            },
        )
    }
```

# Discussion History
# Action History
- Created by: YichiZhang0613 | 2025-06-02T14:52:47+00:00
