---
title: Monero RPC routes/types/docs discrepancies
source_url: https://github.com/Cuprate/cuprate/issues/159
author: hinto-janai
assignees: []
labels:
- A-rpc
created_at: '2024-06-12T21:41:29+00:00'
updated_at: '2024-08-06T00:27:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue will keep track of problems with `monerod` RPC routes/types.

## Undocumented endpoint
These endpoints exist in code but are not documented on the [website](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html).

| Endpoint | Definition | Notes |
|----------|------------|-------|
| `/get_transaction_pool_hashes` | [rpc/core_rpc_server.h @ 125](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.h#L125), [rpc/core_rpc_server_commands_defs.h @ 1625..L1635](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1615-L1635) | This is the same as `/get_transaction_pool_hashes.bin` but it returns `tx_hashes` as a JSON array instead of binary |
| `/get_public_nodes` | [rpc/core_rpc_server.h @ 119](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.h#L119), [rpc/core_rpc_server_commands_defs.h @ 1398..L1448](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1398-L1448) | Returns public peer node information |
| `/get_output_distribution.bin` | [rpc/core_rpc_server.h @ 138](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.h#L138), [rpc/core_rpc_server_commands_defs.h @ 2445..2520](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2445-L2520) | This routes to the same handler as `/json_rpc`'s `get_output_distribution` |
| `/get_txids_loose` | [rpc/core_rpc_server.h @ 181](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.h#L181), [rpc/core_rpc_server_commands_defs.h @ 2798..2823](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2798-L2823) | |

## Unused endpoint/type
These endpoints/types exist in code but are not actively used.

| Route/type name | Link | Notes |
|-----------------|------|-------|
| RPC access endpoints and types | [rpc/core_rpc_server.h @ 182..187](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.h#L182-L187), [rpc/core_rpc_server.h @ 2522..2720](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2522-L2720) | Pseudo-deprecated endpoints |
| `COMMAND_RPC_SUBMIT_RAW_TX` | [rpc/core_rpc_server_commands_defs.h @ 340..368](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L340-L368) | Added in: <https://github.com/monero-project/monero/pull/2109>. This is not quite "unused", it is for usage in the [OpenMonero API](https://github.com/monero-project/meta/blob/master/api/lightwallet_rest.md#submit_raw_tx). |
| `COMMAND_RPC_FAST_EXIT` | [rpc/core_rpc_server_commands_defs.h @ 1833..1850](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1833-L1850) | Unused type leftover from `/fast_exit` endpoint |
| `/start_save_graph` | [/start_save_graph](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#start_save_graph) | Obsolete endpoint that doesn't return anything, but documents output |
| `/stop_save_graph` | [/stop_save_graph](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#stop_save_graph) | Obsolete endpoint that doesn't return anything, but documents output |

## Undocumented request fields
These endpoints have request fields that are missing on the [website](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html).

| Route/type name | Link | Notes |
|-----------------|------|-------|
| `get_block_header_by_hash` | [rpc/core_rpc_server_commands_defs.h @ 1245](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1245) | `hashes` |
| `hard_fork_info` | [rpc/core_rpc_server_commands_defs.h @ 1962](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1962), [rpc/core_rpc_server.cpp @ 2760](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.cpp#L2760) | `version`. This field lets you specify which hardfork info to retrieve |
| `get_output_distribution` | [rpc/core_rpc_server_commands_defs.h @ 2445..2465](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2445-L2465) | `binary`, `compress`, `top_hash`, `credits` |
| `get_output_distribution` | [rpc/message_data_structs.h @ 205](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/message_data_structs.h#L205) | Field in inner `struct output_distribution`: `cumulative` |
| `/get_blocks.bin` | [rpc/core_rpc_server_commands_defs.h @ 174..179](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L174-L179) | Optional fields: `requested_info`, `no_miner_tx`, `pool_info_since` |
| `/send_raw_transaction` | [rpc/core_rpc_server_commands_defs.h @ 617](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L617) | `do_sanity_checks` |
| `/get_peer_list` | [rpc/core_rpc_server_commands_defs.h @ 1373..1374](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1373-L1374) | `public_only`, `include_blocked` |
| `/out_peers` | [rpc/core_rpc_server_commands_defs.h @ 1909](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1909) | `set` |

## Undocumented response fields
These endpoints have response fields that are missing on the [website](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html).

| Route/type name | Link | Notes |
|-----------------|------|-------|
| `get_block_header_by_hash` | [rpc/core_rpc_server_commands_defs.h @ L1260](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1260) | `block_headers`. This method will return a `block_header` AND `block_headers` if the request only provided a `hashes`. The `block_header` struct is a bunch of default values (`0`, "", false). |
| `get_block_header_by_height` | [rpc/core_rpc_server_commands_defs.h @ 1271..1296](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1271-L1296) | `top_hash`, `credits` |
| `get_connections` | [cryptonote_protocol/cryptonote_protocol_defs.h @ 47..87](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/cryptonote_protocol/cryptonote_protocol_defs.h#L47-L87) | Fields in inner `struct connection_info`: `address_type`, `ssl`, `rpc_port`, `rpc_credits_per_hash`, `pruning_seed` |
| `set_bans` | [rpc/core_rpc_server_commands_defs.h @ 2063](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2063) | `untrusted` |
| `get_version` | [rpc/core_rpc_server_commands_defs.h @ 2170..2211](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2170-L2211) | `current_height`, `hard_forks`, `target_height` |
| `sync_info` | [rpc/core_rpc_server_commands_defs.h @ 2433](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2433) | `untrusted` |
| `get_txpool_backlog` | [diff @ 1567..1575](https://github.com/monero-project/monero/commit/5ffb2ff9b7c301eda5811a939c705f26627c4735#diff-da6ab0aecdf9547f57bb822783cae11fcfbaf7a2eae0d9cb5dbb69c8fc3b660aL1567-R1575), [rpc/core_rpc_server_commands_defs.h @ 1639](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1639) | Field rename: `blob_size` -> `weight` |
| `get_output_distribution` | [rpc/core_rpc_server_commands_defs.h @ 2445..2465](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2445-L2465) | `top_hash`, `credits` |
| `add_aux_pow` | [rpc/core_rpc_server_commands_defs.h @ 1103](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1103) | `status`, `untrusted` |
| `/get_blocks.bin` | [rpc/core_rpc_server_commands_defs.h @ 232..240](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L232-L240) | `daemon_time`, `credits`, `top_hash` |
| `/get_blocks_by_height.bin` | [rpc/core_rpc_server_commands_defs.h @ 281](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L281) | `credits`, `top_hash` |
| `/get_hashes_fast.bin` | [rpc/core_rpc_server_commands_defs.h @ 331](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L331) | `credits`, `top_hash` |
| `/get_o_indexes.bin` | [rpc/core_rpc_server_commands_defs.h @ 505](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L505) | `credits`, `top_hash` |
| `/get_transactions` | [rpc/core_rpc_server_commands_defs.h @ 418](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L418) | `credits`, `confirmations` |
| `/send_raw_transaction` | [rpc/core_rpc_server_commands_defs.h @ 640..643](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L640-L643) | `nonzero_unlock_time`, `sanity_check_failed`, `too_few_outputs`, `tx_extra_too_big` |
| `/get_peer_list` | [rpc/core_rpc_server_commands_defs.h @ 1390](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1390) | `untrusted` |
| `/stop_daemon` | [rpc/core_rpc_server_commands_defs.h @ 1827](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1827) | `untrusted` |
| `submit_block` | [rpc/core_rpc_server_commands_defs.h @ 1123](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1123) | `block_id`, `status`, `untrusted` |

## Incorrect documentation
These endpoints have incorrect documentation on the [website](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html). These range from nitpicks to truely incorrect documentation.

| Route/type name | Link | Notes |
|-----------------|------|-------|
| `get_miner_data` | [get_miner_data](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_miner_data) | Example uses non-standard `18082` for RPC port |
| `get_miner_data` | [get_miner_data](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_miner_data) | `difficulty` field is noted as `unsigned int`, although it is actually a JSON string containing an unsigned int in hex form. Other documentation describes these hex int strings as `string`. |
| `calc_pow` | [calc_pow](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#calc_pow), [cryptonote_basic/blobdatatype.h @ 39](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/cryptonote_basic/blobdatatype.h#L39) | Type used to describe `block_data` is `blobdata`. This is a `monerod`-specific type alias to `std::string`. Documentation should explain that it is a hex-encoded string of a block. |
| `flush_cache` | [flush_cache](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#flush_cache) | Missing space between `curl` command and output in example |
| `add_aux_pow` | [add_aux_pow](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#add_aux_pow) | Missing space between `curl` command and output in example, extra `'` at the end of `curl` command |
| `/get_outs.bin` | [get_outs.bin](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_outsbin), [rpc/core_rpc_server_commands_defs.h @ 538..544](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L538-L544) | Documentation mentions non-existent field: `amount` |
| `/get_alt_blocks_hashes` | [get_alt_blocks_hashes](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_alt_blocks_hashes) | `blks_hashes` should be marked as optional as an empty `std::vec` will not generate a JSON field |
| `/send_raw_transaction` | [send_raw_transaction](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#send_raw_transaction), [rpc/core_rpc_server_commands_defs.h @ 629..663](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L629-L663) | Documentation mentions non-existent field: `not_rct` |
| `/mining_status` | [mining_status](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#mining_status), [core_rpc_server_commands_defs.h @ 857..873](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L857-L873) | Documentation notates numbers as `int` instead of `unsigned int`. These are `unsigned int` both in code and elsewhere in documentation. |
| `/get_transaction_pool` | [get_transaction_pool](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_transaction_pool) | Missing documentation for `weight` field, should be `unsigned int; <DESCRIPTION>` |
| `submit_block` | [submit_block](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#submit_block) | Missing ending `}` in example |
| `get_block_template` | [get_block_template](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_block_template) | Missing ending `}` in example |
| `generateblocks` | [generateblocks](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#generateblocks) | Missing ending `}` in example |
| `flush_txpool` | [flush_txpool](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#flush_txpool) | Empty `""` transaction in example causes error |
| `get_block` | [get_block](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_block) | Documentation states for `tx_hashes` field: "If there are no other transactions, this will be an empty list." This is not true, `monerod`'s serializer will omit fields completely if the container is empty |

## Unoptimal behavior
These endpoints/types are set-up in an unoptimal way for seemingly no benefit.

| Route/type name | Link | Notes |
|-----------------|------|-------|
| `sync_info` | [rpc/core_rpc_server_commands_defs.h @ 2428](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#2433) | Unnecessarily nested field: `peers`. The `peers` struct just contains a single `connection_info` field, this causes the JSON output to be an array of maps containing `"info": {/* connection_info */}` instead of just an array of `connection_info`s |


## Undocumented behavior
These endpoints have undocumented behavior in certain situations.

| Route/type name | Link | Notes |
|-----------------|------|-------|
| `get_block` | [rpc/core_rpc_server_commands_defs.h @ 1298..1313](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L1298-L1313), [rpc/core_rpc_server.cpp @ 2674](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.cpp#L2674) | Undocumented behavior with mixed fields: `height`, `hash`. If both fields are provided, `monerod` will always pick `hash`, if an empty `hash` is provided, the genesis block is returned since the `height` gets set to the default `0` |

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-12T21:41:29+00:00
