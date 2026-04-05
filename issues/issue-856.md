---
title: I tried to build xmrig through MSYS2, wrong.
source_url: https://github.com/xmrig/xmrig/issues/856
author: ghost
assignees: []
labels:
- question
created_at: '2018-10-30T08:15:23+00:00'
updated_at: '2018-10-30T11:53:00+00:00'
type: issue
status: closed
closed_at: '2018-10-30T11:53:00+00:00'
---

# Original Description
pacman -Sy
pacman -S mingw-w64-x86_64-gcc
pacman -S make
pacman -S mingw-w64-x86_64-cmake
pacman -S mingw-w64-x86_64-pkg-config

mkdir build
cd build
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64

C:\xmrig-deps-3.3\xmrig-2.8.3\build>cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=C:\xmrig-deps-3.3\gcc\x64 -DWITH_HTTPD=OFF -DWITH_TLS=OFF
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "C:/xmrig-deps-3.3/xmrig-2.8.3/build/CMakeFiles/CMakeOutput.log".

![snipaste_2018-10-30_16-13-23](https://user-images.githubusercontent.com/32661990/47704531-e6ae0180-dc5e-11e8-9ea9-e71c0b5081d4.png)




# Discussion History
## xmrig | 2018-10-30T08:23:34+00:00
You should run `cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64` inside MSYS2 shell, not in `cmd`.
Thank you.

## ghost | 2018-10-30T09:43:05+00:00
> 
> 
> You should run `cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64` inside MSYS2 shell, not in `cmd`.
> Thank you.

$ make
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
C:/msys32/home/▒▒/xmrig-deps-3.3/xmrig-2.8.3/src/api/NetworkState.cpp:31:10: fatal error: api/NetworkState.h: No such file or directory
 #include "api/NetworkState.h"
          ^~~~~~~~~~~~~~~~~~~~
wht?

## xmrig | 2018-10-30T09:57:44+00:00
Don't use any special non English/Latin characters in path including spaces.

## ghost | 2018-10-30T10:44:07+00:00
> Don't use any special non English/Latin characters in path including spaces.

Windows need to install cmake?
Or install cmake in msys2, windows does not need to install cmake. 


## 2010phenix | 2018-10-30T11:46:15+00:00
@Unlash this is issue tracker, not a help desk..
use search and read wiki HOW TO BUILD: https://github.com/xmrig/xmrig/wiki/Windows-Build

# Action History
- Created by: ghost | 2018-10-30T08:15:23+00:00
- Closed at: 2018-10-30T11:53:00+00:00
