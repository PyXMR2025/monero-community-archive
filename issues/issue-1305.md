---
title: 'With the 5.0 installation: c++: fatal error: Killed signal terminated program
  cc1plus'
source_url: https://github.com/xmrig/xmrig/issues/1305
author: djiesr
assignees: []
labels:
- arm
created_at: '2019-11-20T02:04:44+00:00'
updated_at: '2021-04-12T15:28:50+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:28:50+00:00'
---

# Original Description
Ubuntu server 19.10 on Raspberry PI 4

Scanning dependencies of target argon2
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  4%] Linking C static library libargon2.a
[  4%] Built target argon2
Scanning dependencies of target xmrig
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 21%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn0Kernel.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1Kernel.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2Kernel.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/CnBranchKernel.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclBackend.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclConfig.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclLaunchData.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThread.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclThreads.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclBaseRunner.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclCnRunner.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclCnR.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedData.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/tools/OclSharedState.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclContext.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclDevice.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclError.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclKernel.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclLib.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/OclPlatform.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/OclCache_unix.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_rx_generator.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bHashRegistersKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/Blake2bInitialHashKernel.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/ExecuteVmKernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FillAesKernel.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/FindSharesKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/InitVmKernel.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxJitKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/RxRunKernel.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxBaseRunner.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxJitRunner.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRxVmRunner.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_gpu_generator.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn00RyoKernel.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn1RyoKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/Cn2RyoKernel.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/runners/OclRyoRunner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaBackend.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaConfig.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaLaunchData.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThread.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaThreads.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/CudaWorker.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaBaseRunner.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaCnRunner.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaDevice.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/CudaLib.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/wrappers/NvmlLib.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cuda/runners/CudaRxRunner.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 73%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 73%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 74%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 74%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Coin.cpp.o
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
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
In file included from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/crypto/randomx/common.hpp:36,
                 from /home/ubuntu/xmrig/src/crypto/randomx/bytecode_machine.hpp:31,
                 from /home/ubuntu/xmrig/src/crypto/randomx/bytecode_machine.cpp:29:
/home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_swap_vec_f128(rx_vec_f128)’:
/home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:412:25: warning: ‘temp’ is used uninitialized in this function [-Wuninitialized]
  412 |  temp = vcopyq_laneq_f64(temp, 1, a, 1);
      |         ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
/home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_cvt_packed_int_vec_f128(const void*)’:
/home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:503:20: warning: ‘x’ is used uninitialized in this function [-Wuninitialized]
  503 |  x = vsetq_lane_f64(lo, x, 0);
      |      ~~~~~~~~~~~~~~^~~~~~~~~~
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 86%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
In file included from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/crypto/randomx/common.hpp:36,
                 from /home/ubuntu/xmrig/src/crypto/randomx/vm_interpreted.hpp:33,
                 from /home/ubuntu/xmrig/src/crypto/randomx/vm_interpreted.cpp:29:
/home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_cvt_packed_int_vec_f128(const void*)’:
/home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:503:20: warning: ‘x’ is used uninitialized in this function [-Wuninitialized]
  503 |  x = vsetq_lane_f64(lo, x, 0);
      |      ~~~~~~~~~~~~~~^~~~~~~~~~
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
c++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2221: CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
ubuntu@ubuntu:~/xmrig/build$ cmake ..make[2]: *** [CMakeFiles/xmrig.dir/build.make:2221: CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o] Error 1
CMake Error: The source directory "/home/ubuntu/xmrig/build/1" does not exist.
Specify --help for usage, or press the help button on the CMake GUI.
ubuntu@ubuntu:~/xmrig/build$ ^C
ubuntu@ubuntu:~/xmrig/build$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 19.10
Release:        19.10
Codename:       eoan


# Discussion History
## xmrig | 2019-11-21T08:23:16+00:00
Try create swap file.
Thank you.

## djiesr | 2019-11-29T03:44:35+00:00
I create a swap file of 4G.
Exchange de SD card for a U3
I got the same fatal error.
Another solution?

## bormoley1983 | 2019-11-29T22:40:09+00:00
Same problem, building stuck on aarch64 with 
-DWITH_RANDOMX=ON 
if I do 
-DWITH_RANDOMX=OFF
building completes

## xwry | 2020-01-20T21:33:25+00:00
Same here on armv8 Ubuntu 18 server and xfce
On gcc-9 It compiles only with cmake ..  -DCMAKE_BUILD_TYPE=Debug, otherwise fatal error.
On gcc-8 there is no such problem, everything works.

## tenaciousRas | 2020-04-08T02:24:14+00:00
+1 using master branch - had to downgrade docker container OS for gcc-8

## xmrig | 2020-11-02T13:02:58+00:00
This issue should be fixed in dev branch https://github.com/xmrig/xmrig/pull/1926
Thank you.

# Action History
- Created by: djiesr | 2019-11-20T02:04:44+00:00
- Closed at: 2021-04-12T15:28:50+00:00
