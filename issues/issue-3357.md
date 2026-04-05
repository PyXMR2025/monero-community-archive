---
title: bulid error
source_url: https://github.com/xmrig/xmrig/issues/3357
author: calojohn806
assignees: []
labels: []
created_at: '2023-11-15T13:26:22+00:00'
updated_at: '2025-06-18T22:18:30+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:18:30+00:00'
---

# Original Description
root@vuln-VirtualBox:/home/vuln/Desktop/test# git clone https://github.com/xmrig/xmrig.git

Cloning into 'xmrig'...

remote: Enumerating objects: 27957, done.

remote: Counting objects: 100% (291/291), done.

remote: Compressing objects: 100% (158/158), done.

remote: Total 27957 (delta 159), reused 218 (delta 132), pack-reused 27666

Receiving objects: 100% (27957/27957), 13.30 MiB | 1.95 MiB/s, done.

Resolving deltas: 100% (20460/20460), done.

root@vuln-VirtualBox:/home/vuln/Desktop/test# cmake -DBUILD_STATIC=ON -DWITH_EMBEDDED_CONFIG=ON .

CMake Error: The source directory "/home/vuln/Desktop/test" does not appear to contain CMakeLists.txt.

Specify --help for usage, or press the help button on the CMake GUI.

root@vuln-VirtualBox:/home/vuln/Desktop/test# cd xmrig/

root@vuln-VirtualBox:/home/vuln/Desktop/test/xmrig# cmake -DBUILD_STATIC=ON -DWITH_EMBEDDED_CONFIG=ON .

-- The C compiler identification is GNU 11.4.0

-- The CXX compiler identification is GNU 11.4.0

-- Detecting C compiler ABI info

-- Detecting C compiler ABI info - done

-- Check for working C compiler: /usr/bin/cc - skipped

-- Detecting C compile features

-- Detecting C compile features - done

-- Detecting CXX compiler ABI info

-- Detecting CXX compiler ABI info - done

-- Check for working CXX compiler: /usr/bin/c++ - skipped

-- Detecting CXX compile features

-- Detecting CXX compile features - done

-- Performing Test VAES_SUPPORTED

-- Performing Test VAES_SUPPORTED - Success

-- Looking for syslog.h

-- Looking for syslog.h - found

-- Found HWLOC: /usr/lib/x86_64-linux-gnu/libhwloc.so  

CMake Warning at src/backend/opencl/opencl.cmake:2 (message):

  OpenCL backend is not compatible with static build, use -DWITH_OPENCL=OFF

  to suppress this warning

Call Stack (most recent call first):

  src/backend/backend.cmake:2 (include)

  CMakeLists.txt:49 (include)





CMake Warning at src/backend/cuda/cuda.cmake:2 (message):

  CUDA backend is not compatible with static build, use -DWITH_CUDA=OFF to

  suppress this warning

Call Stack (most recent call first):

  src/backend/backend.cmake:3 (include)

  CMakeLists.txt:49 (include)





-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.so  

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

-- Looking for pthread.h

-- Looking for pthread.h - found

-- Performing Test CMAKE_HAVE_LIBC_PTHREAD

-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success

-- Found Threads: TRUE  

-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.a (found version "3.0.2")  

-- The ASM compiler identification is GNU

-- Found assembler: /usr/bin/cc

-- Configuring done

-- Generating done

-- Build files have been written to: /home/vuln/Desktop/test/xmrig

root@vuln-VirtualBox:/home/vuln/Desktop/test/xmrig# make 

Scanning dependencies of target xmrig-asm

