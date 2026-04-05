---
title: ' MSYS2 build xmrig  error'
source_url: https://github.com/xmrig/xmrig/issues/417
author: echotxl
assignees: []
labels: []
created_at: '2018-02-28T07:49:20+00:00'
updated_at: '2018-03-07T14:01:32+00:00'
type: issue
status: closed
closed_at: '2018-03-04T05:27:10+00:00'
---

# Original Description
`echo@echo-PC MINGW32 ~/xmrig/build
$ cmake .. -G "Unix Makefiles" -DUV_INCLUDE_DIR="c:\xmrig-deps-2.2\gcc\libuv\x86\include" -DUV_LIBRARY="c:\xmrig-deps-2.2\gcc\libuv\x86\lib\libuv.a" -DMHD_INCLUDE_DIR="c:\xmrig-deps-2.2\gcc\libmicrohttpd\x86\include" -DMHD_LIBRARY="c:\xmrig-deps-2.2\gcc\libmicrohttpd\x86\lib\libmicrohttpd.a"
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: F:/Program Files/MSYS2/mingw32/bin/cc.exe
-- Check for working C compiler: F:/Program Files/MSYS2/mingw32/bin/cc.exe -- broken
CMake Error at F:/Program Files/MSYS2/mingw32/share/cmake-3.10/Modules/CMakeTestCCompiler.cmake:52 (message):
  The C compiler

    "F:/Program Files/MSYS2/mingw32/bin/cc.exe"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: F:/Program Files/MSYS2/home/echo/xmrig/build/CMakeFiles/CMakeTmp

    Run Build Command:"F:/PROGRA~1/MSYS2/usr/bin/make.exe" "cmTC_ee997/fast"
    /usr/bin/make -f CMakeFiles/cmTC_ee997.dir/build.make CMakeFiles/cmTC_ee997.dir/build
    make[1]: 杩涘叆鐩綍鈥?f/Program Files/MSYS2/home/echo/xmrig/build/CMakeFiles/CMakeTmp鈥?Building C object CMakeFiles/cmTC_ee997.dir/testCCompiler.c.obj
    "F:/Program Files/MSYS2/mingw32/bin/cc.exe"    -o CMakeFiles/cmTC_ee997.dir/testCCompiler.c.obj   -c "F:/Program Files/MSYS2/home/echo/xmrig/build/CMakeFiles/CMakeTmp/testCCompiler.c"
    Linking C executable cmTC_ee997.exe
    "F:/Program Files/MSYS2/mingw32/bin/cmake.exe" -E remove -f CMakeFiles/cmTC_ee997.dir/objects.a
    "F:/Program Files/MSYS2/mingw32/bin/ar.exe" cr CMakeFiles/cmTC_ee997.dir/objects.a @CMakeFiles/cmTC_ee997.dir/objects1.rsp
    "F:/Program Files/MSYS2/mingw32/bin/cc.exe"      -Wl,--whole-archive CMakeFiles/cmTC_ee997.dir/objects.a -Wl,--no-whole-archive  -o cmTC_ee997.exe -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles/cmTC_ee997.dir/linklibs.rsp
    F:/Program Files/MSYS2/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find F:/Program: No such file or directory
    F:/Program Files/MSYS2/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find Files/MSYS2/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/lib/../lib/default-manifest.o: No such file or directory
    collect2.exe: error: ld returned 1 exit status
    make[1]: *** [CMakeFiles/cmTC_ee997.dir/build.make:101锛歝mTC_ee997.exe] 閿欒 1
    make[1]: 绂诲紑鐩綍鈥?f/Program Files/MSYS2/home/echo/xmrig/build/CMakeFiles/CMakeTmp鈥?make: *** [Makefile:126锛歝mTC_ee997/fast] 閿欒 2




  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:2 (project)


-- Configuring incomplete, errors occurred!
See also "F:/Program Files/MSYS2/home/echo/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "F:/Program Files/MSYS2/home/echo/xmrig/build/CMakeFiles/CMakeError.log".
`

# Discussion History
## echotxl | 2018-02-28T07:50:36+00:00
how to fix it ,thanks

## xmrig | 2018-02-28T10:06:17+00:00
Probably MSYS2 should be installed to path without spaces, for example `F:\MSYS2`.
Thank you.

## echotxl | 2018-03-01T08:49:39+00:00
awesome! its done,thanks
![image](https://user-images.githubusercontent.com/6007411/36835238-84e5b126-1d70-11e8-9140-0dbf54435a3a.png)


## kimats | 2018-03-07T14:01:32+00:00
@echotxl how do you install the libuv on windows?

# Action History
- Created by: echotxl | 2018-02-28T07:49:20+00:00
- Closed at: 2018-03-04T05:27:10+00:00
