---
title: Database fast-then-slow sync
source_url: https://github.com/Cuprate/cuprate/issues/78
author: hinto-janai
assignees: []
labels:
- A-storage
- C-discussion
created_at: '2024-02-26T21:35:48+00:00'
updated_at: '2024-05-27T00:52:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
Cuprate's database's default disk syncing mode may be `fast-then-slow`, which would cause the database to operate in `fast` mode, _not_ flushing to disk during initial sync for speed, then eventually switch to `safe` mode, flushing whenever possible for reliability.

This was discussed for `monerod` here:
- https://github.com/monero-project/monero/issues/706#issuecomment-267501242
- https://github.com/monero-project/monero/issues/1463
- https://github.com/monero-project/monero/pull/1506

## Open questions

- Q1. Under what conditions do we start in `fast-then-safe` mode? (accounting for restarts, practically empty database files, etc)
- Q2. How will we _reliably_ know when to switch to `safe` mode? (when is the node close enough to being synced?)
- Q3. Should this be the default sync mode?

# Discussion History
# Action History
- Created by: hinto-janai | 2024-02-26T21:35:48+00:00
