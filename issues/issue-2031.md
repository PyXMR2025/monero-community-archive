---
title: 'benchmark failed: "Unknown CPU."'
source_url: https://github.com/xmrig/xmrig/issues/2031
author: Motsyo
assignees: []
labels: []
created_at: '2021-01-10T23:29:33+00:00'
updated_at: '2021-02-05T22:36:57+00:00'
type: issue
status: closed
closed_at: '2021-02-05T22:36:57+00:00'
---

# Original Description
OS - ALT Linux 9
CPU - Intel Xeon CPU E5-2630 v2

xmrig --version
XMRig 6.7.0
 built on Jan  2 2021 with GCC 8.4.1
 features: 64-bit AES

libuv/1.40.0
OpenSSL/1.1.1i

![Знімок екрану_2021-01-11_01-25-56](https://user-images.githubusercontent.com/23234078/104138383-693cba80-53ac-11eb-8497-8c00fc7d66bd.png)


# Discussion History
## Motsyo | 2021-01-10T23:31:52+00:00
Stress test - all Ok...
![Знімок екрану_2021-01-11_01-28-22](https://user-images.githubusercontent.com/23234078/104138442-c5074380-53ac-11eb-9568-8a53ea2a515a.png)


## Motsyo | 2021-01-10T23:39:03+00:00
Offline benchmark (without --submit option) - All Ok :)
![Знімок екрану_2021-01-11_01-36-06](https://user-images.githubusercontent.com/23234078/104138602-c5eca500-53ad-11eb-9621-859e106fa5d0.png)


## xmrig | 2021-01-11T01:03:25+00:00
Builds without hwloc not accepted by online benchmark.
Thank you. 

## Motsyo | 2021-02-02T18:59:00+00:00
```
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o
/usr/src/RPM/BUILD/xmrig/src/crypto/rx/RxNUMAStorage.cpp: In function 'bool xmrig::bindToNUMANode(uint32_t)':
/usr/src/RPM/BUILD/xmrig/src/crypto/rx/RxNUMAStorage.cpp:50:24: error: 'hwloc_get_numanode_obj_by_os_index' was not declared in this scope
     hwloc_obj_t node = hwloc_get_numanode_obj_by_os_index(cpu->topology(), nodeId);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/src/RPM/BUILD/xmrig/src/crypto/rx/RxNUMAStorage.cpp:50:24: note: suggested alternative: 'hwloc_get_pu_obj_by_os_index'
     hwloc_obj_t node = hwloc_get_numanode_obj_by_os_index(cpu->topology(), nodeId);
                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        hwloc_get_pu_obj_by_os_index
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2806: CMakeFiles/xmrig.dir/src/crypto/rx/RxNUMAStorage.cpp.o] Error 1
```
rpm -q libhwloc-devel
libhwloc-devel-1.9-alt1.x86_64

## xmrig | 2021-02-02T22:04:55+00:00
Minimum supported hwloc version is 1.10.
Thank you.

## Spudz76 | 2021-02-05T21:03:44+00:00
Build the included dependencies using the provided `build_deps.sh` script in `./scripts/`, then point your `CMAKE_PREFIX_PATH` to that location, and then you'll have all the correct versions of things.

Example: add `-DCMAKE_PREFIX_PATH=/usr/src/xmrig/scripts/deps` to whatever else on the first cmake command (configure step).  Observe cmake having found those libraries in that location with the built versions (currently `libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0`)...

Chances are the rest of the devel packs are old (oops I mean "**stable**") like the rest of RedHat.

# Action History
- Created by: Motsyo | 2021-01-10T23:29:33+00:00
- Closed at: 2021-02-05T22:36:57+00:00
