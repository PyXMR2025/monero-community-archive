---
title: '`constants` crate'
source_url: https://github.com/Cuprate/cuprate/issues/189
author: hinto-janai
assignees: []
labels:
- C-proposal
created_at: '2024-06-22T00:23:02+00:00'
updated_at: '2024-10-02T17:52:00+00:00'
type: issue
status: closed
closed_at: '2024-10-02T17:52:00+00:00'
---

# Original Description
## What
This proposal proposes creating a `constants` crate that contains general constant/static data used throughout Cuprate such as CryptoNote related data, genesis information, etc.

For example: `CRYPTONOTE_MAX_BLOCK_HEIGHT`.

## Why
There are many constants used throughout `monerod` and `cuprated` that would be better
off in their own crate such that crates can share.

The equivalent in `monerod` would be: https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_config.h.

## Where
In a new `constants/` crate.

1 module per area, i.e. `::cryptonote`, `::genesis`, etc.

# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-22T00:23:02+00:00
- Closed at: 2024-10-02T17:52:00+00:00
