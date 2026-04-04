---
title: Mingw64 build warning
source_url: https://github.com/monero-project/monero/issues/3572
author: Keksov
assignees: []
labels: []
created_at: '2018-04-06T18:09:19+00:00'
updated_at: '2022-03-16T15:33:45+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:33:45+00:00'
---

# Original Description
Probably not a problem, but better to report...
```
C:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:15:2: warning: #warning Please include winsock2.h before windows.h [-Wcpp]
 #warning Please include winsock2.h before windows.h
```


# Discussion History
## moneromooo-monero | 2018-04-07T09:01:10+00:00
Does it print out the stack of includes ? It'd be helpful to know where it's included from.

## Keksov | 2018-04-07T09:06:37+00:00
```
In file included from C:/msys64/usr/src/monero/external/easylogging++/easylogging++.h:375:0,
                 from C:/msys64/usr/src/monero/contrib/epee/include/misc_log_ex.h:33,
                 from C:/msys64/usr/src/monero/src/ringct/bulletproofs.cc:34:
C:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:15:2: warning: #warning Please include winsock2.h before windows.h [-Wcpp]
 #warning Please include winsock2.h before windows.h
  ^~~~~~~
make[3]: Leaving directory '/usr/src/monero/build/debug'

```

## Keksov | 2018-04-07T09:08:18+00:00
And a bit more warnings...
```
[ 91%] Building CXX object src/daemon/CMakeFiles/daemon.dir/daemon.cpp.obj
In file included from C:/msys64/usr/src/monero/src/daemonizer/daemonizer.h:63:0,
                 from C:/msys64/usr/src/monero/src/daemon/command_line_args.h:34,
                 from C:/msys64/usr/src/monero/src/daemon/daemon.cpp:47:
C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl: At global scope:
C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl:64:0: warning: 'std::__cxx11::string daemonizer::{anonymous}::get_argument_string(int, const char**)' defined but not used [-Wunused-function]
     std::string get_argument_string(int argc, char const * argv[])

In file included from C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl:33:0,
                 from C:/msys64/usr/src/monero/src/daemonizer/daemonizer.h:63,
                 from C:/msys64/usr/src/monero/src/daemon/command_line_args.h:34,
                 from C:/msys64/usr/src/monero/src/daemon/daemon.cpp:47:
C:/msys64/usr/src/monero/src/daemonizer/windows_service_runner.h:45:23: warning: 'std::vector<char> windows::{anonymous}::vecstring(const string&)' defined but not used [-Wunused-function]
     std::vector<char> vecstring(std::string const & str)
                       ^~~~~~~~~
[ 92%] Building CXX object src/daemon/CMakeFiles/daemon.dir/executor.cpp.obj
[ 92%] Building CXX object src/daemon/CMakeFiles/daemon.dir/main.cpp.obj
In file included from C:/msys64/usr/src/monero/src/daemonizer/daemonizer.h:63:0,
                 from C:/msys64/usr/src/monero/src/daemon/main.cpp:40:
C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
C:/msys64/usr/src/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

```

## moneromooo-monero | 2018-08-15T11:33:02+00:00
Does this patch fix it ? 

```
diff --git a/src/ringct/bulletproofs.cc b/src/ringct/bulletproofs.cc
index ed79dc3..97d1b9a 100644
--- a/src/ringct/bulletproofs.cc
+++ b/src/ringct/bulletproofs.cc
@@ -29,7 +29,6 @@
 // Adapted from Java code by Sarang Noether
 
 #include <stdlib.h>
-#include <openssl/ssl.h>
 #include <boost/thread/mutex.hpp>
 #include "misc_log_ex.h"
 #include "common/perf_timer.h"
@@ -42,6 +41,8 @@ extern "C"
 #include "multiexp.h"
 #include "bulletproofs.h"
 
+#include <openssl/ssl.h>
+
 #undef MONERO_DEFAULT_LOG_CATEGORY
 #define MONERO_DEFAULT_LOG_CATEGORY "bulletproofs"
 

```

# Action History
- Created by: Keksov | 2018-04-06T18:09:19+00:00
- Closed at: 2022-03-16T15:33:45+00:00
