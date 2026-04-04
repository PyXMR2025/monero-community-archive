---
title: Breaks with lmdb-0.9.21,1
source_url: https://github.com/monero-project/monero/issues/3125
author: yurivict
assignees: []
labels:
- invalid
created_at: '2018-01-15T04:24:47+00:00'
updated_at: '2018-01-15T05:48:27+00:00'
type: issue
status: closed
closed_at: '2018-01-15T05:48:27+00:00'
---

# Original Description
```
/usr/ports/net-p2p/libmonero/work/monero-0.11.1.0/src/blockchain_db/lmdb/db_lmdb.cpp:876:7: error: unknown type name 'mdb_size_t'
      mdb_size_t num_elems = 0;
      ^
/usr/ports/net-p2p/libmonero/work/monero-0.11.1.0/src/blockchain_db/lmdb/db_lmdb.cpp:1135:18: error: use of undeclared identifier 'MDB_PREVSNAPSHOT'
    mdb_flags |= MDB_PREVSNAPSHOT;
                 ^
/usr/ports/net-p2p/libmonero/work/monero-0.11.1.0/src/blockchain_db/lmdb/db_lmdb.cpp:2188:3: error: unknown type name 'mdb_size_t'
  mdb_size_t num_elems = 0;
  ^
/usr/ports/net-p2p/libmonero/work/monero-0.11.1.0/src/blockchain_db/lmdb/db_lmdb.cpp:3014:7: error: unknown type name 'mdb_size_t'
      mdb_size_t num_elems = 0;
      ^
/usr/ports/net-p2p/libmonero/work/monero-0.11.1.0/src/blockchain_db/lmdb/db_lmdb.cpp:3032:9: error: unknown type name 'mdb_size_t'
        mdb_size_t num_elems = 0;
        ^
```

# Discussion History
## hyc | 2018-01-15T05:41:10+00:00
Monero requires the bundled LMDB source.

+invalid

# Action History
- Created by: yurivict | 2018-01-15T04:24:47+00:00
- Closed at: 2018-01-15T05:48:27+00:00
