---
title: GTest can no longer be cross-compiled
source_url: https://github.com/monero-project/monero/issues/1739
author: vtnerd
assignees: []
labels:
- tests
created_at: '2017-02-17T00:49:40+00:00'
updated_at: '2025-12-19T15:26:20+00:00'
type: issue
status: closed
closed_at: '2025-12-19T15:26:19+00:00'
---

# Original Description
GTest is now built as an external project. The cmake configuration is not forwarded to gtest, so cross-compiling the library does not work. This only affects a couple of the test targets, and is likely not seen by many users.

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:51:35+00:00
+tests

## selsta | 2025-12-19T15:26:16+00:00
I'm not certain that this issue is still relevant since we don't cross compile tests anymore and there were some gtest related changes.

https://github.com/monero-project/monero/pull/9715

# Action History
- Created by: vtnerd | 2017-02-17T00:49:40+00:00
- Closed at: 2025-12-19T15:26:19+00:00
