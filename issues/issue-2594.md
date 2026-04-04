---
title: 'monerod sync error:'
source_url: https://github.com/monero-project/monero/issues/2594
author: joijuke
assignees: []
labels:
- bug
created_at: '2017-10-07T01:26:31+00:00'
updated_at: '2018-01-27T18:08:26+00:00'
type: issue
status: closed
closed_at: '2018-01-27T18:08:26+00:00'
---

# Original Description
os: Ubuntu 16.04.1 x86_64 x86_64 GNU/Linux
version:  monero-linux-x64-v0.11.0.0 

error:

2017-10-06 11:04:07.820 [P2P8]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:578  [batch] DB resize needed
2017-10-06 11:04:07.897 [P2P8]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 47104MiB, New: 48128MiB
2017-10-06 11:08:41.495 [P2P5]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:578  [batch] DB resize needed
2017-10-06 11:08:41.519 [P2P5]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 48128MiB, New: 49152MiB
2017-10-06 11:10:25.187 [P2P9]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 12 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 11:59:56.122 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-06 12:43:29.610 [P2P1]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 44 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 12:43:45.995 [P2P4]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 4 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 12:59:58.181 [P2P8]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-06 13:23:27.383 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    SYNCHRONIZED OK
2017-10-06 13:49:23.814 [P2P3]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:24.849 [P2P9]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:25.922 [P2P7]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:26.995 [P2P0]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:28.062 [P2P9]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:29.132 [P2P2]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:30.202 [P2P3]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:31.272 [P2P0]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8
2017-10-06 13:49:31.942 [P2P0]  ERROR   daemon  contrib/epee/include/serialization/keyvalue_serialization_overloads.h:152       size in blob 36 not have not zero modulo for sizeof(value_type) = 8


# Discussion History
## moneromooo-monero | 2017-10-07T07:53:51+00:00
If you can repeat that, can you run with --log-level 1,\*p2p\*:DEBUG please ? It should give more info. If it's still running and continues printing this, "set_log 1,\*p2p\*:DEBUG" while it is running also works.

## joijuke | 2017-10-08T01:13:53+00:00
sorry, the error can'e be repeated.
when the error happened, i executed monerod with option: --fluffy-blocks --fast-block-sync=1

## palexande | 2017-12-12T20:25:58+00:00
Getting this same type of error on my node. Initiated set_log 1,*p2p*:DEBUG.  @moneromooo-monero do you want a link to the log? I'm also using --fluffy-blocks

update:  Going to have to wait until I get the error again.

## moneromooo-monero | 2017-12-13T09:42:43+00:00
Yes, please.

## leonklingele | 2018-01-02T22:22:51+00:00
@palexande happened to me twice today, please check if you were affected as well :)
I'm now tracking this with debug mode enabled on my instances too.

## moneromooo-monero | 2018-01-03T14:08:05+00:00
If you're seeing this, please rebuild with this patch:
```
diff --git a/contrib/epee/include/serialization/keyvalue_serialization_overloads.h b/contrib/epee/include/serialization/keyvalue_serializati
on_overloads.h
index 7087136..11a234f 100644
--- a/contrib/epee/include/serialization/keyvalue_serialization_overloads.h
+++ b/contrib/epee/include/serialization/keyvalue_serialization_overloads.h
@@ -154,6 +154,9 @@ namespace epee
       {
         size_t loaded_size = buff.size();
         typename stl_container::value_type* pelem =  (typename stl_container::value_type*)buff.data();
+        if (loaded_size%sizeof(typename stl_container::value_type))
+           try {throw "Wheee";} catch(...){}
+
         CHECK_AND_ASSERT_MES(!(loaded_size%sizeof(typename stl_container::value_type)), 
           false, 
           "size in blob " << loaded_size << " not have not zero modulo for sizeof(value_type) = " << sizeof(typename stl_container::value_t
ype));
```

This will dump a stack trace when it happens, showing what's calling it.


## leonklingele | 2018-01-03T15:10:23+00:00
Will keep you updated @moneromooo-monero 

## dEBRUYNE-1 | 2018-01-08T12:31:09+00:00
+bug

## leonklingele | 2018-01-10T23:32:26+00:00
@moneromooo-monero yay, it crashed again 🎉 
Stacktrace here: https://gist.github.com/leonklingele/2d55550da29b22816ae7e524c92e3377

## moneromooo-monero | 2018-01-11T17:36:33+00:00
Thanks, that was very helpful. I think it's now fixed in https://github.com/monero-project/monero/pull/3105

## moneromooo-monero | 2018-01-27T18:02:08+00:00
+resolved

# Action History
- Created by: joijuke | 2017-10-07T01:26:31+00:00
- Closed at: 2018-01-27T18:08:26+00:00
