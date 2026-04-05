---
title: 'error: ‘hwloc_get_numanode_obj_by_os_index’ was not declared in this scope'
source_url: https://github.com/xmrig/xmrig/issues/1115
author: duku1
assignees: []
labels: []
created_at: '2019-08-15T15:03:44+00:00'
updated_at: '2019-08-17T18:37:37+00:00'
type: issue
status: closed
closed_at: '2019-08-17T18:37:37+00:00'
---

# Original Description
Hello. I try compile xmrig on CentOS 6. Use gcc 6.3 or 7.2 but got same result: 
`[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o /xmrig/src/crypto/rx/Rx.cpp: In function ‘void xmrig::bindToNUMANode(uint32_t)’: /xmrig/src/crypto/rx/Rx.cpp:68:24: error: ‘hwloc_get_numanode_obj_by_os_index’ was not declared in this scope hwloc_obj_t node = hwloc_get_numanode_obj_by_os_index(topology, nodeId); ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /xmrig/src/crypto/rx/Rx.cpp:68:24: note: suggested alternative: ‘hwloc_get_pu_obj_by_os_index’ hwloc_obj_t node = hwloc_get_numanode_obj_by_os_index(topology, nodeId); ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ hwloc_get_pu_obj_by_os_index At global scope: cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’ make[2]: *** [CMakeFiles/xmrig.dir/build.make:2415: CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o] Error 1 make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2 make: *** [Makefile:84: all] Error 2`

# Discussion History
## xmrig | 2019-08-17T14:01:24+00:00
Probably hwloc version is too old, minimum tested version is 1.10.0.
You have 2 options:
1. Build without hwloc support, cmake option `-DWITH_HWLOC=OFF`.
2. Somehow get new hwloc version, for example build from it source https://github.com/xmrig/xmrig/issues/1099#issuecomment-518089405


# Action History
- Created by: duku1 | 2019-08-15T15:03:44+00:00
- Closed at: 2019-08-17T18:37:37+00:00
