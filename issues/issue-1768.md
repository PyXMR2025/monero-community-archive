---
title: 'advanced: No rule to make target `../hwloc-2.1.0/hwloc/.libs/libhwloc.a'',
  needed by `xmrig'''
source_url: https://github.com/xmrig/xmrig/issues/1768
author: mp0wr
assignees: []
labels: []
created_at: '2020-07-10T04:39:39+00:00'
updated_at: '2020-07-10T04:48:03+00:00'
type: issue
status: closed
closed_at: '2020-07-10T04:48:03+00:00'
---

# Original Description
**Describe the bug**
macos build Advanced failed. Message implies that libhwloc is unneeded. 

**To Reproduce**

1. go https://xmrig.com/docs/miner/macos-build 
2. preparation steps
3. perform Basic Steps. success.
4. perform Advanced steps. Note that 
    - `cd xmrig` is ambiguous
    - `cd ../build` does not work in context of these steps. after step 2, you are already in `build`

**Expected behavior**
Basic steps would set up xmrig.
Advanced steps would build upon that, by replacing `hwloc` with a custom-built version.
Build would succeed

**Required data**
 - Miner log as text or screenshot
```
brew install cmake libuv openssl hwloc
# ...
Warning: cmake 3.17.3 is already installed and up-to-date
To reinstall 3.17.3, run `brew reinstall cmake`
Warning: libuv 1.38.1 is already installed and up-to-date
To reinstall 1.38.1, run `brew reinstall libuv`
Warning: openssl@1.1 1.1.1g is already installed and up-to-date
To reinstall 1.1.1g, run `brew reinstall openssl@1.1`
Warning: hwloc 2.2.0 is already installed and up-to-date
To reinstall 2.2.0, run `brew reinstall hwloc`

mkdir xmrig/build
2020-07-09 21:03:43 ~/bin 
cd xmrig/build 
cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl

-- The C compiler identification is AppleClang 11.0.3.11030032
-- The CXX compiler identification is AppleClang 11.0.3.11030032
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/local/lib/libhwloc.dylib  
-- Found UV: /usr/local/lib/libuv.a  
-- Looking for _rotr
-- Looking for _rotr - found
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Failed
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
-- The ASM compiler identification is Clang
-- Found assembler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Found OpenSSL: /usr/local/opt/openssl/lib/libcrypto.a (found version "1.1.1g")  
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/<USERNAME>/bin/xmrig/build
2020-07-09 21:04:18 ~/bin/xmrig/build 
make -j$(sysctl -n hw.logicalcpu)
Scanning dependencies of target argon2-avx2
Scanning dependencies of target xmrig-asm
Scanning dependencies of target ethash
Scanning dependencies of target argon2-avx512f
Scanning dependencies of target argon2-xop
Scanning dependencies of target argon2-sse2
Scanning dependencies of target argon2-ssse3
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  5%] Linking C static library libxmrig-asm.a
[  5%] Built target xmrig-asm
[  5%] Linking C static library libargon2-xop.a
[  5%] Built target argon2-xop
[  5%] Linking C static library libargon2-sse2.a
[  6%] Linking C static library libargon2-avx512f.a
[  7%] Linking C static library libargon2-avx2.a
[  7%] Linking C static library libargon2-ssse3.a
[  7%] Linking C static library libethash.a
[  7%] Built target argon2-avx512f
[  7%] Built target argon2-sse2
[  7%] Built target argon2-avx2
[  7%] Built target argon2-ssse3
Scanning dependencies of target argon2
[  7%] Built target ethash
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
/Users/<USERNAME>/bin/xmrig/src/base/kernel/Entry.cpp:87:56: warning: adding 'int' to a string does not append to the string
      [-Wstring-plus-int]
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                  ~~~~~~~~~~~~~~~~~~~~~^~~
/Users/<USERNAME>/bin/xmrig/src/base/kernel/Entry.cpp:87:56: note: use array indexing to silence this warning
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                                       ^
                                  &                    [  ]
/Users/<USERNAME>/bin/xmrig/src/base/kernel/config/BaseConfig.cpp:158:56: warning: adding 'int' to a string does not append to the
      string [-Wstring-plus-int]
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                  ~~~~~~~~~~~~~~~~~~~~~^~~
/Users/<USERNAME>/bin/xmrig/src/base/kernel/config/BaseConfig.cpp:158:56: note: use array indexing to silence this warning
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                                       ^
                                  &                    [  ]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
