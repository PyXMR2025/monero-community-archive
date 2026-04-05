---
title: 'collect2: error: ld returned 1 exit status'
source_url: https://github.com/xmrig/xmrig/issues/1284
author: minzak
assignees: []
labels:
- bug
created_at: '2019-11-14T00:59:13+00:00'
updated_at: '2019-11-23T11:20:45+00:00'
type: issue
status: closed
closed_at: '2019-11-23T11:20:45+00:00'
---

# Original Description
I'm use Debian 10 and xmrig v5 with config:
```
cmake -DWITH_HWLOC=ON -DWITH_LIBCPUID=ON -DWITH_HTTP=ON -DWITH_TLS=ON -DWITH_ASM=ON -DWITH_OPENCL=ON -DWITH_CUDA=ON \
-DWITH_EMBEDDED_CONFIG=OFF \
-DWITH_CN_LITE=OFF \
-DWITH_CN_HEAVY=OFF \
-DWITH_CN_PICO=OFF \
-DWITH_CN_GPU=ON \
-DWITH_RANDOMX=OFF \
-DWITH_ARGON2=OFF \
..
make -j4
```
And i got this full log:

```
me@e7470 /usr/src/xmrig (master) $ ./build.sh
-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
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
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.1d")  
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/xmrig/build
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target xmrig
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 25%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_gpu_generator.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn00RyoKernel.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1RyoKernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2RyoKernel.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRyoRunner.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 86%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Coin.cpp.o
/usr/src/xmrig/src/crypto/common/Algorithm.cpp: In member function ‘size_t xmrig::Algorithm::l3() const’:
/usr/src/xmrig/src/crypto/common/Algorithm.cpp:160:22: warning: unused variable ‘oneMiB’ [-Wunused-variable]
     constexpr size_t oneMiB = 0x100000;
                      ^~~~~~
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/keccak.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o: in function `xmrig::CudaRxRunner::set(xmrig::Job const&, unsigned char*)':
CudaRxRunner.cpp:(.text+0xe6): undefined reference to `xmrig::Rx::dataset(xmrig::Job const&, unsigned int)'
/usr/bin/ld: CudaRxRunner.cpp:(.text+0xfc): undefined reference to `xmrig::RxDataset::size(bool) const'
/usr/bin/ld: CudaRxRunner.cpp:(.text+0x107): undefined reference to `xmrig::RxDataset::raw() const'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2114: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:110: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

me@e7470 /usr/src/xmrig (master) $ 
```
If build option was: `-DWITH_OPENCL=OFF -DWITH_CUDA=OFF`
All works (but one warning still present)

# Discussion History
## xmrig | 2019-11-14T08:13:36+00:00
Fixed in dev branch, error has happened with `-DWITH_RANDOMX=OFF -DWITH_CUDA=ON`.
Thank you.

# Action History
- Created by: minzak | 2019-11-14T00:59:13+00:00
- Closed at: 2019-11-23T11:20:45+00:00
