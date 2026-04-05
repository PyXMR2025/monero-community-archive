---
title: Tracking Issue for RPC integration
source_url: https://github.com/Cuprate/cuprate/issues/379
author: hinto-janai
assignees: []
labels:
- A-rpc
- C-tracking-issue
created_at: '2025-02-04T22:00:20+00:00'
updated_at: '2025-05-01T22:26:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is the 3rd tracking issue surrounding the initial RPC implementation in `cuprated`.

The scope is:
- Practical input/output compatibility with `monerod`
- Compatibility with existing wallets
- Request/response call stack for each method
- Integration into `cuprated` i.e. RPC server on `18081/18089` 

### Steps

- Internal changes
    - https://github.com/Cuprate/cuprate/pull/450
- [ ] `cuprated` <-> `monerod` RPC input/output testing harness: https://github.com/Cuprate/cuprate/pull/357
- Method enabling
    - Required for wallet compatibility
        - [ ] TODO
    - Useful but optional
        - [ ] TODO    
    - Everything else
        - [ ] TODO
- RPC server: https://github.com/Cuprate/cuprate/pull/423
- Documentation
    - https://github.com/Cuprate/cuprate/pull/451 


### Related

- https://github.com/Cuprate/cuprate/issues/183
- https://github.com/Cuprate/cuprate/issues/244

# Discussion History
# Action History
- Created by: hinto-janai | 2025-02-04T22:00:20+00:00
