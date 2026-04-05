---
title: Allow information on block sync to be returned from the block downloader.
source_url: https://github.com/Cuprate/cuprate/issues/475
author: Boog900
assignees: []
labels:
- A-p2p
- C-request
created_at: '2025-05-13T17:44:03+00:00'
updated_at: '2025-05-13T17:44:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

## Feature

The block downloader currently just returns a stream of blocks: https://github.com/Cuprate/cuprate/blob/ce7a04f2d964875a95530b4cb2cb9522f6fce2f4/p2p/p2p/src/block_downloader.rs#L144-L148

This issue for creating a way to get information on the sync state from the block downloader.

This could be done by instead returning a struct from the block downloader:

```rust
struct BlockDownloaderHandle {
    stream: BufferStream<BlockBatch>,
    tx: mpsc::Sender<(BlockDownloaderRequest, oneshot::Sender<BlockDownloaderResponse>)>,
}
```

with `BlockDownloaderRequest` & `BlockDownloaderResponse` being enums, for now they can just be:

```rust
enum BlockDownloaderRequest {
    TargetHeight
}

enum BlockDownloaderResponse {
    /// The height we are syncing to.
    TargetHeight(usize)
}
```

Then a new branch in here should listen on the other end of the channel to respond to requests:

https://github.com/Cuprate/cuprate/blob/ce7a04f2d964875a95530b4cb2cb9522f6fce2f4/p2p/p2p/src/block_downloader.rs#L649


# Discussion History
# Action History
- Created by: Boog900 | 2025-05-13T17:44:03+00:00
