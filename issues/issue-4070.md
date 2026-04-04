---
title: Compilation errors on Arch gcc 8.1.1
source_url: https://github.com/monero-project/monero/issues/4070
author: moneroexamples
assignees: []
labels: []
created_at: '2018-06-28T01:45:41+00:00'
updated_at: '2018-06-28T02:05:29+00:00'
type: issue
status: closed
closed_at: '2018-06-28T02:05:29+00:00'
---

# Original Description
```
/home/mwo/monero/src/common/util.cpp:241:60: error: ‘strerr’ is not a member of ‘std’
       MERROR("Failed to open " << filename << ": " << std::strerr(errno));
```

Did you mean std:strerror?

and 

```
/home/mwo/monero/src/common/util.cpp:229:17: error: cannot convert ‘const string’ {aka ‘const std::__cxx11::basic_string<char>’} to ‘const char*’
     m_fd = open(filename, O_RDONLY | O_CREAT, 0666);
```

I think it should be filename.c_str()?



# Discussion History
## moneroexamples | 2018-06-28T01:57:03+00:00
I patched it, and at least it compiles now:

```diff
diff --git a/src/common/util.cpp b/src/common/util.cpp
index eed6fd8d..7d9d7b40 100644
--- a/src/common/util.cpp
+++ b/src/common/util.cpp
@@ -226,19 +226,19 @@ namespace tools
       MERROR("Failed to open " << filename << ": " << std::error_code(GetLastError(), std::system_category()));
     }
 #else
-    m_fd = open(filename, O_RDONLY | O_CREAT, 0666);
+    m_fd = open(filename.c_str(), O_RDONLY | O_CREAT, 0666);
     if (m_fd != -1)
     {
       if (flock(m_fd, LOCK_EX | LOCK_NB) == -1)
       {
-        MERROR("Failed to lock " << filename << ": " << std::strerr(errno));
+        MERROR("Failed to lock " << filename << ": " << std::strerror(errno));
         close(m_fd);
         m_fd = -1;
       }
     }
     else
     {
-      MERROR("Failed to open " << filename << ": " << std::strerr(errno));
+      MERROR("Failed to open " << filename << ": " << std::strerror(errno));
     }
 #endif
   }
```

## anonimal | 2018-06-28T02:00:51+00:00
This was already fixed in https://github.com/monero-project/monero/pull/4069/files.

## moneroexamples | 2018-06-28T02:05:29+00:00
Thanks.

# Action History
- Created by: moneroexamples | 2018-06-28T01:45:41+00:00
- Closed at: 2018-06-28T02:05:29+00:00
