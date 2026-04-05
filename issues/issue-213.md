---
title: Error trying to build with MSVC2017
source_url: https://github.com/xmrig/xmrig/issues/213
author: coen800
assignees: []
labels:
- question
created_at: '2017-11-21T10:36:55+00:00'
updated_at: '2018-03-14T22:53:42+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:53:42+00:00'
---

# Original Description
Trying to build xmrig-cpu with MSVC 2017.
Latest cmake installed.
Xmrig-master is at C:/xmrig-master
build is in C:/xmrig-master/build
Deps are at C:/deps
I changed to release.
get this error: 1>------ Build started: Project: ZERO_CHECK, Configuration: Release x64 ------
1>Checking Build System
1>CMake does not need to re-run because C:/xmrig-master/build/CMakeFiles/generate.stamp is up-to-date.
1>CMake does not need to re-run because C:/xmrig-master/build/src/3rdparty/libcpuid/CMakeFiles/generate.stamp is up-to-date.
2>------ Build started: Project: cpuid, Configuration: Release x64 ------
2>Building Custom Rule C:/xmrig-master/src/3rdparty/libcpuid/CMakeLists.txt
2>CMake does not need to re-run because C:/xmrig-master/build/src/3rdparty/libcpuid/CMakeFiles/generate.stamp is up-to-date.
2>Assembling C:\xmrig-master\src\3rdparty\libcpuid\masm-x64.asm...
2>cpuid_main.c
2>asm-bits.c
2>recog_amd.c
2>recog_intel.c
2>libcpuid_util.c
2>LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
2>cpuid.vcxproj -> C:\xmrig-master\build\src\3rdparty\libcpuid\Release\cpuid.lib
3>------ Build started: Project: xmrig, Configuration: Release x64 ------
3>Building Custom Rule C:/xmrig-master/CMakeLists.txt
3>CMake does not need to re-run because C:/xmrig-master/build/CMakeFiles/generate.stamp is up-to-date.
3>Api.cpp
3>C:\xmrig-master\src\api/Api.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>ApiState.cpp
3>C:\xmrig-master\src\api\ApiState.cpp(26): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>NetworkState.cpp
3>C:\xmrig-master\src\api\NetworkState.cpp(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>App.cpp
3>C:\xmrig-master\src\App.cpp(26): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Console.cpp
3>c:\xmrig-master\src\Console.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>ConsoleLog.cpp
3>C:\xmrig-master\src\log/ConsoleLog.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>FileLog.cpp
3>C:\xmrig-master\src\log/FileLog.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Log.cpp
3>C:\xmrig-master\src\log/Log.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Mem.cpp
3>Client.cpp
3>C:\xmrig-master\src\log/Log.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Job.cpp
3>Network.cpp
3>C:\xmrig-master\src\api/Api.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>DonateStrategy.cpp
3>C:\xmrig-master\src\net/Client.h(29): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>FailoverStrategy.cpp
3>C:\xmrig-master\src\net/Client.h(29): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>SinglePoolStrategy.cpp
3>C:\xmrig-master\src\net/Client.h(29): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>SubmitResult.cpp
3>C:\xmrig-master\src\net\SubmitResult.cpp(25): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Url.cpp
3>Options.cpp
3>C:\xmrig-master\src\Options.cpp(26): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Platform.cpp
3>C:\xmrig-master\src\Platform.cpp(26): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Summary.cpp
3>C:\xmrig-master\src\Summary.cpp(27): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Compiling...
3>DoubleWorker.cpp
3>C:\xmrig-master\src\workers/Workers.h(30): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Handle.cpp
3>C:\xmrig-master\src\workers/Handle.h(29): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Hashrate.cpp
3>C:\xmrig-master\src\log/Log.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>SingleWorker.cpp
3>C:\xmrig-master\src\workers/Workers.h(30): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Worker.cpp
3>C:\xmrig-master\src\workers/Handle.h(29): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Workers.cpp
3>C:\xmrig-master\src\api/Api.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>xmrig.cpp
3>c:\xmrig-master\src\App.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>App_win.cpp
3>c:\xmrig-master\src\App.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Cpu_win.cpp
3>Mem_win.cpp
3>c:\xmrig-master\src\log/Log.h(28): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Platform_win.cpp
3>C:\xmrig-master\src\Platform_win.cpp(27): fatal error C1083: Cannot open include file: 'uv.h': No such file or directory
3>Cpu.cpp
3>CryptoNight.cpp
3>Done building project "xmrig.vcxproj" -- FAILED.
4>------ Build started: Project: ALL_BUILD, Configuration: Release x64 ------
4>Building Custom Rule C:/xmrig-master/CMakeLists.txt
4>CMake does not need to re-run because C:/xmrig-master/build/CMakeFiles/generate.stamp is up-to-date.
========== Build: 3 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========

I tried moving the deps folder everywhere even tried moving the uv.h file to xmrig-master/build doesn't work.
Help :(



# Discussion History
## xmrig | 2017-11-21T10:52:56+00:00
https://github.com/xmrig/xmrig/wiki/Windows-Build You need specify path to libuv when you run cmake. before sln file created.
Thank you.

## coen800 | 2017-11-21T13:50:33+00:00
Thanks for fast response.
Works now :)

## sh17156 | 2017-12-10T12:39:37+00:00
Hi, I have following error during make command. I am using 16.04 LTS ubuntu
root@sam08016-1:~/xmrig/build# make
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
g++-7: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-7/README.Bugs> for instructions.
CMakeFiles/xmrig.dir/build.make:278: recipe for target 'CMakeFiles/xmrig.dir/src/net/Client.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/net/Client.cpp.o] Error 4
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


# Action History
- Created by: coen800 | 2017-11-21T10:36:55+00:00
- Closed at: 2018-03-14T22:53:42+00:00
