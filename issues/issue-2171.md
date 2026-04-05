---
title: XMRig fails to build on Alpine 3.13
source_url: https://github.com/xmrig/xmrig/issues/2171
author: bisand
assignees: []
labels:
- bug
created_at: '2021-03-11T10:49:07+00:00'
updated_at: '2021-04-12T13:23:57+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:23:57+00:00'
---

# Original Description
When following the build instructions from the documentation site, the latest version (6.10) of XMRig fails to build under on Apline Linux 3.13 (_and perhaps on other versions_).

Install latest version of Alpine Linux (3.13) and follow the steps in the XMRig documentation to reproduce the results: https://xmrig.com/docs/miner/build/alpine

**Suggested resolution**
Adding a reference to limits.h in AdlLib_linux.cpp seems to fix the problem.

```c++
...
#include <limits.h>
...
```

**Error log**
```c++
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:94:38: error: 'PATH_MAX' was not declared in this scope
   94 | static size_t sysfs_prefix(char path[PATH_MAX], const PciTopology &topology)
      |                                      ^~~~~~~~
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:94:47: error: expected ')' before ',' token
   94 | static size_t sysfs_prefix(char path[PATH_MAX], const PciTopology &topology)
      |                           ~                   ^
      |                                               )
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:94:49: error: expected unqualified-id before 'const'
   94 | static size_t sysfs_prefix(char path[PATH_MAX], const PciTopology &topology)
      |                                                 ^~~~~
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp: In static member function 'static AdlHealth xmrig::AdlLib::health(const xmrig::OclDevice&)':
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:167:22: error: 'PATH_MAX' was not declared in this scope
  167 |     static char path[PATH_MAX]{};
      |                      ^~~~~~~~
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:169:17: error: 'path' was not declared in this scope
  169 |     char *buf = path + sysfs_prefix(path, device.topology());
      |                 ^~~~
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp: At global scope:
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:94:15: warning: 'size_t xmrig::sysfs_prefix(...)' declared 'static' but never defined [-Wunused-function]
   94 | static size_t sysfs_prefix(char path[PATH_MAX], const PciTopology &topology)
      |               ^~~~~~~~~~~~
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:78:17: warning: 'uint32_t xmrig::sysfs_read(const char*, char*, const char*)' defined but not used [-Wunused-function]
   78 | static uint32_t sysfs_read(const char *path, char *buf, const char *filename)
      |                 ^~~~~~~~~~
/home/bisand/dev/xmrig/src/backend/opencl/wrappers/AdlLib_linux.cpp:58:13: warning: 'bool xmrig::sysfs_is_amdgpu(const char*, char*, const char*)' defined but not used [-Wunused-function]
   58 | static bool sysfs_is_amdgpu(const char *path, char *buf, const char *filename)
      |             ^~~~~~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1837: CMakeFiles/xmrig.dir/src/backend/opencl/wrappers/AdlLib_linux.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:155: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2
```

# Discussion History
# Action History
- Created by: bisand | 2021-03-11T10:49:07+00:00
- Closed at: 2021-04-12T13:23:57+00:00