[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o

[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o

[  2%] Linking C static library libxmrig-asm.a

[  2%] Built target xmrig-asm

[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o

[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o

[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o

[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o

[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fugue.c.o

[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_groestl.c.o

[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_hamsi.c.o

[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.c.o

[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_keccak.c.o

[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luffa.c.o

[  7%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shabal.c.o

[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_shavite.c.o

[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_simd.c.o

[  8%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha2.c.o

[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_skein.c.o

[  9%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whirlpool.c.o

[ 10%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o

[ 10%] Linking CXX static library libghostrider.a

[ 10%] Built target ghostrider

[ 10%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o

[ 11%] Linking C static library libargon2-sse2.a

[ 11%] Built target argon2-sse2

[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o

[ 12%] Linking C static library libargon2-ssse3.a

[ 12%] Built target argon2-ssse3

[ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o

[ 13%] Linking C static library libargon2-xop.a

[ 13%] Built target argon2-xop

[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o

[ 14%] Linking C static library libargon2-avx2.a

[ 14%] Built target argon2-avx2

[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o

[ 15%] Linking C static library libargon2-avx512f.a

[ 15%] Built target argon2-avx512f

[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o

[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o

[ 16%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o

[ 16%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o

[ 17%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o

[ 17%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o

[ 18%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o

[ 18%] Linking C static library libargon2.a

[ 18%] Built target argon2

[ 18%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o

[ 19%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o

[ 19%] Linking C static library libethash.a

[ 19%] Built target ethash

[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o

[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o

[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o

[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o

[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o

[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o

[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o

[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o

[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o

[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o

[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o

[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o

[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o

[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o

[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o

[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o

[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o

[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o

[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o

[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o

[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o

[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o

[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o

[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o

[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o

[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o

[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o

[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.o

[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o

[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.o

[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o

[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o

[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o

[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o

[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o

[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o

[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o

[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o

[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o

[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o

[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o

[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o

[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o

[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o

[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o

[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o

[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Chrono.cpp.o

[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o

[ 42%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops-data.c.o

[ 42%] Building C object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o

[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/Signatures.cpp.o

[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/cryptonote/WalletAddress.cpp.o

[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o

[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o

[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o

[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o

[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o

[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o

[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o

[ 47%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o

[ 47%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o

[ 48%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o

[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o

[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o

[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o

[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o

[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o

[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o

[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o

[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o

[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o

[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o

[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o

[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o

[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o

[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o

[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o

[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o

[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o

[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o

[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o

[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o

[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o

[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o

[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o

[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o

[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o

[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o

[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o

[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o

[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o

[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o

[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o

[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o

[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o

[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/core/Taskbar.cpp.o

[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o

[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o

[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o

[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o

[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o

[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/hw/api/HwApi.cpp.o

[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiBoard.cpp.o

[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiMemory.cpp.o

[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader.cpp.o

[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiTools.cpp.o

[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiReader_unix.cpp.o

[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o

[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o

[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process_unix.cpp.o

[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_hwloc.cpp.o

[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o

[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o

[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/LinuxMemory.cpp.o

[ 72%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o

[ 72%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o

[ 73%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o

[ 73%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o

[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o

[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o

[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o

[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o

[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o

[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o

[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CryptoNight_x86_vaes.cpp.o

[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o

[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o

[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o

[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o

[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o

[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o

[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o

[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o

[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o

[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o

[ 81%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o

[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o

[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o

[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o

[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o

[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o

[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o

[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o

[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o

[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o

[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o

[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxBasicStorage.cpp.o

[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o

[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o

[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o

[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxQueue.cpp.o

[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o

[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o

[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o

[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b_sse41.c.o

[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/avx2/blake2b_avx2.c.o

[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o

[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxFix_linux.cpp.o

[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr_linux.cpp.o

[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxMsr.cpp.o

[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/Msr.cpp.o

[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/hw/msr/MsrItem.cpp.o

[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o

[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPCache.cpp.o

[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/kawpow/KPHash.cpp.o

[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o

[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o

[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o

[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o

[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o

[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.o

[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o

[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o

[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o

[100%] Linking CXX executable xmrig

/usr/bin/ld: attempted static link of dynamic object `/usr/lib/gcc/x86_64-linux-gnu/11/../../../x86_64-linux-gnu/libuv.so'

/usr/bin/ld: attempted static link of dynamic object `/usr/lib/gcc/x86_64-linux-gnu/11/../../../x86_64-linux-gnu/libhwloc.so'

/usr/bin/ld: attempted static link of dynamic object `/usr/lib/gcc/x86_64-linux-gnu/11/../../../x86_64-linux-gnu/libuv.so'

/usr/bin/ld: attempted static link of dynamic object `/usr/lib/gcc/x86_64-linux-gnu/11/../../../x86_64-linux-gnu/libhwloc.so'

/usr/bin/ld: attempted static link of dynamic object `/usr/lib/gcc/x86_64-linux-gnu/11/libstdc++.so'

/usr/bin/ld: attempted static link of dynamic object `/lib/x86_64-linux-gnu/libm.so.6'

/usr/bin/ld: attempted static link of dynamic object `/lib/x86_64-linux-gnu/libmvec.so.1'

/usr/bin/ld: attempted static link of dynamic object `/lib/x86_64-linux-gnu/libc.so.6'

/usr/bin/ld: attempted static link of dynamic object `/lib64/ld-linux-x86-64.so.2'

collect2: error: ld returned 1 exit status

make[2]: *** [CMakeFiles/xmrig.dir/build.make:2912: xmrig] Error 1

make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2

make: *** [Makefile:91: all] Error 2

root@vuln-VirtualBox:/home/vuln/Desktop/test/xmrig# sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev

Reading package lists... Done

Building dependency tree... Done

Reading state information... Done

build-essential is already the newest version (12.9ubuntu3).

libuv1-dev is already the newest version (1.43.0-1).

cmake is already the newest version (3.22.1-1ubuntu1.22.04.1).

git is already the newest version (1:2.34.1-1ubuntu1.10).

libssl-dev is already the newest version (3.0.2-0ubuntu1.12).

libhwloc-dev is already the newest version (2.7.0-2ubuntu1).

0 upgraded, 0 newly installed, 0 to remove and 23 not upgraded.

what happen?

# Discussion History
## SChernykh | 2023-11-15T13:57:31+00:00
If you want to do a static build, you have to follow advanced build instructions for your OS: https://xmrig.com/docs/miner/build/ubuntu
i.e. you have to build all dependencies yourself.

## calojohn806 | 2023-11-15T16:02:46+00:00
how can i embedded with config.json  and no longer need config.json
whenever i run xmrig?

SChernykh ***@***.***> 于 2023年11月15日周三 21:57写道：

> If you want to do a static build, you have to follow advanced build
> instructions for your OS: https://xmrig.com/docs/miner/build/ubuntu
> i.e. you have to build all dependencies yourself.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3357#issuecomment-1812582827>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A7WVYKTGWCRJVFEN67AURH3YETC5NAVCNFSM6AAAAAA7MPYWNCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMJSGU4DEOBSG4>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


## Anaphylaxis | 2023-12-10T17:03:26+00:00
>root@vuln-VirtualBox:/home/vuln/Desktop/test# git clone https://github.com/xmrig/xmrig.git
root@vuln-VirtualBox:/home/vuln/Desktop/test# cmake -DBUILD_STATIC=ON -DWITH_EMBEDDED_CONFIG=ON .

You want to run cmake in /home/vuln/Desktop/test/xmrig. Git clone does not cd for you

# Action History
- Created by: calojohn806 | 2023-11-15T13:26:22+00:00
- Closed at: 2025-06-18T22:18:30+00:00
