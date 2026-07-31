---
title: '`get_range` with `heed` does not work.'
source_url: https://github.com/Cuprate/cuprate/issues/348
author: Boog900
assignees:
- Boog900
labels:
- A-storage
- C-bug
- P-high
created_at: '2024-11-25T15:27:08+00:00'
updated_at: '2026-07-28T22:24:55+00:00'
type: issue
status: closed
closed_at: '2026-07-28T22:24:32+00:00'
---

# Original Description
## Bug
`heed`'s  `get_range` function returns incorrect results when a different ordering is used with the DB/table.

## Steps to reproduce
Add this:
```rust
        assert_eq!(table.keys().unwrap().count(), 257);
        assert_eq!(table.values().unwrap().count(), 257);
        assert_eq!(table.get_range(0..257).unwrap().count(), 257);
```

After this:
https://github.com/Cuprate/cuprate/blob/f3c1a5c2aa4629bf69b75268de21fc9112f09405/storage/database/src/backend/tests.rs#L377-L386


---

I think this is because heed's range cursor compares raw bytes here: https://docs.rs/heed/latest/src/heed/iterator/range.rs.html#416

# Discussion History
## gzalz | 2024-11-27T06:54:49+00:00
@Boog900 I think things might be working and that the test may need a slight refactor. Let me know your thoughts.

https://github.com/Cuprate/cuprate/pull/350

## Boog900 | 2024-11-27T14:29:21+00:00
Yeah slightly embarrassing but I went too aggressive on trying to simplify the test case, updated the issue with the new test case that actually fails due to this issue.

## Boog900 | 2024-11-27T23:01:05+00:00
https://github.com/meilisearch/heed/pull/289

## SyntheticBird45 | 2026-07-28T22:24:32+00:00
`heed` has been replaced with Tapes and Fjall

# Action History
- Created by: Boog900 | 2024-11-25T15:27:08+00:00
- Closed at: 2026-07-28T22:24:32+00:00
