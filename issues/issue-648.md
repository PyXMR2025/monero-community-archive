---
title: Static compile help
source_url: https://github.com/xmrig/xmrig/issues/648
author: echotxl
assignees: []
labels: []
created_at: '2018-05-24T12:54:47+00:00'
updated_at: '2018-11-05T13:42:40+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:42:40+00:00'
---

# Original Description
when i compile static file as  issue#238,it comes some errors.
the command is:
 `cmake .. -DWITH_HTTPD=OFF -DBUILD_STATIC=ON -DCMAKE_C_COMPILER=/root/new/musl-cross-make/output/bin/x86_64-linux-musl-gcc  -DCMAKE_CXX_COMPILER=/root/new/musl-cross-make/output/bin/x86_64-linux-musl-g++  -DUV_INCLUDE_DIR=/root/libuv/include -DUV_LIBRARY=/root/libuv/lib/libuv.a`

"/root/new/musl-cross-make/output/bin/x86_64-linux-musl-gcc" and "/root/new/musl-cross-make/output/bin/x86_64-linux-musl-g++" is the complier build by myself (musl-cross-make).

errors comes
`
root@ubuntu:~/xmrig/build# cmake .. -DWITH_HTTPD=OFF -DBUILD_STATIC=ON -DCMAKE_C_COMPILER=/root/musl-cross-make/output/bin/x86_64-linux-musl-gcc-7.2.0  -DCMAKE_CXX_COMPILER=/root/musl-cross-make/output/bin/x86_64-linux-musl-g++ -DUV_INCLUDE_DIR=/root/libuv-1.20.3/include  -DUV_LIBRARY=/usr/local/lib/libuv.a
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
-- Check for working C compiler: /root/musl-cross-make/output/bin/x86_64-linux-musl-gcc-7.2.0
-- Check for working C compiler: /root/musl-cross-make/output/bin/x86_64-linux-musl-gcc-7.2.0 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /root/musl-cross-make/output/bin/x86_64-linux-musl-g++
-- Check for working CXX compiler: /root/musl-cross-make/output/bin/x86_64-linux-musl-g++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/local/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
root@ubuntu:~/xmrig/build# make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[100%] Linking CXX executable xmrig
/usr/local/lib/libuv.a(libuv_la-uv-common.o): In function `fprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:97: undefined reference to `__fprintf_chk'
/usr/local/lib/libuv.a(libuv_la-uv-common.o): In function `snprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:64: undefined reference to `__snprintf_chk'
/usr/local/lib/libuv.a(libuv_la-uv-common.o): In function `memcpy':
/usr/include/x86_64-linux-gnu/bits/string3.h:53: undefined reference to `__memcpy_chk'
/usr/local/lib/libuv.a(libuv_la-async.o): In function `snprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:64: undefined reference to `__snprintf_chk'
/usr/local/lib/libuv.a(libuv_la-core.o): In function `open':
/usr/include/x86_64-linux-gnu/bits/fcntl2.h:57: undefined reference to `__open_2'
/usr/include/x86_64-linux-gnu/bits/fcntl2.h:57: undefined reference to `__open_2'
/usr/local/lib/libuv.a(libuv_la-fs.o): In function `pread':
/usr/include/x86_64-linux-gnu/bits/unistd.h:77: undefined reference to `__pread_chk'
/usr/local/lib/libuv.a(libuv_la-fs.o): In function `read':
/usr/include/x86_64-linux-gnu/bits/unistd.h:39: undefined reference to `__read_chk'
/usr/local/lib/libuv.a(libuv_la-fs.o): In function `snprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:64: undefined reference to `__snprintf_chk'
/usr/local/lib/libuv.a(libuv_la-process.o): In function `open':
/usr/include/x86_64-linux-gnu/bits/fcntl2.h:57: undefined reference to `__open_2'
/usr/local/lib/libuv.a(libuv_la-signal.o): In function `memmove':
/usr/include/x86_64-linux-gnu/bits/string3.h:59: undefined reference to `__memmove_chk'
/usr/local/lib/libuv.a(libuv_la-stream.o): In function `fprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:97: undefined reference to `__fprintf_chk'
/usr/local/lib/libuv.a(libuv_la-thread.o): In function `glibc_version_check':
/root/libuv-1.20.3/src/unix/thread.c:442: undefined reference to `gnu_get_libc_version'
/usr/local/lib/libuv.a(libuv_la-linux-core.o): In function `snprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:64: undefined reference to `__snprintf_chk'
/usr/local/lib/libuv.a(libuv_la-inet.o): In function `snprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:64: undefined reference to `__snprintf_chk'
/usr/local/lib/libuv.a(libuv_la-inet.o): In function `sprintf':
/usr/include/x86_64-linux-gnu/bits/stdio2.h:33: undefined reference to `__sprintf_chk'
/usr/local/lib/libuv.a(libuv_la-inet.o): In function `memcpy':
/usr/include/x86_64-linux-gnu/bits/string3.h:53: undefined reference to `__memcpy_chk'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:1136: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
`

who can help me ,thanks 

# Discussion History
# Action History
- Created by: echotxl | 2018-05-24T12:54:47+00:00
- Closed at: 2018-11-05T13:42:40+00:00
