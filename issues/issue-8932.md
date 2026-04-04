---
title: wallet2 fails to save to disk if first created in-memory
source_url: https://github.com/monero-project/monero/issues/8932
author: woodser
assignees: []
labels: []
created_at: '2023-07-06T12:00:17+00:00'
updated_at: '2023-09-15T03:18:05+00:00'
type: issue
status: closed
closed_at: '2023-09-15T03:18:04+00:00'
---

# Original Description
If wallet2 is first created in-memory (i.e. with empty path `""`), then it will fail to save to disk, due to incorrect assumptions that the other files have already been created, based on this comment and the following logic: https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6238

This issue requests fixing wallet2 to correctly save to disk after being created in-memory with empty path.

# Discussion History
## jeffro256 | 2023-07-06T20:21:13+00:00
Which interface are you invoking to attempt to get it to save to the disk? Are you calling `store_to()` directly? Not necessarily super important, but just curious. Also, I can fix this v soon, thanks for finding that

## woodser | 2023-07-06T20:33:59+00:00
Yeah I'm calling `store_to` directly, to support moving the wallet files [here](https://github.com/monero-ecosystem/monero-cpp/blob/a60c2752bb7f405a1d2e4c405ebfa57dc8efcd96/src/wallet/monero_wallet_full.cpp#L3449).

## jeffro256 | 2023-07-07T16:52:49+00:00
lmao just found another issue with `store_to` which was driving me utterly insane while unit testing a fix: if the new file path contains the old file path, it thinks its the same file and just deletes the cache. 

## jeffro256 | 2023-07-07T16:53:48+00:00
Because I was trying to move a wallet file from `name` to `name_new` and the keys file showed up in the right place but my cache file kept disappearing

## jeffro256 | 2023-07-07T17:13:47+00:00
AND it doesn't save cache on when the file is different anyways??

# Action History
- Created by: woodser | 2023-07-06T12:00:17+00:00
- Closed at: 2023-09-15T03:18:04+00:00
