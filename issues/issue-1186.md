---
title: Debian cmake error
source_url: https://github.com/xmrig/xmrig/issues/1186
author: MarcCrams
assignees: []
labels:
- question
created_at: '2019-09-21T14:22:00+00:00'
updated_at: '2019-12-22T19:27:07+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:27:07+00:00'
---

# Original Description
cmake ..
-- Use ARM_TARGET=7 (armv7l)
CMake Error at /usr/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:29 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:29 (include)


-- Configuring incomplete, errors occurred!
See also "/home/pi/xmrig/build/CMakeFiles/CMakeOutput.log".


# Discussion History
## xmrig | 2019-09-21T14:29:34+00:00
Disable hwloc by `-DWITH_HWLOC=OFF` (for ARM it not necessary) or install or build hwloc.
Thank you.

## MarcCrams | 2019-09-21T14:54:42+00:00
When I do make I have this error
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1662: xmrig-notls] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


## xmrig | 2019-09-25T09:30:37+00:00
Output not contains full information, but if you compile for Android this issue might be fixed in evo branch.

## MarcCrams | 2019-09-25T13:34:55+00:00
How to compile for android?

# Action History
- Created by: MarcCrams | 2019-09-21T14:22:00+00:00
- Closed at: 2019-12-22T19:27:07+00:00
