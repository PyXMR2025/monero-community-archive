---
title: version 2.5.0    use MSYS2 64 bit compile on windows10 error
source_url: https://github.com/xmrig/xmrig/issues/448
author: netmebtc
assignees: []
labels: []
created_at: '2018-03-15T03:44:44+00:00'
updated_at: '2018-03-15T05:57:14+00:00'
type: issue
status: closed
closed_at: '2018-03-15T05:57:14+00:00'
---

# Original Description
$ cd xmrig-2.5.0/build

xjs@HPXJS MINGW64 /d/xmrig-2.5.0/build
$ cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=d:/xmrig-deps-3.0/gcc/x64
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
-- Found UV: D:/xmrig-deps-v2/gcc/libuv/x64/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Found MHD: D:/xmrig-deps-v2/gcc/libmicrohttpd/x64/lib/libmicrohttpd.a
-- Configuring done
-- Generating done
-- Build files have been written to: D:/xmrig-2.5.0/build

xjs@HPXJS MINGW64 /d/xmrig-2.5.0/build
$ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.obj
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.obj
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.obj
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.obj
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.obj
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 72%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/App_win.cpp.obj
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_win.cpp.obj
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_win.cpp.obj
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_win.cpp.obj
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.obj
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.obj
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.obj
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.obj
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.obj
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.obj
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.obj
[100%] Linking CXX executable xmrig.exe
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0\libstdc++.a(vterminate.o):(.text$_ZN9__                       gnu_cxx27__verbose_terminate_handlerEv+0x5b): undefined reference to `__imp___acrt_iob_func'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0\libstdc++.a(vterminate.o):(.text$_ZN9__                       gnu_cxx27__verbose_terminate_handlerEv+0xd7): undefined reference to `__imp___acrt_iob_func'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0\libstdc++.a(vterminate.o):(.text$_ZN9__                       gnu_cxx27__verbose_terminate_handlerEv+0x114): undefined reference to `__imp___acrt_iob_func'
collect2.exe: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1146：xmrig.exe] 错误 1
make[1]: *** [CMakeFiles/Makefile2:68：CMakeFiles/xmrig.dir/all] 错误 2
make: *** [Makefile:84：all] 错误 2


# Discussion History
## xmrig | 2018-03-15T04:29:13+00:00
Strange, did you update your MSYS2 to recent version via pacman?
Thank you.

## netmebtc | 2018-03-15T04:31:47+00:00
I have ran these command  on  my MSYS2

pacman -Sy
pacman -S mingw-w64-x86_64-gcc
pacman -S make
pacman -S mingw-w64-x86_64-cmake
pacman -S mingw-w64-x86_64-pkg-config

## netmebtc | 2018-03-15T04:36:07+00:00
I'm running "pacman -Syu"  now .  After it finish, I'll try build again.

## netmebtc | 2018-03-15T05:57:10+00:00
after update the MSYS2 to the recent version via pacman ,it's done ok. Thank you xmrig.

# Action History
- Created by: netmebtc | 2018-03-15T03:44:44+00:00
- Closed at: 2018-03-15T05:57:14+00:00
