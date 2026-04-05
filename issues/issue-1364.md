---
title: Error compiling Xmrig 5.1.0
source_url: https://github.com/xmrig/xmrig/issues/1364
author: TheIcehawk
assignees: []
labels: []
created_at: '2019-12-02T03:58:21+00:00'
updated_at: '2021-04-12T15:12:52+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:12:52+00:00'
---

# Original Description
I installed the latest version of Cmake for windows and downloaded the latest deps 3.5 and xmrig-5.1.0 source code and extracted them to their own folders on C drive, however after I make the "build" folder and run the "cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=c:\xmrig-deps\msvc2017\x64" command it comes back with this error: 

C:\xmrig-5.1.0\build>cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=c:\xmrig-deps\msvc2017\x64
-- Selecting Windows SDK version 10.0.14393.0 to target Windows 10.0.18362.
-- The C compiler identification is MSVC 19.10.25027.0
-- The CXX compiler identification is MSVC 19.10.25027.0
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.10.25017/bin/HostX86/x64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.10.25017/bin/HostX86/x64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.10.25017/bin/HostX86/x64/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.10.25017/bin/HostX86/x64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:174 (find_package)


-- Configuring incomplete, errors occurred!
See also "C:/xmrig-5.1.0/build/CMakeFiles/CMakeOutput.log".




# Discussion History
# Action History
- Created by: TheIcehawk | 2019-12-02T03:58:21+00:00
- Closed at: 2021-04-12T15:12:52+00:00
