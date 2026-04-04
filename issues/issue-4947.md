---
title: Another failed compile due to 'fallthrough' warning in simplewallet.cpp
source_url: https://github.com/monero-project/monero/issues/4947
author: ghost
assignees: []
labels: []
created_at: '2018-12-06T12:33:21+00:00'
updated_at: '2019-01-16T20:57:11+00:00'
type: issue
status: closed
closed_at: '2019-01-16T20:57:11+00:00'
---

# Original Description
This time with GCC 8.1 on ARMv8

```
[ 79%] Building CXX object src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o
/home/nodey/monero/src/simplewallet/simplewallet.cpp: In member function ‘bool cryptonote::simple_wallet::transfer_main(int, const std::vector<std::__cxx11::basic_string<char> >&)’:
/home/nodey/monero/src/simplewallet/simplewallet.cpp:5032:19: error: this statement may fall through [-Werror=implicit-fallthrough=]
         LOG_ERROR("Unknown transfer method, using default");
                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                                                      
/home/nodey/monero/src/simplewallet/simplewallet.cpp:5034:7: note: here
       case Transfer:
       ^~~~
cc1plus: all warnings being treated as errors
src/simplewallet/CMakeFiles/simplewallet.dir/build.make:62: recipe for target 'src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o' failed
make[3]: *** [src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o] Error 1
make[3]: Leaving directory '/home/nodey/monero/build/release'
CMakeFiles/Makefile2:2687: recipe for target 'src/simplewallet/CMakeFiles/simplewallet.dir/all' failed
make[2]: *** [src/simplewallet/CMakeFiles/simplewallet.dir/all] Error 2
make[2]: Leaving directory '/home/nodey/monero/build/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/nodey/monero/build/release'
Makefile:87: recipe for target 'release' failed
make: *** [release] Error 2
```

# Discussion History
## moneromooo-monero | 2019-01-16T20:29:50+00:00
+resolved

# Action History
- Created by: ghost | 2018-12-06T12:33:21+00:00
- Closed at: 2019-01-16T20:57:11+00:00