1 warning generated.
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
1 warning generated.
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 31%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
In file included from /Users/<USERNAME>/bin/xmrig/src/base/net/http/HttpListener.cpp:20:
/Users/<USERNAME>/bin/xmrig/src/base/net/http/HttpListener.h:38:17: warning: private field 'm_tag' is not used
      [-Wunused-private-field]
    const char *m_tag;
                ^
1 warning generated.
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaAstroBWTRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaKawPowRunner.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_mac.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
/Users/<USERNAME>/bin/xmrig/src/crypto/randomx/randomx.cpp:199:17: warning: function 'Log2' is not needed and will not be emitted
      [-Wunneeded-internal-declaration]
static uint32_t Log2(size_t value) { return (value > 1) ? (Log2(value / 2) + 1) : 0; }
                ^
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
1 warning generated.
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 94%] Building ASM object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3_256_avx2.S.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPCache.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPHash.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o
/Users/<USERNAME>/bin/xmrig/src/crypto/kawpow/KPCache.cpp:94:47: warning: lambda capture 'cache_nodes' is not used
      [-Wunused-lambda-capture]
            threads.emplace_back([this, a, b, cache_nodes, &cache]() {
                                            ~~^~~~~~~~~~~
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o
1 warning generated.
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
	[100%] Linking CXX executable xmrig
[100%] Built target xmrig
2020-07-09 21:05:16 ~/bin/xmrig/build 
cd ..
2020-07-09 21:05:54 ~/bin/xmrig 
curl -O https://download.open-mpi.org/release/hwloc/v2.1/hwloc-2.1.0.tar.bz2

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 6125k  100 6125k    0     0  2333k      0  0:00:02  0:00:02 --:--:-- 2333k
2020-07-09 21:06:04 ~/bin/xmrig 
tar xjf hwloc-2.1.0.tar.bz2
cd hwloc-2.1.0
./configure --disable-shared --enable-static --disable-io --disable-libxml2

###
### Configuring hwloc distribution tarball
### Startup tests
###
checking build system type... x86_64-apple-darwin19.5.0
checking host system type... x86_64-apple-darwin19.5.0
checking target system type... x86_64-apple-darwin19.5.0
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./config/install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether UID '501' is supported by ustar format... yes
checking whether GID '20' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking whether make supports nested variables... (cached) yes
checking whether make supports the include directive... yes (GNU style)
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking dependency style of gcc... gcc3
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking for ar... ar
checking the archiver (ar) interface... ar
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld
checking if the linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) is GNU ld... no
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 196608
checking how to convert x86_64-apple-darwin19.5.0 file names to x86_64-apple-darwin19.5.0 format... func_convert_file_noop
checking how to convert x86_64-apple-darwin19.5.0 file names to toolchain format... func_convert_file_noop
checking for /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for archiver @FILE support... no
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for a working dd... /bin/dd
checking how to truncate binary pipes... /bin/dd bs=4096 count=1
checking for mt... no
checking if : is a manifest tool... no
checking for dsymutil... dsymutil
checking for nmedit... nmedit
checking for lipo... lipo
checking for otool... otool
checking for otool64... no
checking for -single_module linker flag... yes
checking for -exported_symbols_list linker flag... yes
checking for -force_load linker flag... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... yes
checking for gcc option to produce PIC... -fno-common -DPIC
checking if gcc PIC flag -fno-common -DPIC works... yes
checking if gcc static flag -static works... no
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin19.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking for dlopen in -ldl... yes
checking whether a program can dlopen itself... yes
checking whether a statically linked program can dlopen itself... yes
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld
checking if the linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) is GNU ld... no
checking whether the g++ linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) supports shared libraries... yes
checking for g++ option to produce PIC... -fno-common -DPIC
checking if g++ PIC flag -fno-common -DPIC works... yes
checking if g++ static flag -static works... no
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin19.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking for gcc... (cached) gcc
checking whether we are using the GNU C compiler... (cached) yes
checking whether gcc accepts -g... (cached) yes
checking for gcc option to accept ISO C89... (cached) none needed
checking whether gcc understands -c and -o together... (cached) yes
checking dependency style of gcc... (cached) gcc3
checking for gcc option to accept ISO C99... none needed
checking for pkg-config... no
checking for X... no

