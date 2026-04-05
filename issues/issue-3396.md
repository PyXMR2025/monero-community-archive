---
title: Failure to build
source_url: https://github.com/xmrig/xmrig/issues/3396
author: BlakesMakes
assignees: []
labels: []
created_at: '2024-01-01T15:05:07+00:00'
updated_at: '2024-01-02T17:20:26+00:00'
type: issue
status: closed
closed_at: '2024-01-02T17:20:25+00:00'
---

# Original Description
**Describe the bug**
xmrig fails to build

**To Reproduce**
run make

**Expected behavior**
Expected it to build as it did on my other pis I got set up the same day running rpi OS 64 bit desktop

**Required data**
 - OS: raspberry pi OS 64 bit lite

**Additional context**

Attempted to get running using the following:

```
sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build
cd xmrig/build
cmake ..
make
```



When running cmake .. :

```
big_fella@bigfella:~/xmrig/build $ cmake ..
-- The C compiler identification is GNU 12.2.0
-- The CXX compiler identification is GNU 12.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.so
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "3.0.11")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/big_fella/xmrig/build
big_fella@bigfella:~/xmrig/build $ make

```
Error when running make:

```
big_fella@bigfella:~/xmrig/build $ cmake ..
-- The C compiler identification is GNU 12.2.0
-- The CXX compiler identification is GNU 12.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.so
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "3.0.11")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/big_fella/xmrig/build
big_fella@bigfella:~/xmrig/build $ make
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  3%] Linking C static library libargon2.a
[  3%] Built target argon2
[  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  4%] Linking C static library libethash.a
[  4%] Built target ethash
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o
[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o
[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o
[ 10%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
[ 11%] Linking CXX static library libghostrider.a
[ 11%] Built target ghostrider
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
In file included from /usr/include/c++/12/vector:70,
                 from /home/big_fella/xmrig/src/base/io/json/JsonChain.h:23,
                 from /home/big_fella/xmrig/src/base/io/json/JsonChain.cpp:19:
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > >::iterator’ changed in GCC 7.1
  439 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’,
    inlined from ‘void std::vector<_Tp, _Alloc>::push_back(value_type&&) [with _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’ at /usr/include/c++/12/bits/stl_vector.h:1294:21,
    inlined from ‘bool xmrig::JsonChain::add(rapidjson::Document&&)’ at /home/big_fella/xmrig/src/base/io/json/JsonChain.cpp:41:22:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’,
    inlined from ‘void std::vector<_Tp, _Alloc>::push_back(value_type&&) [with _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’ at /usr/include/c++/12/bits/stl_vector.h:1294:21,
    inlined from ‘bool xmrig::JsonChain::add(rapidjson::Document&&)’ at /home/big_fella/xmrig/src/base/io/json/JsonChain.cpp:41:22,
    inlined from ‘bool xmrig::JsonChain::addFile(const char*)’ at /home/big_fella/xmrig/src/base/io/json/JsonChain.cpp:54:19:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’,
    inlined from ‘void std::vector<_Tp, _Alloc>::push_back(value_type&&) [with _Tp = rapidjson::GenericDocument<rapidjson::UTF8<> >; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<> > >]’ at /usr/include/c++/12/bits/stl_vector.h:1294:21,
    inlined from ‘bool xmrig::JsonChain::add(rapidjson::Document&&)’ at /home/big_fella/xmrig/src/base/io/json/JsonChain.cpp:41:22,
    inlined from ‘bool xmrig::JsonChain::addRaw(const char*)’ at /home/big_fella/xmrig/src/base/io/json/JsonChain.cpp:96:15:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<> >*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<> > > >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
In file included from /usr/include/c++/12/vector:70,
                 from /home/big_fella/xmrig/src/base/net/stratum/Pools.h:29,
                 from /home/big_fella/xmrig/src/base/net/stratum/Pools.cpp:26:
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {std::shared_ptr<xmrig::BenchConfig>&}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ changed in GCC 7.1
  439 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ changed in GCC 7.1
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {std::shared_ptr<xmrig::BenchConfig>&}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’,
    inlined from ‘void xmrig::Pools::load(const xmrig::IJsonReader&)’ at /home/big_fella/xmrig/src/base/net/stratum/Pools.cpp:139:28:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’,
    inlined from ‘void std::vector<_Tp, _Alloc>::push_back(value_type&&) [with _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’ at /usr/include/c++/12/bits/stl_vector.h:1294:21,
    inlined from ‘void xmrig::Pools::load(const xmrig::IJsonReader&)’ at /home/big_fella/xmrig/src/base/net/stratum/Pools.cpp:157:29:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Chrono.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 30%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 31%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 35%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 35%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[ 36%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
In file included from /usr/include/c++/12/vector:70,
                 from /home/big_fella/xmrig/src/base/crypto/Algorithm.h:25,
                 from /home/big_fella/xmrig/src/backend/common/Threads.h:29,
                 from /home/big_fella/xmrig/src/backend/cpu/CpuConfig.h:23,
                 from /home/big_fella/xmrig/src/backend/cpu/CpuConfig.cpp:19:
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {long long int}; _Tp = long long int; _Alloc = std::allocator<long long int>]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<long long int>::iterator’ changed in GCC 7.1
  439 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {const xmrig::Miner*&, const xmrig::Algorithm&, const xmrig::CpuConfig&, const xmrig::CpuThread&, const unsigned int&, std::vector<long long int, std::allocator<long long int> >&}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocator<xmrig::CpuLaunchData>]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuLaunchData>::iterator’ changed in GCC 7.1
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {long long int}; _Tp = long long int; _Alloc = std::allocator<long long int>]’,
    inlined from ‘std::vector<xmrig::CpuLaunchData> xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const’ at /home/big_fella/xmrig/src/backend/cpu/CpuConfig.cpp:119:32:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {const xmrig::Miner*&, const xmrig::Algorithm&, const xmrig::CpuConfig&, const xmrig::CpuThread&, const unsigned int&, std::vector<long long int, std::allocator<long long int> >&}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocator<xmrig::CpuLaunchData>]’,
    inlined from ‘std::vector<xmrig::CpuLaunchData> xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const’ at /home/big_fella/xmrig/src/backend/cpu/CpuConfig.cpp:123:25:
/usr/include/c++/12/bits/vector.tcc:123:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’ changed in GCC 7.1
  123 |           _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
In file included from /usr/include/c++/12/vector:70,
                 from /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:23,
                 from /home/big_fella/xmrig/src/backend/cpu/CpuThreads.cpp:22:
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ changed in GCC 7.1
  439 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/12/vector:64:
In member function ‘void std::vector<_Tp, _Alloc>::push_back(const value_type&) [with _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’,
    inlined from ‘void xmrig::CpuThreads::add(const xmrig::CpuThread&)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:44:79,
    inlined from ‘void xmrig::CpuThreads::add(int64_t, uint32_t)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:45:66,
    inlined from ‘xmrig::CpuThreads::CpuThreads(size_t, uint32_t)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.cpp:111:12:
/usr/include/c++/12/bits/stl_vector.h:1287:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1287 |           _M_realloc_insert(end(), __x);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::push_back(const value_type&) [with _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’,
    inlined from ‘void xmrig::CpuThreads::add(const xmrig::CpuThread&)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:44:79,
    inlined from ‘xmrig::CpuThreads::CpuThreads(const rapidjson::Value&)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.cpp:85:20:
/usr/include/c++/12/bits/stl_vector.h:1287:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1287 |           _M_realloc_insert(end(), __x);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
In member function ‘void std::vector<_Tp, _Alloc>::push_back(const value_type&) [with _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’,
    inlined from ‘void xmrig::CpuThreads::add(const xmrig::CpuThread&)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:44:79,
    inlined from ‘void xmrig::CpuThreads::add(int64_t, uint32_t)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:45:66,
    inlined from ‘xmrig::CpuThreads::CpuThreads(const rapidjson::Value&)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.cpp:100:16:
/usr/include/c++/12/bits/stl_vector.h:1287:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1287 |           _M_realloc_insert(end(), __x);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
In file included from /usr/include/c++/12/vector:70,
                 from /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:23,
                 from /home/big_fella/xmrig/src/backend/cpu/interfaces/ICpuInfo.h:23,
                 from /home/big_fella/xmrig/src/backend/cpu/platform/BasicCpuInfo.h:24,
                 from /home/big_fella/xmrig/src/backend/cpu/platform/HwlocCpuInfo.h:23,
                 from /home/big_fella/xmrig/src/backend/cpu/platform/HwlocCpuInfo.cpp:35:
/usr/include/c++/12/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/12/bits/vector.tcc:439:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ changed in GCC 7.1
  439 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/12/vector:64:
In member function ‘void std::vector<_Tp, _Alloc>::push_back(const value_type&) [with _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’,
    inlined from ‘void xmrig::CpuThreads::add(const xmrig::CpuThread&)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:44:79,
    inlined from ‘void xmrig::CpuThreads::add(int64_t, uint32_t)’ at /home/big_fella/xmrig/src/backend/cpu/CpuThreads.h:45:66,
    inlined from ‘xmrig::CpuThreads xmrig::HwlocCpuInfo::allThreads(const xmrig::Algorithm&, uint32_t) const’ at /home/big_fella/xmrig/src/backend/cpu/platform/HwlocCpuInfo.cpp:266:20:
/usr/include/c++/12/bits/stl_vector.h:1287:28: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1287 |           _M_realloc_insert(end(), __x);
      |           ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
/home/big_fella/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp: In constructor ‘xmrig::BasicCpuInfo::BasicCpuInfo()’:
/home/big_fella/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:78:49: error: ‘HWCAP_AES’ was not declared in this scope; did you mean ‘HWCAP2_AES’?
   78 |     m_flags.set(FLAG_AES, getauxval(AT_HWCAP) & HWCAP_AES);
      |                                                 ^~~~~~~~~
      |                                                 HWCAP2_AES
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1364: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:138: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
big_fella@bigfella:~/xmrig/build $
```

# Discussion History
## SChernykh | 2024-01-01T16:29:34+00:00
It looks like you're compiling for 32-bit, based on what I found googling `HWCAP_AES vs HWCAP2_AES`. You should compile 64-bit binary.

Edit: `-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so` - yes, this is definitely 32-bit mode.

## BlakesMakes | 2024-01-01T17:38:14+00:00
Hmm. I never would have caught that. How can I fix it?

## BlakesMakes | 2024-01-02T17:20:26+00:00
Alright well I don't know what OS I was running I picked whatever I downloaded the other day that I thought was 64 bit... I betcha it was 32 bit. I reinstalled 64 bit and it built just fine.

# Action History
- Created by: BlakesMakes | 2024-01-01T15:05:07+00:00
- Closed at: 2024-01-02T17:20:25+00:00
