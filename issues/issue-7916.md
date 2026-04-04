---
title: Error on Running daemon first time Failed to parse transaction from blob
source_url: https://github.com/monero-project/monero/issues/7916
author: vick-coder
assignees: []
labels: []
created_at: '2021-09-01T17:23:58+00:00'
updated_at: '2021-09-01T17:29:05+00:00'
type: issue
status: closed
closed_at: '2021-09-01T17:29:05+00:00'
---

# Original Description
I'm trying to generate a genesis block on the latest monero fork. Build successfully but when try to run a daemon for the first time getting these errors. I have removed the monero genesis block & set it to empty also PER_BLOCK_CHECKPOINT is set to 0.

```
Failed to parse transaction from blob

coinbase transaction in the block has no inputs
Block with id: <0dcf38c90b4a59290e72accc2e95a11b5d092d7857013fe7fc8ec78ad6ce5b0a> failed to pass prevalidation
Failed to add genesis block to blockchain
Failed to initialize blockchain storage
```

# Discussion History
## selsta | 2021-09-01T17:29:05+00:00
I would suggest you to look on the monero stackexchange, it has a tutorial on how to generate a genesis block. Alternatively ask other monero forks for help.

This issue tracker isn't the right place for this.

# Action History
- Created by: vick-coder | 2021-09-01T17:23:58+00:00
- Closed at: 2021-09-01T17:29:05+00:00
