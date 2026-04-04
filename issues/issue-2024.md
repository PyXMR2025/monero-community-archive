---
title: Memory alloc error
source_url: https://github.com/monero-project/monero/issues/2024
author: ElLamparto
assignees: []
labels: []
created_at: '2017-05-10T07:25:33+00:00'
updated_at: '2017-05-15T12:05:26+00:00'
type: issue
status: closed
closed_at: '2017-05-15T12:05:25+00:00'
---

# Original Description
2017-05-10 00:06:36.732	[P2P1]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	DB error attempting to fetch tx from hashCannot allocate memory

By the way, at every restart I get a log entry like:
2017-05-10 06:38:34.418	        b74fe700	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:571	[batch] DB resize needed 2017-05-10 06:38:34.418	        b74fe700	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:487	LMDB Mapsize increased.  Old: 24590MiB, New: 25614MiB

I don't know if it is normal...

monerod  0.10.3.1, Debian 8 32bit.

# Discussion History
## moneromooo-monero | 2017-05-13T10:14:10+00:00
Do you have any swap ? If not, add some. If yes, increase it.


## ElLamparto | 2017-05-15T12:05:25+00:00
There should not be a problem, neither with the memory nor with the swap. Since it happened once only, I close the ticket.

# Action History
- Created by: ElLamparto | 2017-05-10T07:25:33+00:00
- Closed at: 2017-05-15T12:05:25+00:00
