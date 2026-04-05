---
title: static compilation
source_url: https://github.com/xmrig/xmrig/issues/228
author: luoxk123
assignees: []
labels: []
created_at: '2017-11-28T13:32:44+00:00'
updated_at: '2018-03-14T23:30:01+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:30:01+00:00'
---

# Original Description
cmake .. -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libc.a
I get  error

CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::start(long, int)':
Workers.cpp:(.text+0x69c): undefined reference to `uv_mutex_init'
Workers.cpp:(.text+0x6a6): undefined reference to `uv_rwlock_init'
Workers.cpp:(.text+0x6c6): undefined reference to `uv_default_loop'
Workers.cpp:(.text+0x6d8): undefined reference to `uv_async_init'
Workers.cpp:(.text+0x6dd): undefined reference to `uv_default_loop'
Workers.cpp:(.text+0x6ea): undefined reference to `uv_timer_init'
Workers.cpp:(.text+0x703): undefined reference to `uv_timer_start'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::submit(JobResult const&)':
Workers.cpp:(.text+0x64a): undefined reference to `uv_async_send'
CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o: In function `Platform::init(char const*)':
Platform_unix.cpp:(.text+0x64): undefined reference to `uv_version_string'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:1084: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

how to static compilation ?

# Discussion History
## xmrig | 2017-11-28T13:35:01+00:00
Second `-DUV_LIBRARY` overrides first path to libuv.a.
Thank you.

## luoxk123 | 2017-11-28T14:29:11+00:00
how to write

## luoxk123 | 2017-11-28T14:30:42+00:00
root@ubuntu:/home/xmrigCC/build# cmake .. -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libc.a

also get the same errors

# Action History
- Created by: luoxk123 | 2017-11-28T13:32:44+00:00
- Closed at: 2018-03-14T23:30:01+00:00
