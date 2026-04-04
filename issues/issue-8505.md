---
title: Output export string too large for node max string length
source_url: https://github.com/monero-project/monero/issues/8505
author: mrtestyboy781
assignees: []
labels: []
created_at: '2022-08-15T19:27:45+00:00'
updated_at: '2022-08-15T19:27:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For extremely large wallets the output of `export_outputs` with all=true set, the hex blob is longer than the maximum string length allowed in node, making the payload difficult to deal withoutside of `curl`

If there were a way to make output export json chunked like key image export, it would be easier to handle and pass around paginated. 

# Discussion History
# Action History
- Created by: mrtestyboy781 | 2022-08-15T19:27:45+00:00
