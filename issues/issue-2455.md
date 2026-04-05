---
title: 'Compiling failed on huawei y6 s (ARM cortex-A53) - error: this header is for
  x86 only'
source_url: https://github.com/xmrig/xmrig/issues/2455
author: TheStef56
assignees: []
labels: []
created_at: '2021-06-25T10:20:14+00:00'
updated_at: '2021-07-05T13:27:58+00:00'
type: issue
status: closed
closed_at: '2021-07-05T13:27:58+00:00'
---

# Original Description
**Describe the bug**
I tried to compile xmrig on my huawei y6 s on termux, but it failed. 

**To Reproduce**
try to compile with make on huawei y6 s (with termux)

**Expected behavior**
compile to 100%

**Required data**
this is the output :

Consolidate compiler generated dependencies of target ethash
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  2%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  2%] Linking C static library libethash.a
[  2%] Built target ethash
Consolidate compiler generated dependencies of target argon2
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  6%] Linking C static library libargon2.a
[  6%] Built target argon2
Consolidate compiler generated dependencies of target xmrig
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 40%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 40%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 41%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/CpuWorker.cpp:32:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:41:58: warning: 'ms_abi' calling convention is not supported for this target [-Wignored-attributes]
typedef void(*cn_mainloop_fun_ms_abi)(cryptonight_ctx**) ABI_ATTRIBUTE;
                                                         ^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:36:41: note: expanded from macro 'ABI_ATTRIBUTE'
#   define ABI_ATTRIBUTE __attribute__((ms_abi))
                                        ^
