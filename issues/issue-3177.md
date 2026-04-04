---
title: Monero wallet rescan blockchain
source_url: https://github.com/monero-project/monero/issues/3177
author: Revinand
assignees: []
labels:
- invalid
created_at: '2018-01-24T11:38:28+00:00'
updated_at: '2018-01-24T13:40:33+00:00'
type: issue
status: closed
closed_at: '2018-01-24T13:39:11+00:00'
---

# Original Description
How often `rescan_blockchain` method should be called? Suppose I process payments in a cronjob, which runs every 10 minutes. Do I need to rescan blockchain each call?

# Discussion History
## Revinand | 2018-01-24T12:45:13+00:00
Hm, just noticed: wallet receives new transactions and blocks automatically, which means `rescan_blockchain` should be called only in case when wallet was offline for a long period, am I right? IIRC wallet didn't update automatically before

## stoffu | 2018-01-24T13:22:25+00:00
As evident in the code

https://github.com/monero-project/monero/blob/5f09d6c8333b0b0d07252dc157b9e794f6278662/src/wallet/wallet2.cpp#L3944

`rescan_bc` has the same effect as deleting your wallet cache file (the file without any file extension like .keys or .address.txt) and opening the .keys file again to recreate the cache file from scratch. The wallet cache file stores some private data that exist only locally (i.e. not on the blockchain), such as the tx secret keys, the recipient addresses, the address book, etc. Usually you don't want/need to use `rescan_bc`; I guess it exists mainly for debugging/testing purposes.

## hyc | 2018-01-24T13:38:03+00:00
+invalid

The issue tracker is for actual bug reports, not for questions and answers.

## Revinand | 2018-01-24T13:39:11+00:00
@hyc sorry for that.
@stoffu thanks for the clarification

# Action History
- Created by: Revinand | 2018-01-24T11:38:28+00:00
- Closed at: 2018-01-24T13:39:11+00:00
