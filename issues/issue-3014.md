---
title: Issue of Advanced Build at RHEL 7
source_url: https://github.com/xmrig/xmrig/issues/3014
author: kingtonchan
assignees: []
labels: []
created_at: '2022-04-08T17:52:56+00:00'
updated_at: '2025-06-28T10:41:01+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:41:01+00:00'
---

# Original Description
I followed the procedure of "Advanced Build" (CentOS7) to build XMRig at RHEL 7, but got the following error message. Could you please advise how I can fix it.

make[1]: Leaving directory `/root/xmrig/scripts/build/openssl-1.1.1m'
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 4.8.5
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc - works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ - works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /root/xmrig/scripts/deps/lib/libhwloc.a
-- Found UV: /root/xmrig/scripts/deps/lib/libuv.a
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
-- Performing Test FEATURE_avx512f_FLAG - Failed
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Found OpenSSL: /root/xmrig/scripts/deps/lib/libcrypto.a (found version "1.1.1m")
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
Scanning dependencies of target argon2-ssse3
Scanning dependencies of target argon2-xop
Scanning dependencies of target argon2-avx2
Scanning dependencies of target argon2-sse2
Scanning dependencies of target xmrig-asm
Scanning dependencies of target argon2-avx512f
Scanning dependencies of target ghostrider
Scanning dependencies of target ethash
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  2%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  2%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o
[  6%] Linking C static library libxmrig-asm.a
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o
[  7%] Linking C static library libargon2-avx512f.a
[  7%] Built target xmrig-asm
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o
[  8%] Built target argon2-avx512f
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o
[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o
[  9%] Linking C static library libethash.a
[  9%] Built target ethash
[ 10%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o
[ 11%] Linking C static library libargon2-xop.a
[ 11%] Linking C static library libargon2-ssse3.a
[ 11%] Linking C static library libargon2-sse2.a
[ 11%] Built target argon2-xop
[ 11%] Linking C static library libargon2-avx2.a
[ 11%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o
[ 11%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o
[ 11%] Built target argon2-ssse3
[ 12%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o
[ 12%] Built target argon2-sse2
[ 12%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o
[ 12%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
[ 12%] Built target argon2-avx2
Scanning dependencies of target argon2
[ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[ 13%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[ 13%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[ 13%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 14%] Linking C static library libargon2.a
[ 14%] Built target argon2
[ 15%] Linking CXX static library libghostrider.a
[ 15%] Built target ghostrider
Scanning dependencies of target xmrig
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Chrono.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 31%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 32%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 35%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[ 35%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[ 36%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
/root/xmrig/src/base/net/stratum/DaemonClient.cpp: In member function ‘bool xmrig::DaemonClient::WSSWrite(const char*, size_t)’:
/root/xmrig/src/base/net/stratum/DaemonClient.cpp:1115:29: warning: value computed is not used [-Wunused-value]
     BIO_reset(m_wss.m_write);
                             ^
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
At global scope:
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FilterKernel.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_astrobwt_generator.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_FindSharesKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_MainKernel.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_PrepareBatch2Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_Salsa20Kernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3InitialKernel.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt/AstroBWT_SHA3Kernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_BWT_FixOrderKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_BWT_PreprocessKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_FindSharesKernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_Salsa20Kernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_SHA3InitialKernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/astrobwt_v2/AstroBWT_v2_SHA3Kernel.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWTRunner.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclAstroBWT_v2_Runner.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_kawpow_generator.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/kawpow/KawPow_CalculateDAGKernel.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclKawPowRunner.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclKawPow.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaAstroBWTRunner.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaKawPowRunner.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/core/Taskbar.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/hw/api/HwApi.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiBoard.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiMemory.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiTools.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 80%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b_sse41.c.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxFix_linux.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr_linux.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxMsr.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/MsrItem.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sort_indices2.cpp.o
/root/xmrig/src/crypto/astrobwt/sort_indices2.cpp:40:24: error: missing binary operator before token "("
 #if __has_cpp_attribute(unlikely)
                        ^
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/astrobwt/sort_indices2.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

# Discussion History
## SChernykh | 2022-04-08T19:40:34+00:00
Update GCC to newer version.

## Spudz76 | 2022-04-09T00:23:40+00:00
[Here is the info on adding GCC 7.3.1 to old RHEL](https://access.redhat.com/documentation/en-us/red_hat_developer_toolset/7/html/user_guide/chap-red_hat_developer_toolset)

You will have to specify CC and CXX environment vars before executing anything else including the build_deps as the antique gcc-4 will remain the default compiler.

Or, upgrade to RHEL 8 since it has at least gcc-8 by default.

## AcharyaOne | 2022-04-17T03:01:10+00:00
I'm able to compile but I get that same error: 

`/xmrig/scripts/deps/include/openssl/bio.h:480:34: warning: value computed is not used [-Wunused-value]
  480 | # define BIO_reset(b)            (int)BIO_ctrl(b,BIO_CTRL_RESET,0,NULL)
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
xmrig/src/base/net/stratum/DaemonClient.cpp:1115:5: note: in expansion of macro ‘BIO_reset’
 1115 |     BIO_reset(m_wss.m_write);`

safe to ignore?

## Spudz76 | 2022-04-17T06:31:05+00:00
Yes.

# Action History
- Created by: kingtonchan | 2022-04-08T17:52:56+00:00
- Closed at: 2025-06-28T10:41:01+00:00
