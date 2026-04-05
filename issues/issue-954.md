---
title: Build static error
source_url: https://github.com/xmrig/xmrig/issues/954
author: minzak
assignees: []
labels: []
created_at: '2019-02-27T12:07:27+00:00'
updated_at: '2019-08-02T12:58:55+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:58:55+00:00'
---

# Original Description
I'm trying to build Full static under Debian9, or CentOS7/6
Very interested i have when i build atatic under Debian, but ldd says that is not STATIC and shows some library depencies. 
cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF -DBUILD_STATIC=ON -DWITH_TLS=OFF
```
root@debian:/usr/src/xmrig/build# cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF -DBUILD_STATIC=ON -DWITH_TLS=OFF
-- The C compiler identification is GNU 6.3.0
-- The CXX compiler identification is GNU 6.3.0
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
-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.a
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/xmrig/build
root@debian:/usr/src/xmrig/build# make
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/CryptonightR_template.S.o
[  4%] Linking C static library libxmrig-asm.a
[  4%] Built target xmrig-asm
Scanning dependencies of target cpuid
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 12%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 13%] Linking C static library libcpuid.a
[ 13%] Built target cpuid
Scanning dependencies of target xmrig-notls
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/api/NetworkState.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Json.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Signals.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/Pool.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/Pools.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Handle.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/config/CommonConfig.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/config/ConfigLoader.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/config/ConfigWatcher.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/Console.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/crypto/Algorithm.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/crypto/keccak.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/BasicLog.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/ConsoleLog.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/FileLog.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/Log.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/Client.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/Job.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/SubmitResult.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/Platform.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Config.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Mem.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/CpuThread.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Handle.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Hashrate.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/MultiWorker.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Worker.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Workers.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Json_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/Platform_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Mem_unix.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/cpu/AdvancedCpuInfo.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/cpu/Cpu.cpp.o
[ 86%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_blake256.c.o
[ 89%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_jh.c.o
[ 90%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_skein.c.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/CryptonightR_gen.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/SysLog.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/Asm.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn_gpu_avx.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig-notls
[100%] Built target xmrig-notls
root@debian:/usr/src/xmrig/build# ldd xmrig-notls
        linux-vdso.so.1 (0x00007ffc383ae000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f3baa218000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f3baa010000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f3ba9e0c000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f3ba9a8a000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f3ba9786000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3ba93e7000)
        /lib/ld64.so.1 => /lib64/ld-linux-x86-64.so.2 (0x00007f3baa435000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f3ba91d0000)

```

And after that i now that i must make it under CentOS only, and i trying to build under CetnOS6 with RHEL devtoolset-6.
sudo yum install centos-release-scl cmake3
sudo yum install devtoolset-6-gcc devtoolset-6-gcc-c++
sudo scl enable devtoolset-6 bash

Also i have builded libuv v1.8 with libs (.a + .so)
I also replace next:
-std=c++11 to -std=c++0x
-Ofast` to `-O2

Add directives:
add_definitions(/D__STDC_FORMAT_MACROS)
add_executable/iset(CMAKE_EXE_LINKER_FLAGS " -static")

And i have completed this command:
cmake3 .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/local/lib/libuv.a -DWITH_HTTPD=OFF -DBUILD_STATIC=ON -DWITH_TLS=OFF

```
[root@localhost build]# cmake3 .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/local/lib/libuv.a -DWITH_HTTPD=OFF -DBUILD_STATIC=ON -DWITH_TLS=OFF
-- The C compiler identification is GNU 6.3.1
-- The CXX compiler identification is GNU 6.3.1
-- Check for working C compiler: /opt/rh/devtoolset-6/root/usr/bin/cc
-- Check for working C compiler: /opt/rh/devtoolset-6/root/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /opt/rh/devtoolset-6/root/usr/bin/c++
-- Check for working CXX compiler: /opt/rh/devtoolset-6/root/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/local/lib/libuv.a
-- The ASM compiler identification is GNU
-- Found assembler: /opt/rh/devtoolset-6/root/usr/bin/cc
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/src/xmrig/build

```
But in make i have ld errors:

**ld: cannot find -lpthread**

