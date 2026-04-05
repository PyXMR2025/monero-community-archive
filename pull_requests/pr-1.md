---
title: support for static link with musl
source_url: https://github.com/Cuprate/randomx-rs/pull/1
author: Naia-love
assignees: []
labels: []
created_at: '2024-12-26T13:49:15+00:00'
updated_at: '2024-12-26T13:49:15+00:00'
type: pull_request
status: open
closed_at: null
merged_at: null
---

# Original Description
fix https://github.com/Cuprate/cuprate/issues/360

If building statically (which rust do by default for musl), statically link stdc++ instead of dynamically,
if RUSTFLAGS have been set to build dynamically, link it dynamically.

Thank syntheticbird for the help tracing down that it could be the binding causing the crash.

# Discussion History
# Action History
- Created by: Naia-love | 2024-12-26T13:49:15+00:00
