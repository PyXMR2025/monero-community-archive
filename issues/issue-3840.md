---
title: help? trying to build for the first time in awhile...
source_url: https://github.com/xmrig/xmrig/issues/3840
author: alanhasgari
assignees: []
labels: []
created_at: '2026-08-20T04:03:44+00:00'
updated_at: '2026-08-20T04:03:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
First time trying to build in awhile.

I have msys2, cmake, etc., installed correctly.
I got the src, deps, and went to build.

No errors until the very end:
...
[100%] Linking CXX executable xmrig.exe
C:/msys64/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/xmrig-deps/gcc/x64/lib/libuv.a(libuv_la-process.o): in function `_vsnwprintf_s_l':
C:/msys/ucrt64/include/sec_api/stdio_s.h:805:(.text+0x63b): undefined reference to `__local_stdio_printf_options'
C:/msys64/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/xmrig-deps/gcc/x64/lib/libhwloc.a(topology-xml-nolibxml.o): in function `hwloc_nolibxml_read_file':
C:/msys/home/xmrig/build/hwloc-2.12.1/hwloc/topology-xml-nolibxml.c:364:(.text+0x4dd): undefined reference to `stat64i32'
collect2.exe: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:4119: xmrig.exe] Error 1
make[1]: *** [CMakeFiles/Makefile2:213: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

I could use some help troubleshooting this, as Im not entirely familiar with the code myself.

All commands entered are from the Windows build instructions on the xmrig site.

# Discussion History
# Action History
- Created by: alanhasgari | 2026-08-20T04:03:44+00:00
