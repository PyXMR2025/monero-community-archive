---
title: Pruninng Seeds
source_url: https://github.com/Cuprate/cuprate/issues/37
author: Boog900
assignees: []
labels:
- E-easy
- E-help-wanted
created_at: '2023-11-27T16:36:32+00:00'
updated_at: '2024-05-27T00:57:59+00:00'
type: issue
status: closed
closed_at: '2024-03-15T22:11:28+00:00'
---

# Original Description
When doing pruning calculations Cuprate keeps the seed in a compressed form and works off that. A more idiomatic way IMO is to have a CompressedPruningSeed struct which is just a wrapper around u32 and a PruningSeed which has the pruning seed in decompressed form.

So instead of:
https://github.com/Cuprate/cuprate/blob/343e979e8247b36b648b263af7038f20343a6273/common/src/pruning.rs#L53

We would have:
```rust
pub struct CompressedPruningSeed(u32);

pub struct PruningSeed {
    stripe: u32,
    log_stripes: u32
}
```

This would mean that we could enforce that `PruningSeed` always holds a valid seed and we don't have to account for no pruning in `PruningSeed`.

# Discussion History
# Action History
- Created by: Boog900 | 2023-11-27T16:36:32+00:00
- Closed at: 2024-03-15T22:11:28+00:00
