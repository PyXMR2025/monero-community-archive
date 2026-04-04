---
title: problems with transferring the blockchain to an external drive
source_url: https://github.com/monero-project/monero/issues/4773
author: gittyhupbub
assignees: []
labels:
- invalid
created_at: '2018-11-01T13:29:17+00:00'
updated_at: '2018-11-02T02:34:51+00:00'
type: issue
status: closed
closed_at: '2018-11-01T16:49:14+00:00'
---

# Original Description
im having some issues with the monero wallet. I was installing a wallet on a new cpu and ran out of disk space. I changed the block chain location to an external drive by creating a new directory D:\MoneroBlockchain\lmdb (this is properly shown in the client directory) I copied the data.mbd file to the new folder but when i reopen the client it starts downloading the chain to the pre-existing path. Ive tried clearing the cache as well. Any suggesstions? thanks.

# Discussion History
## moneromooo-monero | 2018-11-01T14:48:40+00:00
Did you add --data-dir D:\MoneroBlockchain ?

## dEBRUYNE-1 | 2018-11-01T16:43:35+00:00
@gittyhupbub - This is basically a bug tracker and not a support forum. Therefore, please see:

https://monero.stackexchange.com/questions/7225/how-do-i-move-the-blockchain-data-mdb-to-a-different-directory-during-or-afte

If you have any further questions, please open a new thread on the monerosupport subreddit:

https://www.reddit.com/r/monerosupport/

## dEBRUYNE-1 | 2018-11-01T16:43:40+00:00
+invalid

## gittyhupbub | 2018-11-02T02:34:51+00:00
Thank you that fixed my issue! However i ran into another problem. ive been stuck in the 89% sync range for 6+ hours doing a consistent small 20 block chunks for a long period of time. My connection is good and it never took this long when i first started syncing to the network. Appreciate your help.

# Action History
- Created by: gittyhupbub | 2018-11-01T13:29:17+00:00
- Closed at: 2018-11-01T16:49:14+00:00
