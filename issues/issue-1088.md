---
title: How to build monero-gui in msys2
source_url: https://github.com/monero-project/monero-gui/issues/1088
author: UsFantom
assignees: []
labels:
- resolved
created_at: '2018-01-21T04:29:41+00:00'
updated_at: '2018-12-17T11:36:28+00:00'
type: issue
status: closed
closed_at: '2018-12-17T11:36:28+00:00'
---

# Original Description
Configure error

![image](https://user-images.githubusercontent.com/35334661/35190838-395e7788-fe9e-11e7-800a-65a29c038f5a.png)

CMakeError.log file content is following:


Determining if the include file arpa/inet.h exists failed with the following output:
Change Dir: C:/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp

Run Build Command:"C:/msys32/usr/bin/make.exe" "cmTC_40c9a/fast"
make[1]: Entering directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'
/usr/bin/make -f CMakeFiles/cmTC_40c9a.dir/build.make CMakeFiles/cmTC_40c9a.dir/build
make[2]: Entering directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_40c9a.dir/CheckIncludeFile.c.obj

/C/msys32/mingw32/bin/i686-w64-mingw32-gcc.exe    -o CMakeFiles/cmTC_40c9a.dir/CheckIncludeFile.c.obj   -c /C/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp/CheckIncludeFile.c
C:/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp/CheckIncludeFile.c:1:10: fatal error: arpa/inet.h: No such file or directory

 #include <arpa/inet.h>

          ^~~~~~~~~~~~~

compilation terminated.

make[2]: *** [CMakeFiles/cmTC_40c9a.dir/build.make:66: CMakeFiles/cmTC_40c9a.dir/CheckIncludeFile.c.obj] Error 1
make[2]: Leaving directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'
make[1]: *** [Makefile:126: cmTC_40c9a/fast] Error 2
make[1]: Leaving directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'


Determining if the include file endian.h exists failed with the following output:
Change Dir: C:/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp

Run Build Command:"C:/msys32/usr/bin/make.exe" "cmTC_50040/fast"
make[1]: Entering directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'
/usr/bin/make -f CMakeFiles/cmTC_50040.dir/build.make CMakeFiles/cmTC_50040.dir/build
make[2]: Entering directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_50040.dir/CheckIncludeFile.c.obj

/C/msys32/mingw32/bin/i686-w64-mingw32-gcc.exe    -o CMakeFiles/cmTC_50040.dir/CheckIncludeFile.c.obj   -c /C/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp/CheckIncludeFile.c
C:/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp/CheckIncludeFile.c:1:10: fatal error: endian.h: No such file or directory

 #include <endian.h>

          ^~~~~~~~~~

compilation terminated.

make[2]: *** [CMakeFiles/cmTC_50040.dir/build.make:66: CMakeFiles/cmTC_50040.dir/CheckIncludeFile.c.obj] Error 1
make[2]: Leaving directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'
make[1]: *** [Makefile:126: cmTC_50040/fast] Error 2
make[1]: Leaving directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp'


Determining if the include file dlfcn.h exists failed with the following output:
Change Dir: C:/msys32/home/KiPa/moneda/build/release/CMakeFiles/CMakeTmp

Run Build Command:"C:/msys32/usr/bin/make.exe" "cmTC_f1931/fast"
make[1]: Entering directory '/home/KiPa/moneda/build/release/CMakeFiles/CMakeT

# Discussion History
## mmbyday | 2018-12-17T08:55:58+00:00
+resolved
msys2 can build monero-gui successfully. please try again with latest readme.

## erciccione | 2018-12-17T11:15:53+00:00
+resolved

# Action History
- Created by: UsFantom | 2018-01-21T04:29:41+00:00
- Closed at: 2018-12-17T11:36:28+00:00
