---
title: arm build problem
source_url: https://github.com/xmrig/xmrig/issues/1052
author: willwill85
assignees: []
labels:
- arm
created_at: '2019-07-04T07:40:29+00:00'
updated_at: '2019-08-02T13:08:39+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:08:39+00:00'
---

# Original Description


I use cmake cmd like this:

cmake .. -DCMAKE_C_COMPILER=/home/will/linaro-aarch64-2017.08-gcc7.1/bin/aarch64-linux-gnu-gcc -DCMAKE_CXX_COMPILER=/home/will/linaro-aarch64-2017.08-gcc7.1/bin/aarch64-linux-gnu-g++ -DCMAKE_FIND_ROOT_PATH=/home/will/linaro-aarch64-2017.08-gcc7.1/aarch64-linux-gnu -DUV_LIBRARY=/home/will/libuv_a.a -DWITH_HTTPD=OFF -DCMAKE_SYSTEM_PROCESSOR=aarch64 -DARM_TARGET=8 -DUV_INCLUDE_DIR=/home/will/libuv/include/ -DXMRIG_ARM=ON -DWITH_LIBCPUID=OFF



```

Then I got error:


[  1%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o
In file included from /home/will/xmrig/src/3rdparty/rapidjson/document.h:20:0,
                 from /home/will/xmrig/src/base/io/Json.cpp:27:
/home/will/xmrig/src/3rdparty/rapidjson/reader.h:35:10: fatal error: emmintrin.h: No such file or directory
 #include <emmintrin.h>
          ^~~~~~~~~~~~~
compilation terminated.
CMakeFiles/xmrig.dir/build.make:110: recipe for target 'CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/base/io/Json.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```


# Discussion History
## skuroedov | 2019-07-16T08:25:10+00:00
You have to allow SSE2 instructions with `-msse2`

# Action History
- Created by: willwill85 | 2019-07-04T07:40:29+00:00
- Closed at: 2019-08-02T13:08:39+00:00
