---
title: Remove `REORG_LOCK`
source_url: https://github.com/Cuprate/cuprate/issues/305
author: Boog900
assignees: []
labels:
- C-discussion
created_at: '2024-10-06T16:46:54+00:00'
updated_at: '2024-10-06T16:46:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

## What
Removing the reorg lock from `cuprated`.

## Why

Currently the only purpose of the `REORG_LOCK` is for adding txs to the tx-pool to guarantee the context cache and database are in sync. With some changes to the API of the consensus crates it should be possible to remove the lock.


# Discussion History
# Action History
- Created by: Boog900 | 2024-10-06T16:46:54+00:00
