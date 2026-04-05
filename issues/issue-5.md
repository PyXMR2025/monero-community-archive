---
title: I can not make
source_url: https://github.com/xmrig/xmrig/issues/5
author: Nivoyash
assignees: []
labels: []
created_at: '2017-05-20T23:37:54+00:00'
updated_at: '2017-08-17T14:33:23+00:00'
type: issue
status: closed
closed_at: '2017-08-17T14:33:23+00:00'
---

# Original Description
**Installed**:
- MVS17
- CMake (and TDM-GCC-64)
- cURL

**Source on**: C:\Users\user\Downloads\xmrig-master\xmrig-master
**Build dir**: C:\Users\user\Downloads\xmrig-master\xmrig-master\build
**Command**: cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCURL_INCLUDE_DIR="C:\curl-7.54.0\include" -DCURL_LIBRARY="C:\curl-7.54.0\lib" -DCMAKE_C_COMPILER="C:\MinGW\bin\c++.exe"

**Output**: 
`
C:\Users\user\Downloads\xmrig-master\xmrig-master\build>cmake .. -G "Unix Makefi
les" -DCMAKE_BUILD_TYPE=Release -DCURL_INCLUDE_DIR="C:\curl-7.54.0\include" -DCU
RL_LIBRARY="C:\curl-7.54.0\lib" -DCMAKE_C_COMPILER="C:\MinGW\bin\c++.exe"
-- The C compiler identification is unknown
CMake Error at build/CMakeFiles/3.8.1/CMakeCCompiler.cmake:1 (set):
  Syntax error in cmake code at

    C:/Users/user/Downloads/xmrig-master/xmrig-master/build/CMakeFiles/3.8.1/CMa
keCCompiler.cmake:1

  when parsing string

    C:\MinGW\bin\c++.exe

  Invalid escape sequence \M
Call Stack (most recent call first):
  CMakeLists.txt:2 (project)


-- Configuring incomplete, errors occurred!
See also "C:/Users/user/Downloads/xmrig-master/xmrig-master/build/CMakeFiles/CMa
keOutput.log".
See also "C:/Users/user/Downloads/xmrig-master/xmrig-master/build/CMakeFiles/CMa
keError.log".

C:\Users\user\Downloads\xmrig-master\xmrig-master\build>`


Maby you have .sln MVS2017?

# Discussion History
## xmrig | 2017-05-20T23:57:31+00:00
You need a C compiler (gcc) not C++
MSVC (any version) not supported.

# Action History
- Created by: Nivoyash | 2017-05-20T23:37:54+00:00
- Closed at: 2017-08-17T14:33:23+00:00
