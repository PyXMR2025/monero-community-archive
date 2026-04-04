---
title: Failed to build debug binaries of 0.11.1.0 on Ubuntu 16
source_url: https://github.com/monero-project/monero/issues/2740
author: erciccione
assignees: []
labels: []
created_at: '2017-10-30T12:28:58+00:00'
updated_at: '2018-04-04T12:27:36+00:00'
type: issue
status: closed
closed_at: '2018-04-04T12:27:36+00:00'
---

# Original Description
Release binaries built with no problems. Let me know if you need more details
```
[ 87%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/bootstrap_file.cpp.o
[ 87%] Linking CXX executable ../../bin/monero-utils-deserialize
../common/libcommon.so: undefined reference to `cryptonote::blockchain_db_types(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)'
collect2: error: ld returned 1 exit status
src/debug_utilities/CMakeFiles/cn_deserialize.dir/build.make:117: recipe for target 'bin/monero-utils-deserialize' failed
make[3]: *** [bin/monero-utils-deserialize] Error 1
make[3]: Leaving directory '/.../monero-0.11.1.0/build/debug'
CMakeFiles/Makefile2:2039: recipe for target 'src/debug_utilities/CMakeFiles/cn_deserialize.dir/all' failed
make[2]: *** [src/debug_utilities/CMakeFiles/cn_deserialize.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 87%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blocksdat_file.cpp.o
[ 88%] Linking CXX executable ../../bin/monero-utils-object-sizes
../common/libcommon.so: undefined reference to `cryptonote::blockchain_db_types(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)'
collect2: error: ld returned 1 exit status
src/debug_utilities/CMakeFiles/object_sizes.dir/build.make:117: recipe for target 'bin/monero-utils-object-sizes' failed
make[3]: *** [bin/monero-utils-object-sizes] Error 1
make[3]: Leaving directory '/.../monero-0.11.1.0/build/debug'
CMakeFiles/Makefile2:2087: recipe for target 'src/debug_utilities/CMakeFiles/object_sizes.dir/all' failed
make[2]: *** [src/debug_utilities/CMakeFiles/object_sizes.dir/all] Error 2
[ 89%] Linking CXX executable ../../bin/monero-blockchain-export
make[3]: Leaving directory '/.../monero-0.11.1.0/build/debug'
[ 89%] Built target blockchain_export
make[2]: Leaving directory '.../monero-0.11.1.0/build/debug'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '.../monero-0.11.1.0/build/debug'
Makefile:36: recipe for target 'debug' failed
make: *** [debug] Error 2
```

# Discussion History
## moneromooo-monero | 2017-12-02T09:12:20+00:00
Does master work ? I think the deps were reshuffled to fix something like that. If it works with master, I'm not going to care tbh.

## erciccione | 2017-12-04T12:37:38+00:00
Ok, i'm going to leave this opened until next release, to avoid duplicates

# Action History
- Created by: erciccione | 2017-10-30T12:28:58+00:00
- Closed at: 2018-04-04T12:27:36+00:00
