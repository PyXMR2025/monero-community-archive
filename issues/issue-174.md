---
title: Batch retrieve outputs
source_url: https://github.com/Cuprate/cuprate/issues/174
author: Boog900
assignees: []
labels:
- A-consensus
- A-storage
- A-types
- C-optimization
- C-proposal
- E-hard
created_at: '2024-06-19T16:54:30+00:00'
updated_at: '2025-03-06T16:17:11+00:00'
type: issue
status: closed
closed_at: '2025-03-06T16:17:11+00:00'
---

# Original Description

## What

When batch preparing blocks for verification we could retrieve the outputs used across all the transactions in the blocks, currently this is only done on a per-block level. Then as we verify blocks we would have to add each blocks outputs to the cache.

## Where

`cuprate-consensus`, `cuprate-blockchain` & `cuprate-types`

## Why

To speed up synchronization as we get closer to the top of the chain.

## How

We will need an output cache type, which should be defined in `cuprate-types`, we should then add another DB request type to construct this output cache from the available outputs (the DB shouldn't fail if an output is not there as it could be in the batch of blocks).

This cache will then be used instead of the DB to get ring members.

## Potential issues

How can we limit the number of outputs allowed to be retrieved? 

We already check PoW of the blocks but this could still be an issue if it allows an attacker to make us request millions of outputs.    



# Discussion History
# Action History
- Created by: Boog900 | 2024-06-19T16:54:30+00:00
- Closed at: 2025-03-06T16:17:11+00:00
