---
title: XMRig fails to build on Raspberry Pi 3 (64-bit)
source_url: https://github.com/xmrig/xmrig/issues/2178
author: nyiyui
assignees: []
labels: []
created_at: '2021-03-13T09:35:18+00:00'
updated_at: '2021-04-12T13:59:12+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:59:12+00:00'
---

# Original Description
**Describe the bug**
XMRig fails to build on Raspberry Pi 3 (64-bit) and a generic ARM system (Balena builder, should be similar to Raspberry Pi 3 (64-bit)).

**To Reproduce**
```bash
apt-get update
apt-get -yq --no-install-recommends install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev

git -c http.sslVerify=false clone https://github.com/xmrig/xmrig.git

cd xmrig
git -c http.sslVerify=false checkout `git tag | sort -V | grep -v "\-rc" | tail -1` # not necessary

mkdir -p build
cd build
cmake ..
make
```

**Expected behavior**
`cmake ..` and `make` ends successfully and binary is built.

**Required data**
 - Miner log N/A, providing Build log instead

**Part that probably is important**
```
[main]     In file included from /usr/src/app/xmrig/src/crypto/randomx/randomx.h:35:0,
[main]                      from /usr/src/app/xmrig/src/backend/cpu/CpuWorker.cpp:42:
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_swap_vec_f128(rx_vec_f128)’:
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h:418:39: error: ‘vcopyq_laneq_f64’ was not declared in this scope
[main]       temp = vcopyq_laneq_f64(temp, 1, a, 1);
[main]                                            ^
[main]     
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_set_vec_f128(uint64_t, uint64_t)’:
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h:426:66: error: ‘vcopyq_laneq_u64’ was not declared in this scope
[main]       return vreinterpretq_f64_u64(vcopyq_laneq_u64(temp0, 1, temp1, 0));
[main]                                                                       ^
[main]     
[main]     At global scope:
[main]     cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
[main]     
[main]     CMakeFiles/xmrig.dir/build.make:2006: recipe for target 'CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o' failed
[main]     make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1
[main]     
[main]     CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
[main]     make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
[main]     
[main]     Makefile:83: recipe for target 'all' failed
[main]     make: *** [all] Error 2
```

