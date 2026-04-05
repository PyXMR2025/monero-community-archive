---
title: ApiState.cpp.o
source_url: https://github.com/xmrig/xmrig/issues/450
author: spidero
assignees: []
labels:
- libuv
created_at: '2018-03-15T10:17:07+00:00'
updated_at: '2018-03-16T17:44:23+00:00'
type: issue
status: closed
closed_at: '2018-03-16T17:44:23+00:00'
---

# Original Description
root@spiderohq:~/xmrig# cmake .
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig
root@spiderohq:~/xmrig# make
[ 13%] Built target cpuid
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/root/xmrig/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/root/xmrig/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
/root/xmrig/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^~~~~~~~~
/root/xmrig/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^~~~~~~~~
CMakeFiles/xmrig.dir/build.make:86: recipe for target 'CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed


# Discussion History
## xmrig | 2018-03-15T15:07:12+00:00
libuv 0.10 not supported, you should use libuv 1+.
Thank you.

# Action History
- Created by: spidero | 2018-03-15T10:17:07+00:00
- Closed at: 2018-03-16T17:44:23+00:00
