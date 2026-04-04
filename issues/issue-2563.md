---
title: can't build
source_url: https://github.com/monero-project/monero/issues/2563
author: lelvisl
assignees: []
labels:
- invalid
created_at: '2017-10-02T13:56:04+00:00'
updated_at: '2018-01-26T08:48:12+00:00'
type: issue
status: closed
closed_at: '2017-10-02T14:08:07+00:00'
---

# Original Description
on make command every time i see this

```
Scanning dependencies of target epee
[ 58%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 59%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
contrib/epee/src/CMakeFiles/epee.dir/build.make:86: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o' failed
make[2]: *** [contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o] Error 4
CMakeFiles/Makefile2:424: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/all' failed
make[1]: *** [contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
```

# Discussion History
## moneromooo-monero | 2017-10-02T13:59:34+00:00
It's just out of memory. Use more RAM, or add swap.

+invalid


## lelvisl | 2017-10-02T14:08:07+00:00
thx. write in readme minimal RAM

## lonetech | 2018-01-26T08:48:12+00:00
It's simply insane that such a simple function as authenticating http should require over half a gigabyte of memory to compile. The library is broken, and C++ is encouraging it. 

# Action History
- Created by: lelvisl | 2017-10-02T13:56:04+00:00
- Closed at: 2017-10-02T14:08:07+00:00
