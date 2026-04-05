---
title: Workaround `flatten` imcompatability with `deny_unknown_fields`
source_url: https://github.com/Cuprate/cuprate/issues/492
author: hinto-janai
assignees: []
labels:
- C-discussion
- A-binaries
created_at: '2025-05-29T18:28:24+00:00'
updated_at: '2025-05-30T23:47:42+00:00'
type: issue
status: closed
closed_at: '2025-05-30T23:47:42+00:00'
---

# Original Description
## What
`serde` does not support `flatten` with `deny_unknown_fields`: https://serde.rs/field-attrs.html#flatten.

This causes problems with default values, for example in the config:
- https://github.com/Cuprate/cuprate/pull/423#discussion_r2110581752
- https://github.com/Cuprate/cuprate/actions/runs/15288154950/job/43002509225?pr=423#step:9:743

This could be worked around by manually implementing `flatten` in `config_macro`.

# Discussion History
# Action History
- Created by: hinto-janai | 2025-05-29T18:28:24+00:00
- Closed at: 2025-05-30T23:47:42+00:00
