---
title: 'ApiState.cpp error: no match'
source_url: https://github.com/xmrig/xmrig/issues/154
author: maxtacu
assignees: []
labels:
- libuv
created_at: '2017-10-14T18:38:02+00:00'
updated_at: '2017-10-22T04:51:20+00:00'
type: issue
status: closed
closed_at: '2017-10-22T04:51:20+00:00'
---

# Original Description
```
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
../xmrig/src/api/ApiState.cpp: In member function âvoid ApiState::genId()â:
../xmrig/src/api/ApiState.cpp:143:53: error: no match for âoperator<â (operand types are âuv_err_t {aka uv_err_s}â and âintâ)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
                                                     ^
../xmrig/src/api/ApiState.cpp:150:58: error: âuv_interface_address_t {aka struct uv_interface_address_s}â has no member named âphys_addrâ
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^
../xmrig/src/api/ApiState.cpp:154:41: error: âuv_interface_address_t {aka struct uv_interface_address_s}â has no member named âphys_addrâ
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^
CMakeFiles/xmrig.dir/build.make:86: recipe for target 'CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```
Does anyone know how to fix that? Thanks in advance

# Discussion History
## xmrig | 2017-10-14T21:26:36+00:00
What operation system and libuv version did you use?
Thank you.

## MrSmiths | 2017-10-15T22:21:21+00:00
the same err here on Devuan GNU/Linux 1 (based on debian jessie) using libuv0.10

## MrSmiths | 2017-10-15T22:39:25+00:00
solved with adding 'deb http://auto.mirror.devuan.org/merged **jessie-backports main**' to /etc/apt/sources.list. After that libuv1-dev is  available for install..
~# apt-get update
~# apt-get install libuv1-dev

compilation finished successfully.. 


# Action History
- Created by: maxtacu | 2017-10-14T18:38:02+00:00
- Closed at: 2017-10-22T04:51:20+00:00
