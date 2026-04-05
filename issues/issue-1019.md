---
title: Error building on 2.14.x
source_url: https://github.com/xmrig/xmrig/issues/1019
author: jhony23008
assignees: []
labels:
- arm
- review later
created_at: '2019-05-02T23:37:39+00:00'
updated_at: '2020-02-09T10:38:54+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:38:54+00:00'
---

# Original Description
Hello , i'm trying to compile xmrig for arm64 and i got this error , on previus version 2.13.1 and 2.13.0 compile without problem but now on version 2.14.x i got error , please help me.


Task :libuv:generateJsonModelRelease
Variant=release ABI=arm64-v8a :-- Check for working C compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
Variant=release ABI=arm64-v8a :-- Check for working C compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang -- works
Variant=release ABI=arm64-v8a :-- Detecting C compiler ABI info
Variant=release ABI=arm64-v8a :-- Detecting C compiler ABI info - done
Variant=release ABI=arm64-v8a :-- Detecting C compile features
Variant=release ABI=arm64-v8a :-- Detecting C compile features - done
Variant=release ABI=arm64-v8a :-- Check for working CXX compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++
Variant=release ABI=arm64-v8a :-- Check for working CXX compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ -- works
Variant=release ABI=arm64-v8a :-- Detecting CXX compiler ABI info
Variant=release ABI=arm64-v8a :-- Detecting CXX compiler ABI info - done
Variant=release ABI=arm64-v8a :-- Detecting CXX compile features
Variant=release ABI=arm64-v8a :-- Detecting CXX compile features - done
Variant=release ABI=arm64-v8a :-- Configuring done
Variant=release ABI=arm64-v8a :-- Generating done
Variant=release ABI=arm64-v8a :CMake Warning:
Variant=release ABI=arm64-v8a :  Manually-specified variables were not used by the project:
Variant=release ABI=arm64-v8a :    OUTPUT_DIR
Variant=release ABI=arm64-v8a :-- Build files have been written to: mypath/libuv/.externalNativeBuild/cmake/release/arm64-v8a

> Task :libuv:externalNativeBuildRelease
Build uv arm64-v8a
[1/34] Building C object CMakeFiles/uv.dir/src/fs-poll.c.o
[2/34] Building C object CMakeFiles/uv.dir/src/inet.c.o
[3/34] Building C object CMakeFiles/uv.dir/src/threadpool.c.o
[4/34] Building C object CMakeFiles/uv.dir/src/timer.c.o
[5/34] Building C object CMakeFiles/uv.dir/src/uv-common.c.o
[6/34] Building C object CMakeFiles/uv.dir/src/version.c.o
[7/34] Building C object CMakeFiles/uv.dir/src/uv-data-getter-setters.c.o
[8/34] Building C object CMakeFiles/uv.dir/src/unix/async.c.o
[9/34] Building C object CMakeFiles/uv.dir/src/unix/core.c.o
[10/34] Building C object CMakeFiles/uv.dir/src/unix/dl.c.o
[11/34] Building C object CMakeFiles/uv.dir/src/unix/fs.c.o
[12/34] Building C object CMakeFiles/uv.dir/src/unix/getaddrinfo.c.o
[13/34] Building C object CMakeFiles/uv.dir/src/unix/getnameinfo.c.o
[14/34] Building C object CMakeFiles/uv.dir/src/unix/loop-watcher.c.o
[15/34] Building C object CMakeFiles/uv.dir/src/unix/loop.c.o
[16/34] Building C object CMakeFiles/uv.dir/src/unix/pipe.c.o
[17/34] Building C object CMakeFiles/uv.dir/src/unix/poll.c.o
[18/34] Building C object CMakeFiles/uv.dir/src/unix/process.c.o
[19/34] Building C object CMakeFiles/uv.dir/src/unix/signal.c.o
[20/34] Building C object CMakeFiles/uv.dir/src/unix/stream.c.o
[21/34] Building C object CMakeFiles/uv.dir/src/unix/tcp.c.o
[22/34] Building C object CMakeFiles/uv.dir/src/unix/thread.c.o
[23/34] Building C object CMakeFiles/uv.dir/src/unix/tty.c.o
[24/34] Building C object CMakeFiles/uv.dir/src/unix/udp.c.o
[25/34] Building C object CMakeFiles/uv.dir/src/unix/android-ifaddrs.c.o
[26/34] Building C object CMakeFiles/uv.dir/src/unix/linux-core.c.o
[27/34] Building C object CMakeFiles/uv.dir/src/unix/linux-inotify.c.o
[28/34] Building C object CMakeFiles/uv.dir/src/unix/linux-syscalls.c.o
[29/34] Building C object CMakeFiles/uv.dir/src/unix/procfs-exepath.c.o
[30/34] Building C object CMakeFiles/uv.dir/src/unix/pthread-fixes.c.o
[31/34] Building C object CMakeFiles/uv.dir/src/unix/sysinfo-loadavg.c.o
[32/34] Building C object CMakeFiles/uv.dir/src/unix/sysinfo-memory.c.o
[33/34] Building C object CMakeFiles/uv.dir/src/unix/proctitle.c.o
[34/34] Linking C shared library mypath/libuv/build/intermediates/cmake/release/obj/arm64-v8a/libuv.so

