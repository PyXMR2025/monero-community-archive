---
title: '''hwloc_get_numanode_obj_by_os_index'' was not declared in this scope'
source_url: https://github.com/xmrig/xmrig/issues/2420
author: code1010111
assignees: []
labels: []
created_at: '2021-06-02T13:04:39+00:00'
updated_at: '2021-06-02T14:23:59+00:00'
type: issue
status: closed
closed_at: '2021-06-02T14:23:59+00:00'
---

# Original Description
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
/root/xmrig/xmrig/src/crypto/rx/RxNUMAStorage.cpp: In function 'bool xmrig::bindToNUMANode(uint32_t)':
/root/xmrig/xmrig/src/crypto/rx/RxNUMAStorage.cpp:49:24: error: 'hwloc_get_numanode_obj_by_os_index' was not declared in this scope
     hwloc_obj_t node = hwloc_get_numanode_obj_by_os_index(cpu->topology(), nodeId);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/root/xmrig/xmrig/src/crypto/rx/RxNUMAStorage.cpp:49:24: note: suggested alternative: 'hwloc_get_pu_obj_by_os_index'
     hwloc_obj_t node = hwloc_get_numanode_obj_by_os_index(cpu->topology(), nodeId);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        hwloc_get_pu_obj_by_os_index
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2871: CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:163: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

# Discussion History
## xmrig | 2021-06-02T13:47:17+00:00
hwloc version? Oldest supported hwloc version is 1.10 which is already pretty ancient.
Thank you.

## code1010111 | 2021-06-02T13:53:44+00:00
my hwloc is 1.9
Thanks for help!

## code1010111 | 2021-06-02T14:23:59+00:00
use current stable version for hwloc - problem solved 

# Action History
- Created by: code1010111 | 2021-06-02T13:04:39+00:00
- Closed at: 2021-06-02T14:23:59+00:00
