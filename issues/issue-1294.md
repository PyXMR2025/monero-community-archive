---
title: Who can guide the detailed static compilation steps
source_url: https://github.com/xmrig/xmrig/issues/1294
author: axsoftshi
assignees: []
labels: []
created_at: '2019-11-16T19:57:52+00:00'
updated_at: '2019-11-16T20:09:46+00:00'
type: issue
status: closed
closed_at: '2019-11-16T20:09:46+00:00'
---

# Original Description
localhost:~# cd xmrig/
localhost:~/xmrig# rm -rf build/
localhost:~/xmrig# mkdir build
localhost:~/xmrig# cd build/
localhost:~/xmrig/build# cmake .. -DWITH_EMBEDDED_CONFIG=ON -DWITH_HTTP=OFF -DWITH_TLS
=OFF -DUV_INCLUDE_DIR=/root/libuv-1.33.1/include -DBUILD_STATIC=ON -DUV_LIBRARY=/root/
libuv-1.33.1/build/libuv_a.a
-- The C compiler identification is GNU 9.2.0
-- The CXX compiler identification is GNU 9.2.0
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
-- Found HWLOC: /usr/lib/libhwloc.so  
-- Found UV: /root/libuv-1.33.1/build/libuv_a.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
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
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
localhost:~/xmrig/build# make
Scanning dependencies of target xmrig-asm
[  0%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  1%] Linking C static library libxmrig-asm.a
[  1%] Built target xmrig-asm
Scanning dependencies of target argon2-avx512f
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  2%] Linking C static library libargon2-avx512f.a
[  2%] Built target argon2-avx512f
Scanning dependencies of target argon2-avx2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  3%] Linking C static library libargon2-avx2.a
[  3%] Built target argon2-avx2
Scanning dependencies of target argon2-ssse3
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  4%] Linking C static library libargon2-ssse3.a
[  4%] Built target argon2-ssse3
Scanning dependencies of target argon2-sse2
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  5%] Linking C static library libargon2-sse2.a
[  5%] Built target argon2-sse2
Scanning dependencies of target argon2-xop
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  7%] Linking C static library libargon2-xop.a
[  7%] Built target argon2-xop
Scanning dependencies of target argon2
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[ 10%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[ 10%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
[ 11%] Linking C static library libargon2.a
[ 11%] Built target argon2
Scanning dependencies of target xmrig-notls
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Signals.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Buffer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclBackend.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclCache.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclConfig.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclThread.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclThreads.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclWorker.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_cn_gpu_generator.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn00RyoKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn1RyoKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn2RyoKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRyoRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaBackend.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaConfig.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaThread.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaThreads.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaWorker.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/NetworkState.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 73%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o
[ 73%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o
[ 74%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o
[ 74%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Algorithm.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Coin.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/keccak.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o
[ 81%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_core.c.o
[ 82%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_ref.c.o
[ 82%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 83%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o
[ 85%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/Rx.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxAlgo.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxCache.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxDataset.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxQueue.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxVm.cpp.o
[ 94%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig_hwloc.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxNUMAStorage.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/argon2/Impl.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Assembly.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig-notls
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: cannot find -lhwloc
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:2568: xmrig-notls] Error 1
make[1]: *** [CMakeFiles/Makefile2:116: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Discussion History
## axsoftshi | 2019-11-16T19:58:32+00:00
alpine linux

## axsoftshi | 2019-11-16T20:00:18+00:00
If you add - dwith ﹣ hwloc = off compilation, it will succeed, but - dwith ﹣ embedded ﹣ config = on will not take effect

## xmrig | 2019-11-16T20:02:22+00:00
Try build own libhwloc https://github.com/xmrig/xmrig/issues/1099#issuecomment-518089405
Thank you.

## axsoftshi | 2019-11-16T20:09:41+00:00
Thank you. xmrig 


# Action History
- Created by: axsoftshi | 2019-11-16T19:57:52+00:00
- Closed at: 2019-11-16T20:09:46+00:00
