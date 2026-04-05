---
title: Compile issues under DragonflyBSD
source_url: https://github.com/xmrig/xmrig/issues/3179
author: noice78
assignees: []
labels:
- bug
created_at: '2022-12-16T12:47:18+00:00'
updated_at: '2023-01-04T19:27:45+00:00'
type: issue
status: closed
closed_at: '2023-01-04T19:27:45+00:00'
---

# Original Description
**Describe the bug**
Compile issues under DragonflyBSD

**To Reproduce**
Cmake options, both:

`cmake .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON -DCMAKE_C_COMPILER=clang
`

AND

`cmake .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON
`

Results:

```
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[...]/xmrig/src/crypto/common/VirtualMemory_unix.cpp:154:109: error: use of undeclared identifier 'MAP_POPULATE'
        mem = mmap(0, align(size), PROT_READ | PROT_WRITE | SECURE_PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS | MAP_POPULATE | hugePagesFlag(hugePageSize()), -1, 0);
                                                                                                            ^
/root/gits/xmrig/src/crypto/common/VirtualMemory_unix.cpp:174:85: error: use of undeclared identifier 'MAP_HUGETLB'
    void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE | hugePagesFlag(hugePageSize()), 0, 0);
                                                                                    ^
/root/gits/xmrig/src/crypto/common/VirtualMemory_unix.cpp:174:99: error: use of undeclared identifier 'MAP_POPULATE'
    void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE | hugePagesFlag(hugePageSize()), 0, 0);
                                                                                                  ^
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
3 errors generated.
--- CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o ---
*** [CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o] Error code 1
```

**Expected behavior**
Compile without errors

**Required data**
 - OS: Dragonfly BSD

**Additional context**
N/A


# Discussion History
## SChernykh | 2022-12-16T14:28:46+00:00
@noice78 can you try to compile https://github.com/xmrig/xmrig/pull/3180 ?

## noice78 | 2022-12-17T09:09:23+00:00
Unfortunately, with:
`cmake .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON -DCMAKE_C_COMPILER=clang`

now I get this error:
```
xmrig/src/base/kernel/Platform_unix.cpp:22:13: fatal error: sys/cpuset.h: No such file or directory
 #   include <sys/cpuset.h>
             ^~~~~~~~~~~~~~
compilation terminated.
```

and with:
`cmake .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON -DCMAKE_C_COMPILER=clang`

These warnings:
```
In file included from /root/gits/xmrig/src/core/config/ConfigTransform.cpp:19:
xmrig/src/core/config/ConfigTransform.h:43:10: warning: private field 'm_opencl' is not used [-Wunused-private-field]
    bool m_opencl           = false;
         ^
[...]
xmrig/src/net/JobResults.cpp:294:16: warning: private field 'm_hwAES' is not used [-Wunused-private-field]
    const bool m_hwAES;
               ^
```

And these errors:
```
xmrig/src/base/kernel/Platform_unix.cpp:22:13: fatal error: 'sys/cpuset.h' file not found
#   include <sys/cpuset.h>
            ^~~~~~~~~~~~~~
[...]
xmrig/src/crypto/common/VirtualMemory_unix.cpp:142:102: error: use of undeclared identifier 'MAP_ALIGNED_SUPER'
        mem = mmap(0, size, PROT_READ | PROT_WRITE | SECURE_PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS | MAP_ALIGNED_SUPER | MAP_PREFAULT_READ, -1, 0);
                                                                                                     ^
xmrig/src/crypto/common/VirtualMemory_unix.cpp:142:122: error: use of undeclared identifier 'MAP_PREFAULT_READ'
        mem = mmap(0, size, PROT_READ | PROT_WRITE | SECURE_PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS | MAP_ALIGNED_SUPER | MAP_PREFAULT_READ, -1, 0);
                                                                                                                         ^
xmrig/src/crypto/common/VirtualMemory_unix.cpp:172:85: error: use of undeclared identifier 'MAP_ALIGNED_SUPER'
    void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_ALIGNED_SUPER | MAP_PREFAULT_READ, -1, 0);
                                                                                    ^
xmrig/src/crypto/common/VirtualMemory_unix.cpp:172:105: error: use of undeclared identifier 'MAP_PREFAULT_READ'
    void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_ALIGNED_SUPER | MAP_PREFAULT_READ, -1, 0);
                                                                                                        ^
4 errors generated.
```

I also would like to point-out that the advanced build for FreeBSD (https://xmrig.com/docs/miner/build/freebsd) uses old version of hwloc:
```
4. sh build.uv.sh && sh build.hwloc1.sh && sh build.openssl.sh && cd ../build
                                   ^
```
Should be:
`4. sh build.uv.sh && sh build.hwloc.sh && sh build.openssl.sh && cd ../build`




## SChernykh | 2022-12-17T12:22:24+00:00
More fixes in https://github.com/xmrig/xmrig/pull/3182
This should work, I've tested it in a VM. Note that you must compile without hwloc, or it will core dump at start.

## noice78 | 2022-12-17T16:18:58+00:00
It works now, thank you!
I am using hwloc 2.9.0 (latest) and I had no issues!

# Action History
- Created by: noice78 | 2022-12-16T12:47:18+00:00
- Closed at: 2023-01-04T19:27:45+00:00
