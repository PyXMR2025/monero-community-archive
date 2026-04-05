---
title: 'Error building 2.13.x '
source_url: https://github.com/xmrig/xmrig/issues/961
author: jhony23008
assignees: []
labels:
- arm
created_at: '2019-03-01T01:07:25+00:00'
updated_at: '2019-03-02T20:39:35+00:00'
type: issue
status: closed
closed_at: '2019-03-02T20:30:19+00:00'
---

# Original Description
Hello , I have been getting trouble building xmrig the last version, previously i compile the version 2.8.3 without problem for arm , but now on the version 2.13.x don't compile anymore. please help me.

Variant=release ABI=arm64-v8a :-- Check for working C compiler: /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
Variant=release ABI=arm64-v8a :-- Check for working C compiler: /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang -- works
Variant=release ABI=arm64-v8a :-- Detecting C compiler ABI info
Variant=release ABI=arm64-v8a :-- Detecting C compiler ABI info - done
Variant=release ABI=arm64-v8a :-- Detecting C compile features
Variant=release ABI=arm64-v8a :-- Detecting C compile features - done
Variant=release ABI=arm64-v8a :-- Check for working CXX compiler: /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++
Variant=release ABI=arm64-v8a :-- Check for working CXX compiler: /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ -- works
Variant=release ABI=arm64-v8a :-- Detecting CXX compiler ABI info
Variant=release ABI=arm64-v8a :-- Detecting CXX compiler ABI info - done
Variant=release ABI=arm64-v8a :-- Detecting CXX compile features
Variant=release ABI=arm64-v8a :-- Detecting CXX compile features - done
Variant=release ABI=arm64-v8a :-- Use ARM_TARGET=8 (aarch64)
Variant=release ABI=arm64-v8a :-- Performing Test XMRIG_ARM_CRYPTO
Variant=release ABI=arm64-v8a :-- Performing Test XMRIG_ARM_CRYPTO - Success
Variant=release ABI=arm64-v8a :-- Found UV: /mypathapp/src/main/cpp/xmrig-2.13.0/src/libs/arm64-v8a/libuv.a  
Variant=release ABI=arm64-v8a :-- Found OpenSSL: /my_path/openssl/arm64-v8a/lib/libssl.a;/my_path/openssl/arm64-v8a/lib/libcrypto.a (found version "1.0.2o") 
Variant=release ABI=arm64-v8a :-- Looking for syslog.h
Variant=release ABI=arm64-v8a :-- Looking for syslog.h - found
Variant=release ABI=arm64-v8a :-- Configuring done
Variant=release ABI=arm64-v8a :-- Generating done
Variant=release ABI=arm64-v8a :-- Build files have been written to: /mypathapp/.externalNativeBuild/cmake/release/arm64-v8a


