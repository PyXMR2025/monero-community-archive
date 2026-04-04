---
title: still lookin for berkely db in unit test
source_url: https://github.com/monero-project/monero/issues/370
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-08-14T02:58:18+00:00'
updated_at: '2015-08-27T16:09:43+00:00'
type: issue
status: closed
closed_at: '2015-08-27T16:09:43+00:00'
---

# Original Description
[ 83%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/base58.cpp.o
[ 83%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/blockchain_db.cpp.o
In file included from /home/gbone/bitmonero/tests/unit_tests/blockchain_db.cpp:40:0:
/home/gbone/bitmonero/src/blockchain_db/berkeleydb/db_bdb.h:28:20: fatal error: db_cxx.h: No such file or directory
 #include <db_cxx.h>
                    ^
compilation terminated.
make[3]: **\* [tests/unit_tests/CMakeFiles/unit_tests.dir/blockchain_db.cpp.o] Error 1


# Discussion History
## Gingeropolous | 2015-08-27T16:09:41+00:00
was able to compile recently. My bad. 


# Action History
- Created by: Gingeropolous | 2015-08-14T02:58:18+00:00
- Closed at: 2015-08-27T16:09:43+00:00
