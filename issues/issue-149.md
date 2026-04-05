---
title: 'blockchain: `redb::Durability` page freeing issue'
source_url: https://github.com/Cuprate/cuprate/issues/149
author: hinto-janai
assignees:
- hinto-janai
labels:
- A-storage
- C-bug
- I-size
- I-disk
created_at: '2024-06-04T22:56:14+00:00'
updated_at: '2024-07-10T21:11:11+00:00'
type: issue
status: closed
closed_at: '2024-07-10T21:11:10+00:00'
---

# Original Description
## Bug
When using [`SyncMode::Fast` in `cuprate_blockchain`, it gets mapped to `redb::Durability::None`](https://github.com/Cuprate/cuprate/blob/0622237d19e655fa68b3814c4e3d2ac5b3f71fb8/storage/cuprate-blockchain/src/backend/redb/env.rs#L61), which unfortunately has a side effect:

> [Pages are only freed during commits with higher durability levels.](https://docs.rs/redb/2.1.0/redb/enum.Durability.html#variant.None)

Only using `redb::Durability::None` causes the database file to grow `10x-60x` faster than normal.

## Expected behavior
Normal database growth, similar to `heed`.

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-04T22:56:14+00:00
- Closed at: 2024-07-10T21:11:10+00:00
