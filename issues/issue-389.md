---
title: Add explicit check to `prevalidate_miner_transaction` that coinbase tx has
  at least one output
source_url: https://github.com/seraphis-migration/monero/issues/389
author: j-berman
assignees: []
labels: []
created_at: '2026-05-15T04:28:23+00:00'
updated_at: '2026-05-15T04:28:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This would guarantee the tree root changes every block (except for the period of time when it was empty), and should therefore all be unique. This would avoid any potential issues where one tx includes a `reference_block = n`, but can also validate with `reference_block = m`.

This should already be implicitly required at consensus because since hf `HF_VERSION_EXACT_COINBASE`, `validate_miner_transaction` requires coinbase outputs to sum to the expected block reward + fees from the block. Thus, consensus should already enforce each block has at least one coinbase out in it. But a simple explicit check would be simpler to intuit.

TODO: make sure all coinbase outputs in the chain have at least one output already. Otherwise we can wait to enforce this until the FCMP++ fork, and require all FCMP++ txs `reference_block >= FCMP++ fork height`.

# Discussion History
# Action History
- Created by: j-berman | 2026-05-15T04:28:23+00:00
