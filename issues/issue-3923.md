---
title: monero-blockchain-blackball fails to read forked chains due to DB version mismatch
source_url: https://github.com/monero-project/monero/issues/3923
author: stoffu
assignees: []
labels: []
created_at: '2018-06-04T08:55:38+00:00'
updated_at: '2018-09-14T11:24:54+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:24:54+00:00'
---

# Original Description
The DB version was bumped to v2 since #3251, which makes `monero-blockchain-blackball` fail to read DBs of forked coins in the older DB format.

```
./monero-blockchain-blackball-pr3919 --inputs ~/.bitmonero/lmdb/ ~/temp/monero-v6/lmdb/ --log-level 0,blockchain.db.lmdb:DEBUG

2018-06-04 08:50:29.065   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:222 Starting...
2018-06-04 08:50:29.065   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:248 Initializing source blockchain (BlockchainDB)
2018-06-04 08:50:29.065   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:268 database: lmdb
2018-06-04 08:50:29.065   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:273 Loading blockchain from folder /Users/stoffu/.bitmonero/lmdb ...
2018-06-04 08:50:29.066   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:532  DB map size:     95767597056
2018-06-04 08:50:29.066   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:533  Space used:      56891920384
2018-06-04 08:50:29.066   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:534  Space remaining: 38875676672
2018-06-04 08:50:29.066   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:535  Size threshold:  0
2018-06-04 08:50:29.066   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:537  Percent used: 0.5941  Percent threshold: 0.8000
2018-06-04 08:50:29.066   0x7fffd253d3c0  DEBUG blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:1296 Setting m_height to: 1585477
2018-06-04 08:50:29.120   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:287 Source blockchain storage initialized OK
2018-06-04 08:50:29.120   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:268 database: lmdb
2018-06-04 08:50:29.120   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:273 Loading blockchain from folder /Users/stoffu/temp/monero-v6/lmdb ...
2018-06-04 08:50:29.121   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:532  DB map size:     89267707904
2018-06-04 08:50:29.121   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:533  Space used:      50965635072
2018-06-04 08:50:29.121   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:534  Space remaining: 38302072832
2018-06-04 08:50:29.122   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:535  Size threshold:  0
2018-06-04 08:50:29.122   0x7fffd253d3c0  INFO  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:537  Percent used: 0.5709  Percent threshold: 0.8000
2018-06-04 08:50:29.122   0x7fffd253d3c0  WARN  blockchain.db.lmdb  src/blockchain_db/lmdb/db_lmdb.cpp:74 Failed to open db handle for m_txs_pruned : Permission denied - you may want to start with --db-salvage
2018-06-04 08:50:29.122   0x7fffd253d3c0  WARN  bcutil  src/blockchain_utilities/blockchain_blackball.cpp:281 Error opening database: Failed to open db handle for m_txs_pruned : Permission denied - you may want to start with --db-salvage
```


# Discussion History
## moneromooo-monero | 2018-08-24T13:55:59+00:00
https://github.com/monero-project/monero/pull/4260

## moneromooo-monero | 2018-09-14T11:22:07+00:00
+resolved

# Action History
- Created by: stoffu | 2018-06-04T08:55:38+00:00
- Closed at: 2018-09-14T11:24:54+00:00
