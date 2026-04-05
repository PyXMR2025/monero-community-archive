---
title: Carrot account integration plan
source_url: https://github.com/seraphis-migration/monero/issues/199
author: jeffro256
assignees: []
labels: []
created_at: '2025-10-29T05:33:09+00:00'
updated_at: '2025-12-16T06:52:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The Carrot addressing protocol is already implemented and integrated into `wallet2`, but Carrot accounts are not. It would be nice to integrate this feature into `wallet2` before the beta stressnet. There's a lot of opinionated decisions to make on that path. We would also need to support hybrid key hierarchies and the hot/cold and multisig protocols using these keys combos.

- [x] Refactor `scanning_tools` to take Carrot devices and public addresses instead of `cryptonote::account_keys` #214 
- [x] Finish Carrot spend device interface #216 
- [x] Implement in-memory Carrot-derived spend device #216
- [ ] Refactor `tx_builder` to take Carrot spend devices instead of private keys #216
- [x] Modify subaddress maps to resolve to `carrot::subaddress_index_extended` instead of `cryptonote::subaddress_index`. #216
- [ ] Add Carrot account key storage to `wallet2`
- [ ] Make/use Carrot devices in `wallet2` for spending
- [ ] Expose API to allow `wallet2` to generate Carrot keys instead of legacy keys
- [ ] Expose API to allow `wallet2` to upgrade from legacy hierarchy to hybrid key hierarchy
- [ ] Switch to returning Carrot-derived addresses by default in Carrot/hybrid key hierarchies

# Discussion History
# Action History
- Created by: jeffro256 | 2025-10-29T05:33:09+00:00
