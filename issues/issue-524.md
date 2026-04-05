---
title: Broadcast new alt blocks
source_url: https://github.com/Cuprate/cuprate/issues/524
author: Boog900
assignees: []
labels:
- C-optimization
- C-proposal
- E-easy
- A-binaries
created_at: '2025-08-06T15:43:19+00:00'
updated_at: '2026-02-10T14:37:02+00:00'
type: issue
status: closed
closed_at: '2026-02-10T14:37:02+00:00'
---

# Original Description


## What
New alt-blocks should be broadcasted to peers as well as new blocks.

## Why
Doing what we currently do can slow down the network as it will cause nodes to initiate a sync if they don't have the block and the alt chain wins.

## Where
https://github.com/Cuprate/cuprate/blob/9c2c942d2fcf26ed8916dc3f9be6db43d8d2ae78/binaries/cuprated/src/blockchain/manager/handler.rs#L95-L96



# Discussion History
# Action History
- Created by: Boog900 | 2025-08-06T15:43:19+00:00
- Closed at: 2026-02-10T14:37:02+00:00
