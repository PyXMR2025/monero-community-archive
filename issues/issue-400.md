---
title: '`cuprated` emits `println` messages'
source_url: https://github.com/Cuprate/cuprate/issues/400
author: hinto-janai
assignees: []
labels:
- A-storage
- C-bug
- A-binaries
created_at: '2025-03-12T13:13:59+00:00'
updated_at: '2025-04-02T15:08:29+00:00'
type: issue
status: closed
closed_at: '2025-04-02T15:08:29+00:00'
---

# Original Description
## Environment
All.

## Bug
`cuprated` emits `println` messages.

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/storage/database/src/backend/heed/env.rs#L83-L84

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/storage/database/src/backend/redb/env.rs#L34-L35

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/storage/service/src/service/write.rs#L155-L156

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/storage/service/src/service/write.rs#L173-L174

## Expected behavior
Only `tracing` messages.


# Discussion History
# Action History
- Created by: hinto-janai | 2025-03-12T13:13:59+00:00
- Closed at: 2025-04-02T15:08:29+00:00
