---
title: Custom allocators
source_url: https://github.com/Cuprate/cuprate/issues/336
author: SyntheticBird45
assignees: []
labels:
- C-discussion
- A-binaries
created_at: '2024-11-02T16:00:00+00:00'
updated_at: '2024-11-02T16:00:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<!--
Note: Please search to see if an issue already exists for this discussion.
-->

## What

Add custom allocators to cuprated behind a feature flag.

## Why
Targets that are statically linking (like musl libc by default) will inherit the default (potentially very slow) allocator. Rust permits to easily swap out an allocator and I think this might be beneficial to have a feature flag for it. 
The allocators we could support (or force):
- [jemalloc](https://github.com/jemalloc/jemalloc)
- [mimalloc](https://github.com/microsoft/mimalloc)


# Discussion History
# Action History
- Created by: SyntheticBird45 | 2024-11-02T16:00:00+00:00
