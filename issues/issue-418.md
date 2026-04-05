---
title: cmake error
source_url: https://github.com/xmrig/xmrig/issues/418
author: mmt-itns
assignees: []
labels: []
created_at: '2018-02-28T12:59:55+00:00'
updated_at: '2018-02-28T13:37:34+00:00'
type: issue
status: closed
closed_at: '2018-02-28T13:37:34+00:00'
---

# Original Description
Hi,

I get this error when building in MINGW64:

MINGW64 ~/xmrig-master/xmrig-master/build
.2\xmrig-deps-2.2\gcc\libmicrohttpd\x64\lib\libmicrohttpd.a"\msys64\xmrig-deps-2.
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
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
-- Found UV: C:/msys64/xmrig-deps-2.2/xmrig-deps-2.2/gcc/libuv/x64/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Found mhd: C:/msys64/xmrig-deps-2.2/xmrig-deps-2.2/gcc/libmicrohttpd/x64/include
-- Configuring done
CMake Error at CMakeLists.txt:207 (add_executable):
  Cannot find source file:

    src/Options.cpp

  Tried extensions .c .C .c++ .cc .cpp .cxx .m .M .mm .h .hh .h++ .hm .hpp
  .hxx .in .txx


CMake Error: CMake can not determine linker language for target: xmrig
CMake Error: Cannot determine link language for target "xmrig".
-- Generating done
-- Build files have been written to: C:/msys64/home/Stephen/xmrig-master/xmrig-master/build


After this I do Make:

MINGW64 ~/xmrig-master/xmrig-master/build
$ make
Scanning dependencies of target cpuid
[ 16%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[ 33%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[ 50%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[ 66%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 83%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[100%] Linking C static library libcpuid.a
[100%] Built target cpuid
Scanning dependencies of target xmrig
make[2]: *** No rule to make target 'CMakeFiles/xmrig.dir/build'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


Any suggestions?

KR.

# Discussion History
## mmt-itns | 2018-02-28T13:37:34+00:00
Never mind, AV was breaking the build.

# Action History
- Created by: mmt-itns | 2018-02-28T12:59:55+00:00
- Closed at: 2018-02-28T13:37:34+00:00
