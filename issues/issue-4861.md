---
title: Run node on SSD and store blockchain on HDD?
source_url: https://github.com/monero-project/monero/issues/4861
author: nox956
assignees: []
labels: []
created_at: '2018-11-16T14:53:13+00:00'
updated_at: '2018-11-17T03:29:00+00:00'
type: issue
status: closed
closed_at: '2018-11-17T03:29:00+00:00'
---

# Original Description
If I run my monero node on SSD and use `--data-dir path/of/HDD` to store blockchain data on HDD, will it still increase the efficiency of syncing with network? 

Because I really don't have that much space for entire blockchain data on SSD, it will be great if I can store these huge file on my hard disk even with less efficiency than running the whole thing on SSD.

Thanks!

# Discussion History
## nioroso-x3 | 2018-11-16T16:10:09+00:00
I just let it sync using a SSD, then copy the synced folder back to HDD. Faster than syncing on the HDD from zero.

## nox956 | 2018-11-16T16:14:22+00:00
My node is actually synced, but when a new block is mined on the monero network, read/write files will cause high iowait, and that is my major concern.

## moneromooo-monero | 2018-11-16T19:28:46+00:00
What do you call "If I run my monero node on SSD" then ? Have the monerod binary on a SSD ? If so, it won't change a thing after startup.

## nox956 | 2018-11-17T03:29:00+00:00
@moneromooo-monero Got it, thanks!

# Action History
- Created by: nox956 | 2018-11-16T14:53:13+00:00
- Closed at: 2018-11-17T03:29:00+00:00
