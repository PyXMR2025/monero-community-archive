---
title: sync failure on rpi2 running ubuntu 14.04.4
source_url: https://github.com/monero-project/monero/issues/708
author: iamsmooth
assignees: []
labels: []
created_at: '2016-03-08T01:40:35+00:00'
updated_at: '2016-10-06T05:12:39+00:00'
type: issue
status: closed
closed_at: '2016-10-06T05:12:39+00:00'
---

# Original Description
Using --db-type lmdb 

commit a7310031f4b232af1e059088afc017bfaa1835b7 (pulled from master several days ago)

2016-Mar-07 06:02:14.210060 [P2P1][X.X.X.X:18080 OUT]Synced 543551/986276
2016-Mar-07 06:02:28.936539 [P2P1][X.X.X.X:18080 OUT]Synced 543751/986276
2016-Mar-07 06:02:43.988333 [P2P1][X.X.X.X:18080 OUT]Synced 543951/986276
2016-Mar-07 06:03:47.638078 [P2P1][X.X.X.X:18080 OUT]Synced 544151/986276
2016-Mar-07 06:03:49.317887 [P2P8]Failed to add output pubkey to db transaction
2016-Mar-07 06:03:49.467195 [P2P8]ERROR /home/ubuntu/bitmonero-0.9/src/cryptonote_core/blockchain.cpp:2716 Error adding block with hash: <b6a855618084e4dda2b8bb208d4c09f8203ca6aa62dd26ee40575bcd936416c4> to blockchain, what = Failed to add output pubkey to db transaction
2016-Mar-07 06:03:49.475352 [P2P8]DB error attempting to fetch block index from hash
2016-Mar-07 06:03:49.477070 [P2P8]ERROR /home/ubuntu/bitmonero-0.9/contrib/epee/include/net/abstract_tcp_server2.inl:342 Exception at [connection<t_protocol_handler>::handle_read], what=DB error attempting to fetch block index from hash
2016-Mar-07 06:03:51.120850 [P2P8]Error attempting to retrieve a block hash from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid


# Discussion History
## iamsmooth | 2016-03-08T06:14:14+00:00
After restart it continued syncing. Not sure if this is good or bad.


## moneromooo-monero | 2016-04-03T11:59:24+00:00
The original "Failed to add output pubkey to db transaction" error case now print out the lmdb API return code, so if you get this again, paste the message again.


## iamsmooth | 2016-04-05T17:07:23+00:00
OK. hyc mentioned changing the 32 bit format, so I was planning to redo the whole sync and see what happens.


## ghost | 2016-09-15T14:58:59+00:00
Hi @iamsmooth, is this issue still present or can it be closed?


## iamsmooth | 2016-10-06T05:12:39+00:00
I haven't tried this in a long time, so it may well be obsolete. Closing, can reopen if the problem reappears.


# Action History
- Created by: iamsmooth | 2016-03-08T01:40:35+00:00
- Closed at: 2016-10-06T05:12:39+00:00