###
### Configuring hwloc core
###
checking hwloc building mode... standalone
configure: hwloc builddir: /Users/<USERNAME>/bin/xmrig/hwloc-2.1.0
configure: hwloc srcdir: /Users/<USERNAME>/bin/xmrig/hwloc-2.1.0
checking for hwloc version... 2.1.0
checking if want hwloc maintainer support... disabled
checking for hwloc directory prefix... (none)
checking for hwloc symbol prefix... hwloc_
checking for gcc option to accept ISO C99... (cached) none needed
checking size of void *... 8
checking which OS support to include... Darwin
checking which CPU support to include... x86_64
checking size of unsigned long... 8
checking size of unsigned int... 4
checking for the C compiler vendor... gnu
checking for __attribute__... yes
checking for __attribute__(aligned)... yes
checking for __attribute__(always_inline)... yes
checking for __attribute__(cold)... yes
checking for __attribute__(const)... yes
checking for __attribute__(deprecated)... yes
checking for __attribute__(format)... yes
checking for __attribute__(hot)... yes
checking for __attribute__(malloc)... yes
checking for __attribute__(may_alias)... yes
checking for __attribute__(no_instrument_function)... yes
checking for __attribute__(nonnull)... yes
checking for __attribute__(noreturn)... yes
checking for __attribute__(packed)... yes
checking for __attribute__(pure)... yes
checking for __attribute__(sentinel)... yes
checking for __attribute__(unused)... yes
checking for __attribute__(warn_unused_result)... yes
checking for __attribute__(weak_alias)... no
checking if gcc supports -fvisibility=hidden... yes
checking whether to enable symbol visibility... yes (via -fvisibility=hidden)
configure: WARNING: "-fvisibility=hidden" has been added to the hwloc CFLAGS
checking whether the C compiler rejects function calls with too many arguments... yes
checking whether the C compiler rejects function calls with too few arguments... yes
checking for unistd.h... (cached) yes
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking for strings.h... (cached) yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking for strcasecmp... yes
checking whether strcasecmp is declared... yes
checking whether function strcasecmp has a complete prototype... yes
checking for strncasecmp... yes
checking whether strncasecmp is declared... yes
checking whether function strncasecmp has a complete prototype... yes
checking for strftime... yes
checking for setlocale... yes
checking for stdint.h... (cached) yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking for KAFFINITY... no
checking for PROCESSOR_CACHE_TYPE... no
checking for CACHE_DESCRIPTOR... no
checking for LOGICAL_PROCESSOR_RELATIONSHIP... no
checking for RelationProcessorPackage... no
checking for SYSTEM_LOGICAL_PROCESSOR_INFORMATION... no
checking for GROUP_AFFINITY... no
checking for PROCESSOR_RELATIONSHIP... no
checking for NUMA_NODE_RELATIONSHIP... no
checking for CACHE_RELATIONSHIP... no
checking for PROCESSOR_GROUP_INFO... no
checking for GROUP_RELATIONSHIP... no
checking for SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX... no
checking for PSAPI_WORKING_SET_EX_BLOCK... no
checking for PSAPI_WORKING_SET_EX_INFORMATION... no
checking for PROCESSOR_NUMBER... no
checking for main in -lgdi32... no
checking for PostQuitMessage in -luser32... no
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking sys/lgrp_user.h usability... no
checking sys/lgrp_user.h presence... no
checking for sys/lgrp_user.h... no
checking kstat.h usability... no
checking kstat.h presence... no
checking for kstat.h... no
checking whether fabsf is declared... yes
checking for fabsf in -lm... yes
checking whether modff is declared... yes
checking for modff in -lm... yes
checking picl.h usability... no
checking picl.h presence... no
checking for picl.h... no
checking whether _SC_NPROCESSORS_ONLN is declared... yes
checking whether _SC_NPROCESSORS_CONF is declared... yes
checking whether _SC_NPROC_ONLN is declared... no
checking whether _SC_NPROC_CONF is declared... no
checking whether _SC_PAGESIZE is declared... yes
checking whether _SC_PAGE_SIZE is declared... yes
checking whether _SC_LARGE_PAGESIZE is declared... no
checking mach/mach_host.h usability... yes
checking mach/mach_host.h presence... yes
checking for mach/mach_host.h... yes
checking mach/mach_init.h usability... yes
checking mach/mach_init.h presence... yes
checking for mach/mach_init.h... yes
checking for host_info... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes
checking for sys/sysctl.h... yes
checking whether CTL_HW is declared... yes
checking whether HW_NCPU is declared... yes
checking whether strtoull is declared... yes
checking for ssize_t... yes
checking whether snprintf is declared... yes
checking whether _strdup is declared... no
checking whether _putenv is declared... no
checking whether snprintf is correct... yes
checking for sysctl... yes
checking for sysctlbyname... yes
checking whether getprogname is declared... yes
checking whether getexecname is declared... no
checking whether GetModuleFileName is declared... no
checking for program_invocation_name... no
checking for __progname... yes
checking for pthread_t... yes
checking whether sched_getcpu is declared... no
checking whether sched_setaffinity is declared... no
checking for working CPU_SET... no
checking for working CPU_SET_S... no
checking for working syscall with 6 parameters... yes
checking for lib... no
checking for bash... /bin/sh
checking for ffs... yes
checking whether ffs is declared... yes
checking whether function ffs has a complete prototype... yes
checking for ffsl... yes
checking whether ffsl is declared... yes
checking whether function ffsl has a complete prototype... yes
checking for fls... yes
checking whether fls is declared... yes
checking whether function fls has a complete prototype... yes
checking for flsl... yes
checking whether flsl is declared... yes
checking whether function flsl has a complete prototype... yes
checking for clz... no
checking for clzl... no
checking for openat... yes
checking malloc.h usability... no
checking malloc.h presence... no
checking for malloc.h... no
checking for getpagesize... yes
checking for memalign... no
checking for posix_memalign... yes
checking sys/utsname.h usability... yes
checking sys/utsname.h presence... yes
checking for sys/utsname.h... yes
checking for uname... yes
checking valgrind/valgrind.h usability... no
checking valgrind/valgrind.h presence... no
checking for valgrind/valgrind.h... no
checking whether RUNNING_ON_VALGRIND is declared... no
checking pthread_np.h usability... no
checking pthread_np.h presence... no
checking for pthread_np.h... no
checking whether pthread_setaffinity_np is declared... no
checking whether pthread_getaffinity_np is declared... no
checking for sched_setaffinity... no
checking for sys/cpuset.h... no
checking for cpuset_setaffinity... no
checking for library containing pthread_getthrds_np... no
checking for cpuset_setid... no
checking libudev.h usability... no
checking libudev.h presence... no
checking for libudev.h... no
checking X11/Xlib.h usability... no
checking X11/Xlib.h presence... no
checking for X11/Xlib.h... no
checking for x86 cpuid... yes
checking for pthread_mutex_lock... yes
checking if plugin support is enabled... no
checking components to build statically...  noos xml synthetic xml_nolibxml darwin x86
checking components to build as plugins... 
checking for diff... /usr/bin/diff

