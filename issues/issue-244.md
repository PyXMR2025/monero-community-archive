---
title: Tracking Issue for RPC handlers
source_url: https://github.com/Cuprate/cuprate/issues/244
author: hinto-janai
assignees: []
labels:
- A-rpc
- C-tracking-issue
created_at: '2024-08-04T18:49:03+00:00'
updated_at: '2025-05-31T00:02:12+00:00'
type: issue
status: closed
closed_at: '2025-05-31T00:02:11+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for Cuprate's initial RPC handler implementation. The RPC handlers build upon the previous crates created in https://github.com/Cuprate/cuprate/issues/183. They implement the function bodies responsible for mapping requests to responses.

### Steps
<!--
Describe the steps required to bring this effort to completion.

For larger features, more steps might be involved.
If the feature is changed later, please add those PRs here as well.
-->

- Internal changes required for RPC handlers
    - [x] https://github.com/Cuprate/cuprate/pull/266
    - [x] https://github.com/Cuprate/cuprate/pull/297
    - [x] https://github.com/Cuprate/cuprate/pull/300
    - [x] https://github.com/Cuprate/cuprate/pull/301
    - [x] https://github.com/Cuprate/cuprate/pull/309
    - [x] https://github.com/Cuprate/cuprate/pull/310
    - [x] https://github.com/Cuprate/cuprate/pull/320
- Handlers
    - [x] Initial skeleton, `fn` signatures, mappings
        - [x] https://github.com/Cuprate/cuprate/pull/262 
        - [x] https://github.com/Cuprate/cuprate/pull/272
    - [x] Implementation: https://github.com/Cuprate/cuprate/pull/355
- Documentation
    - [ ] Architecture book: https://github.com/Cuprate/cuprate/pull/341

### Related
- https://github.com/Cuprate/cuprate/issues/183
- https://github.com/Cuprate/cuprate/issues/278
- https://github.com/Cuprate/cuprate/issues/279
- https://github.com/Cuprate/cuprate/pull/345

### TODO
- https://github.com/Cuprate/cuprate/pull/147#discussion_r1654885288
- https://github.com/Cuprate/cuprate/pull/147#discussion_r1654912900
- https://github.com/Cuprate/cuprate/pull/243#discussion_r1706267704

# Discussion History
## hinto-janai | 2025-05-31T00:02:11+00:00
For the remaining architecture book PR, see: https://github.com/Cuprate/cuprate/issues/476.

# Action History
- Created by: hinto-janai | 2024-08-04T18:49:03+00:00
- Closed at: 2025-05-31T00:02:11+00:00
