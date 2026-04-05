---
title: Build Never finishes in CentOS
source_url: https://github.com/xmrig/xmrig/issues/267
author: attackjoker11
assignees: []
labels:
- libuv
created_at: '2017-12-16T09:06:38+00:00'
updated_at: '2018-03-14T23:40:20+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:40:20+00:00'
---

# Original Description
 build]# cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a
CMake Error at CMakeLists.txt:9 (include):
  include could not find load file:

    cmake/cpu.cmake


CMake Error at CMakeLists.txt:158 (find_package):
  By not providing "FindUV.cmake" in CMAKE_MODULE_PATH this project has asked
  CMake to find a package configuration file provided by "UV", but CMake did
  not find one.

  Could not find a package configuration file provided by "UV" with any of
  the following names:

    UVConfig.cmake
    uv-config.cmake

  Add the installation prefix of "UV" to CMAKE_PREFIX_PATH or set "UV_DIR" to
  a directory containing one of the above files.  If "UV" provides a separate
  development package or SDK, be sure it has been installed.


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log".


# Discussion History
## ghost | 2017-12-19T02:04:34+00:00
Error is caused by missing libuv-devel. This should be installed as a dependency of libuv-static. So `yum install libuv-static` or `yum install libuv-devel`. 

## biaxz | 2018-01-07T06:20:59+00:00
Duplicate of #170 

# Action History
- Created by: attackjoker11 | 2017-12-16T09:06:38+00:00
- Closed at: 2018-03-14T23:40:20+00:00
