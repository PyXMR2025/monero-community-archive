---
title: Return unspent txs in a reorg to the pool
source_url: https://github.com/Cuprate/cuprate/issues/526
author: Boog900
assignees: []
labels:
- A-storage
- C-proposal
- E-medium
- P-medium
- A-binaries
created_at: '2025-08-07T19:01:15+00:00'
updated_at: '2025-08-07T19:01:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

## What
During a reorg for any txs that are in blocks that got reorged, return the txs to the pool.

## Why
So we don't lose txs on a reorg.

## Where
Database, cuprated binary.

## How
When a reorg is called on the database the database should check all tx key images to see if any are not spent and return them if the reorg is successful. 


# Discussion History
# Action History
- Created by: Boog900 | 2025-08-07T19:01:15+00:00
