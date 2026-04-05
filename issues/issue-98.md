---
title: How to create Single Static binary for windows.
source_url: https://github.com/xmrig/xmrig/issues/98
author: dorimanx
assignees: []
labels:
- question
created_at: '2017-09-07T12:45:48+00:00'
updated_at: '2019-01-29T18:09:51+00:00'
type: issue
status: closed
closed_at: '2017-09-07T19:15:45+00:00'
---

# Original Description
Hi,
I have followed all instructions and been able to build win64 xmrig.exe without any issues
using the MINGW64 (msys2-x86_64-20161025) + libuv 1.14

now when i try to run the binary (it's smaller than yours) it's demand to fine 3 more dll files and then works as expected.

files are:
libstdc++-6.dll
libgcc_s_seh-1.dll
libwinpthread-1.dll

how can i build ONE static xmrig.exe that already include this dlls inside. and just run.

Thanks.


# Discussion History
## xmrig | 2017-09-07T13:30:48+00:00
It strange by default static build, this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L151 makes it.

## dorimanx | 2017-09-07T13:37:55+00:00
well my win is 64bit. maybe i can add -static to next line?
i have set:

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} static -static-libgcc -static-libstdc++")

compile, and nothing. smaller size and request to have 3 dlls.

## xmrig | 2017-09-07T13:43:42+00:00
It should be static by default, if remove that line, it will be exe + dlls like you get

## dorimanx | 2017-09-07T13:47:42+00:00
well, i have followed 100% install set. and my build was like this:
git clone your repo.
cd xmrig
mkdir build
cd build
cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="e:\msys64\mingw64\include" -DUV_LIBRARY="e:\msys64\mingw64\lib\libuv.a" 
make

creating file xmrig.exe 497,664 bytes that demand + dlls.


## xmrig | 2017-09-07T13:53:57+00:00
What cmake and gcc versions?
`cmake --version`, `gcc -v`

## dorimanx | 2017-09-07T13:55:22+00:00
Dorimanx@My-PC MINGW64 ~/xmrig/build
$ cmake --version
cmake version 3.9.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).

Dorimanx@My-PC MINGW64 ~/xmrig/build
$ gcc -v
Using built-in specs.
COLLECT_GCC=E:\msys64\mingw64\bin\gcc.exe
COLLECT_LTO_WRAPPER=E:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.2.0/lto-wrapper.exe
Target: x86_64-w64-mingw32
Configured with: ../gcc-7.2.0/configure --prefix=/mingw64 --with-local-prefix=/mingw64/local --build=x86_64-w64-mingw32 --host=x86_64-w64-mingw32 --target=x86_64-w64-mingw32 --with-native-system-header-dir=/mingw64/x86_64-w64-mingw32/include --libexecdir=/mingw64/lib --enable-bootstrap --with-arch=x86-64 --with-tune=generic --enable-languages=c,lto,c++,objc,obj-c++,fortran,ada --enable-shared --enable-static --enable-libatomic --enable-threads=posix --enable-graphite --enable-fully-dynamic-string --enable-libstdcxx-time=yes --disable-libstdcxx-pch --disable-libstdcxx-debug --disable-isl-version-check --enable-lto --enable-libgomp --disable-multilib --enable-checking=release --disable-rpath --disable-win32-registry --disable-nls --disable-werror --disable-symvers --with-libiconv --with-system-zlib --with-gmp=/mingw64 --with-mpfr=/mingw64 --with-mpc=/mingw64 --with-isl=/mingw64 --with-pkgversion='Rev1, Built by MSYS2 project' --with-bugurl=https://sourceforge.net/projects/msys2 --with-gnu-as --with-gnu-ld
Thread model: posix
gcc version 7.2.0 (Rev1, Built by MSYS2 project)

Dorimanx@My-PC MINGW64 ~/xmrig/build
$


## dorimanx | 2017-09-07T14:12:01+00:00
Found this.
https://stackoverflow.com/questions/18138635/mingw-exe-requires-a-few-gcc-dlls-regardless-of-the-code
not sure what to change, you are the master of this program!

## xmrig | 2017-09-07T15:14:45+00:00
Pretty strange, it works fine on my machines I able build static (default) and dynamic builds, if remove the line.