> Task :libuv:copyDeps

> Task :app:compileReleaseJavaWithJavac
Note: Some input files use or override a deprecated API.
Note: Recompile with -Xlint:deprecation for details.

> Task :app:generateJsonModelRelease
Variant=release ABI=arm64-v8a :-- Check for working C compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
Variant=release ABI=arm64-v8a :-- Check for working C compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang -- works
Variant=release ABI=arm64-v8a :-- Detecting C compiler ABI info
Variant=release ABI=arm64-v8a :-- Detecting C compiler ABI info - done
Variant=release ABI=arm64-v8a :-- Detecting C compile features
Variant=release ABI=arm64-v8a :-- Detecting C compile features - done
Variant=release ABI=arm64-v8a :-- Check for working CXX compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++
Variant=release ABI=arm64-v8a :-- Check for working CXX compiler: mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ -- works
Variant=release ABI=arm64-v8a :-- Detecting CXX compiler ABI info
Variant=release ABI=arm64-v8a :-- Detecting CXX compiler ABI info - done
Variant=release ABI=arm64-v8a :-- Detecting CXX compile features
Variant=release ABI=arm64-v8a :-- Detecting CXX compile features - done
Variant=release ABI=arm64-v8a :-- Use ARM_TARGET=8 (aarch64)
Variant=release ABI=arm64-v8a :-- Performing Test XMRIG_ARM_CRYPTO
Variant=release ABI=arm64-v8a :-- Performing Test XMRIG_ARM_CRYPTO - Success
Variant=release ABI=arm64-v8a :-- Found UV: mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a  
Variant=release ABI=arm64-v8a :-- Found OpenSSL: mypath/openssl/arm64-v8a/lib/libssl.a;mypath/openssl/arm64-v8a/lib/libcrypto.a (found version "1.0.2o") 
Variant=release ABI=arm64-v8a :-- Looking for syslog.h
Variant=release ABI=arm64-v8a :-- Looking for syslog.h - found
Variant=release ABI=arm64-v8a :-- Configuring done
Variant=release ABI=arm64-v8a :-- Generating done
Variant=release ABI=arm64-v8a :-- Build files have been written to: mypath/app/.externalNativeBuild/cmake/release/arm64-v8a

