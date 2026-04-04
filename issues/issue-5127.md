---
title: Add output_indices to get_blocks_by_height.bin
source_url: https://github.com/monero-project/monero/issues/5127
author: woodser
assignees: []
labels: []
created_at: '2019-02-04T21:31:46+00:00'
updated_at: '2019-02-04T21:33:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue proposes adding `output_indices` to daemon rpc's `get_blocks_by_height.bin`.  Doing so would make this call consistent with `get_blocks.bin`.  Otherwise the client must use `get_blocks.bin` which may not serve their use case or make one RPC call to `get_o_indexes.bin` per transaction which does not scale.

# Discussion History
# Action History
- Created by: woodser | 2019-02-04T21:31:46+00:00
