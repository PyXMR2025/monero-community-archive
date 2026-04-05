---
title: Raspberry PI 3b
source_url: https://github.com/xmrig/xmrig/issues/635
author: StrikerNZL
assignees: []
labels:
- question
- libuv
created_at: '2018-05-17T14:26:51+00:00'
updated_at: '2018-05-30T09:15:03+00:00'
type: issue
status: closed
closed_at: '2018-05-30T09:15:03+00:00'
---

# Original Description
/home/pi/xmrig/src/App.cpp: In member function ‘int App::exec()’:
/home/pi/xmrig/src/App.cpp:131:36: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
                                    ^
CMakeFiles/xmrig.dir/build.make:110: recipe for target 'CMakeFiles/xmrig.dir/src/App.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1

to me it looks like a dependency issue... tho can't figure out which it would be as i have libuv installed along with the devs for it.. 



# Discussion History
## xmrig | 2018-05-17T14:47:30+00:00
You need install libuv1 instead of libuv 0.10, if it not possible, you can compile libuv from source and in cmake phase specify path to your libuv, example:
```
cmake .. -DUV_INCLUDE_DIR=/<path/to/libuv>/include -DUV_LIBRARY=/<path/to/libuv>/.libs/libuv.a
```

## StrikerNZL | 2018-05-17T15:31:28+00:00
thanks for the help..   

# Action History
- Created by: StrikerNZL | 2018-05-17T14:26:51+00:00
- Closed at: 2018-05-30T09:15:03+00:00
