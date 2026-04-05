---
title: Usage of `#[expect(lint)]` over `#[allow(lint)]`
source_url: https://github.com/Cuprate/cuprate/issues/270
author: hinto-janai
assignees: []
labels:
- C-proposal
- E-easy
- P-low
- E-help-wanted
created_at: '2024-09-05T21:34:39+00:00'
updated_at: '2024-09-18T20:31:09+00:00'
type: issue
status: closed
closed_at: '2024-09-18T20:31:09+00:00'
---

# Original Description
## What
[Rust 1.81](https://blog.rust-lang.org/2024/09/05/Rust-1.81.0.html) stabilized `#[expect(lint)]` which is the same as `#[allow(lint)]` but it emits a warning if the lint is not doing anything.

This is a proposal to move over all applicable `allow`s to `expect`s.

## Why
In combination with our fail on warnings CI, moving over some `allow`s to `expect` will reduce the amount of leftover `allow`s in the codebase.

## Where
Any applicable place where `allow` doesn't necessarily need to be used and we would want to check if the lint is actually needed, e.g.:

https://github.com/Cuprate/cuprate/blob/4653ac58849c81b6ab993a1d23f061a97962524b/storage/database/src/resize.rs#L263-L268

Places that are conditional will probably need to continue to use `allow`, e.g. inside macros:

https://github.com/Cuprate/cuprate/blob/4653ac58849c81b6ab993a1d23f061a97962524b/rpc/types/src/macros.rs#L120-L125

## How
Find/replace `allow` -> `expect`, fix as needed.


# Discussion History
# Action History
- Created by: hinto-janai | 2024-09-05T21:34:39+00:00
- Closed at: 2024-09-18T20:31:09+00:00
