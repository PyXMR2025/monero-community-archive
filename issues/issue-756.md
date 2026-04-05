---
title: Win32/MSYS2 build failed
source_url: https://github.com/xmrig/xmrig/issues/756
author: timk74
assignees: []
labels:
- question
created_at: '2018-09-19T04:07:43+00:00'
updated_at: '2018-10-10T22:21:40+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:21:40+00:00'
---

# Original Description
Can't build xmrig for Win32 with MSYS2. CMAKE output:
```
D:\xmrig\xmrig-2.6.4>md build
D:\xmrig\xmrig-2.6.4>cd build
D:\xmrig\xmrig-2.6.4\build>cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=..\deps\gcc\x86
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.

CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.

-- Configuring incomplete, errors occurred!
See also "D:/xmrig/xmrig-2.6.4/build/CMakeFiles/CMakeOutput.log".
See also "D:/xmrig/xmrig-2.6.4/build/CMakeFiles/CMakeError.log".
```
OS: Windows 10 x64.  All MSYS2 packages specified in the build instructions are installed. There is no problem with Win64/MSVS 2017 build.

# Discussion History
## xmrig | 2018-09-19T04:37:34+00:00
You should run commands in MSYS2 shell, for example mingw64.exe.
Thank you.

## timk74 | 2018-09-19T05:35:06+00:00
Thanks for reply. Used the following bath file:
```
md build
cd build
C:\msys32\mingw32.exe cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=../gcc/x86 -DWITH_AEON=OFF -DWITH_HTTPD=OFF
pause
C:\msys32\mingw32.exe cmake --build . --config Release
```
Everything seems to go smoothly... but there is no build\Release folder and output exe file :)


# Action History
- Created by: timk74 | 2018-09-19T04:07:43+00:00
- Closed at: 2018-10-10T22:21:40+00:00
