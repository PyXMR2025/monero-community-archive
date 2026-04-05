---
title: Error to compile
source_url: https://github.com/xmrig/xmrig/issues/220
author: LearnMiner
assignees: []
labels: []
created_at: '2017-11-26T13:43:41+00:00'
updated_at: '2018-03-14T23:27:50+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:27:50+00:00'
---

# Original Description
Im trying compile but i have this error 
MainAkali@DESKTOP-CP6SQRM MINGW64 ~/CMakefiles/xmrig.dir/build
$ cmake .. -G "Visual Studio 15 2017 Win64" -DUV_INCLUDE_DIR="c:\<path>\msvc2017\libuv\x64\include" -DUV_LIBRARY="c:\<path>\msvc2017\libuv\x64\lib\libuv.lib" -DMHD_INCLUDE_DIR="c:\<path>\msvc2017\libmicrohttpd\x64\include" -DMHD_LIBRARY="c:\<path>\msvc2017\libmicrohttpd\x64\lib\libmicrohttpd.lib"
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.



CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.



-- Configuring incomplete, errors occurred!
See also "C:/msys64/home/MainAkali/CMakeFiles/xmrig.dir/build/CMakeFiles/CMakeOutput.log".
See also "C:/msys64/home/MainAkali/CMakeFiles/xmrig.dir/build/CMakeFiles/CMakeError.log".
Im using mingw64.exe

# Discussion History
## dunklesToast | 2017-11-26T17:09:07+00:00
`No CMAKE_C_COMPILER could be found.`

You simply have no CMAKE Compiler installed. To fix this under Windows you can install VisualStudio from Microsoft. This should have a compiler included. Then restart the Session and try it again!

- dunklesToast

## LearnMiner | 2017-11-26T17:23:19+00:00
I use vs 2017 and i update all, and install CMAKE in vs2017 too 
![image](https://user-images.githubusercontent.com/34003340/33242537-de096f5c-d2d6-11e7-83be-f1c4e4a97822.png)


## dunklesToast | 2017-11-26T17:25:22+00:00
What happens if you just type `cmake ..` - could you please send the output?

## LearnMiner | 2017-11-26T17:42:07+00:00
now i have this error 

MainAkali@DESKTOP-CP6SQRM MINGW32 /home/mainakali
$ make
[ 12%] Built target cpuid
[ 14%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
El sistema no puede encontrar el archivo especificado.
C:\msys32\mingw32\bin\windres.exe: fall▒ el preprocesamiento.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:738: CMakeFiles/xmrig.dir/res/app.rc.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

MainAkali@DESKTOP-CP6SQRM MINGW32 /home/mainakali


if you want i can show my screen in teamviewer i need help

## dunklesToast | 2017-11-26T17:44:57+00:00
At least the `cmake ..` seems to help. Have you changed anything or is this the original XMRIG from the repo?

## LearnMiner | 2017-11-26T17:53:22+00:00
is original xmrig

## LearnMiner | 2017-11-26T17:58:33+00:00
i no change nothing bro

## LearnMiner | 2017-11-26T18:09:08+00:00
all time have this error in 32 and 64 bit

MainAkali@DESKTOP-CP6SQRM MINGW64 ~
$ cmake .. -G "Unix Makefiles" -DUV_INCLUDE_DIR="c:\<path>\gcc\libuv\x64\include" -DUV_LIBRARY="c:\<path>\gcc\libuv\x64\lib\libuv.a" -DMHD_INCLUDE_DIR="c:\<path>\gcc\libmicrohttpd\x64\include" -DMHD_LIBRARY="c:\<path>\gcc\libmicrohttpd\x64\lib\libmicrohttpd.a"

-- Configuring done
-- Generating done
-- Build files have been written to: C:/msys64/home/MainAkali

MainAkali@DESKTOP-CP6SQRM MINGW64 ~
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
El sistema no puede encontrar el archivo especificado.
C:\msys64\mingw64\bin\windres.exe: fall▒ el preprocesamiento.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:738: CMakeFiles/xmrig.dir/res/app.rc.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Action History
- Created by: LearnMiner | 2017-11-26T13:43:41+00:00
- Closed at: 2018-03-14T23:27:50+00:00
