---
title: Internal data needed for `cuprated`'s RPC
source_url: https://github.com/Cuprate/cuprate/issues/279
author: hinto-janai
assignees: []
labels:
- A-p2p
- A-storage
- C-discussion
- P-high
- A-rpc
created_at: '2024-09-11T21:21:33+00:00'
updated_at: '2024-10-08T21:57:10+00:00'
type: issue
status: closed
closed_at: '2024-10-08T21:57:10+00:00'
---

# Original Description
## What
This is a discussion for what data is required for `cuprated`'s RPC system.

Notably, this is:
- Blockchain data
- Transaction pool data
- P2P data
- General process state

The following tables (except the general process state) are newly proposed requests/responses to be added to each system's `tower::Service` API such that the RPC system can fulfill the request. The RPC system is assumed to have read access (and write access where needed) to all systems via `tower::Service` handles.

## Blockchain

| Request                   | Response                       | Needed for              | Description |
|---------------------------|--------------------------------|-------------------------|-------------|
| `PopBlocks(u64)`          | `u64`                          | `/pop_blocks`           | Pop `n` blocks, return the new height
| `Prune`                   | TODO                           | `prune_blockchain`      | Prune the blockchain
| `Pruned`                  | `bool`                         | `prune_blockchain`      | Is the blockchain pruned?
| `Block(u64)`              | `Block`                        | `get_block`             | Retrieve block information
| `BlockByHash([u8; 32])`   | `Block`                        | `get_block`             | Same as `Block`; for convenience
| `TopBlock`                | `Block`                        |                         | Get the latest `Block`, Same as `Block`; for convenience
| `TopBlockExtendedHeader`  | `ExtendedBlockHeader`          |                         | Get the latest `ExtendedBlockHeader`; for convenience
| `KeyImageSpent([u8; 32])` | `bool`                         | `/is_key_image_spent`   | Singular version of already existing `KeyImagesSpent`
| `TopBlockFull`            | `(Block, ExtendedBlockHeader)` | `get_last_block_header` | Get information on the last block to map to `cuprate_rpc_types::misc::BlockHeader`
| `TopBlockHash`            | `[u8; 32]`                     | `get_info`              | Get the top block hash.
| `TotalTxCount`            | `u64`                          | `get_info`              | Get the total amount of non-coinbase transactions; `cuprate_rpc_types::json::GetInfoResponse::tx_count`
| `DatabaseSize`            | `(u64, u64)`                   | `get_info` | Return byte size of database file and available space for `cuprate_rpc_types::json::GetInfoResponse::{database_size,free_space}`
| `BlockWeightLimit`        | `u64`                          | `get_info` | `cuprate_rpc_types::json::GetInfoResponse::block_weight_limit`
| `BlockWeightMedian`       | `u64`                          | `get_info` | `cuprate_rpc_types::json::GetInfoResponse::block_weight_median`
| `Difficulty(usize)`       | `u128`                         | `get_info` | Difficulty for a specific block (input = height) `cuprate_rpc_types::json::GetInfoResponse::difficulty[_top64]`
| `CurrentHardFork`         | `HardFork`                     | `hard_fork_info` | Retrieve the latest `HardFork`
| `HardForkInfo(Hardfork)`  | `HardForkInfo`                 | `hard_fork_info` | Retrieve various information about a hardfork; `cuprate_rpc_types::json::HardForkInfoResponse`; https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.cpp#L2751; https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_basic/hardfork.cpp#L408;
| `OutputHistogram`         | `OutputHistogram`              | `get_output_histogram` | https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/blockchain_db/lmdb/db_lmdb.cpp#L4222
| `CoinbaseTxSum`           | `CoinbaseTxSum`                | `get_coinbase_tx_sum`  | https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_core/cryptonote_core.cpp#L1265
| `FeeEstimate(grace_blocks: u64)`        | TODO             | `get_fee_estimate`     | TODO: Impl of dynamic fees required: https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_core/blockchain.cpp#L3791
| `MinerData`                             | TODO             | `get_miner_data`       | https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_core/blockchain.cpp#L1822
| TODO | TODO | `get_alternate_chains` | TODO
| TODO | TODO | TODO | TODO |

## Transaction pool

