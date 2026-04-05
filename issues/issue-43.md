---
title: 'error: ‘uv_loop_close’ was not declared in this scope      uv_loop_close(uv_default_loop());'
source_url: https://github.com/xmrig/xmrig/issues/43
author: Liddll
assignees: []
labels: []
created_at: '2017-07-20T08:28:52+00:00'
updated_at: '2017-07-29T04:51:22+00:00'
type: issue
status: closed
closed_at: '2017-07-29T04:51:22+00:00'
---

# Original Description
make get fail - I have no idea what is wrong :(

[  2%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/memory.c.o
[  4%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o
[  6%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/value.c.o
[  8%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/utf.c.o
[ 10%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/pack_unpack.c.o
[ 12%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/error.c.o
[ 14%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.o
[ 16%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable.c.o
[ 18%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strconv.c.o
[ 20%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strbuffer.c.o
[ 22%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/load.c.o
Linking C static library libjansson.a
[ 22%] Built target jansson
[ 24%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[ 26%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[ 28%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[ 30%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 32%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 32%] Built target cpuid
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
/root/xmrig/src/App.cpp: In member function ‘int App::exec()’:
/root/xmrig/src/App.cpp:113:5: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
     ^~~~~~~~~~~~~
/root/xmrig/src/App.cpp:113:5: note: suggested alternative: ‘uv_fs_close’
     uv_loop_close(uv_default_loop());
     ^~~~~~~~~~~~~
     uv_fs_close
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Fehler 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Fehler 2
make: *** [all] Fehler 2

# Discussion History
## jpascal | 2017-07-20T16:49:39+00:00
+1

## xmrig | 2017-07-20T16:52:08+00:00
What libuv version do you use? only version 1 supported, minimum tested version is 1.8.0.
Thank you. 

## jpascal | 2017-07-20T17:08:08+00:00
I try build version from github. And all build success!

# Action History
- Created by: Liddll | 2017-07-20T08:28:52+00:00
- Closed at: 2017-07-29T04:51:22+00:00
