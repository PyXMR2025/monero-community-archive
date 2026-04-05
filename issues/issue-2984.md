---
title: Compiling issue on Raspberry Pi 4, Ubuntu 20.04
source_url: https://github.com/xmrig/xmrig/issues/2984
author: sscanavini
assignees: []
labels:
- duplicate
created_at: '2022-03-22T10:02:34+00:00'
updated_at: '2022-04-03T07:46:47+00:00'
type: issue
status: closed
closed_at: '2022-04-03T07:46:47+00:00'
---

# Original Description
Hi,
i paste here the results of the compilation, which I'm not able to finish, I have Ubuntu 64 installed with 64bit dependencies:

root@bytelighter:/home/phoenix# uname -a
Linux bytelighter 5.4.0-1052-raspi #58-Ubuntu SMP PREEMPT Mon Feb 7 16:52:35 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux


root@bytelighter:/home/phoenix# apt list git build-essential* cmake libuv1-dev* libssl-dev* libhw loc-dev* -i
Listing... Done
build-essential/focal-updates,now 12.8ubuntu1.1 arm64 [installed]
cmake/focal,now 3.16.3-1ubuntu1 arm64 [installed]
git/focal-updates,focal-security,now 1:2.25.1-1ubuntu3.2 arm64 [installed,automatic]
libssl-dev/focal-updates,focal-security,now 1.1.1f-1ubuntu2.12 arm64 [installed]
libuv1-dev/focal-updates,focal-security,now 1.34.2-1ubuntu1.3 arm64 [installed]

root@bytelighter:/home/phoenix/xmrig/build# cmake ..
-- The C compiler identification is GNU 9.4.0
-- The CXX compiler identification is GNU 9.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/aarch64-linux-gnu/libhwloc.so
-- Found UV: /usr/lib/aarch64-linux-gnu/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libcrypto.so (found version "1.1.1f")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/phoenix/xmrig/build


root@bytelighter:/home/phoenix/xmrig/build# make -j$(nproc)
Scanning dependencies of target argon2
Scanning dependencies of target ethash
Scanning dependencies of target ghostrider
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
[  1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
[  2%] Linking C static library libethash.a
[  2%] Built target ethash
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o
[  9%] Linking C static library libargon2.a
[  9%] Built target argon2
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o
[ 10%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
[ 10%] Linking CXX static library libghostrider.a
[ 10%] Built target ghostrider
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Chrono.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 29%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 29%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 33%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 33%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[ 34%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
In file included from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/home/phoenix/xmrig/src/crypto/randomx/randomx.h:160:1: error: template with C linkage
  160 | template<typename T>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
In file included from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:48:
/home/phoenix/xmrig/src/crypto/astrobwt/AstroBWT.h:37:1: error: template with C linkage
   37 | template<Algorithm::Id ALGO>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
In file included from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:48:
/home/phoenix/xmrig/src/crypto/astrobwt/AstroBWT.h:40:1: error: template specialization with C linkage
   40 | template<>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:71:1: error: template with C linkage
   71 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:109:1: error: template with C linkage
  109 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:132:1: error: template with C linkage
  132 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:156:1: error: template with C linkage
  156 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:236:1: error: template with C linkage
  236 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:244:1: error: template with C linkage
  244 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:379:1: error: template with C linkage
  379 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:398:1: error: template with C linkage
  398 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:442:1: error: template with C linkage
  442 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:471:1: error: template specialization with C linkage
  471 | template<>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:493:1: error: template with C linkage
  493 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:511:1: error: template with C linkage
  511 | template<size_t N>
      | ^~~~~~~~
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:550:1: error: expected ‘}’ at end of input
  550 | } // namespace xmrig
      | ^
In file included from /home/phoenix/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/phoenix/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/phoenix/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:12: note: to match this ‘{’
   33 | extern "C" {
      |            ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1233: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:140: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Discussion History
## SChernykh | 2022-03-22T14:38:37+00:00
Read https://github.com/xmrig/xmrig/issues/2978

## Spudz76 | 2022-03-22T20:11:32+00:00
A new package just dropped on focal-updates with version `9.4.0-1ubuntu1~20.04.1` that claims to fix this.  Previous version was same without the last `.1` (`9.4.0-1ubuntu1~20.04`)

Relevant [launchpad bug thread](https://bugs.launchpad.net/ubuntu/+source/gcc-9/+bug/1964260) -- it was crashing similarly in many other projects.

# Action History
- Created by: sscanavini | 2022-03-22T10:02:34+00:00
- Closed at: 2022-04-03T07:46:47+00:00
