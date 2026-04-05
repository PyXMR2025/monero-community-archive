---
title: armv8l make error (using _x86 instead of _arm)
source_url: https://github.com/xmrig/xmrig/issues/744
author: sahand-sh
assignees:
- xmrig
labels:
- arm
- review later
created_at: '2018-08-29T10:49:38+00:00'
updated_at: '2020-07-09T08:36:53+00:00'
type: issue
status: closed
closed_at: '2019-02-03T19:28:14+00:00'
---

# Original Description
cmake result:
-- The C compiler identification is Clang 6.0.1
-- The CXX compiler identification is Clang 6.0.1
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
-- Found UV: /usr/lib/libuv.so  
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/xmrig/xmrig/build





Make Result:
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
clang-6.0: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /home/xmrig/xmrig/src/workers/CpuThread.cpp:35:
In file included from /home/xmrig/xmrig/src/crypto/CryptoNight_x86.h:30:
In file included from /usr/lib/clang/6.0.1/include/x86intrin.h:27:
/usr/lib/clang/6.0.1/include/ia32intrin.h:48:10: error: use of undeclared identifier '__builtin_ia32_readeflags_u32'
  return __builtin_ia32_readeflags_u32();
         ^
/usr/lib/clang/6.0.1/include/ia32intrin.h:54:3: error: use of undeclared identifier '__builtin_ia32_writeeflags_u32'
  __builtin_ia32_writeeflags_u32(__f);
  ^
/usr/lib/clang/6.0.1/include/ia32intrin.h:60:10: error: use of undeclared identifier '__builtin_ia32_rdpmc'; did you mean '__builtin_arm_dmb'?
  return __builtin_ia32_rdpmc(__A);
         ^
/usr/lib/clang/6.0.1/include/ia32intrin.h:60:10: note: '__builtin_arm_dmb' declared here
/usr/lib/clang/6.0.1/include/ia32intrin.h:60:10: error: argument to '__builtin_arm_dmb' must be a constant integer
  return __builtin_ia32_rdpmc(__A);
         ^                    ~~~
/usr/lib/clang/6.0.1/include/ia32intrin.h:66:10: error: use of undeclared identifier '__builtin_ia32_rdtscp'; did you mean '__builtin_arm_rsrp'?
  return __builtin_ia32_rdtscp(__A);
         ^
/usr/lib/clang/6.0.1/include/ia32intrin.h:66:10: note: '__builtin_arm_rsrp' declared here
/usr/lib/clang/6.0.1/include/ia32intrin.h:66:32: error: cannot initialize a parameter of type 'const char *' with an lvalue of type 'unsigned int *'
  return __builtin_ia32_rdtscp(__A);
                               ^~~
In file included from /home/xmrig/xmrig/src/workers/CpuThread.cpp:35:
In file included from /home/xmrig/xmrig/src/crypto/CryptoNight_x86.h:30:
In file included from /usr/lib/clang/6.0.1/include/x86intrin.h:29:
In file included from /usr/lib/clang/6.0.1/include/immintrin.h:28:
/usr/lib/clang/6.0.1/include/mmintrin.h:47:5: error: use of undeclared identifier '__builtin_ia32_emms'; did you mean '__builtin_isless'?
    __builtin_ia32_emms();
    ^
/usr/lib/clang/6.0.1/include/mmintrin.h:47:5: note: '__builtin_isless' declared here
/usr/lib/clang/6.0.1/include/mmintrin.h:47:25: error: too few arguments to function call, expected 2, have 0
    __builtin_ia32_emms();
                        ^
/usr/lib/clang/6.0.1/include/mmintrin.h:64:19: error: use of undeclared identifier '__builtin_ia32_vec_init_v2si'
    return (__m64)__builtin_ia32_vec_init_v2si(__i, 0);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:81:12: error: use of undeclared identifier '__builtin_ia32_vec_ext_v2si'
    return __builtin_ia32_vec_ext_v2si((__v2si)__m, 0);
           ^