```
[root@localhost build]# make
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/CryptonightR_template.S.o
[  4%] Linking C static library libxmrig-asm.a
[  4%] Built target xmrig-asm
Scanning dependencies of target cpuid
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 12%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 13%] Linking C static library libcpuid.a
[ 13%] Built target cpuid
Scanning dependencies of target xmrig-notls
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/api/NetworkState.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Json.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Signals.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/Pool.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/Pools.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Handle.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/config/CommonConfig.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/config/ConfigLoader.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/config/ConfigWatcher.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/Console.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/crypto/Algorithm.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/crypto/keccak.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/BasicLog.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/ConsoleLog.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/FileLog.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/Log.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/Client.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/Job.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/net/SubmitResult.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/Platform.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Config.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Mem.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/CpuThread.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Handle.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Hashrate.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/MultiWorker.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Worker.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/Workers.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Json_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/Platform_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Mem_unix.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/cpu/AdvancedCpuInfo.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/cpu/Cpu.cpp.o
[ 86%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_blake256.c.o
[ 89%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_jh.c.o
[ 90%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_skein.c.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/CryptonightR_gen.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/log/SysLog.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/Asm.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn_gpu_avx.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig-notls
/opt/rh/devtoolset-6/root/usr/libexec/gcc/x86_64-redhat-linux/6.3.1/ld: cannot find -lpthread
/opt/rh/devtoolset-6/root/usr/libexec/gcc/x86_64-redhat-linux/6.3.1/ld: cannot find -lrt
/opt/rh/devtoolset-6/root/usr/libexec/gcc/x86_64-redhat-linux/6.3.1/ld: cannot find -ldl
/opt/rh/devtoolset-6/root/usr/libexec/gcc/x86_64-redhat-linux/6.3.1/ld: cannot find -lm
/opt/rh/devtoolset-6/root/usr/libexec/gcc/x86_64-redhat-linux/6.3.1/ld: cannot find -lc
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig-notls] Error 1
make[1]: *** [CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [all] Error 2
[root@localhost build]#
```
After **ld -lpthread --verbose** i have:
```
==================================================
attempt to open //opt/rh/devtoolset-6/root/usr/x86_64-redhat-linux/lib64/libpthread.so failed
attempt to open //opt/rh/devtoolset-6/root/usr/x86_64-redhat-linux/lib64/libpthread.a failed
attempt to open //opt/rh/devtoolset-6/root/usr/lib64/libpthread.so failed
attempt to open //opt/rh/devtoolset-6/root/usr/lib64/libpthread.a failed
attempt to open //usr/local/lib64/libpthread.so failed
attempt to open //usr/local/lib64/libpthread.a failed
attempt to open //lib64/libpthread.so failed
attempt to open //lib64/libpthread.a failed
attempt to open //usr/lib64/libpthread.so succeeded
opened script file //usr/lib64/libpthread.so
opened script file //usr/lib64/libpthread.so
attempt to open /lib64/libpthread.so.0 succeeded
/lib64/libpthread.so.0
attempt to open /usr/lib64/libpthread_nonshared.a succeeded
libc.so.6 needed by /lib64/libpthread.so.0
found libc.so.6 at //lib64/libc.so.6
ld-linux-x86-64.so.2 needed by /lib64/libpthread.so.0
found ld-linux-x86-64.so.2 at //lib64/ld-linux-x86-64.so.2
ld: warning: cannot find entry symbol _start; not setting start address
```

what is wrong?


# Discussion History
## ghost | 2019-02-28T03:38:29+00:00
i'm not familiar with devtoolset-6 but redhat/fedora/centos variants will generally not supply the static libraries by default.  look at installing glibc-static.

## 0xman | 2019-03-01T23:23:13+00:00
Its not gonna be 100% static you need to use murl

## minzak | 2019-03-02T07:41:56+00:00
https://github.com/xmrig/xmrig/issues/954#issuecomment-468845898 You wrong, for example this link for fulled static https://github.com/mlove19/xmrig.
Also a year ago I was made static, but forget how I did it. 

## 0xman | 2019-03-04T14:50:08+00:00
Pretty sure i'm not but ok

# Action History
- Created by: minzak | 2019-02-27T12:07:27+00:00
- Closed at: 2019-08-02T12:58:55+00:00
