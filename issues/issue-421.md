---
title: '`cuprated` does not log block batches after initial sync'
source_url: https://github.com/Cuprate/cuprate/issues/421
author: hinto-janai
assignees: []
labels:
- C-bug
- A-binaries
created_at: '2025-03-25T02:34:37+00:00'
updated_at: '2025-05-03T15:57:35+00:00'
type: issue
status: closed
closed_at: '2025-05-03T15:57:35+00:00'
---

# Original Description
## Environment
All, `cuprated v0.0.1`.

## Bug
`cuprated` does not log when a block batch has been added after the initial `Synchronised with the network.` message.

## Expected behavior
All block batches to be logged.

## Steps to reproduce
1. Sync `cuprated` until `Synchronised with the network.` message appears
2. Wait
3. `status`, see height past initial sync height
4. See no sync messages

## Log
```
2025-03-23T06:06:36.414055Z  INFO incoming_block_batch{start_height=3374075 len=3}: Successfully added block batch fast_sync=false
2025-03-23T06:06:36.568945Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-23T06:06:37.073961Z  INFO incoming_block_batch{start_height=3374078 len=1}: Successfully added block batch fast_sync=false
2025-03-23T06:06:37.793049Z  INFO incoming_block_batch{start_height=3374079 len=1}: Successfully added block batch fast_sync=false
2025-03-23T06:06:37.793070Z  INFO Synchronised with the network.
status
STATUS:
  uptime: 22h 17m 27s,
  height: 3375193,
  top_hash: b54b627129b04a541e915b06fe45bdb374020aad4dfac77ac6d9332a86ec2b99
```

# Discussion History
## Boog900 | 2025-03-25T14:59:51+00:00
This is semi-intentional, although I have mentioned in the past making new block notifications `info` level. New blocks are received as notifications old blocks are downloaded in batches. 

Also seems to be a duplicate of #405

# Action History
- Created by: hinto-janai | 2025-03-25T02:34:37+00:00
- Closed at: 2025-05-03T15:57:35+00:00
