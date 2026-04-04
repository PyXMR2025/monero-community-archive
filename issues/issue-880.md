---
title: blockchain_import crash
source_url: https://github.com/monero-project/monero/issues/880
author: raedah
assignees: []
labels: []
created_at: '2016-06-23T00:29:34+00:00'
updated_at: '2017-09-25T19:12:22+00:00'
type: issue
status: closed
closed_at: '2017-09-25T19:12:22+00:00'
---

# Original Description
./blockchain_import  crash

...

[- batch commit at height 1005000 -]

2016-Jun-22 15:30:23.782518 loading block number 1006000
2016-Jun-22 15:30:47.942209 loading block number 1007000
2016-Jun-22 15:31:11.137136 loading block number 1008000
2016-Jun-22 15:31:39.319855 loading block number 1009000
2016-Jun-22 15:32:05.168360 loading block number 1010000

[- batch commit at height 1010000 -]

2016-Jun-22 15:32:49.778107 loading block number 1011000
2016-Jun-22 15:33:27.197471 loading block number 1012000
2016-Jun-22 15:34:10.006569 loading block number 1013000
2016-Jun-22 15:34:43.400935 loading block number 1014000
block 1014250 / 10720722016-Jun-22 15:34:52.868683 ERROR /DISTRIBUTION-BUILD/src/cryptonote_core/blockchain.cpp:2757 Error adding block with hash: <faf14ddeef5a04d563615748da9555fe1a5506969bb6eae6ba7af04096695b3a> to blockchain, what = Error adding spent key image to db transaction: MDB_MAP_FULL: Environment mapsize limit reached
2016-Jun-22 15:34:52.869458 Error attempting to retrieve a block hash from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Jun-22 15:34:52.870326 exception while reading from file, height=1014252: Error attempting to retrieve a block hash from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Jun-22 15:34:52.871395 Failed to query m_blocks
terminate called after throwing an instance of 'cryptonote::DB_ERROR'
  what():  Failed to query m_blocks
Aborted (core dumped)

resumed without issue on reattempt.


# Discussion History
## radfish | 2016-07-12T04:36:45+00:00
IIRC, I got MDB_MAP_FULL error when my disk filled up -- out of space.


## radfish | 2016-08-28T11:50:11+00:00
Since others are hitting this issue, could you please change title to:
bitmonerod: MDB_MAP_FULL: Environment mapsize limit reached


## moneromooo-monero | 2017-09-20T21:16:29+00:00
Should be fixed by https://github.com/monero-project/monero/pull/2457

## moneromooo-monero | 2017-09-25T18:48:35+00:00
+resolved

# Action History
- Created by: raedah | 2016-06-23T00:29:34+00:00
- Closed at: 2017-09-25T19:12:22+00:00
