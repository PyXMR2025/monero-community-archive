---
title: Entry API for `cuprate_database`
source_url: https://github.com/Cuprate/cuprate/issues/181
author: hinto-janai
assignees: []
labels:
- A-storage
- C-proposal
- E-medium
- E-help-wanted
created_at: '2024-06-20T13:32:54+00:00'
updated_at: '2024-09-11T21:26:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This proposal describes a new `std::collections::btree_map::Entry`-like API to be added to `cuprate_database`.

3 public types will be added:
- `enum Entry`
- `struct OccupiedEntry`
- `struct VacantEntry`

The API for these types will closely resemble `std`'s API.

## Where
Added onto the [`cuprate_database::DatabaseRw`](https://github.com/Cuprate/cuprate/blob/b76042a4e4f364aa2c3b53235f30382ac632d2e8/storage/cuprate-blockchain/src/database.rs#L156) trait:
```rust
// where
//     T: Table
fn entry(&mut self, key: &T::Key) -> Entry<'_, T>;
```

This replaces functions like `DatabaseRw::update`:

https://github.com/Cuprate/cuprate/blob/b76042a4e4f364aa2c3b53235f30382ac632d2e8/storage/cuprate-blockchain/src/database.rs#L195

and some awkward code:

https://github.com/Cuprate/cuprate/blob/b76042a4e4f364aa2c3b53235f30382ac632d2e8/storage/cuprate-blockchain/src/ops/output.rs#L32-L41

## Why
All the same reasons why `std::collections::btree_map::Entry` exists.

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-20T13:32:54+00:00