Build xmrig arm64-v8a
[1/55] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[2/55] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[3/55] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o
[4/55] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[5/55] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o
[6/55] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[7/55] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[8/55] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[9/55] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o
[10/55] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[11/55] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[12/55] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o
[13/55] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[14/55] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
[15/55] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
[16/55] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[17/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[18/55] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[19/55] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[20/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
[21/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[22/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[23/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[24/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
[25/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[26/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[27/55] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[28/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[29/55] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[30/55] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[31/55] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[32/55] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[33/55] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[34/55] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[35/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[36/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
[37/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[38/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[39/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
[40/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[41/55] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[42/55] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[43/55] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[44/55] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
[45/55] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[46/55] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o
[47/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[48/55] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o
[49/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[50/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[51/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[52/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
[53/55] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o
[54/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[55/55] Linking CXX executable xmrig
FAILED: : && /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  --target=aarch64-none-linux-android21 --gcc-toolchain=/home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=/home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/sysroot  -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,--noexecstack -Wformat -Werror=format-security -stdlib=libc++ -std=gnu++11 -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -march=armv8-a+crypto -O2 -DNDEBUG  -Ofast -funroll-loops -fmerge-all-constants  -Wl,--exclude-libs,libgcc.a -Wl,--exclude-libs,libatomic.a -static-libstdc++ -Wl,--build-id -Wl,--warn-shared-textrel -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments -Wl,-z,noexecstack -Wl,-z,relro -Wl,-z,now -Wl,--gc-sections CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o CMakeFiles/xmrig.dir/src/App.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o CMakeFiles/xmrig.dir/src/common/Console.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o CMakeFiles/xmrig.dir/src/common/Platform.cpp.o CMakeFiles/xmrig.dir/src/core/Config.cpp.o CMakeFiles/xmrig.dir/src/core/Controller.cpp.o CMakeFiles/xmrig.dir/src/Mem.cpp.o CMakeFiles/xmrig.dir/src/net/Network.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig.dir/src/Summary.cpp.o CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o CMakeFiles/xmrig.dir/src/xmrig.cpp.o CMakeFiles/xmrig.dir/src/App_unix.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o  -o xmrig  /my_path/openssl/arm64-v8a/lib/libssl.a /my_path/openssl/arm64-v8a/lib/libcrypto.a /mypathapp/src/main/cpp/xmrig-2.13.0/src/libs/arm64-v8a/libuv.a -lpthread -lrt -ldl -latomic -lm && :
/home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lpthread
/home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lrt

clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.



 Error while executing process /home/user/Sdk/cmake/3.6.4111459/bin/cmake with arguments {--build /mypathapp/.externalNativeBuild/cmake/release/arm64-v8a --target xmrig}
  [1/55] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
  [2/55] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
  [3/55] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o
  [4/55] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
  [5/55] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o
  [6/55] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
  [7/55] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
  [8/55] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
  [9/55] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o
  [10/55] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
  [11/55] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
  [12/55] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o
  [13/55] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
  [14/55] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
  [15/55] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
  [16/55] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
  [17/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
  [18/55] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
  [19/55] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
  [20/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
  [21/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
  [22/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
  [23/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
  [24/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
  [25/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
  [26/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
  [27/55] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
  [28/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
  [29/55] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
  [30/55] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
  [31/55] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
  [32/55] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
  [33/55] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
  [34/55] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
  [35/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
  [36/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
  [37/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
  [38/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
  [39/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
  [40/55] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
  [41/55] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
  [42/55] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
  [43/55] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
  [44/55] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
  [45/55] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
  [46/55] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o
  [47/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
  [48/55] Building CXX object CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o
  [49/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
  [50/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
  [51/55] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
  [52/55] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
  [53/55] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o
  [54/55] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
  [55/55] Linking CXX executable xmrig
  FAILED: : && /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  --target=aarch64-none-linux-android21 --gcc-toolchain=/home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=/home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/sysroot  -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,--noexecstack -Wformat -Werror=format-security -stdlib=libc++ -std=gnu++11 -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -march=armv8-a+crypto -O2 -DNDEBUG  -Ofast -funroll-loops -fmerge-all-constants  -Wl,--exclude-libs,libgcc.a -Wl,--exclude-libs,libatomic.a -static-libstdc++ -Wl,--build-id -Wl,--warn-shared-textrel -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments -Wl,-z,noexecstack -Wl,-z,relro -Wl,-z,now -Wl,--gc-sections CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o CMakeFiles/xmrig.dir/src/App.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o CMakeFiles/xmrig.dir/src/common/Console.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o CMakeFiles/xmrig.dir/src/common/Platform.cpp.o CMakeFiles/xmrig.dir/src/core/Config.cpp.o CMakeFiles/xmrig.dir/src/core/Controller.cpp.o CMakeFiles/xmrig.dir/src/Mem.cpp.o CMakeFiles/xmrig.dir/src/net/Network.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig.dir/src/Summary.cpp.o CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o CMakeFiles/xmrig.dir/src/xmrig.cpp.o CMakeFiles/xmrig.dir/src/App_unix.cpp.o CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/Cpu.cpp.o CMakeFiles/xmrig.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o  -o xmrig  /my_path/openssl/arm64-v8a/lib/libssl.a /my_path/openssl/arm64-v8a/lib/libcrypto.a /mypathapp/src/main/cpp/xmrig-2.13.0/src/libs/arm64-v8a/libuv.a -lpthread -lrt -ldl -latomic -lm && :
  /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lpthread
  /home/user/Sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lrt

  clang++: error: linker command failed with exit code 1 (use -v to see invocation)
  ninja: build stopped: subcommand failed.


# Discussion History
## xmrig | 2019-03-01T16:44:36+00:00
Try remove `pthread` and `rt` from this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L189
but v2.8 was also require these libraries.
Thank you.

## jhony23008 | 2019-03-02T20:26:39+00:00
ok, trank you, fixed .

# Action History
- Created by: jhony23008 | 2019-03-01T01:07:25+00:00
- Closed at: 2019-03-02T20:30:19+00:00
