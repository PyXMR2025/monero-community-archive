---
title: TODO list for launch
source_url: https://github.com/seraphis-migration/monero/issues/53
author: j-berman
assignees: []
labels: []
created_at: '2025-06-05T17:49:37+00:00'
updated_at: '2026-03-30T19:57:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Wallet features

- [x] Restore
- [x] Sync
- [x] Transfers
- [x] Sweeps
- [x] Support >8 input txs
  - #57
- [x] Payments to integrated address
  - #61 
- [ ] `scan_tx`
  - https://github.com/seraphis-migration/monero/pull/49
  - #89
- [x] Background sync
- [ ] Hot/cold wallet integration
  - #51 
  - #52
- [ ] HW wallet interface changes
  -  https://github.com/seraphis-migration/monero/issues/63
- [ ] Knowledge proofs
  - #270
- [ ] Multisig
  - #291
- [ ] 3rd party HW wallet integrations
  - Helpful link: https://github.com/seraphis-migration/monero/issues/63
  - [ ] Trezor
  - [ ] Ledger
- [ ] Clean up CLI references to rings in UI
- [ ] Clean up GUI references to rings
- [ ] Wallet RPC `describe_transfer` command for Carrot transaction proposals
  - Resolved by: https://github.com/seraphis-migration/monero/issues/52
- [ ] Don't remove existing tx dests when opening an old wallet with the new software
  - https://github.com/seraphis-migration/monero/pull/106
- [x] Don't need `simple_wallet::prompt_if_old` after fork
  - [x] Don't need `Transaction spends more than one very old outputs. Privacy would be better if they were sent separately.` after FCMP++.
  - [x] #305
- [x] Remove block hashes download on restore
  - #81
- [x] Speed up `prove()`
  - https://github.com/kayabaNerve/fcmp-plus-plus/issues/34
  - Integrate faster `prove()` into fcmp++-stage
  - Solved by https://github.com/seraphis-migration/monero/pull/93