> Task :app:externalNativeBuildRelease
Build xmrig arm64-v8a
[1/54] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[2/54] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[3/54] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o
[4/54] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[5/54] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o
[6/54] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[7/54] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[8/54] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[9/54] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o
[10/54] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[11/54] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[12/54] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o
[13/54] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[14/54] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
[15/54] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
[16/54] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[17/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[18/54] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[19/54] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[20/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
[21/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[22/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[23/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[24/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
[25/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[26/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[27/54] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[28/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[29/54] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[30/54] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[31/54] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[32/54] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[33/54] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[34/54] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[35/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[36/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
[37/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[38/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[39/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
[40/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[41/54] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[42/54] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[43/54] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[44/54] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
[45/54] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[46/54] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o
[47/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[48/54] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o
[49/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[50/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[51/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[52/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
[53/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[54/54] Linking CXX executable xmrig
FAILED: : && mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  --target=aarch64-none-linux-android21 --gcc-toolchain=mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/sysroot  -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,--noexecstack -Wformat -Werror=format-security -stdlib=libc++ -std=gnu++11 -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -march=armv8-a+crypto -O2 -DNDEBUG  -Ofast -funroll-loops -fmerge-all-constants  -Wl,--exclude-libs,libgcc.a -Wl,--exclude-libs,libatomic.a -static-libstdc++ -Wl,--build-id -Wl,--warn-shared-textrel -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments -Wl,-z,noexecstack -Wl,-z,relro -Wl,-z,now -Wl,--gc-sections CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o CMakeFiles/xmrig.dir/src/App.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o CMakeFiles/xmrig.dir/src/common/Console.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o CMakeFiles/xmrig.dir/src/common/Platform.cpp.o CMakeFiles/xmrig.dir/src/core/Config.cpp.o CMakeFiles/xmrig.dir/src/core/Controller.cpp.o CMakeFiles/xmrig.dir/src/Mem.cpp.o CMakeFiles/xmrig.dir/src/net/Network.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig.dir/src/Summary.cpp.o CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o CMakeFiles/xmrig.dir/src/xmrig.cpp.o CMakeFiles/xmrig.dir/src/App_unix.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o  -o xmrig  mypath/openssl/arm64-v8a/lib/libssl.a mypath/openssl/arm64-v8a/lib/libcrypto.a mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a -latomic -ldl -latomic -lm && :
mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a: undefined reference to `__register_atfork@LIBC'
mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a: undefined reference to `stderr@LIBC'
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.

> Task :app:externalNativeBuildRelease FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:externalNativeBuildRelease'.
> Build command failed.
  Error while executing process mypath/cmake/3.6.4111459/bin/cmake with arguments {--build mypath/app/.externalNativeBuild/cmake/release/arm64-v8a --target xmrig}
  [1/54] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
  [2/54] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
  [3/54] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o
  [4/54] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
  [5/54] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o
  [6/54] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
  [7/54] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
  [8/54] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
  [9/54] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o
  [10/54] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
  [11/54] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
  [12/54] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o
  [13/54] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
  [14/54] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
  [15/54] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
  [16/54] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
  [17/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
  [18/54] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
  [19/54] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
  [20/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
  [21/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
  [22/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
  [23/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
  [24/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
  [25/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
  [26/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
  [27/54] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
  [28/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
  [29/54] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
  [30/54] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
  [31/54] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
  [32/54] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
  [33/54] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
  [34/54] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
  [35/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
  [36/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
  [37/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
  [38/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
  [39/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
  [40/54] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
  [41/54] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
  [42/54] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
  [43/54] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
  [44/54] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
  [45/54] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
  [46/54] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o
  [47/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
  [48/54] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o
  [49/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
  [50/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
  [51/54] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
  [52/54] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
  [53/54] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
  [54/54] Linking CXX executable xmrig
  FAILED: : && mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  --target=aarch64-none-linux-android21 --gcc-toolchain=mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=mypath/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/sysroot  -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,--noexecstack -Wformat -Werror=format-security -stdlib=libc++ -std=gnu++11 -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -march=armv8-a+crypto -O2 -DNDEBUG  -Ofast -funroll-loops -fmerge-all-constants  -Wl,--exclude-libs,libgcc.a -Wl,--exclude-libs,libatomic.a -static-libstdc++ -Wl,--build-id -Wl,--warn-shared-textrel -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments -Wl,-z,noexecstack -Wl,-z,relro -Wl,-z,now -Wl,--gc-sections CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o CMakeFiles/xmrig.dir/src/App.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o CMakeFiles/xmrig.dir/src/common/Console.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o CMakeFiles/xmrig.dir/src/common/Platform.cpp.o CMakeFiles/xmrig.dir/src/core/Config.cpp.o CMakeFiles/xmrig.dir/src/core/Controller.cpp.o CMakeFiles/xmrig.dir/src/Mem.cpp.o CMakeFiles/xmrig.dir/src/net/Network.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig.dir/src/Summary.cpp.o CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o CMakeFiles/xmrig.dir/src/xmrig.cpp.o CMakeFiles/xmrig.dir/src/App_unix.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o  -o xmrig  mypath/openssl/arm64-v8a/lib/libssl.a mypath/openssl/arm64-v8a/lib/libcrypto.a mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a -latomic -ldl -latomic -lm && :
  mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a: undefined reference to `__register_atfork@LIBC'
  mypath/app/src/main/cpp/xmrig-2.14.1/src/libs/arm64-v8a/libuv.a: undefined reference to `stderr@LIBC'
  clang++: error: linker command failed with exit code 1 (use -v to see invocation)
  ninja: build stopped: subcommand failed.

# Discussion History
# Action History
- Created by: jhony23008 | 2019-05-02T23:37:39+00:00
- Closed at: 2020-02-09T10:38:54+00:00
