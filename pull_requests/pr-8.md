---
title: 'build: fix OpenBSD compilation'
source_url: https://github.com/Cuprate/randomx-rs/pull/8
author: redsh4de
assignees: []
labels: []
created_at: '2026-07-31T13:00:36+00:00'
updated_at: '2026-07-31T15:03:17+00:00'
type: pull_request
status: merged
closed_at: '2026-07-31T15:03:16+00:00'
merged_at: '2026-07-31T15:03:16+00:00'
---

# Original Description
Enable compiling on OpenBSD

Fixes Cuprate/cuprate#465. Should be noted that due to `sysinfo` not supporting OpenBSD yet (GuillaumeGomez/sysinfo#1318), the total max memory will need to be configured manually in Cuprated.toml.

# Discussion History
# Action History
- Created by: redsh4de | 2026-07-31T13:00:36+00:00
- Merged at: 2026-07-31T15:03:16+00:00
