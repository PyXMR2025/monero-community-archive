---
title: 'Raspberry compiling error:'
source_url: https://github.com/xmrig/xmrig/issues/1357
author: quantflares
assignees: []
labels: []
created_at: '2019-12-01T17:44:48+00:00'
updated_at: '2019-12-01T17:49:09+00:00'
type: issue
status: closed
closed_at: '2019-12-01T17:48:42+00:00'
---

# Original Description
I tried to figure out without success..

-- Use ARM_TARGET=7 (armv7l)
CMake Error at /usr/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake                                                   :137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_                                                   FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:34 (include)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log".


# Discussion History
## quantflares | 2019-12-01T17:49:09+00:00
find the way 
https://www.ourtecads.com/2019/10/how-to-fix-hwloc-issue-when-running.html

# Action History
- Created by: quantflares | 2019-12-01T17:44:48+00:00
- Closed at: 2019-12-01T17:48:42+00:00
