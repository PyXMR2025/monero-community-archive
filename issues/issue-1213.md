---
title: v3.2.0 compile for arm8 termux android
source_url: https://github.com/xmrig/xmrig/issues/1213
author: bitcoin-hub
assignees: []
labels:
- arm
created_at: '2019-10-02T07:48:48+00:00'
updated_at: '2019-10-02T09:49:05+00:00'
type: issue
status: closed
closed_at: '2019-10-02T09:49:05+00:00'
---

# Original Description
$ cmake ..
-- Use ARM_TARGET=8 (aarch64)
-- Found HWLOC: /data/data/com.termux/files/usr/lib/libhwloc.so
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- Found OpenSSL: /data/data/com.termux/files/usr/lib/libcrypto.so (found version "1.1.1
d")
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrig/build
$ make
Scanning dependencies of target argon2
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argo
n2-arch.c.o
[  6%] Linking C static library libargon2.a
[  6%] Built target argon2
Scanning dependencies of target xmrig
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.
o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
/data/data/com.termux/files/home/xmrig/src/base/kernel/config/BaseConfig.cpp:107:56: war
ning:
      adding 'int' to a string does not append to the string [-Wstring-plus-int]
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                  ~~~~~~~~~~~~~~~~~~~~~^~~
/data/data/com.termux/files/home/xmrig/src/base/kernel/config/BaseConfig.cpp:107:56: not
e:
      use array indexing to silence this warning
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                                       ^
                                  &                    [  ]
1 warning generated.
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp
.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
/data/data/com.termux/files/home/xmrig/src/base/kernel/Entry.cpp:79:56: warning: adding
      'int' to a string does not append to the string [-Wstring-plus-int]
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                  ~~~~~~~~~~~~~~~~~~~~~^~~
/data/data/com.termux/files/home/xmrig/src/base/kernel/Entry.cpp:79:56: note: use array
      indexing to silence this warning
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                                       ^
                                  &                    [  ]
1 warning generated.
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/Failover
Strategy.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePo
olStrategy.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 32%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp
.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp
.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cp
p.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_ar
m.cpp.o
[ 65%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 66%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 67%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 68%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Coin.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/keccak.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/allocator.cpp:50:11: warning:
      class template 'AlignedAllocator' was previously declared as a struct template;
      this is valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
        template class AlignedAllocator<CacheLineSize>;
                 ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/allocator.hpp:36:9: note:
      previous use is here
        struct AlignedAllocator {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/allocator.cpp:50:11: note:
      did you mean struct here?
        template class AlignedAllocator<CacheLineSize>;
                 ^~~~~
                 struct
1 warning generated.
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_core.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_ref.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.
o
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.
o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable
.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.
cpp:31:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_inter
preted.hpp:34:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_machine.hpp:36:1: warn
ing:
      'randomx_vm' defined as a class here but previously declared as a struct; this is
      valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
class randomx_vm
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.h:54:9: note: did you
      mean class here?
typedef struct randomx_vm randomx_vm;
        ^~~~~~
        class
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.
cpp:33:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_comp
iler.hpp:34:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_a64.hpp:39:2: war
ning:
      class 'ProgramConfiguration' was previously declared as a struct; this is valid,
      but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note:
      previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_a64.hpp:39:2: not
e:
      did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
2 warnings generated.
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_
machine.cpp:32:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_machine.hpp:36:1: warn
ing:
      'randomx_vm' defined as a class here but previously declared as a struct; this is
      valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
class randomx_vm
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.h:54:9: note: did you
      mean class here?
typedef struct randomx_vm randomx_vm;
        ^~~~~~
        class
1 warning generated.
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp
.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led_light.cpp:29:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led_light.hpp:32:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.hpp:33:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_machine.hpp:36:1: warn
ing:
      'randomx_vm' defined as a class here but previously declared as a struct; this is
      valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
class randomx_vm
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.h:54:9: note: did you
      mean class here?
typedef struct randomx_vm randomx_vm;
        ^~~~~~
        class
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led_light.cpp:29:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led_light.hpp:32:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_comp
iler.hpp:34:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_a64.hpp:39:2: war
ning:
      class 'ProgramConfiguration' was previously declared as a struct; this is valid,
      but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note:
      previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_a64.hpp:39:2: not
e:
      did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
2 warnings generated.
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.cpp:29:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.hpp:33:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_machine.hpp:36:1: warn
ing:
      'randomx_vm' defined as a class here but previously declared as a struct; this is
      valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
class randomx_vm
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.h:54:9: note: did you
      mean class here?
typedef struct randomx_vm randomx_vm;
        ^~~~~~
        class
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.cpp:29:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_compi
led.hpp:34:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_comp
iler.hpp:34:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_a64.hpp:39:2: war
ning:
      class 'ProgramConfiguration' was previously declared as a struct; this is valid,
      but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
        class ProgramConfiguration;
        ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/program.hpp:38:9: note:
      previous use is here
        struct ProgramConfiguration {
               ^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/jit_compiler_a64.hpp:39:2: not
e:
      did you mean struct here?
        class ProgramConfiguration;
        ^~~~~
        struct
2 warnings generated.
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.
cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_inter
preted_light.cpp:29:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_inter
preted_light.hpp:32:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_inter
preted.hpp:34:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_machine.hpp:36:1: warn
ing:
      'randomx_vm' defined as a class here but previously declared as a struct; this is
      valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
class randomx_vm
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.h:54:9: note: did you
      mean class here?
typedef struct randomx_vm randomx_vm;
        ^~~~~~
        class
1 warning generated.
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_inter
preted.cpp:29:
In file included from /data/data/com.termux/files/home/xmrig/src/crypto/randomx/vm_inter
preted.hpp:34:
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/virtual_machine.hpp:36:1: warn
ing:
      'randomx_vm' defined as a class here but previously declared as a struct; this is
      valid, but may result in linker errors under the Microsoft C++ ABI
      [-Wmismatched-tags]
class randomx_vm
^
/data/data/com.termux/files/home/xmrig/src/crypto/randomx/randomx.h:54:9: note: did you
      mean class here?
typedef struct randomx_vm randomx_vm;
        ^~~~~~
        class
1 warning generated.
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_arm.cpp.o
[100%] Linking CXX executable xmrig
/data/data/com.termux/files/usr/bin/aarch64-linux-android-ld: CMakeFiles/xmrig.dir/src/b
ase/io/log/backends/SysLog.cpp.o: in function `android_polyfill_syslog(int, char const*,
...)':
SysLog.cpp:(.text+0x100): undefined reference to `__android_log_print'
/data/data/com.termux/files/usr/bin/aarch64-linux-android-ld: SysLog.cpp:(.text+0x13c):
undefined reference to `__android_log_vprint'
clang-8: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1724: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:78: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
$ clang -v
clang version 8.0.1 (tags/RELEASE_801/final)
Target: aarch64-unknown-linux-android
Thread model: posix
InstalledDir: /data/data/com.termux/files/usr/bin
$


# Discussion History
## xmrig | 2019-10-02T08:36:34+00:00
Use v4. Thank you.

## bitcoin-hub | 2019-10-02T09:49:05+00:00
Thank you. It worked.

# Action History
- Created by: bitcoin-hub | 2019-10-02T07:48:48+00:00
- Closed at: 2019-10-02T09:49:05+00:00
