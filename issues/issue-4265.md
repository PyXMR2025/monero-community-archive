---
title: ' Arch gcc 8.2: fatal error: ustat.h: No such file or directory  #include <ustat.h>'
source_url: https://github.com/monero-project/monero/issues/4265
author: moneroexamples
assignees: []
labels: []
created_at: '2018-08-16T00:07:18+00:00'
updated_at: '2018-08-23T05:01:27+00:00'
type: issue
status: closed
closed_at: '2018-08-23T05:01:27+00:00'
---

# Original Description
```
/home/mwo/monero/src/common/util.cpp:41:10: fatal error: ustat.h: No such file or directory
 #include <ustat.h>
```
From what I found `ustat.h` has been deprecated in glibc and finally got removed in Arch. 

Found this https://github.com/zatrazz/glibc/blob/master/NEWS

> The obsolete function ustat is no longer available to newly linked
  binaries; the headers <ustat.h> and <sys/ustat.h> have been removed.  This
  function has been deprecated in favor of fstatfs and statfs.



# Discussion History
## moneroexamples | 2018-08-16T01:40:31+00:00
I removed the `ustat.h` and also fixed a problem with `generate_chacha_key` and now it all compiles. This is the patch:

```diff
diff --git a/src/common/util.cpp b/src/common/util.cpp
index 5e0d2726..25312bdd 100644
--- a/src/common/util.cpp
+++ b/src/common/util.cpp
@@ -38,7 +38,6 @@
 #include <sys/types.h>
 #include <sys/stat.h>
 #include <sys/resource.h>
-#include <ustat.h>
 #include <unistd.h>
 #include <dirent.h>
 #include <string.h>
diff --git a/tests/unit_tests/ringdb.cpp b/tests/unit_tests/ringdb.cpp
index 8b0ea10d..9b842569 100644
--- a/tests/unit_tests/ringdb.cpp
+++ b/tests/unit_tests/ringdb.cpp
@@ -47,7 +47,7 @@ static crypto::chacha_key generate_chacha_key()
 {
   crypto::chacha_key chacha_key;
   uint64_t password = crypto::rand<uint64_t>();
-  crypto::generate_chacha_key(std::string((const char*)&password, sizeof(password)), chacha_key);
+  crypto::generate_chacha_key(std::string((const char*)&password, sizeof(password)), chacha_key, 1);
   return chacha_key;
 }
```



## jtgrassie | 2018-08-18T14:49:33+00:00
https://github.com/monero-project/monero/pull/4274

# Action History
- Created by: moneroexamples | 2018-08-16T00:07:18+00:00
- Closed at: 2018-08-23T05:01:27+00:00
