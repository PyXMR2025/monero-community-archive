---
title: CMake no longer defines WIN32 on MSYS
source_url: https://github.com/xmrig/xmrig/issues/950
author: minhng99
assignees: []
labels: []
created_at: '2019-02-26T08:59:04+00:00'
updated_at: '2019-08-02T12:04:30+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:04:30+00:00'
---

# Original Description
Hello, looks like CMake no longer defines WIN32, thus make compile error because it trying to compile _unix on Windows
```
# cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=/d/xmrig-deps/gcc/x64/  -DWITH_TLS=OFF
-- The C compiler identification is GNU 7.4.0
-- The CXX compiler identification is GNU 7.4.0
CMake Warning at /usr/share/cmake-3.13.2/Modules/Platform/MSYS.cmake:15 (message):
  CMake no longer defines WIN32 on MSYS!

  (1) If you are just trying to build this project, ignore this warning or
  quiet it by setting CMAKE_LEGACY_CYGWIN_WIN32=0 in your environment or in
  the CMake cache.  If later configuration or build errors occur then this
  project may have been written under the assumption that MSYS is WIN32.  In
  that case, set CMAKE_LEGACY_CYGWIN_WIN32=1 instead.

  (2) If you are developing this project, add the line

    set(CMAKE_LEGACY_CYGWIN_WIN32 0) # Remove when CMake >= 2.8.4 is required

  at the top of your top-level CMakeLists.txt file or set the minimum
  required version of CMake to 2.8.4 or higher.  Then teach your project to
  build on Cygwin without WIN32.
Call Stack (most recent call first):
  /usr/share/cmake-3.13.2/Modules/CMakeSystemSpecificInformation.cmake:27 (include)
  CMakeLists.txt:2 (project)
```

You could temporary workaround this by adding `-DCMAKE_LEGACY_CYGWIN_WIN32=1` while `cmake`


# Discussion History
## DeadManWalkingTO | 2019-03-21T14:08:51+00:00
Please check #993. 

# Action History
- Created by: minhng99 | 2019-02-26T08:59:04+00:00
- Closed at: 2019-08-02T12:04:30+00:00
