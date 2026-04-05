---
title: armv8 termux (pixel 3) wont compile binary
source_url: https://github.com/xmrig/xmrig/issues/2434
author: calvintam236
assignees: []
labels: []
created_at: '2021-06-10T09:20:58+00:00'
updated_at: '2021-06-13T13:37:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Just normal build from source with cmake params `-DWITH_HWLOC=OFF` and `-DCMAKE_CXX_COMPILER=clang`.

**Expected behavior**
A clear and concise description of what you expected to happen.
Build successfully.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.
ARMv8, Termux, Pixel 3
```bash
$ cmake .. -DWITH_HWLOC=OFF -DCMAKE_CXX_COMPILER=clang
-- The C compiler identification is Clang 12.0.0        -- The CXX compiler identification is Clang 12.0.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/clang - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so                                                       -- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /data/data/com.termux/files/usr/lib/libcrypto.so (found version "1.1.1h")
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrig/build
$ make -j$(nproc)
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o                       [  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o                               [  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  4%] Linking C static library libethash.a
[  4%] Built target ethash                              [  4%] Linking C static library libargon2.a
[  4%] Built target argon2
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o                             [  6%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o               [  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o                                      [  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o                                           [  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o                                     [  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o                                [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o                              [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o                       [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o                          [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o                             [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o                                       [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o                                      [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o                                       [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o                                       [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o                                      [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o                         [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o                      [ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o                              [ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o                                     [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o                                  [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o                                   [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o                                      [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o                                [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o                                [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o                               [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o                             [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o                                    [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o                           [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o                               [ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o                                  [ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o                         [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o                                 [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o                                [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o                             [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o                               [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o          [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o        [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o                                  [ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o                             [ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o                              [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o                                  [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o                                        [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o                                     [ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o                                      [ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o                           [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o                     [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o                [ 28%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o                                       [ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o                                        [ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o                          [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o                      [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o                              [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o                                [ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o                            [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o                               [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o                                [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o                                [ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o                   [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o                   [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o                              [ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o                                       [ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o                                [ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o                                 [ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o                                 [ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o                                [ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o                                 [ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o                 [ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o                        [ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o                           [ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o    [ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o                      [ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o                      [ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o                    [ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o                   [ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o            [ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o           [ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o    [ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o  [ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o    [ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o                [ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o                 [ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o                                                     [ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o                                                  [ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o                                                    [ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o   [ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o                [ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o                               [ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o                               [ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o                              [ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o                               [ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o                   [ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o                     [ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o                         [ 69%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o                     [ 70%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaAstroBWTRunner.cpp.o               [ 70%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaKawPowRunner.cpp.o                 [ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o                                    [ 71%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o                                       [ 72%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o                                        [ 73%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o                         [ 74%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o                                                 [ 75%] Building CXX object CMakeFiles/xmrig.dir/src/hw/api/HwApi.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o                                [ 76%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_unix.cpp.o                              [ 77%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o                      [ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o                                       [ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o                                         [ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o                                       [ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o                        [ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o                         [ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o                      [ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o                            [ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o                   [ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o                         [ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o                                          [ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o                                      [ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o                              [ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o                                     [ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_a64_static.S.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_a64.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 94%] Building C object CMakeFiles/xmrig.dir/src/crypto/astrobwt/salsa20_ref/salsa20.c.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPCache.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPHash.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o                            [100%] Linking CXX executable xmrig
/data/data/com.termux/files/usr/bin/ld: /system/lib64/liblog.so: unknown type [0x13] section `.relr.dyn'
/data/data/com.termux/files/usr/bin/ld: skipping incompatible /system/lib64/liblog.so when searching for -llog
/data/data/com.termux/files/usr/bin/ld: /system/lib64/liblog.so: unknown type [0x13] section `.relr.dyn'
/data/data/com.termux/files/usr/bin/ld: skipping incompatible /system/lib64/liblog.so when searching for -llog
/data/data/com.termux/files/usr/bin/ld: cannot find -llog
/data/data/com.termux/files/usr/bin/ld: /system/lib64/liblog.so: unknown type [0x13] section `.relr.dyn'        /data/data/com.termux/files/usr/bin/ld: skipping incompatible /system/lib64/liblog.so when searching for -llog
/data/data/com.termux/files/usr/bin/ld: /system/lib64/liblog.so: unknown type [0x13] section `.relr.dyn'
/data/data/com.termux/files/usr/bin/ld: skipping incompatible /system/lib64/liblog.so when searching for -llog
clang-12: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3590: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

**Additional context**
Add any other context about the problem here.


# Discussion History
## peme14k | 2021-06-10T09:25:05+00:00
CC

## Spudz76 | 2021-06-10T16:31:04+00:00
Bug in `ld` you have to either use `lld` to match Clang, or use gcc which doesn't generate the `.relr.dyn` sections that bintools doesn't know about.

Add to cmake command `-DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=lld`

## calvintam236 | 2021-06-10T21:14:21+00:00
> Bug in `ld` you have to either use `lld` to match Clang, or use gcc which doesn't generate the `.relr.dyn` sections that bintools doesn't know about.
> 
> Add to cmake command `-DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=lld`

With some trial and errors, the working cmake line: `cmake .. -DWITH_HWLOC=OFF -DCMAKE_CXX_FLAGS="-fuse-ld=lld"`. Using `-DCMAKE_EXE_LINKER_FLAGS` will throw error when you run `cmake`.

@xmrig I believe this flag `-fuse-ld=lld` should be added to `CMakeLists.txt`.

## Spudz76 | 2021-06-11T14:26:16+00:00
It only affects clang on ChomeOS/Android and there is a bintools patch thing just have to catch up.

For instance Clang works fine, with regular `ld`, on x86_64

## ghost | 2021-06-11T19:14:36+00:00
Try update to latest termux v113
https://f-droid.org/repo/com.termux_113.apk


then install xmrig with this single line command

```
pkg update -y && pkg upgrade -y && pkg install -y wget nano git cmake clang libuv automake libtool autoconf && git clone https://github.com/xmrig/xmrig.git && mkdir xmrig/build && cd xmrig/build && cmake .. -DWITH_HWLOC=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_SSE4_1=OFF -DCMAKE_BUILD_TYPE=Release -Wno-dev && make -j$(nproc) && mv xmrig-notls xmrig && cp ../src/config.json config.json && ./xmrig
```
hope this will help out ....


## Pemekk | 2021-06-13T13:37:55+00:00
#2434

ในวันที่ พฤ. 10 มิ.ย. 2021 16:25 น. peme14k ***@***.***>
เขียนว่า:

> CC
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2434#issuecomment-858463571>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AUEA5UKJFLQ25ISRNA3VWGLTSCAIHANCNFSM46N2N4ZA>
> .
>


# Action History
- Created by: calvintam236 | 2021-06-10T09:20:58+00:00
