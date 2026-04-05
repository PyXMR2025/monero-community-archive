---
title: Database keys are not sorted correctly.
source_url: https://github.com/Cuprate/cuprate/issues/179
author: Boog900
assignees:
- hinto-janai
labels:
- A-storage
- C-bug
- P-medium
created_at: '2024-06-19T21:37:54+00:00'
updated_at: '2024-07-01T19:24:49+00:00'
type: issue
status: closed
closed_at: '2024-07-01T19:24:49+00:00'
---

# Original Description

## Bug

integer keys in the database are sorted lexicographically, which is not how they should be stored.

### Expected behavior
Integer keys should be sorted by value.

## Steps to reproduce

Increase the range here and it will fail:

https://github.com/Cuprate/cuprate/blob/b76042a4e4f364aa2c3b53235f30382ac632d2e8/storage/cuprate-blockchain/src/backend/tests.rs#L336-L340


# Discussion History
# Action History
- Created by: Boog900 | 2024-06-19T21:37:54+00:00
- Closed at: 2024-07-01T19:24:49+00:00
