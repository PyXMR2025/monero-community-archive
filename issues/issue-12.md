---
title: Cursors methods cause deref trait to consider transactions as cursors
source_url: https://github.com/Cuprate/cuprate/issues/12
author: SyntheticBird45
assignees: []
labels:
- A-docs
- C-bug
created_at: '2023-03-23T16:34:53+00:00'
updated_at: '2024-05-27T01:00:36+00:00'
type: issue
status: closed
closed_at: '2023-12-05T13:35:45+00:00'
---

# Original Description
In the current [dev-database-method](https://github.com/Cuprate/cuprate/tree/dev-database-method) branch (see the [draft pull request](https://github.com/Cuprate/cuprate/pull/6)), the Deref trait is implemented at the `Interface` struct to more easily access its inner database transaction :
https://github.com/Cuprate/cuprate/blob/746d7eb09a5d35740f7bfe664935cacd6f0220b4/database/src/lib.rs#L203-L209

But if the `get_cursor(&mut self)` method : https://github.com/Cuprate/cuprate/blob/746d7eb09a5d35740f7bfe664935cacd6f0220b4/database/src/lib.rs#L219-L223
is renamed as `get(&mut self)`, then all the `get::<table>(key)` methods under `Interface` implementation will suddenly become the `get(&mut self)` method coming from the `Cursor` trait. Causing all sorts of errors with an argument that shouldn't be supplied, but if we delete this argument, then it suddenly tell you that it needs one.

# Discussion History
# Action History
- Created by: SyntheticBird45 | 2023-03-23T16:34:53+00:00
- Closed at: 2023-12-05T13:35:45+00:00
