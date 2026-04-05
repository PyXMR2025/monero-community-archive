---
title: Split `BlockBlobs` table
source_url: https://github.com/Cuprate/cuprate/issues/282
author: Boog900
assignees:
- Asurar0
labels:
- A-storage
- C-proposal
- E-medium
- E-help-wanted
created_at: '2024-09-16T02:11:49+00:00'
updated_at: '2024-09-19T19:05:42+00:00'
type: issue
status: closed
closed_at: '2024-09-19T19:05:42+00:00'
---

# Original Description


## What

The `BlockBlobs` table stores the serialized block blob, this issues is for splitting that table into a `BlockHeaderBlobs` and `BlockTxHashes`.


## Why 

The block blob contains the miner tx blob which means we are duplicating miner txs in the DB. Splitting the table also means we wouldn't have to parse the full block when we need to retrieve tx blobs for the block. 



# Discussion History
## Asurar0 | 2024-09-16T22:45:12+00:00
I would appreciate being assigned to this issue.

## Boog900 | 2024-09-18T13:02:34+00:00
@Asurar0 I am having problems with matrix but I saw your message.

You will need to add another field to `BlockInfo`, the miner transactions index. You can then use this index to look up the miner tx

# Action History
- Created by: Boog900 | 2024-09-16T02:11:49+00:00
- Closed at: 2024-09-19T19:05:42+00:00
