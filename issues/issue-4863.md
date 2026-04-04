---
title: Another case/switch fallthrough problem with GCC 7.3
source_url: https://github.com/monero-project/monero/issues/4863
author: ghost
assignees: []
labels: []
created_at: '2018-11-17T13:10:38+00:00'
updated_at: '2018-11-20T22:19:20+00:00'
type: issue
status: closed
closed_at: '2018-11-20T22:19:20+00:00'
---

# Original Description
Previous one in `base58.cpp` was solved

Now compilation halts at `db_lmdb.cpp` because of the same stupid warning

```Scanning dependencies of target obj_blockchain_db
make[3]: Leaving directory '/home/nodey/monero/build/release'
make[3]: Entering directory '/home/nodey/monero/build/release'
[ 60%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 60%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
/home/nodey/monero/src/blockchain_db/lmdb/db_lmdb.cpp: In member function ‘void cryptonote::BlockchainLMDB::migrate(uint32_t)’:
/home/nodey/monero/src/blockchain_db/lmdb/db_lmdb.cpp:4363:16: error: this statement may fall through [-Werror=implicit-fallthrough=]
     migrate_0_1(); /* FALLTHRU */
     ~~~~~~~~~~~^~
/home/nodey/monero/src/blockchain_db/lmdb/db_lmdb.cpp:4364:3: note: here
   case 1:
   ^~~~
/home/nodey/monero/src/blockchain_db/lmdb/db_lmdb.cpp:4365:16: error: this statement may fall through [-Werror=implicit-fallthrough=]
     migrate_1_2(); /* FALLTHRU */
     ~~~~~~~~~~~^~
/home/nodey/monero/src/blockchain_db/lmdb/db_lmdb.cpp:4366:3: note: here
   case 2:
   ^~~~
cc1plus: all warnings being treated as errors
src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/build.make:75: recipe for target 'src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o' failed
make[3]: *** [src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o] Error 1
make[3]: Leaving directory '/home/nodey/monero/build/release'
CMakeFiles/Makefile2:1529: recipe for target 'src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/all' failed
make[2]: *** [src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/all] Error 2
make[2]: Leaving directory '/home/nodey/monero/build/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/nodey/monero/build/release'
Makefile:87: recipe for target 'release' failed
make: *** [release] Error 2
```

@hyc @xiphon any chance you could work similar coding magic here?

# Discussion History
## moneromooo-monero | 2018-11-17T13:16:07+00:00
https://github.com/monero-project/monero/pull/4864

## xiphon | 2018-11-17T14:17:26+00:00
```diff
diff --git a/src/blockchain_db/lmdb/db_lmdb.cpp b/src/blockchain_db/lmdb/db_lmdb.cpp
index ea3638a8..62227878 100644
--- a/src/blockchain_db/lmdb/db_lmdb.cpp
+++ b/src/blockchain_db/lmdb/db_lmdb.cpp
@@ -4358,16 +4358,12 @@ void BlockchainLMDB::migrate_2_3()
 
 void BlockchainLMDB::migrate(const uint32_t oldversion)
 {
-  switch(oldversion) {
-  case 0:
-    migrate_0_1(); /* FALLTHRU */
-  case 1:
-    migrate_1_2(); /* FALLTHRU */
-  case 2:
-    migrate_2_3(); /* FALLTHRU */
-  default:
-    ;
-  }
+  if (oldversion < 1)
+    migrate_0_1();
+  if (oldversion < 2)
+    migrate_1_2();
+  if (oldversion < 3)
+    migrate_2_3();
 }
 
 }  // namespace cryptonote
```

## hyc | 2018-11-17T15:13:56+00:00
That'd be OK, but the entire point of `/* FALLTHRU */` comments is to shut up tool warnings. Whatever compiler is emitting warnings anyway, is broken.

## ghost | 2018-11-17T15:38:11+00:00
Could we put break clauses in each case or would that change the behaviour?

## moneromooo-monero | 2018-11-17T17:25:47+00:00
It would break it (huh huh huh).

## moneromooo-monero | 2018-11-18T23:42:53+00:00
Do you want to PR that xiphon ?

## xiphon | 2018-11-19T22:38:09+00:00
@moneromooo-monero 
will do

## ghost | 2018-11-20T22:19:20+00:00
Thanks. Closing.

# Action History
- Created by: ghost | 2018-11-17T13:10:38+00:00
- Closed at: 2018-11-20T22:19:20+00:00
