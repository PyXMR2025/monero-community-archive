---
title: Build with -DWITH_OPENCL=OFF fails
source_url: https://github.com/xmrig/xmrig/issues/2224
author: 00-matt
assignees: []
labels: []
created_at: '2021-04-01T09:56:06+00:00'
updated_at: '2021-04-06T14:11:55+00:00'
type: issue
status: closed
closed_at: '2021-04-06T14:11:55+00:00'
---

# Original Description
##### Describe the bug

XMRig fails to build when it is configured with `-DWITH_OPENCL=OFF`.

```
[75/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
FAILED: CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o 
/usr/bin/c++ -DASTROBWT_AVX2 -DHAVE_BUILTIN_CLEAR_CACHE -DHAVE_ROTR -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_ASTROBWT -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_KAWPOW -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_CUDA -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_NVML -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D__STDC_FORMAT_MACROS -I../src -I../src/3rdparty -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -maes -O3 -DNDEBUG -Ofast -s -std=c++11 -MD -MT CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o -MF CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o.d -o CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o -c ../src/backend/cuda/CudaBackend.cpp
In file included from ../src/backend/cuda/CudaBackend.cpp:35:
../src/backend/common/Workers.h:63:55: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                       ^~~~~~~~~~
../src/backend/common/Workers.h:34:1: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   33 | #   include "backend/cuda/CudaLaunchData.h"
  +++ |+#include <memory>
   34 | #endif
../src/backend/common/Workers.h:63:65: error: expected ‘,’ or ‘...’ before ‘<’ token
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |         
```

##### To Reproduce

1. Clone and change into XMRig sources:
    ```bash
    git clone https://github.com/xmrig/xmrig.git
    ```
2. Configure build:
    ```bash
    cmake -Bbuild -DCMAKE_BUILD_TYPE=Release -DWITH_OPENCL=OFF
    ```
3. Build and observe error:
    ```bash
    make -Cbuild
    ```

##### Expected behavior

Build succeeds.

##### Required data

###### Toolchain

```
~ $ gcc --version
gcc (Gentoo 11.0.1_pre9999 p6, commit 4d66685e49d20e0c7a87c5fa0757c7eb63ffcdaa) 11.0.1 20210305 (experimental)
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

~ $ cmake --version
cmake version 3.20.0
```

###### CMake Log

```
-- The C compiler identification is GNU 11.0.1
-- The CXX compiler identification is GNU 11.0.1
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
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib64/libhwloc.so  
-- Found UV: /usr/lib64/libuv.so  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=ON
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Success
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Success
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Success
-- argon2: feature 'avx512f' detected!
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Found OpenSSL: /usr/lib64/libcrypto.so (found version "1.1.1k")  
-- Configuring done
-- Generating done
-- Build files have been written to: /tmp/xmrig-6.10.0/build
```

###### Build Log

