---
title: Centos and Ubuntu 14.04 build Error
source_url: https://github.com/xmrig/xmrig/issues/334
author: putuoka
assignees: []
labels: []
created_at: '2018-01-11T06:54:09+00:00'
updated_at: '2018-11-05T12:35:30+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:35:30+00:00'
---

# Original Description
I have tried with ubuntu and cannot install libuv1-dev after googling i successfully install using libuv-dev but error when running make. frustrate and i moved to centos. everything going fine in centos untill the last part when i type cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a i got an error:

Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc1: error: invalid option argument '-Ofast'
cc1: error: unrecognized command line option "-ftree-loop-if-convert-stores"
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [all] Error 2 

# Discussion History
## biaxz | 2018-01-11T09:02:30+00:00
-DWITH_LIBCPUID=OFF Disable libcpuid. Auto configuration of CPU after this will be very limited.

https://github.com/xmrig/xmrig/wiki/CentOS-Build
https://github.com/xmrig/xmrig/wiki/Ubuntu-Build


## wivern-co-uk | 2018-02-12T23:09:07+00:00
After adding `-DWITH_LIBCPUID=OFF` got another set of errors on `centos-release-6-9.el6.12.3.x86_64`:
```
$ cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a -DWITH_LIBCPUID=OFF
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
cc1plus: error: invalid option argument '-Ofast'
cc1plus: error: unrecognized command line option "-std=c++11"
cc1plus: error: unrecognized command line option "-ftree-loop-if-convert-stores"
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

## wivern-co-uk | 2018-02-12T23:36:57+00:00
Update g++ (GCC) to version 4.8.2 fixed both previous issues, but new one arised:
```
$ cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a
...
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
/xmrig/src/api/ApiState.cpp: In member function 'void ApiState::genId()':
/xmrig/src/api/ApiState.cpp:143:53: error: no match for 'operator<' (operand types are 'uv_err_t {aka uv_err_s}' and 'int')
     if (uv_interface_addresses(&interfaces, &count) < 0) {
                                                     ^
/xmrig/src/api/ApiState.cpp:150:58: error: 'uv_interface_address_t' has no member named 'phys_addr'
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^
/xmrig/src/api/ApiState.cpp:154:41: error: 'uv_interface_address_t' has no member named 'phys_addr'
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```


## wivern-co-uk | 2018-02-12T23:44:18+00:00
Looks like issue connected to https://github.com/xmrig/xmrig/issues/185

The original issue could be solved by `g++` update.

## Kustanto2 | 2018-03-01T08:20:21+00:00
hello how to make mining tomos ? with xmrig and vps

## sv0 | 2018-04-29T04:57:31+00:00
@wivern-co-uk This particular error happens because of [libuv](https://github.com/libuv/libuv) old version.
I guess CentOS 6.9 has libuv 0.10, and xmrig requires at least version 1.0.0

I'm strugling with the same issue on Debian 7.

# Action History
- Created by: putuoka | 2018-01-11T06:54:09+00:00
- Closed at: 2018-11-05T12:35:30+00:00