/usr/lib/clang/6.0.1/include/mmintrin.h:143:19: error: use of undeclared identifier '__builtin_ia32_packsswb'
    return (__m64)__builtin_ia32_packsswb((__v4hi)__m1, (__v4hi)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:173:19: error: use of undeclared identifier '__builtin_ia32_packssdw'
    return (__m64)__builtin_ia32_packssdw((__v2si)__m1, (__v2si)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:203:19: error: use of undeclared identifier '__builtin_ia32_packuswb'
    return (__m64)__builtin_ia32_packuswb((__v4hi)__m1, (__v4hi)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:230:19: error: use of undeclared identifier '__builtin_ia32_punpckhbw'
    return (__m64)__builtin_ia32_punpckhbw((__v8qi)__m1, (__v8qi)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:253:19: error: use of undeclared identifier '__builtin_ia32_punpckhwd'
    return (__m64)__builtin_ia32_punpckhwd((__v4hi)__m1, (__v4hi)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:274:19: error: use of undeclared identifier '__builtin_ia32_punpckhdq'
    return (__m64)__builtin_ia32_punpckhdq((__v2si)__m1, (__v2si)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:301:19: error: use of undeclared identifier '__builtin_ia32_punpcklbw'
    return (__m64)__builtin_ia32_punpcklbw((__v8qi)__m1, (__v8qi)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:324:19: error: use of undeclared identifier '__builtin_ia32_punpcklwd'
    return (__m64)__builtin_ia32_punpcklwd((__v4hi)__m1, (__v4hi)__m2);
                  ^
/usr/lib/clang/6.0.1/include/mmintrin.h:345:19: error: use of undeclared identifier '__builtin_ia32_punpckldq'
    return (__m64)__builtin_ia32_punpckldq((__v2si)__m1, (__v2si)__m2);
                  ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:375: CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Discussion History
## sahand-sh | 2018-08-29T10:53:02+00:00
I tried to compile for arm using `cmake .. -DXMRIG_ARM=ON`  but I had same error

## lhirlimann | 2018-11-07T11:57:05+00:00
Try to set -ferror-limit to a big number and see if that helps. Else fix the issues (clang is precise for that) and propose a patch. Or use gcc it should compile fine (it did on my system a few weeks ago).

## xmrig | 2019-02-03T19:28:14+00:00
https://github.com/xmrig/xmrig/commit/7e4858db2a537b4777073814157ce17a90740fab now possible override ARM architecture detection via cmake options `-DARM_TARGET=8` or `-DARM_TARGET=7`.
Thank you.

## pragathoys | 2020-05-12T05:28:37+00:00
> [7e4858d](https://github.com/xmrig/xmrig/commit/7e4858db2a537b4777073814157ce17a90740fab) now possible override ARM architecture detection via cmake options `-DARM_TARGET=8` or `-DARM_TARGET=7`.
> Thank you.

thank you @xmrig  !
This help me to build it for an RPi 3 with  armv7l

## alterhu2020 | 2020-07-08T16:31:58+00:00
It still not working when use cmake command as below: `cmake ..  -DARM_TARGET=7 ` with `Raspberry Pi 4 Model B Rev 1.2` and Raspian version `Raspbian GNU/Linux 10 (buster)`, the error when run the `make` command shows below:

```
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[100%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: in function `xmrig::OclWorker::consumeJob()':
OclWorker.cpp:(.text+0x3cc): undefined reference to `__atomic_load_8'
/usr/bin/ld: OclWorker.cpp:(.text+0x3fc): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: in function `xmrig::OclWorker::start()':
OclWorker.cpp:(.text+0x66c): undefined reference to `__atomic_load_8'
/usr/bin/ld: OclWorker.cpp:(.text+0x6d8): undefined reference to `__atomic_load_8'
/usr/bin/ld: OclWorker.cpp:(.text+0x6ec): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o:OclWorker.cpp:(.text+0x728): more undefined references to `__atomic_load_8' follow
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x3c): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x1a0): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x1e0): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): undefined reference to `__atomic_store_8'
/usr/bin/ld: Worker.cpp:(.text+0xbc): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0xdc): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::start(std::vector<xmrig::OclLaunchData, std::allocator<xmrig::OclLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x200): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::start(std::vector<xmrig::CudaLaunchData, std::allocator<xmrig::CudaLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<3u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<4u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<5u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x14): more undefined references to `__atomic_load_8' follow
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3195：xmrig] error 1
make[1]: *** [CMakeFiles/Makefile2:74：CMakeFiles/xmrig.dir/all] error 2
make: *** [Makefile:84：all] error 2

```
Any update for this issue? thanks very much. @xmrig

## pragathoys | 2020-07-09T08:36:53+00:00
Hi,
please have a look at this example:
[https://github.com/pragathoys/build_xmrig_for_armv7](https://github.com/pragathoys/build_xmrig_for_armv7)



> It still not working when use cmake command as below: `cmake .. -DARM_TARGET=7 ` with `Raspberry Pi 4 Model B Rev 1.2` and Raspian version `Raspbian GNU/Linux 10 (buster)`, the error when run the `make` command shows below:
> 
> ```
> [ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
> [100%] Linking CXX executable xmrig
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: in function `xmrig::OclWorker::consumeJob()':
> OclWorker.cpp:(.text+0x3cc): undefined reference to `__atomic_load_8'
> /usr/bin/ld: OclWorker.cpp:(.text+0x3fc): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: in function `xmrig::OclWorker::start()':
> OclWorker.cpp:(.text+0x66c): undefined reference to `__atomic_load_8'
> /usr/bin/ld: OclWorker.cpp:(.text+0x6d8): undefined reference to `__atomic_load_8'
> /usr/bin/ld: OclWorker.cpp:(.text+0x6ec): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o:OclWorker.cpp:(.text+0x728): more undefined references to `__atomic_load_8' follow
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::Nonce()':
> Nonce.cpp:(.text+0x3c): undefined reference to `__atomic_store_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::stop()':
> Nonce.cpp:(.text+0x1a0): undefined reference to `__atomic_store_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::touch()':
> Nonce.cpp:(.text+0x1e0): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::storeStats()':
> Worker.cpp:(.text+0x90): undefined reference to `__atomic_store_8'
> /usr/bin/ld: Worker.cpp:(.text+0xbc): undefined reference to `__atomic_store_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::timestamp() const':
> Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::hashCount() const':
> Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
> /usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
> /usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::stop()':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
> /usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0xdc): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::tick(unsigned long long)':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
> /usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::stop()':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
> /usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::tick(unsigned long long)':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
> /usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> > const&)':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::start(std::vector<xmrig::OclLaunchData, std::allocator<xmrig::OclLaunchData> > const&)':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x200): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::start(std::vector<xmrig::CudaLaunchData, std::allocator<xmrig::CudaLaunchData> > const&)':
> Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): undefined reference to `__atomic_fetch_add_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
> CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
> CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<3u>::allocateRandomX_VM()':
> CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<4u>::allocateRandomX_VM()':
> CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<5u>::allocateRandomX_VM()':
> CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
> /usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x14): more undefined references to `__atomic_load_8' follow
> collect2: error: ld returned 1 exit status
> make[2]: *** [CMakeFiles/xmrig.dir/build.make:3195：xmrig] error 1
> make[1]: *** [CMakeFiles/Makefile2:74：CMakeFiles/xmrig.dir/all] error 2
> make: *** [Makefile:84：all] error 2
> ```
> 
> Any update for this issue? thanks very much. @xmrig



# Action History
- Created by: sahand-sh | 2018-08-29T10:49:38+00:00
- Closed at: 2019-02-03T19:28:14+00:00
