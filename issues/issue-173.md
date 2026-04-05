---
title: '[fast-sync] switching from SHA3 Keccak256 to BLAKE3'
source_url: https://github.com/Cuprate/cuprate/issues/173
author: SyntheticBird45
assignees: []
labels:
- C-proposal
created_at: '2024-06-19T09:57:23+00:00'
updated_at: '2025-04-08T18:46:10+00:00'
type: issue
status: closed
closed_at: '2025-04-08T18:46:10+00:00'
---

# Original Description
## What

Fast-sync is actually checking the integrity of blocks with Keccak256, like monerod does. However, BLAKE3 is much, much faster and profit from nice feature such as verified streaming.
https://github.com/BLAKE3-team/BLAKE3

## Where/How
For the moment, basically replace https://github.com/Cuprate/cuprate/blob/main/consensus/fast-sync/src/util.rs#L6 with BLAKE3 hasher from the official BLAKE3 crate. And modify the building binary to make BLAKE3 hashes.

## Why
It would be a free performance improvements. BLAKE3 is as said above, capable of being used for verified streaming. We could imagine in the future an asynchronous verifier that hashes (using blake3) blocks bytes as they arrive and then add them to the batch hasher tree in order to verify a batch.

# Discussion History
# Action History
- Created by: SyntheticBird45 | 2024-06-19T09:57:23+00:00
- Closed at: 2025-04-08T18:46:10+00:00
