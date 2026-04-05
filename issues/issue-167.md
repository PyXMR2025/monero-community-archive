---
title: Casting into/from pointer-sized integers without `unwrap()`
source_url: https://github.com/Cuprate/cuprate/issues/167
author: hinto-janai
assignees: []
labels:
- C-proposal
created_at: '2024-06-17T00:10:33+00:00'
updated_at: '2024-09-02T17:09:53+00:00'
type: issue
status: closed
closed_at: '2024-09-02T17:09:53+00:00'
---

# Original Description
## What
If Cuprate only supports 64-bit hardware, it means that `usize` can be losslessly casted into `u64` and vice-versa. Same goes for `isize` <-> `i64`.

We could also allow `u32` -> `usize`, as Rust doesn't impl anything higher than `From<u16> for usize`.

## Why
Prevents needless `unwrap()`; is more explicit.

## Where
This will replace any code where `try_{into,from}()` -> `unwrap()` is used, e.g.:

https://github.com/Cuprate/cuprate/blob/c837f2f48e2f99e10c81e790afe5d5e8d866df3f/helper/src/map.rs#L80

https://github.com/Cuprate/cuprate/blob/c837f2f48e2f99e10c81e790afe5d5e8d866df3f/consensus/src/context/hardforks.rs#L82

https://github.com/Cuprate/cuprate/blob/c837f2f48e2f99e10c81e790afe5d5e8d866df3f/helper/src/map.rs#L100

https://github.com/Cuprate/cuprate/blob/c837f2f48e2f99e10c81e790afe5d5e8d866df3f/consensus/src/context/weight.rs#L154

## How
Implementation can be free functions:
```rust
#[inline(always)]
fn u64_to_usize(u: u64) -> usize {
    u as usize
}

#[inline(always)]
fn usize_to_u64(u: usize) -> u64 {
    u as u64
}

// repeat for isize, i64
```
Safety is upheld by using a `#[cfg]` option where the functions are implemented:
```rust
// in {lib.mod}.rs
#[cfg(not(target_pointer_width = "64"))]
compile_error!("Cuprate is only compatible with 64-bit CPUs");
```
This prevents any user of this function from compiling on any non-64-bit architecture.

Using `as` directly would also work, but it means `as` will be more prevalent in the codebase. `as` can be used in a lossly manner, so it muddies things and is less explicit, e.g.:
```rust
let i: i64 = -1;
let u = i as u64; // lossy
let u = usize_to_u64(i); // compile error
```

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-17T00:10:33+00:00
- Closed at: 2024-09-02T17:09:53+00:00