###
### Configuring hwloc documentation
###
checking if this is a developer build... no (doxygen generation is optional)
checking for doxygen... no
checking for pdflatex... no
checking for makeindex... no
checking for fig2dev... no
checking for gs... no
checking for epstopdf... no
checking if can build doxygen docs... no
checking for w3m... no
checking for lynx... /usr/local/bin/lynx
checking if can build top-level README... yes
checking if will build doxygen docs... no
checking if will install doxygen docs... yes
checking whether to enable "picky" compiler mode... no (default)

###
### Configuring hwloc command line utilities
###
checking for CAIRO... cannot check without pkg-config
checking for wchar_t... yes
checking for putwc... yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking for setlocale... (cached) yes
checking for uselocale... yes
checking xlocale.h usability... yes
checking xlocale.h presence... yes
checking for xlocale.h... yes
checking for setlocale... (cached) yes
checking for uselocale... (cached) yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking for nl_langinfo... yes
checking termcap support using ncurses and ... no
checking termcap support using ncurses and -ltermcap... yes
checking whether diff accepts -u... yes
checking whether diff accepts -w... yes
checking whether bind is declared... yes
checking for bind in -lsocket... no
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking for clock_gettime... yes

###
### Configuring tests
###
checking for pthread_self in -lpthread... yes
checking for NUMA... cannot check without pkg-config
checking for numa_available in -lnuma... no
checking for stdlib.h... (cached) yes
checking for mkstemp... yes
checking infiniband/verbs.h usability... no
checking infiniband/verbs.h presence... no
checking for infiniband/verbs.h... no
checking for xmllint... xmllint
checking for bunzip2... bunzip2
checking if CXX works... yes
checking whether diff accepts -u... yes

