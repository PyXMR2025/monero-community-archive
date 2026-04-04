---
title: '`get_fee_estimate` RPC should take in the block to get the estimate from'
source_url: https://github.com/monero-project/monero/issues/8906
author: kayabaNerve
assignees: []
labels:
- pending review
- proposal
created_at: '2023-06-14T01:20:46+00:00'
updated_at: '2023-12-07T21:11:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`get_dynamic_base_fee_estimate_2021_scaling` (and other called functions) grabs the local height/globally cached variables. This breaks distributed systems requiring consistency, as each Monero node may have a temporary delay/slightly distinct view of the network, forcing them to write their own algorithms. If the block hash to base off of was an optional argument, Monero's estimation could be used with guaranteed consistency.

# Discussion History
# Action History
- Created by: kayabaNerve | 2023-06-14T01:20:46+00:00
