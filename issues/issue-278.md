---
title: Different RPC behavior between `cuprated` and `monerod`
source_url: https://github.com/Cuprate/cuprate/issues/278
author: hinto-janai
assignees: []
labels:
- C-discussion
- A-rpc
created_at: '2024-09-10T22:23:22+00:00'
updated_at: '2024-10-23T23:47:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This is a discussion for [daemon RPC calls](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html) in `cuprated` that will behave differently than `monerod` or not be supported.

The RPC calls considered are the publically available ones from [`cc73fe7`](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454).

In general, adhoc `string` fields in `monerod` (including errors) will most likely differ in `cuprated`.

## Different behavior
This table describes RPC calls that will exist in `cuprated` but will have slightly different behavior than `monerod`.

| RPC method/endpoint | Reason |
|---------------------|--------|
| [`get_connections`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_connections) | TODO: `peer_id`, `connection_id`: https://github.com/Cuprate/cuprate/issues/278#issue-2518048784
| [`get_info`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_info) | TODO: `update_available`, `version` fields
| [`version`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#version) | TODO
| [`/set_log_level`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#set_log_level) | `cuprated`'s log levels may differ from `monerod`'s
| [`/set_log_categories`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#set_log_categories) | TODO: dynamic log levels: <https://docs.rs/tracing-subscriber/latest/tracing_subscriber/reload/index.html>
| [`/update`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#update) | TODO: update `cuprated`?
| [`generateblocks`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#generateblocks) | TODO: this is only supported on `monerod`'s `--regtest`, will `cuprated` have `--regtest`?
| [`flush_cache`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#flush_cache) | TODO: will `cuprated` have [`m_invalid_blocks`](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_core/blockchain.cpp#L2822)? Should this only flush the txpool?
| [`sync_info`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#sync_info) | TODO: `overview`: https://github.com/Cuprate/cuprate/pull/320#discussion_r1811063772

## Not supported
This table describes RPC calls which exist in `monerod` but will not be supported in `cuprated`.

This may mean they return a `404` or return some special error message that indicates it isn't supported.

| RPC method/endpoint | Reason |
|---------------------|--------|
| [`/start_mining`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#start_mining), [`/stop_mining`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#stop_mining), [`/mining_status`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#mining_status), [`/set_log_hash_rate`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#set_log_hash_rate) | `cuprated` will not include a miner
| [`/get_info`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_info), [`/start_save_graph`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#start_save_graph), [`/stop_save_graph`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#stop_save_graph) | Deprecated

# Discussion History
## dimalinux | 2024-09-17T18:23:05+00:00
I'd put in a vote for supporting a `--regtest` flag. When I was working on ETH<->XMR atomic swaps, we made extensive use of both the `--regtest` flag and `generateblocks` in our tests. If you are writing client RPC libraries and other tooling, it is also very useful to spin up a test instance for tests to query. I'm assuming it would be less work and code to maintain than having a simulator like Hardhat for Ethereum.

# Action History
- Created by: hinto-janai | 2024-09-10T22:23:22+00:00
