---
title: Crates depend on `cargo` feature unification
source_url: https://github.com/Cuprate/cuprate/issues/325
author: hinto-janai
assignees: []
labels:
- A-dependency
- A-storage
- C-bug
- E-easy
- E-help-wanted
created_at: '2024-10-22T00:55:04+00:00'
updated_at: '2024-11-01T22:01:09+00:00'
type: issue
status: closed
closed_at: '2024-11-01T22:01:08+00:00'
---

# Original Description
## Environment
All.

## Bug
Some crates have `Cargo.toml`s that do not pull in dependencies with the correct features.

They can get away with it in CI as all/most used features are usually enabled and [`cargo`'s feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification).

For example, `cuprate-{blockchain,txpool}`. Some other crates outside `storage/` probably rely on the feature unification as well. 

## Expected behavior
Crates to build as single crates with any feature combination.

## Steps to reproduce
The following does not work due to lots of feature related errors:
```bash
cargo build --package cuprate-blockchain
```

# Discussion History
## Boog900 | 2024-11-01T22:01:08+00:00
Should be fixed by  #170

# Action History
- Created by: hinto-janai | 2024-10-22T00:55:04+00:00
- Closed at: 2024-11-01T22:01:08+00:00
