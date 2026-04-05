---
title: file not found after compiled
source_url: https://github.com/xmrig/xmrig/issues/1373
author: jasonwee
assignees: []
labels: []
created_at: '2019-12-03T14:39:01+00:00'
updated_at: '2021-08-04T00:15:18+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:42:37+00:00'
---

# Original Description
very puzzled, not sure what is happening, even after compile at 100%, the end binary file is not found??!!

```
[100%] Linking CXX executable xmrig-notls
/usr/bin/cmake -E cmake_link_script CMakeFiles/xmrig-notls.dir/link.txt --verbose=1
/usr/bin/g++-6   -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -mfpu=neon -flax-vector-conversions -O3 -DNDEBUG -Ofast -s   -static -rdynamic CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/Signals.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o CMakeFiles/xmrig-notls.dir/src/base/tools/Buffer.cpp.o CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/cl/OclSource.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclBackend.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclCache.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclConfig.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclLaunchData.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclThread.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclThreads.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclWorker.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclCnRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclContext.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclDevice.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclError.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclLib.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclCache_unix.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaBackend.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaConfig.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaLaunchData.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaThread.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaThreads.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaWorker.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/CudaLib.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o CMakeFiles/xmrig-notls.dir/src/App.cpp.o CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o CMakeFiles/xmrig-notls.dir/src/net/NetworkState.cpp.o CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/Algorithm.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/Coin.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/keccak.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_core.c.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_ref.c.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted_light.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/Rx.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxAlgo.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxBasicStorage.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxCache.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxDataset.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxQueue.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxVm.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig_basic.cpp.o CMakeFiles/xmrig-notls.dir/src/crypto/argon2/Impl.cpp.o CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/SysLog.cpp.o  -o xmrig-notls -Wl,-Bstatic -luv -Wl,-Bdynamic -lpthread -lrt -ldl src/3rdparty/argon2/libargon2.a 
make[2]: Leaving directory '/home/pi/xmrig/xmrig/build'
[100%] Built target xmrig-notls
make[1]: Leaving directory '/home/pi/xmrig/xmrig/build'
/usr/bin/cmake -E cmake_progress_start /home/pi/xmrig/xmrig/build/CMakeFiles 0
pi@m00:~/xmrig/xmrig/build $ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile  src  xmrig-notls
pi@m00:~/xmrig/xmrig/build $ ./xmrig-notls 
-bash: ./xmrig-notls: No such file or directory
pi@m00:~/xmrig/xmrig/build $ file xmrig-notls 
xmrig-notls: ELF 32-bit LSB executable, ARM, EABI5 version 1 (GNU/Linux), dynamically linked, interpreter /usr/lib/ld.so.1, for GNU/Linux 3.2.0, BuildID[sha1]=7166bf9609ea393cf79896bd6a421d1811d244d5, stripped
pi@m00:~/xmrig/xmrig/build $ ls -lh xmrig-notls 
-rwxr-xr-x 1 pi pi 1.4M Dec  3 22:12 xmrig-notls
pi@m00:~/xmrig/xmrig/build $ 
```

any idea why?

# Discussion History
## jasonwee | 2019-12-04T13:16:14+00:00
```
$ make -j1
Scanning dependencies of target argon2
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  5%] Linking C static library libargon2.a
[  5%] Built target argon2
Scanning dependencies of target xmrig-notls
[  5%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Signals.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Buffer.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclBackend.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclCache.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclConfig.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclThread.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclThreads.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclWorker.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaBackend.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaConfig.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaThread.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaThreads.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/CudaWorker.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/NetworkState.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 73%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o
[ 74%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o
[ 74%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o
[ 75%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Algorithm.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Coin.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/keccak.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o
[ 82%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_core.c.o
[ 83%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_ref.c.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 84%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o
[ 87%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/Rx.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxAlgo.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxCache.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxDataset.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxQueue.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxVm.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig_basic.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/argon2/Impl.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/SysLog.cpp.o
[100%] Linking CXX executable xmrig-notls
[100%] Built target xmrig-notls
$ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile  src  xmrig-notls
$ ./xmrig-notls 
-bash: ./xmrig-notls: No such file or directory
$ file xmrig-notls 
xmrig-notls: ELF 32-bit LSB executable, ARM, EABI5 version 1 (GNU/Linux), dynamically linked, interpreter /usr/lib/ld.so.1, for GNU/Linux 3.2.0, BuildID[sha1]=826105e5b5e0a5cc3f2c0146eb6fadfdb6dfc51b, stripped
$ ls -lh xmrig-notls 
-rwxr-xr-x 1 pi pi 1.5M Dec  4 20:56 xmrig-notls
```

## niraj-vachhani | 2021-08-04T00:15:18+00:00
I have the same issue:
./xmrig -o xmr-asia1.nanopool.org:14433 -u  41sdQi4TRSS28ZuwqWcaXDguEBjpuE6VNieXy5QgeBeRfUbKb3NpnWDZbg7CAVD7t7A4yQjwYVJUC56MVs8XxoPpThtdrut --tls --coin monero
bash: ./xmrig: No such file or directory

Pl help reg. solution.

# Action History
- Created by: jasonwee | 2019-12-03T14:39:01+00:00
- Closed at: 2020-02-09T10:42:37+00:00
