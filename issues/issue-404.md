---
title: Stuck on re-orgs
source_url: https://github.com/Cuprate/cuprate/issues/404
author: Boog900
assignees: []
labels:
- C-bug
created_at: '2025-03-12T16:56:48+00:00'
updated_at: '2025-03-21T17:52:12+00:00'
type: issue
status: closed
closed_at: '2025-03-21T17:52:11+00:00'
---

# Original Description
## Bug
Cuprate struggles to handle alt-blocks

## Log

```
2025-03-12T16:25:05.763628Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:25:05.783531Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:25:34.725632Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:25:43.922410Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:25:43.923871Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:26:01.172687Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:26:01.829728Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:26:01.830084Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:26:31.160953Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:26:32.338206Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:26:32.339295Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:27:01.128378Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:27:01.445344Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:27:01.446267Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:27:31.365338Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:27:32.015854Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:27:32.017144Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:28:01.230414Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:28:02.156343Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:28:02.157181Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:28:32.218018Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:28:32.706109Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:28:32.706931Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:29:01.234183Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:29:07.743187Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:29:07.744348Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:29:31.364990Z  INFO block_downloader: Attempting to download blocks from peers, this may take a while.
2025-03-12T16:29:31.867630Z  INFO incoming_block_batch{start_height=3366243 len=1}: Successfully added block batch alt_chain=true
2025-03-12T16:29:31.868741Z  INFO incoming_block_batch{start_height=3366244 len=1}: Successfully added block batch alt_chain=true
```

Here Cuprate is repeatedly downloading an alt chain (it is not adding it to the DB multiple times).




# Discussion History
## Boog900 | 2025-03-13T14:55:09+00:00
This issue can be resolved on a restart for anyone that has it.

# Action History
- Created by: Boog900 | 2025-03-12T16:56:48+00:00
- Closed at: 2025-03-21T17:52:11+00:00
