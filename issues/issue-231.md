---
title: Trying to compile XMRig (Ubuntu 14.04.5 LTS)
source_url: https://github.com/xmrig/xmrig/issues/231
author: syrius01
assignees: []
labels: []
created_at: '2017-12-01T17:20:34+00:00'
updated_at: '2018-03-14T23:31:33+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:31:33+00:00'
---

# Original Description
$ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/home/sirius/XMR/XMRIG/xmrig/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/home/sirius/XMR/XMRIG/xmrig/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
                                                     ^
/home/sirius/XMR/XMRIG/xmrig/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^
/home/sirius/XMR/XMRIG/xmrig/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## mxjoe | 2017-12-02T14:01:52+00:00
It seems like I have a similiar error on macOS 10.13.2 Beta (libuv version 1.18.0). Please see below.

Steps to reproduce:

1. `cmake .. -DWITH_HTTPD=OFF -DUV_LIBRARY=/usr/local/opt/libuv/lib/libuv.a`
2. `make`

Result:
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
In file included from /Users/joe/Documents/Software/Mining/xmrig-mac/xmrig/src/api/Api.cpp:24:
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/string.h:61:15: fatal error: 'string.h' file not
      found
#include_next <string.h>
              ^~~~~~~~~~
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

## abale | 2017-12-03T15:16:57+00:00
I think it is due to an older version of libuv.  I have this same error with libuv 0.10

```
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/root/stak/xmrig-2.4.3/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/root/stak/xmrig-2.4.3/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
/root/stak/xmrig-2.4.3/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^~~~~~~~~
/root/stak/xmrig-2.4.3/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
```

## abale | 2017-12-03T15:21:50+00:00
Fixed by doing this:

```
sudo apt-get install make automake libtool curl -y
curl -sSL https://github.com/libuv/libuv/archive/v1.8.0.tar.gz | sudo tar zxfv - -C /usr/local/src
cd /usr/local/src/libuv-1.8.0
sudo sh autogen.sh
sudo ./configure
sudo make
sudo make install
sudo rm -rf /usr/local/src/libuv-1.8.0 && cd ~/
sudo ldconfig
```

then build with:

```
rm -rf CMakeFiles
rm -rf CMakeCache.txt
cmake -DWITH_HTTPD=OFF -DUV_LIBRARY=/usr/local/lib/libuv.so .
make clean
make
```

and you should get this:
```
worker1# make
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
[ 86%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
Linking CXX executable xmrig
[100%] Built target xmrig
```

## howTOdoIT2 | 2017-12-08T21:19:29+00:00
from what do I read here...it's seems that you remove the donation feature ... ain't that right   abale ?
:))))

# Action History
- Created by: syrius01 | 2017-12-01T17:20:34+00:00
- Closed at: 2018-03-14T23:31:33+00:00
