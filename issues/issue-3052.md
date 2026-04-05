---
title: Warnings thrown when compiling with LLVM 15
source_url: https://github.com/xmrig/xmrig/issues/3052
author: iamhumanipromise
assignees: []
labels: []
created_at: '2022-05-20T04:06:46+00:00'
updated_at: '2025-06-28T10:36:18+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:36:18+00:00'
---

# Original Description
LLVM 14 is released; which means of course I'm playing around to see what I can break with the next version!!!!!

Xmrig compiles successfully using make flags _-DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++_
Even works with the Intel NEO/LevelZero OpenCL 3.0 drivers on a Comet Lake i3-10100U laptop! (32GB of shared system/GPU RAM = kawpow mines with all 23 EUs successfully) 

(compile time warnings do not occur with GNU C/C++ 12.1.0 compiler, but opencl throws invalid pointer error). Here are the warnings for the devs to have for their records: 

`[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  4%] Linking C static library libargon2-xop.a
[  4%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  4%] Built target argon2-xop
[  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  5%] Linking C static library libxmrig-asm.a
[  5%] Built target xmrig-asm
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
[  6%] Linking C static library libargon2-avx512f.a
[  6%] Linking C static library libargon2-sse2.a
[  6%] Linking C static library libargon2-ssse3.a
[  6%] Built target argon2-avx512f
[  6%] Linking C static library libargon2-avx2.a
[  7%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  7%] Built target argon2-sse2
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
[  8%] Built target argon2-ssse3
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o
[  8%] Built target argon2-avx2
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o
[ 10%] Linking C static library libethash.a
[ 10%] Built target ethash
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o
[ 10%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[ 10%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 11%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o
[ 12%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o
clang-15: warning: optimization flag '-fno-tree-vrp' is not supported [-Wignored-optimization-argument]
[ 12%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o
[ 12%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o
[ 13%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o
[ 13%] Linking C static library libargon2.a
[ 13%] Built target argon2
[ 13%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o
[ 13%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o
[ 14%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o
[ 14%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o
[ 14%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o
[ 15%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
/home/eric/Playground/xmrig-CL3.0CLANG/src/crypto/ghostrider/ghostrider.cpp:577:30: warning: lambda capture 'n' is not required to be captured for this use [-Wunused-lambda-capture]
        helper->launch_task([n, av, data, size, &ctx_memory, ctx, &cn_indices, &core_indices, &tmp, output, tune]() {
                             ^~
1 warning generated.
[ 15%] Linking CXX static library libghostrider.a
[ 15%] Built target ghostrider
Scanning dependencies of target xmrig
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
/home/eric/Playground/xmrig-CL3.0CLANG/src/base/kernel/config/BaseConfig.cpp:152:73: warning: adding 'int' to a string does not append to the string [-Wstring-plus-int]
        snprintf(buf, sizeof buf, "LibreSSL/%s ", LIBRESSL_VERSION_TEXT + 9);
                                                  ~~~~~~~~~~~~~~~~~~~~~~^~~
/home/eric/Playground/xmrig-CL3.0CLANG/src/base/kernel/config/BaseConfig.cpp:152:73: note: use array indexing to silence this warning
        snprintf(buf, sizeof buf, "LibreSSL/%s ", LIBRESSL_VERSION_TEXT + 9);
                                                                        ^
                                                  &                     [  ]
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
1 warning generated.
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
/home/eric/Playground/xmrig-CL3.0CLANG/src/base/kernel/Entry.cpp:85:55: warning: adding 'int' to a string does not append to the string [-Wstring-plus-int]
        printf("LibreSSL/%s\n", LIBRESSL_VERSION_TEXT + 9);
                                ~~~~~~~~~~~~~~~~~~~~~~^~~
/home/eric/Playground/xmrig-CL3.0CLANG/src/base/kernel/Entry.cpp:85:55: note: use array indexing to silence this warning
        printf("LibreSSL/%s\n", LIBRESSL_VERSION_TEXT + 9);
                                                      ^
                                &                     [  ]
1 warning generated.
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Chrono.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 33%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 33%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 37%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 37%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[ 37%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_BWT_FixOrderKernel.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_BWT_PreprocessKernel.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_FindSharesKernel.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_Salsa20Kernel.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_SHA3InitialKernel.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_SHA3Kernel.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWT_v2_Runner.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/core/Taskbar.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/hw/api/HwApi.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiBoard.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiMemory.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiTools.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader_unix.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
/home/eric/Playground/xmrig-CL3.0CLANG/src/hw/dmi/DmiReader.cpp:91:9: warning: variable 'i' set but not used [-Wunused-but-set-variable]
    int i         = 0;
        ^
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
1 warning generated.
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
/home/eric/Playground/xmrig-CL3.0CLANG/src/crypto/common/LinuxMemory.cpp:34:18: warning: unused variable 'twoMiB' [-Wunused-const-variable]
constexpr size_t twoMiB = 2U * 1024U * 1024U;
                 ^
/home/eric/Playground/xmrig-CL3.0CLANG/src/crypto/common/LinuxMemory.cpp:35:18: warning: unused variable 'oneGiB' [-Wunused-const-variable]
constexpr size_t oneGiB = 1024U * 1024U * 1024U;
                 ^
2 warnings generated.
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CryptoNight_x86_vaes.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b_sse41.c.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxFix_linux.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr_linux.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxMsr.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/MsrItem.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Profiler.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sort_indices2.cpp.o
[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/astrobwt/xmm6int/salsa20_xmm6int-avx2.c.o
[ 95%] Building ASM object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3_256_avx2.S.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPCache.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPHash.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig
`

# Discussion History
# Action History
- Created by: iamhumanipromise | 2022-05-20T04:06:46+00:00
- Closed at: 2025-06-28T10:36:18+00:00
