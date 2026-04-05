---
title: question, cmake did nothing.
source_url: https://github.com/xmrig/xmrig/issues/858
author: sailei00
assignees: []
labels:
- question
created_at: '2018-10-30T14:20:58+00:00'
updated_at: '2018-11-03T01:56:16+00:00'
type: issue
status: closed
closed_at: '2018-11-02T15:06:24+00:00'
---

# Original Description
OS: windows    msys2 64bit
1. git clone https://github.com/xmrig/xmrig.git
2. mkdir build
3. cd build
4. cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64

here ,when i press the ENTER,it did nothing ,like this :

> wulei@wulei-T410 MINGW64 ~/xmrig/build
$ cmake .. -DXMRIG_DEPS=c:/xmrig-deps/gcc/x86
wulei@wulei-T410 MINGW64 ~/xmrig/build
$


why?and what's wrong?

# Discussion History
## snipeTR | 2018-10-31T22:36:22+00:00
![image](https://user-images.githubusercontent.com/31975916/47822535-8958a400-dd75-11e8-94f8-a77e794507d9.png)
download:https://github.com/xmrig/xmrig-deps/releases
![image](https://user-images.githubusercontent.com/31975916/47822687-113eae00-dd76-11e8-9c56-04704453e862.png)


## jiaxu2000 | 2018-11-01T07:37:29+00:00
do not use cmd shell, use msys2 shell

## snipeTR | 2018-11-01T10:15:40+00:00
Yes me to.. but look xmrig deps

## sailei00 | 2018-11-01T13:28:58+00:00
i put xmrig-deps in c:\   ,and execute 

> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64

i got nothing like before;

i copy xmrig-deps in c:\msys64 , and execute

> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=/xmrig-deps/gcc/x64

i got nothing too ,like before;

then ,i execute 

> cmake 

got nothing stills  …… 

i think the "cmake" looks like has some problem .

> 

## sailei00 | 2018-11-01T13:48:06+00:00
i found something.

> wulei@wulei-T410 MINGW64 /bin
$ **_whereis cmake_**
cmake: /usr/bin/cmake.exe /usr/share/cmake /mingw64/bin/cmake.exe /mingw32/bin/cmake.exe

oh ,i have 4 cmake,and i don't know which is the default one.
then :

> wulei@wulei-T410 MINGW64 ~/xmrig/build
$ _/usr/bin/cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=/xmrig-deps/gcc/x64_
-- The C compiler identification is GNU 8.2.0
-- The CXX compiler identification is GNU 8.2.0
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Check for working C compiler: /mingw64/bin/cc.exe
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Check for working C compiler: /mingw64/bin/cc.exe -- works
-- Detecting C compiler ABI info
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Detecting C compiler ABI info - done
-- Detecting C compile features
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Detecting C compile features - done
-- Check for working CXX compiler: /mingw64/bin/CC.exe
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Check for working CXX compiler: /mingw64/bin/CC.exe -- works
-- Detecting CXX compiler ABI info
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Detecting CXX compile features - done
-- Found UV: /xmrig-deps/gcc/x64/lib/libuv.a
-- Found OpenSSL: /xmrig-deps/gcc/x64/lib/libcrypto.a (found version "1.1.1")
-- The ASM compiler identification is GNU
-- Found assembler: /mingw64/bin/cc.exe
-- Looking for syslog.h
System is unknown to cmake, create:
Platform/MINGW64_NT-10.0 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Looking for syslog.h - not found
-- Found MHD: /xmrig-deps/gcc/x64/lib/libmicrohttpd.a
-- Configuring done
-- Generating done
-- Build files have been written to: /home/wulei/xmrig/build


and make:

> wulei@wulei-T410 MINGW64 ~/xmrig/build
$ _make_
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cnv2_main_loop.S.obj
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target cpuid
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 12%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 14%] Linking C static library libcpuid.a
[ 14%] Built target cpuid
Scanning dependencies of target xmrig
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.obj
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.obj
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.obj
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.obj
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.obj
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.obj
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.obj
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.obj
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.obj
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.obj
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.obj
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.obj
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.obj
C:/msys64/home/wulei/xmrig/src/App_unix.cpp: In member function 'void App::background()':
C:/msys64/home/wulei/xmrig/src/App_unix.cpp:39:12: error: 'SIGPIPE' was not declared in this scope
     signal(SIGPIPE, SIG_IGN);
            ^~~~~~~
C:/msys64/home/wulei/xmrig/src/App_unix.cpp:39:12: note: suggested alternative: 'SIGFPE'
     signal(SIGPIPE, SIG_IGN);
            ^~~~~~~
            SIGFPE
C:/msys64/home/wulei/xmrig/src/App_unix.cpp:45:13: error: 'fork' was not declared in this scope
     int i = fork();
             ^~~~
C:/msys64/home/wulei/xmrig/src/App_unix.cpp:45:13: note: suggested alternative: 'far'
     int i = fork();
             ^~~~
             far
C:/msys64/home/wulei/xmrig/src/App_unix.cpp:54:9: error: 'setsid' was not declared in this scope
     i = setsid();
         ^~~~~~
C:/msys64/home/wulei/xmrig/src/App_unix.cpp:54:9: note: suggested alternative: 'getpid'
     i = setsid();
         ^~~~~~
         getpid
make[2]: *** [CMakeFiles/xmrig.dir/build.make:479：CMakeFiles/xmrig.dir/src/App_unix.cpp.obj] 错误 1
make[1]: *** [CMakeFiles/Makefile2:111：CMakeFiles/xmrig.dir/all] 错误 2
make: *** [Makefile:84：all] 错误 2



i got some error,and i don't know what's that ,please help.

![image](https://user-images.githubusercontent.com/18213259/47855783-74851a80-de20-11e8-82ce-77ab376a0a31.png)


## xmrig | 2018-11-01T14:40:27+00:00
Something really messy.
1. Remove build directory and create again or remove all files inside build directory.
2. Install official CMake build from https://cmake.org/download/ and run `"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64` inside MSYS2 shell.

It might help. Compile errors above is because cmake think you use Linux.

## sailei00 | 2018-11-02T09:40:33+00:00
       thanks a lot ,it works.

# Action History
- Created by: sailei00 | 2018-10-30T14:20:58+00:00
- Closed at: 2018-11-02T15:06:24+00:00
