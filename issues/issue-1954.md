---
title: v6.6.0 build issues
source_url: https://github.com/xmrig/xmrig/issues/1954
author: k0ste
assignees: []
labels: []
created_at: '2020-11-24T08:58:04+00:00'
updated_at: '2020-11-30T12:37:20+00:00'
type: issue
status: closed
closed_at: '2020-11-30T12:37:20+00:00'
---

# Original Description
```shell
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 10.2.0
-- The CXX compiler identification is GNU 10.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/libhwloc.so  
-- Found UV: /usr/lib/libuv.so  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=ON
CMake Deprecation Warning at src/3rdparty/argon2/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


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
-- Found assembler: /usr/bin/gcc
CMake Deprecation Warning at src/3rdparty/libethash/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Found OpenSSL: /usr/lib/libcrypto.so (found version "1.1.1h")  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/build
Scanning dependencies of target argon2-xop
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  1%] Linking C static library libargon2-xop.a
[  1%] Built target argon2-xop
Scanning dependencies of target argon2-avx512f
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  1%] Linking C static library libargon2-avx512f.a
[  1%] Built target argon2-avx512f
Scanning dependencies of target argon2-ssse3
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  2%] Linking C static library libargon2-ssse3.a
[  2%] Built target argon2-ssse3
Scanning dependencies of target argon2-sse2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  3%] Linking C static library libargon2-sse2.a
[  3%] Built target argon2-sse2
Scanning dependencies of target argon2-avx2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  4%] Linking C static library libargon2-avx2.a
[  4%] Built target argon2-avx2
Scanning dependencies of target argon2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[  7%] Linking C static library libargon2.a
[  7%] Built target argon2
Scanning dependencies of target ethash
[  7%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  8%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  8%] Linking C static library libethash.a
[  8%] Built target ethash
Scanning dependencies of target xmrig-asm
[  9%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  9%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[ 10%] Linking C static library libxmrig-asm.a
[ 10%] Built target xmrig-asm
Scanning dependencies of target xmrig
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
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
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 31%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
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
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaAstroBWTRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaKawPowRunner.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_unix.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
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
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:1:3: error: invalid preprocessing directive #Copyright
    1 | # Copyright (c) 2018-2019, tevador <tevador@gmail.com>
      |   ^~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:3:3: error: invalid preprocessing directive #All
    3 | # All rights reserved.
      |   ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:5:3: error: invalid preprocessing directive #Redistribution
    5 | # Redistribution and use in source and binary forms, with or without
      |   ^~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:6:3: error: invalid preprocessing directive #modification
    6 | # modification, are permitted provided that the following conditions are met:
      |   ^~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:7:4: error: invalid preprocessing directive #*
    7 | #  * Redistributions of source code must retain the above copyright
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:8:6: error: invalid preprocessing directive #notice
    8 | #    notice, this list of conditions and the following disclaimer.
      |      ^~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:9:4: error: invalid preprocessing directive #*
    9 | #  * Redistributions in binary form must reproduce the above copyright
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:10:6: error: invalid preprocessing directive #notice
   10 | #    notice, this list of conditions and the following disclaimer in the
      |      ^~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:11:6: error: invalid preprocessing directive #documentation
   11 | #    documentation and/or other materials provided with the distribution.
      |      ^~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:12:4: error: invalid preprocessing directive #*
   12 | #  * Neither the name of the copyright holder nor the
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:13:6: error: invalid preprocessing directive #names
   13 | #    names of its contributors may be used to endorse or promote products
      |      ^~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:14:6: error: invalid preprocessing directive #derived
   14 | #    derived from this software without specific prior written permission.
      |      ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:16:3: error: invalid preprocessing directive #THIS
   16 | # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
      |   ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:17:3: error: invalid preprocessing directive #ANY
   17 | # ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
      |   ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:18:3: error: invalid preprocessing directive #WARRANTIES
   18 | # WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
      |   ^~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:19:3: error: invalid preprocessing directive #DISCLAIMED
   19 | # DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
      |   ^~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:20:3: error: invalid preprocessing directive #FOR
   20 | # FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
      |   ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:21:3: error: invalid preprocessing directive #DAMAGES
   21 | # DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
      |   ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:22:3: error: invalid preprocessing directive #SERVICES
   22 | # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
      |   ^~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:23:3: error: invalid preprocessing directive #CAUSED
   23 | # CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
      |   ^~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:24:3: error: invalid preprocessing directive #OR
   24 | # OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
      |   ^~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:25:3: error: invalid preprocessing directive #OF
   25 | # OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
      |   ^~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:27:1: error: expected identifier or ‘(’ before ‘.’ token
   27 | .intel_syntax noprefix
      | ^
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:84:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:1:3: error: stray ‘#’ in program
    1 |  ;# callee-saved registers - System V AMD64 ABI
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:1:11: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘-’ token
    1 |  ;# callee-saved registers - System V AMD64 ABI
      |           ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:9:3: error: stray ‘#’ in program
    9 |  ;# function arguments
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:9:5: error: unknown type name ‘function’; did you mean ‘union’?
    9 |  ;# function arguments
      |     ^~~~~~~~
      |     union
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:10:2: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘mov’
   10 |  mov rbx, rcx                ;# loop counter
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:10:2: error: unknown type name ‘mov’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:10:31: error: stray ‘#’ in program
   10 |  mov rbx, rcx                ;# loop counter
      |                               ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:10:33: error: unknown type name ‘loop’
   10 |  mov rbx, rcx                ;# loop counter
      |                                 ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:11:2: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘push’
   11 |  push rdi                    ;# RegisterFile& registerFile
      |  ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:11:2: error: unknown type name ‘push’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:11:31: error: stray ‘#’ in program
   11 |  push rdi                    ;# RegisterFile& registerFile
      |                               ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:11:45: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘&’ token
   11 |  push rdi                    ;# RegisterFile& registerFile
      |                                             ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:13:31: error: stray ‘#’ in program
   13 |  mov rbp, qword ptr [rsi]    ;# "mx", "ma"
      |                               ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:13:33: error: expected identifier or ‘(’ before string constant
   13 |  mov rbp, qword ptr [rsi]    ;# "mx", "ma"
      |                                 ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:14:31: error: stray ‘#’ in program
   14 |  mov rdi, qword ptr [rsi+8]  ;# uint8_t* dataset
      |                               ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:14:33: error: unknown type name ‘uint8_t’
   14 |  mov rdi, qword ptr [rsi+8]  ;# uint8_t* dataset
      |                                 ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:16:3: error: stray ‘#’ in program
   16 |  ;# dataset prefetch for the first iteration of the main loop
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:16:5: error: unknown type name ‘dataset’
   16 |  ;# dataset prefetch for the first iteration of the main loop
      |     ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:16:22: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘for’
   16 |  ;# dataset prefetch for the first iteration of the main loop
      |                      ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:22:31: error: stray ‘#’ in program
   22 |  mov rsi, rdx                ;# uint8_t* scratchpad
      |                               ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:22:33: error: unknown type name ‘uint8_t’
   22 |  mov rsi, rdx                ;# uint8_t* scratchpad
      |                                 ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:24:2: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘mov’
   24 |  mov rax, rbp
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:24:2: error: unknown type name ‘mov’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:26:3: error: stray ‘#’ in program
   26 |  ;# zero integer registers
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:26:5: error: unknown type name ‘zero’
   26 |  ;# zero integer registers
      |     ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:26:18: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘registers’
   26 |  ;# zero integer registers
      |                  ^~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:26:18: error: unknown type name ‘registers’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:36:3: error: stray ‘#’ in program
   36 |  ;# load constant registers
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:36:5: error: unknown type name ‘load’
   36 |  ;# load constant registers
      |     ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:36:19: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘registers’
   36 |  ;# load constant registers
      |                   ^~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_prologue_linux.inc:36:19: error: unknown type name ‘registers’
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:125:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:1:38: error: stray ‘#’ in program
    1 |  xor rbp, rax                       ;# modify "mx"
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:1:47: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before string constant
    1 |  xor rbp, rax                       ;# modify "mx"
      |                                               ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:2:38: error: stray ‘#’ in program
    2 |  mov edx, ebp                       ;# edx = mx
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:2:40: warning: data definition has no type or storage class
    2 |  mov edx, ebp                       ;# edx = mx
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:2:40: warning: type defaults to ‘int’ in declaration of ‘edx’ [-Wimplicit-int]
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:2:46: error: ‘mx’ undeclared here (not in a function)
    2 |  mov edx, ebp                       ;# edx = mx
      |                                              ^~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:3:2: error: expected ‘,’ or ‘;’ before ‘and’
    3 |  and edx, RANDOMX_DATASET_BASE_MASK
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:5:38: error: stray ‘#’ in program
    5 |  ror rbp, 32                        ;# swap "ma" and "mx"
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:5:45: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before string constant
    5 |  ror rbp, 32                        ;# swap "ma" and "mx"
      |                                             ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:6:38: error: stray ‘#’ in program
    6 |  mov edx, ebp                       ;# edx = ma
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:6:40: warning: data definition has no type or storage class
    6 |  mov edx, ebp                       ;# edx = ma
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:6:40: warning: type defaults to ‘int’ in declaration of ‘edx’ [-Wimplicit-int]
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:6:40: error: redefinition of ‘edx’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:2:40: note: previous definition of ‘edx’ was here
    2 |  mov edx, ebp                       ;# edx = mx
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:6:46: error: ‘ma’ undeclared here (not in a function)
    6 |  mov edx, ebp                       ;# edx = ma
      |                                              ^~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:7:2: error: expected ‘,’ or ‘;’ before ‘and’
    7 |  and edx, RANDOMX_DATASET_BASE_MASK
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:8:38: error: stray ‘#’ in program
    8 |  lea rcx, [rdi+rdx]                 ;# dataset cache line
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:8:40: error: unknown type name ‘dataset’
    8 |  lea rcx, [rdi+rdx]                 ;# dataset cache line
      |                                        ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:8:54: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘line’
    8 |  lea rcx, [rdi+rdx]                 ;# dataset cache line
      |                                                      ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:8:54: error: unknown type name ‘line’
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:128:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:1:38: error: stray ‘#’ in program
    1 |  mov rcx, rbp                       ;# ecx = ma
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:1:40: warning: data definition has no type or storage class
    1 |  mov rcx, rbp                       ;# ecx = ma
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:1:40: warning: type defaults to ‘int’ in declaration of ‘ecx’ [-Wimplicit-int]
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:2:2: error: expected ‘,’ or ‘;’ before ‘shr’
    2 |  shr rcx, 32
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:5:38: error: stray ‘#’ in program
    5 |  xor rbp, rax                       ;# modify "mx"
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:5:47: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before string constant
    5 |  xor rbp, rax                       ;# modify "mx"
      |                                               ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:6:38: error: stray ‘#’ in program
    6 |  mov edx, ebp                       ;# edx = mx
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:6:40: warning: data definition has no type or storage class
    6 |  mov edx, ebp                       ;# edx = mx
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:6:40: warning: type defaults to ‘int’ in declaration of ‘edx’ [-Wimplicit-int]
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:6:40: error: redefinition of ‘edx’
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:125:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset.inc:2:40: note: previous definition of ‘edx’ was here
    2 |  mov edx, ebp                       ;# edx = mx
      |                                        ^~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:128:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:7:2: error: expected ‘,’ or ‘;’ before ‘and’
    7 |  and edx, RANDOMX_DATASET_BASE_MASK
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:9:38: error: stray ‘#’ in program
    9 |  ror rbp, 32                        ;# swap "ma" and "mx"
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:9:45: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before string constant
    9 |  ror rbp, 32                        ;# swap "ma" and "mx"
      |                                             ^~~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:131:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:11:38: error: stray ‘#’ in program
   11 |  xor rbp, rax                       ;# modify "mx"
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:11:47: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before string constant
   11 |  xor rbp, rax                       ;# modify "mx"
      |                                               ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:12:38: error: stray ‘#’ in program
   12 |  ror rbp, 32                        ;# swap "ma" and "mx"
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:12:45: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before string constant
   12 |  ror rbp, 32                        ;# swap "ma" and "mx"
      |                                             ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:13:38: error: stray ‘#’ in program
   13 |  mov ebx, ebp                       ;# ecx = ma
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:13:40: warning: data definition has no type or storage class
   13 |  mov ebx, ebp                       ;# ecx = ma
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:13:40: warning: type defaults to ‘int’ in declaration of ‘ecx’ [-Wimplicit-int]
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:13:40: error: redefinition of ‘ecx’
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:128:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_ryzen.inc:1:40: note: previous definition of ‘ecx’ was here
    1 |  mov rcx, rbp                       ;# ecx = ma
      |                                        ^~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:131:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:14:2: error: expected ‘,’ or ‘;’ before ‘and’
   14 |  and ebx, RANDOMX_DATASET_BASE_MASK
      |  ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:15:38: error: stray ‘#’ in program
   15 |  shr ebx, 6                         ;# ebx = Dataset block number
      |                                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:15:40: warning: data definition has no type or storage class
   15 |  shr ebx, 6                         ;# ebx = Dataset block number
      |                                        ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:15:40: warning: type defaults to ‘int’ in declaration of ‘ebx’ [-Wimplicit-int]
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:15:46: error: ‘Dataset’ undeclared here (not in a function); did you mean ‘dataset’?
   15 |  shr ebx, 6                         ;# ebx = Dataset block number
      |                                              ^~~~~~~
      |                                              dataset
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:15:54: error: expected ‘,’ or ‘;’ before ‘block’
   15 |  shr ebx, 6                         ;# ebx = Dataset block number
      |                                                      ^~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:16:3: error: stray ‘#’ in program
   16 |  ;# add ebx, datasetOffset / 64
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:16:5: error: unknown type name ‘add’
   16 |  ;# add ebx, datasetOffset / 64
      |     ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:16:28: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘/’ token
   16 |  ;# add ebx, datasetOffset / 64
      |                            ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:17:3: error: stray ‘#’ in program
   17 |  ;# call 32768
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_read_dataset_sshash_init.inc:17:10: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before numeric constant
   17 |  ;# call 32768
      |          ^~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:158:28: error: stray ‘#’ in program
  158 |  mov rdi, qword ptr [rdi] ;# cache->memory
      |                            ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:158:35: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘->’ token
  158 |  mov rdi, qword ptr [rdi] ;# cache->memory
      |                                   ^~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:159:3: error: stray ‘#’ in program
  159 |  ;# dataset in rsi
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:159:5: error: unknown type name ‘dataset’
  159 |  ;# dataset in rsi
      |     ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:159:16: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘rsi’
  159 |  ;# dataset in rsi
      |                ^~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:159:16: error: unknown type name ‘rsi’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:160:17: error: stray ‘#’ in program
  160 |  mov rbp, rdx  ;# block index
      |                 ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:160:19: error: unknown type name ‘block’
  160 |  mov rbp, rdx  ;# block index
      |                   ^~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:161:2: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘push’
  161 |  push rcx      ;# max. block index
      |  ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:161:2: error: unknown type name ‘push’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:161:17: error: stray ‘#’ in program
  161 |  push rcx      ;# max. block index
      |                 ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:161:22: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘.’ token
  161 |  push rcx      ;# max. block index
      |                      ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:166:13: error: stray ‘#’ in program
  166 |  .byte 232 ;# 0xE8 = call
      |             ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:166:15: error: expected identifier or ‘(’ before numeric constant
  166 |  .byte 232 ;# 0xE8 = call
      |               ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:167:3: error: stray ‘#’ in program
  167 |  ;# .set CALL_LOC,
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:167:5: error: expected identifier or ‘(’ before ‘.’ token
  167 |  ;# .set CALL_LOC,
      |     ^
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:197:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_store.inc:1:3: error: stray ‘#’ in program
    1 |  ;# save VM register values
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_store.inc:1:5: error: unknown type name ‘save’
    1 |  ;# save VM register values
      |     ^~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_store.inc:1:12: error: expected ‘;’ before ‘register’
    1 |  ;# save VM register values
      |            ^~~~~~~~~
      |            ;
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_store.inc:1:22: error: unknown type name ‘values’
    1 |  ;# save VM register values
      |                      ^~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_store.inc:2:6: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘rsp’
    2 |  add rsp, 40
      |      ^~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:201:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_linux.inc:1:3: error: stray ‘#’ in program
    1 |  ;# restore callee-saved registers - System V AMD64 ABI
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_linux.inc:1:5: error: unknown type name ‘restore’
    1 |  ;# restore callee-saved registers - System V AMD64 ABI
      |     ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_linux.inc:1:19: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘-’ token
    1 |  ;# restore callee-saved registers - System V AMD64 ABI
      |                   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_linux.inc:9:3: error: stray ‘#’ in program
    9 |  ;# program finished
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_linux.inc:9:5: error: unknown type name ‘program’
    9 |  ;# program finished
      |     ^~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_epilogue_linux.inc:10:2: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘ret’
   10 |  ret 0
      |  ^~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/jit_compiler_x86_static.S:236:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:2:3: error: stray ‘#’ in program
    2 |  ;#/ 6364136223846793005
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:2:4: error: expected identifier or ‘(’ before ‘/’ token
    2 |  ;#/ 6364136223846793005
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:5:3: error: stray ‘#’ in program
    5 |  ;#/ 9298411001130361340
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:5:4: error: expected identifier or ‘(’ before ‘/’ token
    5 |  ;#/ 9298411001130361340
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:5:6: warning: integer constant is so large that it is unsigned
    5 |  ;#/ 9298411001130361340
      |      ^~~~~~~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:8:3: error: stray ‘#’ in program
    8 |  ;#/ 12065312585734608966
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:8:4: error: expected identifier or ‘(’ before ‘/’ token
    8 |  ;#/ 12065312585734608966
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:8:6: warning: integer constant is so large that it is unsigned
    8 |  ;#/ 12065312585734608966
      |      ^~~~~~~~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:11:3: error: stray ‘#’ in program
   11 |  ;#/ 9306329213124626780
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:11:4: error: expected identifier or ‘(’ before ‘/’ token
   11 |  ;#/ 9306329213124626780
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:11:6: warning: integer constant is so large that it is unsigned
   11 |  ;#/ 9306329213124626780
      |      ^~~~~~~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:14:3: error: stray ‘#’ in program
   14 |  ;#/ 5281919268842080866
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:14:4: error: expected identifier or ‘(’ before ‘/’ token
   14 |  ;#/ 5281919268842080866
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:17:3: error: stray ‘#’ in program
   17 |  ;#/ 10536153434571861004
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:17:4: error: expected identifier or ‘(’ before ‘/’ token
   17 |  ;#/ 10536153434571861004
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:17:6: warning: integer constant is so large that it is unsigned
   17 |  ;#/ 10536153434571861004
      |      ^~~~~~~~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:20:3: error: stray ‘#’ in program
   20 |  ;#/ 3398623926847679864
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:20:4: error: expected identifier or ‘(’ before ‘/’ token
   20 |  ;#/ 3398623926847679864
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:23:3: error: stray ‘#’ in program
   23 |  ;#/ 9549104520008361294
      |   ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:23:4: error: expected identifier or ‘(’ before ‘/’ token
   23 |  ;#/ 9549104520008361294
      |    ^
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-6.6.0/src/crypto/randomx/asm/program_sshash_constants.inc:23:6: warning: integer constant is so large that it is unsigned
   23 |  ;#/ 9549104520008361294
      |      ^~~~~~~~~~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2695: CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:155: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2
==> ERROR: A failure occurred in build().
    Aborting...
```

# Discussion History
## s-bernard | 2020-11-24T17:24:41+00:00
Caused by cmake 3.19.0, I suspect because of 

> Changes made since CMake 3.19.0 include the following.

> CMake 3.19.0 compiles source files with the LANGUAGE property by passing an explicit language flag such as -x c. This is consistent with the property’s documented meaning that the source file is written in the specified language. However, it can break projects that were using the property only to cause the specified language’s compiler to be used. This has been reverted to restore behavior from CMake 3.18 and below.

## jivanpal | 2020-11-28T19:08:28+00:00
Can confirm that CMake 3.19.0 causes the issue; with CMake 3.19.1, the problem is resolved.

## k0ste | 2020-11-30T12:37:16+00:00
@jivanpal yes, thanks

# Action History
- Created by: k0ste | 2020-11-24T08:58:04+00:00
- Closed at: 2020-11-30T12:37:20+00:00
