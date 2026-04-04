---
title: Blockchain import utility fails due to chunk_size inconsistency
source_url: https://github.com/monero-project/monero/issues/9961
author: mivuzu
assignees: []
labels:
- question
created_at: '2025-06-16T22:29:43+00:00'
updated_at: '2025-09-09T04:48:28+00:00'
type: issue
status: closed
closed_at: '2025-09-09T04:48:28+00:00'
---

# Original Description
Hi,
After downloading the blockchain and trying to import it with `monero-blockchain-import` I'm getting an error, something about chunk size and buffer size inconsistencies. Here's the log.
```
2025-06-16 21:43:00.000 W WARNING: chunk_size 334246481 > BUFFER_SIZE 2097152  height: 3, offset 64753
2025-06-16 21:43:00.096 E Exception at [Import error], what=Aborting: chunk size exceeds buffer size
```
I first suspected this was a version related issue since I was using the archlinux package, so I downloaded the latest binaries directly from getmonero.org and I still got the same error.

I downloaded the blockchain from [https://downloads.getmonero.org/blockchain.raw]( https://downloads.getmonero.org/blockchain.raw) and I have no way of verifying if the file was corrupted midtransit since there's no hash for it, no that I could find anyway. Running curl with continue flags and checking the file size suggest that it's at least complete.
Looked up this error and found people saying that it would work with `--dangerous-unverified-import=1` or `--verify=0`, neither worked.

# Discussion History
## selsta | 2025-06-16T23:26:54+00:00
Where did you find the link to the blockchain.raw? We removed it from the website as it's not recommended anymore.

## mivuzu | 2025-06-17T05:54:33+00:00
> Where did you find the link to the blockchain.raw? We removed it from the website as it's not recommended anymore.

tbh I found out about it by asking an AI about faster ways to get a local node.
I also saw it on some tutorial about `monero-blockchain-import` afterwards, I'll send the link in a sec [(here)](https://www.monero.how/tutorial-how-to-speed-up-initial-blockchain-sync)

## selsta | 2025-06-18T12:16:19+00:00
This file is not maintained anymore and I don't know of its integrity. I would recommend to sync up using `monerod`.

## mivuzu | 2025-09-09T04:48:28+00:00
fair enough

# Action History
- Created by: mivuzu | 2025-06-16T22:29:43+00:00
- Closed at: 2025-09-09T04:48:28+00:00
