---
title: Usage of `LazyLock` over `OnceLock` + `fn`
source_url: https://github.com/Cuprate/cuprate/issues/236
author: hinto-janai
assignees: []
labels:
- C-proposal
- E-easy
- P-low
created_at: '2024-07-25T20:53:40+00:00'
updated_at: '2024-08-20T21:53:33+00:00'
type: issue
status: closed
closed_at: '2024-08-20T21:53:33+00:00'
---

# Original Description
## What
[Rust 1.80 stablized `LazyLock`](https://blog.rust-lang.org/2024/07/25/Rust-1.80.0.html#lazycell-and-lazylock).

This can replace any `std::sync::OnceLock` + `fn` usage.

## Where
Any place using `OnceLock` + `fn` for `LazyLock` behavior, e.g.:

https://github.com/Cuprate/cuprate/blob/929d19c4508a84d886ece03009a6fcdc5edea5c2/helper/src/fs.rs#L86-L90

## How
Replace `OnceLock` + `fn` with:
```rust
static _: LazyLock<T> = LazyLock::new(|| {
    /* old OnceLock::get_or_init function */
});
```


# Discussion History
# Action History
- Created by: hinto-janai | 2024-07-25T20:53:40+00:00
- Closed at: 2024-08-20T21:53:33+00:00
