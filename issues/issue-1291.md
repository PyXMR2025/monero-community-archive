---
title: Alpine linux compilation failed
source_url: https://github.com/xmrig/xmrig/issues/1291
author: axsoftshi
assignees: []
labels:
- question
created_at: '2019-11-15T23:29:11+00:00'
updated_at: '2021-11-25T09:42:30+00:00'
type: issue
status: closed
closed_at: '2019-11-16T20:02:27+00:00'
---

# Original Description
localhost:~/xmrig/b# cmake -DCMAKE_BUILD_TYPE=Release ..
CMake Error at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:34 (include)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/b/CMakeFiles/CMakeOutput.log".


# Discussion History
## y0bagu1 | 2019-11-15T23:42:58+00:00
add -DWITH_HWLOC=OFF in cmake and it will be ok.

## axsoftshi | 2019-11-15T23:57:13+00:00
> 在cmake中添加-DWITH_HWLOC = OFF即可。
Can I compile statically in other Linux

## xmrig | 2019-11-16T07:05:54+00:00
You should install `hwloc-dev` package, in general disabling hwloc not so good idea, without it auto-configuration will be limited. Exceptions are ARM targets and some virtual machines where hwloc not much useful itself.
Thank you.

## l-we | 2019-11-18T02:52:43+00:00
install hwloc-dev
```
apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing hwloc-dev
cmake .. -DBUILD_STATIC=ON -DUV_LIBRARY=/usr/lib/libuv.so -DHWLOC_LIBRARY=/usr/lib/libhwloc.so
make
```
error
```
[100%] Linking CXX executable xmrig
/usr/lib/gcc/x86_64-alpine-linux-musl/8.3.0/../../../../x86_64-alpine-linux-musl/bin/ld: cannot find -lhwloc
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2585: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:116: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```



## BourgeoisBear | 2021-11-25T09:41:44+00:00
It builds easily enough from source--needs GNU autotools though.

https://github.com/open-mpi/hwloc

```sh
./autogen.sh
./configure
make
make install
```

# Action History
- Created by: axsoftshi | 2019-11-15T23:29:11+00:00
- Closed at: 2019-11-16T20:02:27+00:00