<details>
<summary>Build Log</summary>
<code>
[main]     + cmake ..
[main]     
[main]     -- The C compiler identification is GNU 6.3.0
[main]     -- The CXX compiler identification is GNU 6.3.0
[main]     -- Check for working C compiler: /usr/bin/cc
[main]     -- Check for working C compiler: /usr/bin/cc -- works
[main]     -- Detecting C compiler ABI info
[main]     -- Detecting C compiler ABI info - done
[main]     -- Detecting C compile features
[main]     -- Detecting C compile features - done
[main]     -- Check for working CXX compiler: /usr/bin/c++
[main]     -- Check for working CXX compiler: /usr/bin/c++ -- works
[main]     -- Detecting CXX compiler ABI info
[main]     -- Detecting CXX compiler ABI info - done
[main]     -- Detecting CXX compile features
[main]     -- Detecting CXX compile features - done
[main]     -- Use ARM_TARGET=8 (aarch64)
[main]     -- Performing Test XMRIG_ARM_CRYPTO
[main]     -- Performing Test XMRIG_ARM_CRYPTO - Success
[main]     -- Looking for syslog.h
[main]     -- Looking for syslog.h - found
[main]     -- Found HWLOC: /usr/lib/aarch64-linux-gnu/libhwloc.so  
[main]     -- Found UV: /usr/lib/aarch64-linux-gnu/libuv.a  
[main]     -- Looking for __builtin___clear_cache
[main]     -- Looking for __builtin___clear_cache - found
[main]     -- WITH_MSR=OFF
[main]     
[main]     -- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libssl.so;/usr/lib/aarch64-linux-gnu/libcrypto.so (found version "1.1.0l") 
[main]     -- Configuring done
[main]     -- Generating done
[main]     -- Build files have been written to: /usr/src/app/xmrig/build
[main]     + make
[main]     
[main]     Scanning dependencies of target argon2
[main]     [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[main]     [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[main]     [  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[main]     [  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[main]     [  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[main]     [  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[main]     [  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[main]     [  3%] Linking C static library libargon2.a
[main]     [  3%] Built target argon2
[main]     Scanning dependencies of target ethash
[main]     [  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[main]     [  4%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[main]     [  4%] Linking C static library libethash.a
[main]     [  4%] Built target ethash
[main]     Scanning dependencies of target xmrig
[main]     [  5%] Building CXX object CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o
[main]     [  5%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[main]     [  5%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[main]     [  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[main]     [  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[main]     [  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[main]     [  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[main]     [  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
[main]     [  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[main]     [  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
[main]     [  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[main]     [  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[main]     [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[main]     [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[main]     [ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[main]     [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
[main]     [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[main]     [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
[main]     [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
[main]     [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[main]     [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[main]     [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[main]     [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[main]     [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
[main]     [ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[main]     [ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[main]     [ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[main]     [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[main]     [ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[main]     [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[main]     [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[main]     [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[main]     [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[main]     [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
[main]     [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[main]     [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[main]     [ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[main]     [ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[main]     [ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[main]     [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[main]     [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Url.cpp.o
[main]     [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/LineReader.cpp.o
[main]     [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/NetBuffer.cpp.o
[main]     [ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[main]     [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Cvt.cpp.o
[main]     [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[main]     [ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[main]     [ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/AutoClient.cpp.o
[main]     [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/EthStratumClient.cpp.o
[main]     [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[main]     [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[main]     [ 26%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/llhttp.c.o
[main]     [ 26%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/api.c.o
[main]     [ 27%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/llhttp/http.c.o
[main]     [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[main]     [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[main]     [ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[main]     [ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[main]     [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Fetch.cpp.o
[main]     [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[main]     [ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[main]     [ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[main]     [ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpData.cpp.o
[main]     [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpListener.cpp.o
[main]     [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[main]     [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[main]     [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[main]     [ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[main]     [ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[main]     [ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[main]     [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[main]     [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[main]     [ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/Benchmark.cpp.o
[main]     [ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/benchmark/BenchState.cpp.o
[main]     [ 35%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/HashrateInterpolator.cpp.o
[main]     [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/GpuWorker.cpp.o
[main]     [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[main]     [ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[main]     [ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[main]     [ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[main]     [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[main]     [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[main]     In file included from /usr/src/app/xmrig/src/crypto/randomx/randomx.h:35:0,
[main]                      from /usr/src/app/xmrig/src/backend/cpu/CpuWorker.cpp:42:
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_swap_vec_f128(rx_vec_f128)’:
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h:418:39: error: ‘vcopyq_laneq_f64’ was not declared in this scope
[main]       temp = vcopyq_laneq_f64(temp, 1, a, 1);
[main]                                            ^
[main]     
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_set_vec_f128(uint64_t, uint64_t)’:
[main]     /usr/src/app/xmrig/src/crypto/randomx/intrin_portable.h:426:66: error: ‘vcopyq_laneq_u64’ was not declared in this scope
[main]       return vreinterpretq_f64_u64(vcopyq_laneq_u64(temp0, 1, temp1, 0));
[main]                                                                       ^
[main]     
[main]     At global scope:
[main]     cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
[main]     
[main]     CMakeFiles/xmrig.dir/build.make:2006: recipe for target 'CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o' failed
[main]     make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1
[main]     
[main]     CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
[main]     make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
[main]     
[main]     Makefile:83: recipe for target 'all' failed
[main]     make: *** [all] Error 2
[main]     
[main]     Removing intermediate container e14b628e47f7
[main]     The command '/bin/sh -c sh build.sh' returned a non-zero code: 2
</code>
</details>
 - Config file or command line N/A
 - OS: Raspbian/Debian Buster (64-bit)
 - For GPU related issues: N/A

**Additional context**
I am using balena.io and 2 Raspberry Pi 3s to hopefully run XMRig on each of them for fun.
Also, I am suspicious I have the wrong (version of the) libraries.


# Discussion History
## SChernykh | 2021-03-13T09:43:08+00:00
Try newer GCC version: https://github.com/xmrig/xmrig/issues/1203

## nyiyui | 2021-03-13T09:52:05+00:00
Seems like old GCC may be the culprit. somehow, gcc 7+ isn't available...
```
[main]     Setting up gcc-6 (6.3.0-18+deb9u1) ...
[main]     Setting up g++-6 (6.3.0-18+deb9u1) ...
[main]     Setting up dpkg-dev (1.18.25) ...
[main]     Setting up libnuma-dev:arm64 (2.0.11-2.1) ...
[main]     Setting up cmake (3.7.2-1) ...
[main]     Setting up libhwloc-dev:arm64 (1.11.5-1) ...
[main]     Setting up gcc (4:6.3.0-4) ...
[main]     Setting up g++ (4:6.3.0-4) ...
```

## nyiyui | 2021-03-13T10:12:20+00:00
Is there a sort of minimum required GCC version? Can't seem to find GCC 10 for Raspbian... (although I can build it from source, that would be painful)

## SChernykh | 2021-03-13T10:16:47+00:00
GCC 8 and newer should probably work.

## nyiyui | 2021-03-13T10:30:13+00:00
I'm using this to try to get GCC 10.1, so if that works then it should be fine. https://solarianprogrammer.com/2017/12/08/raspberry-pi-raspbian-install-gcc-compile-cpp-17-programs/

## resistor4u | 2021-03-23T17:36:22+00:00
on rpi 3b+ running `Linux ubuntu 5.4.0-1030-raspi #33-Ubuntu SMP PREEMPT Wed Feb 24 11:20:11 UTC 2021 aarch64 aarch64 aarch64 GNU/Linux`, I'm able to compile and execute xmrig, but connections are met with:
```
[2021-03-23 13:04:02.558]  net      xmr.pool.minergate.com:45700 connect error: "operation canceled"
[2021-03-23 13:20:28.890]  signal   Ctrl+C received, exiting
double free or corruption (fasttop)
```
the stress test also fails with:
```
[2021-03-23 13:21:51.878]  net      randomx.xmrig.com:3333 connect error: "operation canceled"
[2021-03-23 13:22:07.767]  signal   Ctrl+C received, exiting
double free or corruption (fasttop)
Aborted (core dumped)
```

but... the benchmark works:
```
ubuntu@ubuntu:~/github/xmrig/build_dev_gcc7$ ./xmrig-notls --bench=1M
 * ABOUT        XMRig/6.11.0-dev gcc/7.5.0
 * LIBS         libuv/1.34.2 hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (1) 64-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.4/0.9 GB (49%)
 * DONATE       1%
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-03-23 13:22:20.216]  bench    start benchmark hashes 1M algo rx/0
[2021-03-23 13:22:20.217]  cpu      use argon2 implementation default
[2021-03-23 13:22:21.417]  randomx  init dataset algo rx/0 (4 threads) seed 0000000000000000...
[2021-03-23 13:22:21.417]  randomx  not enough memory for RandomX dataset
[2021-03-23 13:22:21.418]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2021-03-23 13:22:26.982]  randomx  dataset ready (5564 ms)
[2021-03-23 13:22:26.983]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-03-23 13:22:26.989]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (6 ms)
[2021-03-23 13:23:27.028]  miner    speed 10s/60s/15m 23.87 n/a n/a H/s max 23.99 H/s
[2021-03-23 13:23:27.028]  bench     0.14% 1426/1000000
```

This is a gcc-7 build, but I'm getting the same for gcc-9. I haven't tried gcc-8.

## nyiyui | 2021-03-23T22:15:29+00:00
@resistor4u, how did you install GCC 9? I couldn't get it to install. I'll try Ubuntu later today, I have been using Raspbian.

About the `operation cancelled` error, I got mine working (on a non Raspberry Pi) by running it from a terminal emulator instead of the usual (?) terminal without X.

## resistor4u | 2021-03-24T00:44:32+00:00
@colourdelete it might be the case Raspian doesn't have gcc-8 in standard repos. I can't swap OS at the moment because I'm logging some weather data.

@SChernykh FWIW, gcc v. 8.4.0 and also clang 10 gives the same `operation cancelled` error. They build fine, but will not mine. Separate issue?

## nyiyui | 2021-03-24T03:57:40+00:00
I switched to using Ubuntu and it worked. I was using Balena, so I changes it from `debian` to `ubuntu`. I'm stuck on a bash error, but build seems fine.

# Action History
- Created by: nyiyui | 2021-03-13T09:35:18+00:00
- Closed at: 2021-04-12T13:59:12+00:00
