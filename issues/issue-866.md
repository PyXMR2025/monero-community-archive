---
title: Compile xmrig with 32-bit MSYS2, run .exe, prompting the computer to lose libwinpthred-1.dll
source_url: https://github.com/xmrig/xmrig/issues/866
author: ghost
assignees: []
labels:
- question
created_at: '2018-11-02T14:25:54+00:00'
updated_at: '2018-11-03T07:36:51+00:00'
type: issue
status: closed
closed_at: '2018-11-02T15:56:14+00:00'
---

# Original Description
z@z-PC MINGW32 /c/xmrig-2.8.3/build
# "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x86 -DWITH_HTTPD=OFF
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: C:/msys32/mingw32/bin/cc.exe
-- Check for working C compiler: C:/msys32/mingw32/bin/cc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys32/mingw32/bin/c++.exe
-- Check for working CXX compiler: C:/msys32/mingw32/bin/c++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: C:/msys32/mingw32/lib/libuv.a
-- Found OpenSSL: C:/msys32/mingw32/lib/libcrypto.a (found version "1.1.1")
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Configuring done
-- Generating done
-- Build files have been written to: C:/xmrig-2.8.3/build

z@z-PC MINGW32 /c/xmrig-2.8.3/build
# make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.obj
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.obj
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.obj
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.obj
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.obj
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.obj
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.obj
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 78%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/App_win.cpp.obj
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_win.cpp.obj
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_win.cpp.obj
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.obj
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.obj
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.obj
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.obj
[ 94%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.obj
[ 96%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.obj
[100%] Linking CXX executable xmrig.exe
[100%] Built target xmrig


# Discussion History
## xmrig | 2018-11-02T14:47:34+00:00
```
-- Found UV: C:/msys32/mingw32/lib/libuv.a
-- Found OpenSSL: C:/msys32/mingw32/lib/libcrypto.a (found version "1.1.1")
```
Libraries from MSYS2 not from xmrig-deps, please double check path.

## ghost | 2018-11-02T15:30:28+00:00
> 
> 
> ```
> -- Found UV: C:/msys32/mingw32/lib/libuv.a
> -- Found OpenSSL: C:/msys32/mingw32/lib/libcrypto.a (found version "1.1.1")
> ```
> 
> Libraries from MSYS2 not from xmrig-deps, please double check path.


 "C:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=C:\xmrig-deps-3.3\gcc\x86  -DWITH_HTTPD=OFF
![snipaste_2018-11-02_08-33-25](https://user-images.githubusercontent.com/32661990/47924899-d795b080-def7-11e8-8e83-2095a1dabe6a.png)


cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x86  -DWITH_HTTPD=OFF
![snipaste_2018-11-02_08-39-53](https://user-images.githubusercontent.com/32661990/47925265-bd100700-def8-11e8-93d5-21f984235d18.png)


![snipaste_2018-11-02_08-35-58](https://user-images.githubusercontent.com/32661990/47925028-1f1c3c80-def8-11e8-83ab-5c71edef1bb4.png)







-- Found UV: C:/msys32/mingw32/lib/libuv.a
-- Found OpenSSL: C:/msys32/mingw32/lib/libcrypto.a (found version "1.1.1")
wht？

## xmrig | 2018-11-02T15:45:18+00:00
`C:\xmrig-deps-3.3\gcc\x86` <- it's wrong.
`C:/xmrig-deps-3.3/gcc/x86` <- it's OK.

## ghost | 2018-11-02T15:55:59+00:00
> 
> 
> `C:\xmrig-deps-3.3\gcc\x86` <- it's wrong.
> `C:/xmrig-deps-3.3/gcc/x86` <- it's OK.
# cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=C:/xmrig-deps-3.3/gcc/x86  -DWITH_HTTPD=OFF
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: C:/msys32/mingw32/bin/cc.exe
-- Check for working C compiler: C:/msys32/mingw32/bin/cc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys32/mingw32/bin/c++.exe
-- Check for working CXX compiler: C:/msys32/mingw32/bin/c++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: C:/xmrig-deps-3.3/gcc/x86/lib/libuv.a
-- Found OpenSSL: C:/xmrig-deps-3.3/gcc/x86/lib/libcrypto.a (found version "1.1.1")
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Configuring done
-- Generating done
-- Build files have been written to: C:/xmrig-2.8.3/build

z@z-PC MINGW32 /c/xmrig-2.8.3/build
# make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.obj
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.obj
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.obj
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.obj
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.obj
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.obj
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.obj
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 78%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/App_win.cpp.obj
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_win.cpp.obj
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_win.cpp.obj
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.obj
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.obj
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.obj
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.obj
[ 94%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.obj
[ 96%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.obj
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.obj
[100%] Linking CXX executable xmrig.exe
[100%] Built target xmrig



The problem is solved thanks.

## ghost | 2018-11-02T16:47:28+00:00
> 
> 
> `C:\xmrig-deps-3.3\gcc\x86` <- it's wrong.
> `C:/xmrig-deps-3.3/gcc/x86` <- it's OK.

Compiling with MSYS2, performance is 10% higher than Microsoft Visual Studio.
Is this result normal?

## xmrig | 2018-11-03T07:36:51+00:00
Yes it expected.

# Action History
- Created by: ghost | 2018-11-02T14:25:54+00:00
- Closed at: 2018-11-02T15:56:14+00:00
