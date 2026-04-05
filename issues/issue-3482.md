---
title: XMRig compiling error
source_url: https://github.com/xmrig/xmrig/issues/3482
author: Ixolaro
assignees: []
labels: []
created_at: '2024-05-20T15:01:47+00:00'
updated_at: '2025-06-18T22:13:16+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:13:16+00:00'
---

# Original Description
Compiling error

C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x10e9): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1125): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x11fd): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1249): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x12c8): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x12f4): more unde
fined references to `hwloc_bitmap_isset' follow
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1658): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1698): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x173c): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1780): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1794): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x180f): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1823): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1844): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x186c): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1884): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x18a9): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x18d1): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x18e9): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1911): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1929): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1957): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x196f): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.ee
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1a96): undefined
 reference to `hwloc_get_closest_objs'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1cc7): undefined
 reference to `hwloc_bitmap_alloc'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1cd5): undefined
 reference to `hwloc_bitmap_set'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x22d4): undefined
 reference to `hwloc_bitmap_free'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x262c): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x275a): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x2864): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x2908): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x2954): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x2a81): more unde
fined references to `hwloc_bitmap_isset' follow
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x32e1): undefined
 reference to `hwloc_bitmap_alloc'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x32eb): undefined
 reference to `hwloc_bitmap_alloc'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x330c): undefined
 reference to `hwloc_bitmap_set'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x33c0): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x34f2): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x3509): undefined
 reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x35d1): undefined
 reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe
: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x3829): undefined
 reference to `hwloc_bitmap_free'
collect2.exe: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:4082: xmrig.exe] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

# Discussion History
## SChernykh | 2024-05-20T16:50:05+00:00
You're missing xmrig-deps. Please follow the instructions from https://xmrig.com/docs/miner/build/windows

## FrankHB | 2024-06-03T13:28:46+00:00
MSYS2 deps from `pacman` should be enough (with `hwloc` package), and there is no ucrt64 xmrig-deps. There is something wrong in the final linker command. For `-static` build it should be `libhwloc.a libltdl.a` instead of `libhwloc.dll.a`.

## alanhasgari | 2024-08-12T13:16:13+00:00
fresh install, trying to compile the latest xmrig for my new Ryzen 5 8600G, but I keep getting undefined references for hwloc...

I am building with MSYS2 Ming64, all packages installed with pacman, all '--version' and 'which' commands check out and are verified, and I even downloaded the dependencies and extracted them properly.

Is the [https://xmrig.com/docs/miner/build/windows] guide out of date? if so, can we get that updated?

Any current solution to the undefined references for hwloc?

>
[ 15%] Linking CXX executable xmrig.exe
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x10bb): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x10f5): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1184): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x11d2): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1241): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x126b): more undefined references to `hwloc_bitmap_isset' follow
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1608): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1648): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x16f0): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1704): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x17a3): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x17b7): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x17df): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x17f7): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x181c): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1844): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x185c): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1884): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x189c): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x18c4): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x18ee): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x191f): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1954): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1a65): undefined reference to `hwloc_get_closest_objs'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1c53): undefined reference to `hwloc_bitmap_alloc'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1c60): undefined reference to `hwloc_bitmap_set'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x1eef): undefined reference to `hwloc_bitmap_free'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x2577): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x26a2): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x27b4): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x2861): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x28aa): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x29c9): more undefined references to `hwloc_bitmap_isset' follow
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x3261): undefined reference to `hwloc_bitmap_alloc'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x3269): undefined reference to `hwloc_bitmap_alloc'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x328c): undefined reference to `hwloc_bitmap_set'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x3340): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x345a): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32//../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x346c): undefined reference to `hwloc_bitmap_andnot'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x355e): undefined reference to `hwloc_bitmap_isset'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/../../../../../x86_64-w64-mingw32/bin/ld.exe: src/crypto/ghostrider/libghostrider.a(ghostrider.cpp.obj):ghostrider.cpp:(.text+0x3769): undefined reference to `hwloc_bitmap_free'
collect2.exe: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:4099: xmrig.exe] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
> 

## SChernykh | 2024-08-12T15:12:12+00:00
The build works for me if you change
```
"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
```
to
```
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
```
in the build instructions (and you install cmake in msys64 first).

## alanhasgari | 2024-08-12T15:29:58+00:00
> The build works for me if you change
> 
> ```
> "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
> ```
> 
> to
> 
> ```
> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
> ```
> 
> in the build instructions (and you install cmake in msys64 first).

Didn't work for me. Still having issues with hwloc

# Action History
- Created by: Ixolaro | 2024-05-20T15:01:47+00:00
- Closed at: 2025-06-18T22:13:16+00:00
