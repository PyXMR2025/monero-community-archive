---
title: 'When compiling 2.99.3 beta on Mac, error is thrown: "Could NOT find HWLOC
  (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)"'
source_url: https://github.com/xmrig/xmrig/issues/1094
author: tommyprevatt
assignees: []
labels: []
created_at: '2019-08-01T18:32:13+00:00'
updated_at: '2019-08-01T18:42:55+00:00'
type: issue
status: closed
closed_at: '2019-08-01T18:42:54+00:00'
---

# Original Description
This error is thrown when compiling for Mac: "Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)"

Full terminal output is this. Log is below:

`cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
-- The C compiler identification is AppleClang 10.0.0.10001044
-- The CXX compiler identification is AppleClang 10.0.0.10001044
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
CMake Error at /usr/local/Cellar/cmake/3.15.0/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.15.0/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:27 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:28 (include)


-- Configuring incomplete, errors occurred!`

[CMakeOutput.log](https://github.com/xmrig/xmrig/files/3458197/CMakeOutput.log)


# Discussion History
## tommyprevatt | 2019-08-01T18:42:54+00:00
Figured this out. Had to run "brew install hwloc" and install those libs. 

# Action History
- Created by: tommyprevatt | 2019-08-01T18:32:13+00:00
- Closed at: 2019-08-01T18:42:54+00:00
