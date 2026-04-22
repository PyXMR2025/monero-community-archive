---
title: Build Error
source_url: https://github.com/xmrig/xmrig/issues/695
author: corrm
assignees: []
labels:
- libuv
created_at: '2018-06-17T13:43:07+00:00'
updated_at: '2018-06-17T19:07:55+00:00'
type: issue
status: closed
closed_at: '2018-06-17T17:51:44+00:00'
---

# Original Description
CMake Error at C:/Program Files/CMake/share/cmake-3.12/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.12/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:175 (find_package)

# Discussion History
## xmrig | 2018-06-17T17:51:44+00:00
Specify paths to libuv or use xmrig-deps https://github.com/xmrig/xmrig/wiki/Windows-Build
Thank you.

## corrm | 2018-06-17T19:07:55+00:00
can u give me example for VS2017 CMD Command
libuv: C:\Users\CorrM\Downloads\Compressed\libuv-1.20.3\Debug\lib

# Action History
- Created by: corrm | 2018-06-17T13:43:07+00:00
- Closed at: 2018-06-17T17:51:44+00:00
