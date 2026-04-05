---
title: windows mingw64 compile error
source_url: https://github.com/xmrig/xmrig/issues/142
author: usoppx
assignees: []
labels:
- libuv
created_at: '2017-10-08T00:21:07+00:00'
updated_at: '2018-05-06T07:03:42+00:00'
type: issue
status: closed
closed_at: '2017-10-22T05:20:28+00:00'
---

# Original Description
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 70%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
The system cannot find the file specified.
C:\msys64\mingw64\bin\windres.exe: preprocessing failed.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:738: CMakeFiles/xmrig.dir/res/app.rc.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


file is physically there in C:\msys64\home\user\xmrig-master\res


not sure what to do. 

running commands:
user@comp MINGW64 ~/xmrig-master
$ cmake -G "Unix Makefiles" -DUV_INCLUDE_DIR="c:\<path>\gcc\libuv\x86\include" -DUV_LIBRARY="c:\<path>\gcc\libuv\x86\lib\libuv.a" -DMHD_INCLUDE_DIR="c:\<path>\gcc\libmicrohttpd\x86\include" -DMHD_LIBRARY="c:\<path>\gcc\libmicrohttpd\x86\lib\libmicrohttpd.a"

make



# Discussion History
## xmrig | 2017-10-08T10:40:20+00:00
`C:\msys64\mingw64\bin\windres.exe` file exists?
Also you can comment/remove this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L109 just lose icon and version information in exe file.
Thank you.

## usoppx | 2017-10-09T20:23:37+00:00
C:\msys64\mingw64\bin\windres.exe exists.

commenting the line allowed it to proceed further.

next one:
 fatal error: microhttpd.h: No such file or directory
 #include <microhttpd.h>

going to try cmake with -DWITH_HTTPD=OFF

**Edit; that worked.

next one:
make[2]: *** No rule to make target 'C:/<path>/gcc/libuv/x64/lib/libuv.a', needed by 'xmrig.exe'.  Stop.

Any suggestions?

what I've tried:
1: 
pacman -S mingw-w64-x86_64-libuv

2:
unzipped libuv1.x.zip to home folder
pacman -S make autoconf autogen automake python
pacman -S libtool 
cd ~/libuv1.x/
./autogen.sh
./configure
make check (error)
make install

libuv --version = command not found

Never mind got it going!!

Thank you

## ghost | 2017-11-22T12:21:02+00:00
Same issues, some ppl have a solution ?

make[2]: *** No rule to make target 'C://gcc/libuv/x64/lib/libuv.a', needed by 'xmrig.exe'. Stop.

## briancosie | 2018-05-06T07:03:42+00:00
![screenshot 10](https://user-images.githubusercontent.com/39021200/39670766-b2605a2a-5114-11e8-93ef-3a532129fa65.png)

me too having the same error

# Action History
- Created by: usoppx | 2017-10-08T00:21:07+00:00
- Closed at: 2017-10-22T05:20:28+00:00