- [x] When the CLI identifies a receives and requires password and/or user inputs the wrong password, make block popping instant
  - See [this comment](https://github.com/seraphis-migration/monero/blob/8fb0f5631bc83525743ee8c73f01bd71db449670/src/wallet/wallet2.cpp#L3364)
  - https://github.com/seraphis-migration/monero/pull/96

## Daemon features

- [x] Build FCMP++ tree
- [x] DB migration for FCMP++ tree
- [x] Validate FCMP++ txs
- [x] Validate Carrot txs
- [x] Include init sync data needed to restore a wallet from arbitrary restore height
- [x] Include FCMP++ tree root and n tree layers in PoW hash 
- [x] Prohibit torsioned outputs at consensus 
- [ ] Endpoint to get path by output id
  - #49
  - #89
- [x] Hardened tx weight calculations (#44)
  - #232
  - Revisit FCMP++ [transaction weight limit](https://github.com/seraphis-migration/monero/pull/57#discussion_r2272077568) since a 128-in tx can be bigger than 1/2 the penalty free block size
- [x] Dynamic block weight changes
  - Proposed: https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf
- [ ] PoW-enabled relay (PoWER)
  - #230
  - https://github.com/monero-project/research-lab/issues/133
- [ ] [RandomX commitments w/double hashing](https://github.com/monero-project/monero/issues/8827)
  - https://github.com/monero-project/monero/pull/10038
- [x] https://github.com/monero-project/monero/issues/10142
  - Resolved by cache input verification results

## Known bugs

- [x] #45 
  - #81 may help
- [x] #46
  - #81 may help
- [x] @nahuhh reported a segfault in wallet, broken wallet state
  - Should be fixed by #39 and #59 
- [x] Sweep when some txs don't cover fees.
  - Mitigated by #51.
  - Should be fixed by #54.
- [x] Handle uncaught errors in tx construction (e.g. no unlocked outputs triggering "no input candidates provided" currently breaks the RPC wallet)
  - Possibly https://github.com/seraphis-migration/monero/pull/61
  - Add a functional test for error handling in the RPC wallet
- [x] Sporadic failure in `k_anonymity` functional test ([link](https://github.com/seraphis-migration/monero/pull/50#issuecomment-2940488580))
  - Maybe this one is ok to leave for now since allowing >8 inputs per tx should solve it.
- [x] Handle tx dests taking Carrot changes into account.
  - https://github.com/seraphis-migration/monero/pull/61
- [x] Handle tx priv keys taking Carrot changes into account.
  - https://github.com/seraphis-migration/monero/pull/61
- [x] Fee-included transfers.
   - https://github.com/seraphis-migration/monero/pull/61
- [x] `wallet2::get_payment_id` updated for Carrot.
  - https://github.com/seraphis-migration/monero/pull/61
- [x] Require new wallets point to updated daemon (required for building the tree from an arbitrary restore height)
  - #58 
- [x] #70
- [ ] Creating watch-only wallet from full wallet, `wallet2::import_blockchain` has a FIXME for tree
- [ ] Blockchain import should add locked outputs and update FCMP++ tree
- [ ] Fix CLI/RPC displaying locked status of time-based locked outputs after FCMP++ fork 
- [x] Fix `monero-blockchain-prune` utility
  - #196

## Misc.

- [x] Use new unbiased hash to point for Carrot outputs
  - https://github.com/seraphis-migration/monero/blob/64190feb26151e186b86c27bcd7c08e2ca09db6b/src/crypto/crypto.cpp#L650-L653
  - Set the tree up here: https://github.com/j-berman/monero/commits/unbiased-hash-curve-trees/
- [x] FFI cleanup
  - #39
  - #90
  - #91
- [x] #43
- [ ] #40 
- [x] Don't store output pubkeys and commitments in db twice
  - https://github.com/seraphis-migration/monero/pull/62
- [x] Test pre-RCT to FCMP++
  - https://github.com/seraphis-migration/monero/pull/67
- [x] Clean up compile warnings
  - https://github.com/seraphis-migration/monero/pull/66
- [x] xmrig
- [ ] p2pool
- [ ] Block explorer
  - https://github.com/moneroexamples/onion-monero-blockchain-explorer/issues/335
- [ ] LWS
- [ ] Updated documentation for the FCMP++ integration
  - #110 
- [ ] Carrot integration documentation
  - Heuristics wallet implementers must keep in mind (e.g. zero-change dummies back to sender, input selection prefers powers of 2, 1/2-input probability)
  - New things users should understand (new priv keys, tx keys, tx proofs, view balance key)
- [ ] Document general wallet changes users should keep in mind
  - Updated wallets must point to updated daemons, old wallets can point to updated daemons
  - Deprecated `scan_tx` scanning *future* txs relative to wallet sync height, faster wallet restore at high height
  - Updated wallets re-sync from restore height (in order to sync tree)
- [ ] Document general daemon changes users should keep in mind
  - Long migration
  - Deprecated building on top of alt chains
- [x] Make sure functional tests pass excluding the HF from `hardforks.cpp` too
  - #111
- [x] Use optimized libs (https://github.com/j-berman/fcmp-plus-plus-optimization-competition)
- [x] https://github.com/seraphis-migration/monero/pull/93
- [ ] Remove static proof len table and use the latest fast proof len size calc from the FCMP++ lib instead
  - Move the static proof len table into a test just to sanity check the proof len size calc

## On hold

- [x] ~~Blinds cache (#25)~~ (no longer necessary thanks to contest success)
- [x] ~~Update references to "weight" instead of "bytes" as necessary~~
  - Not necessary for launch once #232 is in, since weight will be much closer to bytes with that change.


# Discussion History
## jeffro256 | 2025-07-09T17:43:04+00:00
## Stressnet Blockers

The following tasks are blockers before a useful stressnet network can be launched.

- [x] Support >8 input txs (including fixing quadratic prove bug)
- [ ] ~Divisors re-impl from SLVer bullet~ (edit: see [this MRL discussion](https://github.com/monero-project/meta/issues/1244))
- [x] Pulling in @fabrizio-m's `ec-divisors` submission
- [x] Pulling in @lederstrumpf's `helioselene` submission, plus kayaba's inversion changes
- [x] #78
- [x] #81
- [x] #87
- [x] #88 

These tasks may significantly impact the performance characteristics of the nodes and should be merged before undergoing stressnet testing.

#9473 is a nice to have as well.

## spackle-xmr | 2025-07-16T19:57:08+00:00
### Unresolved from the 2024 stressnet

- [ ] Serialization limits: [Daemons processing big blocks may bump against serializer sanity checks and fail to sync #9388](https://github.com/monero-project/monero/issues/9388) and [contrib: change default value of epee::serialization to fix limitation #9433](https://github.com/monero-project/monero/pull/9433) 

- [x] Dynamic block sync size: [src: dynamic block sync size #9494](https://github.com/monero-project/monero/pull/9494)

- [ ] Dynamic span: [src: dynamic span, to calculate span limit dynamically #9495](https://github.com/monero-project/monero/pull/9495)

## nahuhh | 2025-07-16T22:01:00+00:00
> ### Unresolved from the 2024 stressnet
> 
> - [ ] Serialization limits: [Daemons processing big blocks may bump against serializer sanity checks and fail to sync #9388](https://github.com/monero-project/monero/issues/9388) and [contrib: change default value of epee::serialization to fix limitation #9433](https://github.com/monero-project/monero/pull/9433) 
> 

serialization limits might best be resolved by 8867

> - [ ] Dynamic block sync size: [src: dynamic block sync size #9494](https://github.com/monero-project/monero/pull/9494)

this should be ready for review, and had been tested many times. This works around the serialization limits (by keeping batches, by default, below them), while also syncing batches based on size instead of an arbitrary 100 or 20 blocks.

> - [ ] Dynamic span: [src: dynamic span, to calculate span limit dynamically #9495](https://github.com/monero-project/monero/pull/9495)

This is unrelated to stressnet / hopes to fix an unrelated issue

---

So unless we plan on going above ~30mb blocks, 9494 (dynamic block sync size) is the only one of these 4 prs that need to make it into the stressnet

edit: also need [#9473](https://github.com/monero-project/monero/pull/9473). When txpool > 100mb, you cannot connect a wallet to the unrestricted RPC. Restricted does not have the problem because it batches into 100tx.

# Action History
- Created by: j-berman | 2025-06-05T17:49:37+00:00
