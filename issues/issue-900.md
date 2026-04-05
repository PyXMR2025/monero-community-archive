---
title: Cannot build on x86 alpine why?
source_url: https://github.com/xmrig/xmrig/issues/900
author: MasterDeflate
assignees: []
labels: []
created_at: '2018-12-27T23:52:29+00:00'
updated_at: '2019-08-02T13:10:00+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:10:00+00:00'
---

# Original Description
Can you tell me why i cannot build with Alpine x86?

```
# cmake .. -DCMAKE_BUILD_TYPE=Release
 -DWITH_HTTPD=OFF -DWITH_TLS=OFF -DWITH_AEON=OFF  -DCMAKE_C_COMPILER=clang -DCMA
KE_CXX_COMPILER=clang++ -DCMAKE_EXE_LINKER_FLAGS="-static" -DUV_INCLUDE_DIR=/usr
/local/src/libuv/include -DUV_LIBRARY=/usr/local/src/libuv/build/libuv_a.a
-- The C compiler identification is Clang 5.0.1
-- The CXX compiler identification is Clang 5.0.1
-- Check for working C compiler: /usr/bin/clang
-- Check for working C compiler: /usr/bin/clang -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/clang++
-- Check for working CXX compiler: /usr/bin/clang++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/local/src/libuv/build/libuv_a.a
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/local/src/xmrig-2.8.3/build
alpine2018:/usr/local/src/xmrig-2.8.3/build# make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.c                                                                                                                                                              pp.o
/usr/local/src/xmrig-2.8.3/src/common/config/CommonConfig.cpp:177:9: warning:
      unused variable 'length' [-Wunused-variable]
    int length = 0;
        ^
1 warning generated.
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo.cpp.o
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::setEnabled(bool)':
/usr/local/src/xmrig-2.8.3/src/workers/Workers.cpp:(.text+0x38a): undefined reference to `__atomic_fetch_add_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::setJob(Job const&, bool)':
/usr/local/src/xmrig-2.8.3/src/workers/Workers.cpp:(.text+0x515): undefined reference to `__atomic_fetch_add_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::start(xmrig::Controller*)':
/usr/local/src/xmrig-2.8.3/src/workers/Workers.cpp:(.text+0x62c): undefined reference to `__atomic_store_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::stop()':
/usr/local/src/xmrig-2.8.3/src/workers/Workers.cpp:(.text+0xbd8): undefined reference to `__atomic_store_8'
CMakeFiles/xmrig.dir/src/net/Network.cpp.o: In function `Network::onPause(IStrategy*)':
/usr/local/src/xmrig-2.8.3/src/net/Network.cpp:(.text+0x8f1): undefined reference to `__atomic_fetch_add_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: In function `MultiWorker<1u>::start()':
/usr/local/src/xmrig-2.8.3/src/workers/MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x3c): undefined reference to `__atomic_load_8'
/usr/local/src/xmrig-2.8.3/src/workers/MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0xf5): undefined reference to `__atomic_load_8'
/usr/local/src/xmrig-2.8.3/src/workers/MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x120): undefined reference to `__atomic_load_8'
/usr/local/src/xmrig-2.8.3/src/workers/MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x168): undefined reference to `__atomic_load_8'
/usr/local/src/xmrig-2.8.3/src/workers/MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x2b3): undefined reference to `__atomic_load_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o:/usr/local/src/xmrig-2.8.3/src/workers/MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE10consumeJobEv[_ZN11MultiWorkerILj1EE10consumeJobEv]+0x4c): more undefined references to `__atomic_load_8' follow
CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o: In function `Worker::storeStats()':
/usr/local/src/xmrig-2.8.3/src/workers/Worker.cpp:(.text+0x129): undefined reference to `__atomic_store_8'
/usr/local/src/xmrig-2.8.3/src/workers/Worker.cpp:(.text+0x139): undefined reference to `__atomic_store_8'
clang-5.0: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [CMakeFiles/xmrig.dir/build.make:700: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

```

# Discussion History
## DeadManWalkingTO | 2019-03-17T15:41:47+00:00
Try to build the [latest XMRig version](https://github.com/xmrig/xmrig/releases/latest).
Does the issue still exist?
Feedback please.
Thank you!

## Spudz76 | 2019-03-18T16:26:52+00:00
Due to ancient clang trying to interoperate with ancient local glibc (before they became compatible), try adding flags to force the clang libraries as described [here](https://stackoverflow.com/q/28920489/2395052) and then those things will be found and link correctly (maybe even actually run, too)


# Action History
- Created by: MasterDeflate | 2018-12-27T23:52:29+00:00
- Closed at: 2019-08-02T13:10:00+00:00
