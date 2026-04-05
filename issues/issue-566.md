---
title: '-bash: ./xmrig: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/566
author: wsm3
assignees: []
labels:
- question
created_at: '2018-04-19T21:13:48+00:00'
updated_at: '2018-04-22T18:09:45+00:00'
type: issue
status: closed
closed_at: '2018-04-22T18:09:45+00:00'
---

# Original Description
Hello!


**option(WITH_LIBCPUID "Use Libcpuid" OFF)
option(WITH_AEON     "CryptoNight-Lite support" OFF)
option(WITH_HTTPD    "HTTP REST API" OFF)
option(BUILD_STATIC  "Build static binary" ON)**


```
root@server:~//xmrig/build# cmake ..
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
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
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /root//xmrig/build
root@server:~//xmrig/build# make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_stub.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig
root@server:~//xmrig/build# ./xmrig
-bash: ./xmrig: No such file or directory
root@server:~//xmrig/build# ls -la
total 564
drwxr-xr-x 3 root root   4096 Apr 20 00:06 .
drwxr-xr-x 8 root root   4096 Apr 20 00:05 ..
-rw-r--r-- 1 root root  11960 Apr 20 00:05 CMakeCache.txt
drwxr-xr-x 5 root root   4096 Apr 20 00:06 CMakeFiles
-rw-r--r-- 1 root root   1362 Apr 20 00:05 cmake_install.cmake
-rw-r--r-- 1 root root  38129 Apr 20 00:05 Makefile
-rwxr-xr-x 1 root root 503608 Apr 20 00:06 xmrig
root@server:~//xmrig/build# ./xmrig
```


How build static version?
thx 


# Discussion History
## kpcyrd | 2018-04-19T21:34:12+00:00
the file is not static (and missing libraries, apparently), run `ldd xmrig` to confirm this.

You need to build a static binary on a musl based system, I recommend to use alpine and docker for this. Check this comment for instructions to run after you started an alpine docker container: https://github.com/xmrig/xmrig/pull/442#issuecomment-372456960

# Action History
- Created by: wsm3 | 2018-04-19T21:13:48+00:00
- Closed at: 2018-04-22T18:09:45+00:00
