---
title: Trying to build a static executable
source_url: https://github.com/xmrig/xmrig/issues/1686
author: zn3x
assignees: []
labels:
- question
created_at: '2020-05-22T17:26:59+00:00'
updated_at: '2020-05-23T00:24:46+00:00'
type: issue
status: closed
closed_at: '2020-05-23T00:24:46+00:00'
---

# Original Description
**Describe the bug**
I'm trying to compile a static compilation under linux alpine. I have compiled all the requirements manually (hwloc, libssl...)
The issue seems to be because of `libudev` which I already have.

What I run to get this error:

```
$ cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXE_LINKER_FLAGS="-static"
-- WITH_MSR=ON
-- argon2: detecting feature 'sse2'...
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- argon2: feature 'avx512f' detected!
-- Configuring done
-- Generating done
-- Build files have been written to: /home/xmrig-5.11.1/build
```

```
$ make
[  2%] Built target xmrig-asm
[  3%] Built target argon2-avx512f
[  4%] Built target argon2-avx2
[  5%] Built target argon2-ssse3
[  6%] Built target argon2-sse2
[  7%] Built target argon2-xop
[ 11%] Built target argon2
[ 11%] Linking CXX executable xmrig
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /usr/local/lib/libhwloc.a(topology-linux.o): in function `hwloc_linux_component_instantiate':
/home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:6897: undefined reference to `udev_new'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /usr/local/lib/libhwloc.a(topology-linux.o): in function `hwloc_linux_backend_disable':
/home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:6819: undefined reference to `udev_unref'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /usr/local/lib/libhwloc.a(topology-linux.o): in function `hwloc_linuxfs_block_class_fillinfos':
/home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5711: undefined reference to `udev_device_new_from_subsystem_sysname'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5714: undefined reference to `udev_device_get_property_value'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5719: undefined reference to `udev_device_get_property_value'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5724: undefined reference to `udev_device_get_property_value'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5729: undefined reference to `udev_device_get_property_value'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5734: undefined reference to `udev_device_get_property_value'
/usr/lib/gcc/x86_64-alpine-linux-musl/9.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: /home/hwloc-hwloc-2.1.0/hwloc/topology-linux.c:5740: undefined reference to `udev_device_unref'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2892: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:116: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

Is `-ludev` flag not added?

# Discussion History
## xmrig | 2020-05-22T22:42:47+00:00
You need build hwloc without udev support https://github.com/xmrig/xmrig/blob/dev/scripts/build.hwloc.sh#L15
Thank you.

# Action History
- Created by: zn3x | 2020-05-22T17:26:59+00:00
- Closed at: 2020-05-23T00:24:46+00:00
