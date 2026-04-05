---
title: TODO's for beta stressnet
source_url: https://github.com/seraphis-migration/monero/issues/166
author: j-berman
assignees: []
labels: []
created_at: '2025-10-11T18:45:10+00:00'
updated_at: '2026-04-03T19:54:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
- [x] Fees and scaling
  - [x] [Fees and weights updated for FCMP++](https://github.com/seraphis-migration/monero/issues/44)
    - #232
  - [x] #282
    - [x] https://github.com/jeffro256/monero/pull/4
  - [x] Stressnet-specific 2w long term window https://github.com/seraphis-migration/monero/pull/301
- [x] Tx relay v2 11731ff86cd0d9cbaac72d7c8d5528086a8ffd18
- [x] https://github.com/monero-project/monero/pull/10157
- [ ] Carrot-derived wallets #199 
- [ ] Hot/cold wallets #52
- [x] Use new unbiased hash to point for Carrot outputs #279 
- [x] #302
- [x] #142 
- [x] Rebase on master again
- [x] Runaway span PR's
  - [x] #234
    - Note this was merged into master, so rebasing on master would pull that in
  - [x] #303
- [ ] OOM fixes from alpha
   - [ ] #224
   - [x] #228
- [ ] FCMP++ lib with fast proof size
- [ ] Solution for https://github.com/kayabaNerve/monero-oxide/pull/5
- [ ] Changes to GBP's in FCMP++ lib from Cypher Stack audit
- [x] #307
- [x] https://github.com/seraphis-migration/monero/pull/296
- [x] Change p2p connection limit per IP to 10
  - [x] https://github.com/seraphis-migration/monero/pull/298 
- [x] https://github.com/seraphis-migration/monero/pull/300
- [ ] xmrchat issues
   - [x] https://github.com/seraphis-migration/monero/pull/297
   - [ ] Needs https://github.com/monero-project/monero/pull/10352
   - [ ] first node detecting stem loop never reported via zmq (separate issue from 10352) 
- [ ] HF table and checkpoint update
- [ ] GUI binaries
  - Working here: https://github.com/j-berman/monero-gui/commit/fe687dc3b9adb245beb55d130e6dcb78ad9d2202

# Discussion History
# Action History
- Created by: j-berman | 2025-10-11T18:45:10+00:00
