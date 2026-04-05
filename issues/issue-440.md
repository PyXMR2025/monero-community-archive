---
title: Database resizing log is not specific to blockchain/txpool
source_url: https://github.com/Cuprate/cuprate/issues/440
author: hinto-janai
assignees: []
labels:
- A-storage
- C-bug
- E-help-wanted
created_at: '2025-04-10T20:43:30+00:00'
updated_at: '2025-04-10T20:43:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Environment
- Cuprate: v0.0.2

## Bug
The database being resized can be inferred by the MB from this line, although it isn't specific:

https://github.com/Cuprate/cuprate/blob/24265ac43c1d87760ed01e227b8200ac8f9bf15f/storage/service/src/service/write.rs#L163

## Expected behavior
Ideally it should indicate which database is being resized.

Alternatively, when initializing the txpool, it could be `resize()`ed to something like `consensus_limit * 10` such that the message never appears.

## Log
Blockchain:
```
INFO Resizing database memory map, old: 111670MB, new: 112743MB
```

Txpool:
```
INFO Resizing database memory map, old: 1MB, new: 1074MB
```

# Discussion History
# Action History
- Created by: hinto-janai | 2025-04-10T20:43:30+00:00
