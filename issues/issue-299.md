---
title: Building XmRig Failed On Kali Linux
source_url: https://github.com/xmrig/xmrig/issues/299
author: fubuki-is-cat
assignees: []
labels:
- libuv
created_at: '2017-12-28T03:30:38+00:00'
updated_at: '2018-08-02T15:55:17+00:00'
type: issue
status: closed
closed_at: '2018-08-02T15:55:17+00:00'
---

# Original Description
This is the output :
`root@kali:~/xmrig-2.4.3/build# cmake .. -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
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
CMake Error at /usr/share/cmake-3.9/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find UV (missing: UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.9/Modules/FindPackageHandleStandardArgs.cmake:377 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:8 (find_package_handle_standard_args)
  CMakeLists.txt:158 (find_package)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig-2.4.3/build/CMakeFiles/CMakeOutput.log".
root@kali:~/xmrig-2.4.3/build# cmake .. -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a
CMake Error at /usr/share/cmake-3.9/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find UV (missing: UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.9/Modules/FindPackageHandleStandardArgs.cmake:377 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:8 (find_package_handle_standard_args)
  CMakeLists.txt:158 (find_package)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig-2.4.3/build/CMakeFiles/CMakeOutput.log".
root@kali:~/xmrig-2.4.3/build# 
`


# Discussion History
## xmrig | 2017-12-28T07:51:35+00:00
If you already install libuv dependence try clean cmake run without -DUV_LIBRARY option, this path valid only for Ubuntu.
Otherwise you need install libuv1-dev (or something like that) package.
Thank you.

## Gill1000 | 2018-01-05T03:03:37+00:00
Bro , i have compile in first attempt..either do above method or remove  installed files and re-install files and follow guidelines in build section.

# Action History
- Created by: fubuki-is-cat | 2017-12-28T03:30:38+00:00
- Closed at: 2018-08-02T15:55:17+00:00
