---
title: Usage of inline `const` for static assertions
source_url: https://github.com/Cuprate/cuprate/issues/235
author: hinto-janai
assignees: []
labels:
- C-proposal
- E-medium
- P-low
- E-help-wanted
created_at: '2024-07-25T20:47:20+00:00'
updated_at: '2025-11-26T20:40:56+00:00'
type: issue
status: closed
closed_at: '2025-11-26T20:40:56+00:00'
---

# Original Description
## What
Rust 1.79 brought [inline `const` expressions](https://blog.rust-lang.org/2024/06/13/Rust-1.79.0.html#inline-const-expressions).

These can be used to _conditionally_ make static assertions (among other things).

## Why
Turns runtime panics into compile time errors.

## Where/How
Certain runtime panics can be replaced with these new inline `const` expressions, e.g.:

https://github.com/Cuprate/cuprate/blob/929d19c4508a84d886ece03009a6fcdc5edea5c2/storage/database/src/env.rs#L126-L128

Can be turned into:
```rust
fn resize_map(&self, resize_algorithm: Option<ResizeAlgorithm>) -> NonZeroUsize {
    const {
        assert!(
            Self::MANUAL_RESIZE,
            "This function should not be called as this database backend automatically resizes.",
        )
    }
}
```
This will make calling `resize()` from database backends that _shouldn't_ be calling `resize_map()` in the first place to fail at _compile time_ instead of at _runtime_.

The `const` expression will only be evaluated _if_ `resize()` is called, e.g.:
```rust
fn main() {}

fn f<const B: bool>() {
    const {
        assert!(B);
    }
}
```
This program will only fail if `f::<false>()` is called. It is commented out (not called) so it compiles fine. 

# Discussion History
## antonio-hickey | 2024-11-11T16:38:20+00:00
Hello, anyone working on this?

I'll take it on if not

## SyntheticBird45 | 2024-11-11T18:41:44+00:00
Hi @antonio-hickey, No one is working on it. You are welcome to take it.

## iskyd | 2025-11-06T17:53:55+00:00
@hinto-janai  I thinkg this can be closed since https://github.com/Cuprate/cuprate/pull/560 it is merged

# Action History
- Created by: hinto-janai | 2024-07-25T20:47:20+00:00
- Closed at: 2025-11-26T20:40:56+00:00
