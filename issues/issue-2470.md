---
title: 'Transactions page: sort by Blockheight and Date are redundant'
source_url: https://github.com/monero-project/monero-gui/issues/2470
author: rating89us
assignees: []
labels: []
created_at: '2019-11-23T23:12:45+00:00'
updated_at: '2019-11-24T08:47:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/45968869/69486705-e0348e00-0e4e-11ea-8a2e-477f7cc29613.png)

Sort by Blockheight and sort by Date have the same function. I suggest keeping only sort by Date.

# Discussion History
## dEBRUYNE-1 | 2019-11-24T08:47:29+00:00
Technically there can be differences as the time stamp of the block is set by the miner's local clock. Thus, differences can arise if the local clock is off (e.g. a block with a higher height, but an earlier date). In general, however, I kind of agree it is redundant. 

# Action History
- Created by: rating89us | 2019-11-23T23:12:45+00:00
