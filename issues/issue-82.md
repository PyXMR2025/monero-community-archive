---
title: Support for automated verification tools
source_url: https://github.com/Cuprate/cuprate/issues/82
author: SyntheticBird45
assignees: []
labels:
- C-discussion
- C-feature
created_at: '2024-02-29T17:51:04+00:00'
updated_at: '2024-05-27T00:51:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Support for automated verification tools

While Cuprate is almost entirely written in safe Rust, it is still a huge codebase. Such size could lead us to have introduced, without knowing, the very far corner cases of safe Rust, that could lead to [memory unsafety and undefined behavior](https://github.com/Speykious/cve-rs). 

It might be beneficial to add support for the following automated verifiers:
- [Miri](https://github.com/rust-lang/miri). Rust's official MIR verifier, provide example of CI integration
- [Kani](https://github.com/model-checking/kani). The bit-precise model checker for Rust. Focused on memory safety and assertions check
- [Loom](https://github.com/tokio-rs/loom). Tokio's concurrency verifier. Check all possible interleaving for race conditions

Honorable mention: [Proptest](https://github.com/proptest-rs), fuzzing of properties framework. Can be used directly as a `dev.dependencies` for `#[test]`

If this is adopted with [reproducible builds](https://github.com/Cuprate/cuprate/issues/39), this will make Cuprate able to deliver deterministic and fully verified binaries.

# Discussion History
# Action History
- Created by: SyntheticBird45 | 2024-02-29T17:51:04+00:00
