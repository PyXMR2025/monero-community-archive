---
title: Duplicated dependencies
source_url: https://github.com/Cuprate/cuprate/issues/58
author: hinto-janai
assignees: []
labels:
- A-dependency
- C-discussion
created_at: '2024-02-11T20:59:22+00:00'
updated_at: '2024-05-27T00:52:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
As of commit ba0f82c3562dd16f55079e0c4591cf3ed8be874d, Cuprate's workspace `Cargo.toml` builds some duplicated dependencies.

| Dependency         | Versions |
|--------------------|----------|
| `bitflags`         | `v1.3.2`, `v2.4.2`
| `hashbrown`        | `v0.12.3`, `v0.14.3`
| `indexmap`         | `v1.9.3`, `v2.2.2`
| `parking_lot`      | `v0.11.2`, `v0.12.1`
| `parking_lot_core` | `v0.8.6`, `v0.9.9`

The full list can be seen with `cargo tree -d`.

There are some same-version dependencies that are built twice with different features (`libc`, `proc-macro2`, `syn`, `quote`) but I believe `cargo` only builds them once with a union of the features selected: https://doc.rust-lang.org/cargo/commands/cargo-tree.html#feature-unification.

## Todo
Eventually, de-duplicating as many dependencies (as much as possible...) should be done.

The current list isn't too bad, but it may grow as more dependencies are added.

# Discussion History
# Action History
- Created by: hinto-janai | 2024-02-11T20:59:22+00:00
