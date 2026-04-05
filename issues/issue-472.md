---
title: Expanded tier 1/2 build targets
source_url: https://github.com/Cuprate/cuprate/issues/472
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2025-05-13T01:58:46+00:00'
updated_at: '2025-11-07T00:32:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This is for discussing an expanded tier 1/2 build target list for `cuprated`.

Notable targets:
- x86_64-unknown-linux-musl
- aarch64-unknown-linux-musl
- x86_64-unknown-freebsd
- aarch64-unknown-freebsd
- aarch64-pc-windows-msvc
- x86_64-unknown-openbsd
- riscv64gc-unknown-linux-gnu
- riscv64gc-unknown-linux-musl

# Discussion History
## SyntheticBird45 | 2025-05-13T09:52:35+00:00
In order of priority imo:
1. x86_64/aarch64 musl linux
2. riscv64 linux gnu/musl
3. freebsd/openbsd
4. aarch64 windows

The intersection of "arm cpu with windows" set and "monero user" set is practically null, so i really wonder if its even worth it to provide 4.

## hinto-janai | 2025-11-07T00:32:34+00:00
Noting that industry ([including Rust](https://blog.rust-lang.org/2025/10/30/Rust-1.91.0/#aarch64-pc-windows-msvc-is-now-a-tier-1-platform)) are continuing to push aarch64 Windows, I suspect it will become quite relevant in the future.

# Action History
- Created by: hinto-janai | 2025-05-13T01:58:46+00:00
