---
title: 'c++: error: unrecognized command line option ''-maes'''
source_url: https://github.com/xmrig/xmrig/issues/729
author: mike2001
assignees: []
labels: []
created_at: '2018-08-03T01:10:52+00:00'
updated_at: '2018-08-03T02:06:01+00:00'
type: issue
status: closed
closed_at: '2018-08-03T02:06:01+00:00'
---

# Original Description

-- The C compiler identification is GNU 5.3.1
-- The CXX compiler identification is GNU 5.3.1
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/android/xmrig/build

Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
c++: error: unrecognized command line option '-maes'
CMakeFiles/xmrig.dir/build.make:62: recipe for target 'CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed


# Discussion History
# Action History
- Created by: mike2001 | 2018-08-03T01:10:52+00:00
- Closed at: 2018-08-03T02:06:01+00:00
