---
title: 'build: support for static linking'
source_url: https://github.com/Cuprate/randomx-rs/pull/7
author: redsh4de
assignees: []
labels: []
created_at: '2026-07-29T13:18:23+00:00'
updated_at: '2026-07-30T21:24:24+00:00'
type: pull_request
status: merged
closed_at: '2026-07-30T21:24:24+00:00'
merged_at: '2026-07-30T21:24:24+00:00'
---

# Original Description
fixes Cuprate/cuprate#360

detects whether we are building statically/dynamically and links accordingly

remake of #1 - `build.rs` has evolved since then

# Discussion History
## Boog900 | 2026-07-30T15:44:01+00:00
could we use `CARGO_CFG_TARGET_FEATURE` here?

## redsh4de | 2026-07-30T20:22:46+00:00
Won't work here - on musl, crt-static isn't passed in `CARGO_CFG_TARGET_FEATURE`, so even though we are linking statically the script would think that due to it's absence we are doing it dynamically

## redsh4de | 2026-07-30T20:31:15+00:00
Initially i did want to just check the environment, and default `musl` to static unless overriden with `-crt-static`, but thats worse imo as then that's an extra branch to check next to `target_os`. Reading the actual info from rustc is more reliable and simpler in comparison imo

## Boog900 | 2026-07-30T21:23:56+00:00
ah ok

# Action History
- Created by: redsh4de | 2026-07-29T13:18:23+00:00
- Merged at: 2026-07-30T21:24:24+00:00
