---
title: MSYS64 build
source_url: https://github.com/xmrig/xmrig/issues/35
author: Nivoyash
assignees: []
labels: []
created_at: '2017-07-11T10:08:17+00:00'
updated_at: '2017-07-19T23:58:02+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:58:02+00:00'
---

# Original Description
Searched everything, but can not find the libuv.a file to build. I found the old version 1.8 but on it I get the error:
`hustle@home MINGW64 /c/Users/hustle/Downloads/xmrig-master/xmrig-master
$ mkdir build3

hustle@home MINGW64 /c/Users/hustle/Downloads/xmrig-master/xmrig-master
$ cd build3

hustle@home MINGW64 /c/Users/hustle/Downloads/xmrig-master/xmrig-master/build3
$ cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="C:\libuv-master\include" -DUV_LIBRARY="C:\libuv-master\lib\x64\libuv.a"
-- The C compiler identification is GNU 7.1.0
-- The CXX compiler identification is GNU 7.1.0
-- Check for working C compiler: C:/msys64/mingw64/bin/cc.exe
-- Check for working C compiler: C:/msys64/mingw64/bin/cc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/c++.exe
-- Check for working CXX compiler: C:/msys64/mingw64/bin/c++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: C:/libuv-master/lib/x64/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Users/hustle/Downloads/xmrig-master/xmrig-master/build3

hustle@home MINGW64 /c/Users/hustle/Downloads/xmrig-master/xmrig-master/build3
$ make
Scanning dependencies of target jansson
[  1%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.obj
[  3%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/error.c.obj
[  5%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable.c.obj
[  7%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.obj
[  9%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/load.c.obj
[ 11%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/memory.c.obj
[ 12%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/pack_unpack.c.obj
[ 14%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strbuffer.c.obj
[ 16%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strconv.c.obj
[ 18%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/utf.c.obj
[ 20%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/value.c.obj
[ 22%] Linking C static library libjansson.a
[ 22%] Built target jansson
Scanning dependencies of target cpuid
[ 24%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[ 25%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[ 27%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[ 29%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 31%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 33%] Linking C static library libcpuid.a
[ 33%] Built target cpuid
Scanning dependencies of target xmrig
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp: In constructor 'FileLog::FileLog(const char*)':
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp:44:60: error: 'O_CREAT' was not declared in this scope
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                            ^~~~~~~
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp:44:60: note: suggested alternative: 'OF_CREATE'
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                            ^~~~~~~
                                                            OF_CREATE
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp:44:70: error: 'O_APPEND' was not declared in this scope
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                      ^~~~~~~~
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp:44:70: note: suggested alternative: 'MF_APPEND'
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                      ^~~~~~~~
                                                                      MF_APPEND
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp:44:81: error: 'O_WRONLY' was not declared in this scope
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                                 ^~~~~~~~
C:/Users/hustle/Downloads/xmrig-master/xmrig-master/src/log/FileLog.cpp:44:81: note: suggested alternative: 'CF_TTONLY'
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                                 ^~~~~~~~
                                                                                 CF_TTONLY
make[2]: *** [CMakeFiles/xmrig.dir/build.make:114: CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj] Ошибка 1
make[1]: *** [CMakeFiles/Makefile2:69: CMakeFiles/xmrig.dir/all] Ошибка 2
make: *** [Makefile:84: all] Ошибка 2

hustle@home MINGW64 /c/Users/hustle/Downloads/xmrig-master/xmrig-master/build3
$
`

Perhaps someone has an archive libuv / include and libuv / libuv.a? For a day I'm trying to build ...

# Discussion History
## xmrig | 2017-07-11T10:19:11+00:00
Try add `#include <fcntl.h>` in `src/log/FileLog.cpp` might help.
Thank you.

# Action History
- Created by: Nivoyash | 2017-07-11T10:08:17+00:00
- Closed at: 2017-07-19T23:58:02+00:00
