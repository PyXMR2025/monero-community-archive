---
title: Can't build for armh architecture
source_url: https://github.com/xmrig/xmrig/issues/2085
author: Motsyo
assignees: []
labels: []
created_at: '2021-02-05T22:55:18+00:00'
updated_at: '2021-04-13T20:33:16+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:16:45+00:00'
---

# Original Description
OS - ALT Linux 9...
=========================================================
> [00:00:02] Building target platforms: armh
> [00:00:02] Building for target armh
> [00:00:02] Wrote: /usr/src/in/nosrpm/xmrig-6.8.1-alt2.1.nosrc.rpm (w1.gzdio)
> [00:00:05] Installing xmrig-6.8.1-alt2.1.src.rpm
> [00:00:05] Building target platforms: armh
> [00:00:05] Building for target armh
> [00:00:05] Executing(%prep): /bin/sh -e /usr/src/tmp/rpm-tmp.72817
> [00:00:05] + umask 022
> [00:00:05] + /bin/mkdir -p /usr/src/RPM/BUILD
> [00:00:05] + cd /usr/src/RPM/BUILD
> [00:00:05] + cd /usr/src/RPM/BUILD
> [00:00:05] + rm -rf xmrig
> [00:00:05] + echo 'Source #0 (xmrig.tar.xz):'
> [00:00:05] Source #0 (xmrig.tar.xz):
> [00:00:05] + /usr/bin/xz -dc /usr/src/RPM/SOURCES/xmrig.tar.xz
> [00:00:05] + /bin/tar -xf -
> [00:00:05] + cd xmrig
> [00:00:05] + /bin/chmod -c -Rf u+rwX,go-w .
> [00:00:05] + echo 'Patch #0 (xmrig-6.3.0-minimum_donate_0.diff):'
> [00:00:05] Patch #0 (xmrig-6.3.0-minimum_donate_0.diff):
> [00:00:05] + /usr/bin/patch -p1
> [00:00:05] patching file src/donate.h
> [00:00:05] + echo 'Patch #1 (xmrig-5.10.0-Wno-class-memaccess_alt_rm.diff):'
> [00:00:05] Patch #1 (xmrig-5.10.0-Wno-class-memaccess_alt_rm.diff):
> [00:00:05] + /usr/bin/patch -p1
> [00:00:05] patching file cmake/flags.cmake
> [00:00:05] + echo 'Patch #2 (xmrig-6.8.1-maes_armh.diff):'
> [00:00:05] Patch #2 (xmrig-6.8.1-maes_armh.diff):
> [00:00:05] + /usr/bin/patch -p1
> [00:00:05] patching file cmake/flags.cmake
> [00:00:05] + exit 0
> [00:00:05] Executing(%build): /bin/sh -e /usr/src/tmp/rpm-tmp.74980
> [00:00:05] + umask 022
> [00:00:05] + /bin/mkdir -p /usr/src/RPM/BUILD
> [00:00:05] + cd /usr/src/RPM/BUILD
> [00:00:05] + cd xmrig
> [00:00:05] + mkdir ./build
> [00:00:05] + cd ./build
> [00:00:05] + cmake ../. -DCMAKE_BUILD_TYPE=Release '-DCMAKE_CXX_FLAGS:STRING=-pipe -frecord-gcc-switches -Wall -g -O2 -fomit-frame-pointer -march=armv7-a -mthumb' '-DCMAKE_C_FLAGS:STRING=-pipe -frecord-gcc-switches -Wall -g -O2 -fomit-frame-pointer -march=armv7-a -mthumb' -DWITH_HWLOC=OFF -DWITH_EMBEDDED_CONFIG=ON
> [00:00:05] -- The C compiler identification is GNU 10.2.1
> [00:00:05] -- The CXX compiler identification is GNU 10.2.1
> [00:00:06] -- Detecting C compiler ABI info
> [00:00:06] -- Detecting C compiler ABI info - done
> [00:00:06] -- Check for working C compiler: /usr/bin/cc - skipped
> [00:00:06] -- Detecting C compile features
> [00:00:06] -- Detecting C compile features - done
> [00:00:06] -- Detecting CXX compiler ABI info
> [00:00:06] -- Detecting CXX compiler ABI info - done
> [00:00:06] -- Check for working CXX compiler: /usr/bin/c++ - skipped
> [00:00:06] -- Detecting CXX compile features
> [00:00:06] -- Detecting CXX compile features - done
> [00:00:06] -- Looking for syslog.h
> [00:00:06] -- Looking for syslog.h - found
> [00:00:06] -- Found UV: /usr/lib/libuv.so
> [00:00:06] -- Looking for __builtin___clear_cache
> [00:00:06] -- Looking for __builtin___clear_cache - found
> [00:00:06] -- WITH_MSR=OFF
> [00:00:06] -- Found OpenSSL: /usr/lib/libcrypto.so (found version "1.1.1i")
> [00:00:06] -- Configuring done
> [00:00:06] -- Generating done
> [00:00:06] -- Build files have been written to: /usr/src/RPM/BUILD/xmrig/build
> [00:00:06] + make -j64
> [00:00:06] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] Scanning dependencies of target ethash
> [00:00:06] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] Scanning dependencies of target argon2
> [00:00:06] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] [ 3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
> [00:00:06] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:06] [ 2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
> [00:00:06] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
> [00:00:07] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
> [00:00:07] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
> [00:00:07] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
> [00:00:07] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 4%] Linking C static library libethash.a
> [00:00:07] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[1]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 4%] Built target ethash
> [00:00:07] make[1]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:07] [ 1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
> [00:00:07] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:08] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:08] [ 3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
> [00:00:08] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 4%] Linking C static library libargon2.a
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[1]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 4%] Built target argon2
> [00:00:15] make[1]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] Scanning dependencies of target xmrig
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 6%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 5%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:15] [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
> [00:00:15] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
> [00:00:16] /usr/src/RPM/BUILD/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:13: fatal error: cpuid.h: No such file or directory
> [00:00:16] 29 | # include <cpuid.h>
> [00:00:16] | ^~~~~~~~~
> [00:00:16] compilation terminated.
> [00:00:16] make[2]: *** [CMakeFiles/xmrig.dir/build.make:1122: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: *** Waiting for unfinished jobs....
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:16] [ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
> [00:00:16] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
> [00:00:17] In file included from /usr/include/c++/10/vector:72,
> [00:00:17] from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuThreads.h:29,
> [00:00:17] from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuThreads.cpp:29:
> [00:00:17] /usr/include/c++/10/bits/vector.tcc: In member function 'void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocatorxmrig::CpuThread]':
> [00:00:17] /usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type 'std::vectorxmrig::CpuThread::iterator' changed in GCC 7.1
> [00:00:17] 426 | vector<_Tp, _Alloc>::
> [00:00:17] | ^~~~~~~~~~~~~~~~~~~
> [00:00:17] /usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type 'std::vectorxmrig::CpuThread::iterator' changed in GCC 7.1
> [00:00:17] In file included from /usr/include/c++/10/vector:67,
> [00:00:17] from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuThreads.h:29,
> [00:00:17] from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuThreads.cpp:29:
> [00:00:17] /usr/include/c++/10/bits/stl_vector.h: In constructor 'xmrig::CpuThreads::CpuThreads(size_t, uint32_t)':
> [00:00:17] /usr/include/c++/10/bits/stl_vector.h:1198:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vectorxmrig::CpuThread >' changed in GCC 7.1
> [00:00:17] 1198 | _M_realloc_insert(end(), __x);
> [00:00:17] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
> [00:00:17] /usr/include/c++/10/bits/stl_vector.h: In constructor 'xmrig::CpuThreads::CpuThreads(const Value&)':
> [00:00:17] /usr/include/c++/10/bits/stl_vector.h:1198:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vectorxmrig::CpuThread >' changed in GCC 7.1
> [00:00:17] 1198 | _M_realloc_insert(end(), __x);
> [00:00:17] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
> [00:00:17] /usr/include/c++/10/bits/stl_vector.h:1198:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vectorxmrig::CpuThread >' changed in GCC 7.1
> [00:00:17] 1198 | _M_realloc_insert(end(), __x);
> [00:00:17] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 26%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
> [00:00:17] In file included from /usr/include/c++/10/vector:72,
> [00:00:17] from /usr/src/RPM/BUILD/xmrig/src/base/net/stratum/Pools.h:29,
> [00:00:17] from /usr/src/RPM/BUILD/xmrig/src/base/net/stratum/Pools.cpp:26:
> [00:00:17] /usr/include/c++/10/bits/vector.tcc: In member function 'void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {std::shared_ptrxmrig::BenchConfig&}; _Tp = xmrig::Pool; _Alloc = std::allocatorxmrig::Pool]':
> [00:00:17] /usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type 'std::vectorxmrig::Pool::iterator' changed in GCC 7.1
> [00:00:17] 426 | vector<_Tp, _Alloc>::
> [00:00:17] | ^~~~~~~~~~~~~~~~~~~
> [00:00:17] /usr/include/c++/10/bits/vector.tcc: In member function 'void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocatorxmrig::Pool]':
> [00:00:17] /usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type 'std::vectorxmrig::Pool::iterator' changed in GCC 7.1
> [00:00:17] /usr/include/c++/10/bits/vector.tcc: In member function 'void xmrig::Pools::load(const xmrig::IJsonReader&)':
> [00:00:17] /usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vectorxmrig::Pool >' changed in GCC 7.1
> [00:00:17] 121 | _M_realloc_insert(end(), std::forward<_Args>(__args)...);
> [00:00:17] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
> [00:00:17] /usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vectorxmrig::Pool >' changed in GCC 7.1
> [00:00:17] 121 | _M_realloc_insert(end(), std::forward<_Args>(__args)...);
> [00:00:17] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:17] [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
> [00:00:17] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:18] [ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
> [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:18] [ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp: In static member function 'static xmrig::IWorker* xmrig::Workers::create(xmrig::Thread_) [with T = xmrig::CpuLaunchData]': [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:230:63: warning: 'new' of type 'xmrig::CpuWorker<1>' with extended alignment 16 [-Waligned-new=] [00:00:18] 230 | return new CpuWorker<1>(handle->id(), handle->config()); [00:00:18] | ^ [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:230:63: note: uses 'void_ operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:230:63: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:233:63: warning: 'new' of type 'xmrig::CpuWorker<2>' with extended alignment 16 [-Waligned-new=]
> [00:00:18] 233 | return new CpuWorker<2>(handle->id(), handle->config());
> [00:00:18] | ^
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:233:63: note: uses 'void* operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:233:63: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:236:63: warning: 'new' of type 'xmrig::CpuWorker<3>' with extended alignment 16 [-Waligned-new=]
> [00:00:18] 236 | return new CpuWorker<3>(handle->id(), handle->config());
> [00:00:18] | ^
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:236:63: note: uses 'void* operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:236:63: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:239:63: warning: 'new' of type 'xmrig::CpuWorker<4>' with extended alignment 16 [-Waligned-new=]
> [00:00:18] 239 | return new CpuWorker<4>(handle->id(), handle->config());
> [00:00:18] | ^
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:239:63: note: uses 'void* operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:239:63: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:242:63: warning: 'new' of type 'xmrig::CpuWorker<5>' with extended alignment 16 [-Waligned-new=]
> [00:00:18] 242 | return new CpuWorker<5>(handle->id(), handle->config());
> [00:00:18] | ^
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:242:63: note: uses 'void* operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:242:63: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp: In static member function 'static xmrig::IWorker* xmrig::Workers::create(xmrig::Thread_) [with T = xmrig::OclLaunchData]': [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:261:56: warning: 'new' of type 'xmrig::OclWorker' with extended alignment 16 [-Waligned-new=] [00:00:18] 261 | return new OclWorker(handle->id(), handle->config()); [00:00:18] | ^ [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:261:56: note: uses 'void_ operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:261:56: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp: In static member function 'static xmrig::IWorker* xmrig::Workers::create(xmrig::Thread_) [with T = xmrig::CudaLaunchData]': [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:273:57: warning: 'new' of type 'xmrig::CudaWorker' with extended alignment 16 [-Waligned-new=] [00:00:18] 273 | return new CudaWorker(handle->id(), handle->config()); [00:00:18] | ^ [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:273:57: note: uses 'void_ operator new(std::size_t)', which does not have an alignment parameter
> [00:00:18] /usr/src/RPM/BUILD/xmrig/src/backend/common/Workers.cpp:273:57: note: use '-faligned-new' to enable C++17 over-aligned new support
> [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:18] [ 9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
> [00:00:18] In file included from /usr/include/c++/10/vector:72,
> [00:00:18] from /usr/src/RPM/BUILD/xmrig/src/base/io/json/JsonChain.h:23,
> [00:00:18] from /usr/src/RPM/BUILD/xmrig/src/base/io/json/JsonChain.cpp:20:
> [00:00:18] /usr/include/c++/10/bits/vector.tcc: In member function 'void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8, rapidjson::MemoryPoolAllocatorrapidjson::CrtAllocator, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]':
> [00:00:18] /usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type 'std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > >::iterator' changed in GCC 7.1
> [00:00:18] 426 | vector<_Tp, _Alloc>::
> [00:00:18] | ^~~~~~~~~~~~~~~~~~~
> [00:00:18] /usr/include/c++/10/bits/vector.tcc: In member function 'bool xmrig::JsonChain::add(rapidjson::Document&&)':
> [00:00:18] /usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >_, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >' changed in GCC 7.1 [00:00:18] 121 | _M_realloc_insert(end(), std::forward<_Args>(__args)...); [00:00:18] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [00:00:18] /usr/include/c++/10/bits/vector.tcc: In member function 'bool xmrig::JsonChain::addFile(const char_)':
> [00:00:18] /usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >_, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >' changed in GCC 7.1 [00:00:18] 121 | _M_realloc_insert(end(), std::forward<_Args>(__args)...); [00:00:18] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [00:00:18] /usr/include/c++/10/bits/vector.tcc: In member function 'bool xmrig::JsonChain::addRaw(const char_)':
> [00:00:18] /usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >_, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >' changed in GCC 7.1 [00:00:18] 121 | _M_realloc_insert(end(), std::forward<_Args>(__args)...); [00:00:18] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:18] [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o [00:00:18] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] [ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o [00:00:19] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] [ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o [00:00:19] In file included from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuWorker.cpp:30: [00:00:19] /usr/src/RPM/BUILD/xmrig/src/crypto/cn/CryptoNight.h:36:48: warning: 'ms_abi' attribute directive ignored [-Wattributes] [00:00:19] 36 | # define ABI_ATTRIBUTE **attribute**((ms_abi)) [00:00:19] | ^ [00:00:19] /usr/src/RPM/BUILD/xmrig/src/crypto/cn/CryptoNight.h:41:58: note: in expansion of macro 'ABI_ATTRIBUTE' [00:00:19] 41 | typedef void(_cn_mainloop_fun_ms_abi)(cryptonight_ctx_*) ABI_ATTRIBUTE; [00:00:19] | ^~~~~~~~~~~~~ [00:00:19] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o [00:00:19] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o [00:00:19] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o [00:00:19] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:19] [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o [00:00:19] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:20] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build' [00:00:20] [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o [00:00:20] In file included from /usr/include/c++/10/vector:72, [00:00:20] from /usr/src/RPM/BUILD/xmrig/src/base/crypto/Algorithm.h:30, [00:00:20] from /usr/src/RPM/BUILD/xmrig/src/backend/common/Threads.h:34, [00:00:20] from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuConfig.h:23, [00:00:20] from /usr/src/RPM/BUILD/xmrig/src/backend/cpu/CpuConfig.cpp:20: [00:00:20] /usr/include/c++/10/bits/vector.tcc: In member function 'void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Miner_&, const xmrig::Algorithm&, const xmrig::CpuConfig&, const xmrig::CpuThread&, const unsigned int&}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocatorxmrig::CpuLaunchData]':
> [00:00:20] /usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type 'std::vectorxmrig::CpuLaunchData::iterator' changed in GCC 7.1
> [00:00:20] 426 | vector<_Tp, _Alloc>::
> [00:00:20] | ^~~~~~~~~~~~~~~~~~~
> [00:00:20] /usr/include/c++/10/bits/vector.tcc: In member function 'std::vectorxmrig::CpuLaunchData xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const':
> [00:00:20] /usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type '__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vectorxmrig::CpuLaunchData >' changed in GCC 7.1
> [00:00:20] 121 | _M_realloc_insert(end(), std::forward<_Args>(__args)...);
> [00:00:20] | ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
> [00:00:20] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:20] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:20] [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
> [00:00:20] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:22] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:22] [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
> [00:00:22] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:24] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:24] [ 5%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
> [00:00:24] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:27] make[2]: Entering directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:27] [ 9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
> [00:00:27] make[2]: Leaving directory '/usr/src/RPM/BUILD/xmrig/build'
> [00:00:27] make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/xmrig.dir/all] Error 2
> [00:00:27] make: *** [Makefile:103: all] Error 2
> [00:00:27] error: Bad exit status from /usr/src/tmp/rpm-tmp.74980 (%build)
=========================================================
All logs for armh build: http://git.altlinux.org/tasks/265866/build/100/armh/log
All logs for task build: http://git.altlinux.org/tasks/265866/

# Discussion History
## MaximoMachado | 2021-02-06T00:48:44+00:00
I'm also having a similar problem, although my errors are different. I attached a decent chunk of the error messages, but I can't figure out a way to copy them all and it was far too long to do manually.

Edit:
Nevermind, I was able to figure out how to get the entire error log. I should note this is on a Raspberry Pi 4.
[New Link is here](https://pastebin.com/46e82HjS)

## SChernykh | 2021-02-06T08:51:55+00:00
@MaximoMachado Only armv8 (64-bit) is supported, you need to use 64-bit OS and compiler.

## Tastyled | 2021-02-17T23:11:06+00:00
@SChernykh Raspberry Pi 4 is Arm v8 64bit

## MaximoMachado | 2021-02-17T23:13:04+00:00
@Tastyled Usually the Raspberry Pi 4 Kits will come with the 32 bit Raspbian OS installed on the sd instead of the 64 bit version.

## Motsyo | 2021-04-12T22:04:56+00:00
6.11.2 - http://git.altlinux.org/tasks/269784/build/100/armh/log

## SChernykh | 2021-04-12T22:08:02+00:00
`cpuid.h` not found. You should probably install libcpuid-devel package.

## Motsyo | 2021-04-13T20:31:33+00:00
> `cpuid.h` not found. You should probably install libcpuid-devel package.

Hmm... This package in ALT Linux does not contain the cpuid.h file. But on armh architecture at compilation this error arises. libcpuid-devel package contains the libcpuid.h file...

## Motsyo | 2021-04-13T20:33:16+00:00

[libcpuid.zip](https://github.com/xmrig/xmrig/files/6306560/libcpuid.zip)


# Action History
- Created by: Motsyo | 2021-02-05T22:55:18+00:00
- Closed at: 2021-04-12T14:16:45+00:00