1. Please try download official cmake build (`cmake-3.9.1-win64-x64.msi`) from https://cmake.org/download/ 
2. Then remove anything in build folder.
3. Use `"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="e:\msys64\mingw64\include" -DUV_LIBRARY="e:\msys64\mingw64\lib\libuv.a"`

## dorimanx | 2017-09-07T15:46:45+00:00
no change. cleaned the folder.
====================
Dorimanx@My-PC MINGW64 ~/xmrig/build
$ "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="e:\msys64\mingw64\include" -DUV_LIBRARY="e:\msys64\mingw64\lib\libuv.a"
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
-- Check for working C compiler: E:/msys64/mingw64/bin/cc.exe
-- Check for working C compiler: E:/msys64/mingw64/bin/cc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: E:/msys64/mingw64/bin/c++.exe
-- Check for working CXX compiler: E:/msys64/mingw64/bin/c++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: E:/msys64/mingw64/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Configuring done
-- Generating done
-- Build files have been written to: E:/msys64/home/Dorimanx/xmrig/build

Dorimanx@My-PC MINGW64 ~/xmrig/build
$

Dorimanx@My-PC MINGW64 ~/xmrig/build
$ make
Scanning dependencies of target jansson
[  1%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.obj
[  3%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/error.c.obj
[  5%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable.c.obj
[  7%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.obj
[  9%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/load.c.obj
[ 10%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/memory.c.obj
[ 12%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/pack_unpack.c.obj
[ 14%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strbuffer.c.obj
[ 16%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strconv.c.obj
[ 18%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/utf.c.obj
[ 20%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/value.c.obj
[ 21%] Linking C static library libjansson.a
[ 21%] Built target jansson
Scanning dependencies of target cpuid
[ 23%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[ 25%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[ 27%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[ 29%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 30%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 32%] Linking C static library libcpuid.a
[ 32%] Built target cpuid
Scanning dependencies of target xmrig
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.obj
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.obj
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.obj
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.obj
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.obj
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.obj
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.obj
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.obj
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 76%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/App_win.cpp.obj
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_win.cpp.obj
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_win.cpp.obj
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_win.cpp.obj
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.obj
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.obj
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.obj
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.obj
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.obj
[ 94%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.obj
[ 96%] Building C object CMakeFiles/xmrig.dir/src/crypto/soft_aes.c.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
[100%] Linking CXX executable xmrig.exe
[100%] Built target xmrig

Dorimanx@My-PC MINGW64 ~/xmrig/build
$
====================

## dorimanx | 2017-09-07T19:15:45+00:00
I am happy to report that problem is resolved when i have used your rebuilt libuv
from here : https://github.com/xmrig/xmrig-deps/releases

cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="c:\msys64\libuv\libuv-gcc-x64\include" -DUV_LIBRARY="c:\msys64\libuv\libuv-gcc-x64\lib\libuv.a"

make
got xmrig.exe full static. no dlls needed.
so problem is with build in libuv in MSYS2 application.

Please update your build guide or just add the libs inside source.

Thanks for support.

## ghost | 2018-10-31T12:12:28+00:00



> 
> 
> I am happy to report that problem is resolved when i have used your rebuilt libuv
> from here : https://github.com/xmrig/xmrig-deps/releases
> 
> cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="c:\msys64\libuv\libuv-gcc-x64\include" -DUV_LIBRARY="c:\msys64\libuv\libuv-gcc-x64\lib\libuv.a"
> 
> make
> got xmrig.exe full static. no dlls needed.
> so problem is with build in libuv in MSYS2 application.
> 
> Please update your build guide or just add the libs inside source.
> 
> Thanks for support.


c:\msys64\libuv\libuv-gcc-x64\include

libuv\libuv-gcc-x64\include
I did not find this folder

![default](https://user-images.githubusercontent.com/32661990/47787259-47b20400-dd49-11e8-80b9-2a1aea92d2bc.png)



## sanitariu | 2019-01-29T18:09:51+00:00
This problem still exists on latest windows 7 build

# Action History
- Created by: dorimanx | 2017-09-07T12:45:48+00:00
- Closed at: 2017-09-07T19:15:45+00:00
