---
title: Tracking Issue for `cuprate_database`
source_url: https://github.com/Cuprate/cuprate/issues/187
author: hinto-janai
assignees: []
labels:
- A-storage
- C-tracking-issue
created_at: '2024-06-21T13:56:10+00:00'
updated_at: '2024-06-21T14:01:44+00:00'
type: issue
status: closed
closed_at: '2024-06-21T14:01:44+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for Cuprate's initial database implementation.

This includes the base database abstraction, as well as the blockchain specific layer built on-top.

### Steps
- [x] Initial design & rough implementation skeleton
    - https://github.com/Cuprate/cuprate/pull/35
    - https://github.com/Cuprate/cuprate/pull/60
    - https://github.com/Cuprate/cuprate/pull/61
    - https://github.com/Cuprate/cuprate/pull/62
    - https://github.com/Cuprate/cuprate/pull/68
- [x] Filesystem definitions
    - https://github.com/Cuprate/cuprate/issues/46
    - https://github.com/Cuprate/cuprate/pull/67
- [x] (De)serialization
    - https://github.com/Cuprate/cuprate/pull/81
    - https://github.com/Cuprate/cuprate/pull/92
- [x] `trait` abstractions
    - https://github.com/Cuprate/cuprate/pull/96
    - https://github.com/Cuprate/cuprate/pull/104
- [x] Backend implementation
    - https://github.com/Cuprate/cuprate/pull/79
    - https://github.com/Cuprate/cuprate/pull/80
    - https://github.com/Cuprate/cuprate/pull/85
    - https://github.com/Cuprate/cuprate/pull/95
    - https://github.com/Cuprate/cuprate/pull/97
- [x] `ops` implementation
    - https://github.com/Cuprate/cuprate/pull/102
- [x] `tower::Service` implementation
    - https://github.com/Cuprate/cuprate/pull/93
    - https://github.com/Cuprate/cuprate/pull/101
    - https://github.com/Cuprate/cuprate/pull/113
- [x] Tables & types
    - https://github.com/Cuprate/cuprate/pull/91
    - https://github.com/Cuprate/cuprate/pull/94
    - https://github.com/Cuprate/cuprate/pull/103
    - https://github.com/Cuprate/cuprate/pull/114
- [x] Documentation
    - https://github.com/Cuprate/cuprate/pull/77
    - https://github.com/Cuprate/cuprate/pull/117
    - https://github.com/Cuprate/cuprate/pull/126
- [x] Tests and testing utilities
    - https://github.com/Cuprate/cuprate/pull/107
    - https://github.com/Cuprate/cuprate/pull/108
    - https://github.com/Cuprate/cuprate/pull/110
    - https://github.com/Cuprate/cuprate/pull/115
- [x] Cleanup
    - https://github.com/Cuprate/cuprate/pull/119
    - https://github.com/Cuprate/cuprate/pull/135

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-21T13:56:10+00:00
- Closed at: 2024-06-21T14:01:44+00:00
