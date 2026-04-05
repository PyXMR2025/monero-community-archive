---
title: make error on raspi4
source_url: https://github.com/xmrig/xmrig/issues/2660
author: razer1337o
assignees: []
labels:
- bug
- arm
created_at: '2021-10-30T19:06:59+00:00'
updated_at: '2024-03-20T07:58:50+00:00'
type: issue
status: closed
closed_at: '2023-06-05T15:22:07+00:00'
---

# Original Description
Hello, i get error at 83% at make.
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j$(nproc)
start here ...
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.                                                  o
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2507: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/home/pi/xmrig/src/crypto/randomx/aes_hash.cpp: In lambda function:
/home/pi/xmrig/src/crypto/randomx/aes_hash.cpp:391:38: warning: requested alignment 16 is larger than 8 [-Wattributes]
           alignas(16) uint8_t hash[64] = {};
                                                    ^
/home/pi/xmrig/src/crypto/randomx/aes_hash.cpp:392:39: warning: requested alignment 16 is larger than 8 [-Wattributes]
           alignas(16) uint8_t state[64] = {};
                                                    ^
make[1]: *** [CMakeFiles/Makefile2:118: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

Thanks for help!

# Discussion History
## Spudz76 | 2021-10-30T21:15:47+00:00
The error was before where you copied.  Thanks to multi-threaded build (`-j` option) things keep happening after the actual thread that crashed (CnHash.cpp not aes_hash.cpp).

Shown are just warnings which wouldn't crash the build.

## razer1337o | 2021-10-31T11:35:31+00:00
ok i understand but can you provide me a solution?

## SChernykh | 2021-10-31T11:40:49+00:00
First we need to see the actual compilation error, right?

## sigkill | 2021-11-02T16:51:08+00:00
Similar error, if not the same error, on a 64 bit mode Pi Zero 2 W:

`root@zero-w-001:~/code/xmrig# cmake .
-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
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
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1d")
-- Configuring done
-- Generating done
-- Build files have been written to: /root/code/xmrig
root@zero-w-001:~/code/xmrig# make -j4
Scanning dependencies of target ethash
Scanning dependencies of target argon2
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  2%] Linking C static library libethash.a
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  3%] Built target ethash
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  4%] Linking C static library libargon2.a
[  4%] Built target argon2
Scanning dependencies of target xmrig
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/io/json/JsonChain.h:23,
                 from /root/code/xmrig/src/base/io/json/JsonChain.cpp:19:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > >::iterator’ {aka ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::add(rapidjson::Document&&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::addFile(const char*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::addRaw(const char*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/net/stratum/Pools.h:29,
                 from /root/code/xmrig/src/base/net/stratum/Pools.cpp:26:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {std::shared_ptr<xmrig::BenchConfig>&}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’} changed in GCC 7.1
/usr/include/c++/8/bits/vector.tcc: In member function ‘void xmrig::Pools::load(const xmrig::IJsonReader&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 24%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 24%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 28%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
/root/code/xmrig/src/backend/common/Workers.cpp: In static member function ‘static xmrig::IWorker* xmrig::Workers<T>::create(xmrig::Thread<T>*) [with T = xmrig::CpuLaunchData]’:
/root/code/xmrig/src/backend/common/Workers.cpp:229:63: warning: ‘new’ of type ‘xmrig::CpuWorker<1>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<1>(handle->id(), handle->config());
                                                               ^
/root/code/xmrig/src/backend/common/Workers.cpp:229:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:229:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/root/code/xmrig/src/backend/common/Workers.cpp:232:63: warning: ‘new’ of type ‘xmrig::CpuWorker<2>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<2>(handle->id(), handle->config());
                                                               ^
/root/code/xmrig/src/backend/common/Workers.cpp:232:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:232:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/root/code/xmrig/src/backend/common/Workers.cpp:235:63: warning: ‘new’ of type ‘xmrig::CpuWorker<3>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<3>(handle->id(), handle->config());
                                                               ^
/root/code/xmrig/src/backend/common/Workers.cpp:235:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:235:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/root/code/xmrig/src/backend/common/Workers.cpp:238:63: warning: ‘new’ of type ‘xmrig::CpuWorker<4>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<4>(handle->id(), handle->config());
                                                               ^
/root/code/xmrig/src/backend/common/Workers.cpp:238:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:238:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/root/code/xmrig/src/backend/common/Workers.cpp:241:63: warning: ‘new’ of type ‘xmrig::CpuWorker<5>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<5>(handle->id(), handle->config());
                                                               ^
/root/code/xmrig/src/backend/common/Workers.cpp:241:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:241:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/root/code/xmrig/src/backend/common/Workers.cpp: In static member function ‘static xmrig::IWorker* xmrig::Workers<T>::create(xmrig::Thread<T>*) [with T = xmrig::OclLaunchData]’:
/root/code/xmrig/src/backend/common/Workers.cpp:260:56: warning: ‘new’ of type ‘xmrig::OclWorker’ with extended alignment 16 [-Waligned-new=]
     return new OclWorker(handle->id(), handle->config());
                                                        ^
/root/code/xmrig/src/backend/common/Workers.cpp:260:56: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:260:56: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/root/code/xmrig/src/backend/common/Workers.cpp: In static member function ‘static xmrig::IWorker* xmrig::Workers<T>::create(xmrig::Thread<T>*) [with T = xmrig::CudaLaunchData]’:
/root/code/xmrig/src/backend/common/Workers.cpp:272:57: warning: ‘new’ of type ‘xmrig::CudaWorker’ with extended alignment 16 [-Waligned-new=]
     return new CudaWorker(handle->id(), handle->config());
                                                         ^
/root/code/xmrig/src/backend/common/Workers.cpp:272:57: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/root/code/xmrig/src/backend/common/Workers.cpp:272:57: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/backend/cpu/CpuThreads.h:23,
                 from /root/code/xmrig/src/backend/cpu/CpuThreads.cpp:22:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /root/code/xmrig/src/backend/cpu/CpuThreads.h:23,
                 from /root/code/xmrig/src/backend/cpu/CpuThreads.cpp:22:
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(size_t, uint32_t)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(const Value&)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/crypto/Algorithm.h:25,
                 from /root/code/xmrig/src/backend/common/Threads.h:29,
                 from /root/code/xmrig/src/backend/cpu/CpuConfig.h:23,
                 from /root/code/xmrig/src/backend/cpu/CpuConfig.cpp:19:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Miner*&, const xmrig::Algorithm&, const xmrig::CpuConfig&, const xmrig::CpuThread&, const unsigned int&}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocator<xmrig::CpuLaunchData>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuLaunchData>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘std::vector<xmrig::CpuLaunchData> xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/root/code/xmrig/src/backend/cpu/CpuWorker.cpp: In member function ‘void xmrig::CpuWorker<N>::start()’:
/root/code/xmrig/src/backend/cpu/CpuWorker.cpp:246:40: warning: requested alignment 16 is larger than 8 [-Wattributes]
         alignas(16) uint64_t tempHash[8] = {};
                                        ^
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/backend/cpu/CpuThreads.h:23,
                 from /root/code/xmrig/src/backend/cpu/interfaces/ICpuInfo.h:23,
                 from /root/code/xmrig/src/backend/cpu/platform/BasicCpuInfo.h:24,
                 from /root/code/xmrig/src/backend/cpu/platform/HwlocCpuInfo.h:23,
                 from /root/code/xmrig/src/backend/cpu/platform/HwlocCpuInfo.cpp:35:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /root/code/xmrig/src/backend/cpu/CpuThreads.h:23,
                 from /root/code/xmrig/src/backend/cpu/interfaces/ICpuInfo.h:23,
                 from /root/code/xmrig/src/backend/cpu/platform/BasicCpuInfo.h:24,
                 from /root/code/xmrig/src/backend/cpu/platform/HwlocCpuInfo.h:23,
                 from /root/code/xmrig/src/backend/cpu/platform/HwlocCpuInfo.cpp:35:
/usr/include/c++/8/bits/stl_vector.h: In member function ‘xmrig::CpuThreads xmrig::HwlocCpuInfo::allThreads(const xmrig::Algorithm&, uint32_t) const’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/backend/opencl/OclThread.h:27,
                 from /root/code/xmrig/src/backend/opencl/OclThread.cpp:19:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {long long int}; _Tp = long long int; _Alloc = std::allocator<long long int>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<long long int>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {int}; _Tp = long long int; _Alloc = std::allocator<long long int>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<long long int>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >’} changed in GCC 7.1
/usr/include/c++/8/bits/vector.tcc: In constructor ‘xmrig::OclThread::OclThread(const Value&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
In file included from /usr/include/c++/8/map:60,
                 from /root/code/xmrig/src/backend/opencl/runners/tools/OclSharedState.cpp:31:
/usr/include/c++/8/bits/stl_tree.h: In member function ‘std::pair<std::_Rb_tree_node_base*, std::_Rb_tree_node_base*> std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::_M_get_insert_hint_unique_pos(std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::const_iterator, const key_type&) [with _Key = unsigned int; _Val = std::pair<const unsigned int, xmrig::OclSharedData>; _KeyOfValue = std::_Select1st<std::pair<const unsigned int, xmrig::OclSharedData> >; _Compare = std::less<unsigned int>; _Alloc = std::allocator<std::pair<const unsigned int, xmrig::OclSharedData> >]’:
/usr/include/c++/8/bits/stl_tree.h:2146:5: note: parameter passing for argument of type ‘std::_Rb_tree<unsigned int, std::pair<const unsigned int, xmrig::OclSharedData>, std::_Select1st<std::pair<const unsigned int, xmrig::OclSharedData> >, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, xmrig::OclSharedData> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const unsigned int, xmrig::OclSharedData> >’} changed in GCC 7.1
     _Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/backend/opencl/OclThread.h:27,
                 from /root/code/xmrig/src/backend/opencl/OclLaunchData.h:30,
                 from /root/code/xmrig/src/backend/opencl/runners/tools/OclCnR.cpp:23:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Algorithm&, long long unsigned int&, unsigned int&, _cl_program*&}; _Tp = xmrig::CnrCacheEntry; _Alloc = std::allocator<xmrig::CnrCacheEntry>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CnrCacheEntry>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CnrCacheEntry*, std::vector<xmrig::CnrCacheEntry> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
/usr/include/c++/8/bits/vector.tcc: In member function ‘_cl_program* xmrig::CnrBuilder::build(const xmrig::IOclRunner&, uint64_t)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CnrCacheEntry*, std::vector<xmrig::CnrCacheEntry> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/crypto/Algorithm.h:25,
                 from /root/code/xmrig/src/backend/cuda/CudaLaunchData.h:24,
                 from /root/code/xmrig/src/backend/cuda/CudaConfig.h:23,
                 from /root/code/xmrig/src/backend/cuda/CudaConfig.cpp:19:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Miner*&, const xmrig::Algorithm&, const xmrig::CudaThread&, const xmrig::CudaDevice&}; _Tp = xmrig::CudaLaunchData; _Alloc = std::allocator<xmrig::CudaLaunchData>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CudaLaunchData>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CudaLaunchData*, std::vector<xmrig::CudaLaunchData> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘std::vector<xmrig::CudaLaunchData> xmrig::CudaConfig::get(const xmrig::Miner*, const xmrig::Algorithm&, const std::vector<xmrig::CudaDevice>&) const’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CudaLaunchData*, std::vector<xmrig::CudaLaunchData> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/backend/cuda/CudaThreads.h:23,
                 from /root/code/xmrig/src/backend/cuda/CudaThreads.cpp:19:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CudaThread&}; _Tp = xmrig::CudaThread; _Alloc = std::allocator<xmrig::CudaThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CudaThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CudaThread*, std::vector<xmrig::CudaThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CudaThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CudaThread*, std::vector<xmrig::CudaThread> >’} changed in GCC 7.1
In file included from /usr/include/c++/8/vector:64,
                 from /root/code/xmrig/src/backend/cuda/CudaThreads.h:23,
                 from /root/code/xmrig/src/backend/cuda/CudaThreads.cpp:19:
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CudaThreads::CudaThreads(const Value&)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CudaThread*, std::vector<xmrig::CudaThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaAstroBWTRunner.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/tools/String.h:27,
                 from /root/code/xmrig/src/backend/common/misc/PciTopology.h:26,
                 from /root/code/xmrig/src/backend/cuda/wrappers/CudaDevice.h:29,
                 from /root/code/xmrig/src/backend/cuda/wrappers/CudaDevice.cpp:26:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CudaThread&}; _Tp = xmrig::CudaThread; _Alloc = std::allocator<xmrig::CudaThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CudaThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CudaThread*, std::vector<xmrig::CudaThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /root/code/xmrig/src/base/tools/String.h:27,
                 from /root/code/xmrig/src/backend/common/misc/PciTopology.h:26,
                 from /root/code/xmrig/src/backend/cuda/wrappers/CudaDevice.h:29,
                 from /root/code/xmrig/src/backend/cuda/wrappers/CudaDevice.cpp:26:
/usr/include/c++/8/bits/stl_vector.h: In member function ‘void xmrig::CudaDevice::generate(const xmrig::Algorithm&, xmrig::CudaThreads&) const’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CudaThread*, std::vector<xmrig::CudaThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaKawPowRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Taskbar.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
/root/code/xmrig/src/net/JobResults.cpp: In function ‘void xmrig::getResults(xmrig::JobBundle&, std::vector<xmrig::JobResult>&, uint32_t&, bool)’:
/root/code/xmrig/src/net/JobResults.cpp:119:32: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint8_t hash[32]{ 0 };
                                ^
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/tools/String.h:27,
                 from /root/code/xmrig/src/net/JobResult.h:34,
                 from /root/code/xmrig/src/net/JobResults.cpp:33:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Job&, unsigned int&, unsigned char*&}; _Tp = xmrig::JobResult; _Alloc = std::allocator<xmrig::JobResult>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::JobResult>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::JobResult*, std::vector<xmrig::JobResult> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/map:60,
                 from /root/code/xmrig/src/backend/common/Threads.h:24,
                 from /root/code/xmrig/src/backend/cpu/CpuConfig.h:23,
                 from /root/code/xmrig/src/core/config/Config.h:27,
                 from /root/code/xmrig/src/core/Miner.cpp:36:
/usr/include/c++/8/bits/stl_tree.h: In function ‘std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::iterator std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::_M_emplace_hint_unique(std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::const_iterator, _Args&& ...) [with _Args = {const std::piecewise_construct_t&, std::tuple<xmrig::Algorithm::Id&&>, std::tuple<>}; _Key = xmrig::Algorithm::Id; _Val = std::pair<const xmrig::Algorithm::Id, double>; _KeyOfValue = std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >; _Compare = std::less<xmrig::Algorithm::Id>; _Alloc = std::allocator<std::pair<const xmrig::Algorithm::Id, double> >]’:
/usr/include/c++/8/bits/stl_tree.h:2411:7: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
       _Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::Job&, long long unsigned int&, unsigned char*, unsigned char*, unsigned char*}; _Tp = xmrig::JobResult; _Alloc = std::allocator<xmrig::JobResult>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::JobResult>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::JobResult*, std::vector<xmrig::JobResult> >’} changed in GCC 7.1
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::JobResult>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::JobResult*, std::vector<xmrig::JobResult> >’} changed in GCC 7.1
In file included from /usr/include/c++/8/map:61,
                 from /root/code/xmrig/src/backend/common/Threads.h:24,
                 from /root/code/xmrig/src/backend/cpu/CpuConfig.h:23,
                 from /root/code/xmrig/src/core/config/Config.h:27,
                 from /root/code/xmrig/src/core/Miner.cpp:36:
/usr/include/c++/8/bits/stl_map.h: In member function ‘void xmrig::MinerPrivate::getHashrate(rapidjson::Value&, rapidjson::Document&, int) const’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/vector.tcc: In function ‘void xmrig::getResults(xmrig::JobBundle&, std::vector<xmrig::JobResult>&, uint32_t&, bool)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::JobResult*, std::vector<xmrig::JobResult> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::JobResult*, std::vector<xmrig::JobResult> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::JobResult*, std::vector<xmrig::JobResult> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
/usr/include/c++/8/bits/stl_map.h: In member function ‘void xmrig::Miner::execCommand(char)’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
/usr/include/c++/8/bits/stl_map.h: In member function ‘virtual void xmrig::Miner::onTimer(const xmrig::Timer*)’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/hw/api/HwApi.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiBoard.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiMemory.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiTools.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /root/code/xmrig/src/base/tools/String.h:27,
                 from /root/code/xmrig/src/hw/dmi/DmiBoard.h:25,
                 from /root/code/xmrig/src/hw/dmi/DmiReader.h:25,
                 from /root/code/xmrig/src/hw/dmi/DmiReader.cpp:21:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::dmi_header*}; _Tp = xmrig::DmiMemory; _Alloc = std::allocator<xmrig::DmiMemory>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::DmiMemory>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::DmiMemory*, std::vector<xmrig::DmiMemory> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In function ‘bool xmrig::DmiReader::decode(uint8_t*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::DmiMemory*, std::vector<xmrig::DmiMemory> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
In file included from /root/code/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /root/code/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /root/code/xmrig/src/crypto/cn/CnHash.cpp:27:
/root/code/xmrig/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
In file included from /root/code/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /root/code/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /root/code/xmrig/src/crypto/cn/CnHash.cpp:27:
/root/code/xmrig/src/crypto/cn/sse2neon.h:7594:9: warning: ‘#pragma GCC pop_options’ without a corresponding ‘#pragma GCC push_options’ [-Wpragmas]
 #pragma GCC pop_options
         ^~~
In file included from /root/code/xmrig/src/crypto/cn/CnHash.cpp:27:
/root/code/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i aes_round_tweak_div(const __m128i&, const __m128i&)’:
/root/code/xmrig/src/crypto/cn/CryptoNight_arm.h:332:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/root/code/xmrig/src/crypto/cn/CryptoNight_arm.h:333:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
/root/code/xmrig/src/crypto/randomx/aes_hash.cpp: In lambda function:
/root/code/xmrig/src/crypto/randomx/aes_hash.cpp:391:38: warning: requested alignment 16 is larger than 8 [-Wattributes]
           alignas(16) uint8_t hash[64] = {};
                                      ^
/root/code/xmrig/src/crypto/randomx/aes_hash.cpp:392:39: warning: requested alignment 16 is larger than 8 [-Wattributes]
           alignas(16) uint8_t state[64] = {};
                                       ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2507: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
make[1]: *** [CMakeFiles/Makefile2:118: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2`

## Spudz76 | 2021-11-02T22:45:55+00:00
Found the needle in that haystack:

```
/root/code/xmrig/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A." #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
```

So it's not selecting the right ARM_TARGET, try forcing it with `-DARM_TARGET=8` in the CMake command.

#2394 might fix it but it's been collecting dust.  You could build with that patch included and see if it "just works" then.  Would be neat if this very very common error never happened again.

## rakuuhwa | 2021-11-19T10:21:44+00:00
The error is still the same, does not matter if i include the fix in 2394 or i force the -DARM_TARGET (i tested with all 4 possible scenario)
[errorstuff.txt](https://github.com/xmrig/xmrig/files/7569502/errorstuff.txt)


Resolved.
Error was i was using a 32bit OS. with "cmake .. -DARM_TARGET=8" the 64bit OS was able to perform the make command


## Spudz76 | 2021-11-19T14:03:37+00:00
Yes that would force ARM7 and then also not work.

## benthetechguy | 2022-01-26T00:10:41+00:00
Issue is fixed in #2898

## sigkill | 2022-02-07T15:20:02+00:00
Okay to close issue?

## Anto9977 | 2023-06-26T22:39:43+00:00
 I have these problem
make[2]: *** [CMakeFiles/xmrig.dir/build.make:76: CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o] Error 1                                                   make[1]: *** [CMakeFiles/Makefile2:138: CMakeFiles/xmrig.dir/all] Error 2          make: *** [Makefile:91: all] Error 2                                               (arg: -1)

## benthetechguy | 2023-06-26T23:54:42+00:00
The actual error is further up in the output. Can you post the full log?

## mustaqim-project | 2024-03-20T07:58:48+00:00
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
/home/agung/xmrig/src/crypto/randomx/randomx.cpp: In member function ‘void RandomX_ConfigurationBase::Apply()’:
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:291:9: note: in expansion of macro ‘INST_HANDLE’
  291 |         INST_HANDLE(IADD_RS, NULL);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:291:9: note: in expansion of macro ‘INST_HANDLE’
  291 |         INST_HANDLE(IADD_RS, NULL);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:292:9: note: in expansion of macro ‘INST_HANDLE’
  292 |         INST_HANDLE(IADD_M, IADD_RS);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:292:9: note: in expansion of macro ‘INST_HANDLE’
  292 |         INST_HANDLE(IADD_M, IADD_RS);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:293:9: note: in expansion of macro ‘INST_HANDLE’
  293 |         INST_HANDLE(ISUB_R, IADD_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:293:9: note: in expansion of macro ‘INST_HANDLE’
  293 |         INST_HANDLE(ISUB_R, IADD_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:294:9: note: in expansion of macro ‘INST_HANDLE’
  294 |         INST_HANDLE(ISUB_M, ISUB_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:294:9: note: in expansion of macro ‘INST_HANDLE’
  294 |         INST_HANDLE(ISUB_M, ISUB_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:295:9: note: in expansion of macro ‘INST_HANDLE’
  295 |         INST_HANDLE(IMUL_R, ISUB_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:295:9: note: in expansion of macro ‘INST_HANDLE’
  295 |         INST_HANDLE(IMUL_R, ISUB_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:296:9: note: in expansion of macro ‘INST_HANDLE’
  296 |         INST_HANDLE(IMUL_M, IMUL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:296:9: note: in expansion of macro ‘INST_HANDLE’
  296 |         INST_HANDLE(IMUL_M, IMUL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:306:17: note: in expansion of macro ‘INST_HANDLE’
  306 |                 INST_HANDLE(IMULH_R, IMUL_M);
      |                 ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:306:17: note: in expansion of macro ‘INST_HANDLE’
  306 |                 INST_HANDLE(IMULH_R, IMUL_M);
      |                 ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:307:17: note: in expansion of macro ‘INST_HANDLE’
  307 |                 INST_HANDLE(IMULH_M, IMULH_R);
      |                 ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:307:17: note: in expansion of macro ‘INST_HANDLE’
  307 |                 INST_HANDLE(IMULH_M, IMULH_R);
      |                 ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:310:9: note: in expansion of macro ‘INST_HANDLE’
  310 |         INST_HANDLE(ISMULH_R, IMULH_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:310:9: note: in expansion of macro ‘INST_HANDLE’
  310 |         INST_HANDLE(ISMULH_R, IMULH_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:311:9: note: in expansion of macro ‘INST_HANDLE’
  311 |         INST_HANDLE(ISMULH_M, ISMULH_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:311:9: note: in expansion of macro ‘INST_HANDLE’
  311 |         INST_HANDLE(ISMULH_M, ISMULH_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:312:9: note: in expansion of macro ‘INST_HANDLE’
  312 |         INST_HANDLE(IMUL_RCP, ISMULH_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:312:9: note: in expansion of macro ‘INST_HANDLE’
  312 |         INST_HANDLE(IMUL_RCP, ISMULH_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:313:9: note: in expansion of macro ‘INST_HANDLE’
  313 |         INST_HANDLE(INEG_R, IMUL_RCP);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:313:9: note: in expansion of macro ‘INST_HANDLE’
  313 |         INST_HANDLE(INEG_R, IMUL_RCP);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:314:9: note: in expansion of macro ‘INST_HANDLE’
  314 |         INST_HANDLE(IXOR_R, INEG_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:314:9: note: in expansion of macro ‘INST_HANDLE’
  314 |         INST_HANDLE(IXOR_R, INEG_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:315:9: note: in expansion of macro ‘INST_HANDLE’
  315 |         INST_HANDLE(IXOR_M, IXOR_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:315:9: note: in expansion of macro ‘INST_HANDLE’
  315 |         INST_HANDLE(IXOR_M, IXOR_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:316:9: note: in expansion of macro ‘INST_HANDLE’
  316 |         INST_HANDLE(IROR_R, IXOR_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:316:9: note: in expansion of macro ‘INST_HANDLE’
  316 |         INST_HANDLE(IROR_R, IXOR_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:317:9: note: in expansion of macro ‘INST_HANDLE’
  317 |         INST_HANDLE(IROL_R, IROR_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:317:9: note: in expansion of macro ‘INST_HANDLE’
  317 |         INST_HANDLE(IROL_R, IROR_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:318:9: note: in expansion of macro ‘INST_HANDLE’
  318 |         INST_HANDLE(ISWAP_R, IROL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:318:9: note: in expansion of macro ‘INST_HANDLE’
  318 |         INST_HANDLE(ISWAP_R, IROL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:319:9: note: in expansion of macro ‘INST_HANDLE’
  319 |         INST_HANDLE(FSWAP_R, ISWAP_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:319:9: note: in expansion of macro ‘INST_HANDLE’
  319 |         INST_HANDLE(FSWAP_R, ISWAP_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:320:9: note: in expansion of macro ‘INST_HANDLE’
  320 |         INST_HANDLE(FADD_R, FSWAP_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:320:9: note: in expansion of macro ‘INST_HANDLE’
  320 |         INST_HANDLE(FADD_R, FSWAP_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:321:9: note: in expansion of macro ‘INST_HANDLE’
  321 |         INST_HANDLE(FADD_M, FADD_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:321:9: note: in expansion of macro ‘INST_HANDLE’
  321 |         INST_HANDLE(FADD_M, FADD_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:322:9: note: in expansion of macro ‘INST_HANDLE’
  322 |         INST_HANDLE(FSUB_R, FADD_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:322:9: note: in expansion of macro ‘INST_HANDLE’
  322 |         INST_HANDLE(FSUB_R, FADD_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:323:9: note: in expansion of macro ‘INST_HANDLE’
  323 |         INST_HANDLE(FSUB_M, FSUB_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:323:9: note: in expansion of macro ‘INST_HANDLE’
  323 |         INST_HANDLE(FSUB_M, FSUB_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:324:9: note: in expansion of macro ‘INST_HANDLE’
  324 |         INST_HANDLE(FSCAL_R, FSUB_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:324:9: note: in expansion of macro ‘INST_HANDLE’
  324 |         INST_HANDLE(FSCAL_R, FSUB_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:325:9: note: in expansion of macro ‘INST_HANDLE’
  325 |         INST_HANDLE(FMUL_R, FSCAL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:325:9: note: in expansion of macro ‘INST_HANDLE’
  325 |         INST_HANDLE(FMUL_R, FSCAL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:326:9: note: in expansion of macro ‘INST_HANDLE’
  326 |         INST_HANDLE(FDIV_M, FMUL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:326:9: note: in expansion of macro ‘INST_HANDLE’
  326 |         INST_HANDLE(FDIV_M, FMUL_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:327:9: note: in expansion of macro ‘INST_HANDLE’
  327 |         INST_HANDLE(FSQRT_R, FDIV_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:327:9: note: in expansion of macro ‘INST_HANDLE’
  327 |         INST_HANDLE(FSQRT_R, FDIV_M);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:337:9: note: in expansion of macro ‘INST_HANDLE’
  337 |         INST_HANDLE(CBRANCH, FSQRT_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:337:9: note: in expansion of macro ‘INST_HANDLE’
  337 |         INST_HANDLE(CBRANCH, FSQRT_R);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:347:17: note: in expansion of macro ‘INST_HANDLE’
  347 |                 INST_HANDLE(CFROUND, CBRANCH);
      |                 ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:347:17: note: in expansion of macro ‘INST_HANDLE’
  347 |                 INST_HANDLE(CFROUND, CBRANCH);
      |                 ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:350:9: note: in expansion of macro ‘INST_HANDLE’
  350 |         INST_HANDLE(ISTORE, CFROUND);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:350:9: note: in expansion of macro ‘INST_HANDLE’
  350 |         INST_HANDLE(ISTORE, CFROUND);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:351:9: note: in expansion of macro ‘INST_HANDLE’
  351 |         INST_HANDLE(NOP, ISTORE);
      |         ^~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/agung/xmrig/src/crypto/randomx/randomx.cpp:351:9: note: in expansion of macro ‘INST_HANDLE’
  351 |         INST_HANDLE(NOP, ISTORE);
      |         ^~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2792: CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:138: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

# Action History
- Created by: razer1337o | 2021-10-30T19:06:59+00:00
- Closed at: 2023-06-05T15:22:07+00:00