```
ninja: Entering directory `build'
[1/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[2/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[3/208] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[4/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[5/208] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[6/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[7/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[8/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[9/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[10/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[11/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[12/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[13/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[14/208] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[15/208] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[16/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[17/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[18/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[19/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[20/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[21/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[22/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[23/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[24/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[25/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[26/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[27/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[28/208] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[29/208] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[30/208] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[31/208] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[32/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[33/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[34/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[35/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[36/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[37/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[38/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[39/208] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[40/208] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[41/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[42/208] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[43/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[44/208] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[45/208] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[46/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[47/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[48/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[49/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[50/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[51/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[52/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[53/208] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[54/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[55/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[56/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[57/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[58/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[59/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
FAILED: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o 
/usr/bin/c++ -DASTROBWT_AVX2 -DHAVE_BUILTIN_CLEAR_CACHE -DHAVE_ROTR -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_ASTROBWT -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_KAWPOW -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_CUDA -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_NVML -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D__STDC_FORMAT_MACROS -I../src -I../src/3rdparty -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -maes -O3 -DNDEBUG -Ofast -s -std=c++11 -MD -MT CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o -MF CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o.d -o CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o -c ../src/backend/common/Workers.cpp
In file included from ../src/backend/common/Workers.cpp:20:
../src/backend/common/Workers.h:63:55: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                       ^~~~~~~~~~
../src/backend/common/Workers.h:34:1: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   33 | #   include "backend/cuda/CudaLaunchData.h"
  +++ |+#include <memory>
   34 | #endif
../src/backend/common/Workers.h:63:65: error: expected ‘,’ or ‘...’ before ‘<’ token
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                                 ^
../src/backend/common/Workers.cpp:56:10: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   56 |     std::shared_ptr<Benchmark> benchmark;
      |          ^~~~~~~~~~
../src/backend/common/Workers.cpp:41:1: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   40 | #   include "backend/common/benchmark/Benchmark.h"
  +++ |+#include <memory>
   41 | #endif
../src/backend/common/Workers.cpp:57:10: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   57 |     std::shared_ptr<Hashrate> hashrate;
      |          ^~~~~~~~~~
../src/backend/common/Workers.cpp:57:5: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   57 |     std::shared_ptr<Hashrate> hashrate;
      |     ^~~
../src/backend/common/Workers.cpp: In member function ‘bool xmrig::Workers<T>::tick(uint64_t)’:
../src/backend/common/Workers.cpp:82:17: error: ‘class xmrig::WorkersPrivate’ has no member named ‘hashrate’
   82 |     if (!d_ptr->hashrate) {
      |                 ^~~~~~~~
../src/backend/common/Workers.cpp:96:20: error: ‘class xmrig::WorkersPrivate’ has no member named ‘hashrate’
   96 |             d_ptr->hashrate->add(handle->id(), hashCount, ts);
      |                    ^~~~~~~~
../src/backend/common/Workers.cpp:107:16: error: ‘class xmrig::WorkersPrivate’ has no member named ‘hashrate’
  107 |         d_ptr->hashrate->add(totalHashCount, Chrono::steadyMSecs());
      |                ^~~~~~~~
../src/backend/common/Workers.cpp:111:20: error: ‘class xmrig::WorkersPrivate’ has no member named ‘benchmark’
  111 |     return !d_ptr->benchmark || !d_ptr->benchmark->finish(totalHashCount);
      |                    ^~~~~~~~~
../src/backend/common/Workers.cpp:111:41: error: ‘class xmrig::WorkersPrivate’ has no member named ‘benchmark’
  111 |     return !d_ptr->benchmark || !d_ptr->benchmark->finish(totalHashCount);
      |                                         ^~~~~~~~~
../src/backend/common/Workers.cpp: In member function ‘const xmrig::Hashrate* xmrig::Workers<T>::hashrate() const’:
../src/backend/common/Workers.cpp:121:19: error: ‘class xmrig::WorkersPrivate’ has no member named ‘hashrate’
  121 |     return d_ptr->hashrate.get();
      |                   ^~~~~~~~
../src/backend/common/Workers.cpp: In member function ‘void xmrig::Workers<T>::stop()’:
../src/backend/common/Workers.cpp:149:12: error: ‘class xmrig::WorkersPrivate’ has no member named ‘hashrate’
  149 |     d_ptr->hashrate.reset();
      |            ^~~~~~~~
../src/backend/common/Workers.cpp: At global scope:
../src/backend/common/Workers.cpp:155:70: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
  155 | void xmrig::Workers<T>::start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark)
      |                                                                      ^~~~~~~~~~
../src/backend/common/Workers.cpp:155:65: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
  155 | void xmrig::Workers<T>::start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark)
      |                                                                 ^~~
../src/backend/common/Workers.cpp:155:80: error: expected ‘,’ or ‘...’ before ‘<’ token
  155 | void xmrig::Workers<T>::start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark)
      |                                                                                ^
../src/backend/common/Workers.cpp: In member function ‘void xmrig::Workers<T>::start(const std::vector<T>&, int)’:
../src/backend/common/Workers.cpp:157:10: error: ‘benchmark’ was not declared in this scope
  157 |     if (!benchmark) {
      |          ^~~~~~~~~
../src/backend/common/Workers.cpp:163:12: error: ‘class xmrig::WorkersPrivate’ has no member named ‘benchmark’
  163 |     d_ptr->benchmark = benchmark;
      |            ^~~~~~~~~
../src/backend/common/Workers.cpp:163:24: error: ‘benchmark’ was not declared in this scope
  163 |     d_ptr->benchmark = benchmark;
      |                        ^~~~~~~~~
../src/backend/common/Workers.cpp:164:12: error: ‘class xmrig::WorkersPrivate’ has no member named ‘benchmark’
  164 |     d_ptr->benchmark->start();
      |            ^~~~~~~~~
../src/backend/common/Workers.cpp: In member function ‘void xmrig::Workers<T>::start(const std::vector<T>&, bool)’:
../src/backend/common/Workers.cpp:209:12: error: ‘class xmrig::WorkersPrivate’ has no member named ‘hashrate’
  209 |     d_ptr->hashrate = std::make_shared<Hashrate>(m_workers.size());
      |            ^~~~~~~~
../src/backend/common/Workers.cpp:209:28: error: ‘make_shared’ is not a member of ‘std’
  209 |     d_ptr->hashrate = std::make_shared<Hashrate>(m_workers.size());
      |                            ^~~~~~~~~~~
../src/backend/common/Workers.cpp:209:28: note: ‘std::make_shared’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
../src/backend/common/Workers.cpp:209:48: error: expected primary-expression before ‘>’ token
  209 |     d_ptr->hashrate = std::make_shared<Hashrate>(m_workers.size());
      |                                                ^
../src/backend/common/Workers.cpp: In instantiation of ‘const xmrig::Hashrate* xmrig::Workers<T>::hashrate() const [with T = xmrig::CpuLaunchData]’:
../src/backend/common/Workers.cpp:254:16:   required from here
../src/backend/common/Workers.cpp:122:1: warning: no return statement in function returning non-void [-Wreturn-type]
  122 | }
      | ^
../src/backend/common/Workers.cpp: In instantiation of ‘const xmrig::Hashrate* xmrig::Workers<T>::hashrate() const [with T = xmrig::CudaLaunchData]’:
../src/backend/common/Workers.cpp:277:16:   required from here
../src/backend/common/Workers.cpp:122:1: warning: no return statement in function returning non-void [-Wreturn-type]
../src/backend/common/Workers.cpp: In member function ‘bool xmrig::Workers<T>::tick(uint64_t) [with T = xmrig::CpuLaunchData]’:
../src/backend/common/Workers.cpp:115:1: warning: control reaches end of non-void function [-Wreturn-type]
  115 | }
      | ^
../src/backend/common/Workers.cpp: In member function ‘bool xmrig::Workers<T>::tick(uint64_t) [with T = xmrig::CudaLaunchData]’:
../src/backend/common/Workers.cpp:115:1: warning: control reaches end of non-void function [-Wreturn-type]
[60/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[61/208] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[62/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[63/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[64/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[65/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[66/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[67/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[68/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[69/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[70/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[71/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[72/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
FAILED: CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o 
/usr/bin/c++ -DASTROBWT_AVX2 -DHAVE_BUILTIN_CLEAR_CACHE -DHAVE_ROTR -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_ASTROBWT -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_KAWPOW -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_CUDA -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_NVML -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D__STDC_FORMAT_MACROS -I../src -I../src/3rdparty -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -maes -O3 -DNDEBUG -Ofast -s -std=c++11 -MD -MT CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o -MF CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o.d -o CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o -c ../src/backend/cpu/CpuBackend.cpp
In file included from ../src/backend/cpu/CpuBackend.cpp:34:
../src/backend/common/Workers.h:63:55: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                       ^~~~~~~~~~
../src/backend/common/Workers.h:34:1: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   33 | #   include "backend/cuda/CudaLaunchData.h"
  +++ |+#include <memory>
   34 | #endif
../src/backend/common/Workers.h:63:65: error: expected ‘,’ or ‘...’ before ‘<’ token
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                                 ^
../src/backend/cpu/CpuBackend.cpp: In member function ‘void xmrig::CpuBackendPrivate::start()’:
../src/backend/cpu/CpuBackend.cpp:162:41: error: no matching function for call to ‘xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> >&, std::shared_ptr<xmrig::Benchmark>&)’
  162 |         workers.start(threads, benchmark);
      |                                         ^
In file included from ../src/backend/cpu/CpuBackend.cpp:34:
../src/backend/common/Workers.h:54:17: note: candidate: ‘void xmrig::Workers<T>::start(const std::vector<T>&) [with T = xmrig::CpuLaunchData]’
   54 |     inline void start(const std::vector<T> &data)   { start(data, true); }
      |                 ^~~~~
../src/backend/common/Workers.h:54:17: note:   candidate expects 1 argument, 2 provided
../src/backend/common/Workers.h:63:10: note: candidate: ‘void xmrig::Workers<T>::start(const std::vector<T>&, int) [with T = xmrig::CpuLaunchData]’
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |          ^~~~~
../src/backend/common/Workers.h:63:44: note:   no known conversion for argument 2 from ‘std::shared_ptr<xmrig::Benchmark>’ to ‘int’
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                            ^~~~~~~~~~~~~~~~~~~~~
../src/backend/common/Workers.h:70:10: note: candidate: ‘void xmrig::Workers<T>::start(const std::vector<T>&, bool) [with T = xmrig::CpuLaunchData]’
   70 |     void start(const std::vector<T> &data, bool sleep);
      |          ^~~~~
../src/backend/common/Workers.h:70:49: note:   no known conversion for argument 2 from ‘std::shared_ptr<xmrig::Benchmark>’ to ‘bool’
   70 |     void start(const std::vector<T> &data, bool sleep);
      |                                            ~~~~~^~~~~
[73/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[74/208] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[75/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
FAILED: CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o 
/usr/bin/c++ -DASTROBWT_AVX2 -DHAVE_BUILTIN_CLEAR_CACHE -DHAVE_ROTR -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_ASTROBWT -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_KAWPOW -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_CUDA -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_NVML -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D__STDC_FORMAT_MACROS -I../src -I../src/3rdparty -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -maes -O3 -DNDEBUG -Ofast -s -std=c++11 -MD -MT CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o -MF CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o.d -o CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o -c ../src/backend/cuda/CudaBackend.cpp
In file included from ../src/backend/cuda/CudaBackend.cpp:35:
../src/backend/common/Workers.h:63:55: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                       ^~~~~~~~~~
../src/backend/common/Workers.h:34:1: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   33 | #   include "backend/cuda/CudaLaunchData.h"
  +++ |+#include <memory>
   34 | #endif
../src/backend/common/Workers.h:63:65: error: expected ‘,’ or ‘...’ before ‘<’ token
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                                 ^
[76/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[77/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[78/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[79/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[80/208] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[81/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[82/208] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[83/208] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[84/208] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
ninja: build stopped: subcommand failed.
```


# Discussion History
## 00-matt | 2021-04-01T09:57:39+00:00
The same happens with `-DWITH_OPENCL=OFF` and `-DWITH_CUDA=OFF` both set:

```
FAILED: CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
/usr/bin/c++ -DASTROBWT_AVX2 -DHAVE_BUILTIN_CLEAR_CACHE -DHAVE_ROTR -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_ASTROBWT -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_KAWPOW -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D__STDC_FORMAT_MACROS -I../src -I../src/3rdparty -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -maes -O3 -DNDEBUG -Ofast -s -std=c++11 -MD -MT CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o -MF CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o.d -o CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o -c ../src/backend/cpu/CpuBackend.cpp
In file included from ../src/backend/cpu/CpuBackend.cpp:34:
../src/backend/common/Workers.h:63:55: error: ‘shared_ptr’ in namespace ‘std’ does not name a template type
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                       ^~~~~~~~~~
../src/backend/common/Workers.h:25:1: note: ‘std::shared_ptr’ is defined in header ‘<memory>’; did you forget to ‘#include <memory>’?
   24 | #include "backend/cpu/CpuLaunchData.h"
  +++ |+#include <memory>
   25 |
../src/backend/common/Workers.h:63:65: error: expected ‘,’ or ‘...’ before ‘<’ token
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                                                 ^
../src/backend/cpu/CpuBackend.cpp: In member function ‘void xmrig::CpuBackendPrivate::start()’:
../src/backend/cpu/CpuBackend.cpp:162:41: error: no matching function for call to ‘xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> >&, std::shared_ptr<xmrig::Benchmark>&)’
  162 |         workers.start(threads, benchmark);
      |                                         ^
In file included from ../src/backend/cpu/CpuBackend.cpp:34:
../src/backend/common/Workers.h:54:17: note: candidate: ‘void xmrig::Workers<T>::start(const std::vector<T>&) [with T = xmrig::CpuLaunchData]’
   54 |     inline void start(const std::vector<T> &data)   { start(data, true); }
      |                 ^~~~~
../src/backend/common/Workers.h:54:17: note:   candidate expects 1 argument, 2 provided
../src/backend/common/Workers.h:63:10: note: candidate: ‘void xmrig::Workers<T>::start(const std::vector<T>&, int) [with T = xmrig::CpuLaunchData]’
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |          ^~~~~
../src/backend/common/Workers.h:63:44: note:   no known conversion for argument 2 from ‘std::shared_ptr<xmrig::Benchmark>’ to ‘int’
   63 |     void start(const std::vector<T> &data, const std::shared_ptr<Benchmark> &benchmark);
      |                                            ^~~~~~~~~~~~~~~~~~~~~
../src/backend/common/Workers.h:70:10: note: candidate: ‘void xmrig::Workers<T>::start(const std::vector<T>&, bool) [with T = xmrig::CpuLaunchData]’
   70 |     void start(const std::vector<T> &data, bool sleep);
      |          ^~~~~
../src/backend/common/Workers.h:70:49: note:   no known conversion for argument 2 from ‘std::shared_ptr<xmrig::Benchmark>’ to ‘bool’
   70 |     void start(const std::vector<T> &data, bool sleep);
      |                                            ~~~~~^~~~~
```

## Spudz76 | 2021-04-01T19:31:47+00:00
I know this has already been merged, but I compile without GPUs all the time and never hit this error, weird.

## 00-matt | 2021-04-01T19:43:04+00:00
It used to work okay. It got broken by commit 36c1cb23e which has been
included since v6.5.0.


# Action History
- Created by: 00-matt | 2021-04-01T09:56:06+00:00
- Closed at: 2021-04-06T14:11:55+00:00
