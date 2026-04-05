---
title: 'Declare member crates as workspace dependencies to avoid dealing with duplicated/relative
  `path` '
source_url: https://github.com/Cuprate/cuprate/issues/315
author: SyntheticBird45
assignees: []
labels:
- A-workspace
- C-proposal
created_at: '2024-10-14T18:47:59+00:00'
updated_at: '2024-10-24T22:12:32+00:00'
type: issue
status: closed
closed_at: '2024-10-24T22:12:31+00:00'
---

# Original Description
<!--
Note: Please search to see if an issue already exists for this proposal.
-->

## What

Currently the way to import cuprate crates as a dependency is like follow:
```toml
[dependencies]
cuprate-crate-name =  { path = "../crate/name", features = [] }
```
We could instead declare crates in [`/Cargo.toml`](https://github.com/Cuprate/cuprate/blob/main/Cargo.toml#L51) as follows:
```toml 
# /Cargo.toml L51
[workspace.dependencies]
# Cuprate members
cuprate-fast-sync = { path = "consensus/fast-sync" }
cuprate-consensus-rules = { path = "consensus/rules" }
cuprate-constants = { path = "constants" }
cuprate-consensus = { path = "consensus" }
cuprate-cryptonight = { path = "cryptonight" }
cuprate-helper = { path = "helper" }
cuprate-epee-encoding = { path = "net/epee-encoding" }
cuprate-fixed-bytes = { path = "net/fixed-bytes" }
cuprate-levin = { path = "net/levin" }
cuprate-wire = { path = "net/wire" }
cuprate-p2p = { path = "p2p/p2p" }
cuprate-p2p-core = { path = "p2p/p2p-core" }
cuprate-dandelion-tower = { path = "p2p/dandelion-tower" }
cuprate-address-book = { path = "p2p/address-book" }
cuprate-blockchain = { path = "storage/blockchain" }
cuprate-database = { path = "storage/database" }
cuprate-txpool = { path = "storage/txpool" }
cuprate-pruning = { path = "pruning" }
cuprate-test-utils = { path = "test-utils" }
cuprate-types = { path = "types" }
cuprate-json-rpc = { path = "rpc/json-rpc" }
cuprate-rpc-types = { path = "rpc/types" }
cuprate-rpc-interface = { path = "rpc/interface" }

# External dependencies
anyhow                = { version = "1.0.89", default-features = false }
async-trait           = { version = "0.1.82", default-features = false }
# ...
```

This would permit to transform this:
https://github.com/Cuprate/cuprate/blob/f9b847b2272f4e7a57172028d295acb4e13c225e/consensus/fast-sync/Cargo.toml#L11-L17

Into this:
```toml
[dependencies]
cuprate-blockchain      = { workspace = true }
cuprate-consensus       = { workspace = true }
cuprate-consensus-rules = { workspace = true }
cuprate-types           = { workspace = true }
cuprate-helper          = { workspace = true, features = ["cast"] }
```
## Why

This permit to avoid recurrent and relative dependency `path`. Also looks overall cleaner.


# Discussion History
# Action History
- Created by: SyntheticBird45 | 2024-10-14T18:47:59+00:00
- Closed at: 2024-10-24T22:12:31+00:00
