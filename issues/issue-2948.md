---
title: '[Build] Windows include files ordering'
source_url: https://github.com/monero-project/monero/issues/2948
author: danrmiller
assignees: []
labels: []
created_at: '2017-12-17T17:03:57+00:00'
updated_at: '2017-12-25T20:16:23+00:00'
type: issue
status: closed
closed_at: '2017-12-25T20:16:23+00:00'
---

# Original Description
Resident windows build expert @iDunk5400 mentions this issue on IRC from #2864 :

https://build.getmonero.org/builders/monero-static-win64/builds/3199/steps/compile/logs/stdio:

```
[ 62%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.obj
In file included from C:/msys64/home/vagrant/slave/monero-static-win64/build/contrib/epee/include/string_tools.h:34:0,
                 from C:/msys64/home/vagrant/slave/monero-static-win64/build/src/common/command_line.cpp:37:
C:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:15:2: warning: #warning Please include winsock2.h before windows.h [-Wcpp]
 #warning Please include winsock2.h before windows.h
  ^~~~~~~
```

```
C:/msys64/mingw64/include/boost/asio/detail/socket_types.hpp:24:4: error: #error WinSock.h has already been included
 #  error WinSock.h has already been included
    ^~~~~
```



# Discussion History
## danrmiller | 2017-12-17T17:04:07+00:00
+windows

## moneromooo-monero | 2017-12-23T09:43:35+00:00
dEBRUYNE got a fix, will PR within a few days.

## dEBRUYNE-1 | 2017-12-23T14:44:05+00:00
#2994 

## moneromooo-monero | 2017-12-25T20:08:50+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-12-17T17:03:57+00:00
- Closed at: 2017-12-25T20:16:23+00:00
