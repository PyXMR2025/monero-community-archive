---
title: Upstreaming plan
source_url: https://github.com/seraphis-migration/monero/issues/103
author: jeffro256
assignees: []
labels: []
created_at: '2025-09-15T21:27:56+00:00'
updated_at: '2026-05-01T17:02:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Upstreaming Plan

| ID   | Change-set description | Components affected | Upstream PR | Depends on | Merged |
|------|--------------------------------|------------------------------|--------------------|------------------|------------|
| A    | `wallet2_basic` library types | wallet | https://github.com/monero-project/monero/pull/10084 | | ❌ |
| B    |  Separation of hot-cold wallet stuff into different code file pair | wallet | | A | ❌ |
| C    | `carrot_core` library     |                                    |  https://github.com/monero-project/monero/pull/9559 | AM, AN, L, J | ❌ |
| D    | Cold device depends on `wallet2_basic` + hot-cold instead of all `wallet2` | device, device_trezor | | B | ❌ |
| E    | Add FCMP++ / Carrot basic shared type and function definitions | cryptonote_basic  | | C | ❌ |
| F    | Add container helpers and vector merge functions | common | | |  ❌ |
| G    | `carrot_impl` library | | https://github.com/monero-project/monero/pull/9697 | C, E| ❌ |
| H   | View-scan changes and splitting `process_new_transaction()` | wallet | | C | ❌ |
| I    | Unclamped changes to `mx25519` | crypto | | | ❌ |
| J    | Faster zero commit | blockchain_db, carrot_core, carrot_impl, cryptonote_core, ringct, wallet | https://github.com/monero-project/monero/pull/10108 | | ❌ |
| K   | Collect transparent amount commitments helper | blockchain_db, cryptonote_core, wallet | | J | ❌ |
| L   | FCMP++ crypto | fcmp_pp, ringct | https://github.com/monero-project/monero/pull/10111, https://github.com/monero-project/monero/pull/10338, https://github.com/monero-project/monero/pull/10134, https://github.com/monero-project/monero/pull/10135, https://github.com/monero-project/monero/pull/10342, https://github.com/monero-project/monero/pull/10345 (there are more) | | ❌ |
| M  | FCMP++ Rust FFI | | | | ❌ |
| N  | FCMP++ format utils | blockchain_db, cryptonote_basic, cryptonote_core, wallet | | | ❌ |
| O  | FCMP++ static proof len calculation| fcmp_pp, ringct, wallet, cryptonote_core | | M | ❌ |
| P  | FCMP++ types | fcmp_pp, ringct, wallet | | M, O | ❌ |
| Q  | FCMP++ RingCT type | carrot_impl, cryptonote_basic, cryptonote_core, ringct, wallet | | P | ❌ |
| R  | FCMP++ tower cycle | fcmp_pp, wallet | | M, P | ❌ |
| S  | FCMP++ curve trees| blockchain_db, carrot_impl, cryptonote_basic, cryptonote_core, fcmp_pp, rpc, wallet |  | L, M, P, R | ❌ |
| T  | FCMP++ tree cache | wallet | | F, P, S | ❌ |
| U  | FCMP++ db integration | blockchain_db, cryptonote_core | | J, K, N, S | ❌ |
| V  | Daemon RPC path by output ID | rpc, wallet | | U | ❌ |
| W  | Daemon RPC getblocks.bin init tree sync data | rpc | | U | ❌ |
| X   | Daemon RPC return false on get hash by too high block | rpc | https://github.com/monero-project/monero/pull/10109 | | ✅️ |
| Y   | Daemon RPC allow skipping common block in getblocks.bin by block_ids | rpc | https://github.com/monero-project/monero/pull/10143 | | ✅️ |
| Z  | FCMP++ wallet2 scanning integration | wallet | | K, N, S, T, W, X, Y | ❌ |
| AA  | FCMP++ wallet2 `scan_tx` integration | wallet | | Z, V| ❌ |
| AB  | Require wallets point to updated daemon | wallet | | V, W, X, Y | ❌ |
| AC | FCMP++ consensus integration | cryptonote_core | | U, Q | ❌ |  
| AD | Daemon: relay empty fluffy block on found block #155 | cryptonote_core | https://github.com/monero-project/monero/pull/10205 | | ✅️ |
| AE | Daemon: bump fluffy block byte size limit, match new block #159 | cryptonote_basic | | | ❌ |
| AF |  wallet: CLI & RPC speed up refresh/show_transfers w/large pool #162  | wallet | | | ❌ |
| AG | Daemon: send tx slices in pool complement response #168 | cryptonote_protocol | | |❌ |
| AH | blockchain_prune: check DB version | blockchain_utilities | https://github.com/monero-project/monero/pull/10179 | | ✅️ |
| AI | tx pool: only increment m_txpool_weight for newly added pool txs #194 | cryptonote_core | https://github.com/monero-project/monero/pull/10203 | | ✅️ |
| AJ | tx pool: don't drop connections relaying key images spent in chain #204 | cryptonote_core | | | ❌ |
| AK | simplewallet: use passed decrypted payment ID from wallet2 for notifications | simplewallet, wallet | https://github.com/monero-project/monero/pull/10189 | | ❌ |
| AL | common: add std equivalent of hash_combine() | common | https://github.com/monero-project/monero/pull/10215 | | ✅️ |
| AM | crypto: add FCMP++ generators T, U, & V | crypto | https://github.com/monero-project/monero/pull/9827 | | ❌ |
| AN | crypto: add Ed25519->X25519 conversion functions | crypto | https://github.com/monero-project/monero/pull/9828 | L (partially) | ❌ |
| AO | cryptonote_basic: add overload for `get_block_longhash()` | cryptonote_basic | https://github.com/monero-project/monero/pull/10039 | | ❌ |
| AP | less noisy perf logs #100 | wallet2 | | | ❌ |
| AQ | #253 | cryptonote_core | | | ❌ |
| AR | runaway spans #234, #275 | cryptonote_protocol |https://github.com/monero-project/monero/pull/9495, https://github.com/monero-project/monero/pull/10303 | | ❌ |
| AS | common: fix `apply_permutation()` for `std::vector<bool>` | common | https://github.com/monero-project/monero/pull/10273 | | ❌ | 
| AT | OOM fix for FCMP++ #228 | | | | ❌ |


# Discussion History
# Action History
- Created by: jeffro256 | 2025-09-15T21:27:56+00:00