1 warning generated.
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:14:2: error: this header is for x86 only
#error this header is for x86 only
 ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:286:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, __eax, __ebx, __ecx, __edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:251:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:301:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:251:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:315:5: error: invalid output constraint '=a' in asm
    __cpuid_count(__leaf, __subleaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:258:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:74:5: error: invalid output constraint '=a' in asm
    __cpuid_count(level, 0, output[0], output[1], output[2], output[3]);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:258:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:132:36: error: invalid output constraint '=a' in asm
    __asm__ __volatile__("xgetbv": "=a"(eax_reg), "=d"(edx_reg) : "c"(0) : "cc");
                                   ^
6 errors generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1224: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2


 - Config file or command line (without wallets)
 - OS: skin, EMUI 9.0, android 9.
 - For GPU related issues: ARM cortex-A53

**Additional context**
Could somebody tell me how to avoid this compilation problem, please?

# Discussion History
## Spudz76 | 2021-06-25T17:11:43+00:00
It should detect properly but you can force ARM with cmake option `-DARM_TARGET=8` and it may work properly then.

Dump entire cache (build folder) first or it will probably mix up the x86 vs ARM8 configuration.

Not sure if clang is known to work on ARM, gcc definitely does.

## TheStef56 | 2021-06-25T17:25:40+00:00
> It should detect properly but you can force ARM with cmake option `-DARM_TARGET=8` and it may work properly then.
> 
> Dump entire cache (build folder) first or it will probably mix up the x86 vs ARM8 configuration.
> 
> Not sure if clang is known to work on ARM, gcc definitely does.

First of all, thanks for having replied. I already tried to compile with - DARM_TARGET=8 (also tried with - DARM_TARGET=7), but i got another error: "use of undeclared identifier 'HWCAP_AES'". Another guy had the same error and opened an issue, nobody could tell how to fix it. Xmrig gave two options in order to fix the error, but both didn't work. 


## ghost | 2021-06-25T22:12:06+00:00
Try with this single command might help

pkg update -y && pkg upgrade -y && pkg install -y wget nano git cmake clang libuv automake libtool autoconf && git clone https://github.com/xmrig/xmrig.git && mkdir xmrig/build && cd xmrig/build && cmake .. -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig


## TheStef56 | 2021-06-25T22:14:39+00:00
> Try with this single command might help
> 
> pkg update -y && pkg upgrade -y && pkg install -y wget nano git cmake clang libuv automake libtool autoconf && git clone https://github.com/xmrig/xmrig.git && mkdir xmrig/build && cd xmrig/build && cmake .. -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig

Thanks very much, I'll try as soon as possibile. 

## TheStef56 | 2021-06-26T19:42:44+00:00
> Try with this single command might help
> 
> pkg update -y && pkg upgrade -y && pkg install -y wget nano git cmake clang libuv automake libtool autoconf && git clone https://github.com/xmrig/xmrig.git && mkdir xmrig/build && cd xmrig/build && cmake .. -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig

this is my output:

[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12clang-12: : warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  8%] Linking C static library libethash.a
[  8%] Built target ethash
[  8%] Linking C static library libargon2.a
[  8%] Built target argon2
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/3rdparty/fmt/format.cc.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Coin.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Algorithm.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Async.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/sha3.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/keccak.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Env.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/FileLogWriter.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Tags.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Signals.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/Title.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecords.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsUvBackend.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/NetworkState.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/ProxyUrl.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Socks5.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/LineReader.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/NetBuffer.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Cvt.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/AutoClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/EthStratumClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.cpp:19:
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:111:13: warning: private field 'm_request' is not used [-Wunused-private-field]
    Request m_request           = NO_REQUEST;
            ^
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:123:14: warning: private field 'm_startTime' is not used [-Wunused-private-field]
    uint64_t m_startTime        = 0;
             ^
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/Benchmark.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/BenchState.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
2 warnings generated.
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:14:2: error: this header is for x86 only
#error this header is for x86 only
 ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:286:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, __eax, __ebx, __ecx, __edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:251:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:301:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:251:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:315:5: error: invalid output constraint '=a' in asm
    __cpuid_count(__leaf, __subleaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:258:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:74:5: error: invalid output constraint '=a' in asm
    __cpuid_count(level, 0, output[0], output[1], output[2], output[3]);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:258:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:132:36: error: invalid output constraint '=a' in asm
    __asm__ __volatile__("xgetbv": "=a"(eax_reg), "=d"(edx_reg) : "c"(0) : "cc");
                                   ^
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/CpuWorker.cpp:32:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:41:58: warning: 'ms_abi' calling convention is not supported for this target [-Wignored-attributes]
typedef void(*cn_mainloop_fun_ms_abi)(cryptonight_ctx**) ABI_ATTRIBUTE;
                                                         ^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:36:41: note: expanded from macro 'ABI_ATTRIBUTE'
#   define ABI_ATTRIBUTE __attribute__((ms_abi))
                                        ^
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
6 errors generated.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:986: CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.cpp:20:
/data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.h:43:10: warning: private field 'm_opencl' is not used [-Wunused-private-field]
    bool m_opencl           = false;
         ^
/data/data/com.termux/files/home/xmrig/src/net/JobResults.cpp:296:16: warning: private field 'm_hwAES' is not used [-Wunused-private-field]
    const bool m_hwAES;
               ^
1 warning generated.
1 warning generated.
1 warning generated.
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

## SChernykh | 2021-06-26T19:47:17+00:00
Show the full output of your cmake command, especially any lines having ARM_TARGET in it.

## TheStef56 | 2021-06-26T21:58:45+00:00
> Show the full output of your cmake command, especially any lines having ARM_TARGET in it.

this is the full output

~ $ pkg update -y && pkg upgrade -y && pkg install -y wget nano git cmake clang libuv automake libtool autoconf && git clone https://github.com/xmrig/xmrig.git && mkdir xmrig/build && cd xmrig/build && cmake .. -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig
Checking availability of current mirror: ok
Hit:1 https://packages.termux.org/apt/termux-games games InRelease
0% [Waiting for headers]
Hit:3 https://packages.termux.org/apt/termux-root root InRelease
Hit:2 https://packages.kcubeterm.me/apt/termux-main stable InRelease
Hit:4 https://packages.termux.org/apt/termux-science science InRelease
Hit:5 https://packages.termux.org/apt/termux-unstable unstable InRelease
Hit:6 https://packages.termux.org/apt/termux-x11 x11 InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Checking availability of current mirror: ok
Hit:1 https://packages.termux.org/apt/termux-games games InRelease
Hit:2 https://packages.termux.org/apt/termux-root root InRelease
Hit:3 https://packages.termux.org/apt/termux-science science InRelease
Hit:5 https://packages.termux.org/apt/termux-unstable unstable InRelease
Hit:6 https://packages.termux.org/apt/termux-x11 x11 InRelease
Hit:4 https://packages.kcubeterm.me/apt/termux-main stable InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Checking availability of current mirror: ok
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
autoconf is already the newest version (2.71).
automake is already the newest version (1.16.3-1).
clang is already the newest version (12.0.0-1).
cmake is already the newest version (3.20.5).
git is already the newest version (2.32.0).
libtool is already the newest version (2.4.6-8).
libuv is already the newest version (1.41.0).
nano is already the newest version (5.7).
wget is already the newest version (1.21.1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Cloning into 'xmrig'...
remote: Enumerating objects: 23764, done.
remote: Total 23764 (delta 0), reused 0 (delta 0), pack-reused 23764
Receiving objects: 100% (23764/23764), 9.73 MiB | 1.84 MiB/s, done.
Resolving deltas: 100% (17539/17539), done.
-- The C compiler identification is Clang 12.0.0
-- The CXX compiler identification is Clang 12.0.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for _rotr
-- Looking for _rotr - not found
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrig/build
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  2%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  2%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  8%] Linking C static library libethash.a
[  8%] Built target ethash
[  8%] Linking C static library libargon2.a
[  8%] Built target argon2
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/3rdparty/fmt/format.cc.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Algorithm.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/keccak.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Coin.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/sha3.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Async.cpp.o
clang-12clang-12: : warningwarning: : argument unused during compilation: '-maes' [-Wunused-command-line-argument]argument unused during compilation: '-maes' [-Wunused-command-line-argument]

clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12clang-12: : warningwarning: : argument unused during compilation: '-maes' [-Wunused-command-line-argument]argument unused during compilation: '-maes' [-Wunused-command-line-argument]

clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Env.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/FileLogWriter.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Tags.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Signals.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/Title.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsConfig.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecords.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsUvBackend.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/NetworkState.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/ProxyUrl.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Socks5.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/LineReader.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/NetBuffer.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Cvt.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/AutoClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/EthStratumClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.cpp:19:
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:111:13: warning: private field 'm_request' is not used [-Wunused-private-field]
    Request m_request           = NO_REQUEST;
            ^
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:123:14: warning: private field 'm_startTime' is not used [-Wunused-private-field]
    uint64_t m_startTime        = 0;
             ^
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/Benchmark.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/BenchState.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
2 warnings generated.
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:14:2: error: this header is for x86 only
#error this header is for x86 only
 ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:286:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, __eax, __ebx, __ecx, __edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:251:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:301:5: error: invalid output constraint '=a' in asm
    __cpuid(__leaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:251:11: note: expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:315:5: error: invalid output constraint '=a' in asm
    __cpuid_count(__leaf, __subleaf, *__eax, *__ebx, *__ecx, *__edx);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:258:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:74:5: error: invalid output constraint '=a' in asm
    __cpuid_count(level, 0, output[0], output[1], output[2], output[3]);
    ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/cpuid.h:258:11: note: expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(__ecx), "=d"(__edx) \
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:132:36: error: invalid output constraint '=a' in asm
    __asm__ __volatile__("xgetbv": "=a"(eax_reg), "=d"(edx_reg) : "c"(0) : "cc");
                                   ^
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/CpuWorker.cpp:32:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:41:58: warning: 'ms_abi' calling convention is not supported for this target [-Wignored-attributes]
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
typedef void(*cn_mainloop_fun_ms_abi)(cryptonight_ctx**) ABI_ATTRIBUTE;
                                                         ^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight.h:36:41: note: expanded from macro 'ABI_ATTRIBUTE'
#   define ABI_ATTRIBUTE __attribute__((ms_abi))
                                        ^
6 errors generated.
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:986: CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
clang-12: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.cpp:20:
/data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.h:43:10: warning: private field 'm_opencl' is not used [-Wunused-private-field]
    bool m_opencl           = false;
         ^
1 warning generated.
1 warning generated.
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

## SChernykh | 2021-06-26T22:25:22+00:00
You should add `-DARM_TARGET=8` to cmake command line and replace https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo_arm.cpp#L79 with
```
m_flags.set(FLAG_AES, false);
```
Or you can try `m_flags.set(FLAG_AES, true);` if you're sure your CPU has AES support.

## TheStef56 | 2021-06-26T22:27:20+00:00
> You should add `-DARM_TARGET=8` to cmake command line and replace https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo_arm.cpp#L79 with
> 
> ```
> m_flags.set(FLAG_AES, false);
> ```
> 
> Or you can try `m_flags.set(FLAG_AES, true);` if you're sure your CPU has AES support.

I'll try, thanks a lot for your help

## dytra | 2021-07-04T20:22:32+00:00
any update on this ?

## TheStef56 | 2021-07-04T22:46:05+00:00
> any update on this ?

Sorry, I had no time to try...tomorrow I will try to compile with that change and will post the result 

## TheStef56 | 2021-07-05T07:44:48+00:00
this is the output with m_flags.set(FLAG_AES, false);

~/xmrig/build $ cmake .. -DARM_TARGET=8 -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig
-- Use ARM_TARGET=8 (armv8l)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrig/build
Consolidate compiler generated dependencies of target ethash
Consolidate compiler generated dependencies of target argon2
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  6%] Linking C static library libethash.a
[  6%] Built target ethash
[  7%] Linking C static library libargon2.a
[  7%] Built target argon2
Consolidate compiler generated dependencies of target xmrig-notls
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Algorithm.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/sha3.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Async.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/3rdparty/fmt/format.cc.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/keccak.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Coin.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Env.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/FileLogWriter.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Tags.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Signals.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/Title.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsConfig.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecords.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/NetworkState.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Socks5.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/LineReader.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/NetBuffer.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Cvt.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 45%] Building C object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 46%] Building C object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/AutoClient.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/Benchmark.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.cpp:19:
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:111:13: warning: private field 'm_request' is not used [-Wunused-private-field]
    Request m_request           = NO_REQUEST;
            ^
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:123:14: warning: private field 'm_startTime' is not used [-Wunused-private-field]
    uint64_t m_startTime        = 0;
             ^
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
2 warnings generated.
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.cpp:20:
/data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.h:43:10: warning: private field 'm_opencl' is not used [-Wunused-private-field]
    bool m_opencl           = false;
         ^
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
1 warning generated.
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
/data/data/com.termux/files/home/xmrig/src/net/JobResults.cpp:296:16: warning: private field 'm_hwAES' is not used [-Wunused-private-field]
    const bool m_hwAES;
               ^
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o
1 warning generated.
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process_unix.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 70%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o
[ 70%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o
[ 71%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o
[ 72%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CnHash.cpp:37:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight_arm.h:35:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/soft_aes.h:31:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:122:2: error: "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
#error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 ^
[ 79%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7029:32: error: use of undeclared identifier 'vreinterpret_p64_u64'; did you mean 'vreinterpret_s64_u64'?
    poly64_t a = vget_lane_p64(vreinterpret_p64_u64(_a), 0);
                               ^~~~~~~~~~~~~~~~~~~~
                               vreinterpret_s64_u64
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/arm_neon.h:33595:16: note: 'vreinterpret_s64_u64' declared here
__ai int64x1_t vreinterpret_s64_u64(uint64x1_t __p0) {
               ^
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CnHash.cpp:37:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight_arm.h:35:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/soft_aes.h:31:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7029:18: error: use of undeclared identifier 'vget_lane_p64'
    poly64_t a = vget_lane_p64(vreinterpret_p64_u64(_a), 0);
                 ^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7030:32: error: use of undeclared identifier 'vreinterpret_p64_u64'; did you mean 'vreinterpret_s64_u64'?
    poly64_t b = vget_lane_p64(vreinterpret_p64_u64(_b), 0);
                               ^~~~~~~~~~~~~~~~~~~~
                               vreinterpret_s64_u64
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/arm_neon.h:33595:16: note: 'vreinterpret_s64_u64' declared here
__ai int64x1_t vreinterpret_s64_u64(uint64x1_t __p0) {
               ^
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CnHash.cpp:37:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight_arm.h:35:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/soft_aes.h:31:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7030:18: error: use of undeclared identifier 'vget_lane_p64'
    poly64_t b = vget_lane_p64(vreinterpret_p64_u64(_b), 0);
                 ^
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7031:35: error: use of undeclared identifier 'vmull_p64'; did you mean 'vmull_p8'?
    return vreinterpretq_u64_p128(vmull_p64(a, b));
                                  ^~~~~~~~~
                                  vmull_p8
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/arm_neon.h:16795:17: note: 'vmull_p8' declared here
__ai poly16x8_t vmull_p8(poly8x8_t __p0, poly8x8_t __p1) {
                ^
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CnHash.cpp:37:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight_arm.h:35:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/soft_aes.h:31:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7031:45: error: cannot initialize a parameter of type 'poly8x8_t' (vector of 8 'poly8_t' values) with an lvalue of type 'poly64_t' (aka 'long long')
    return vreinterpretq_u64_p128(vmull_p64(a, b));
                                            ^
/data/data/com.termux/files/usr/lib/clang/12.0.0/include/arm_neon.h:16795:36: note: passing argument to parameter '__p0' here
__ai poly16x8_t vmull_p8(poly8x8_t __p0, poly8x8_t __p1) {
                                   ^
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o
[ 82%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler.hpp:36:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: warning: class 'ProgramConfiguration' was previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note: previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: note: did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
[ 87%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:282:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(IADD_RS, NULL);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:38: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:282:2: error: no member named 'engine' in 'randomx::JitCompilerFallback'
        INST_HANDLE(IADD_RS, NULL);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:54: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~~~~~~~~~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:282:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(IADD_RS, NULL);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:76: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:282:2: error: no member named 'h_IADD_RS' in 'randomx::JitCompilerFallback'
        INST_HANDLE(IADD_RS, NULL);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:92: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~^
<scratch space>:71:1: note: expanded from here
h_IADD_RS
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:283:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(IADD_M, IADD_RS);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:38: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:283:2: error: no member named 'engine' in 'randomx::JitCompilerFallback'
        INST_HANDLE(IADD_M, IADD_RS);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:54: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~~~~~~~~~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:283:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(IADD_M, IADD_RS);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:76: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:283:2: error: no member named 'h_IADD_M' in 'randomx::JitCompilerFallback'
        INST_HANDLE(IADD_M, IADD_RS);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:92: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~^
<scratch space>:73:1: note: expanded from here
h_IADD_M
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:284:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(ISUB_R, IADD_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:38: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:284:2: error: no member named 'engine' in 'randomx::JitCompilerFallback'
        INST_HANDLE(ISUB_R, IADD_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:54: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~~~~~~~~~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:284:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(ISUB_R, IADD_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:76: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:284:2: error: no member named 'h_ISUB_R' in 'randomx::JitCompilerFallback'
        INST_HANDLE(ISUB_R, IADD_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:92: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~^
<scratch space>:75:1: note: expanded from here
h_ISUB_R
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:285:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(ISUB_M, ISUB_R);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:38: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:285:2: error: no member named 'engine' in 'randomx::JitCompilerFallback'
        INST_HANDLE(ISUB_M, ISUB_R);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:54: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~~~~~~~~~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:285:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(ISUB_M, ISUB_R);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:76: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:285:2: error: no member named 'h_ISUB_M' in 'randomx::JitCompilerFallback'
        INST_HANDLE(ISUB_M, ISUB_R);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:92: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~^
<scratch space>:77:1: note: expanded from here
h_ISUB_M
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:286:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(IMUL_R, ISUB_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:38: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:286:2: error: no member named 'engine' in 'randomx::JitCompilerFallback'
        INST_HANDLE(IMUL_R, ISUB_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:54: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                            ~~~~~~~~~~~~~~~~~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:286:2: error: no member named 'JitCompilerA64' in namespace 'randomx'; did you mean 'JitCompiler'?
        INST_HANDLE(IMUL_R, ISUB_M);
        ^~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:276:30: note: expanded from macro 'INST_HANDLE'
        for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                                    ^~~~~~~~~~~~~~~~~~~
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:265:76: note: expanded from macro 'JIT_HANDLE'
#define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                  ~~~~~~~~~^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/common.hpp:117:8: note: 'JitCompiler' declared here
        using JitCompiler = JitCompilerFallback;
              ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
1 warning and 20 errors generated.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1532: CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
7 errors generated.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1364: CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o] Error 1
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled_light.cpp:31:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled_light.hpp:32:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler.hpp:36:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: warning: class 'ProgramConfiguration' was previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note: previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: note: did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.cpp:31:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler.hpp:36:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: warning: class 'ProgramConfiguration' was previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note: previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: note: did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
1 warning generated.
1 warning generated.
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:91: all] Error 2


> any update on this ?



## ghost | 2021-07-05T08:38:41+00:00
Not supporting devices only works on armv7 and armv8

## TheStef56 | 2021-07-05T12:46:58+00:00
> Not supporting devices only works on armv7 and armv8

So my device is not supported and there is no chance I can compile xmrig on that device? 

## ghost | 2021-07-05T12:53:37+00:00
You can verify by excute this command 
lscpu 

If armv7 or above mostly possible 
If below than 7 not possible 

## TheStef56 | 2021-07-05T12:56:19+00:00
> You can verify by excute this command
> lscpu
> 
> If armv7 or above mostly possible
> If below than 7 not possible

It's armv8l

## ghost | 2021-07-05T12:57:32+00:00
Could you share the screenshot 

## TheStef56 | 2021-07-05T13:04:43+00:00
> Could you share the screenshot

![Screenshot_20210705_150135_com termux](https://user-images.githubusercontent.com/68242764/124475828-760dfa00-dda2-11eb-9c88-53d662729223.jpg)


## ghost | 2021-07-05T13:08:35+00:00
Cool now replace the darmtarget from 8 to 7 and try if can compile 

## TheStef56 | 2021-07-05T13:20:49+00:00
> Cool now replace the darmtarget from 8 to 7 and try if can compile

~/xmrig/build $ cmake .. -DARM_TARGET=7 -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig
-- The C compiler identification is Clang 12.0.0
-- The CXX compiler identification is Clang 12.0.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=7 (armv8l)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrig/build
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  5%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  6%] Linking C static library libethash.a
[  6%] Built target ethash
[  7%] Linking C static library libargon2.a
[  7%] Built target argon2
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Algorithm.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/3rdparty/fmt/format.cc.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Coin.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Async.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/keccak.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/sha3.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Env.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/FileLogWriter.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Tags.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Signals.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/Title.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsConfig.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecords.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/NetworkState.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Socks5.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/LineReader.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/NetBuffer.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Cvt.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 45%] Building C object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 46%] Building C object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/AutoClient.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/Benchmark.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.cpp:19:
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:111:13: warning: private field 'm_request' is not used [-Wunused-private-field]
    Request m_request           = NO_REQUEST;
            ^
/data/data/com.termux/files/home/xmrig/src/base/net/stratum/benchmark/BenchClient.h:123:14: warning: private field 'm_startTime' is not used [-Wunused-private-field]
    uint64_t m_startTime        = 0;
             ^
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
2 warnings generated.
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.cpp:20:
/data/data/com.termux/files/home/xmrig/src/core/config/ConfigTransform.h:43:10: warning: private field 'm_opencl' is not used [-Wunused-private-field]
    bool m_opencl           = false;
         ^
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o
/data/data/com.termux/files/home/xmrig/src/net/JobResults.cpp:296:16: warning: private field 'm_hwAES' is not used [-Wunused-private-field]
    const bool m_hwAES;
               ^
1 warning generated.
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o
1 warning generated.
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process_unix.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 70%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o
[ 70%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o
[ 71%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o
[ 72%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CnHash.cpp:37:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/CryptoNight_arm.h:35:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/cn/soft_aes.h:31:
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:122:2: error: "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
#error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 ^
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 79%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o
/data/data/com.termux/files/home/xmrig/src/crypto/cn/sse2neon.h:7303:9: warning: array designators are a C99 extension [-Wc99-designator]
        [0] = {SSE2NEON_sbox[vreinterpretq_nth_u8_m128i(a, 0)],
        ^~~
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o
[ 82%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.cpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler.hpp:36:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: warning: class 'ProgramConfiguration' was previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note: previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: note: did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
1 warning and 1 error generated.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1364: CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled_light.cpp:31:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled_light.hpp:32:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler.hpp:36:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: warning: class 'ProgramConfiguration' was previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note: previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: note: did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
1 warning generated.
1 warning generated.
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.cpp:31:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compiled.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler.hpp:36:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: warning: class 'ProgramConfiguration' was previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note: previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_fallback.hpp:41:2: note: did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
1 warning generated.
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:91: all] Error 2


## ghost | 2021-07-05T13:25:59+00:00
Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A.
So no point trying anymore :(

## TheStef56 | 2021-07-05T13:27:51+00:00
> Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A.
> So no point trying anymore :(

F. I'll close the issue, thanks for your help ; ) 

# Action History
- Created by: TheStef56 | 2021-06-25T10:20:14+00:00
- Closed at: 2021-07-05T13:27:58+00:00
