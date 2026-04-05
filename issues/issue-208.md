---
title: Tracking Issue for Benchmarks
source_url: https://github.com/Cuprate/cuprate/issues/208
author: hinto-janai
assignees: []
labels:
- A-benches
- C-tracking-issue
created_at: '2024-07-01T16:51:39+00:00'
updated_at: '2025-01-17T20:05:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### About tracking issues
Tracking issues are used to record the overall progress of implementation. They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions. A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature. Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for integrating initial benchmarking code for Cuprate as described in #193.

### Steps

N/A = not applicable (the crate in question does not benefit from micro benchmarking).

- [x] Initial proposal: https://github.com/Cuprate/cuprate/issues/193
- [x] `benches/` initial setup: https://github.com/Cuprate/cuprate/pull/196 
- [ ] Move to `Cuprate/benches`: https://github.com/Cuprate/cuprate/pull/354
- Criterion benchmarks
    - [ ] cuprate-fast-sync
    - [ ] cuprate-consensus
    - [ ] cuprate-consensus-rules
    - [ ] cuprate-consensus-context
    - [x] cuprate-constants: N/A
    - [x] cuprate-cryptonight: https://github.com/Cuprate/cuprate/pull/352
    - [x] cuprate-helper: https://github.com/Cuprate/cuprate/pull/352
    - [ ] cuprate-epee-encoding
    - [ ] cuprate-fixed-bytes
    - [ ] cuprate-levin
    - [ ] cuprate-wire
    - [ ] cuprate-p2p
    - [ ] cuprate-p2p-core
    - [ ] cuprate-dandelion-tower
    - [ ] cuprate-address-book
    - [x] cuprate-blockchain: https://github.com/Cuprate/cuprate/pull/352
    - [x] cuprate-database: https://github.com/Cuprate/cuprate/pull/352
    - [ ] cuprate-database-service
    - [ ] cuprate-txpool
    - [ ] cuprate-pruning
    - [x] cuprate-test-utils: N/A
    - [x] cuprate-types: N/A
    - [x] cuprate-json-rpc: https://github.com/Cuprate/cuprate/pull/196
    - [x] cuprate-rpc-types: https://github.com/Cuprate/cuprate/pull/352
    - [x] cuprate-rpc-interface: N/A

# Discussion History
# Action History
- Created by: hinto-janai | 2024-07-01T16:51:39+00:00