###
### Performing final hwloc configuration
###
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating include/Makefile
config.status: creating hwloc/Makefile
config.status: creating doc/Makefile
config.status: creating doc/examples/Makefile
config.status: creating doc/doxygen-config.cfg
config.status: creating utils/Makefile
config.status: creating utils/hwloc/Makefile
config.status: creating utils/lstopo/Makefile
config.status: creating hwloc.pc
config.status: creating netloc/Makefile
config.status: creating utils/netloc/infiniband/Makefile
config.status: creating utils/netloc/draw/Makefile
config.status: creating utils/netloc/scotch/Makefile
config.status: creating utils/netloc/mpi/Makefile
config.status: creating netloc.pc
config.status: creating netlocscotch.pc
config.status: creating tests/Makefile
config.status: creating tests/hwloc/Makefile
config.status: creating tests/hwloc/linux/Makefile
config.status: creating tests/hwloc/linux/allowed/Makefile
config.status: creating tests/hwloc/linux/gather/Makefile
config.status: creating tests/hwloc/x86/Makefile
config.status: creating tests/hwloc/x86+linux/Makefile
config.status: creating tests/hwloc/xml/Makefile
config.status: creating tests/hwloc/ports/Makefile
config.status: creating tests/hwloc/rename/Makefile
config.status: creating tests/hwloc/linux/allowed/test-topology.sh
config.status: creating tests/hwloc/linux/gather/test-gather-topology.sh
config.status: creating tests/hwloc/linux/test-topology.sh
config.status: creating tests/hwloc/x86/test-topology.sh
config.status: creating tests/hwloc/x86+linux/test-topology.sh
config.status: creating tests/hwloc/xml/test-topology.sh
config.status: creating tests/hwloc/wrapper.sh
config.status: creating utils/hwloc/hwloc-compress-dir
config.status: creating utils/hwloc/hwloc-gather-topology
config.status: creating utils/hwloc/test-hwloc-annotate.sh
config.status: creating utils/hwloc/test-hwloc-calc.sh
config.status: creating utils/hwloc/test-hwloc-compress-dir.sh
config.status: creating utils/hwloc/test-hwloc-diffpatch.sh
config.status: creating utils/hwloc/test-hwloc-distrib.sh
config.status: creating utils/hwloc/test-hwloc-info.sh
config.status: creating utils/hwloc/test-fake-plugin.sh
config.status: creating utils/hwloc/test-hwloc-dump-hwdata/Makefile
config.status: creating utils/hwloc/test-hwloc-dump-hwdata/test-hwloc-dump-hwdata.sh
config.status: creating utils/lstopo/test-lstopo.sh
config.status: creating utils/lstopo/test-lstopo-shmem.sh
config.status: creating utils/netloc/infiniband/netloc_ib_gather_raw
config.status: creating contrib/hwloc-ps.www/Makefile
config.status: creating contrib/systemd/Makefile
config.status: creating contrib/misc/Makefile
config.status: creating contrib/windows/Makefile
config.status: creating contrib/windows/test-windows-version.sh
config.status: creating tests/netloc/Makefile
config.status: creating tests/netloc/tests.sh
config.status: creating include/private/autogen/config.h
config.status: creating include/hwloc/autogen/config.h
config.status: linking hwloc/topology-solaris.c to tests/hwloc/ports/topology-solaris.c
config.status: linking hwloc/topology-solaris-chiptype.c to tests/hwloc/ports/topology-solaris-chiptype.c
config.status: linking hwloc/topology-aix.c to tests/hwloc/ports/topology-aix.c
config.status: linking hwloc/topology-windows.c to tests/hwloc/ports/topology-windows.c
config.status: linking hwloc/topology-darwin.c to tests/hwloc/ports/topology-darwin.c
config.status: linking hwloc/topology-freebsd.c to tests/hwloc/ports/topology-freebsd.c
config.status: linking hwloc/topology-netbsd.c to tests/hwloc/ports/topology-netbsd.c
config.status: linking hwloc/topology-hpux.c to tests/hwloc/ports/topology-hpux.c
config.status: linking hwloc/topology-bgq.c to tests/hwloc/ports/topology-bgq.c
config.status: linking hwloc/topology-opencl.c to tests/hwloc/ports/topology-opencl.c
config.status: linking hwloc/topology-cuda.c to tests/hwloc/ports/topology-cuda.c
config.status: linking hwloc/topology-nvml.c to tests/hwloc/ports/topology-nvml.c
config.status: linking hwloc/topology-gl.c to tests/hwloc/ports/topology-gl.c
config.status: linking utils/lstopo/lstopo-windows.c to tests/hwloc/ports/lstopo-windows.c
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing chmoding-scripts commands

