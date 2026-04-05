---
title: Panic at `binaries/cuprated/src/blockchain/manager/handler.rs:170:32`
source_url: https://github.com/Cuprate/cuprate/issues/435
author: hinto-janai
assignees: []
labels:
- C-bug
created_at: '2025-04-09T15:29:21+00:00'
updated_at: '2025-05-06T18:24:18+00:00'
type: issue
status: closed
closed_at: '2025-05-06T18:24:17+00:00'
---

# Original Description
## Bug
This line (sometimes) panics when going from cuprated `0.0.1` -> `0.0.2`.

https://github.com/Cuprate/cuprate/blob/95aca1d4a52c56975ab9e859cfb283be8a7d4838/binaries/cuprated/src/blockchain/manager/handler.rs#L170

Restarting enough times seems to fix it.

## Steps to reproduce
1. Sync `cuprated 0.0.1` to chaintip
2. Run `cuprated 0.0.2`
3. Panic

## Log
macOS ARM64:
```
INFO Starting blockchain syncer
INFO block_downloader: Attempting to download blocks from peers, this may take a while.
INFO incoming_block_batch{start_height=3386273 len=1}:pop_blocks_diff_cache{numb_blocks=1}:get_blocks_timestamps{block_heights=3385538..3385539 chain=Main}: Getting blocks timestamps
INFO incoming_block_batch{start_height=3386273 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_long_term_weights{range=3286273..3286274 chain=Main}: getting block long term weights.
INFO incoming_block_batch{start_height=3386273 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_block_weights{range=3386173..3386174 chain=Main}: getting block weights.
INFO incoming_block_batch{start_height=3386273 len=1}: Successfully added block batch alt_chain=true
INFO incoming_block_batch{start_height=3386274 len=1}:pop_blocks_diff_cache{numb_blocks=1}:get_blocks_timestamps{block_heights=3385538..3385539 chain=Main}: Getting blocks timestamps
INFO incoming_block_batch{start_height=3386274 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_long_term_weights{range=3286273..3286274 chain=Main}: getting block long term weights.
INFO incoming_block_batch{start_height=3386274 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_block_weights{range=3386173..3386174 chain=Main}: getting block weights.

thread 'cuprated-tokio' panicked at binaries/cuprated/src/blockchain/manager/handler.rs:170:32:
called `Option::unwrap()` on a `None` value
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Abort trap: 6
```

Linux x64:
```
INFO inbound_server: Starting inbound connection server
INFO Starting blockchain syncer
INFO block_downloader: Attempting to download blocks from peers, this may take a while.
INFO incoming_block_batch{start_height=3386273 len=1}:pop_blocks_diff_cache{numb_blocks=1}:get_blocks_timestamps{block_heights=3385538..3385539 chain=Main}: Getting blocks timestamps
INFO incoming_block_batch{start_height=3386273 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_long_term_weights{range=3286273..3286274 chain=Main}: getting block long term weights.
INFO incoming_block_batch{start_height=3386273 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_block_weights{range=3386173..3386174 chain=Main}: getting block weights.
INFO incoming_block_batch{start_height=3386273 len=1}: Successfully added block batch alt_chain=true
INFO incoming_block_batch{start_height=3386274 len=1}:pop_blocks_diff_cache{numb_blocks=1}:get_blocks_timestamps{block_heights=3385538..3385539 chain=Main}: Getting blocks timestamps
INFO incoming_block_batch{start_height=3386274 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_long_term_weights{range=3286273..3286274 chain=Main}: getting block long term weights.
INFO incoming_block_batch{start_height=3386274 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_block_weights{range=3386173..3386174 chain=Main}: getting block weights.

thread 'cuprated-tokio' panicked at binaries/cuprated/src/blockchain/manager/handler.rs:170:32:
called `Option::unwrap()` on a `None` value
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Aborted
```

# Discussion History
## Boog900 | 2025-04-09T15:39:17+00:00
I think this is due to this here:

https://github.com/Cuprate/cuprate/blob/95aca1d4a52c56975ab9e859cfb283be8a7d4838/binaries/cuprated/src/blockchain/manager/handler.rs#L271-L276

If the last block caused the re-org then there are no more blocks to add, so we should just return.

## hinto-janai | 2025-05-06T18:12:50+00:00
Still occurs on `cuprated v0.0.2`.

## Logs
Linux arm64:
```
INFO incoming_block_batch{start_height=3405694 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_block_weights{range=3405593..3405594 chain=Main}: getting block weights.
thread 'cuprated-tokio' panicked at binaries/cuprated/src/blockchain/manager/handler.rs:170:32:
called `Option::unwrap()` on a `None` value
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

macOS arm64:
```
INFO incoming_block_batch{start_height=3404857 len=1}:pop_blocks_weight_cache{numb_blocks=1}:get_block_weights{range=3404756..3404757 chain=Main}: getting block weights.

thread 'cuprated-tokio' panicked at binaries/cuprated/src/blockchain/manager/handler.rs:170:32:
called `Option::unwrap()` on a `None` value
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Abort trap: 6
```

macOS arm64 `tail ~/Library/"Application Support"/Cuprate/logs/2025-05-05`:

```
DEBUG incoming_block_batch{start_height=3404857 len=1}: Accounting for new blocks timestamp (1746434755) and cumulative_difficulty (452428535896961533)
DEBUG incoming_block_batch{start_height=3404857 len=1}: Adding new block's 3404856 weights to block cache, weight: 227530, long term weight: 227530
DEBUG incoming_block_batch{start_height=3404857 len=1}: Accounting for new blocks vote, height: 3404856, vote: V16
DEBUG incoming_block_batch{start_height=3404857 len=1}: verifying block: a5d1aa06cd634047b69a3a3f82ce69861fb18d31bc6f098ff33126913beada09
DEBUG incoming_block_batch{start_height=3404857 len=1}: Verifying block header.
DEBUG incoming_block_batch{start_height=3404857 len=1}: Updating blockchain cache with new block, height: 3404857
DEBUG incoming_block_batch{start_height=3404857 len=1}: Accounting for new blocks timestamp (1746434872) and cumulative_difficulty (452429074977382286)
DEBUG incoming_block_batch{start_height=3404857 len=1}: Adding new block's 3404857 weights to block cache, weight: 155724, long term weight: 176470
DEBUG incoming_block_batch{start_height=3404857 len=1}: Accounting for new blocks vote, height: 3404857, vote: V16
DEBUG net{zone="ClearNet"}:handle_free_permit:connect_to_outbound_peer:handshaker{addr=24.159.246.160:18080}: Sending handshake request.
```

## hinto-janai | 2025-05-06T18:24:17+00:00
https://github.com/Cuprate/cuprate/pull/438 fixes this but was not included in `v0.0.2`.

# Action History
- Created by: hinto-janai | 2025-04-09T15:29:21+00:00
- Closed at: 2025-05-06T18:24:17+00:00
