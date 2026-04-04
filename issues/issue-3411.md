---
title: Settings > Info doesn't inform whether blockchain is full or pruned
source_url: https://github.com/monero-project/monero-gui/issues/3411
author: rating89us
assignees: []
labels: []
created_at: '2021-04-18T15:52:26+00:00'
updated_at: '2021-04-24T05:43:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If the wallet is set to local node, it should inform about the blockchain (full vs. pruned)

# Discussion History
## selsta | 2021-04-24T05:43:57+00:00
This will not be easy to add. Checking for pruning status requires a RPC call so it isn't something that is instantly visible.

# Action History
- Created by: rating89us | 2021-04-18T15:52:26+00:00
