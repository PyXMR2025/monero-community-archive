---
title: 'Env.cpp:(.text+0x16e): undefined reference to `uv_os_gethostname'''
source_url: https://github.com/xmrig/xmrig/issues/1576
author: minzak
assignees: []
labels:
- libuv
created_at: '2020-03-03T17:20:54+00:00'
updated_at: '2020-03-03T17:56:05+00:00'
type: issue
status: closed
closed_at: '2020-03-03T17:56:05+00:00'
---

# Original Description
```
cmake .. && make -j3
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
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
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/x86_64-linux-gnu/libhwloc.so  
-- Found UV: /usr/local/lib/libuv.a  
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
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.0l") 
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/xmrig/build
Scanning dependencies of target xmrig-asm
Scanning dependencies of target argon2-xop
Scanning dependencies of target argon2-avx512f
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target argon2-sse2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  3%] Linking C static library libargon2-xop.a
[  3%] Built target argon2-xop
Scanning dependencies of target argon2-ssse3
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  5%] Linking C static library libargon2-avx512f.a
[  5%] Linking C static library libargon2-sse2.a
[  5%] Built target argon2-avx512f
Scanning dependencies of target argon2-avx2
[  5%] Built target argon2-sse2
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  5%] Linking C static library libargon2-ssse3.a
[  6%] Linking C static library libargon2-avx2.a
[  6%] Built target argon2-ssse3
[  6%] Built target argon2-avx2
Scanning dependencies of target argon2
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 28%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_gpu_generator.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn00RyoKernel.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1RyoKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2RyoKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRyoRunner.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 73%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 74%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 74%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 75%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Coin.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/keccak.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 81%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_core.c.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_ref.c.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx_linux.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/msr/MsrItem.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o: In function `xmrig::Env::hostname()':
Env.cpp:(.text+0x16e): undefined reference to `uv_os_gethostname'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:5071: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:73: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```


# Discussion History
## xmrig | 2020-03-03T17:28:41+00:00
https://github.com/xmrig/xmrig/issues/1530#issuecomment-581163070

`-- Found UV: /usr/local/lib/libuv.a ` this is some custom old libuv version.
Thank you.

## minzak | 2020-03-03T17:43:20+00:00
Hmm, yes, I remover it old one, but not helps.
```
cmake ..
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
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
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/x86_64-linux-gnu/libhwloc.so  
-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.a  
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
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.0l") 
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/xmrig/build
root@node:/usr/src/xmrig/build# make -j3
Scanning dependencies of target argon2-avx512f
Scanning dependencies of target argon2-xop
Scanning dependencies of target xmrig-asm
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target argon2-sse2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  3%] Linking C static library libargon2-xop.a
[  3%] Linking C static library libargon2-sse2.a
[  3%] Built target argon2-xop
Scanning dependencies of target argon2-ssse3
[  3%] Built target argon2-sse2
Scanning dependencies of target argon2-avx2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  5%] Linking C static library libargon2-avx512f.a
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  5%] Built target argon2-avx512f
[  5%] Linking C static library libargon2-ssse3.a
[  5%] Built target argon2-ssse3
[  6%] Linking C static library libargon2-avx2.a
[  6%] Built target argon2-avx2
Scanning dependencies of target argon2
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 28%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_gpu_generator.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn00RyoKernel.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1RyoKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2RyoKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRyoRunner.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 73%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 74%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 74%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 75%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Coin.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/keccak.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 81%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_core.c.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_ref.c.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx_linux.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/msr/MsrItem.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o: In function `xmrig::Env::hostname()':
Env.cpp:(.text+0x16e): undefined reference to `uv_os_gethostname'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:5071: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:73: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

## minzak | 2020-03-03T17:46:25+00:00
rebuild with `do-make.sh`
`cmake -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a .. && make -j3`

got `collect2: error: ld returned 1 exit status`

```
root@node:/usr/src/xmrig/build# ./do-make.sh
-- WITH_MSR=ON
-- argon2: detecting feature 'sse2'...
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- argon2: feature 'avx512f' detected!
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/xmrig/build
[  1%] Built target argon2-xop
[  1%] Built target argon2-sse2
[  2%] Built target argon2-avx512f
[  4%] Built target xmrig-asm
[  6%] Built target argon2-ssse3
[  6%] Built target argon2-avx2
[ 10%] Built target argon2
[ 10%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o: In function `xmrig::Env::hostname()':
Env.cpp:(.text+0x16e): undefined reference to `uv_os_gethostname'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:5071: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:73: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

## minzak | 2020-03-03T17:56:05+00:00
At last.
Apt purge, find and remove all libuv*, apt reinstall - helps!

# Action History
- Created by: minzak | 2020-03-03T17:20:54+00:00
- Closed at: 2020-03-03T17:56:05+00:00
