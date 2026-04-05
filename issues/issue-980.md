---
title: unrecognized command line option ‘-Wno-class-memaccess’
source_url: https://github.com/xmrig/xmrig/issues/980
author: mbob001
assignees: []
labels: []
created_at: '2019-03-10T08:51:49+00:00'
updated_at: '2022-01-27T20:59:29+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:59:31+00:00'
---

# Original Description
Last version 2.14.1, in Debian with gcc version:

Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/6/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Debian 6.3.0-18+deb9u1' --with-bugurl=file:///usr/share/doc/gcc-6/README.Bugs --enable-languages=c,ada,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-6 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-6-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-6-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-6-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 6.3.0 20170516 (Debian 6.3.0-18+deb9u1) 

I will get an warning and after build cannot run:
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/CryptonightR_template.S.o
[  4%] Linking C static library libxmrig-asm.a
[  4%] Built target xmrig-asm
Scanning dependencies of target cpuid
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pool.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/Pools.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Handle.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.o
[ 80%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 81%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiRouter.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
/home/marek/App/xmrig/src/common/api/Httpd.cpp:74:13: warning: Value MHD_USE_EPOLL_LINUX_ONLY is deprecated, use MHD_USE_EPOLL
         flags |= MHD_USE_EPOLL_LINUX_ONLY;
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                   
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig

After run error: Unauthorized access to memory (SIGSEGV)

All packages (gcc) is updated to last version from repository.
Thanks.

# Discussion History
## Pasha49 | 2019-03-11T12:22:44+00:00
+1 same problem

## Uyouii | 2021-04-19T15:02:57+00:00
+2

## szczot3k | 2022-01-11T12:53:16+00:00
same here, gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)

## dvershinin | 2022-01-27T20:59:28+00:00
@szczot3k apparently, GCC 8.x is the minimum version supported.

# Action History
- Created by: mbob001 | 2019-03-10T08:51:49+00:00
- Closed at: 2019-08-02T11:59:31+00:00
