---
title: TODO's for beta stressnet
source_url: https://github.com/seraphis-migration/monero/issues/166
author: j-berman
assignees: []
labels: []
created_at: '2025-10-11T18:45:10+00:00'
updated_at: '2026-04-28T23:27:35+00:00'
type: issue
status: closed
closed_at: '2026-04-28T23:27:35+00:00'
---

# Original Description
- [x] Fees and scaling
  - [x] [Fees and weights updated for FCMP++](https://github.com/seraphis-migration/monero/issues/44)
    - #232
  - [x] #282
    - [x] https://github.com/jeffro256/monero/pull/4
  - [x] Stressnet-specific 2w long term window https://github.com/seraphis-migration/monero/pull/301
  - [x] #314
  - [x] Need #321
- [x] Tx relay v2 11731ff86cd0d9cbaac72d7c8d5528086a8ffd18
- [x] https://github.com/monero-project/monero/pull/10157
- [x] Use new unbiased hash to point for Carrot outputs #279 
- [x] #302
- [x] #142 
- [x] Rebase on master again
- [x] Runaway span PR's
  - [x] #234
    - Note this was merged into master, so rebasing on master would pull that in
  - [x] #303
- [x] OOM fixes from alpha
   - [x] #319
   - [x] #228
- [x] FCMP++ lib with fast proof size
  - [x] https://github.com/monero-oxide/monero-oxide/commit/a5cc436d43750ae4c58a808719da2ee25143ed6a
- [x] Solution for https://github.com/kayabaNerve/monero-oxide/pull/5
  - [x] https://github.com/monero-oxide/monero-oxide/commit/756851892eb2d5a82b01e43f63b268127143ad62
- [x] Changes to GBP's in FCMP++ lib from Cypher Stack audit
  - [x] #319
  - [x] #330
- [x] #307
- [x] https://github.com/seraphis-migration/monero/pull/296
- [x] Change p2p connection limit per IP to 10
  - [x] https://github.com/seraphis-migration/monero/pull/298 
- [x] https://github.com/seraphis-migration/monero/pull/300
- [x] https://github.com/seraphis-migration/monero/pull/329
- [x] xmrchat issues
   - [x] https://github.com/seraphis-migration/monero/pull/297 ([source](https://github.com/seraphis-migration/monero/blob/ca8d443e964fb16682bae0e927bd3b1a303d9494/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1003))
   - [x] Needs https://github.com/monero-project/monero/pull/10352
   - [x] Needs https://github.com/monero-project/monero/pull/10415
- [x] GUI binaries
  - https://github.com/j-berman/monero-gui/commits/refs/heads/fcmp%2B%2B-beta-stressnet/
- [x] HF table and checkpoint update

Nice to have
- [ ] Carrot-derived wallets #199 
- [ ] Hot/cold wallets #52

# Discussion History
## j-berman | 2026-04-28T23:27:35+00:00
Launched

# Action History
- Created by: j-berman | 2025-10-11T18:45:10+00:00
- Closed at: 2026-04-28T23:27:35+00:00
