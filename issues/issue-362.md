---
title: MVS 2017 error build
source_url: https://github.com/xmrig/xmrig/issues/362
author: Nivoyash
assignees: []
labels: []
created_at: '2018-01-25T22:44:02+00:00'
updated_at: '2018-11-05T12:47:40+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:47:40+00:00'
---

# Original Description
Use Minggw to create sln but:
` cmake .. -G "Visual Studio 15 2017" -DUV_INCLUDE_DIR="C:\MVC_TEST\msvc2017\libuv\x64\include" -DUV_LIBRARY="C:\MVC_TEST\msvc2017\libuv\x64\lib\libuv.lib" -DMHD_INCLUDE_DIR="C:\MVC_TEST\msvc2017\libmicrohttpd\x64\include" -DMHD_LIBRARY="C:\MVC_TEST\msvc2017\libmicrohttpd\x64\lib\libmicrohttpd.lib"
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.



CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.



-- Configuring incomplete, errors occurred!
See also "C:/Miner/build3/CMakeFiles/CMakeOutput.log".
See also "C:/Miner/build3/CMakeFiles/CMakeError.log".
`

Okay, set compilator:
` cmake .. -G "Visual Studio 15 2017" -DCMAKE_CXX_COMPILER="C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.12.25827\bin\Hostx86\x64\cl.exe" -DCMAKE_C_COMPILER="C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.12.25827\bin\Hostx86\x64\cl.exe" -DUV_INCLUDE_DIR="C:\MVC_TEST\msvc2017\libuv\x64\include" -DUV_LIBRARY="C:\MVC_TEST\msvc2017\libuv\x64\lib\libuv.lib" -DMHD_INCLUDE_DIR="C:\MVC_TEST\msvc2017\libmicrohttpd\x64\include" -DMHD_LIBRARY="C:\MVC_TEST\msvc2017\libmicrohttpd\x64\lib\libmicrohttpd.lib"
-- The C compiler identification is unknown
CMake Error at build3/CMakeFiles/3.9.6/CMakeCCompiler.cmake:1 (set):
  Syntax error in cmake code at

    C:/Miner/build3/CMakeFiles/3.9.6/CMakeCCompiler.cmake:1

  when parsing string

    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.12.25827\bin\Hostx86\x64\cl.exe

  Invalid escape sequence \P
Call Stack (most recent call first):
  CMakeLists.txt:2 (project)


-- Configuring incomplete, errors occurred!
See also "C:/Miner/build3/CMakeFiles/CMakeOutput.log".
See also "C:/Miner/build3/CMakeFiles/CMakeError.log".
`

# Discussion History
## RansomFuck | 2018-02-12T22:07:19+00:00
Re-install Visual Studio with included Windows 10 Dev. Pack.

# Action History
- Created by: Nivoyash | 2018-01-25T22:44:02+00:00
- Closed at: 2018-11-05T12:47:40+00:00
