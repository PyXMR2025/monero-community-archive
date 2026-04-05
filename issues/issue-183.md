---
title: Tracking Issue for RPC interface
source_url: https://github.com/Cuprate/cuprate/issues/183
author: hinto-janai
assignees: []
labels:
- A-rpc
- C-tracking-issue
created_at: '2024-06-20T18:14:44+00:00'
updated_at: '2025-05-31T00:01:01+00:00'
type: issue
status: closed
closed_at: '2025-05-31T00:01:01+00:00'
---

# Original Description
### About tracking issues

Tracking issues are used to record the overall progress of implementation. They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions. A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature. Instead, open a dedicated issue for the specific matter.

### What

This is a tracking issue for Cuprate's initial RPC interface implementation.

### Steps
- [x] Initial RPC design
    - https://github.com/Cuprate/cuprate/issues/106
    - https://github.com/Cuprate/cuprate/pull/146
- [x] JSON-RPC 2.0 implementation
    - https://github.com/Cuprate/cuprate/pull/43
    - https://github.com/Cuprate/cuprate/pull/148
- [x] RPC types
    - [x] Type generation macro implementation
        - https://github.com/Cuprate/cuprate/pull/147
        - https://github.com/Cuprate/cuprate/pull/184
        - https://github.com/Cuprate/cuprate/pull/185
    - [x] Feature flags, misc types, changes, fixes
        - https://github.com/Cuprate/cuprate/pull/210
        - https://github.com/Cuprate/cuprate/pull/218
        - https://github.com/Cuprate/cuprate/pull/211
        - https://github.com/Cuprate/cuprate/pull/226
    - [x] JSON types: https://github.com/Cuprate/cuprate/pull/219
    - [x] Binary types: https://github.com/Cuprate/cuprate/pull/220
    - [x] Other endpoint types: https://github.com/Cuprate/cuprate/pull/221
    - [x] Custom (de)serialization: https://github.com/Cuprate/cuprate/pull/229
    - [x] Misc type moving: https://github.com/Cuprate/cuprate/pull/230
    - [x] Type optimizations: https://github.com/Cuprate/cuprate/pull/227
    - [x] Doc-tests
        - [x] JSON request/response data: https://github.com/Cuprate/cuprate/pull/231
        - [x] JSON/other types: https://github.com/Cuprate/cuprate/pull/232
- [x] RPC interface
    - [x] https://github.com/Cuprate/cuprate/pull/241
    - [x] https://github.com/Cuprate/cuprate/pull/233
- [x] Documentation
    - [x] Architecture book: https://github.com/Cuprate/cuprate/pull/243
    - [x] Crate documentation
        - [x] `cuprate-json-rpc` 
        - [x] `cuprate-rpc-types`
        - [x] `cuprate-rpc-interface`
- [x] Cleanup: https://github.com/Cuprate/cuprate/pull/255
- [ ] Monero RPC discrepancies upstreaming
    - https://github.com/Cuprate/cuprate/issues/159
    - https://github.com/monero-project/monero-site/pull/2335
    - https://github.com/monero-project/monero-site/pull/2336
    - https://github.com/monero-project/monero-site/pull/2337
    - https://github.com/monero-project/monero-site/pull/2340
    - https://github.com/monero-project/monero/pull/9423

### Related
- https://github.com/Cuprate/cuprate/issues/244

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-20T18:14:44+00:00
- Closed at: 2025-05-31T00:01:01+00:00