************************************************************************
Could not detect/enable some features such as libxml2 and Cairo support
because pkg-config isn't available.
************************************************************************

-----------------------------------------------------------------------------
Hwloc optional build support status (more details can be found above):

Probe / display I/O devices: no
Graphical output:            no
XML input / output:          basic
Netloc functionality:        no
Plugin support:              no
-----------------------------------------------------------------------------
cd ../build 
2020-07-09 21:07:38 ~/bin/xmrig/build 
ls -1p | grep '/'
CMakeFiles/
src/
2020-07-09 21:07:40 ~/bin/xmrig/build 
cd ../
2020-07-09 21:08:09 ~/bin/xmrig 
lsd
bin/
build/
cmake/
doc/
hwloc-2.1.0/
res/
scripts/
src/
cd ../build/
cd: no such file or directory: ../build/
2020-07-09 21:08:53 ~/bin/xmrig 
cd build 
2020-07-09 21:08:58 ~/bin/xmrig/build 
cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl -DHWLOC_INCLUDE_DIR=../hwloc-2.1.0/include -DHWLOC_LIBRARY=../hwloc-2.1.0/hwloc/.libs/libhwloc.a

-- Found HWLOC: /Users/<USERNAME>/bin/xmrig/hwloc-2.1.0/hwloc/.libs/libhwloc.a  
-- WITH_MSR=OFF
-- argon2: detecting feature 'sse2'...
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- argon2: detecting feature 'avx2'...
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- argon2: feature 'avx512f' detected!
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/<USERNAME>/bin/xmrig/build
2020-07-09 21:09:11 ~/bin/xmrig/build 
make -j$(sysctl -n hw.logicalcpu)

Scanning dependencies of target argon2-xop
Scanning dependencies of target xmrig-asm
Scanning dependencies of target argon2-avx2
Scanning dependencies of target argon2-ssse3
Scanning dependencies of target argon2-avx512f
Scanning dependencies of target argon2-sse2
Scanning dependencies of target ethash
[  0%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  5%] Linking C static library libxmrig-asm.a
[  5%] Linking C static library libargon2-xop.a
[  5%] Built target xmrig-asm
[  5%] Built target argon2-xop
[  5%] Linking C static library libargon2-ssse3.a
[  6%] Linking C static library libargon2-avx512f.a
[  7%] Linking C static library libargon2-avx2.a
[  7%] Linking C static library libethash.a
[  7%] Linking C static library libargon2-sse2.a
[  7%] Built target argon2-ssse3
[  7%] Built target argon2-avx512f
[  7%] Built target ethash
[  7%] Built target argon2-avx2
[  7%] Built target argon2-sse2
Scanning dependencies of target argon2
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
/Users/<USERNAME>/bin/xmrig/src/base/kernel/Entry.cpp:87:56: warning: adding 'int' to a string does not append to the string
      [-Wstring-plus-int]
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                  ~~~~~~~~~~~~~~~~~~~~~^~~
/Users/<USERNAME>/bin/xmrig/src/base/kernel/Entry.cpp:87:56: note: use array indexing to silence this warning
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                                       ^
                                  &                    [  ]
