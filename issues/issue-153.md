---
title: '[Proposal] Fast Sync'
source_url: https://github.com/Cuprate/cuprate/issues/153
author: Boog900
assignees: []
labels:
- C-proposal
- E-help-wanted
created_at: '2024-06-07T16:35:24+00:00'
updated_at: '2024-06-14T22:02:41+00:00'
type: issue
status: closed
closed_at: '2024-06-14T22:02:41+00:00'
---

# Original Description
## What

Fast sync is used by monerod speed up synchronization by embedding known hashes and skipping verification of those blocks.

## Where

This should be its own crate under `consensus`.

## How

There will be 2 parts of fast sync, a separate binary that takes in a block height and produces the list of verified hashes up to that point and the fast sync service itself.

The embedded hashes will be a separate file that will be [`include`]( https://doc.rust-lang.org/std/macro.include.html)ed in a static. 

The embedded hashes will contain hashes of a group of N block hahses, `N` being a configurable number, monerod uses 512.

i.e. the file will contain: `H(blockID_1, BlockID_2 ... , BlockID_N), H(BlockID_N+1, ...) ....`.

The format of the embedded file should be something like:  

```
[
    HASH_1,
    HASH_2,
    ....,
]
```

The fast sync `tower::Service` will hold the `context_svc` like the block verifier currently does:

https://github.com/Cuprate/cuprate/blob/07f61bdb9c365c5f51e3fd0254c5ca1b6a186c38/consensus/src/block.rs#L102-L111

For the fast sync service the request/response enums will look something like:

```rust
/// This struct holds a blockId which is contained in our hash of hashes file.
/// People outside this crate should not be able to create this.
struct ValidBlockId([u8; 32]);

enum FastSyncRequest {
    /// Checks if the `block_ids` are contained in the hash of hashes file.
    /// it is an error to call this with a start_height which is not a multiple of `N` (could make it a const generic to enforce this).
    ValidateHashes {
        start_height: u64,
        block_ids: Vec<[u8; 32]>
    },
    /// A request to validate a block.
    ValidateBlock {
        block: Block,
        txs: HashMap<[u8; 32], Transaction>,
        /// The token got from a call to [`FastSyncRequest::ValidateHashes`]
        token: ValidBlockId,
    }
}

enum FastSyncResponse {
    /// A response to a [`FastSyncRequest::ValidateHashes`]
    ValidateHashes {
        /// hashes which are known to be valid.
        validated_hashes: Vec<ValidBlockId>,
        /// hashes which can not be validated as there are not enough to fill the next batch.
        unknown_hashes: Vec<[u8; 32]>,
    }
    /// This block is valid.
    ValidateBlock(VerifiedBlockInformation)
}

enum FastSyncError {
    /// The request to validate hashes was too high, past the amount of embedded hashes. 
    OutOfRange,
    /// The request to validate hashes contained a group of hashes not in our embedded list.
    NotContained,  
    .... (Maybe more?)
}
```

The process of synchronization would now look like:  

1) peer sends hashes 
2) we validate hashes with our Fast Sync service, getting a token for each hash.
3) we download blocks from peer(s).
4) we give block and token to Fast Sync service to validate hashes match.
5) Fast Sync service computes `VerifiedBlockInformation`, leaving the PoW hash as all 0s like monerod.

`VerifiedBlockInformation`: https://github.com/Cuprate/cuprate/blob/07f61bdb9c365c5f51e3fd0254c5ca1b6a186c38/types/src/types.rs#L67


# Discussion History
## SyntheticBird45 | 2024-06-07T18:22:05+00:00
 > The embedded hashes will be a separate file that will be [include](https://doc.rust-lang.org/std/macro.include.html)ed in a static.

What is the expected size of this rainbow table ?

## Boog900 | 2024-06-07T19:22:08+00:00
>What is the expected size of this rainbow table ?

Pretty big, I updated the issue with a different scheme 

## Boog900 | 2024-06-14T22:02:41+00:00
completed in #156 

# Action History
- Created by: Boog900 | 2024-06-07T16:35:24+00:00
- Closed at: 2024-06-14T22:02:41+00:00
