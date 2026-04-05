---
title: Compiled on Windows
source_url: https://github.com/xmrig/xmrig/issues/53
author: mik2141797
assignees: []
labels: []
created_at: '2017-08-04T13:15:35+00:00'
updated_at: '2017-08-07T14:13:28+00:00'
type: issue
status: closed
closed_at: '2017-08-07T14:13:28+00:00'
---

# Original Description
When i try compiled on windows 10 i get error

```
make
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
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
C:/xmrig/src/log/FileLog.cpp: In constructor 'FileLog::FileLog(const char*)':
C:/xmrig/src/log/FileLog.cpp:37:60: error: 'O_CREAT' was not declared in this scope
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                            ^~~~~~~
C:/xmrig/src/log/FileLog.cpp:37:60: note: suggested alternative: 'OF_CREATE'
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                            ^~~~~~~
                                                            OF_CREATE
C:/xmrig/src/log/FileLog.cpp:37:70: error: 'O_APPEND' was not declared in this scope
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                      ^~~~~~~~
C:/xmrig/src/log/FileLog.cpp:37:70: note: suggested alternative: 'MF_APPEND'
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                      ^~~~~~~~
                                                                      MF_APPEND
C:/xmrig/src/log/FileLog.cpp:37:81: error: 'O_WRONLY' was not declared in this scope
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                                 ^~~~~~~~
C:/xmrig/src/log/FileLog.cpp:37:81: note: suggested alternative: 'CF_TTONLY'
     m_file = uv_fs_open(uv_default_loop(), &req, fileName, O_CREAT | O_APPEND | O_WRONLY, 0644, nullptr);
                                                                                 ^~~~~~~~
                                                                                 CF_TTONLY
make[2]: *** [CMakeFiles/xmrig.dir/build.make:139: CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj] Ошибка 1
make[1]: *** [CMakeFiles/Makefile2:69: CMakeFiles/xmrig.dir/all] Ошибка 2
make: *** [Makefile:84: all] Ошибка 2

```

# Discussion History
## xmrig | 2017-08-04T13:25:50+00:00
Please check solution from this issue #35
It was unanswered. Thank you.

## mik2141797 | 2017-08-07T11:49:16+00:00
I try compiled via Visual Studio
I install x32 libuv and try compiled x32 miner
`cmake .. -G "Visual Studio 15 2017" -T v140_xp -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR=c:\libuv32\include -DUV_LIBRARY=c:\libuv32\libuv.dll`

when i try run xmrig.exe i get error "libuv.dll not found". If I put libuv.dll next to xmrig.exe the miner works fine. How can i compiled exe include dll?

## xmrig | 2017-08-07T11:57:12+00:00
Where you get libuv? On this page https://github.com/libuv/libuv very detailed instructions how build it from source.
Also UV_LIBRARY it path to .lib file not .dll.

## mik2141797 | 2017-08-07T12:00:45+00:00
i use binaries for Windows http://dist.libuv.org/dist/v1.13.1/libuv-x86-v1.13.1.build12.exe
after install 
https://farm5.staticflickr.com/4375/35615437013_e93ff94c3f_o.png


## mik2141797 | 2017-08-07T12:12:15+00:00
I compiled new lib and miner work fine. 
The file from the Windows binaries is not integrated into the miner

## xmrig | 2017-08-07T12:14:46+00:00
Right that precompiled lib for dynamic linking so it required .dll file to work.

# Action History
- Created by: mik2141797 | 2017-08-04T13:15:35+00:00
- Closed at: 2017-08-07T14:13:28+00:00