/Users/<USERNAME>/bin/xmrig/src/base/kernel/config/BaseConfig.cpp:158:56: warning: adding 'int' to a string does not append to the
      string [-Wstring-plus-int]
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                  ~~~~~~~~~~~~~~~~~~~~~^~~
/Users/<USERNAME>/bin/xmrig/src/base/kernel/config/BaseConfig.cpp:158:56: note: use array indexing to silence this warning
        constexpr const char *v = OPENSSL_VERSION_TEXT + 8;
                                                       ^
                                  &                    [  ]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
1 warning generated.
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
1 warning generated.
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 31%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
In file included from /Users/<USERNAME>/bin/xmrig/src/base/net/http/HttpListener.cpp:20:
/Users/<USERNAME>/bin/xmrig/src/base/net/http/HttpListener.h:38:17: warning: private field 'm_tag' is not used
      [-Wunused-private-field]
    const char *m_tag;
                ^
1 warning generated.
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaAstroBWTRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaKawPowRunner.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_mac.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
/Users/<USERNAME>/bin/xmrig/src/crypto/randomx/randomx.cpp:199:17: warning: function 'Log2' is not needed and will not be emitted
      [-Wunneeded-internal-declaration]
static uint32_t Log2(size_t value) { return (value > 1) ? (Log2(value / 2) + 1) : 0; }
                ^
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
1 warning generated.
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 94%] Building ASM object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3_256_avx2.S.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPCache.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPHash.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o
/Users/<USERNAME>/bin/xmrig/src/crypto/kawpow/KPCache.cpp:94:47: warning: lambda capture 'cache_nodes' is not used
      [-Wunused-lambda-capture]
            threads.emplace_back([this, a, b, cache_nodes, &cache]() {
                                            ~~^~~~~~~~~~~
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.o
1 warning generated.
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
make[2]: *** No rule to make target `../hwloc-2.1.0/hwloc/.libs/libhwloc.a', needed by `xmrig'.  Stop.
make[2]: *** Waiting for unfinished jobs....
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
2020-07-09 21:10:22 ~/bin/xmrig/build 
make -j$(sysctl -n hw.logicalcpu)
[  2%] Built target argon2-avx2
[  2%] Built target argon2-avx512f
[  4%] Built target argon2-ssse3
[  5%] Built target argon2-xop
[  6%] Built target xmrig-asm
[  7%] Built target ethash
[  7%] Built target argon2-sse2
[ 10%] Built target argon2
make[2]: *** No rule to make target `../hwloc-2.1.0/hwloc/.libs/libhwloc.a', needed by `xmrig'.  Stop.
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

cd ~/bin/xmrig/build
otool -L xmrig
xmrig:
	/usr/local/opt/hwloc/lib/libhwloc.15.dylib (compatibility version 18.0.0, current version 18.0.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 902.1.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1281.100.1)

```

 - Config file or command line (without wallets)
n/a. was build-time issue. have not run xmrig.

 - OS: [e.g. Windows]
macOS Catalina 10.15.5 (19F101)

 - For GPU related issues: information about GPUs and driver version.

```
AMD Radeon R9 M370X:

  Chipset Model:	AMD Radeon R9 M370X
  Type:	GPU
  Bus:	PCIe
  PCIe Lane Width:	x8
  VRAM (Total):	2 GB
  Vendor:	AMD (0x1002)
  Device ID:	0x6821
  Revision ID:	0x0083
  ROM Revision:	113-C5670E-945
  VBIOS Version:	113-C567A1-006
  EFI Driver Version:	01.00.945
  Automatic Graphics Switching:	Supported
  gMux Version:	4.0.20 [3.2.8]
  Metal:	Supported, feature set macOS GPUFamily2 v1
```

**Additional context**

I want to run xmrig on a macbook pro and use GPU + CPU.


# Discussion History
## mp0wr | 2020-07-10T04:48:02+00:00
my bad. works as expected.

these assumptions of mine were wrong:


- Basic steps would set up xmrig.
- Advanced steps would build upon that, by replacing hwloc with a custom-built version.

# Action History
- Created by: mp0wr | 2020-07-10T04:39:39+00:00
- Closed at: 2020-07-10T04:48:03+00:00
