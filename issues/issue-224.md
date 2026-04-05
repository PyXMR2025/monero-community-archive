---
title: Error when i compile XMRig
source_url: https://github.com/xmrig/xmrig/issues/224
author: LearnMiner
assignees: []
labels: []
created_at: '2017-11-27T20:25:40+00:00'
updated_at: '2018-03-14T23:28:45+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:28:45+00:00'
---

# Original Description
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
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.obj
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.obj
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.obj
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.obj
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.obj
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.obj
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.obj
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 70%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
El sistema no puede encontrar el archivo especificado.
C:\msys64\mingw32\bin\windres.exe: fall▒ el preprocesamiento.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:738: CMakeFiles/xmrig.dir/res/app.rc.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


please help me

# Discussion History
## xmrig | 2017-11-27T20:31:39+00:00
Remove this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L114 you just lose version information from exe file, nothing important. Other people sometimes also report this issue, but I can't reproduce it.
Thank you.

## LearnMiner | 2017-11-27T20:35:56+00:00
thanks but now i have this error

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.obj
C:/msys64/home/src/api/Httpd.cpp:25:10: fatal error: microhttpd.h: No such file or directory
 #include <microhttpd.h>
          ^~~~~~~~~~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1039: CMakeFiles/xmrig.dir/src/api/Httpd.cpp.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


## xmrig | 2017-11-27T20:44:28+00:00
https://github.com/xmrig/xmrig/wiki/Windows-Build run cmake with `-DWITH_HTTPD=OFF` to disable HTTP API or set proper path to microhttpd headers and library.

## LearnMiner | 2017-11-27T20:48:58+00:00
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
make[2]: *** No hay ninguna regla para construir el objetivo 'C:/<path>/gcc/libuv/x86/lib/libuv.a', necesario para 'xmrig.exe'.  Alto.
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


## LearnMiner | 2017-11-27T21:16:53+00:00
I downloaded xmrig-deps-v2  and put in C:/ all folder, and C:\msys64\home but same error :S

## Ekinox49 | 2017-11-30T23:20:05+00:00
Same problem here

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
make[2]: ***  No rules to make the target « C:/<path>/gcc/libuv/x64/lib/libuv.a », necessary to « xmrig.exe ». Stop.
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

Did you find the answer @LearnMiner  ?

## LearnMiner | 2017-12-01T10:59:22+00:00
No and they no help :(

## xmrig | 2017-12-01T11:12:35+00:00
You need replace `c:\<path>\` to actual path.
Thank you.

## LearnMiner | 2017-12-01T11:40:22+00:00
cmake .. -G "Unix Makefiles" -DUV_INCLUDE_DIR="c:\home\gcc\libuv\x64\include" -DUV_LIBRARY="c:\home\gcc\libuv\x64\lib\libuv.a" -DMHD_INCLUDE_DIR="c:\home\gcc\libmicrohttpd\x64\include" -DMHD_LIBRARY="c:\home\gcc\libmicrohttpd\x64\lib\libmicrohttpd.a" -DWITH_HTTPD=OFF
make
same error 

[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/soft_aes.c.obj
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
make[2]: *** No hay ninguna regla para construir el objetivo 'C:/home/gcc/libuv/x64/lib/libuv.a', necesario para 'xmrig.exe'.  Alto.
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


## Ekinox49 | 2017-12-01T17:42:42+00:00
After update the <path> with your already compiled deps, it Works !

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
[100%] Linking CXX executable xmrig.exe
[100%] Built target xmrig

Thanks to you and sorry for the inconvenience.

## chri121 | 2017-12-12T08:54:40+00:00
Hello, i got another problem: 

i compiled it with vs2017 and if I start the xmrig.exe, it closes right after the start without any error code.

I tried to debug it says "File: minkernel\crts\ucrt\src\appcrt\stdio\fdopen.cpp
Line 29
Expression: _osfile(fh) & FOPEN


# Action History
- Created by: LearnMiner | 2017-11-27T20:25:40+00:00
- Closed at: 2018-03-14T23:28:45+00:00
