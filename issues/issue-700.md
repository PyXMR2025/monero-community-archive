---
title: Return the correct prunable hash for miner txs
source_url: https://github.com/Cuprate/cuprate/issues/700
author: Boog900
assignees: []
labels:
- C-bug
created_at: '2026-09-02T14:29:55+00:00'
updated_at: '2026-09-14T11:32:27+00:00'
type: issue
status: closed
closed_at: '2026-09-14T11:32:27+00:00'
---

# Original Description
## Bug
We match monerod in returning an incorrect prunable hash for miner V2 txs. See somewhat related: https://github.com/monero-project/monero/issues/11222. monerod will return `keccak256([])`, a hash of no bytes.

## Expected behavior
We should return `[0; 32]`



# Discussion History
# Action History
- Created by: Boog900 | 2026-09-02T14:29:55+00:00
- Closed at: 2026-09-14T11:32:27+00:00
