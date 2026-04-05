---
title: '`cuprated` panics due to `heed::MdbError::BadDbi`'
source_url: https://github.com/Cuprate/cuprate/issues/412
author: hinto-janai
assignees: []
labels:
- C-bug
created_at: '2025-03-20T21:16:31+00:00'
updated_at: '2025-03-20T21:27:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Environment
- OS: Linux ARM64
- Hardware: Raspberry Pi 5
- Cuprate: v0.0.1

## Bug
Panic at:

https://github.com/Cuprate/cuprate/blob/21ad35d44a465efbb5414a902cb6c370b8358303/storage/database/src/backend/heed/error.rs#L103

This happened after a system crash with `SyncMode::Fast`. Most likely is a corrupted DB, which is to be expected with that sync mode. Perhaps a special error message should be placed here.

## Log
Initial crash:
```
2025-03-18T08:02:23.725277Z  INFO incoming_block_batch{start_height=2628933 len=3}: Successfully added block batch fast_sync=true

thread 'cuprate_database_service::service::write::DatabaseWriter' panicked at storage/database/src/backend/heed/error.rs:103:33:
BadDbi
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Aborted
```
Subsequent run:
```
Using config at: Cuprated.toml

thread 'cuprate_database_service::reader_threads::DatabaseReader(0)' panicked at storage/database/src/backend/heed/error.rs:103:33:
BadDbi
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Aborted
```
For some reason, running `cuprated` after this makes it ignore the current DB and start from height `0`, then after exiting and running it again:
```
thread 'main' panicked at binaries/cuprated/src/main.rs:108:18:
called `Result::unwrap()` on an `Err` value: DBErr(KeyNotFound)
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Aborted
``` 

# Discussion History
# Action History
- Created by: hinto-janai | 2025-03-20T21:16:31+00:00
