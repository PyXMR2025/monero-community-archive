---
title: v0.11.1.0 fails to build `make debug`
source_url: https://github.com/monero-project/monero/issues/2776
author: jfreeze
assignees: []
labels:
- duplicate
created_at: '2017-11-08T04:48:57+00:00'
updated_at: '2017-11-08T11:00:29+00:00'
type: issue
status: closed
closed_at: '2017-11-08T11:00:29+00:00'
---

# Original Description
Debug build fails for version v0.11.1.0

git checkout v0.11.1.0
make debug
[elided...]
[ 92%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blockchain_export.cpp.o
[ 93%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/bootstrap_file.cpp.o
[ 94%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blocksdat_file.cpp.o
[ 95%] Linking CXX executable ../../bin/monero-blockchain-export
make[3]: Leaving directory '/home/jimfreeze/monero/build/debug'
[ 95%] Built target blockchain_export
make[3]: Entering directory '/home/jimfreeze/monero/build/debug'
Scanning dependencies of target cn_deserialize
make[3]: Leaving directory '/home/jimfreeze/monero/build/debug'
make[3]: Entering directory '/home/jimfreeze/monero/build/debug'
[ 96%] Building CXX object src/debug_utilities/CMakeFiles/cn_deserialize.dir/cn_deserialize.cpp.o
[ 97%] Linking CXX executable ../../bin/monero-utils-deserialize
../common/libcommon.so: undefined reference to `cryptonote::blockchain_db_types(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)'
collect2: error: ld returned 1 exit status
src/debug_utilities/CMakeFiles/cn_deserialize.dir/build.make:119: recipe for target 'bin/monero-utils-deserialize' failed
make[3]: *** [bin/monero-utils-deserialize] Error 1
make[3]: Leaving directory '/home/jimfreeze/monero/build/debug'
CMakeFiles/Makefile2:1971: recipe for target 'src/debug_utilities/CMakeFiles/cn_deserialize.dir/all' failed
make[2]: *** [src/debug_utilities/CMakeFiles/cn_deserialize.dir/all] Error 2
make[2]: Leaving directory '/home/jimfreeze/monero/build/debug'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/jimfreeze/monero/build/debug'
Makefile:36: recipe for target 'debug' failed
make: *** [debug] Error 2

# Discussion History
## moneromooo-monero | 2017-11-08T09:42:14+00:00
Apply a95e460c7116589b5dedf5c966cb84893fe8d521. Though you might need to apply a few more if it doesn't apply cleanly.

## erciccione | 2017-11-08T10:38:59+00:00
Isn't this a duplicate of #2740 ? @moneromooo-monero the same solution apply?

## moneromooo-monero | 2017-11-08T10:57:07+00:00
Looks like it, thanks :)

+duplicate


# Action History
- Created by: jfreeze | 2017-11-08T04:48:57+00:00
- Closed at: 2017-11-08T11:00:29+00:00
