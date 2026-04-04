---
title: print_bc fails with the latest block
source_url: https://github.com/monero-project/monero/issues/3570
author: binaryFate
assignees: []
labels: []
created_at: '2018-04-06T15:23:47+00:00'
updated_at: '2018-04-06T20:26:42+00:00'
type: issue
status: closed
closed_at: '2018-04-06T20:26:42+00:00'
---

# Original Description
`print_bc <whatever> <latest_block_in_chain>` fails with "Unsuccessful --".

Error message when blocks are out of range could be improved too while we're at it, something like "block not available"

# Discussion History
## binaryFate | 2018-04-06T15:25:38+00:00
Mmm i'm not sure anymore, print_block does the same thing, might be I just get confused with what is the last block

## moneromooo-monero | 2018-04-06T17:23:29+00:00
Works for me. On a height N chain, the last block is N-1 (and the first is 0).

## binaryFate | 2018-04-06T20:26:28+00:00
Ah yes, makes sense, closing

# Action History
- Created by: binaryFate | 2018-04-06T15:23:47+00:00
- Closed at: 2018-04-06T20:26:42+00:00
