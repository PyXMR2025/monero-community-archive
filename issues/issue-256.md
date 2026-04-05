---
title: issue during make
source_url: https://github.com/xmrig/xmrig/issues/256
author: akicked
assignees: []
labels:
- libuv
created_at: '2017-12-11T14:35:14+00:00'
updated_at: '2017-12-11T14:59:12+00:00'
type: issue
status: closed
closed_at: '2017-12-11T14:59:12+00:00'
---

# Original Description
root@triadica-desktop:/home/triadica/xmrig/build# make
[ 12%] Built target cpuid
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/home/triadica/xmrig/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/home/triadica/xmrig/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
                                                     ^
/home/triadica/xmrig/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^
/home/triadica/xmrig/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^
CMakeFiles/xmrig.dir/build.make:86: recipe for target 'CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

root@triadica-desktop:/home/triadica/xmrig/build# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial


Thanks in advance :) 




# Discussion History
## xmrig | 2017-12-11T14:55:08+00:00
Please install libuv1-dev package. https://github.com/xmrig/xmrig/wiki/Ubuntu-Build
Thank you.

## akicked | 2017-12-11T14:59:02+00:00
God bless you Sir, that did the trick ! 

# Action History
- Created by: akicked | 2017-12-11T14:35:14+00:00
- Closed at: 2017-12-11T14:59:12+00:00
