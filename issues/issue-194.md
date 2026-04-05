---
title: Alt Block/ Chain Handling
source_url: https://github.com/Cuprate/cuprate/issues/194
author: Boog900
assignees: []
labels:
- A-consensus
- A-storage
- C-proposal
created_at: '2024-06-26T01:22:50+00:00'
updated_at: '2024-07-31T00:02:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
 
## What

Adding alt block handling to Cuprate's components, the consensus and DB code needs to be able to handle reorgs.

The block downloader can already handle downloading an alt chain.

## How

### Consensus changes

The consensus changes are being completed in this PR: #214

### Database changes

#214 makes some changes to the `BCRequest`/response enums these new requests will need to be handled in the DB.

To do this some new tables will need to be added:

#### AltChainsInfo

Key: `ChainID`
Value: `AltChainInfo`

```rust
struct AltChainInfo {
    parent_chain: Chain,
    common_ancestor_height: u64
}
``` 

#### AltBlockHeights

Key: Block Hash (`[u8; 32]`).
Value: `AltBlockHeight` 

```rust
struct AltBlockHeight {
     /// The ID of the alt chain the alt block is on.
    chain_id: ChainID,
    height: u64
}
```
#### AltBlocksInfo

Key: `AltBlockHeight`
Value: `CompactAltBlockInfo`

```rust
struct CompactAltBlockInfo {
    /// The block's hash.
    ///
    /// [`Block::hash`].
    pub block_hash: [u8; 32],
    /// The block's proof-of-work hash.
    pub pow_hash: [u8; 32],
    /// The block's height.
    pub height: u64,
    /// The adjusted block size, in bytes.
    pub weight: usize,
    /// The long term block weight, which is the weight factored in with previous block weights.
    pub long_term_weight: usize,
    /// The cumulative difficulty of all blocks up until and including this block.
    pub cumulative_difficulty: u128,
}
```

#### AltBlockBlobs

Key: `AltBlockHeight`
Value: `Vec<u8>`

#### AltTransactionBlobs

Key: Tx hash (`[u8; 32]`)
Value: `Vec<u8>`

#### AltTransactionsInfo

Key: Tx hash (`[u8; 32]`)
Value: `AltTransactionInfo`

```rust
struct AltTransactionInfo {
    /// The transaction's weight.
    ///
    /// [`Transaction::weight`].
    pub tx_weight: usize,
    /// The transaction's total fees.
    pub fee: u64,
    /// The transaction's hash.
    ///
    /// [`Transaction::hash`].
    pub tx_hash: [u8; 32],
}
```
### DB request changes 

And some new request variants need to be added:

```rust

// https://github.com/Cuprate/cuprate/blob/dced4ed7ecd6f5a93b0102f3bde6bf13ad5aff4d/types/src/blockchain.rs#L110
pub enum BCWriteRequest {
    ....

    /// Pop some blocks from the top of the main chain, adding the popped blocks to the alt block tables 
    PopBlocks(usize),
    /// Add an alt block to the alt block tables.
    AddAltBlock(AltBlockInformation),
    /// Clear all alt block tables.
    FlushAltBlocks,
}

// https://github.com/Cuprate/cuprate/blob/dced4ed7ecd6f5a93b0102f3bde6bf13ad5aff4d/types/src/blockchain.rs#L24
pub enum BCReadRequest {
    ....

    /// Returns all blocks in an alt chain up to the point the chain meets the main chain.
    /// The input is the top block hash in the alt chain 
    AltChain([u8; 32])
}

// https://github.com/Cuprate/cuprate/blob/dced4ed7ecd6f5a93b0102f3bde6bf13ad5aff4d/types/src/blockchain.rs#L125
pub enum BCResponse {
    ....
    /// A list of alt blocks in chronological order.
    AltChain(Vec<AltBlockInformation>)
    
```

These todos also need to be completed:

https://github.com/Cuprate/cuprate/blob/dced4ed7ecd6f5a93b0102f3bde6bf13ad5aff4d/storage/blockchain/src/service/read.rs#L210

https://github.com/Cuprate/cuprate/blob/dced4ed7ecd6f5a93b0102f3bde6bf13ad5aff4d/storage/blockchain/src/service/read.rs#L326

https://github.com/Cuprate/cuprate/blob/dced4ed7ecd6f5a93b0102f3bde6bf13ad5aff4d/storage/blockchain/src/service/read.rs#L382




# Discussion History
# Action History
- Created by: Boog900 | 2024-06-26T01:22:50+00:00
