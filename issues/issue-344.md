---
title: Raspberry Pi-3B-Centos7 complied in arm-xmrig
source_url: https://github.com/xmrig/xmrig/issues/344
author: rainmo
assignees: []
labels:
- arm
created_at: '2018-01-17T09:44:07+00:00'
updated_at: '2018-01-19T02:35:01+00:00'
type: issue
status: closed
closed_at: '2018-01-19T02:35:01+00:00'
---

# Original Description
I get a problem like this,  who can tell me how to fix it. Thanks.
arm-xmrig edtion
[root@centos-rpi3 build]# make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc: error: unrecognized command line option '-maes'
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [all] Error 2

# Discussion History
## xmrig | 2018-01-17T11:23:06+00:00
Please add line `message("CMAKE_SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR}")` into begin of file `cmake/cpu.cmake`, run `cmake` and copy first line.

Output should looks like `CMAKE_SYSTEM_PROCESSOR: armv7-a` probably CPU arch not exists in this list https://github.com/xmrig/xmrig/blob/master/cmake/cpu.cmake#L18
Thank you.

## rainmo | 2018-01-18T02:03:56+00:00
@xmrig 
## cpu edtion: CMAKE_SYSTEM_PROCESSOR: armv7l
I have modify cpu.cmake file.
if (NOT CMAKE_SYSTEM_PROCESSOR)
    message(WARNING "CMAKE_SYSTEM_PROCESSOR not defined")
endif()

if (CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|AMD64)$")
    add_definitions(/DRAPIDJSON_SSE2)
endif()

## if (CMAKE_SYSTEM_PROCESSOR MATCHES "^(armv7l)$")
    set(XMRIG_ARM ON)
    set(XMRIG_ARMv7l ON)
    set(WITH_LIBCPUID OFF)

    add_definitions(/DXMRIG_ARM)
    add_definitions(/DXMRIG_ARMv7)

endif()

++++++++++
but when I run "make", get a new problem.
[root@centos-rpi3 build]# make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
c++: error: unrecognized command line option '-maes'
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

Please tell me how to fix it. Many thanks.



# Action History
- Created by: rainmo | 2018-01-17T09:44:07+00:00
- Closed at: 2018-01-19T02:35:01+00:00