| Request                | Response              | Needed for            | Description |
|------------------------|-----------------------|-----------------------|-------------|
| `Backlog`              | `Vec<TxBacklogEntry>` | `get_txpool_backlog`  | Get misc information on all transactions in the pool.
| `PoolSize`             | `u64`                 | `get_info`            | Number of transactions that have been broadcast but not included in a block; `cuprate_rpc_types::json::GetInfoResponse::tx_pool_size`
| `Flush(Vec<[u8; 32]>)` | `()`                  | `flush_txpool`        | Flush the given transaction hashes from the txpool (all if `Vec` is empty).
| TODO | TODO | TODO | TODO |

## P2P

| Request                                          | Response            | Needed for            | Description |
|--------------------------------------------------|---------------------|-----------------------|-------------|
| `RelayBlock(Block)`                              | `()`                | `submit_block`        | Relay a found block
| `ConnectionInfo`                                 | P2P connection data | `get_connections`     | Must map into `cuprate_rpc_types::misc::ConnectionInfo`
| `Syncing`                                        | `bool`              | `get_info`            | `cuprate_rpc_types::json::GetInfoResponse::busy_syncing`
| `Synced`                                         | `bool`              | `get_info`            | `cuprate_rpc_types::json::GetInfoResponse::synchronized`
| `Target`                                         | `u64`               | `get_info`            | `cuprate_rpc_types::json::GetInfoResponse::target`
| `TargetHeight`                                   | `u64`               | `get_info`            | `cuprate_rpc_types::json::GetInfoResponse::target_height`
| `PeerlistSize`                                   | `(u64, u64)`        | `get_info`            | `cuprate_rpc_types::json::GetInfoResponse::{white,grey}_peerlist_size`
| `ConnectionCount`                                | `(u64, u64)`   | `get_info`            | `cuprate_rpc_types::json::GetInfoResponse::{incoming,outgoing}_connections_count`
| `SetBan(cuprate_rpc_types::json::SetBanRequest)` | `()` | `set_ban` | (Un)ban an IP for `n` seconds
| `GetBan`                                         | `cuprate_rpc_types::json::GetBan`       | `banned` | Get information about a single ban
| `GetBans`                                        | `Vec<cuprate_rpc_types::json::GetBan>` | `get_ban` | Get information about all bans
| TODO | TODO | TODO | TODO |

## `cuprated` state
There is extra state the RPC needs on the more global binary/process level.

This is state that makes sense as global `static`s on the `cuprated`-level (or some library exposed to all).

| Static                                | Type                | Needed for | Description |
|---------------------------------------|---------------------|------------|-------------|
| `START_INSTANT`, `START_INSTANT_UNIX` | `SystemTime`, `u64` | `get_info` | Start time of daemon; `cuprate_rpc_types::json::GetInfoResponse::start_time`
| TODO | TODO | TODO | TODO |

# Discussion History
## Boog900 | 2024-09-14T15:33:25+00:00
## Blockchain

| Request                |                                                                                                                               |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| PopBlocks(u64)         | This will be a request for the blockchain manager.                                                                            |
| Prune                  | This should be left as a TODO                               |
| Pruned                 | The could just return false for now until we decide on how pruning will be done.                                              |
| TopBlock               | The could be a request to the context cache to get the blockchain context and then a request to the DB with the top block height |
| TopBlockExtendedHeader | Same as above                                                                                                                 |
| TopBlockHash           | The blockchain context cache can already give this information.                                                               |
| BlockWeightLimit       | The blockchain context cache can already give this information.                                                               |
| BlockWeightMedian      | The blockchain context cache can already give this information.                                                               |
| CurrentHardFork        | The blockchain context cache can already give this information.                                                               |
| HardForkInfo           | This request should go to the context cache - it is not currently available though                                            |
| FeeEstimate            | This request should go to the context cache - it is not currently available though                                            |

## Transaction pool

The transaction pool is going to have a specific interface for requests that mutate the pool, just to keep in mind, it wont directly use the write handle.

## P2P

| Request         |                                                |
|-----------------|------------------------------------------------|
| RelayBlock      | This will be handled by the blockchain manager |
| Syncing         | Same as above                                  |
| Synced          | Same as above                                  |
| Target          | Same as above                                  |
| TargetHeight    | Same as above                                  |
| PeerlistSize    | This should go to the address book service     |
| ConnectionCount | Same as above                                  |
| SetBan          | Same as above                                  |
| GetBan          | Same as above                                  |
| GetBans         | Same as above                                  |


# Action History
- Created by: hinto-janai | 2024-09-11T21:21:33+00:00
- Closed at: 2024-10-08T21:57:10+00:00
