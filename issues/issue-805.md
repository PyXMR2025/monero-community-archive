---
title: Compiling on CentOS 6.10 with SCL devtoolset-7 error
source_url: https://github.com/xmrig/xmrig/issues/805
author: ratkobucic
assignees: []
labels:
- libuv
created_at: '2018-10-16T10:31:00+00:00'
updated_at: '2018-11-05T14:40:02+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:40:02+00:00'
---

# Original Description
Compiling on CentOS 6.10 with SCL devtoolset-7 which was working great before for previous versions, now reporting this error. Any idea?

```
# make
[  2%] Built target xmrig-asm
[ 12%] Built target cpuid
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
/tmp/xmrig/src/App.cpp: In member function â€int App::exec()â€™:
/tmp/xmrig/src/App.cpp:131:5: error: â€uv_loop_closeâ€™ was not declared in this scope
     uv_loop_close(uv_default_loop());
     ^~~~~~~~~~~~~
/tmp/xmrig/src/App.cpp:131:5: note: suggested alternative: â€uv_fs_closeâ€™
     uv_loop_close(uv_default_loop());
     ^~~~~~~~~~~~~
     uv_fs_close
At global scope:
cc1plus: warning: unrecognized command line option â€-Wno-class-memaccessâ€™
make[2]: *** [CMakeFiles/xmrig.dir/build.make:82: CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:65: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:76: all] Error 2
```

# Discussion History
## ratkobucic | 2018-10-16T10:33:00+00:00
Compiler version: 
- gcc version 7.3.1 20180303 (Red Hat 7.3.1-5) (GCC)
- GNU Make 4.2.1
- cmake version 2.8.12.2

## srwx666 | 2018-10-16T16:03:07+00:00
it does
https://github.com/xmrig/xmrig/issues/796#issuecomment-430295811


## ratkobucic | 2018-10-16T17:43:38+00:00
Yup... I know... have to see what is CentOS 6.10 issue ;) 
https://github.com/xmrig/xmrig/issues/796#issuecomment-430330383

## xmrig | 2018-10-19T02:27:22+00:00
You should use libuv > 1.0.0 not 0.10.xx.
Thank you.

# Action History
- Created by: ratkobucic | 2018-10-16T10:31:00+00:00
- Closed at: 2018-11-05T14:40:02+00:00
