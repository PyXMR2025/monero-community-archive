---
title: error compile debian 7
source_url: https://github.com/xmrig/xmrig/issues/536
author: MasteRTriX
assignees: []
labels: []
created_at: '2018-04-11T04:13:32+00:00'
updated_at: '2018-11-05T13:23:55+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:23:55+00:00'
---

# Original Description
I have the following error in debian 7 trying to compile

```
make
Scanning dependencies of target cpuid
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
In file included from /root/xmrig/src/api/ApiState.cpp:37:0:
/root/xmrig/src/Mem.h:63:13: error: expected identifier before numeric constant
/root/xmrig/src/Mem.h:63:13: error: expected ‘,’ or ‘...’ before numeric constant
/root/xmrig/src/Mem.h:63:15: error: ISO C++ forbids declaration of ‘alignas’ with no type [-fpermissive]
/root/xmrig/src/Mem.h:63:15: error: expected ‘;’ at end of member declaration
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

# Discussion History
## passnet | 2018-04-11T10:11:04+00:00
Whats your gcc version? Post `gcc --version`.

## MasteRTriX | 2018-04-11T12:00:40+00:00
gcc (Debian 4.7.2-5) 4.7.2


## uzelacgs | 2018-04-14T12:37:50+00:00
I have same error with gcc (OpenSuSE 12.3 GCC) 5.1.0
[ 11%] Built target cpuid
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
In file included from /opt/xmrig-2.5.2/src/api/ApiState.cpp:37:0:
/opt/xmrig-2.5.2/src/Mem.h:63:13: error: expected identifier before numeric constant
/opt/xmrig-2.5.2/src/Mem.h:63:13: error: expected ‘,’ or ‘...’ before numeric constant
/opt/xmrig-2.5.2/src/Mem.h:63:15: error: ISO C++ forbids declaration of ‘alignas’ with no type [-fpermissive]
/opt/xmrig-2.5.2/src/Mem.h:63:15: error: expected ‘;’ at end of member declaration
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


## Oleg78an | 2018-05-18T07:08:41+00:00
Is there any solution?
Debian 7, gcc (Debian 4.7.2-5) 4.7.2

```
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
In file included from /home/odmin/xmrig/src/App.cpp:37:0:
/home/odmin/xmrig/src/crypto/CryptoNight.h:34:13: error: expected identifier before numeric constant
/home/odmin/xmrig/src/crypto/CryptoNight.h:34:13: error: expected ‘,’ or ‘...’ before numeric constant
/home/odmin/xmrig/src/crypto/CryptoNight.h:34:15: error: ISO C++ forbids declaration of ‘alignas’ with no type [-fpermissive]
/home/odmin/xmrig/src/crypto/CryptoNight.h:34:15: error: expected ‘;’ at end of member declaration
/home/odmin/xmrig/src/crypto/CryptoNight.h:35:13: error: expected identifier before numeric constant
/home/odmin/xmrig/src/crypto/CryptoNight.h:35:13: error: expected ‘,’ or ‘...’ before numeric constant
/home/odmin/xmrig/src/crypto/CryptoNight.h:35:15: error: ISO C++ forbids declaration of ‘alignas’ with no type [-fpermissive]
/home/odmin/xmrig/src/crypto/CryptoNight.h:35:15: error: expected ‘;’ at end of member declaration
/home/odmin/xmrig/src/crypto/CryptoNight.h:35:5: error: ‘int cryptonight_ctx::alignas(int)’ cannot be overloaded
/home/odmin/xmrig/src/crypto/CryptoNight.h:34:5: error: with ‘int cryptonight_ctx::alignas(int)’
In file included from /home/odmin/xmrig/src/App.cpp:38:0:
/home/odmin/xmrig/src/Mem.h:41:13: error: expected identifier before numeric constant
/home/odmin/xmrig/src/Mem.h:41:13: error: expected ‘,’ or ‘...’ before numeric constant
/home/odmin/xmrig/src/Mem.h:41:15: error: ISO C++ forbids declaration of ‘alignas’ with no type [-fpermissive]
/home/odmin/xmrig/src/Mem.h:41:15: error: expected ‘;’ at end of member declaration
In file included from /home/odmin/xmrig/src/workers/Workers.h:34:0,
                 from /home/odmin/xmrig/src/App.cpp:42:
/home/odmin/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/odmin/xmrig/src/net/JobResult.h:52:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Ошибка 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Ошибка 2
make: *** [all] Ошибка 2

```

Fedora 15, gcc (GCC) 4.6.3 20120306 (Red Hat 4.6.3-2)

```
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 10%] Built target cpuid
Scanning dependencies of target xmrig
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
cc1plus: error: unrecognized command line option ‘-std=c++11’
make[2]: *** [CMakeFiles/xmrig.dir/src/core/Config.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```



# Action History
- Created by: MasteRTriX | 2018-04-11T04:13:32+00:00
- Closed at: 2018-11-05T13:23:55+00:00
