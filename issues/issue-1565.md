---
title: 'Build error: uv.h: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/1565
author: yazeed44
assignees: []
labels:
- question
- libuv
created_at: '2020-02-23T10:31:08+00:00'
updated_at: '2020-08-28T16:27:02+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:27:02+00:00'
---

# Original Description
List of the commands I used:
 cmake .. -DUV_LIBRARY=/usr/lib64/libuv.a
make

xmrig/xmrig/src/base/io/Console.h:32:10: fatal error: uv.h: No such file or directory
 #include <uv.h>
          ^~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:89: CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:141: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


Trying to build within Fedora 30. I have libuv.x86_64, libuv-devel.x86_64, libuv-static.x86_64 on my machine




# Discussion History
## xmrig | 2020-02-23T23:10:52+00:00
Probably you need specify `-DUV_INCLUDE_DIR=` or not specify both options at all.
Thank you.

# Action History
- Created by: yazeed44 | 2020-02-23T10:31:08+00:00
- Closed at: 2020-08-28T16:27:02+00:00
