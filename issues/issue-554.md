---
title: '`cuprated` as a library'
source_url: https://github.com/Cuprate/cuprate/issues/554
author: hinto-janai
assignees: []
labels:
- C-proposal
- A-binaries
created_at: '2025-10-01T19:19:38+00:00'
updated_at: '2025-10-01T19:19:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
Initial implementation and type/signature proposal for `cuprated` as a library.

https://github.com/Cuprate/cuprate/issues/516.

## Where
`binaries/cuprated` could be a double binary/library.

Another option is `binaries/cuprated` could be turned into a thin shell around a new library that contains the core node functionality, perhaps this would be cleaner. 

Library name/location: TODO.

## How
Some changes/fixes are necessary as `binaries/cuprated` currently assumes it is a standalone binary e.g.:

- Many types/signatures are `pub`
- Global `rayon`, `tokio`, `tracing` usage; these will panic when initialized elsewhere
- CLI handling is intermixed with the config code, this must be separated

## API (wip)
```rust
//! # `cuprated` library.

/// An active `cuprated` node.
///
/// `Drop` will end the node process.
pub struct Node {/* ... */}

pub struct NodeConfig {/* ... */}
pub struct NodeEventListener {/* ... */}

impl Node {
    /// Launch a new `cuprated` process.
    pub fn launch(conifg: NodeConfig) -> Result<Self, Error>;

    /// `Stream` of events emitted by `cuprated`.
    pub fn events(&self) -> NodeEventListener;

    /// Current config in use.
    pub fn config(&self) -> &NodeConfig;
}

pub mod statics {
    /* `binaries/cuprated/src/statics.rs` could be moved here */
}

pub mod signals {
    /* `binaries/cuprated/src/signals.rs` could be moved here */
}
```


# Discussion History
# Action History
- Created by: hinto-janai | 2025-10-01T19:19:38+00:00
